"""Narration for c0804_degree_baseline — "Move 3: beat a degree baseline".

Source: responses/lnm_critique/sections/06_single_target.md  (Move 3)
        responses/lnm_critique/sections/08_recipe.md           (C8, the credibility bar)

Move 3 is the credibility bar of the single-target recipe: out-of-sample
prediction that beats a DEGREE BASELINE. The critique's whole worry is that LNM
maps recover the connectome's degree structure (P1: basic connectome properties
explain ninety-three percent of map variance, p.1244). So the recipe makes degree
the thing to beat. If the residualized full-fingerprint model out-predicts the
degree baseline on held-out patients, there is genuine off-backbone,
location-specific signal — the very thing the critique doubted.

Numbers carried verbatim from source (do NOT invent):
  - degree baseline:  y-hat_i^deg = a + b (u_1^T l_i) + c s_i   (06, Move 3 box)
  - 93% of LNM-map variance explained by basic connectome properties (P1 p.1244)
  - REBUTTAL degree-aware test: same-symptom r=0.44 vs 0.16 to degree, 0.09 to
    different symptom; 0 false positives / 1000 iterations at t>10 (REBUTTAL p.3)

Each scene maps to an ordered list of (text, seconds) beats. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
Numbers are spelled out for the text-to-speech voice.
"""

SCENES = {
    # S1 — define the degree baseline predictor and decode every symbol
    "S1_Baseline": [
        ("Move three is the credibility bar of the recipe, and it starts by building the model you have to beat. Call it the degree baseline.",
         9.0),
        ("Here it is. y-hat sub i for the degree model equals a, plus b times u-one transpose l sub i, plus c times s sub i.",
         9.0),
        ("y-hat sub i is the predicted outcome for patient i, the tremor relief or adverse-effect score the model tries to forecast.",
         8.5),
        ("u-one transpose l sub i is the seed's loading on the leading connectome component: how strongly this lesion sits on the hub backbone.",
         9.5),
        ("s sub i is lesion size, the count of destroyed voxels, the dominant nuisance, written as the one-vector transpose times l sub i.",
         9.0),
        ("a, b, and c are just fitted weights: an intercept, a slope on hub-loading, and a slope on size. Three numbers, nothing else.",
         9.0),
        ("So the whole baseline predicts outcome from two cheap facts: how hub-connected the lesion is, and how big it is. No location detail at all.",
         9.5),
    ],
    # S2 — why this baseline; it operationalizes the critique
    "S2_Why": [
        ("Why pick exactly this baseline? Because it is the critique's own claim, turned into a competitor you must out-predict.",
         8.5),
        ("The critique says published maps are mostly backbone plus size. P1 quantifies it: basic connectome properties explain ninety-three percent of map variance.",
         9.5),
        ("If ninety-three percent of the map is just degree-and-size structure, then degree-and-size should already predict the outcome rather well.",
         9.0),
        ("So any honest method must beat a model that uses only backbone overlap and lesion size. That is the bar made of the critique itself.",
         9.5),
        ("Crucially, the backbone is inside the baseline. You cannot wave a result away as just degree, because degree is the thing being out-competed.",
         9.5),
        ("This is not exotic. The rebuttal's own specificity test compares against the degree map directly: same-symptom r of zero-point-four-four versus zero-point-one-six to degree.",
         10.0),
        ("So both sides agree on the standard. Make degree the thing to clear, then ask whether the fingerprint clears it.",
         8.5),
    ],
    # S3 — out-of-sample test; train/test split
    "S3_OutOfSample": [
        ("Now the second half of the bar, the part the field too often skips. The comparison must be made out of sample, not in sample.",
         8.5),
        ("A within-sample p-value can be argued away as overfitting or as backbone. Out-of-sample prediction cannot.",
         8.0),
        ("So split the patients. Fit on a training set; hold out the rest as a test set the model never saw while learning.",
         8.5),
        ("On the training patients, learn how the graded outcome relates to the lesion: its connectivity fingerprint, its size, its position.",
         9.0),
        ("Then predict the held-out patients' continuous outcomes, and score both models by out-of-sample error, the gain in test R-squared.",
         9.5),
        ("The full residualized-fingerprint model must beat the degree baseline on those unseen patients, not merely fit the training data better.",
         9.5),
        ("And keep the features low-dimensional, size, within-target position, a few fingerprint scalars, because tens of thousands of voxels with N in the tens is guaranteed overfit.",
         10.5),
    ],
    # S4 — what beating it would mean (the verdict)
    "S4_Verdict": [
        ("Suppose the full model wins. The residualized map out-predicts the degree baseline, out of sample, on patients it never saw.",
         9.0),
        ("By construction, that win cannot be the backbone, because the backbone is already in the baseline it just beat.",
         8.5),
        ("And it cannot be a pure size dose-response, because lesion size, s sub i, is also already in the baseline.",
         8.5),
        ("So a positive, replicable prediction gain means the fingerprint carries outcome information beyond degree and beyond dose.",
         9.0),
        ("That is genuine off-backbone, location-specific signal: exactly the thing the critique doubted could exist.",
         8.5),
        ("And it is demonstrated on the critique's own terms, against a degree baseline the critique would have endorsed.",
         8.5),
        ("The rebuttal already shows this is achievable: with the right threshold, zero false positives in one thousand iterations at t greater than ten.",
         9.5),
    ],
    # S5 — the three moves together (recap)
    "S5_Recipe": [
        ("Step back and put the single-target recipe together. Three moves, each aimed at a threat that is actually present.",
         8.5),
        ("Move one: permute the outcome labels, size-protected, so neither the backbone nor lesion size can fake a result.",
         8.5),
        ("Move two: strip the backbone first, projecting each map off the leading connectome components to lift the small patient-specific signal.",
         9.5),
        ("Move three, today's move: beat a degree baseline out of sample, so the win is signal that is neither backbone nor dose.",
         9.0),
        ("Move one fixes calibration, the null cannot lie. Move two improves power. Move three certifies the whole thing on held-out patients.",
         9.5),
        ("Together they form a single-target recipe that answers the critique rather than dodging it, on the critique's own chosen battleground.",
         9.0),
        ("Make the backbone cancel, subtract it, then out-predict it. Pass all three, and the verdict that L-N-M is hopeless simply does not follow.",
         9.5),
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
