"""Narration for c0102_real_pipeline — "From the operator to a real LNM pipeline".

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is shown as a subtitle in manim AND spoken by the TTS in build_video.py.
`seconds` is the target on-screen duration; the manim scene is built so its
animations fill roughly that long, and the audio is padded to match.

The BEAT-COUNT CONTRACT: len(SCENES[key]) MUST equal the number of
play_beat()/wait_beat() calls in the matching scene class in scenes.py.
"""

SCENES = {
    # ------------------------------------------------------------------
    # S1 — the seed: lesion voxels become the 0/1 indicator ell
    # ------------------------------------------------------------------
    "S1_Seed": [
        ("We have written lesion network mapping as one clean product: m equals C times ell. Beautiful on paper. But where does that ell actually come from, and what does a real pipeline do that this single line hides?", 12.0),
        ("It starts with a patient and a brain scan. A lesion is a region of tissue that was damaged: a stroke, a tumor cavity, a surgical target. Someone traces it, voxel by voxel, on the image.", 11.0),
        ("That tracing becomes the seed. Inside the lesion, every voxel is marked one. Outside, every voxel is marked zero. Stack those marks into a long vector and you have ell, the lesion indicator.", 11.0),
        ("So ell is not abstract. It is literally a column of zeros and ones, one entry per voxel in the brain atlas, with ones exactly where the damage was traced.", 9.5),
        ("Real lesions are not one voxel. They are blobs, hundreds of voxels wide, and the ones in ell mark all of them at once. That is the only thing the patient contributes: which rows of the brain light up.", 11.0),
        ("Everything downstream reads from this seed. Get ell, and we ask the connectome what this damaged tissue is wired to. That question is the next step.", 9.0),
    ],
    # ------------------------------------------------------------------
    # S2 — the normative connectome: group connectome C, m = C ell
    # ------------------------------------------------------------------
    "S2_Connectome": [
        ("Here is the move that makes lesion network mapping unusual. We do not scan this patient's own connections. We look the lesion up in a normative connectome.", 9.5),
        ("A normative connectome is a single big matrix, C, built once from a group of healthy subjects. Its entry C-a-b records the normative functional connectivity between voxel a and voxel b: how strongly they co-activate in healthy brains.", 12.0),
        ("C is symmetric. The wiring from a to b equals the wiring from b to a, in the standard correlation construction. So the matrix is mirror-image across its diagonal.", 9.5),
        ("Now multiply. The lesion network map is m equals C times ell. One matrix-vector product, evaluated at every voxel a in the brain.", 8.5),
        ("Read out a single voxel. Entry a of the map, C-ell sub a, equals the sum over b of C-a-b times ell-b. The sum runs over every voxel b.", 10.0),
        ("But ell-b is zero everywhere outside the lesion and one inside. So the sum collapses: it only adds up C-a-b for the b's that were lesioned. The total normative wiring from voxel a into the wound.", 11.0),
        ("Do that at every a and you get one map for this one patient: each voxel scored by how connected it is, in healthy brains, to this patient's damaged tissue.", 10.0),
    ],
    # ------------------------------------------------------------------
    # S3 — per-subject seed map, then the group t-map (define t)
    # ------------------------------------------------------------------
    "S3_GroupTmap": [
        ("One patient gives one map. But a single map proves nothing. We want the circuit whose disruption tends to produce a symptom. So we pool a group.", 9.5),
        ("Take n patients who all share the symptom. Each one's lesion ell-i gives a seed map m-i equals C times ell-i. We now have n maps, stacked voxel by voxel.", 10.5),
        ("At each voxel we have n numbers, one per patient. We want to know: is this voxel reliably connected to the lesions, across the group, or is it just noise?", 9.5),
        ("That is a t statistic. At voxel v, t equals the mean of the n values, divided by their standard error. Let us decode every symbol.", 9.0),
        ("The mean, x-bar, is just the average map value at this voxel across all n patients. Add the n numbers, divide by n. That is the signal in the numerator.", 9.5),
        ("The standard error, S-E, is the spread of those values divided by the square root of n. It is how much the average would wobble if we resampled patients. That is the noise in the denominator.", 11.0),
        ("So t is signal over noise. A large mean is only convincing if the standard error is small. Divide them, and a big t means: consistently connected, not just connected in one lucky patient.", 11.0),
        ("Compute t at every voxel and you get the group t-map. That, not any single patient's map, is the published lesion network of the symptom.", 9.0),
    ],
    # ------------------------------------------------------------------
    # S4 — where m = C ell is exact vs an idealization
    # ------------------------------------------------------------------
    "S4_Idealization": [
        ("So how faithful is our clean line, m equals C times ell, to that real pipeline? Honestly, it is exact in one place and a deliberate simplification in three.", 9.5),
        ("Exact: the core. A lesion really is a zero-one indicator ell. The connectome really is one fixed matrix C. And the per-patient seed map really is the product C times ell. No approximation there.", 11.0),
        ("Idealization one: Fisher-z. In practice each connectivity value is passed through an inverse-hyperbolic-tangent reshaping before summing. It is a monotone re-scaling. It bends the numbers, but not the leading geometry of the map.", 11.0),
        ("Idealization two: thresholding. The published map is usually thresholded, keeping only voxels above a cutoff. Two maps that are scalar multiples threshold to the same picture, so direction is what survives, and direction is what C-ell sets.", 11.5),
        ("Idealization three: averaging and the t-map. The real group object is a t statistic across patients, mean over standard error, not a bare sum of maps. We fold that into one linear operator and reason about the maps it averages.", 11.0),
        ("None of these touches the engine the debate is about. Fisher-z, thresholds, and the t statistic are monotone reshapings layered on top of one matrix multiply. The shared backbone of C survives all of them.", 11.0),
    ],
    # ------------------------------------------------------------------
    # S5 — recap: the faithful abstraction; the live debate ahead
    # ------------------------------------------------------------------
    "S5_Recap": [
        ("Let us collect the pipeline in one breath. Trace the lesion into a seed ell. Multiply by the group connectome C to get a per-patient map. Pool n patients into a t-map, mean over standard error.", 12.0),
        ("Every patient in that group, and every study, reads from the same one matrix C. Each lesion just selects some rows of it. That single fact is the whole engine of what comes next.", 10.0),
        ("This is why m equals C times ell is faithful enough to analyze. It keeps the one object the critique attacks: a single fixed connectome, sampled over and over by different lesions.", 10.0),
        ("And here the debate goes live. The critique, van den Heuvel and colleagues, proves the group-average map converges to the connectome's degree, its row sums, under uniform, non-overlapping lesion sampling. In that narrow regime, they are right.", 12.5),
        ("But real symptom-causing lesions overlap and are spatially non-random. They hit the same region again and again, sampling only specific rows of C. So the contrast, not the average, can still carry genuine signal.", 11.0),
        ("And the data bite back. Same-symptom maps correlate at zero-point-four-four, versus zero-point-zero-nine for different symptoms and zero-point-one-six to the degree map, with zero false positives in a thousand iterations at t above ten.", 12.0),
        ("Hold that tension. One matrix, sampled by many lesions. The average is nonspecific; the calibrated contrast need not be. That is the abstraction m equals C ell lets us reason about, cleanly, for the rest of the series.", 12.0),
    ],
}

# Estimated total per scene (seconds), for sanity checks.
if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:18s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':18s} target={grand:6.1f}s ({grand/60:.1f} min)")
