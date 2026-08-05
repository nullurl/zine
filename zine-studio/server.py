#!/usr/bin/env python3
"""Local Skill-driven image generation studio."""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
from pathlib import Path
import re
import socket
import threading
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None  # type: ignore[assignment]


APP_ROOT = Path(__file__).resolve().parent
WORKSPACE_ROOT = APP_ROOT.parent
STATIC_ROOT = APP_ROOT / "static"
OUTPUT_ROOT = APP_ROOT / "output"
MAX_REQUEST_BYTES = 28 * 1024 * 1024
MAX_IMAGE_BYTES = 8 * 1024 * 1024
MAX_IMAGES = 3
API_TIMEOUT = 900

JOBS: dict[str, dict[str, Any]] = {}
JOBS_LOCK = threading.Lock()
SKILLS: dict[str, dict[str, Any]] = {}


class ApiError(RuntimeError):
    pass


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def compact_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def parse_frontmatter(path: Path) -> tuple[str, str]:
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return "", ""
    if not lines or lines[0].strip() != "---":
        return "", ""

    name = ""
    description = ""
    index = 1
    while index < len(lines):
        line = lines[index]
        if line.strip() == "---":
            break
        if line.startswith("name:"):
            name = line.partition(":")[2].strip().strip('"\'')
        elif line.startswith("description:"):
            value = line.partition(":")[2].strip()
            if value in {">", ">-", "|", "|-"}:
                parts: list[str] = []
                index += 1
                while index < len(lines) and (lines[index].startswith(" ") or not lines[index].strip()):
                    if lines[index].strip():
                        parts.append(lines[index].strip())
                    index += 1
                description = " ".join(parts)
                continue
            description = value.strip('"\'')
        index += 1
    return name, compact_whitespace(description)


def skill_roots() -> list[tuple[str, Path]]:
    home = Path.home()
    codex_home = Path(os.getenv("CODEX_HOME") or home / ".codex")
    roots = [
        ("workspace", WORKSPACE_ROOT),
        ("installed", codex_home / "skills"),
        ("installed", home / ".codex" / "skills"),
        ("agent", home / ".agents" / "skills"),
        ("plugin", home / ".codex" / "plugins" / "cache"),
    ]
    seen: set[Path] = set()
    unique: list[tuple[str, Path]] = []
    for group, root in roots:
        resolved = root.expanduser().resolve()
        if resolved not in seen and resolved.exists():
            seen.add(resolved)
            unique.append((group, resolved))
    return unique


def visual_skill(name: str, description: str) -> bool:
    text = f"{name} {description}".lower()
    visual_tokens = (
        "image", "poster", "zine", "photo", "visual", "sticker", "banner",
        "tattoo", "illustration", "摄影", "海报", "图像", "视觉", "贴纸", "生图",
    )
    return any(token in text for token in visual_tokens)


def skill_category(name: str, description: str, group: str) -> str:
    if group in {"plugin", "agent"} or name in {
        "skill-creator", "skill-installer", "plugin-creator", "openai-docs",
        "review-agent", "computer-use",
    }:
        return "system"
    text = f"{name} {description}".lower()
    if visual_skill(name, description):
        return "visual"
    if any(token in text for token in ("document", "pdf", "spreadsheet", "excel", "presentation", "ppt")):
        return "productivity"
    return "development"


def scan_skills() -> dict[str, dict[str, Any]]:
    found: dict[str, dict[str, Any]] = {}
    for group, root in skill_roots():
        candidates = root.glob("*/SKILL.md") if group == "workspace" else root.rglob("SKILL.md")
        for path in sorted(candidates):
            name, description = parse_frontmatter(path)
            if not name or name in found:
                continue
            found[name] = {
                "name": name,
                "description": description or "No description provided.",
                "category": skill_category(name, description, group),
                "source": group,
                "visual": visual_skill(name, description),
                "path": str(path),
            }
    return found


def public_skill(skill: dict[str, Any]) -> dict[str, Any]:
    return {key: skill[key] for key in ("name", "description", "category", "source", "visual")}


def config_paths() -> list[Path]:
    home = Path.home()
    paths: list[Path] = []
    if os.getenv("CODEX_HOME"):
        paths.append(Path(os.environ["CODEX_HOME"]) / "config.toml")
    paths.extend([
        home / "Library" / "Application Support" / "Cindy" / "codex-home" / "config.toml",
        home / ".codex" / "config.toml",
    ])
    unique: list[Path] = []
    for path in paths:
        if path not in unique:
            unique.append(path)
    return unique


def load_config() -> tuple[Path | None, dict[str, Any]]:
    if tomllib is None:
        return None, {}
    for path in config_paths():
        if not path.exists():
            continue
        try:
            with path.open("rb") as handle:
                config = tomllib.load(handle)
            if config:
                return path, config
        except (OSError, tomllib.TOMLDecodeError):
            continue
    return None, {}


def provider_settings() -> dict[str, Any]:
    config_path, config = load_config()
    provider_name = str(config.get("model_provider") or "OpenAI")
    provider = (config.get("model_providers") or {}).get(provider_name) or {}
    base_url = os.getenv("OPENAI_BASE_URL") or provider.get("base_url")
    configured_env = ((config.get("shell_environment_policy") or {}).get("set") or {})
    api_key = os.getenv("OPENAI_API_KEY") or configured_env.get("OPENAI_API_KEY")
    return {
        "provider": provider_name,
        "base_url": str(base_url or "").rstrip("/"),
        "api_key": str(api_key or ""),
        "response_model": os.getenv("OPENAI_RESPONSE_MODEL") or str(config.get("model") or "gpt-5.5"),
        "image_model": os.getenv("OPENAI_IMAGE_MODEL") or "gpt-image-2",
        "config_path": str(config_path) if config_path else "",
    }


def request_json(url: str, api_key: str, payload: dict[str, Any], timeout: int = API_TIMEOUT) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "zine-studio/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise ApiError(f"Image service returned HTTP {exc.code}: {detail[:700]}") from exc
    except urllib.error.URLError as exc:
        raise ApiError(f"Image service connection failed: {exc.reason}") from exc
    except (TimeoutError, socket.timeout) as exc:
        raise ApiError(f"Image service timed out after {timeout} seconds") from exc
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ApiError("Image service returned invalid JSON") from exc


def validate_images(raw_images: Any) -> list[dict[str, str]]:
    if raw_images is None:
        return []
    if not isinstance(raw_images, list) or len(raw_images) > MAX_IMAGES:
        raise ApiError(f"Upload up to {MAX_IMAGES} reference images")
    images: list[dict[str, str]] = []
    total = 0
    for raw in raw_images:
        if not isinstance(raw, dict):
            raise ApiError("Invalid reference image payload")
        name = str(raw.get("name") or "reference")[:120]
        data_url = str(raw.get("data") or "")
        match = re.fullmatch(r"data:(image/(?:png|jpeg|webp));base64,([A-Za-z0-9+/=\r\n]+)", data_url)
        if not match:
            raise ApiError(f"Unsupported reference image: {name}")
        try:
            decoded_size = len(base64.b64decode(match.group(2), validate=True))
        except ValueError as exc:
            raise ApiError(f"Invalid image encoding: {name}") from exc
        if decoded_size > MAX_IMAGE_BYTES:
            raise ApiError(f"Reference image is too large: {name}")
        total += decoded_size
        if total > MAX_REQUEST_BYTES:
            raise ApiError("Combined reference images are too large")
        images.append({"name": name, "data": data_url})
    return images


def skill_context(skill: dict[str, Any]) -> str:
    path = Path(skill["path"])
    skill_text = path.read_text(encoding="utf-8", errors="replace")[:28_000]
    recipe_path = path.parent / "references" / "prompt-recipes.md"
    recipe_text = ""
    if recipe_path.exists():
        recipe_text = recipe_path.read_text(encoding="utf-8", errors="replace")[:12_000]
    context = f"SELECTED SKILL:\n{skill_text}"
    if recipe_text:
        context += f"\n\nOPTIONAL PROMPT RECIPES:\n{recipe_text}"
    return context


def build_instruction(skill: dict[str, Any], brief: str, size: str, quality: str, image_count: int) -> str:
    reference_note = (
        f"The user uploaded {image_count} reference image(s). Analyze them as reference material for subject, "
        "palette, composition, and texture. Preserve requested invariants, but do not copy visible signatures, "
        "watermarks, private text, or identifiable people."
        if image_count else
        "No reference images were uploaded. Build the image from the brief and Skill instructions."
    )
    return f"""You are executing a user-selected image-generation Skill inside a local studio.

Apply the Skill's visual grammar and workflow to the user's brief. Resolve open creative details conservatively. Create exactly one finished raster image. You must invoke the image_generation tool. After the tool call, return a compact final image prompt prefixed with FINAL_PROMPT:. Do not explain the Skill.

USER BRIEF:
{brief}

OUTPUT:
- size: {size}
- quality: {quality}
- one final image
- {reference_note}

{skill_context(skill)}
"""


def response_content(instruction: str, images: list[dict[str, str]]) -> list[dict[str, Any]]:
    content: list[dict[str, Any]] = [{"type": "input_text", "text": instruction}]
    for image in images:
        content.append({"type": "input_image", "image_url": image["data"], "detail": "high"})
    return content


def extract_output_text(data: dict[str, Any]) -> str:
    parts: list[str] = []
    for output in data.get("output") or []:
        if output.get("type") != "message":
            continue
        for content in output.get("content") or []:
            text = content.get("text")
            if content.get("type") in {"output_text", "text"} and text:
                parts.append(str(text))
    return "\n".join(parts).strip()


def extract_image(data: dict[str, Any]) -> bytes | None:
    for output in data.get("output") or []:
        if output.get("type") == "image_generation_call" and output.get("result"):
            try:
                return base64.b64decode(output["result"])
            except ValueError:
                continue
    return None


def generate_with_images_api(prompt: str, settings: dict[str, Any], size: str, quality: str) -> bytes:
    payload = {
        "model": settings["image_model"],
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "n": 1,
        "output_format": "png",
        "response_format": "b64_json",
    }
    data = request_json(f"{settings['base_url']}/images/generations", settings["api_key"], payload)
    items = data.get("data") or []
    if not items:
        raise ApiError("Image service did not return an image")
    item = items[0]
    if item.get("b64_json"):
        return base64.b64decode(item["b64_json"])
    if item.get("url"):
        try:
            with urllib.request.urlopen(item["url"], timeout=API_TIMEOUT) as response:
                return response.read()
        except urllib.error.URLError as exc:
            raise ApiError(f"Generated image download failed: {exc.reason}") from exc
    raise ApiError("Image response contained no data")


def execute_generation(skill: dict[str, Any], brief: str, images: list[dict[str, str]], size: str, quality: str) -> tuple[bytes, str]:
    settings = provider_settings()
    if not settings["base_url"]:
        raise ApiError("No OpenAI-compatible base URL is configured")
    if not settings["api_key"]:
        raise ApiError("OPENAI_API_KEY is not configured on the server")

    instruction = build_instruction(skill, brief, size, quality, len(images))
    payload = {
        "model": settings["response_model"],
        "input": [{"role": "user", "content": response_content(instruction, images)}],
        "tools": [{
            "type": "image_generation",
            "model": settings["image_model"],
            "size": size,
            "quality": quality,
            "output_format": "png",
        }],
        "store": False,
    }

    response_error: ApiError | None = None
    try:
        data = request_json(f"{settings['base_url']}/responses", settings["api_key"], payload)
        image_bytes = extract_image(data)
        output_text = extract_output_text(data)
        if image_bytes:
            final_prompt = output_text.removeprefix("FINAL_PROMPT:").strip() or brief
            return image_bytes, final_prompt
        if output_text:
            fallback_prompt = output_text.removeprefix("FINAL_PROMPT:").strip()
            return generate_with_images_api(fallback_prompt, settings, size, quality), fallback_prompt
        response_error = ApiError("Responses API completed without image or prompt output")
    except ApiError as exc:
        response_error = exc

    if images:
        compile_payload = {
            "model": settings["response_model"],
            "input": [{"role": "user", "content": response_content(
                instruction.replace(
                    "You must invoke the image_generation tool. After the tool call, return a compact final image prompt prefixed with FINAL_PROMPT:.",
                    "Return only one compact production-ready image prompt. Do not call tools or explain your reasoning."
                ),
                images,
            )}],
            "store": False,
        }
        try:
            compiled = request_json(f"{settings['base_url']}/responses", settings["api_key"], compile_payload)
            fallback_prompt = extract_output_text(compiled).strip()
            if fallback_prompt:
                return generate_with_images_api(fallback_prompt, settings, size, quality), fallback_prompt
        except ApiError:
            pass
        raise response_error or ApiError("Reference-image generation failed")

    direct_prompt = (
        f"Apply the visual identity of {skill['name']}: {skill['description']}\n\n"
        f"User brief: {brief}\n\nCreate one finished image. Follow the requested text and attribution exactly."
    )
    try:
        return generate_with_images_api(direct_prompt, settings, size, quality), direct_prompt
    except ApiError:
        raise response_error or ApiError("Generation failed")


def update_job(job_id: str, **changes: Any) -> bool:
    with JOBS_LOCK:
        job = JOBS.get(job_id)
        if not job:
            return False
        if job.get("status") == "cancelled" and changes.get("status") != "cancelled":
            return False
        job.update(changes)
        job["updated_at"] = now_iso()
        return True


def write_metadata(job: dict[str, Any]) -> None:
    metadata = {key: value for key, value in job.items() if key not in {"images"}}
    (OUTPUT_ROOT / f"{job['id']}.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def generation_worker(job_id: str) -> None:
    with JOBS_LOCK:
        job = dict(JOBS[job_id])
    try:
        update_job(job_id, status="running", progress=18, message="Compiling Skill and references")
        skill = SKILLS[job["skill"]]
        image_bytes, final_prompt = execute_generation(
            skill, job["brief"], job["images"], job["size"], job["quality"]
        )
        with JOBS_LOCK:
            if JOBS[job_id].get("status") == "cancelled":
                return
        update_job(job_id, progress=88, message="Saving generated image")
        OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
        image_path = OUTPUT_ROOT / f"{job_id}.png"
        prompt_path = OUTPUT_ROOT / f"{job_id}.txt"
        image_path.write_bytes(image_bytes)
        prompt_path.write_text(final_prompt, encoding="utf-8")
        update_job(
            job_id,
            status="completed",
            progress=100,
            message="Completed",
            result_url=f"/api/files/{job_id}.png",
            prompt_url=f"/api/files/{job_id}.txt",
            reference_count=len(job["images"]),
        )
        with JOBS_LOCK:
            write_metadata(JOBS[job_id])
    except Exception as exc:  # noqa: BLE001
        traceback.print_exc()
        update_job(job_id, status="failed", progress=100, message="Generation failed", error=str(exc))
        with JOBS_LOCK:
            if job_id in JOBS:
                write_metadata(JOBS[job_id])


def create_job(payload: dict[str, Any]) -> dict[str, Any]:
    skill_name = str(payload.get("skill") or "")
    if skill_name not in SKILLS:
        raise ApiError("Select a valid Skill")
    brief = str(payload.get("brief") or "").strip()
    if not brief:
        raise ApiError("Enter a generation brief")
    if len(brief) > 5_000:
        raise ApiError("Generation brief is too long")
    images = validate_images(payload.get("images"))
    size = str(payload.get("size") or "1024x1536")
    if size not in {"1024x1536", "1024x1024", "1536x1024"}:
        raise ApiError("Unsupported image size")
    quality = str(payload.get("quality") or "high")
    if quality not in {"medium", "high"}:
        raise ApiError("Unsupported image quality")

    job_id = uuid.uuid4().hex[:16]
    job = {
        "id": job_id,
        "skill": skill_name,
        "brief": brief,
        "size": size,
        "quality": quality,
        "images": images,
        "reference_count": len(images),
        "status": "queued",
        "progress": 5,
        "message": "Queued",
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    with JOBS_LOCK:
        JOBS[job_id] = job
    thread = threading.Thread(target=generation_worker, args=(job_id,), daemon=True)
    thread.start()
    return {key: value for key, value in job.items() if key != "images"}


def job_public(job: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in job.items() if key != "images"}


def history_items() -> list[dict[str, Any]]:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    items: list[dict[str, Any]] = []
    for path in sorted(OUTPUT_ROOT.glob("*.json"), key=lambda item: item.stat().st_mtime, reverse=True)[:30]:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if data.get("status") == "completed" and data.get("result_url"):
            items.append(data)
    return items


class StudioHandler(BaseHTTPRequestHandler):
    server_version = "ZineStudio/1.0"

    def log_message(self, format_string: str, *args: Any) -> None:
        print(f"[{self.log_date_time_string()}] {format_string % args}")

    def send_json(self, payload: Any, status: int = 200) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def send_file(self, path: Path, cache: bool = False) -> None:
        if not path.exists() or not path.is_file():
            self.send_error(404)
            return
        data = path.read_bytes()
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "public, max-age=3600" if cache else "no-store")
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
            self.send_header("Content-Disposition", f'inline; filename="{path.name}"')
        self.end_headers()
        self.wfile.write(data)

    def read_json(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length") or 0)
        if length <= 0 or length > MAX_REQUEST_BYTES:
            raise ApiError("Invalid request size")
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ApiError("Invalid JSON request") from exc
        if not isinstance(payload, dict):
            raise ApiError("Invalid request body")
        return payload

    def do_GET(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(parsed.path)
        if path == "/api/health":
            settings = provider_settings()
            self.send_json({
                "ok": True,
                "skills": len(SKILLS),
                "provider": settings["provider"],
                "response_model": settings["response_model"],
                "image_model": settings["image_model"],
                "configured": bool(settings["base_url"] and settings["api_key"]),
            })
            return
        if path == "/api/skills":
            skills = sorted((public_skill(skill) for skill in SKILLS.values()), key=lambda item: item["name"])
            self.send_json({"skills": skills})
            return
        if path == "/api/history":
            self.send_json({"items": history_items()})
            return
        if path.startswith("/api/jobs/"):
            job_id = path.rsplit("/", 1)[-1]
            with JOBS_LOCK:
                job = JOBS.get(job_id)
                payload = job_public(job) if job else None
            if payload is None:
                self.send_json({"error": "Job not found"}, 404)
            else:
                self.send_json(payload)
            return
        if path.startswith("/api/files/"):
            filename = Path(path.rsplit("/", 1)[-1]).name
            if not re.fullmatch(r"[a-f0-9]{16}\.(?:png|txt|json)", filename):
                self.send_error(404)
                return
            self.send_file(OUTPUT_ROOT / filename, cache=True)
            return

        static_path = "index.html" if path == "/" else path.lstrip("/")
        target = (STATIC_ROOT / static_path).resolve()
        try:
            target.relative_to(STATIC_ROOT.resolve())
        except ValueError:
            self.send_error(404)
            return
        self.send_file(target)

    def do_POST(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(parsed.path)
        try:
            if path == "/api/generate":
                job = create_job(self.read_json())
                self.send_json(job, 202)
                return
            if path.startswith("/api/jobs/") and path.endswith("/cancel"):
                job_id = path.split("/")[-2]
                updated = update_job(job_id, status="cancelled", progress=100, message="Cancelled")
                if not updated:
                    self.send_json({"error": "Job not found"}, 404)
                else:
                    self.send_json({"id": job_id, "status": "cancelled"})
                return
            self.send_json({"error": "Not found"}, 404)
        except ApiError as exc:
            self.send_json({"error": str(exc)}, 400)
        except Exception as exc:  # noqa: BLE001
            traceback.print_exc()
            self.send_json({"error": f"Server error: {exc}"}, 500)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8791)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    global SKILLS
    SKILLS = scan_skills()
    settings = provider_settings()
    if args.check:
        print(json.dumps({
            "skills": len(SKILLS),
            "visual_skills": sum(1 for skill in SKILLS.values() if skill["visual"]),
            "provider": settings["provider"],
            "response_model": settings["response_model"],
            "image_model": settings["image_model"],
            "configured": bool(settings["base_url"] and settings["api_key"]),
        }, ensure_ascii=False, indent=2))
        return

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer((args.host, args.port), StudioHandler)
    print(f"Zine Studio: http://{args.host}:{args.port}")
    print(f"Skills: {len(SKILLS)}; provider: {settings['provider']}; image model: {settings['image_model']}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
