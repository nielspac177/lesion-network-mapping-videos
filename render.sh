#!/bin/bash
# Standard render environment for the LNM series.
# Usage: ./render.sh <script.py> [-q ql|qm|qh] Scene1 Scene2 ...
set -e
cd "$(dirname "$0")"
export PATH="/usr/local/bin:/Library/TeX/texbin:/opt/homebrew/bin:$PATH"
export COPYFILE_DISABLE=1                 # no macOS ._ AppleDouble files
export MEDIA="${MEDIA:-$HOME/lnm_media}"  # native FS: avoids external-volume TeX bugs
export PYTHONPATH="$(pwd):$PYTHONPATH"    # so chapter scripts can `import lnm_engine`
# Homebrew ffmpeg 7.1.1 links libx265.215 (x265 4.1); current keg is 4.2. Point
# dyld at the still-present 4.1 lib so any ffmpeg invocation loads.
export DYLD_FALLBACK_LIBRARY_PATH="/opt/homebrew/Cellar/x265/4.1/lib:/opt/homebrew/lib:$DYLD_FALLBACK_LIBRARY_PATH"
mkdir -p "$MEDIA"

SCRIPT="$1"; shift
QUAL="ql"
if [ "$1" = "-q" ]; then QUAL="$2"; shift 2; fi

exec ./.venv/bin/manim "-$QUAL" --media_dir "$MEDIA" "$SCRIPT" "$@"
