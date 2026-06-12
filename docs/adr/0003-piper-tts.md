# ADR-0003: Piper neural TTS over macOS `say`

**Status**: Accepted · **Date**: 2026-06-12

## Context
The voiceover must sound natural and be reproducible on any machine. macOS `say`
only had the basic "Samantha" voice installed (robotic); Enhanced/Premium voices
require a manual GUI download and are macOS-only. Cloud TTS (ElevenLabs/OpenAI)
sounds best but needs an API key, costs money, and isn't offline-reproducible.

## Decision
Use **Piper** (`piper-tts`), a local neural TTS, with downloadable ONNX voices
(`en_US-lessac-high`, `en_US-ryan-high`). `build_video.py --tts piper` is the
default; `--tts say` remains a fallback.

## Consequences
Good: natural, offline, reproducible, no key/cost; voice models fetched by
`make voices`. Bad: ~100 MB per voice (git-ignored, downloaded on demand).
