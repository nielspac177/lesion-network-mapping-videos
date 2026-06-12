"""Narration for c0103_charge_formalized — "The critique, formalized, and its exact scope".

Source: responses/lnm_critique/sections/01_the_charge_formalized.md
        responses/lnm_critique/papers/P1_critique.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the thesis, stated fairly
    "S1_Thesis": [
        ("Before we rebut anything, we owe the critique a fair hearing. So let us state its strongest form.", 8.5),
        ("In twenty twenty-six, van den Heuvel and colleagues re-examined lesion network mapping in Nature Neuroscience.", 8.0),
        ("Their thesis: the published disease maps may be largely reconstructions of one fixed thing, the connectome's geometry.", 9.0),
        ("Feed in real lesions, synthetic lesions, or random blobs, and you get back roughly the same picture.", 8.0),
        ("That is because the connectivity atlas has a dominant skeleton that every seed lights up. Call it the backbone.", 8.5),
        ("Our job in this video is to make roughly the same picture precise, and then to fence in the one assumption that makes it true.", 9.0),
    ],
    # S2 — the formal object: LNM = sum(M x C) -> deg(C)
    "S2_FormalObject": [
        ("Here is the critique's own bookkeeping. Lesion network mapping compresses to a single matrix expression.", 8.0),
        ("L N M equals the sum over patients of M times C. This is their equation three.", 7.5),
        ("C is the fixed normative connectome: regions by regions, entry C-a-b the connectivity between region a and region b.", 9.0),
        ("M is the lesion matrix: rows are patients, columns are regions, a one where a patient's lesion covers that region, else zero.", 9.5),
        ("So M times C just selects the rows of C that a lesion hit, and the outer sum averages those rows across patients.", 9.0),
        ("Now the key geometric claim. As coverage grows and M approaches the identity, one lesion per region, the averaging copies C.", 9.5),
        ("Summing across rows then yields the row-sum vector of C: its degree. The hub map. Well-connected regions dominate.", 9.0),
        ("And it arrives fast: ten or more heterogeneous lesions already give correlation above zero-point-four-four to degree.", 9.0),
    ],
    # S3 — sLNM -> PC1(C), r=0.82
    "S3_sLNM": [
        ("There is a symptom-weighted variant, s L N M. Instead of a plain average, step three weights each map by a symptom score.", 9.5),
        ("Compressed, that is s-v times the quantity M times C: their equation four, with s-v the standardized symptom vector.", 9.0),
        ("Because s-v multiplies a structured, nearly low-rank matrix, the result aligns with the dominant latent factor of C.", 9.0),
        ("That factor is the first principal component, P C one of C.", 6.0),
        ("And here is the catch that ties the two variants together. P C one overlaps the degree map at r equals zero-point-eight-two.", 9.0),
        ("So both roads, plain averaging and symptom weighting, lead to almost the same hub-shaped destination.", 8.0),
    ],
    # S4 — the evidence
    "S4_Evidence": [
        ("The argument would be thin without evidence. Van den Heuvel and colleagues supply three blunt numbers.", 8.5),
        ("First: randomly shuffled lesions reproduced published disease networks at correlations of zero-point-seven-three to zero-point-nine-five.", 9.5),
        ("Second: a regression on basic connectome properties, degree, modules, and gradients, explained ninety-three percent of map variance.", 9.5),
        ("Third: of one hundred and two re-analyzed maps, seventy-eight carried a significant trace of degree.", 8.5),
        ("Premises stack to a conclusion. The operation samples one fixed C; that sampling converges to degree; the maps look like degree.", 9.5),
        ("So a large share of published L N M networks are nonspecific, and may not reflect genuine, disease-specific biology.", 8.5),
    ],
    # S5 — THE SCOPE (the hidden conditional)
    "S5_Scope": [
        ("Now the most important slide in the whole debate. Everything just proved rests on one hidden conditional.", 8.5),
        ("It holds for the group-average map, under uniform, non-overlapping sampling of lesions across the brain.", 8.5),
        ("That assumption is what makes M approach the identity and the average converge to degree. Remove it and the proof goes loose.", 9.0),
        ("And the rebuttal, Siddiqi and colleagues, concedes the math verbatim, then steps out of that regime.", 8.5),
        ("Because real lesions that cause a specific symptom overlap, and their locations are not random. They re-hit the same region.", 9.0),
        ("So they sample only a structured subset of the rows of C, not a uniform sweep. Which the rebuttal calls the goal of L N M, not a flaw.", 10.0),
        ("And a symptom contrast is a different object from the average. The average is a description; the contrast is an inference.", 9.0),
        ("Concretely: same-symptom maps correlate at zero-point-four-four, different-symptom at zero-point-zero-nine, and degree only zero-point-one-six.", 9.5),
    ],
    # S6 — what is genuinely entailed vs over-claimed
    "S6_EntailedVsOverclaimed": [
        ("So let us separate, cleanly, what the critique genuinely entails from what would be over-reach.", 8.0),
        ("Entailed, and fully conceded: the one-sample average map of a symptomatic group is dominated by the backbone, hence nonspecific.", 9.5),
        ("Also entailed: random, synthetic, and real seeds all funnel into the same cone, so cross-disorder convergence of average maps follows by construction.", 10.0),
        ("Over-claimed: that because the average is nonspecific, L N M cannot recover any lesion-symptom relationship.", 9.0),
        ("That inference does not follow. The average erases the difference; the contrast under a symptom-label null does not.", 9.0),
        ("The witness is real: with the right null, same-symptom specificity survives, and at threshold t above ten, zero false positives in a thousand iterations.", 10.0),
        ("The premises are true. The narrow conclusion is true. Only the leap to L N M is hopeless over-shoots the proof.", 8.5),
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
