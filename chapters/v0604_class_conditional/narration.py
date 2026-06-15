"""Narration for v0604_class_conditional — "Class-conditional and adaptive sets".

Source: volumes/vol6_conformal/chapters/04_class_conditional.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

Numbers are written as words for TTS. Conversational, ~2.5 words/sec, every
symbol decoded.
"""

SCENES = {
    # S1 — Marginal coverage hides gaps
    "S1_Problem": [
        ("Split conformal gave us one promise: the truth lands in our predicted set at least one minus alpha of the time. But that promise is an average over patients.", 9.5),
        ("And an average can lie. Severe ataxia after focused-ultrasound is rare. Most patients never get it. The handful who do are the ones we cannot afford to under-cover.", 9.5),
        ("Write the marginal coverage with the law of total probability. Let pi be the prevalence of the adverse event, the fraction of patients who get it.", 9.0),
        ("Then marginal coverage equals pi times the coverage on the A-E-positive class, plus one minus pi times the coverage on the A-E-negative class. A prevalence-weighted blend.", 9.5),
        ("Now read the failure straight off the algebra. If prevalence is eight percent, the positive term is multiplied by zero-point-zero-eight. It barely counts.", 9.0),
        ("So zero-point-zero-eight times zero-point-one-zero, plus zero-point-nine-two times zero-point-nine-seven, equals zero-point-nine-zero. The headline reads ninety percent.", 9.5),
        ("But the rare class is covered only ten percent of the time. The procedure banked its coverage on the cheap majority. The average abandoned the patient we cared about.", 9.5),
        ("This is not a bug. It is exactly what the theorem promised and no more. If you need the rare class covered, you must ask for it by class.", 9.0),
    ],
    # S2 — Mondrian / class-conditional conformal
    "S2_Mondrian": [
        ("The fix is direct. If blending the two classes is the problem, stop blending. Keep two separate calibration piles, one per class, and compute a separate threshold from each.", 10.0),
        ("First we need a nonconformity score: s of x and y, a number measuring how strange it is to attach label y to a patient with features x. Big means surprising.", 9.5),
        ("The simplest valid choice is s equals one minus p-hat-y of x, where p-hat-y is the model's predicted probability of label y. Confident and correct means a small score.", 9.5),
        ("Now the Mondrian recipe. Let n-sub-c be the number of calibration patients in class c. Collect the within-class scores for just that class.", 9.0),
        ("Set the threshold q-hat-sub-c to the ceiling of one minus alpha times n-c plus one, smallest of those scores. Same quantile index as before, but n-c, the per-class count, replaces n.", 11.0),
        ("The prediction set keeps each label whose score clears its own class threshold: the set of y such that s of x and y is at most q-hat-sub-y.", 9.5),
        ("Read that carefully. To decide whether positive belongs, you compare its score against the positive threshold, built only from positive patients. The majority never touches that comparison.", 9.5),
        ("Why does it work? It inherits the same rank argument. Conditional on the class, the new patient's score is equally likely to land at any rank, so coverage is at least one minus alpha within each class.", 10.0),
        ("Mondrian needs no new theorem. The name is Vovk's: you have carved the data into rectangular blocks, like a Mondrian painting, and calibrate each block on its own.", 9.5),
    ],
    # S3 — Adaptive prediction sets (APS)
    "S3_APS": [
        ("Mondrian fixed who gets covered. A-P-S fixes how informative the set is. The score one minus p-hat can produce sets that tell you nothing.", 9.0),
        ("A good set should be a singleton when the model is confident and grow only when the patient is genuinely ambiguous. The set size should report difficulty.", 9.0),
        ("Here is the adaptive prediction sets idea. Line the labels up from the model's most likely to least likely. Walk down the line, adding up probabilities.", 9.0),
        ("Sort the predicted probabilities in decreasing order, p-(1) at least p-(2), and let r of y be the rank of label y in that order. One for the top, two for the next.", 9.5),
        ("The A-P-S score of label y is the cumulative mass through it: the sum from k equals one to r of y of p-(k). The running total at the moment you include that label.", 10.0),
        ("Concretely: if the model is eighty percent sure the patient is negative, then negative is the top label with score zero-point-eight, and positive sits second with score zero-point-eight plus zero-point-two, equal to one.", 10.5),
        ("So the set includes negative once q-hat is at least zero-point-eight, and only adds positive once q-hat reaches one. A confident patient gets a singleton.", 9.0),
        ("And the payoff is exactness. With the randomized tie-break at the boundary label, split conformal with A-P-S gives coverage exactly one minus alpha, on the nose, not just at least.", 9.5),
    ],
    # S4 — Set size as difficulty
    "S4_SetSize": [
        ("The whole point of A-P-S is that the set width reports difficulty. So let us watch three patients and read their set sizes.", 8.5),
        ("Patient one is split zero-point-nine-five to zero-point-zero-five. The model is sure. The top label clears a low threshold alone, and the patient gets a clean singleton.", 9.5),
        ("Patient three is split zero-point-two-zero to zero-point-eight-zero, sure the other way. Again the top label enters early and the set is a singleton. Confidence, in either direction, means width one.", 9.5),
        ("Patient two is split zero-point-five-five to zero-point-four-five. The model is torn. This fence-sitter is the one who earns the two-label set, admitting the genuine doubt.", 9.5),
        ("That is sharpness: the procedure spends extra width only where it is honestly needed, instead of one-size-fits-all sets that ignore who is hard.", 9.0),
        ("We summarize it with the singleton fraction: how often the set has exactly one label. A high singleton fraction with valid coverage means the sets are both correct and sharp.", 9.5),
        ("In the binary case, true two-label width needs the randomized tie-break. There the second label's score is p-(1) plus a uniform draw times p-(2), so the fence-sitter crosses first.", 10.0),
        ("So the fence-sitter gains its second label at a strictly lower threshold on average. Set width tracks the model's actual confusion, exactly as a difficulty meter should.", 9.5),
    ],
    # S5 — The cost of conditioning
    "S5_Cost": [
        ("Conditioning is not free. The positive threshold is a quantile of only n-one scores. When n-one is small, that quantile is noisy and the index machinery gets coarse.", 9.5),
        ("Take a worked pass: eighty negative scores, twelve positive scores, target ninety percent. The negative index is ceiling of zero-point-nine times eighty-one, which is seventy-three. Plenty of data, a stable quantile.", 10.5),
        ("But the positive index is ceiling of zero-point-nine times thirteen, which is twelve, the maximum of the twelve scores. One atypical positive patient sets it. Report n-one and call it underpowered.", 10.0),
        ("There is a sharper wall. If the ceiling of one minus alpha times n-one plus one exceeds n-one, the index points past the largest score you have. For ninety percent, that happens for any n-one at most eight.", 10.5),
        ("Below that wall, no finite threshold delivers per-class coverage. The honest output for the positive label is the full set, and the write-up should say the coverage is uninformative, not quote a number it cannot back.", 10.0),
        ("This is why leave-one-out matters: it lets every positive patient feed the threshold instead of burning half on a held-out split. Mondrian and jackknife-plus compose cleanly.", 9.5),
        ("State the honest limit out loud. Exact conditional coverage for every individual x is impossible distribution-free. You can have per-class coverage, but not per-person coverage, without assumptions.", 10.0),
        ("And do not over-claim the guarantee. A-P-S, a split score, is exact one minus alpha. Jackknife-plus has a worst-case one minus two-alpha floor. There is no per-individual theorem to write.", 9.5),
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
