"""Single source of truth for narration.

Each scene maps to an ordered list of beats. Each beat is (text, seconds):
the text is shown as a subtitle in manim AND spoken by `say` in make_audio.sh.
`seconds` is the target on-screen duration for that beat; the manim scene is
built so its animations fill roughly that long, and the audio is padded to match.
"""

SCENES = {
    "Scene1_TheMap": [
        ("Lesion network mapping asks a simple question: when a small piece of the brain is damaged, what network does that damage reach?", 8.5),
        ("The ingredients are two. A normative connectome C: a symmetric matrix whose entry C-a-b says how strongly voxel a and voxel b are wired together.", 9.5),
        ("And a lesion: a vector of zeros and ones, ell, marking which voxels were destroyed.", 6.5),
        ("The map is one matrix-vector product. m equals C times ell.", 5.5),
        ("Read out one voxel: its value is the sum over the lesion of its connectivity to every damaged voxel. The total wiring from here into the wound.", 9.0),
        ("Here is the mystery that started a fight in 2026. Lesions in completely different places seem to produce almost the same map. Why would that happen?", 9.5),
    ],
    "Scene2_Backbone": [
        ("The answer is in the spectrum of C. Any symmetric connectome decomposes into orthogonal patterns u-j, each scaled by an eigenvalue lambda-j.", 9.5),
        ("Push a lesion through, and the map becomes a weighted sum of those same patterns, each weighted by how much the lesion overlaps it.", 8.5),
        ("Real connectomes have one giant eigenvalue. Lambda-one towers over lambda-two. We call its pattern u-one the backbone.", 8.5),
        ("So one term dominates the sum: lambda-one, times the lesion's overlap with the backbone, times u-one.", 7.0),
        ("How dominant? The angle between any map and the backbone is bounded by the spectral ratio lambda-two over lambda-one.", 8.0),
        ("Take a tiny example: eigenvalues four, zero-point-three, and zero-point-one. The ratio is seven percent.", 7.0),
        ("Three completely different single-voxel lesions all land within about seven degrees of the same backbone direction. That is the convergence. It is geometry, not biology.", 10.0),
    ],
    "Scene3_Critique": [
        ("In 2026, van den Heuvel and colleagues turned that geometry into a critique.", 6.0),
        ("Average lesion network mapping over many patients, and as the lesions cover the brain more uniformly, the average map converges to the degree of C. The row sums. The hub map.", 10.5),
        ("Weight by symptoms instead, and it converges to the first principal component of C, which itself overlaps degree at r equals zero-point-eight-two.", 9.0),
        ("Their evidence was blunt. Random or reshuffled lesions reproduced published disease networks at correlations of zero-point-seven-three to zero-point-nine-five.", 9.0),
        ("Basic connectome properties explained ninety-three percent of the variance in these maps. Seventy-eight of one hundred-two carried the degree signature.", 9.0),
        ("This is the convergence trap. The average map is the hub map. It looks the same no matter where you lesion, so by itself it certifies nothing.", 9.5),
    ],
    "Scene4_Specificity": [
        ("To see what went wrong, we need two words from diagnostics: sensitivity and specificity.", 6.5),
        ("Sensitivity is true positives over all real positives: does the test fire when there is signal?", 7.0),
        ("Specificity is true negatives over all real negatives: does the test stay silent when there is none?", 7.0),
        ("The critique's null asks: is this lesion location special, compared to random fake lesions?", 7.5),
        ("But the backbone made every map look alike. So the fakes reproduce the real map too. The test fires on noise. Those are false positives, and specificity collapses.", 10.0),
        ("That is why seventy of seventy-eight maps fail this null. Not because the method is fake, but because the question was aimed at a difference the backbone had already erased.", 10.0),
    ],
    "Scene5_Cancellation": [
        ("There is a different question, and it changes everything. Fix the lesions. Fix the connectome. Only shuffle the symptom labels: who was impaired, who was spared.", 10.0),
        ("Under that null, the permutation p-value is exact. The chance of a false alarm is at most alpha, with no distributional assumptions at all.", 9.5),
        ("Now split every patient's map into a backbone piece b-i and a residual r-i. The backbone piece depends on where the lesion sits, never on the symptom label.", 9.5),
        ("When you contrast impaired against spared, the backbone enters both groups identically, in the real labeling and in every shuffle. So it cancels.", 9.0),
        ("Watch it on four patients. Everyone carries a backbone of ten. Only the residuals, plus or minus two, track the symptom.", 8.5),
        ("The observed contrast is four. Across all six relabelings the ten always subtracts away. The p-value, one in six, never even sees the backbone.", 9.5),
        ("Swap the backbone from ten to ten thousand and nothing changes. The villain of the location null is inert here. And at threshold t above ten, zero false positives in a thousand runs.", 10.5),
    ],
    "Scene6_ConvergenceMaps": [
        ("One more place convergence misleads: agreement maps, where you keep only voxels whose sign agrees across K patients.", 8.5),
        ("If the maps were independent coins, all K agreeing has probability two to the one-minus-K. For eight patients, under one percent. Agreement would be impressive.", 10.0),
        ("But add a shared backbone, and each map recovers its sign with probability p. Now the chance all K agree is p to the K plus one-minus-p to the K.", 9.5),
        ("As p approaches one, that goes to one, regardless of K. Convergence becomes automatic, and it certifies the backbone, not the disease.", 9.0),
        ("The critique's own simulation shows it: as lesion overlap climbs, the fraction of significant agreement balloons from ten, to sixty-four, to ninety-seven percent.", 10.0),
    ],
    "Scene7_Resolution": [
        ("So who is right? Both, about different things. The trick is to separate the camera from the court.", 7.5),
        ("The camera is description: the average map. It is dominated by the backbone, it is nonspecific, and the critique proves that correctly.", 8.5),
        ("The court is inference: the contrast under the symptom-label null. The backbone cancels, and only genuine label-linked structure can survive.", 9.0),
        ("You can even subtract the backbone outright: project the map off its leading components. This residual keeps the signal while shedding the dominant nuisance, so the signal-to-noise can only improve.", 11.0),
        ("And the data follow. Same-symptom maps correlate at zero-point-four-four; different-symptom maps at zero-point-zero-nine; the degree map only zero-point-one-six.", 9.5),
        ("One matrix, two operations, opposite verdicts. A failed null is a failed question, not a failed method. That is the whole argument, made visible.", 10.0),
    ],
}

# Estimated total per scene (seconds), for sanity checks.
if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:26s} beats={len(beats):2d}  target={total:5.1f}s  words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':26s} target={grand:5.1f}s ({grand/60:.1f} min)")
