"""Narration for c1003_rebuttal_data — "The rebuttal data".

Source: responses/lnm_critique/papers/REBUTTAL_sound.md
        responses/lnm_critique/sections/08_recipe.md

This chapter presents the rebuttal's DIRECT EMPIRICAL EVIDENCE that the symptom
contrast, done right, carries disease-specific signal. The numbers are quoted
verbatim from the Siddiqi-group rebuttal (1090-lesion / 34-symptom reanalysis,
REBUTTAL p.3) and the Petersen replication (refs 4,14; recipe C2):
  - same-symptom spatial r = 0.44 vs different-symptom r = 0.09 (p < 0.0001)
  - same-symptom r = 0.44 vs degree-map r = 0.16 (p < 0.0001)
  - 0 false positives / 1000 iterations at sensitivity 75%, specificity t > 10
  - 4.6% of permutations only at the lenient t = 3.0
  - Petersen et al.: 2,950-patient label-permutation recovers distinct networks

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — what would prove signal exists
    "S1_Setup": [
        ("We have granted the critique its strongest point: the group-average map, under uniform random lesions, just rebuilds the connectome's degree.", 9.5),
        ("But the rebuttal makes a sharper claim. The disease signal was never supposed to live in the average. It lives in the contrast.", 9.0),
        ("The contrast compares lesions that cause one symptom against control lesions that cause a different symptom.", 8.5),
        ("So here is a clean, falsifiable test. If the contrast really carries disease-specific signal, three inequalities must hold.", 8.5),
        ("One: maps from patients with the SAME symptom should correlate more than maps from DIFFERENT symptoms.", 8.0),
        ("Two: those same-symptom maps should also correlate more with each other than with the degree map, the backbone everyone shares.", 9.0),
        ("If both hold, similarity to the backbone is not the whole story, and the contrast is recovering something specific.", 8.5),
        ("The metric throughout is the spatial Pearson correlation, r, between unthresholded whole-brain maps, the critique's own preferred measure.", 9.0),
    ],
    # S2 — the correlation numbers
    "S2_Correlations": [
        ("The rebuttal ran exactly this test on its own database: one thousand and ninety lesion locations causing thirty-four different symptoms.", 9.5),
        ("Here are the three numbers, all spatial correlations between unthresholded maps. Watch which bar wins.", 8.0),
        ("Same-symptom maps correlate at r equals zero-point-four-four. That is the tall bar, the disease-specific agreement.", 8.5),
        ("Different-symptom maps correlate at only r equals zero-point-zero-nine. Strip the symptom away and the agreement nearly collapses.", 9.0),
        ("And the degree map, the pure backbone, sits at just r equals zero-point-one-six against the same-symptom maps.", 8.5),
        ("So same-symptom beats different-symptom, zero-point-four-four against zero-point-zero-nine, with p less than zero-point-zero-zero-zero-one.", 9.0),
        ("And same-symptom beats degree, zero-point-four-four against zero-point-one-six, again p less than zero-point-zero-zero-zero-one.", 9.0),
        ("Both inequalities hold. The signal that survives is symptom-specific, not just the backbone showing through.", 8.0),
    ],
    # S3 — error control holds
    "S3_FalsePositives": [
        ("A skeptic answers: maybe the method just fires too easily, so even a real difference proves nothing. So the rebuttal measured its false-positive rate.", 9.5),
        ("The test: take fifty lesions drawn at random from the database, compare them to the remaining one thousand and forty, and count spurious hits.", 9.5),
        ("They used the critique's own thresholds, sensitivity seventy-five percent and specificity t greater than ten, and ran one thousand iterations.", 9.5),
        ("The result is striking. At t greater than ten, zero false positives in one thousand iterations. Not a single one.", 9.0),
        ("False positives appeared only when they loosened the threshold far below normal practice, to t equals three-point-zero.", 8.5),
        ("And even there the rate was just four-point-six percent of permutations, at a threshold most published studies would never use.", 9.0),
        ("So the symptom null controls error. The specificity step is what keeps the nonspecific backbone, including degree, from leaking through.", 9.0),
    ],
    # S4 — the Petersen replication
    "S4_Petersen": [
        ("One database could be a fluke. So the strongest support comes from an independent, much larger replication.", 8.5),
        ("Petersen and colleagues, cited by the rebuttal as the source of the raw-data permutation method, ran the test at scale.", 9.0),
        ("Their analysis used label permutation: shuffle each patient's clinical symptom against a different patient's network map.", 9.0),
        ("Shuffling the labels holds the backbone fixed in both the real and the shuffled statistic, so the backbone cannot fake a result.", 9.5),
        ("They ran this across two thousand nine hundred and fifty patients, an order of magnitude beyond the original test.", 9.0),
        ("And distinct symptoms recovered distinct networks. The contrast was specific, not a single shared hub map.", 8.5),
        ("That is large-scale, independent evidence that the contrast, done right, separates one symptom's circuit from another's.", 9.0),
    ],
    # S5 — weighing it
    "S5_Weight": [
        ("Now let us weigh exactly what this data does, and just as carefully, what it does not do.", 8.0),
        ("What it does: it is direct empirical support for the rebuttal's central claim. The contrast, done right, is specific.", 8.5),
        ("Same-symptom at zero-point-four-four, beating different-symptom and the degree map, with zero false positives, is a real existence proof.", 9.5),
        ("But it does not erase the critique's first result. The group-average map, under uniform sampling, really does converge to degree.", 9.0),
        ("And it does not touch the third charge, the biological ceiling: a static connectome is still blind to dynamic reorganization.", 9.0),
        ("What it answers is a different, prior question. The critique implied the contrast can NEVER recover disease-specific signal.", 9.0),
        ("This data answers that question with a clear yes, it can. The average erases the difference; the contrast, under a symptom null, does not.", 9.5),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:22s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':22s} target={grand:5.1f}s ({grand/60:.1f} min)")
