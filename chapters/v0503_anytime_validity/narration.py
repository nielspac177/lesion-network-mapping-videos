"""Narration for v0503_anytime_validity — "Anytime validity and optional stopping".

Source: volumes/vol5_evalues/chapters/03_anytime_validity.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

Numbers are written as words for the TTS engine.
"""

SCENES = {
    # S1 — the peeking problem
    "S1_Problem": [
        ("A classical test is computed once, at a sample size you fixed in advance. That single commitment is its whole guarantee.", 9.0),
        ("But evidence rarely arrives all at once. Patients accrue over years, a few per operating list, and you want to look as it builds.", 9.5),
        ("So you peek. You compute a fresh p-value after twenty patients, then after forty, then after sixty, and you stop the moment it dips below alpha.", 10.0),
        ("Here alpha is your allowed false-positive rate, the line a true null should rarely cross. Say alpha equals zero-point-zero-five.", 9.0),
        ("The trouble: each peek is a fresh chance to cross that line by luck. Three looks roughly triple the chance of a spurious crossing.", 9.5),
        ("So the running p-value sinks under alpha not because the null is false, but because you gave randomness three rolls of the dice.", 9.5),
        ("Classical inference breaks if you peek and stop early. The real error rate balloons well above the alpha you promised.", 9.0),
        ("This chapter gives the opposite guarantee. There is an object you may watch continuously, and stop the instant it is convincing.", 9.0),
    ],
    # S2 — e-processes / test martingales
    "S2_EProcess": [
        ("The fix is to stop computing p-values and start betting. Walk into a casino with one dollar; the null says the coin is fair.", 9.5),
        ("At round t you place a bet, a non-negative multiplier B sub t applied to your current pile. Here t indexes the rounds: one, two, three.", 9.5),
        ("Bet your whole pile each round, so your wealth E sub t is the running product of every multiplier so far, starting from one dollar.", 9.5),
        ("That product, E sub t equals the product over s of B sub s, is the e-process. E sub t is your wealth, a valid e-value at every time t.", 10.0),
        ("Each bet must be fair under the null, but fair given what you already know: the conditional expectation of B sub t given the past is at most one.", 10.0),
        ("F sub t minus one is that past, the entire record of data seen through the previous round, the information you have accumulated.", 9.0),
        ("So whatever you have seen, your next bet cannot grow your money on average if the null is true. You may adapt cleverly, but never escape fairness.", 10.0),
        ("Multiply conditionally-fair bets and the whole trajectory stays fair: the expectation of E sub t is at most one, at every single time t.", 9.5),
    ],
    # S3 — Ville's inequality
    "S3_Ville": [
        ("One fixed peek is easy: Markov says a large wealth at a single time t is rare. But we want to watch every round and still be safe.", 9.5),
        ("Ville's inequality delivers exactly that. It controls not one slice of the wealth, but its entire history at once.", 9.0),
        ("It needs a non-negative supermartingale starting at one. A supermartingale is a game whose expected next value is no larger than its current value.", 10.0),
        ("That is precisely our wealth: each bet is only break-even or worse under the null, so on average the pile never grows. And every bet is non-negative.", 10.0),
        ("Ville then says: the probability that there exists a time t at which E sub t reaches one over alpha is at most alpha.", 9.5),
        ("Read the quantifier carefully. There exists a t means ever, at any round in the whole sequence, not at one moment you fixed beforehand.", 9.5),
        ("The chance of ever getting twenty-fold rich, betting against a true null, is at most one over twenty, five percent. The supremum over all time.", 10.0),
        ("That is the anytime guarantee: the running maximum is bounded by the same constant alpha that would bound a single peek.", 9.0),
    ],
    # S4 — optional stopping is safe
    "S4_Stop": [
        ("Because the bound holds simultaneously for all t, you are free to stop whenever you like. Here is the procedure you actually run.", 9.0),
        ("Fix alpha before you start, so the threshold is one over alpha, say twenty. Begin with wealth one, and update by multiplying in each fair bet.", 10.0),
        ("Reject the null the first time the wealth E sub t reaches one over alpha. This is a data-dependent stopping time: a moment you choose by watching.", 10.0),
        ("Otherwise keep watching. You may quit for any reason at all, funding ends, the cohort closes, you got bored, and still control your error.", 9.5),
        ("Ville guarantees the chance you ever hit the threshold is at most alpha, so rejecting at the first crossing has type-one error at most alpha.", 10.0),
        ("Contrast the p-value disaster. Reuse the zero-point-zero-five cutoff at three interim looks and the chance of crossing somewhere is roughly three times higher.", 10.0),
        ("That is classic alpha inflation, the reason trials need pre-registered spending rules just to peek legally. The martingale builds the freedom in.", 9.5),
        ("You are not committing to a sample size, and you are not paying a peeking tax. That is what anytime-validity means.", 8.5),
    ],
    # S5 — why it matters
    "S5_Meaning": [
        ("Step back and see what we bought. Anytime-valid inference lets you monitor evidence continuously, look after every patient, and stop on a dime.", 10.0),
        ("Stop on success when the wealth crosses one over alpha, declaring the effect real. Or stop on futility when accrual ends and report the wealth you reached.", 10.0),
        ("Either way the number is a calibrated measure of evidence. No pre-committed sample size, no penalty for having looked along the way.", 9.5),
        ("And notice where the validity comes from. Not from a fixed sample size, but from the martingale structure: conditionally-fair bets multiplied through time.", 10.0),
        ("The hinge is non-negativity. Drop the requirement that each bet B sub t is non-negative and Ville fails outright; that is why e-values are non-negative by definition.", 10.0),
        ("The cost is power, not validity. A bet hedging many alternatives grows slower than a fixed-n test tuned to the truth. Validity is free; you trade efficiency.", 10.0),
        ("One caution: the martingale is only valid for the null its bets are fair against. A confounder ignored means accumulating evidence against the wrong null.", 9.5),
        ("Fix confounding in the design, then ride the martingale on top. For a slowly-accruing surgical cohort, this is the honest way to monitor.", 9.0),
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
