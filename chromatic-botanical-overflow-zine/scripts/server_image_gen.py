#!/usr/bin/env python3
"""Generate a Chromatic Botanical Overflow Zine image through an OpenAI-compatible API."""

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
DEFAULT_TIMEOUT = 900


def die(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_config(explicit: str | None) -> tuple[Path | None, dict]:
    paths = [Path(explicit)] if explicit else []
    if os.getenv("CODEX_HOME"):
        paths.append(Path(os.environ["CODEX_HOME"]) / "config.toml")
    paths.append(Path.home() / ".codex" / "config.toml")
    for path in paths:
        if not path.exists():
            continue
        if tomllib is None:
            die("Python 3.11+ is required to read TOML configuration.")
        with path.open("rb") as handle:
            config = tomllib.load(handle)
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


def api_key(config: dict, env_name: str) -> str:
    key = os.getenv(env_name) or os.getenv("OPENAI_API_KEY")
    if key:
        return key
    configured = ((config.get("shell_environment_policy") or {}).get("set") or {})
    key = configured.get(env_name) or configured.get("OPENAI_API_KEY")
    if key:
        return str(key)
    die(f"{env_name} is not set in environment or Codex configuration.")
    return ""


def request_json(url: str, key: str, payload: dict, timeout: int) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "User-Agent": "chromatic-botanical-overflow-zine/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        die(f"Image API HTTP {exc.code}: {exc.read().decode('utf-8', errors='replace')}")
    except urllib.error.URLError as exc:
        die(f"Image API request failed: {exc.reason}")
    except (TimeoutError, socket.timeout):
        die(f"Image API timed out after {timeout} seconds.")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        die(f"Image API returned invalid JSON: {exc}")
    return {}


def outputs(path_text: str, count: int, fmt: str) -> list[Path]:
    path = Path(path_text)
    if count == 1:
        return [path]
    suffix = path.suffix or f".{fmt}"
    stem = path.stem if path.suffix else path.name
    return [path.parent / f"{stem}-{i}{suffix}" for i in range(1, count + 1)]


def build(args: argparse.Namespace, config: dict, prompt: str) -> tuple[str, dict]:
    image_model = args.image_model or os.getenv("OPENAI_IMAGE_MODEL") or DEFAULT_IMAGE_MODEL
    if args.wire_api == "responses":
        if args.n != 1:
            die("Responses image_generation supports one image per request.")
        model = args.response_model or str(config.get("model") or "gpt-5.5")
        payload = {
            "model": model,
            "input": prompt,
            "tools": [{
                "type": "image_generation",
                "model": image_model,
                "size": args.size,
                "quality": args.quality,
                "output_format": args.output_format,
            }],
        }
        if config.get("disable_response_storage"):
            payload["store"] = False
        return model, payload
    return image_model, {
        "model": image_model,
        "prompt": prompt,
        "size": args.size,
        "quality": args.quality,
        "n": args.n,
        "output_format": args.output_format,
        "response_format": "b64_json",
    }


def items(data: dict, wire_api: str) -> list[dict]:
    if wire_api == "images":
        return list(data.get("data") or [])
    return [
        {"b64_json": output["result"]}
        for output in data.get("output") or []
        if output.get("type") == "image_generation_call" and output.get("result")
    ]


def write_item(item: dict, path: Path, timeout: int, force: bool) -> None:
    if path.exists() and not force:
        die(f"Output already exists: {path} (use --force to overwrite)")
    path.parent.mkdir(parents=True, exist_ok=True)
    if item.get("b64_json"):
        path.write_bytes(base64.b64decode(item["b64_json"]))
    elif item.get("url"):
        request = urllib.request.Request(
            item["url"], headers={"User-Agent": "chromatic-botanical-overflow-zine/1.0"}
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                path.write_bytes(response.read())
        except urllib.error.URLError as exc:
            die(f"Generated image download failed: {exc.reason}")
    else:
        die("Image API response did not include b64_json or url.")
    print(f"Wrote {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file")
    parser.add_argument("--out", default="output/imagegen/spectral-type-field-zine-output.png")
    parser.add_argument("--config")
    parser.add_argument("--model-provider")
    parser.add_argument("--base-url")
    parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    parser.add_argument("--wire-api", choices=["images", "responses"])
    parser.add_argument("--response-model")
    parser.add_argument("--image-model")
    parser.add_argument("--size", default=DEFAULT_SIZE)
    parser.add_argument("--quality", default=DEFAULT_QUALITY)
    parser.add_argument("--output-format", default=DEFAULT_FORMAT)
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.n < 1 or args.n > 10:
        die("--n must be between 1 and 10.")

    config_path, config = load_config(args.config)
    providers = config.get("model_providers") or {}
    provider_name = args.model_provider or str(config.get("model_provider") or "OpenAI")
    provider = providers.get(provider_name) or {}
    base_url = args.base_url or os.getenv("OPENAI_BASE_URL") or provider.get("base_url")
    if not base_url:
        die("No OpenAI-compatible base_url found.")
    args.wire_api = args.wire_api or os.getenv("OPENAI_IMAGE_WIRE_API") or "images"
    prompt = read_prompt(args)
    model, payload = build(args, config, prompt)
    endpoint = "responses" if args.wire_api == "responses" else "images/generations"
    url = f"{str(base_url).rstrip('/')}/{endpoint}"
    paths = outputs(args.out, args.n, args.output_format)
    print(f"Provider: {provider_name}", file=sys.stderr)
    print(f"Config: {config_path or 'environment/defaults'}", file=sys.stderr)
    print(f"Endpoint: {url}", file=sys.stderr)
    print(f"Wire API: {args.wire_api}; model: {model}", file=sys.stderr)
    if args.dry_run:
        preview = dict(payload)
        field = "input" if "input" in preview else "prompt"
        preview[field] = prompt[:160] + ("..." if len(prompt) > 160 else "")
        print(json.dumps(preview, indent=2))
        return
    key = api_key(config, args.api_key_env)
    received = items(request_json(url, key, payload, args.timeout), args.wire_api)
    if len(received) < len(paths):
        die(f"Image API returned {len(received)} image(s), expected {len(paths)}.")
    for item, path in zip(received, paths):
        write_item(item, path, args.timeout, args.force)


if __name__ == "__main__":
    main()
