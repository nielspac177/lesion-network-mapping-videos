# ADR-0004: Render to a native-filesystem media dir

**Status**: Accepted · **Date**: 2026-06-12

## Context
The repo lives on an external/non-APFS volume that auto-creates macOS AppleDouble
`._*` sidecar files. Manim's LaTeX cleanup tried to unlink a phantom `._*.log`
companion and crashed with `FileNotFoundError`, masking real errors.

## Decision
Render with `--media_dir $HOME/lnm_media` (native filesystem) and export
`COPYFILE_DISABLE=1`. The media dir is outside the repo and git-ignored.

## Consequences
Good: stable rendering; real LaTeX errors surface. Bad: final videos must be
copied back into `videos/` (the build script handles this). `render.sh` sets both.
