"""Narration for v0607_recipe — "Conformal prediction: the recipe".

Source: volumes/vol6_conformal/chapters/07_recipe.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the recipe: the whole workflow in one flow
    "S1_Recipe": [
        ("Six chapters built the parts. This one assembles them into a single buildable recipe for a calibrated risk predictor.", 9.0),
        ("Step one. Pick a nonconformity score: a number that says how strange this patient looks under your model. We use the A P S score.", 9.5),
        ("Step two. Hold out a calibration set, or, when patients are scarce, let every patient calibrate with jackknife-plus or C V-plus.", 9.5),
        ("Step three. Compute the quantile of those calibration scores: the cut-off that the new patient's score must beat.", 9.0),
        ("Step four. Form the prediction set: every label whose score sits at or below that quantile goes in the set.", 9.0),
        ("Step five. Check the result on two axes: coverage, did the truth land in the set often enough, and sharpness, is the set small enough to be useful.", 10.0),
        ("Score, then calibrate, then quantile, then set, then check. That is the whole loop, and every box is one honest piece.", 9.0),
    ],
    # S2 — choosing the score: efficiency, not validity
    "S2_ScoreChoice": [
        ("Now the most surprising fact in conformal prediction. The score you choose controls how big your sets are, not whether they are valid.", 9.5),
        ("Coverage is guaranteed for any model that treats its training points symmetrically. The base model cannot make you wrong.", 9.0),
        ("It can only make you vague. A bad model still hits ninety percent coverage. It just outputs the full set, both labels, every time.", 9.5),
        ("That full set, A E-positive and A E-negative together, is valid and completely worthless. It never commits to anything.", 9.0),
        ("So a better model does not buy you more validity. Validity is already free. A better model buys you tighter, sharper sets.", 9.5),
        ("Why is validity score-agnostic? Because coverage rests only on exchangeability of the scores, on rank, not on the model being any good.", 9.5),
        ("So you pick the score for efficiency. The default here is L-two logistic regression, stable at small N, feeding the A P S score.", 9.5),
        ("Same coverage either way. The whole point of choosing well is a smaller set, never a more honest one.", 8.5),
    ],
    # S3 — diagnostics: coverage AND sharpness
    "S3_Diagnostics": [
        ("How do you check the wrapper actually works? Two numbers, and you must report both. Coverage alone is gameable.", 9.0),
        ("The first number is empirical coverage: the fraction of held-out patients whose true label landed inside the set.", 9.0),
        ("But coverage by itself can be gamed trivially. Predict everything, output the full set for everyone, and you score one hundred percent.", 9.5),
        ("Perfect coverage, zero information. So coverage is necessary, but it is never sufficient on its own.", 8.5),
        ("The second number is sharpness: the average set size, and the fraction of patients who got a confident singleton, just one label.", 9.5),
        ("A useful predictor has high coverage and high sharpness together. Small sets that are still right.", 8.5),
        ("Picture two models, both at ninety percent coverage. One has mean set size one-point-seven and commits on a third of patients.", 9.0),
        ("The other has mean set size two, the full set always, and never commits. Same coverage, but only the first one tells you anything.", 9.5),
    ],
    # S4 — pitfalls
    "S4_Pitfalls": [
        ("A recipe is the document people copy without reading the caveats. So here are the three ways the guarantee silently breaks.", 9.5),
        ("Pitfall one: leakage between training and calibration. Coverage holds only if the calibration scores and the test score are exchangeable.", 9.5),
        ("Anything computed on all N patients couples the test point to the calibration set: a scaler fit on everyone, a P C A basis, a feature selection step.", 10.0),
        ("The loudest leak runs through the label. Build a feature from a template fit on the same patients, and a patient's own label leaks into its own feature.", 10.0),
        ("Now the held-out patient was never really held out. Coverage looks beautiful and is optimistic, and the inference becomes circular.", 9.5),
        ("The fix is fold discipline: refit the scaler, the template, everything inside each training fold, or use a separate cohort.", 9.5),
        ("Pitfall two: broken exchangeability. Calibrate on site A, deploy on site B with sicker patients, and the promise can crack under the shift.", 9.5),
        ("Pitfall three: conditioning beyond what the data supports. Coverage is marginal, averaged over patients, never a promise about this one patient.", 9.5),
    ],
    # S5 — closing
    "S5_Close": [
        ("Step back and see what conformal actually delivers. It takes any predictor at all and wraps it in a finite-sample coverage guarantee.", 9.5),
        ("Finite-sample means the promise holds at the N you have, not only as N goes to infinity. No asymptotics, no large-sample hand-waving.", 9.5),
        ("It is robust and model-free. The base model can be a logistic, a tree, anything symmetric. Coverage does not care.", 9.0),
        ("And it is honest about its one assumption: exchangeability. That is the single price, and the whole guarantee rests on it.", 9.5),
        ("Quote the right constant for what you ran. Split with A P S is exact one minus alpha. Jackknife-plus and C V-plus give at least one minus two alpha.", 10.0),
        ("And remember what conformal never claims. It calibrates a forecast. It answers this patient's risk, never which connection causes the harm.", 9.5),
        ("Conformal is causation-agnostic and marginal. One assumption, stated plainly, and a guarantee you can actually audit. That is the recipe.", 9.5),
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
