"""Narration for v0605_risk_control — "Conformal risk control".

Source: volumes/vol6_conformal/chapters/05_risk_control.md
        (Angelopoulos, Bates, Fisch, Lei & Schuster, "Conformal Risk Control,"
         ICLR 2024, arXiv:2208.02814.)

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

Numbers are spelled for TTS. lambda-hat is read as "lambda-hat", alpha as
"alpha", and so on. The chapter's source uses beta for the ceiling in its worked
example; we keep the source's alpha-level framing in the title cards but speak
the symbol as it appears on screen.
"""

SCENES = {
    # S1 — Beyond miscoverage: from a 0/1 coverage loss to any monotone loss
    "S1_Beyond": [
        ("Every guarantee so far in this volume has been about coverage: does the true label land inside the prediction set?",
         8.5),
        ("Coverage is secretly a zero-one loss. You pay one when the truth falls outside the set, and zero when it is inside.",
         9.0),
        ("But the clinic does not ask for a set. It asks for a flag, a yes or no decision, and the two ways of being wrong are not equal.",
         9.5),
        ("Missing a real adverse event is far worse than a false alarm. Coverage treats both errors as one currency. The clinic does not.",
         9.0),
        ("So we generalize. Replace the zero-one coverage loss with any loss we care about, and aim to control its expected value.",
         9.0),
        ("Our running example is the false-negative rate in a multilabel flag: of all patients who truly have the event, what fraction do we miss?",
         9.5),
        ("We will pick a procedure that holds that expected miss rate below a level we choose, call it alpha, no matter which model we used.",
         9.5),
    ],
    # S2 — The risk function R(lambda)
    "S2_RiskFn": [
        ("To control a loss we first need a knob to turn. Here it is a single threshold, lambda, living between zero and one.",
         8.5),
        ("The flag rule is simple. T sub lambda of x equals one, flagged, when the model's predicted risk p-hat of x is at least lambda; otherwise zero.",
         9.5),
        ("Slide lambda down toward zero and you flag more people. Slide it up toward one and you flag fewer.",
         8.0),
        ("The loss L sub lambda is one exactly when a patient truly had the event, y equals one, but we failed to flag them, p-hat below lambda.",
         9.5),
        ("Averaged over the true-positive patients, that indicator is precisely the false-negative rate.",
         7.5),
        ("The risk R of lambda is just the expected loss: R of lambda equals the expectation of L sub lambda over a random patient.",
         8.5),
        ("Now the one property everything hangs on. Raise lambda, you flag fewer, so you miss more, or the same, never fewer.",
         9.0),
        ("So the loss is non-decreasing in lambda for every fixed patient, and therefore R of lambda is a monotone, non-decreasing function.",
         9.0),
    ],
    # S3 — Calibrating the threshold
    "S3_Calibrate": [
        ("We have n calibration patients, each with the truth and an out-of-fold predicted risk p-hat. Now we pick the threshold.",
         8.5),
        ("Start with the empirical risk: R-hat-n of lambda is the average of the loss over the n calibration patients.",
         8.5),
        ("As lambda rises, this empirical miss rate climbs. We want the largest, strictest lambda whose risk we can still certify safe.",
         9.0),
        ("But the empirical rate is a noisy estimate. If we stop where it just equals alpha, we overshoot by chance about half the time.",
         9.0),
        ("So conformal risk control, due to Angelopoulos and colleagues, adds a finite-sample cushion that shrinks like one over n.",
         9.0),
        ("The rule: lambda-hat is the supremum over lambda such that R-hat-n of lambda is at most alpha minus the quantity one minus alpha over n.",
         10.0),
        ("That cushion, one minus alpha over n, is the whole price of honesty. At ten patients it is real; at a hundred it nearly vanishes.",
         9.5),
        ("Drop the cushion and you tune the threshold to your calibration noise. Your reported miss rate sits at alpha while the true one drifts above it.",
         9.5),
    ],
    # S4 — The guarantee
    "S4_Guarantee": [
        ("Here is what the cushion buys you. The guarantee is a clean statement about the next, unseen patient.",
         8.0),
        ("Assume the calibration patients and the test patient are exchangeable: interchangeable in order, the only assumption beyond a monotone loss.",
         9.5),
        ("Then the expected loss at the selected threshold, on a fresh point, the expectation of L at lambda-hat for patient n plus one, is at most alpha.",
         10.0),
        ("The expectation runs over both the calibration draw and the new patient. The cushion absorbs the one-patient slack from not knowing the true risk.",
         9.5),
        ("That is why the bound is tight to order one over n: you cannot do better than alpha plus order one over n, and you never do worse than alpha.",
         9.5),
        ("There is no distributional assumption. Any base model p-hat works, and it holds at the actual n you have, not asymptotically.",
         9.0),
        ("And coverage is just the special case. Let the loss be the miscoverage indicator, one when the truth falls outside the set.",
         9.0),
        ("Then controlling its expectation at alpha is exactly the statement that the set covers the truth at least one minus alpha of the time.",
         9.0),
    ],
    # S5 — Example: FNR control
    "S5_FNR": [
        ("Let us land it on a number. We control the false-negative rate of a multilabel flag for gait ataxia after thalamotomy.",
         9.0),
        ("Ten patients truly had the event. Sorted, their out-of-fold predicted risks run from zero-point-one-two up to zero-point-nine-zero.",
         9.0),
        ("Choose alpha equals zero-point-two: we are willing to miss at most twenty percent of true events in expectation.",
         8.5),
        ("The cushion is one minus zero-point-two over ten, which is zero-point-zero-eight. So the conservative target is zero-point-two minus zero-point-zero-eight, zero-point-one-two.",
         10.0),
        ("With ten patients each miss is worth zero-point-one, so a target of zero-point-one-two means we may miss at most one true event.",
         9.0),
        ("Sweep lambda upward. The strictest threshold missing just one patient is zero-point-two-one, the second-smallest score.",
         9.0),
        ("So lambda-hat is zero-point-two-one. Flag any patient whose model risk is at least zero-point-two-one as high-risk for the adverse event.",
         9.5),
        ("As the ceiling tightens, the threshold drops to catch more people; the set of flagged patients grows to meet the lower miss rate. That closes the chapter.",
         10.0),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:16s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':16s} target={grand:5.1f}s ({grand/60:.1f} min)")
