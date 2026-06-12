#!/bin/bash
# Reproducible toolchain setup for the LNM video series (macOS / Apple Silicon).
# Idempotent: safe to re-run. See README.md for the per-step rationale.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$(pwd)"

echo "==> 1. System libraries (Homebrew)"
# cairo/pango: manim render deps.  pkg-config: needed to build pycairo.
# ffmpeg: encode/concat.  (We do NOT use Homebrew's TeX — see step 3.)
for pkg in pkg-config cairo pango ffmpeg; do
  brew list "$pkg" >/dev/null 2>&1 || brew install "$pkg"
done

echo "==> 2. Python 3.12 venv + pinned packages (uv)"
command -v uv >/dev/null 2>&1 || { echo "install uv: https://docs.astral.sh/uv/"; exit 1; }
uv venv --python 3.12 .venv
export PKG_CONFIG_PATH="$(brew --prefix cairo)/lib/pkgconfig:$(brew --prefix pango)/lib/pkgconfig"
VIRTUAL_ENV="$ROOT/.venv" uv pip install --python "$ROOT/.venv/bin/python" -r requirements.txt

echo "==> 3. LaTeX (TinyTeX) packages for MathTex"
# manim needs latex + dvisvgm.  TinyTeX is minimal, so add what MathTex requires.
if command -v tlmgr >/dev/null 2>&1; then
  tlmgr install dvisvgm babel-english standalone preview amsmath amsfonts \
    mathtools doublestroke physics type1cm cm-super xcolor || true
  tlmgr path add || true
else
  echo "   !! tlmgr not found. Install TinyTeX (https://yihui.org/tinytex/) or MacTeX,"
  echo "      then re-run.  dvisvgm + babel-english are mandatory for MathTex."
fi

echo "==> 4. Piper neural-TTS voices"
"$ROOT/.venv/bin/python" -m piper.download_voices en_US-lessac-high en_US-ryan-high \
  --download-dir "$ROOT/piper_voices" || true

echo "==> 5. ffmpeg / x265 note"
# Homebrew ffmpeg 7.1.1 links libx265.215 (x265 4.1); if your keg is 4.2 the
# loader fails. render.sh and build_video.py set DYLD_FALLBACK_LIBRARY_PATH to the
# still-present 4.1 lib. If you upgraded/removed x265 4.1, run: brew reinstall ffmpeg
echo "==> done. Try:  make part0"
