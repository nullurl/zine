#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT="$SCRIPT_DIR/build/StickerDesk.app"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --output)
      [[ $# -ge 2 ]] || { echo "missing value for --output" >&2; exit 2; }
      OUTPUT="$2"
      shift 2
      ;;
    *)
      echo "unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

case "$OUTPUT" in
  ""|"/"|"."|"..")
    echo "unsafe output path" >&2
    exit 2
    ;;
esac

if [[ -e "$OUTPUT" || -L "$OUTPUT" ]]; then
  echo "output already exists: $OUTPUT" >&2
  exit 2
fi

OUTPUT_PARENT="$(dirname "$OUTPUT")"
mkdir -p "$OUTPUT_PARENT"
BUILD_ROOT="$(mktemp -d "$OUTPUT_PARENT/.stickerdesk-build.XXXXXX")"
trap '/bin/rm -rf -- "$BUILD_ROOT"' EXIT

APP="$BUILD_ROOT/StickerDesk.app"
mkdir -p "$APP/Contents/MacOS"
cp "$SCRIPT_DIR/Info.plist" "$APP/Contents/Info.plist"

SWIFTC="$(xcrun --find swiftc)"
SDKROOT="$(xcrun --sdk macosx --show-sdk-path)"
MODULE_CACHE="$BUILD_ROOT/ModuleCache"
mkdir -p "$MODULE_CACHE"
"$SWIFTC" \
  -sdk "$SDKROOT" \
  -module-cache-path "$MODULE_CACHE" \
  -swift-version 5 \
  -O \
  -framework AppKit \
  -framework CoreGraphics \
  "$SCRIPT_DIR/Sources/StickerDesk/main.swift" \
  -o "$APP/Contents/MacOS/StickerDesk"

if command -v codesign >/dev/null 2>&1; then
  codesign --force --deep --sign - "$APP" >/dev/null
fi

mv "$APP" "$OUTPUT"
echo "$OUTPUT"
