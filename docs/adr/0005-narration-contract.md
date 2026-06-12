# ADR-0005: Narration single-source-of-truth + beat-count contract

**Status**: Accepted · **Date**: 2026-06-12

## Context
Subtitles, on-screen pacing, and the synthesized voiceover must stay in sync.
Authoring them separately drifts. Early scenes also crashed (`IndexError`) or
would have desynced audio when the number of visual "beats" didn't match the
number of narration lines.

## Decision
One narration dict per chapter is the single source of truth. `NarratedScene`
ties each visual beat to one narration line (`play_beat`/`wait_beat`).
**Invariant:** #(play_beat+wait_beat) == len(narration[scene_key]), enforced
(raises on over-consumption, warns on under-consumption) and tested statically by
`tests/test_sync.py` (AST) with no render required.

## Consequences
Good: deterministic A/V sync; cheap CI-able check. Bad: authors must count beats
(documented in AUTHORING.md).
