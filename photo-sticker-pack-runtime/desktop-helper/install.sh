#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DESTINATION="${HOME}/Applications/StickerDesk.app"
OPEN_AFTER_INSTALL=true

while [[ $# -gt 0 ]]; do
  case "$1" in
    --destination)
      [[ $# -ge 2 ]] || { echo "missing value for --destination" >&2; exit 2; }
      DESTINATION="$2"
      shift 2
      ;;
    --no-open)
      OPEN_AFTER_INSTALL=false
      shift
      ;;
    *)
      echo "unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

case "$DESTINATION" in
  ""|"/"|"."|".."|"${HOME}"|"${HOME}/")
    echo "unsafe destination path" >&2
    exit 2
    ;;
esac

if [[ -L "$DESTINATION" ]]; then
  echo "destination may not be a symbolic link" >&2
  exit 2
fi

DESTINATION_PARENT="$(dirname "$DESTINATION")"
mkdir -p "$DESTINATION_PARENT"
INSTALL_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/stickerdesk-install.XXXXXX")"
trap '/bin/rm -rf -- "$INSTALL_ROOT"' EXIT

BUILT_APP="$INSTALL_ROOT/StickerDesk.app"
"$SCRIPT_DIR/build.sh" --output "$BUILT_APP"

BACKUP_APP=""
if [[ -e "$DESTINATION" ]]; then
  timestamp="$(date +%Y%m%d-%H%M%S)"
  BACKUP_APP="$DESTINATION_PARENT/StickerDesk.previous-$timestamp.app"
  [[ ! -e "$BACKUP_APP" && ! -L "$BACKUP_APP" ]] || {
    echo "backup destination already exists: $BACKUP_APP" >&2
    exit 2
  }
  mv "$DESTINATION" "$BACKUP_APP"
fi

rollback() {
  if [[ -e "$DESTINATION" || -L "$DESTINATION" ]]; then
    mv "$DESTINATION" "$INSTALL_ROOT/failed-StickerDesk.app"
  fi
  if [[ -n "$BACKUP_APP" && -e "$BACKUP_APP" ]]; then
    mv "$BACKUP_APP" "$DESTINATION"
  fi
}

if ! /usr/bin/ditto "$BUILT_APP" "$DESTINATION"; then
  rollback
  exit 1
fi

if ! /usr/bin/codesign --verify --deep --strict "$DESTINATION"; then
  rollback
  exit 1
fi

LSREGISTER="/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister"
if [[ -x "$LSREGISTER" ]]; then
  "$LSREGISTER" -f "$DESTINATION" || true
fi

if [[ "$OPEN_AFTER_INSTALL" == true ]]; then
  /usr/bin/open "$DESTINATION"
fi

echo "$DESTINATION"
if [[ -n "$BACKUP_APP" ]]; then
  echo "Previous version: $BACKUP_APP"
fi
