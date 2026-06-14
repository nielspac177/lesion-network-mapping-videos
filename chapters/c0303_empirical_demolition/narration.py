"""Narration for c0303_empirical_demolition — "The empirical case".

Source: responses/lnm_critique/papers/P1_critique.md
        responses/lnm_critique/papers/P2_nullmodels.md

This chapter lays out the EMPIRICAL evidence van den Heuvel and colleagues
marshal against lesion network mapping, then scopes exactly what it does and does
not prove. Every number is quoted from the two source files.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the dataset: 102 maps across 72 studies
    "S1_Dataset": [
        ("The critique is not just a piece of algebra. It comes with a re-analysis of the published literature, so let us weigh the evidence.", 9.0),
        ("Van den Heuvel and colleagues assembled one hundred and two published lesion-network maps, drawn from seventy-two separate studies.", 9.0),
        ("Those studies span fifty neurological, eighteen psychiatric, and four behavioral conditions. A broad sweep of the field.", 8.5),
        ("To get there they manually segmented three hundred and fifty lesion masks straight from the papers, and pulled fourteen-hundred-plus coordinates from eight more.", 9.5),
        ("Now, what is a published network? It is one image: every patient's lesion mapped through the connectome, then averaged into a single group map.", 9.5),
        ("Averaged across the symptomatic group, thresholded, and printed as the disorder's signature circuit. That single averaged map is the object on trial.", 9.5),
    ],
    # S2 — 78 of 102 carry a degree trace; explain spin / brainsmash nulls
    "S2_DegreeTrace": [
        ("The first headline number. Of the one hundred and two re-analyzed maps, seventy-eight carried a statistically significant trace of degree.", 9.5),
        ("Degree of a region a is the row-sum of the connectome: fix the row a, then sum C-a-b over every other region b. That total is how strongly region a connects to everything else. The hub map.", 9.5),
        ("But significance against what? You cannot just correlate two brain maps and trust the p-value. Smooth maps overlap by accident.", 8.5),
        ("Brain maps have spatial autocorrelation: nearby regions carry similar values. So a fair null must preserve that smoothness.", 8.5),
        ("The spin test does exactly this. It randomly rotates one map across the cortical surface, keeping its spatial structure but breaking its alignment.", 9.0),
        ("Ten thousand such rotations build a null. The seventy-eight count uses p-spin below zero-point-zero-five against that spatial-autocorrelation null.", 9.5),
        ("BrainSMASH is a second null, generating surrogate maps with matched autocorrelation. Under it, ninety-one of one hundred and two maps carry the degree trace.", 9.5),
        ("So between seventy-eight and ninety-one out of one hundred and two. A large majority of published maps echo the connectome's degree.", 8.5),
    ],
    # S3 — shuffled lesions reproduce networks at r = 0.73 to 0.95
    "S3_Shuffled": [
        ("The second line of evidence is sharper, and more damaging. Take a published disorder map. Now throw away the real lesions.", 8.5),
        ("Replace them with lesions randomly shuffled across the brain, with no clinical meaning at all, and run the same pipeline.", 8.5),
        ("For disrupted agency, autism, addiction, and epilepsy, the shuffled-lesion map was indistinguishable from the real one.", 8.5),
        ("The correlations between real and shuffled ran from zero-point-seven-three all the way up to zero-point-nine-five.", 8.0),
        ("Why is a high correlation under a null so damaging? Because a good disease map should DIE when you destroy the disease signal.", 8.5),
        ("If random lesions reproduce your map at r equals zero-point-nine-five, then the map was never carrying the lesions' information. It was carrying the connectome's.", 9.5),
        ("And that is exactly the prediction of the algebra: any heterogeneous lesion set, real or random, converges to degree under averaging.", 9.0),
        ("So the shuffle test is the empirical face of the convergence proof, aimed squarely at the AVERAGE map.", 8.0),
    ],
    # S4 — 93% of variance explained by basic connectome properties
    "S4_Variance": [
        ("Third, they asked a regression question. How much of a published map can you predict from the connectome alone, ignoring the patients entirely?", 9.5),
        ("The predictors are basic connectome properties: subcortical and cortical degree, the degree of four network modules, and three functional gradients.", 9.5),
        ("No disease information. No symptom scores. Just elementary geometry of the fixed matrix C, regressed onto each map.", 8.5),
        ("For the averaging variant, those properties explained ninety-three percent of the variance in the maps, with a standard deviation of five percent.", 9.5),
        ("For the symptom-weighted variant, s-L-N-M, they explained seventy-nine percent, with a standard deviation of about ten percent.", 9.0),
        ("Picture two bars. Ninety-three percent for L-N-M, seventy-nine percent for s-L-N-M, both filled almost to the top by connectome structure alone.", 9.0),
        ("The crucial caveat: these regressions are run on the aggregate, averaged maps. They describe what the group picture is made of, nothing finer.", 9.0),
    ],
    # S5 — what the evidence does and does not prove (scope honestly)
    "S5_WhatItProves": [
        ("Now the honest accounting. Three numbers, all real, all replicated: seventy-eight of one hundred and two, r up to zero-point-nine-five, ninety-three percent of variance.", 9.5),
        ("From these, one conclusion follows cleanly. The group-average map is backbone-dominated and nonspecific. That premise is true, and the rebuttal concedes it.", 9.5),
        ("So if anyone reads a transdiagnostic hub network off the average and calls it biology, the critique has caught a genuine error.", 9.0),
        ("But watch the object. Every one of these tests is run on the AVERAGE, or on its correlation to degree. That is one specific quantity.", 9.0),
        ("It does NOT prove that a symptom CONTRAST, tested under a label-permutation null, finds nothing. That is a different object entirely.", 9.0),
        ("Averaging erases the across-lesion variability. Zalesky and Cash note that the disease signal may live precisely in the variability that averaging throws away.", 9.5),
        ("And a global correlation of zero-point-eight does not rule out localized differences: two maps can correlate at zero-point-eight while differing sharply in a focal region.", 9.5),
        ("So the verdict is narrow and honest. The average is nonspecific, proven. The contrast is hopeless, not proven, and tested elsewhere it survives.", 9.0),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:24s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':24s} target={grand:5.1f}s ({grand/60:.1f} min)")
