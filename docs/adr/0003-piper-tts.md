# ADR-0003: Local neural TTS (Kokoro, with Piper as fallback)

**Status**: Accepted (updated 2026-06-12) · **Date**: 2026-06-12

## Context
The voiceover must sound human and be reproducible on any machine. macOS `say` only
had the basic "Samantha" voice (robotic). Cloud TTS (ElevenLabs, OpenAI) sounds best
but needs an API key, costs money, and is not offline-reproducible. Piper is local and
natural, but its male voices still sound synthetic on long technical narration.

## Decision
Use **Kokoro** (`kokoro-onnx`, model `kokoro-v1.0`) as the default narrator, voice
`am_michael`. It is local, MIT-licensed, and clearly more human than Piper on this
material. **Piper** stays as a fallback (`--tts piper`), and macOS `say` as a last
resort (`--tts say`). `build_video.py --tts kokoro --kokoro-voice am_michael` is the
default; `kokoro_say.py` does the synthesis.

## Consequences
Good: natural male narration, offline, no key/cost. Bad: Kokoro needs `espeak-ng` for
phonemization and a ~310 MB model file (git-ignored, fetched by `make voices`). Other
male voices to try: `am_fenrir`, `am_puck`.
