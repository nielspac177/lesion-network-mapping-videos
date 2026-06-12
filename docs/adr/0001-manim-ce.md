# ADR-0001: Manim CE as the animation engine

**Status**: Accepted · **Date**: 2026-06-12

## Context
We need programmatic, equation-first math animations with LaTeX, reproducible
from source. Options: Manim CE, 3Blue1Brown's `manimgl`, hand-built After Effects.

## Decision
Use **Manim Community Edition 0.20.1**. It is pip-installable, actively
maintained, renders LaTeX via `MathTex`, and emits `.srt` subtitles via
`add_subcaption` (which we reuse for voiceover sync).

## Consequences
Good: declarative scenes, LaTeX, parallel scene rendering, large community.
Bad: native deps (cairo/pango/pycairo) and a LaTeX toolchain are required
(see ADR-0002, ADR-0004). Python pinned to 3.12 for clean wheels.
