"""Narration for c0104_camera_vs_court — Camera vs Court.

Description versus inference: two questions you can ask of the very same
lesion maps, and why the critique's true fact about the average map places no
bound on the inference built from the contrast.

Each beat is (text, seconds): shown as subtitle and spoken by the TTS pass.
"""

SCENES = {
    # ------------------------------------------------------------------
    # S1 — two questions of the same maps
    # ------------------------------------------------------------------
    "S1_TwoQuestions": [
        ("There is a fight in lesion network mapping, and it dissolves the moment you notice a single thing: the same stack of maps can be asked two completely different questions.", 11.0),
        ("Here is the stack. Each patient gives a map: m equals C times ell. C is the fixed normative connectome, the matrix of what wires to what. Ell is the lesion, ones where tissue was destroyed.", 11.0),
        ("Question one is a description. Pile the maps up and take their average, m-bar. What does the typical map look like?", 8.5),
        ("Question two is an inference. Split the patients by symptom, plus for impaired, minus for spared, and ask whether the difference between the two groups is more than chance.", 10.0),
        ("This book has names for the two machines. The average is a camera: it photographs the stack. The contrast is a court: it weighs evidence and returns a verdict.", 9.5),
        ("The critique of twenty twenty-six is entirely correct about the camera. The claim of this video is that it says nothing about the court. Let us see exactly why.", 9.5),
    ],
    # ------------------------------------------------------------------
    # S2 — the camera: m-bar, backbone-dominated
    # ------------------------------------------------------------------
    "S2_Camera": [
        ("Start with the camera, and give the critique its strongest form. No straw man.", 6.5),
        ("Every connectome splits into orthogonal patterns u-j, each scaled by an eigenvalue lambda-j. A real connectome has one giant eigenvalue, lambda-one. Its pattern, u-one, is the backbone.", 11.0),
        ("So each patient's map is a weighted sum of those patterns: lambda-j, times how much that patient's lesion overlaps pattern j, times u-j.", 9.0),
        ("Average over the group and the patient index collapses into c-bar-j: the average overlap of the group's lesions on component j. The map points along whichever component has the biggest lambda c-bar.", 11.0),
        ("Because lambda-one towers over the rest, the leading term wins. The average map aligns with the backbone u-one almost regardless of which voxels the lesions marked.", 10.0),
        ("That is the convergence trap, and it is real. An addiction average, a depression average, a bag of random seeds: all land on u-one. The critique is right about this, and we are not taking it back.", 11.0),
        ("But read what the disease controls: only the loadings c-bar. The direction is owned by the eigenvalues, a property of C alone. The disease never got a vote on where m-bar points.", 10.5),
    ],
    # ------------------------------------------------------------------
    # S3 — the court: the contrast under the symptom-label null
    # ------------------------------------------------------------------
    "S3_Court": [
        ("Now the court. The signal, if it exists, was never in the average. It is in the difference between the patient who has the symptom and the one who does not.", 10.0),
        ("So split the seeds. m-bar-plus is the average over the symptomatic group; m-bar-minus, the average over the spared. Each one, on its own, is still dragged toward the backbone u-one.", 10.5),
        ("The object the court weighs is the contrast: Delta equals m-bar-plus minus m-bar-minus. Subtract the two averages component by component.", 9.0),
        ("Look at the leading, backbone term. It is now scaled by the difference in loadings, c-bar-one-plus minus c-bar-one-minus, not by the loadings themselves.", 9.5),
        ("And the null seals it. We shuffle only the symptom labels, holding every lesion and the whole connectome fixed. There is no reason a coin-flip relabeling should load on the backbone differently.", 11.0),
        ("So in expectation the two backbone loadings match, their difference is zero, and the backbone term vanishes from Delta, leaving the higher components u-two, u-three, weighted by genuine group differences.", 11.0),
        ("The numbers cooperate. Same-symptom maps correlate at zero-point-four-four; different-symptom at zero-point-zero-nine; the degree map only zero-point-one-six. The contrast carries something the average buried.", 11.0),
    ],
    # ------------------------------------------------------------------
    # S4 — why the backbone cancels: x_i = b_i + r_i
    # ------------------------------------------------------------------
    "S4_WhyItCancels": [
        ("Why does the backbone cancel? The full algebra is a later part, but the mechanism fits on one line. Split every patient's map into two pieces.", 9.0),
        ("x-i equals b-i plus r-i. The backbone piece b-i is lambda-one, times the lesion's overlap with u-one, times u-one. The residual r-i is everything left over.", 10.0),
        ("Here is the single load-bearing fact. b-i depends on where the lesion sits in the connectome. It does not depend on the symptom label the patient happens to carry.", 10.0),
        ("So when you contrast impaired against spared, b-i is distributed identically on both sides, in the real labeling and in every shuffle of the null. A term present identically on both sides has no leverage.", 11.0),
        ("Watch it on four patients. Everyone carries a backbone of ten. Only the residuals, plus or minus two, track the symptom. The observed contrast is twelve minus eight, which is four.", 11.0),
        ("Across all six relabelings, the ten on each side always subtracts away. The p-value, one in six, never even sees the backbone. Swap the ten for ten thousand and not one number in the table changes.", 11.5),
        ("The very thing that made the camera nonspecific, the backbone being in every map, is the thing that makes it inert in the court. One mechanism, opposite consequences.", 9.5),
    ],
    # ------------------------------------------------------------------
    # S5 — the moral, stated as a question to be proved
    # ------------------------------------------------------------------
    "S5_Moral": [
        ("Put the two machines side by side. Same matrix C, same maps, two operations.", 7.0),
        ("The camera, the average m-bar, is dominated by the backbone and is nonspecific. The critique proved that, and we proved it again. Do not headline the average map.", 10.0),
        ("The court, the contrast Delta under the label-shuffling null, has the backbone subtracted away by construction. Only genuine label-linked structure can survive.", 9.5),
        ("So the same connectome can return opposite verdicts. The camera says nothing but hubs. The court says here is the symptom direction, cleanly.", 9.0),
        ("This is why the rebuttal can be right even though the critique's fact about the average map is true. They describe different objects, made by different machines.", 9.5),
        ("And it leaves us a precise thing to prove: that the backbone term, lambda-one times the loading difference, really does cancel from the contrast. The full algebra comes next. A failed null is a failed question, not a failed method.", 12.0),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:20s} beats={len(beats):2d}  target={total:6.1f}s  "
              f"words={words:3d}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':20s} target={grand:6.1f}s ({grand/60:.1f} min)")
