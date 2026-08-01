#!/usr/bin/env python3
"""Direct OpenAI-compatible image generation fallback for this skill.

This avoids the bundled imagegen CLI and the OpenAI SDK. It reads the user's
Codex provider configuration, calls either /v1/responses with the
image_generation tool or /v1/images/generations with urllib, and writes the
returned PNG/WebP/JPEG bytes to disk.
"""

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
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 only
    tomllib = None  # type: ignore[assignment]


DEFAULT_IMAGE_MODEL = "gpt-image-2"
DEFAULT_SIZE = "1024x1536"
DEFAULT_QUALITY = "high"
DEFAULT_OUTPUT_FORMAT = "png"
DEFAULT_WIRE_API = "images"
DEFAULT_TIMEOUT = 900


def die(message: str, code: int = 1) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(code)


def load_toml(path: Path) -> dict:
    if not path.exists():
        return {}
    if tomllib is None:
        die("Python 3.11+ is required to read TOML config without extra dependencies.")
    with path.open("rb") as fh:
        return tomllib.load(fh)


def default_config_paths() -> list[Path]:
    paths: list[Path] = []
    codex_home = os.getenv("CODEX_HOME")
    if codex_home:
        paths.append(Path(codex_home) / "config.toml")
    paths.append(Path.home() / ".codex" / "config.toml")
    return paths


def first_existing_config(explicit: str | None) -> tuple[Path | None, dict]:
    candidates = [Path(explicit)] if explicit else default_config_paths()
    for path in candidates:
        data = load_toml(path)
        if data:
            return path, data
    return None, {}


def resolve_provider(config: dict, provider_name: str | None) -> tuple[str, dict]:
    name = provider_name or str(config.get("model_provider") or "OpenAI")
    providers = config.get("model_providers") or {}
    provider = providers.get(name) or providers.get(str(name)) or {}
    return name, provider


def resolve_api_key(config: dict, env_name: str) -> str:
    key = os.getenv(env_name) or os.getenv("OPENAI_API_KEY")
    if key:
        return key
    shell_env = ((config.get("shell_environment_policy") or {}).get("set") or {})
    key = shell_env.get(env_name) or shell_env.get("OPENAI_API_KEY")
    if key:
        return str(key)
    die(f"{env_name} is not set in environment or Codex config.")
    return ""


def read_prompt(args: argparse.Namespace) -> str:
    if bool(args.prompt) == bool(args.prompt_file):
        die("Use exactly one of --prompt or --prompt-file.")
    if args.prompt:
        return args.prompt.strip()
    prompt_path = Path(args.prompt_file)
    if not prompt_path.exists():
        die(f"Prompt file not found: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8").strip()


def output_paths(out: str, count: int, output_format: str) -> list[Path]:
    path = Path(out)
    if count == 1:
        return [path]
    suffix = path.suffix or f".{output_format}"
    stem = path.stem if path.suffix else path.name
    parent = path.parent
    return [parent / f"{stem}-{idx}{suffix}" for idx in range(1, count + 1)]


def request_json(url: str, api_key: str, payload: dict, timeout: int) -> dict:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        die(f"Image API HTTP {exc.code}: {detail}")
    except urllib.error.URLError as exc:
        die(f"Image API request failed: {exc.reason}")
    except (TimeoutError, socket.timeout):
        die(
            f"Image API timed out after {timeout} seconds. "
            "The server accepted the request but did not return an image in time."
        )
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        die(f"Image API returned invalid JSON: {exc}")
    return {}


def write_image(
    item: dict,
    out_path: Path,
    timeout: int,
    force: bool,
) -> None:
    if out_path.exists() and not force:
        die(f"Output already exists: {out_path} (use --force to overwrite)")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if item.get("b64_json"):
        out_path.write_bytes(base64.b64decode(item["b64_json"]))
        print(f"Wrote {out_path}")
        return

    if item.get("url"):
        image_request = urllib.request.Request(
            item["url"], headers={"User-Agent": "textile-swatch-zine/1.0"}
        )
        try:
            with urllib.request.urlopen(image_request, timeout=timeout) as response:
                out_path.write_bytes(response.read())
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            die(f"Generated image download failed with HTTP {exc.code}: {detail}")
        except urllib.error.URLError as exc:
            die(f"Generated image download failed: {exc.reason}")
        except (TimeoutError, socket.timeout):
            die(f"Generated image download timed out after {timeout} seconds.")
        print(f"Wrote {out_path}")
        return

    die("Image API response did not include b64_json or url.")


def build_payload(args: argparse.Namespace, config: dict, prompt: str) -> tuple[str, dict]:
    response_model = args.response_model or str(config.get("model") or "gpt-5.5")
    image_model = args.image_model or os.getenv("OPENAI_IMAGE_MODEL") or DEFAULT_IMAGE_MODEL

    if args.wire_api == "responses":
        if args.n != 1:
            die("Responses image_generation fallback currently supports one image per request.")
        tool = {
            "type": "image_generation",
            "model": image_model,
            "size": args.size,
            "quality": args.quality,
            "output_format": args.output_format,
        }
        payload = {
            "model": response_model,
            "input": prompt,
            "tools": [tool],
        }
        if bool(config.get("disable_response_storage")):
            payload["store"] = False
        return response_model, payload

    payload = {
        "model": image_model,
        "prompt": prompt,
        "size": args.size,
        "quality": args.quality,
        "n": args.n,
        "output_format": args.output_format,
        "response_format": "b64_json",
    }
    return image_model, payload


def extract_image_items(data: dict, wire_api: str) -> list[dict]:
    if wire_api == "images":
        return list(data.get("data") or [])

    items: list[dict] = []
    for item in data.get("output") or []:
        if item.get("type") == "image_generation_call" and item.get("result"):
            items.append({"b64_json": item["result"]})
    return items


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file")
    parser.add_argument(
        "--out", default="output/imagegen/textile-swatch-zine-output.png"
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
    parser.add_argument("--output-format", default=DEFAULT_OUTPUT_FORMAT)
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.n < 1 or args.n > 10:
        die("--n must be between 1 and 10.")

    config_path, config = first_existing_config(args.config)
    provider_name, provider = resolve_provider(config, args.model_provider)
    base_url = args.base_url or os.getenv("OPENAI_BASE_URL") or provider.get("base_url")
    if not base_url:
        die("No OpenAI-compatible base_url found. Pass --base-url or configure model_providers.")
    api_key = resolve_api_key(config, args.api_key_env)
    prompt = read_prompt(args)
    # The provider's wire_api config describes the text model transport. Image
    # generation is a separate API and must not inherit `responses` from it.
    args.wire_api = (
        args.wire_api
        or os.getenv("OPENAI_IMAGE_WIRE_API")
        or DEFAULT_WIRE_API
    )
    selected_model, payload = build_payload(args, config, prompt)
    endpoint = "responses" if args.wire_api == "responses" else "images/generations"
    url = f"{str(base_url).rstrip('/')}/{endpoint}"
    outputs = output_paths(args.out, args.n, args.output_format)

    print(f"Provider: {provider_name}", file=sys.stderr)
    print(f"Config: {config_path or 'environment/defaults'}", file=sys.stderr)
    print(f"Endpoint: {url}", file=sys.stderr)
    print(f"Wire API: {args.wire_api}", file=sys.stderr)
    print(f"Selected model: {selected_model}", file=sys.stderr)
    if args.wire_api == "responses":
        print(f"Image tool model: {payload['tools'][0]['model']}", file=sys.stderr)
    print(f"Outputs: {', '.join(str(p) for p in outputs)}", file=sys.stderr)

    if args.dry_run:
        redacted = dict(payload)
        if "input" in redacted:
            redacted["input"] = prompt[:160] + ("..." if len(prompt) > 160 else "")
        if "prompt" in redacted:
            redacted["prompt"] = prompt[:160] + ("..." if len(prompt) > 160 else "")
        print(json.dumps(redacted, indent=2))
        return

    data = request_json(url, api_key, payload, args.timeout)
    items = extract_image_items(data, args.wire_api)
    if not items:
        die("Image API response contained no data items.")
    for item, out_path in zip(items, outputs):
        write_image(item, out_path, args.timeout, args.force)


if __name__ == "__main__":
    main()
