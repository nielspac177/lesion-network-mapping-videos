# ADR-0002: TinyTeX + tlmgr for MathTex (dvisvgm, babel-english)

**Status**: Accepted · **Date**: 2026-06-12

## Context
`MathTex` compiles LaTeX to DVI then converts DVI→SVG with `dvisvgm`. The machine
had TinyTeX (minimal) without `dvisvgm`, and Homebrew's `dvisvgm` could not find
TinyTeX's kpathsea config (texmf.cnf), it failed with "none of the default map
files could be found". The minimal TeX also lacked `babel-english`, so every
MathTex failed with "Package babel Error: Unknown option 'english'".

## Decision
Install `dvisvgm` and the math packages **through `tlmgr`** so they integrate with
TinyTeX's kpathsea, and `tlmgr path add` to expose them:
`tlmgr install dvisvgm babel-english standalone preview amsmath amsfonts mathtools
doublestroke physics type1cm cm-super xcolor`.

## Consequences
Good: self-consistent TeX; MathTex renders. Bad: a Homebrew `dvisvgm` on PATH will
shadow and break it, keep `/usr/local/bin` (TinyTeX symlink) ahead of Homebrew.
Captured in `scripts/bootstrap.sh`.
