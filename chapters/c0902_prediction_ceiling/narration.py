"""Narration for c0902_prediction_ceiling — "The prediction ceiling".

Source: responses/lnm_critique/papers/P3_biolimits.md
        responses/lnm_critique/sections/07_biological_limits.md

P3 (Pini, Salvalaggio & Corbetta, Nat Neurosci Comment, s41593-026-02319-8,
posted 20 May 2026) is an opinion Comment with NO new data and NO null model.
Its quantitative claims are quoted from prior work. The load-bearing empirical
fact is a PREDICTION ceiling that survives the obvious anatomical fix:
  - 132 first-stroke patients; LNM behavioral R^2 = 0.01 to 0.18 across domains.
  - Anatomical refinement (restrict to coherent-connectivity voxels) did NOT help.
This bounds effect SIZE / clinical utility for a static, first-order connectome.
It is a separate axis from VALIDITY: a permutation-exact test can still find a
small REAL effect. Keep the two axes distinct.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — How well can it predict? Define R^2.
    "S1_Question": [
        ("Set the statistics aside for a moment, and ask the bluntest clinical question. How well can a connectome-based map actually predict?", 9.0),
        ("This is the third critique paper, by Pini, Salvalaggio and Corbetta: a comment on the biological limitations of lesion network mapping.", 9.5),
        ("It asks an empirical question. Of the variance in patient outcomes, how much can a connectome map explain?", 8.5),
        ("The yardstick is R squared, the fraction of outcome variance the model explains. It runs from zero to one.", 8.5),
        ("R squared of one means the map predicts the outcome perfectly. R squared of zero means it predicts nothing at all.", 8.0),
        ("So this whole chapter lives on one number. Not is the test valid, but how big is the effect it can deliver.", 8.0),
    ],
    # S2 — the stroke numbers: R^2 = 0.01 to 0.18, n = 132
    "S2_Numbers": [
        ("Here are the numbers, quoted by P3 from prior stroke work. The cohort is one hundred and thirty-two first-stroke patients.", 9.0),
        ("In that cohort, lesion network mapping predicted behavioral outcomes across several cognitive domains.", 7.5),
        ("And the explained variance ran from R squared equals zero-point-zero-one, at the worst, to zero-point-one-eight at the best.", 9.0),
        ("Read that as a percentage. Between one percent and eighteen percent of outcome variance explained. The rest is unaccounted for.", 9.0),
        ("Even the ceiling, eighteen percent, leaves more than eighty percent of the clinical outcome on the table.", 8.0),
        ("That is a low ceiling. Whatever signal is here, it is small, and it sits far below what a clinic would want to act on.", 8.5),
        ("Keep that bar in view for the rest of the chapter: zero-point-zero-one to zero-point-one-eight, in n equals one hundred and thirty-two.", 9.0),
    ],
    # S3 — refinement did not help
    "S3_Refinement": [
        ("Now the obvious objection. Maybe the ceiling is just noise, and a cleaner anatomy would lift it. Someone tested exactly that.", 9.0),
        ("They built a refined version of the method, restricting the analysis to voxels with coherent connectivity profiles.", 8.5),
        ("The goal was to strip out non-specific signal, the white-and-gray-matter overlap that blurs a lesion's true connections.", 8.5),
        ("More anatomical detail, more specificity, a sharper input. And the result, in P3's words, did not improve prediction.", 9.0),
        ("Same low ceiling. The refined map landed essentially where the standard map did.", 7.0),
        ("That is the critical tell. If cleaning the anatomy does not raise R squared, the limit is not a noise problem you can residualize away.", 9.5),
        ("It points instead at the model class itself. The ceiling is intrinsic to predicting through a static, first-order connectome.", 9.0),
    ],
    # S4 — what that bounds
    "S4_Bounds": [
        ("So what, precisely, does a low, refinement-proof ceiling bound? Be careful here, because it is easy to over-read.", 8.5),
        ("It bounds clinical utility. It says how much any static, linear lesion-mapping method can deliver in the clinic.", 8.5),
        ("And the word any matters. This is a bound on the model class, not on one careless analysis.", 7.5),
        ("Even a statistically spotless pipeline, exact nulls, honest residualization, runs into the same ceiling.", 8.0),
        ("Because the residual outcome variance lives in dimensions a static first-order map simply cannot reach: higher-order reorganization, and the swing between hyper- and hypoconnectivity over time.", 10.5),
        ("Now what it does not bound. It does not say no real circuit exists. It does not say the maps are noise.", 8.0),
        ("It bounds the size of what a static-linear method can deliver. Nothing it says forbids a small, genuine effect from being real.", 9.0),
    ],
    # S5 — honest framing: effect size vs validity
    "S5_Honest": [
        ("This is the honest framing, and it turns on keeping two axes apart. Validity is one axis. Effect size is the other.", 9.0),
        ("Validity asks: does the test control its error rate? Is the answer trustworthy? That is the permutation question.", 8.5),
        ("Effect size asks something separate: granted the effect is real, how big is it? How much variance does it move?", 8.5),
        ("P3 is a statement about the second axis, not the first. It is a limit on clinical utility, on effect size.", 8.5),
        ("And the two are independent. A perfectly valid test can find a real effect that is also genuinely small.", 8.5),
        ("So a low R squared does not refute validity, and a valid test does not promise a large effect. Different questions, different answers.", 9.0),
        ("That is the fair reading of the prediction ceiling. Concede the small effect size; keep it distinct from the question of whether the test is sound.", 9.5),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:28s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':28s} target={grand:5.1f}s ({grand/60:.1f} min)")
