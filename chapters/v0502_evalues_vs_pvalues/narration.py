"""Narration for v0502_evalues_vs_pvalues — "E-values versus p-values".

Source: volumes/vol5_evalues/chapters/02_evalues_and_pvalues.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

Numbers are spelled out for the TTS engine.
"""

SCENES = {
    # S1 — what a p-value is
    "S1_Pvalue": [
        ("Before we bridge the two currencies of evidence, let us pin down the one you already know: the p-value.", 8.5),
        ("A p-value is a tail probability. It asks: if the null were true, how often would I see data this extreme, or worse?", 9.0),
        ("So p lives between zero and one, and small means surprising. Surprising data is evidence against nothing-going-on.", 8.5),
        ("The anchor we will lean on all chapter: under the null, a perfectly calibrated p-value is uniform on the interval zero to one.", 9.5),
        ("Uniform means every value is equally likely. So the chance that p falls at or below a level alpha is exactly alpha.", 9.0),
        ("That is the decision rule. Fix a level alpha, say zero point zero five, and reject the null whenever p is at most alpha.", 9.0),
        ("Uniformity is what guarantees the rule is safe: the false-positive rate is held at alpha, no more.", 8.5),
    ],
    # S2 — calibrators, both directions
    "S2_Calibrate": [
        ("Two languages, one bridge. We can convert an e-value into a p-value, and a p-value back into an e-value.", 8.5),
        ("Recall the e-value E: you stake one dollar against the null, the data play, and E is your payout. Under the null its average is at most one.", 10.0),
        ("Going from E to p is one line. Markov's inequality gives p equals the minimum of one and one over E. We unpack that next chapter-segment.", 9.5),
        ("Going the other way needs a calibrator: a function f that turns a p-value into an e-value, E equals f of p.", 9.0),
        ("A calibrator must be non-increasing, so small p pays a big E, and its area under uniform input must be at most one.", 9.5),
        ("In symbols: the integral of f of u, as u runs from zero to one, is at most one. That is the e-value property re-expressed for p-values.", 9.5),
        ("Here is one concrete calibrator, the smooth power family: E equals kappa times p to the power kappa minus one, for kappa between zero and one.", 9.5),
        ("Because kappa minus one is negative, the payout grows smoothly as p shrinks toward zero. Small p, big E, with no cliff.", 9.0),
        ("Check it: the integral of kappa times u to the kappa minus one, from zero to one, equals exactly one. A valid calibrator for every kappa.", 9.5),
    ],
    # S3 — 1/E as a conservative p-value
    "S3_Conservative": [
        ("Now the reverse trip, in detail. Define p as the minimum of one and one over E. This is always a valid p-value.", 9.0),
        ("Why valid? Markov says the chance that E reaches one over alpha is at most alpha. So rejecting when E is at least one over alpha is a level-alpha test.", 10.0),
        ("Reading that as a number: one over E is the cut-off. Any alpha at or above one over E rejects; below it, you do not. Cap it at one, since a probability cannot exceed one.", 10.5),
        ("But it is conservative. A perfectly calibrated p-value hits its bound with equality; this one under-reports its own significance.", 9.5),
        ("Watch it bite. A single point three null-standard-deviations out gives an e-value of about twelve point one eight.", 9.0),
        ("Translate: p equals the minimum of one and one over twelve point one eight, which is about zero point zero eight two. Not quite significant at five percent.", 9.5),
        ("Yet the exact normal p-value here is about zero point zero zero one three five. The e-value's verdict is sixty times more cautious.", 9.0),
        ("That gap is not a mistake. E-values pay for extra robustness: the conservative p stays valid even if the model is wrong, which the exact tail does not.", 10.0),
    ],
    # S4 — when each shines
    "S4_WhenEach": [
        ("So when do you reach for each currency? The honest answer is: it depends on the freedom you need.", 8.5),
        ("For a single, fixed, pre-registered test against a clean parametric null, the exact p-value is tight. It spends no power.", 9.0),
        ("There the e-value translation just leaves power on the table. The exact tail is the right tool.", 8.0),
        ("E-values shine the moment you want to peek. Under optional stopping, you can watch the evidence and halt whenever you like.", 9.0),
        ("They shine under optional continuation too: gather more data, keep betting, without spending a fresh error budget each look.", 9.0),
        ("And they shine when combining dependent evidence: bets multiply across cohorts where tail probabilities simply do not.", 9.0),
        ("State the trade plainly. P-values are sharp but rigid; e-values are a touch looser but they travel.", 8.5),
    ],
    # S5 — takeaway
    "S5_Takeaway": [
        ("Step back. We now hold two currencies for evidence, and one bridge between them.", 8.0),
        ("A p-value is a tail probability: surprise. An e-value is a wealth multiplier: evidence that composes.", 8.5),
        ("Markov runs the bridge one way, p equals the minimum of one and one over E; a calibrator runs it back, E equals f of p.", 9.5),
        ("The crossing is lossy, so do not round-trip casually. A calibrated p-value loses power when you e-value it and re-p-value it.", 9.5),
        ("The deal in one sentence: e-values trade a little power for the freedom to peek, stop, and combine without inflating error.", 9.5),
        ("That freedom is the whole point of the chapters to come, where wealth becomes a martingale you can watch, stop, and multiply.", 9.0),
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
