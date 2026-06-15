"""Narration for v0603_jackknife_cv — "Jackknife+ and CV+".

Source: volumes/vol6_conformal/chapters/03_jackknife_cv.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

All equations/numbers come from the source chapter. Numbers are written as words
for the TTS engine.
"""

SCENES = {
    # S1 — Splitting wastes data
    "S1_Waste": [
        ("Last chapter we built split conformal: carve the cohort into a training set and a calibration set, fit once, score the held-out patients.", 9.5),
        ("It works exactly. Coverage lands between one minus alpha and one minus alpha plus one over n plus one. So why isn't that the end?", 9.5),
        ("Because the split has a price you cannot pay at small sizes. Suppose thirty-six patients, and an adverse event that fires in about one patient in six.", 9.5),
        ("Split fifty-fifty: eighteen train, eighteen calibrate. Of the eighteen calibration patients, only about three are event-positive. Three scores.", 9.5),
        ("Ask for the ninety-percent quantile of three scores, and the index runs off the end of the list. You cannot even form the threshold.", 9.0),
        ("So here is the goal: use all the data to calibrate, while keeping honest coverage. That motivates leaving each patient out, one at a time.", 9.5),
        ("The catch: a patient's score must come from a model that never trained on them, or the guarantee evaporates. Leave-one-out honors both.", 9.0),
    ],
    # S2 — Jackknife+
    "S2_JackknifePlus": [
        ("Number the patients one to N. For patient i, refit the model on the other N minus one patients. That is the leave-i-out fit, mu-hat minus i.", 9.5),
        ("Then ask how badly that model predicts the patient it never saw. For regression, that is the absolute residual: the size of Y i minus mu-hat minus i of X i.", 10.0),
        ("Call that miss R i, the leave-one-out score. Do it for all N. Now every patient calibrates, and no score came from a model that trained on it.", 9.5),
        ("But to cover a new patient you do not have one model. You have N leave-out models. Jackknife-plus uses all of them.", 9.0),
        ("Each leave-i-out model predicts the new patient, then pads that prediction by patient i's own residual R i, giving a lower and an upper edge.", 9.5),
        ("A candidate value y stays in the set unless too many of these padded intervals exclude it on the same side.", 8.5),
        ("Too many means the count reaches the ceiling of one minus alpha times n plus one. The same quantile index from the split proof.", 9.0),
        ("That pairing, each comparison using its own center and its own radius, is what the plus denotes, and what the proof needs.", 8.5),
    ],
    # S3 — The 1-2alpha floor
    "S3_Floor": [
        ("Now the guarantee. Under exchangeability, the new patient's truth, Y sub n plus one, lands in the prediction set C alpha with probability at least one minus two alpha.", 9.0),
        ("Note: one minus two alpha, not one minus alpha. Where does the factor of two come from? Picture a square matrix of out-of-sample residuals.", 9.5),
        ("Entry R i j is how badly the model trained on everyone except j predicts point i. On the diagonal, that is the ordinary leave-one-out residual.", 10.0),
        ("Exchangeability makes this matrix invariant under swapping rows and columns together, so the pattern of large entries is symmetric across patients.", 9.5),
        ("A counting argument over the strange pairs bounds how many patients can be left uncovered, and translating that count to a probability gives the floor.", 9.5),
        ("The factor of two is the price of comparing against N different leave-out models instead of one. Each comparison can be unlucky in two directions.", 9.5),
        ("But the floor is a guarantee, not a prediction. It is the worst case over every distribution and model. In practice coverage sits near one minus alpha.", 9.5),
        ("So report it honestly. To promise ninety percent, set alpha to zero point zero five so one minus two alpha equals ninety percent. Do not quote one minus alpha as guaranteed.", 10.0),
    ],
    # S4 — CV+
    "S4_CVPlus": [
        ("N refits is a lot when each fit is a voxelwise regression. C-V-plus is the same idea with K folds instead of N.", 8.5),
        ("Partition the patients into K equal groups, the folds. Refit the model K times, each time leaving out one whole fold.", 8.5),
        ("Every patient is scored by the one model that did not train on their fold. So you get N honest scores from only K fits.", 9.0),
        ("Formally, mu-hat minus S of k of i is the model fit on all folds except the one containing i, and R i C-V is that patient's out-of-fold score.", 10.0),
        ("The prediction set is structurally identical to jackknife-plus. Just swap the leave-one-out fit for the leave-one-fold-out fit, and the same for the score.", 9.5),
        ("And the guarantee is identical too: at least one minus two alpha under exchangeability. C-V-plus shares jackknife-plus's theorem exactly.", 9.0),
        ("With K equal to N you recover jackknife-plus, each fold one patient. With K equal to ten you do a tenth of the work and lose only a little sharpness.", 9.5),
    ],
    # S5 — The trade-off
    "S5_Tradeoff": [
        ("So how do you choose? Lay the two options side by side. The split is cheap, just one fit, and its coverage is the exact one minus alpha.", 9.0),
        ("But the split is data-hungry. It spends a calibration set the model never trains on, and at rare-event sizes it spends the wrong data.", 9.0),
        ("Jackknife-plus and C-V-plus use all N patients. Every patient calibrates, the outlier widens the set rather than being discarded.", 9.0),
        ("The price they pay is a worst-case floor of one minus two alpha instead of one minus alpha, and more compute: N fits, or K fits.", 9.0),
        ("So use the split only when N is comfortably large and the event-positive count is adequate, where its exact statement and low cost win.", 9.0),
        ("Otherwise, at the sizes we actually face, use jackknife-plus, or C-V-plus with K equal to ten. The guarantee is the same one minus two alpha.", 9.5),
        ("One more caution: do not cross the wires. One minus two alpha is the residual theorem. For a split classification score the guarantee is still the exact one minus alpha.", 10.0),
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
