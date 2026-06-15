"""Narration for c0803_strip_backbone — "Move 2: strip the backbone".

Source: responses/lnm_critique/sections/06_single_target.md  (Move 2, R5)
        responses/lnm_critique/sections/04_removing_the_backbone.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

Numbers are spelled out for TTS.
"""

SCENES = {
    # S1 — Why strip even here
    "S1_Why": [
        ("Move one fixed the null. Move two fixes the estimate. And it matters even in the single-target case, where every lesion sits in one tiny thalamic spot.", 9.5),
        ("Recall the single-target decomposition. Each patient's map m sub i splits into a shared term C times l-naught, plus a patient-specific term C times delta sub i.", 9.5),
        ("C times l-naught is the connectivity fingerprint of the V-I-M target itself. Every patient contributes it identically, so it is constant across the cohort.", 9.0),
        ("And by our backbone result, that shared fingerprint is approximately lambda one, the top eigenvalue, times how much the target loads on the leading mode u sub one, times u sub one itself. It is almost pure backbone.", 9.5),
        ("So the single-target average map is more backbone-dominated than the scattered case, not less, because everyone adds the same C times l-naught.", 8.5),
        ("Everything that varies between patients, and everything tied to the outcome, lives in the small term C times delta sub i. That is where the discriminative fingerprint hides.", 9.5),
        ("So we strip the backbone. We residualize: m-tilde sub i equals m sub i minus the backbone projection of m sub i. Let us decode that operator.", 9.0),
    ],
    # S2 — The residualization
    "S2_Operator": [
        ("Here is the residualization, the same operator we built in chapters six-oh-one and six-oh-two. m-tilde sub i equals the quantity I minus Pi sub B, applied to m sub i.", 9.5),
        ("Pi sub B is the orthogonal projector onto the backbone subspace: the span of the top r connectome eigenvectors, u sub one through u sub r.", 9.0),
        ("Concretely, Pi sub B is the sum, from j equals one to r, of u sub j times u sub j transpose. It keeps only the part of a map lying along the leading modes.", 9.5),
        ("Apply it to m sub i and you get exactly the backbone slice: the dominant, shared, nonspecific bulk the critique named.", 8.5),
        ("Now subtract. The complement operator I minus Pi sub B projects onto everything orthogonal to the backbone, the off-backbone tail of the spectrum.", 9.0),
        ("What survives is m-tilde sub i, the residualized map. In the single-target case the shared C times l-naught is gone, so m-tilde is approximately the complement applied to C times delta sub i.", 9.5),
        ("And notice: Pi sub B is fixed before any patient is seen. It is a property of C alone, label-blind. That fixedness is what keeps the move honest.", 9.0),
    ],
    # S3 — The VIM fingerprint concentrates
    "S3_Fingerprint": [
        ("Now watch what stripping does to the signal. Before residualizing, every map is dominated by the same backbone direction, so they all point nearly the same way.", 9.5),
        ("The only thing that differs between patients is C times delta sub i, the connectivity consequence of a slightly different size and position within the target.", 9.0),
        ("On the raw maps that difference is a thin sliver riding on a huge shared chord. Correlations get squashed toward one, and the difference hides in the third decimal.", 9.5),
        ("Apply I minus Pi sub B. The shared chord cancels exactly, because the shared part lives in the backbone we just removed.", 8.5),
        ("What is left is the V-I-M fingerprint: the patient-to-patient differences C times delta sub i, now concentrated in the residual subspace where the test can finally see them.", 9.5),
        ("This is signal-preserving and noise-reducing. The between-group difference was all in the residual already, so the numerator is untouched, while the backbone variance drops out of the denominator.", 10.0),
        ("So the per-voxel signal-to-noise ratio can only go up. The fingerprint that was invisible under the chord becomes visible once the chord is silenced.", 9.0),
    ],
    # S4 — Combine with Move 1
    "S4_Combine": [
        ("Move two never travels alone. We run the outcome-permutation test from Move one on top of the residualized maps.", 8.0),
        ("Recall the division of labour. The permutation null calibrates: it controls false positives. Residualization sharpens: it raises power and specificity.", 9.0),
        ("And the backbone is now neutralized twice over. In the null it is held fixed by exchangeability, so it cannot manufacture a small p-value.", 8.5),
        ("In the estimate it has been projected out by Pi sub B, so it is not even in the statistic to begin with.", 8.0),
        ("Size, the dominant nuisance in the single-target case, is protected by the Freedman-Lane permutation; the backbone is stripped by the projector.", 9.0),
        ("Backbone removed, size controlled, outcome permuted. A critic who says your network is just the connectome's degree structure must now get past both defences at once.", 9.5),
        ("So any signal that survives is clean. It cannot be the shared fingerprint and it cannot be the dose. If it clears the threshold, it lives in C times delta sub i.", 9.5),
    ],
    # S5 — The honest caveat
    "S5_Caveat": [
        ("Now the honesty, because Move two rests on one assumption that can fail.", 7.0),
        ("Residualizing assumes backbone-sharing: that the shared modes carry no between-group difference. That is just the critique's own convergence claim, read at the population level, and it only holds under uniform, non-overlapping sampling. Real symptom lesions overlap and are non-random, so the symptom subset lives in the off-backbone tail.", 11.0),
        ("But suppose the real effect lived in the backbone itself, that the disease genuinely added or removed hubs, not just an off-backbone sliver.", 8.5),
        ("Then Pi sub B would carry signal, and stripping it would delete the very thing you came to find. The cure would erase the disease.", 8.5),
        ("So Move two is not an assumption to make silently. It is a hypothesis: that the V-I-M fingerprint signal lives off the backbone. And a hypothesis is testable.", 9.5),
        ("The guard is simple. Compare the backbone projections across groups before you discard them. If they differ on some mode, do not residualize that mode.", 9.5),
        ("And keep the scope. This whole move lives inside a static connectome C. It sharpens the estimate; it cannot recover the dynamic, higher-order structure that C never encoded.", 9.5),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:20s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':20s} target={grand:5.1f}s ({grand/60:.1f} min)")
