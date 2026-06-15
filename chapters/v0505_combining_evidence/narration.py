"""Narration for v0505_combining_evidence — "Combining evidence".

Source: volumes/vol5_evalues/chapters/05_combining_evidence.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

All equations, numbers, and claims are quoted from the source chapter. Numbers
are spelled out for the text-to-speech engine.
"""

SCENES = {
    # S1 — the goal: pool many studies into one e-value
    "S1_Goal": [
        ("You ran the same analysis in two cohorts. How do you fold the evidence into a single number?", 8.5),
        ("Toronto maps an adverse-event network and hands you one e-value. Seoul runs the same analysis and hands you another.", 9.0),
        ("Recall what an e-value is: a bet against the null. Under the null its expectation is at most one, so it cannot grow your dollar on average.", 9.5),
        ("A payout of twenty means you twentupled your stake betting against nothing's going on. Big payout, strong evidence.", 8.5),
        ("So name the inputs. We have K studies, each minting an e-value: E sub one, E sub two, up to E sub K.", 8.5),
        ("Every E sub i is non-negative and, under any null distribution P, has expectation at most one. That is the only property we will use.", 9.5),
        ("The whole chapter is one fork. Combine them by multiplying, or by averaging, and which one depends entirely on independence.", 9.0),
    ],
    # S2 — the product: independent e-values multiply
    "S2_Product": [
        ("First the product. If the studies are genuinely separate, you re-bet the whole pot. Win four in Toronto, carry all four to Seoul.", 9.5),
        ("The claim: for independent e-values, the product E sub one times E sub two up to E sub K is again an e-value.", 9.0),
        ("Independent under the null means the joint distribution factorizes. Knowing E sub one tells you nothing about E sub two.", 9.0),
        ("That is exactly what separate cohorts give you: different patients, different scanners, no shared data, no shared peeking.", 9.0),
        ("Step one uses independence and nothing else. The expectation of the product splits into the product of the expectations.", 9.0),
        ("Step two: each factor is an e-value, so its expectation under P is at most one.", 7.5),
        ("Step three: a product of numbers each at most one, and all non-negative, is itself at most one. So the product is a valid e-value.", 9.5),
        ("Make it concrete. Toronto gives four, Seoul gives six. Multiply to twenty-four. A cautious p-value of one over twenty-four, about zero point zero four two.", 10.0),
        ("And notice: this running product is exactly the test martingale from chapter three. Multiply across sites, peek across time, same object.", 9.5),
    ],
    # S3 — the average: arbitrary dependence
    "S3_Average": [
        ("But the product is only as honest as the independence claim. If Seoul re-used Toronto's patients, multiplying parlays the same fluke twice.", 9.5),
        ("Here is the failure, made arithmetic. Let E equal four with probability one quarter, else zero. Its mean is one, a valid e-value.", 9.5),
        ("But E squared is sixteen one quarter of the time, so its expectation is four, strictly above one. The product is no longer an e-value.", 9.5),
        ("So when dependence might lurk, split your stake instead. The average, one over K times the sum of the E sub i, is always safe.", 9.5),
        ("The proof needs one word: linearity. The expectation of a sum is the sum of expectations, for any variables, dependent or not.", 9.0),
        ("Push expectation through the sum, bound each term by one, and the average of bounds is at most one. No independence anywhere.", 9.0),
        ("With four and six the average is five, versus the product's twenty-four. Always between the inputs, never above the maximum.", 9.0),
        ("That is the trade. The average refuses to ever be fooled, but it cannot reward genuine replication the way a legitimate parlay does.", 9.0),
    ],
    # S4 — product vs average tradeoff
    "S4_Tradeoff": [
        ("Set the two combiners side by side. They answer the same question with opposite temperaments.", 8.0),
        ("The product is powerful. Two independent positives compound, and twenty-four is replication doing real work.", 8.5),
        ("But it is fragile. It needs independence, and the moment that fails, the product can overstate the evidence badly.", 8.5),
        ("The average is robust. It stays a valid e-value under any dependence at all, even adversarially chosen inputs.", 8.5),
        ("But it is conservative. Averaging never beats a legitimate parlay; it throws away the compounding to buy safety.", 8.5),
        ("So the rule. Separate cohorts, no shared patients, no shared peeking: multiply, for clean replication.", 8.5),
        ("Any doubt about shared data or adversarial selection: average. When you are unsure, average. It is never wrong, only cautious.", 9.0),
    ],
    # S5 — merging is closed, the takeaway of the volume
    "S5_Merge": [
        ("Step back. What we have built is a closed, composable calculus of evidence.", 7.5),
        ("Both combiners take e-values in and return an e-value out. The output is the same kind of object as the inputs.", 9.0),
        ("So you can keep going. Combine Toronto and Seoul, then fold in Boston, then next year's cohort. The chain never leaves the family.", 9.5),
        ("And across time it is the same move. The running product is the test martingale, so Ville's inequality and safe peeking come for free.", 9.5),
        ("P-values cannot be merged this freely. There is no running-product structure to ride, no clean way to pool under dependence.", 9.0),
        ("One guardrail: a combiner is only as good as the shared null underneath it. Multiplying e-values for different claims answers neither.", 9.5),
        ("And report these alongside the within-map permutation maps from volume four, never instead of them. The two layers are orthogonal.", 9.0),
        ("That is the takeaway of the volume. E-values compose; evidence accumulates; and the average is the number you can never get wrong.", 9.0),
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
