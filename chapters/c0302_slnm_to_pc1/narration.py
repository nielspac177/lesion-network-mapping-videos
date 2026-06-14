"""Narration for c0302_slnm_to_pc1 — "Symptom-weighted LNM converges to PC1".

Source: responses/lnm_critique/papers/P1_critique.md
        responses/lnm_critique/sections/01_the_charge_formalized.md

The symptom-weighted variant sLNM = s_v x (M x C) (P1 Eq. 4). Because s_v
multiplies a structured, nearly low-rank matrix, sLNM aligns with the dominant
latent factor of C — its first principal component PC1, which equals the leading
eigenvector u1 (the backbone). PC1 overlaps the degree map at r = 0.82 (P1
p.1241). So symptom-weighting lands almost where plain averaging does. BUT the
symptom CONTRAST — the difference of conditional means — is a different object
the average throws away: same-symptom r=0.44 vs different-symptom r=0.09 vs
degree r=0.16 (REBUTTAL p.3).

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the symptom-weighted variant: sLNM = s_v x (M x C)
    "S1_Def": [
        ("Plain lesion network mapping averages every patient's map. The symptom-weighted variant does something else: it weights each map by a symptom score.", 9.5),
        ("Compressed, the critique writes it as s-v times the quantity M times C. This is their equation four.", 8.0),
        ("M times C is the same object as before: the lesion matrix M selects rows of the fixed connectome C, one row per region a patient's lesion hit.", 9.5),
        ("The new ingredient is s-v: a standardized symptom vector. One number per patient, centered and scaled, measuring how severe that patient's symptom is.", 9.5),
        ("Contrast the two. Plain L N M uses a flat weight: every patient counts the same, an average. s L N M lets the symptom set the weight.", 9.5),
        ("That is why s L N M looks like it injects disease signal. The symptom scores are real clinical numbers, so surely the weighted map must carry the symptom.", 9.0),
        ("Hold that intuition. Over the next minutes we will see where the symptom weighting actually lands, and it is not where you would hope.", 8.5),
    ],
    # S2 — M x C is structured and nearly low-rank
    "S2_LowRank": [
        ("To see where s L N M lands, look hard at the matrix it reweights: the product M times C.", 7.5),
        ("This product is not arbitrary noise. It is highly structured, because the connectome C itself is nearly low-rank.", 8.0),
        ("Nearly low-rank means a handful of patterns explain almost all of C. Most of its content lives in just a few directions.", 8.5),
        ("And one pattern dwarfs the rest. The single biggest direction is the degree, or hub, pattern. We have been calling it the backbone.", 9.0),
        ("Spell out the spectrum. C equals a sum over patterns u-j, each one written as the outer product u-j times u-j transpose, and scaled by an eigenvalue lambda-j, with lambda one far larger than lambda two.", 11.0),
        ("Because one factor dominates, any reweighting of the rows is steered toward that leading factor. The weights barely matter; the geometry decides.", 9.5),
        ("So whatever s-v does, multiplying a nearly low-rank, backbone-dominated matrix forces the answer to align with that one dominant factor.", 9.0),
    ],
    # S3 — sLNM -> PC1(C), the first principal component
    "S3_PC1": [
        ("Name that dominant factor precisely. It is the first principal component of C, written P C one of C.", 8.0),
        ("The first principal component is the direction of maximum variance: the single axis along which the rows of C spread out the most.", 9.0),
        ("For a symmetric connectome, that axis is exactly the leading eigenvector u one, the same backbone direction from the spectral decomposition.", 9.0),
        ("So the claim sharpens to an arrow. As you reweight by any standardized symptom vector, s L N M converges to P C one of C.", 9.0),
        ("Read every symbol. s L N M is the symptom-weighted map; P C one of C is the top variance direction; u one is its eigenvector, the backbone.", 9.5),
        ("And the critical phrase from the paper: this happens regardless of whether the lesions or the symptom scores are clinically informed or random.", 9.0),
        ("That is the trap. Random symptom numbers and real symptom numbers both steer s L N M onto the same fixed direction, P C one.", 8.5),
    ],
    # S4 — PC1 is almost the degree map: r = 0.82
    "S4_Correlation": [
        ("Now connect the two variants. Plain averaging converges to the degree map; symptom-weighting converges to P C one. Are those the same place?", 9.5),
        ("Almost. The paper reports a single number: P C one of C overlaps the degree map at r equals zero-point-eight-two.", 9.0),
        ("Decode that r. It is the correlation between two maps over the brain's regions: P C one and the degree, the row-sum of C.", 9.0),
        ("Zero-point-eight-two is a very high overlap. P C one is essentially the degree map wearing a slightly different hat.", 8.5),
        ("So symptom-weighting lands almost exactly where plain averaging does. Both roads arrive at the same backbone-shaped object.", 8.5),
        ("This is the result to remember from this chapter. Box it: r of P C one and degree equals zero-point-eight-two.", 8.0),
    ],
    # S5 — both roads, one hub place; but the contrast is different
    "S5_BothRoads": [
        ("Step back and see the whole picture. Two different recipes, averaging and symptom-weighting, both converge to a hub-shaped object.", 9.0),
        ("Averaging lands on the degree map. Symptom-weighting lands on P C one. And those two overlap at zero-point-eight-two. One hub place, two roads.", 9.5),
        ("If that were the end of the story, s L N M would be hopeless: the symptom would just be repainting the backbone.", 8.5),
        ("But there is an object that neither road computes, and that the average actively throws away: the symptom contrast.", 8.5),
        ("The contrast is the difference of conditional means: the average map of patients who have the symptom, minus the average of those who do not.", 9.5),
        ("Subtraction is the trick. The shared backbone is in both groups, so it cancels in the difference, leaving the part that knows the symptom.", 9.0),
        ("And the contrast behaves. Same-symptom lesions correlate at zero-point-four-four; different-symptom only zero-point-zero-nine; the degree map only zero-point-one-six.", 9.5),
        ("So the symptom-weighted average lands on the backbone, yes. But the symptom contrast is a different object, and it carries the signal the average discards.", 9.5),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:16s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':16s} target={grand:5.1f}s ({grand/60:.1f} min)")
