# Authoring a chapter, contract for humans and agents

Every mini-video is one manim file + one narration file that share the validated
engine in `lnm_engine.py`. Follow this exactly; it encodes hard-won fixes and the
pedagogical standard for the series.

## 0. Pedagogical standard (non-negotiable)

1. **Explain every sign.** When an equation appears, annotate *each symbol* on
   screen before moving on: what `C` is (the normative connectome matrix), what
   `ℓ` is (the 0/1 lesion indicator), what the product `Cℓ` does, what a subscript
   like `(Cℓ)_a` selects, what `Σ_b C_ab ℓ_b` sums over. Use `Brace`/labels/arrows
   and a dedicated narration beat per symbol cluster. Never show a formula the
   viewer can't fully decode from the video alone.
2. **Do not pre-concede the critique.** Frame it as a live debate. The critique
   (van den Heuvel et al.) is correct about ONE narrow object, the *group-average*
   map under *uniform, non-overlapping* lesion sampling, which converges to the
   connectome degree. State that scope explicitly. Give the rebuttal full standing:
   real symptom-causing lesions **overlap and are spatially non-random**, so they
   sample only specific rows of `C`; the *contrast* (not the average) carries
   genuine signal; empirically same-symptom maps correlate r=0.44 vs r=0.09 for
   different symptoms and r=0.16 for the degree map, with zero false positives in
   1000 iterations at t>10. Present claim and counter-claim side by side, then the
   resolution (camera vs court).
3. **Fidelity.** Every equation, number, and claim must come from the source
   `responses/lnm_critique/` files. No invented constants. Where the source flags
   `[verify against primary source]`, keep that caveat.
4. **Long-form math.** For proofs: pre-proof strategy → proof with words between
   every step → post-proof moral. Type every variable.

## 1. Files & naming (flat, collision-free)

A chapter with id `cNN_slug` (e.g. `c0203_alignment_bound`) is two files in
`chapters/cNN_slug/`:

```
chapters/c0203_alignment_bound/
├── narration.py     # SCENES = {"SceneKey": [(text, seconds), ...], ...}
└── scenes.py        # the manim scenes
```

The manim file basename determines the media output dir, so it MUST be unique
across the repo. Render with the file path; manim adds its dir to sys.path, so
`from narration import SCENES` (sibling) works. `lnm_engine` is importable because
`render.sh` puts the repo root on PYTHONPATH.

## 2. scenes.py skeleton

```python
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

NarratedScene.narration = SCENES          # bind this chapter's narration

class S1_Intro(NarratedScene):
    scene_key = "S1_Intro"                # MUST be a key in SCENES
    def construct(self):
        eq = MathTex("m", "=", "C", r"\ell")
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        self.play_beat(Write(eq))         # one beat = one narration line
        ...
```

## 3. THE BEAT-COUNT CONTRACT (the #1 bug source)

The number of `play_beat()` + `wait_beat()` calls in a `construct()` MUST equal
`len(SCENES[scene_key])`. Over-consumption raises `IndexError` immediately;
under-consumption prints a sync WARNING. Either desyncs the voiceover. Count them.

- To play several animations inside ONE beat, pass them all to one `play_beat`,
  optionally `lag_ratio=0.3` to stagger: `self.play_beat(a, b, c, lag_ratio=0.4)`.
- Helper methods that build mobjects must NOT call `play_beat` unless you count it.

## 4. narration.py

```python
SCENES = {
    "S1_Intro": [
        ("First spoken line. ~2.5 words/sec; keep each beat one idea.", 7.0),
        ("Second line, tied to the next visual beat.", 6.0),
    ],
}
```

- 6–9 beats per scene; each beat 5–11 s. Spoken, conversational, decodes the math.
- Write numbers as words for TTS ("zero point four four", "ten to the one minus K").
- `python narration.py` (add the `__main__` sanity block) prints per-scene totals.

## 5. Manim pitfalls (all hit & fixed already)

- **MathTex sub-indexing:** `MathTex("a","=","b")[2]` indexes the *arguments*. An
  argument that renders to zero glyphs (e.g. a lone `r"\,"`) is dropped and shifts
  indices. Keep each indexed argument visibly non-empty, or color via `.set_color`
  on the whole thing.
- **Helpers must return shiftable mobjects:** return a `VGroup`, not a Python list,
  if the caller does `.shift(...)`. Iterate with `for m in grp.submobjects`.
- **No `\emph` / exotic packages.** Stick to amsmath/amssymb. `\text{}`, `\top`,
  `\perp`, `\underbrace`, `\frac`, `\sum`, `\mathrm`, `\mathbb` (doublestroke) are
  available.
- **Tables:** `MathTable`/`Table` are fine; scale down (`.scale(0.55)`).
- Keep ≤ ~6 mobjects dense on screen; `FadeOut` a group before the next block.

## 6. Render / voice / preview

```
./render.sh chapters/c0203_alignment_bound/scenes.py -q qm S1_Intro S2_Proof ...
python3 build_video.py --media ~/lnm_media --quality 720p30 \
    --script scenes --narration chapters.c0203_alignment_bound.narration \
    --tts piper --piper-voice en_US-ryan-high \
    --out videos/c0203_alignment_bound.mp4
```

(`--script` is the manim file basename = its media dir; the narration module is
the dotted path from repo root.)

## 7. Source map (read before authoring)

| Part | Source file(s) under responses/lnm_critique/ |
|------|----------------------------------------------|
| 1 Setup            | sections/00_abstract_intro.md, 01_the_charge_formalized.md |
| 2 Backbone (R1)    | sections/02_what_is_entailed.md |
| 3 Critique         | papers/P1_critique.md, sections/05 intro |
| 4 Specificity      | sections/03_the_right_null.md (first half) |
| 5 Cancellation     | sections/03_the_right_null.md (second half) |
| 6 Residualization  | sections/04_removing_the_backbone.md |
| 7 Convergence maps | sections/05_the_convergence_trap.md |
| 8 Single-target    | sections/06_single_target.md |
| 9 Bio limits       | sections/07_biological_limits.md, papers/P3_biolimits.md |
| 10 Recipe          | sections/08_recipe.md, 09_references_caveats.md |
| Vols 1–6           | companion volumes (e-values, conformal, three maps) |
