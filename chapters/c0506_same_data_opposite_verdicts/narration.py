"""Narration for c0506_same_data_opposite_verdicts — "Same data, opposite verdicts".

Source: responses/lnm_critique/sections/03_the_right_null.md
        responses/lnm_critique/papers/REBUTTAL_sound.md

The chapter takes the section's tiny worked example — four patients, one voxel —
and runs the LOCATION null and the SYMPTOM null on the SAME data, side by side.
The location null finds nothing; the symptom null finds T equals four, p equals
one sixth. Nothing changed but the null hypothesis — the question. Then the
rebuttal's empirical witness: zero false positives in a thousand iterations at
threshold t above ten.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — two nulls, one dataset
    "S1_TwoNulls": [
        ("To feel the whole argument, watch one tiny dataset judged by two different courts.", 7.5),
        ("Four patients. One voxel of map value each, so we strip away space and keep only the contrast logic.", 9.0),
        ("Every map value splits in two. A backbone piece b sub i, the same large connectome offset of ten for everyone.", 9.0),
        ("Plus a small residual r sub i: plus two, plus two, minus two, minus two. The only thing a symptom could plausibly track.", 9.5),
        ("So the observed maps x sub i are twelve, twelve, eight, eight. The first two patients are impaired, the last two spared.", 9.0),
        ("Now we ask two questions of these exact numbers. The location null: is this place special?", 8.0),
        ("And the symptom null: do the labels track these fixed lesions more than chance allows? Same data, two courts.", 8.5),
    ],
    # S2 — the location null finds nothing
    "S2_LocationFinds": [
        ("Run the location null first. We compare each patient's map against random seeds drawn from an ensemble.", 8.5),
        ("But recall R one, the backbone result. Every seed's map is nearly a scalar multiple of one fixed direction, u sub one.", 9.0),
        ("Decode each piece. m sub ell is the seed's map. Lambda one is the connectome's top eigenvalue. u sub one transpose ell is a single scalar — how much the lesion overlaps that direction.", 10.0),
        ("So every fake map is about ten, all backbone — and every real map is about ten too. The crowd of fakes looks just like the data.", 9.5),
        ("The statistic T of each random draw lands right where the observed value sits. T-b is roughly T observed for almost every b.", 9.0),
        ("The observed map is not extreme against the ensemble. Its p-value is large, dead-center in the null. Nothing rejects.", 9.0),
        ("This is no miscalibration. The location null is a valid test — of a question the backbone was always going to blur.", 8.5),
        ("A non-significant result here is not evidence against a lesion-symptom link. It is the wrong question, correctly answered.", 9.0),
    ],
    # S3 — the symptom null finds T = 4
    "S3_SymptomFinds": [
        ("Now the same four patients, the second court. Keep every lesion fixed; only shuffle who is labelled impaired.", 8.5),
        ("Our statistic is the difference in group means. Impaired mean minus spared mean: twelve minus eight gives T observed equals four.", 9.5),
        ("With two ones and two zeros among four patients, there are exactly six ways to assign the labels. We compute T for each.", 9.0),
        ("And watch the backbone vanish. The offset of ten is the same constant on both sides, so it cancels in every single difference.", 9.5),
        ("T depends only on the residuals. The six values are: plus four, minus four, and zero, zero, zero, zero.", 8.5),
        ("The observed T of four is the single largest. Its one-sided permutation p-value is one over six, about zero point one seven.", 9.5),
        ("That p came from counting labelings, not from any distribution. Swap the offset from ten to ten thousand and nothing changes.", 9.0),
        ("The same data that rejected nothing under location now surfaces a real effect: T equals four, the top of its null.", 8.5),
    ],
    # S4 — the difference is the question
    "S4_Difference": [
        ("Put the two verdicts side by side. Same patients. Same connectome. Same maps. Opposite fate.", 8.0),
        ("Under the location null, T observed is unremarkable — it finds nothing. Under the symptom null, T equals four tops its null.", 9.0),
        ("Nothing changed between them but the null hypothesis. Nothing changed but the question we chose to ask.", 8.0),
        ("Because the two nulls test opposite hypotheses. Location asks if the place is special; symptom asks if the label tracks the place.", 9.5),
        ("And the backbone has opposite fates too. It is the villain that swamps the location null and a non-entity in the symptom null.", 9.0),
        ("So a failed null is a failed question, not a failed method. A failure to reject was never proof of no signal.", 8.5),
        ("This is the thesis of the whole series, demonstrated on numbers you can check by hand. The question is everything.", 8.5),
    ],
    # S5 — the empirical witness
    "S5_Witness": [
        ("The hand example shows the mechanism. The rebuttal supplies the empirical witness at scale.", 8.0),
        ("Siddiqi and colleagues re-analysed their own database: one thousand and ninety real lesion locations causing thirty-four symptoms.", 9.5),
        ("They drew fifty lesions at random and compared them to the remaining one thousand and forty, a thousand times over.", 9.0),
        ("At the standard thresholds — sensitivity seventy-five percent, specificity t above ten — zero false positives in a thousand iterations.", 10.0),
        ("Leakage appears only when you drop below standard. At the lenient threshold t equals three, four point six percent of permutations.", 9.5),
        ("So the symptom-label null controls error exactly where it matters, at the thresholds real LNM studies actually use.", 8.5),
        ("Same data, opposite verdicts. The location null asks the wrong question; the symptom null asks the right one, and it holds.", 9.0),
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
