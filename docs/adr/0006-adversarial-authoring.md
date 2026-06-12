# ADR-0006: Adversarial multi-agent chapter authoring

**Status**: Accepted · **Date**: 2026-06-12

## Context
The series is ~40+ mini-videos plus companion volumes. Hand-authoring each is slow,
and AI-authored manim/narration risks math infidelity and render errors.

## Decision
Author each chapter with an agent team: an **author** writes narration+scenes from
the source `.md`; a **math-fidelity adversary** checks every symbol/number against
the source; a **render-lint adversary** checks the manim code against the known
pitfalls (ADR-0005, AUTHORING.md §5). Self-validating authors render at -ql until
clean. Final render/voice is run centrally at 720p.

## Consequences
Good: scale with fidelity gates. Bad: orchestration cost; requires the validated
engine + AUTHORING.md as the shared contract.
