"""Narration for c1001_full_pipeline — "The full recommended pipeline".

Source: responses/lnm_critique/sections/08_recipe.md
        responses/lnm_critique/sections/04_removing_the_backbone.md (projector)

This is the operational summary of the whole series: one diagram, five steps,
each neutralizing one named failure of the one-sample-average practice. Nothing
new is proven here; the moral is the MAPPING — charge to fix, with the reason
the fix works written next to it.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the recipe, one diagram (the full flow, naming each box)
    "S1_Overview": [
        ("We have spent the series taking the critique apart. Now we put the answer back together as one pipeline.", 8.5),
        ("Read it as a flow of five boxes. Each box is one move, and each move neutralizes one specific charge.", 8.5),
        ("Box one: form a contrast under the symptom-label null, H-nought-sym. Test the difference between symptom and no-symptom, never the average.", 9.5),
        ("Box two: calibrate it with Freedman and Lane. Permute size-adjusted residuals, so the lesion-size confound cannot leak into the result.", 9.5),
        ("Box three: residualize the backbone. Strip the connectome's leading modes with the projector, so the test sees only off-backbone signal.", 9.5),
        ("Box four: demand the contrast beat a degree-plus-size baseline out of sample. If degree alone predicts as well, you have found only the backbone.", 10.0),
        ("Box five: control family-wise error with the permutation max-statistic, so sweeping many voxels or thresholds cannot manufacture a false hit.", 9.5),
        ("That is the whole recipe. The rest of this chapter walks the boxes and names the failure each one shuts down.", 8.0),
    ],
    # S2 — symptom null + Freedman-Lane (steps 1-2)
    "S2_NullAndFL": [
        ("Start with the first two boxes, because they come first for a reason. They decide what question you ask and how you calibrate it.", 9.0),
        ("Step one: form the symptom-label contrast. For each patient i you have a residualized map and a symptom label y-sub-i, zero or one.", 9.0),
        ("The statistic is the difference between the labelled and unlabelled groups at every voxel, or the slope of the map on the outcome.", 9.0),
        ("Now the null. Under H-nought-sym the labels are exchangeable given the fixed lesions. So you shuffle the symptom labels, not the lesions.", 9.5),
        ("Why labels and not locations? The backbone is the same in every patient. Shuffling labels keeps it fixed in the real and the shuffled statistic, so it cancels and cannot fake a result.", 11.0),
        ("Step two: protect against size. Lesion size is the dominant nuisance, so we permute size-adjusted residuals. This is the Freedman and Lane scheme.", 9.5),
        ("Freedman and Lane fits the size covariate first, then permutes only the residualized part of the outcome, holding the nuisance fixed across permutations.", 10.0),
        ("So these two come first because together they are valid and size-protected: the right question, asked with a null that the backbone and the size confound cannot bias.", 10.0),
    ],
    # S3 — residualize the backbone (step 3, recall the projector)
    "S3_Residualize": [
        ("Step three sharpens the estimate. The null already made the test valid; residualization makes it powerful and specific.", 8.5),
        ("Recall the spectral picture. Write the connectome C as a sum over modes: lambda-sub-j times u-sub-j, the j-th eigenvector, times its transpose.", 9.5),
        ("The leading modes u-one through u-r are the backbone: the dominant skeleton every seed lights up. Call that span the backbone subspace B.", 9.5),
        ("Build its projector: Pi-sub-B equals the sum from j equals one to r of u-sub-j u-sub-j transpose. Pi-sub-B x is the part of x that lies in the backbone.", 10.0),
        ("Its complement, Pi-sub-B-perp equals the identity minus Pi-sub-B, keeps everything orthogonal to the leading modes.", 9.0),
        ("The residualized map is m-sub-ell minus Pi-sub-B m-sub-ell, which equals Pi-sub-B-perp m-sub-ell. We subtract the backbone and keep the tail of the spectrum.", 10.0),
        ("And this costs no signal. Under backbone-sharing the backbone is label-independent, so all of the between-group difference lives in the residual; only nonspecific noise is removed.", 10.5),
        ("So the test now sees off-backbone signal alone. The thing P-one says is shared, and the thing we remove, are one and the same object.", 9.0),
    ],
    # S4 — degree baseline + FWE max-statistic (steps 4-5)
    "S4_BaselineFWE": [
        ("The last two boxes set the bar for belief. One is a prediction standard, the other a multiple-comparisons control.", 8.5),
        ("Step four: out-of-sample prediction against a degree baseline. Train on one cohort, predict the graded outcome in a held-out cohort.", 9.5),
        ("And require it to beat a map built from node degree and lesion size alone. That is the actual control the rebuttal used.", 9.0),
        ("The logic is sharp: if the disease map were only the backbone, a degree map would predict just as well. Beating it is the evidence that something beyond the backbone is doing work.", 11.0),
        ("Step five: control family-wise error with the permutation max-statistic. For each shuffle, record the single largest voxel statistic in the brain.", 9.5),
        ("Those maxima form a null distribution. Your threshold is its ninety-fifth percentile, with at least five thousand permutations, controlling family-wise error at five percent.", 10.0),
        ("Because you compare against the maximum, surviving voxels are significant across the whole family at once, so sweeping voxels or thresholds cannot inflate false positives.", 10.0),
        ("The witness that real signal survives all of this: at threshold t above ten, zero false positives in a thousand iterations.", 9.0),
    ],
    # S5 — why each step earns its place (the pipeline IS the critique, answered)
    "S5_Why": [
        ("Step back and read the pipeline as an argument. Each box neutralizes exactly one failure of the average-map practice.", 8.5),
        ("The symptom-label contrast answers the wrong question. The average erases the difference; the contrast is where any disease signal was ever supposed to live.", 9.5),
        ("Freedman and Lane answers the size confound. By permuting size-adjusted residuals, lesion size cannot masquerade as a finding.", 9.0),
        ("Residualization answers backbone dominance. Projecting out the leading modes removes the nonspecific bulk that explains ninety-three percent of map variance.", 10.0),
        ("The degree baseline answers the hub artifact. Beating degree out of sample proves the result is not just the brain's wiring showing through.", 9.5),
        ("The max-statistic answers multiple comparisons. It holds family-wise error fixed across every voxel and threshold you examined.", 9.0),
        ("Notice the single theme: every fix either makes the backbone cancel, subtracts it, or refuses to read its shadow as a result.", 9.0),
        ("So the pipeline is the critique, answered point by point. The premises are true; only the leap to L N M is hopeless over-shoots, once these five moves are in place.", 10.0),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:18s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':18s} target={grand:5.1f}s ({grand/60:.1f} min)")
