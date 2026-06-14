"""Narration for c0301_lnm_to_degree — "LNM converges to the degree map".

Source: responses/lnm_critique/papers/P1_critique.md
        responses/lnm_critique/sections/01_the_charge_formalized.md

This chapter states P1's convergence claim precisely and derives it: the
group-average LNM map equals sum(M x C), and under UNIFORM, NON-OVERLAPPING
sampling the average column becomes proportional to the row-sum of C, which is
the node degree, which is the fixed lesion-independent hub map. The final scene
fences the scope: this holds ONLY for the group-average map under that null;
real symptom lesions overlap and are non-random, sampling a structured subset of
rows, and the contrast is a different object.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the convergence claim, stated
    "S1_Claim": [
        ("Here is the strongest form of the critique's central claim, stated as cleanly as we can.", 7.5),
        ("As lesion coverage becomes uniform across the brain, the group-average lesion network map converges to one fixed thing: the degree of the connectome.", 10.0),
        ("The whole pipeline compresses to a single matrix expression. L N M equals the sum over patients of M times C. This is their equation three.", 9.5),
        ("Read the pieces. M is the lesion matrix: its rows are patients, its columns are brain regions.", 8.0),
        ("Each entry of M is a one if that patient's lesion covers that region, and a zero if it does not. Just an on-off indicator.", 8.5),
        ("And C is the fixed normative connectome: a regions-by-regions table, entry C-b-v the connectivity between region b and region v, the same for every patient.", 10.0),
        ("So the only thing that changes from patient to patient is M. The matrix C never moves. Hold that thought; it is the engine of the whole argument.", 9.0),
    ],
    # S2 — what M x C does: row selection
    "S2_RowSelection": [
        ("Now look at what the product M times C actually does, one patient at a time.", 7.0),
        ("Take patient a. Their row of M is a string of zeros and ones, marking which regions their lesion hit.", 8.0),
        ("Multiplying that row into C gives, for each target region v, the sum over b of M-a-b times C-b-v.", 8.5),
        ("Decode the indices. The a is the patient. The b runs over every region that could be hit. The v is the target region we are scoring.", 9.0),
        ("Wherever M-a-b is zero, that term vanishes. Wherever it is one, the whole row C-b-dot is pulled into the sum.", 8.5),
        ("So a row of M simply selects which rows of C get added up. The lesion picks a subset of the rows of the connectome.", 9.0),
        ("That is the entire content of a single lesion's map: a structured pick of rows from one fixed matrix C, then summed.", 8.5),
    ],
    # S3 — the uniform-coverage limit
    "S3_Limit": [
        ("Now push the group to the limit the critique cares about: coverage that becomes uniform across all regions.", 8.0),
        ("Average M over all N patients. The empirical row-average tends to the same weight on every region, because every region gets hit equally often.", 9.5),
        ("In matrix terms, the averaged lesion matrix M approaches the identity matrix I, up to a constant: one unit of coverage per region.", 9.0),
        ("And when M approaches the identity, M times C just copies C. The selection step stops selecting and returns every row.", 9.0),
        ("So the average column, region v's score, becomes one over N times the sum over all R rows b of C-b-v, where R is the number of regions.", 9.5),
        ("That is exactly the column-sum, and because C is symmetric, the row-sum, of the connectome, up to the fixed normalization one over N.", 9.0),
        ("The lesions have washed out. What survives is proportional to the row-sum of C, the same vector for every disorder.", 8.5),
    ],
    # S4 — row-sum = degree = hub map
    "S4_Degree": [
        ("Give that surviving vector its name. The row-sum of C is the degree of C.", 7.0),
        ("Degree just means total connectivity. The degree of region v adds up C-b-v over every other region b: how strongly v talks to the whole brain.", 9.5),
        ("High-degree regions are the hubs. So the row-sum vector, drawn as a brain map, is the hub map: bright at the connectome's busiest crossroads.", 9.5),
        ("And here is the sting. This hub map depends only on C. It is completely lesion-independent. It does not know which disorder you fed in.", 9.0),
        ("Feed in addiction lesions, depression lesions, or random blobs, and the uniform-coverage average lands on this one fixed picture.", 8.5),
        ("That is why we color it as the villain of this story: a single, disease-blind object that the group-average keeps reconstructing.", 8.5),
        ("And it arrives fast. P one reports that ten or more spatially heterogeneous lesions already give correlation above zero-point-four-four to degree.", 9.0),
    ],
    # S5 — the exact scope
    "S5_Scope": [
        ("Now fence the claim precisely, because its power is also its limit.", 7.0),
        ("Everything we just derived holds for the group-average map, under uniform, non-overlapping sampling of lesions across the brain.", 9.0),
        ("That null is exactly what makes M approach the identity. It is the one assumption the whole convergence rests on.", 8.5),
        ("Real symptom-causing lesions break it. Lesions that cause the same symptom overlap, and their locations are not random; they re-hit the same region.", 9.5),
        ("So they sample only a structured subset of the rows of C, not a uniform sweep. The rebuttal calls that the goal of L N M, not a flaw.", 9.5),
        ("And the object that carries signal is not the average; it is the contrast between symptomatic and asymptomatic seeds, a different object entirely.", 9.5),
        ("The numbers bear it out: same-symptom maps correlate at zero-point-four-four, different-symptom at zero-point-zero-nine, and degree only zero-point-one-six.", 9.5),
        ("With the right null, that contrast survives: at threshold t above ten, zero false positives in a thousand iterations. So do not over-claim that L N M is hopeless.", 9.5),
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
