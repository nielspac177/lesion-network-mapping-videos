"""Narration for c0504_four_patient_example — "The four-patient worked example".

Source: responses/lnm_critique/sections/03_the_right_null.md
        (the "A tiny worked example" subsection, p. lines 114-147)

Four patients, one voxel each. Map value x_i = backbone b_i + residual r_i with
b_i = 10 for everyone and r_i = +/- 2. Two impaired (y=1), two spared (y=0). The
contrast statistic is the difference in group means, T = mean(impaired) - mean(spared).
We compute T_obs = 4, enumerate all six relabelings (values +4, -4, 0, 0, 0, 0),
read off the permutation p-value 1/6, and prove the backbone is irrelevant by
swapping 10 for 10,000 and watching nothing change.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle AND the spoken line. The number of play_beat()/wait_beat()
calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — Four patients: the setup and the table
    "S1_Setup": [
        ("Let us watch the cancellation happen on numbers you can check by hand. Four patients, one voxel of map value each.", 9.0),
        ("Every patient's map value x sub i splits into two pieces: a backbone piece b sub i, plus a small residual r sub i.", 9.0),
        ("The backbone is the same large connectome offset for everyone. Here b sub i equals ten, for all four patients.", 8.5),
        ("The residual is the only thing the symptom could plausibly track. For two patients it is plus two, for two it is minus two.", 9.0),
        ("So patient one and patient two have map value twelve, while patient three and patient four have map value eight.", 8.5),
        ("Now attach the symptom labels. Patients one and two are impaired, label y equals one. Patients three and four are spared, label zero.", 9.5),
        ("Our statistic is the observed contrast: T equals the impaired group mean minus the spared group mean. Let us compute it.", 9.0),
    ],
    # S2 — The observed statistic: T_obs = 4
    "S2_Tobs": [
        ("Start with the impaired group, patients one and two. Their map values are twelve and twelve, so their mean is twelve.", 9.0),
        ("Now the spared group, patients three and four. Their values are eight and eight, so their mean is eight.", 8.5),
        ("The observed contrast is twelve minus eight, which is four. So T observed equals four.", 8.0),
        ("Watch where that four came from. The impaired mean is the backbone ten plus the residual plus two. The spared mean is ten minus two.", 9.5),
        ("Subtract them. The backbone ten appears on both sides and cancels exactly. Ten minus ten is zero.", 8.5),
        ("What survives is purely the residuals: plus two minus the minus two, which is four. The huge offset contributes nothing.", 9.0),
    ],
    # S3 — All six relabelings
    "S3_AllSix": [
        ("Now the symptom-label null. We keep every map fixed and only reshuffle who is labeled impaired.", 8.5),
        ("With two ones and two zeros among four patients, there are four-choose-two, equals six ways to assign the labels.", 9.0),
        ("The observed labeling, impaired equals patients one and two, gives T equals plus four, as we just found.", 8.5),
        ("Its mirror, impaired equals three and four, swaps the groups: eight minus twelve, giving T equals minus four.", 9.0),
        ("The remaining four labelings each split one twelve and one eight into each group. Twelve plus eight over two, both sides.", 9.5),
        ("So each of those four gives an impaired mean of ten and a spared mean of ten. T equals zero, four times over.", 9.0),
        ("The full permutation distribution is six numbers: plus four, minus four, and zero, zero, zero, zero.", 8.5),
        ("And notice the backbone vanished from the entire table. Every offset of ten cancelled in every group-mean difference.", 9.0),
    ],
    # S4 — The p-value
    "S4_Pvalue": [
        ("Now read a p-value straight off that table, by counting. No distribution, no formula, just counting labelings.", 8.5),
        ("The one-sided p-value is the fraction of labelings whose T is at least as large as the observed four.", 8.5),
        ("Scan the six values: plus four, minus four, zero, zero, zero, zero. How many reach four or higher?", 8.5),
        ("Exactly one: the observed labeling itself, at plus four. Nothing else ties it or beats it.", 8.5),
        ("So the p-value is one out of six, about zero point one six seven. The rank of the observed among all equally likely labelings.", 9.5),
        ("With only four patients you cannot beat one-sixth. That is the resolution the design buys you, and it is honest.", 9.0),
        ("Crucially, that p-value came from counting labelings, not from any assumption about the distribution of the map values.", 9.0),
    ],
    # S5 — Swap 10 for 10,000
    "S5_Invariance": [
        ("Here is the proof that the backbone is genuinely irrelevant. Swap the backbone offset from ten to ten thousand.", 9.0),
        ("Now every patient's map value jumps. Impaired become ten thousand and two, spared become nine thousand nine hundred ninety-eight.", 9.5),
        ("Recompute the observed contrast. Impaired mean minus spared mean is still plus two minus the minus two, which is four.", 9.5),
        ("T observed is unchanged at four, because the ten thousand sits on both sides of the difference and cancels.", 9.0),
        ("Walk the whole table again, and every entry is identical: plus four, minus four, and four zeros, exactly as before.", 9.0),
        ("So the p-value is still one out of six. The null never noticed the backbone, because the contrast never did.", 9.0),
        ("That is the cancellation made concrete. The backbone magnitude is irrelevant to the test: it could be ten, or ten thousand, or anything.", 9.5),
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
