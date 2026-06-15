"""Narration for v0501_what_is_an_evalue — "What is an e-value".

Source: volumes/vol5_evalues/chapters/01_what_is_an_evalue.md
        volumes/vol5_evalues/VOLUME.md

The e-value of testing-by-betting (Shafer, Vovk, Ramdas, Wang, Grunwald):
the realized payout of a one-dollar bet rigged to be fair against the null.
NOT the causal-inference E-value of VanderWeele and Ding.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — evidence as betting: the casino picture
    "S1_Betting": [
        ("Forget brains for a second. Picture a bet against a null hypothesis, the claim that nothing is going on.", 8.5),
        ("You walk up and stake one dollar. The data come in. A number, capital E, comes out, and that is your payout.", 8.5),
        ("If E is three, you tripled your money. If E is zero point two, you lost most of it. If E is zero, you are wiped out.", 8.5),
        ("Two rules make this a fair bet. Rule one: you can never owe money. The payout E is never negative.", 8.0),
        ("Rule two: if the null is true, you cannot profit on average. Averaged over the null, the payout is at most the one dollar you staked.", 9.5),
        ("That average is the expectation under the null, written E-sub-H-naught of E, the long-run payout if nothing were going on.", 9.0),
        ("Now flip the logic. If you walk away with forty dollars, the rigged-fair game says that should not happen under the null.", 9.0),
        ("So a big payout is evidence against the null, and the size of the payout is the strength of that evidence.", 8.0),
    ],
    # S2 — the formal definition
    "S2_Definition": [
        ("Now the formal track. Every symbol below is a piece of the bet we just described.", 7.5),
        ("First, the null. H-naught is not one distribution but a set of them: every distribution P under which nothing is going on.", 9.0),
        ("The data is a random object, capital X. The payout is a function of that data, the random variable E equals E of X.", 8.5),
        ("An e-variable is that payout E of X, required to be greater than or equal to zero. Rule one, never owe money.", 8.5),
        ("And its expectation under the null is at most one: E-sub-P of E is less than or equal to one, for every distribution P in the null.", 9.5),
        ("Note it is less than or equal to one, not exactly one. A conservative bet that leaves money on the table is still valid.", 9.0),
        ("And the constraint binds only under the null. Under the alternative the average can, and should, blow past one.", 8.5),
        ("A realized value of E on observed data is called an e-value. Big E means surprising under the null: evidence against it.", 9.0),
    ],
    # S3 — Markov gives validity
    "S3_Markov": [
        ("Why is the rule about the average enough? Because a non-negative quantity with a small average cannot be large very often.", 9.0),
        ("The tool that makes this exact is Markov's inequality. Let me walk the one line, defining each symbol first.", 8.0),
        ("Let c be the threshold, a fixed positive number. And let the indicator, one-bracket E greater than c, be one when the payout clears c, else zero.", 9.5),
        ("Step one, the flooring inequality: E is greater than or equal to c times that indicator. True outcome by outcome, using E non-negative.", 9.5),
        ("Step two, take expectations of both sides. The average of E is at least c times the probability that E reaches c.", 9.0),
        ("Step three, divide by c and use the e-value rule. The null probability that E is at least c is at most one over c.", 9.5),
        ("Now set the threshold c equal to one over alpha. Then the null probability that E reaches one-over-alpha is at most alpha.", 9.0),
        ("So rejecting when E is at least one-over-alpha is a valid level-alpha test. For a five percent test, reject when your dollar grew to twenty.", 9.5),
    ],
    # S4 — the likelihood-ratio e-value
    "S4_LR": [
        ("Where do actual e-variables come from? The cleanest source, the one everything traces back to, is a likelihood ratio.", 8.5),
        ("The null says the data come from a density p. You have a rival in mind, an alternative density q, that you think fits better.", 9.0),
        ("Your bet is E equals q of X over p of X: how likely the observed data is under your rival, divided by under the null.", 9.0),
        ("If the data look much more like q than p, the ratio is big and you cash in. If they look like p, the ratio is small and you lose.", 9.5),
        ("Why is this fair under the null? Because when p is the truth, the average of q over p is exactly one. Watch the cancellation.", 9.0),
        ("The expectation under the null integrates q over p, times p, over all x. The p in the denominator cancels the p weight.", 9.0),
        ("What is left is the integral of q over all outcomes, which is one because q is a probability density. Exactly one, no slack.", 9.0),
        ("So the likelihood ratio is an e-value automatically, by the structure of integration. E-values are likelihood ratios in disguise.", 8.5),
    ],
    # S5 — reading an e-value
    "S5_Reading": [
        ("So how do you read an e-value? Suppose you played and walked away with E equals twenty. Your dollar became twenty dollars.", 8.5),
        ("The bet was rigged so that under the null you have no business making that kind of money. So twenty is strong evidence.", 9.0),
        ("The scale is direct. One dollar means you learned nothing. Twenty is this null is in trouble. Forty is in serious trouble.", 9.0),
        ("This is what a p-value never quite gives you: the payout is the evidence, in one number you can read off directly.", 8.5),
        ("And unlike a p-value, an e-value is a measure of accrued evidence you can keep multiplying as more data arrive.", 8.5),
        ("Flip a biased coin again, multiply the new ratio onto the old. Ten heads in a row compounds to about fifty-seven point seven.", 8.5),
        ("That multiplication is honest. Peek whenever you like, stop whenever the evidence is strong, with no penalty for looking.", 8.5),
        ("That property, optional stopping, is where the real power lives, and it is exactly what the next chapter builds.", 8.0),
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
