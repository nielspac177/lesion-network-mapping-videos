"""Narration for v0506_universal_inference — "Universal inference".

Source: volumes/vol5_evalues/chapters/06_universal_inference.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

All equations, numbers, and claims are quoted from the source chapter (result E6,
Wasserman, Ramdas and Balakrishnan, 2020). No invented constants.
"""

SCENES = {
    # S1 — When the null is hard
    "S1_Hard": [
        ("Every e-value so far came from a bet we already knew how to write down: a likelihood ratio between two fully specified distributions.", 9.5),
        ("But that needs you to name the alternative in advance. What if your null is not a tidy point hypothesis, but a model with parameters to estimate?", 9.5),
        ("The classical answer is the likelihood ratio test. Take the best free fit over the best null-allowed fit, then convert with a rule.", 9.0),
        ("The rule is Wilks' theorem: two log of the ratio is approximately chi-square distributed, under H-naught. That gives you a p-value.", 9.0),
        ("But that rule is a large-sample, well-behaved-model promise. It assumes the likelihood is smooth in theta, and the true theta is not on the edge.", 9.5),
        ("Break any of those and chi-square is the wrong reference. Mixtures, a variance pinned at the boundary, a constrained space: the table prints a number, just the wrong one.", 10.0),
        ("Think of chi-square as a conversion table printed for one engine. Mixtures and boundary nulls are different engines, and nothing warns you.", 9.0),
    ],
    # S2 — The split likelihood ratio
    "S2_SplitLR": [
        ("Universal inference sidesteps all of it with one move. Cut the data into two disjoint halves, D-naught and D-one.", 8.5),
        ("On D-one, fit the model however you like. Maximum likelihood, a Bayesian posterior mean, a neural net, even a coin flip. Get an estimate theta-hat-one.", 9.5),
        ("Now freeze it. Once D-one is fixed, theta-hat-one is just a number: a fixed alternative, chosen without ever peeking at D-naught.", 9.0),
        ("The split likelihood ratio U is one fraction. On top, the likelihood of the frozen alternative theta-hat-one, scored on the held-out half D-naught.", 9.5),
        ("On the bottom, the supremum over the null set: the best any null-allowed parameter can do, optimizing freely on that same scoring half.", 9.5),
        ("That asymmetry is the whole point. The alternative is frozen and cross-fitted; the null is given every advantage to optimize on the data we score on.", 9.5),
        ("In the casino language: you stake one dollar that the frozen alternative predicts the held-out data better than any null parameter can. U is the payout.", 9.5),
        ("Reject the null when U is at least one over alpha. A payout that large is rare enough under the null to be evidence at level alpha.", 9.0),
    ],
    # S3 — Always a valid e-value
    "S3_Valid": [
        ("Here is the claim. If the true distribution is in the null, then the expectation of U is at most one. So U is an e-value, full stop.", 9.5),
        ("The proof is short. We cannot reason about U directly because theta-hat-one is random, so we condition on D-one and freeze it.", 9.0),
        ("Because the halves are disjoint and the data are i-i-d, D-naught is independent of D-one. The scoring half is a fresh sample, untouched by the fitting.", 9.5),
        ("The null is true, so the true parameter theta-star lives in the null set. The supremum on the bottom can pick it, so the denominator is at least the likelihood at theta-star.", 10.5),
        ("Replace the denominator by that smaller quantity and U only goes up. Now it is a plain ratio of two fixed parameters: theta-one on top, the truth on the bottom.", 9.5),
        ("Take the conditional expectation. The true density in the denominator cancels the sampling density, leaving the integral of f-theta-one: a density, at most one.", 10.0),
        ("Finally the tower rule. The expectation of U is the expectation of its conditional expectation, which is at most one. Average over D-one and we are done.", 9.5),
        ("And notice what the proof never used. No smoothness, no interior point, no central limit theorem. That is why it is called universal: any model you can write.", 9.5),
    ],
    # S4 — The price
    "S4_Price": [
        ("Nothing is free. Universal inference spends data twice over, and the price has a name: sample-splitting.", 8.5),
        ("Half your patients fit the model and never vote on the evidence. The other half score the evidence and never improved the fit.", 9.0),
        ("The classical test uses every patient for both jobs. With N in the dozens, losing half to fitting can drop you below where any honest test had a chance.", 9.5),
        ("So the trade is honest but real. At small N the split test can be valid but underpowered to the point of uselessness. A modest effect may never push U past one over alpha.", 10.5),
        ("Validity is free; power you have to earn. A bad estimator, or a wastefully small fitting half, gives a valid but feeble bet that rarely clears the threshold.", 9.5),
        ("There is some relief. Run the split both ways, fit on each half and score on the other, then average the two payouts. The average of e-values is an e-value.", 9.5),
        ("But the splits share a partition, so they are dependent. You must average, never multiply. Multiplying dependent e-values can blow past one and silently invalidate the test.", 10.0),
    ],
    # S5 — Why it is remarkable
    "S5_Use": [
        ("Step back and see what we bought. A single recipe turns any likelihood model into a valid e-value, where nothing else works.", 9.0),
        ("Testing k components against k plus one in a mixture is a notorious irregularity: the extra component is unidentified and Wilks fails. The split test just works.", 9.5),
        ("Boundary and constrained nulls: a variance pinned at zero, an ordered parameter, a one-sided test at the edge. The constrained supremum handles it honestly.", 9.5),
        ("Or any model where you can compute a likelihood but cannot prove regularity. You still get a valid e-value, exact at finite sample size.", 9.0),
        ("The one e-value it mints drops straight into the machinery we built: one input to e-B-H across a sweep, one summand when accumulating across cohorts.", 9.5),
        ("But it fixes irregularity, not confounding. A valid e-value of the wrong null is worthless: if lesion size confounds the effect, U faithfully measures the wrong question.", 10.0),
        ("So the lesson is sharp. Validity of the bet is one thing; validity of the question is another. Universal inference guarantees the first, and only the first.", 9.5),
        ("That is the remarkable part. For messy, irregular, real-world models, one recipe extends honest inference to exactly the cases where the textbook table lies.", 9.5),
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
