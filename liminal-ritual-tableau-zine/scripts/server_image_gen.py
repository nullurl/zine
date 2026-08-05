#!/usr/bin/env python3
"""Generate an image through an OpenAI-compatible Images or Responses API."""

from __future__ import annotations

import argparse
import base64
import json
import os
from pathlib import Path
import socket
import sys
import urllib.error
import urllib.request

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None  # type: ignore[assignment]


DEFAULT_IMAGE_MODEL = "gpt-image-2"
DEFAULT_SIZE = "1024x1536"
DEFAULT_QUALITY = "high"
DEFAULT_FORMAT = "png"
DEFAULT_WIRE_API = "images"
DEFAULT_TIMEOUT = 900


def die(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_toml(path: Path) -> dict:
    if not path.exists():
        return {}
    if tomllib is None:
        die("Python 3.11+ is required to read TOML configuration.")
    with path.open("rb") as handle:
        return tomllib.load(handle)


def load_config(explicit: str | None) -> tuple[Path | None, dict]:
    candidates = [Path(explicit)] if explicit else []
    if os.getenv("CODEX_HOME"):
        candidates.append(Path(os.environ["CODEX_HOME"]) / "config.toml")
    candidates.append(Path.home() / ".codex" / "config.toml")
    for path in candidates:
        config = load_toml(path)
        if config:
            return path, config
    return None, {}


def read_prompt(args: argparse.Namespace) -> str:
    if bool(args.prompt) == bool(args.prompt_file):
        die("Use exactly one of --prompt or --prompt-file.")
    if args.prompt:
        return args.prompt.strip()
    path = Path(args.prompt_file)
    if not path.exists():
        die(f"Prompt file not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def provider_settings(config: dict, explicit_name: str | None) -> tuple[str, dict]:
    name = explicit_name or str(config.get("model_provider") or "OpenAI")
    providers = config.get("model_providers") or {}
    return name, providers.get(name) or {}


def resolve_api_key(config: dict, env_name: str) -> str:
    key = os.getenv(env_name) or os.getenv("OPENAI_API_KEY")
    if key:
        return key
    configured = ((config.get("shell_environment_policy") or {}).get("set") or {})
    key = configured.get(env_name) or configured.get("OPENAI_API_KEY")
    if key:
        return str(key)
    die(f"{env_name} is not set in the environment or Codex configuration.")
    return ""


def request_json(url: str, api_key: str, payload: dict, timeout: int) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "liminal-ritual-tableau-zine/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        die(f"Image API HTTP {exc.code}: {detail}")
    except urllib.error.URLError as exc:
        die(f"Image API request failed: {exc.reason}")
    except (TimeoutError, socket.timeout):
        die(f"Image API timed out after {timeout} seconds.")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        die(f"Image API returned invalid JSON: {exc}")
    return {}


def build_payload(args: argparse.Namespace, config: dict, prompt: str) -> tuple[str, dict]:
    image_model = args.image_model or os.getenv("OPENAI_IMAGE_MODEL") or DEFAULT_IMAGE_MODEL
    if args.wire_api == "responses":
        if args.n != 1:
            die("Responses image generation supports one image per request.")
        response_model = args.response_model or str(config.get("model") or "gpt-5.5")
        payload = {
            "model": response_model,
            "input": prompt,
            "tools": [{
                "type": "image_generation",
                "model": image_model,
                "size": args.size,
                "quality": args.quality,
                "output_format": args.output_format,
            }],
        }
        if bool(config.get("disable_response_storage")):
            payload["store"] = False
        return response_model, payload
    return image_model, {
        "model": image_model,
        "prompt": prompt,
        "size": args.size,
        "quality": args.quality,
        "n": args.n,
        "output_format": args.output_format,
        "response_format": "b64_json",
    }


def extract_items(data: dict, wire_api: str) -> list[dict]:
    if wire_api == "images":
        return list(data.get("data") or [])
    items: list[dict] = []
    for output in data.get("output") or []:
        if output.get("type") == "image_generation_call" and output.get("result"):
            items.append({"b64_json": output["result"]})
    return items


def output_paths(out: str, count: int, output_format: str) -> list[Path]:
    path = Path(out)
    if count == 1:
        return [path]
    suffix = path.suffix or f".{output_format}"
    stem = path.stem if path.suffix else path.name
    return [path.parent / f"{stem}-{index}{suffix}" for index in range(1, count + 1)]


def write_item(item: dict, path: Path, timeout: int, force: bool) -> None:
    if path.exists() and not force:
        die(f"Output already exists: {path} (use --force to overwrite)")
    path.parent.mkdir(parents=True, exist_ok=True)
    if item.get("b64_json"):
        path.write_bytes(base64.b64decode(item["b64_json"]))
    elif item.get("url"):
        request = urllib.request.Request(
            item["url"], headers={"User-Agent": "liminal-ritual-tableau-zine/1.0"}
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                path.write_bytes(response.read())
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            die(f"Generated image download HTTP {exc.code}: {detail}")
        except urllib.error.URLError as exc:
            die(f"Generated image download failed: {exc.reason}")
        except (TimeoutError, socket.timeout):
            die(f"Generated image download timed out after {timeout} seconds.")
    else:
        die("Image API response did not include b64_json or url.")
    print(f"Wrote {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file")
    parser.add_argument(
        "--out", default="output/imagegen/liminal-ritual-tableau-zine-output.png"
    )
    parser.add_argument("--config")
    parser.add_argument("--model-provider")
    parser.add_argument("--base-url")
    parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    parser.add_argument("--wire-api", choices=["responses", "images"])
    parser.add_argument("--response-model")
    parser.add_argument("--image-model")
    parser.add_argument("--size", default=DEFAULT_SIZE)
    parser.add_argument("--quality", default=DEFAULT_QUALITY)
    parser.add_argument("--output-format", default=DEFAULT_FORMAT)
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.n < 1 or args.n > 10:
        die("--n must be between 1 and 10.")

    config_path, config = load_config(args.config)
    provider_name, provider = provider_settings(config, args.model_provider)
    base_url = args.base_url or os.getenv("OPENAI_BASE_URL") or provider.get("base_url")
    if not base_url:
        die("No OpenAI-compatible base_url found.")

    args.wire_api = args.wire_api or os.getenv("OPENAI_IMAGE_WIRE_API") or DEFAULT_WIRE_API
    prompt = read_prompt(args)
    selected_model, payload = build_payload(args, config, prompt)
    endpoint = "responses" if args.wire_api == "responses" else "images/generations"
    url = f"{str(base_url).rstrip('/')}/{endpoint}"
    outputs = output_paths(args.out, args.n, args.output_format)

    print(f"Provider: {provider_name}", file=sys.stderr)
    print(f"Config: {config_path or 'environment/defaults'}", file=sys.stderr)
    print(f"Endpoint: {url}", file=sys.stderr)
    print(f"Wire API: {args.wire_api}", file=sys.stderr)
    print(f"Selected model: {selected_model}", file=sys.stderr)
    print(f"Outputs: {', '.join(str(path) for path in outputs)}", file=sys.stderr)

    if args.dry_run:
        preview = dict(payload)
        field = "input" if "input" in preview else "prompt"
        preview[field] = prompt[:160] + ("..." if len(prompt) > 160 else "")
        print(json.dumps(preview, indent=2))
        return

    api_key = resolve_api_key(config, args.api_key_env)
    data = request_json(url, api_key, payload, args.timeout)
    items = extract_items(data, args.wire_api)
    if not items:
        die("Image API response contained no image items.")
    if len(items) < len(outputs):
        die(f"Image API returned {len(items)} image(s), expected {len(outputs)}.")
    for item, path in zip(items, outputs):
        write_item(item, path, args.timeout, args.force)


if __name__ == "__main__":
    main()
