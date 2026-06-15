"""Narration for v0507_recipe_and_limits — "E-values: recipe and limits".

Source: volumes/vol5_evalues/chapters/07_recipe_and_limits.md  (Results E7, E8)

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

Numbers are spelled for TTS. All quantities are quoted from the chapter:
the calibrator e equals kappa p to the kappa minus one, the e-BH threshold
m over alpha k, the worked m equals five sweep with alpha zero-point-zero-five,
the FDR-inflation example summing to zero-point-zero-six, and the three fences.
"""

SCENES = {
    # S1 — the end-to-end recipe (E8): one flow diagram
    "S1_Recipe": [
        ("We have built every piece. This chapter bolts them into one recipe, then draws the fences where an e-value must not be used.", 9.0),
        ("Step one: mint. For each analysis cell you produce one e-value, a single number that says how much you'd have won betting against this network being noise.", 10.5),
        ("Two roads mint it. If a cell has a permutation p-value, calibrate: e sub i equals kappa times p sub i to the power kappa minus one, which integrates to one over a uniform p.", 11.0),
        ("If a cell has a real likelihood, skip the p-value and use the split likelihood-ratio of universal inference. Either road gives the same shape: a non-negative number with null-expectation at most one.", 11.0),
        ("Step two: adjudicate the whole table at once. Hand the column of e-values to e-BH, which rejects the strongest cells while holding the false-discovery rate at alpha, under any dependence.", 11.0),
        ("Step three: pool across sites and time. Independent cohorts multiply. Shared or adversarial ones average. A live, accruing cohort is a martingale, so by Ville you can stop the moment it's convincing.", 11.0),
        ("Step four: report alongside the family-wise maps, never instead of them. The e-value layer is the across-analyses accountant; the within-map test is still the referee.", 10.0),
        ("None of this is new mathematics. It is the calibrator, e-BH, products, averages, and the martingale, simply composed into one pipeline.", 9.0),
    ],
    # S2 — when e-values are worth it
    "S2_WhenWorth": [
        ("So when is the e-value layer worth its cost? Three situations, and one where it is not.", 8.0),
        ("Worth it when you need optional stopping. The running product is a test martingale, so you may peek as the cohort trickles in and stop the instant it clears one over alpha.", 10.0),
        ("Worth it when you need dependence-robust multiple testing. e-BH controls the false-discovery rate under arbitrary dependence, exactly the tangled sweep of overlapping patients and correlated voxels.", 11.0),
        ("Worth it when the null is composite, or has no regularity conditions. Universal inference mints a valid e-value from a likelihood with no asymptotics required.", 9.5),
        ("In our worked five-cell sweep, e-BH at alpha zero-point-zero-five rejected nothing, while plain Benjamini-Hochberg on the raw p-values rejected cells one and two.", 10.0),
        ("That gap is the premium. e-BH pays for needing no dependence assumption with a more conservative threshold.", 8.5),
        ("So it is not worth the power loss for a single, fixed, clean test with a defensible independence assumption. There, reach for the ordinary p-value.", 9.5),
    ],
    # S3 — the power cost (calibrator intuition)
    "S3_Limit_power": [
        ("Now the first honest limit. An e-value is typically less powerful than the optimal fixed-sample p-value. Let's see why, from the calibrator.", 9.5),
        ("A calibrator is a non-increasing function f from the unit interval to the non-negatives, whose integral over a uniform p is at most one.", 9.0),
        ("That integral constraint is a budget. To stay an honest e-value, f cannot be large everywhere; what it spends on small p-values it must save elsewhere.", 10.0),
        ("Take the workhorse, f of p equals kappa times p to the kappa minus one. With kappa one-half, a p-value of zero-point-zero-four becomes an e-value of only two-point-five.", 10.0),
        ("Two-point-five is real evidence, but it is a softer statement than the p-value zero-point-zero-four was. The conversion deliberately gives ground.", 9.0),
        ("And you must pick kappa before looking. Tuning it to maximize your e-value after the fact breaks the integral bound, the very thing that made it valid.", 9.5),
        ("So the power cost is the price of two gifts: you may stop whenever you like, and you may combine across anything. For a single clean test you don't need those gifts.", 10.5),
    ],
    # S4 — a wrong null still misleads
    "S4_Limit_wrongnull": [
        ("The second limit is the recurring lesson of this whole series, now in e-value form. A valid e-value of the wrong null is still the wrong question.", 9.5),
        ("The defining property is conditional. The expectation of E under P is at most one, for every P in the null H-zero. It promises nothing about whether H-zero is the right null.", 10.5),
        ("Suppose lesion size confounds the ataxia effect, and you mint an e-value whose null ignores size. The machinery works flawlessly; the expectation bound holds under that null.", 10.5),
        ("You get a big E and declare a discovery. But a big E here only says the data are surprising if the network is noise and size doesn't matter.", 9.5),
        ("And the data are surprising, because size matters. You have faithfully measured strong evidence against a strawman. The e-value did its job and told you nothing about ataxia.", 10.0),
        ("Validity and correctness are independent promises. You can have a perfectly valid e-value of a useless null: the arithmetic is right, but the books are cooked.", 9.5),
        ("The fix lives upstream, in the design matrix and Freedman-Lane. Put size in the model, permute under the partial null. The e-value inherits whatever the null already encodes; it adds none of its own.", 11.0),
        ("Worse still, if you mis-specify the null as a probability object, even the expectation bound can fail, and then e-BH, Ville, and Markov all snap at that one step.", 10.5),
    ],
    # S5 — closing
    "S5_Close": [
        ("So let us close. E-values are a robust, composable currency for evidence: one common shape that calibrators, products, averages, and e-BH all accept.", 9.5),
        ("Their guarantees are real. Anytime-validity lets you peek; e-BH controls the false-discovery rate under any dependence; universal inference needs no regularity.", 10.0),
        ("But every one of those guarantees is a corollary of a single inequality: under the null, the expected payout is at most one.", 9.0),
        ("Spend your skepticism there, on each cell's null. The combiners are bookkeeping; they cannot manufacture a guarantee the input null doesn't have.", 9.0),
        ("E-values do not rescue a bad question. A valid bet against the wrong null is worthless, however cleverly you combine it.", 9.0),
        ("What they do give is honest sequential and multiple inference: a way to stop when convinced, and to weigh many analyses, without lying about the evidence.", 10.0),
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
