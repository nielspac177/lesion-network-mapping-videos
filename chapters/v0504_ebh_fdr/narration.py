"""Narration for v0504_ebh_fdr — "E-values for FDR: the e-BH procedure".

Source: volumes/vol5_evalues/chapters/04_ebh_fdr.md
        (Wang & Ramdas, JRSS-B 84(3):822-852, 2022; doi:10.1111/rssb.12489;
         arXiv:2009.02824)

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — many tests at once; define FDR
    "S1_Multiple": [
        ("CircuitPyPer never runs one analysis. It runs a sweep: every adverse event, every timepoint, every model spec is its own whole-brain map, its own test.", 10.0),
        ("So we have m hypotheses, and for each one an e-value. Call them E sub one through E sub m, one number per cell of the sweep.", 9.0),
        ("Recall what an e-value is. It is a non-negative score whose expectation under its own null is at most one. Big e-value means strong evidence against that null.", 10.0),
        ("Run forty maps, declare the impressive ones real, and some fraction of those discoveries are noise. The false discovery proportion is that fraction.", 9.5),
        ("Written out: the F D P is the number of discoveries that are actually null, divided by the number of discoveries you made.", 8.5),
        ("But you never get told which discoveries were flukes. So you cannot see the F D P. Instead you control its average over reruns of the sweep.", 9.5),
        ("That average is the false discovery rate. F D R is the expected F D P. Targeting F D R at most five percent means, on average, no more than five percent of your calls are false.", 10.5),
        ("This is looser than family-wise error, which forbids even one false positive. For a sweep of dozens of maps, F D R is the right currency: tolerate a few liars, keep the slice small.", 10.5),
    ],
    # S2 — the e-BH procedure
    "S2_eBH": [
        ("Here is e-B-H, the e-value version of Benjamini-Hochberg. One threshold, applied to the whole pile of e-values.", 9.0),
        ("Step one: sort the e-values in descending order. Biggest evidence first. We write E in parentheses k for the k-th largest.", 9.0),
        ("Step two: find the cutoff rank. Walk down the sorted list and find the largest rank k whose e-value still clears a rising bar.", 9.5),
        ("That bar is m divided by alpha times k. So k-star is the largest k with E in parentheses k at least m over alpha k. If none clears, k-star is zero.", 10.0),
        ("Step three: reject the top k-star. Declare the k-star analyses with the largest e-values to be your discoveries. One sort, one threshold.", 9.5),
        ("Read the bar as a price of admission. At rank one the bar is m over alpha: with forty maps at alpha five percent, that is eight hundred. A lone discovery must be overwhelming.", 10.5),
        ("But admit twenty members and the bar per member drops to m over alpha times twenty, just forty. A big club shares the burden of proof.", 9.5),
        ("Now compare to plain B-H on p-values. There small is good: sort ascending, and the bar alpha k over m grows with k. Note that one over E is a cautious p-value, so e-B-H is the exact mirror, running on one over E.", 11.0),
    ],
    # S3 — the FDR guarantee under any dependence
    "S3_Guarantee": [
        ("Now the payoff, and it is the e-value superpower. e-B-H controls the F D R at alpha for arbitrary dependence between the e-values.", 9.5),
        ("State it carefully. Let E one through E m be e-values: each non-negative, each with expectation at most one under its own null hypothesis.", 9.5),
        ("Run e-B-H at level alpha. Reject the top k-star, the largest k with E in parentheses k at least m over alpha k.", 9.0),
        ("Then the F D R is at most alpha over m times the sum, over the truly null hypotheses, of their expected e-values, which is itself at most alpha.", 10.0),
        ("And here is the load-bearing phrase: with no assumption on the joint dependence of the e-values. None.", 8.5),
        ("Voxels bleed into their neighbors. The three-month map and the twelve-month map share patients. Two models share data. e-B-H does not care.", 9.5),
        ("This is the Wang and Ramdas theorem, from the Journal of the Royal Statistical Society, twenty twenty-two. Plain B-H cannot promise this without a positive-dependence assumption you often cannot defend.", 10.5),
    ],
    # S4 — why dependence is free
    "S4_Why": [
        ("Why is dependence free? Because the guarantee rides on linearity of expectation, not on independence. Let me walk the argument at altitude.", 9.5),
        ("Move one: the rejection rule never rejects a cheap e-value. If hypothesis i is rejected, it sat among the top k-star, so its e-value cleared the rank k-star bar.", 10.5),
        ("That gives, for every rejected i, E sub i at least m over alpha times the number of rejections R. Flip it: one over R is at most alpha over m times E sub i.", 10.5),
        ("Move two: each true-null rejection contributes one over R to the F D P. Trade that one over R for alpha over m times E sub i, and sum over the true nulls.", 10.0),
        ("So the F D P is at most alpha over m times the sum of true-null e-values. Notice the coefficient alpha over m is a fixed constant, not random.", 9.5),
        ("Move three: take the expectation of both sides. Expectation is linear, always. It splits a sum into a sum of expectations no matter how the terms are correlated.", 10.0),
        ("This is the exact place where dependence would have killed a p-value argument, and where it simply does not enter. Linearity never needs independence.", 9.5),
        ("Then use the one fact every e-value has: expectation at most one under its null. Each term is at most one, there are at most m of them, and alpha over m times m is alpha. Done.", 10.5),
    ],
    # S5 — where this helps
    "S5_Use": [
        ("Where does this help? Voxelwise brain-map testing is massively dependent, and that is precisely the setting e-B-H was built for.", 9.0),
        ("The code-review audit flagged it as finding D-three: the batch pipeline tests timepoint by adverse-event by model as separate maps, and nothing controls error across them.", 10.5),
        ("Per-map control already exists. The max-stat permutation method of Volume four asks: is there a false positive anywhere in this one map? That is within-map family-wise error.", 10.0),
        ("e-B-H sits on top and asks a different question: of all the maps I called real, what fraction are false? Across-sweep F D R. You want both layers.", 10.0),
        ("And the maps are wildly dependent: overlapping cohorts, autocorrelated voxels, shared data. Plain B-H would need a positive-dependence claim you cannot honestly defend here.", 10.0),
        ("Because the e-B-H proof never used a dependence assumption, that whole worry is off the table. Mint one e-value per cell, run e-B-H, get an F D R-controlled subset.", 10.5),
        ("Two honest caveats. e-B-H is conservative; it buys robustness with power, and can reject nothing where B-H would flag a cell. And it is only as good as the null behind each e-value, so adjust for confounders like lesion size.", 11.5),
        ("That closes the loop. One e-value at a time built the bet; e-B-H takes the whole pile and hands back an honest, dependence-proof slice of discoveries. That is the across-the-sweep knob the series needed.", 11.0),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:18s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':18s} target={grand:5.1f}s ({grand/60:.1f} min)")
