"""Narration for v0606_exchangeability_shift — "Exchangeability and distribution shift".

Source: volumes/vol6_conformal/chapters/06_exchangeability_shift.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

All equations and claims are drawn from the source chapter:
  - exchangeability defined as invariance under permutation; uniform rank => coverage
  - split-conformal coverage band  1 - alpha <= Pr(cover) < 1 - alpha + 1/(n+1)
  - covariate shift: P(X) changes, P(Y|X) fixed; weight w(x) = q_X(x) / p_X(x)
  - weighted conformal (Tibshirani, Barber, Candes & Ramdas 2019): normalized
    weights p_i, weighted quantile, coverage restored if w known
  - effective sample size  (sum w)^2 / sum w^2  collapses when densities barely overlap
  - label / concept shift: P(Y|X) moves, no reweighting saves you
  - tie to permutation tests: both rest on a symmetry assumption
"""

SCENES = {
    # S1 — Exchangeability is load-bearing
    "S1_Assumption": [
        ("Every guarantee in this volume rested on one word: exchangeability. Let us see why it is load-bearing.", 8.5),
        ("Write each patient as a pair Z-i, the features X-i and the outcome Y-i, AE-minus or AE-plus.", 8.5),
        ("Exchangeability means the joint law of all n-plus-one patients is invariant under every reordering, every permutation pi.", 9.0),
        ("Under that symmetry, the rank of the new patient's strangeness score is uniform on one through n-plus-one.", 9.0),
        ("That uniform rank is the whole engine. It is why split conformal covers between one-minus-alpha and one-minus-alpha plus one over n-plus-one.", 9.5),
        ("Now break it. Calibrate at a gentle site, then deploy where lesions are bigger and the next patient is systematically stranger.", 9.0),
        ("The rank is no longer uniform, the lower bound no longer holds, and realized coverage can land anywhere in zero to one.", 9.0),
        ("And nothing crashes. The sets still print. The calibration number still says ninety percent. The failure is silent.", 8.5),
    ],
    # S2 — Covariate shift
    "S2_Covariate": [
        ("Two distinct things can shift, and it pays to name them apart. The first is covariate shift.", 7.5),
        ("Covariate shift: the feature distribution P of X changes, but the rule connecting features to risk, P of Y given X, is fixed.", 9.5),
        ("A larger lesion carries the same risk wherever it is made; the new site simply makes more of them. Same physiology, different mixture.", 9.5),
        ("So your calibration set is the wrong mixture: too many small lesions, too few big ones to stand in for the new population.", 9.0),
        ("The repair is to reweight each calibration patient by a likelihood ratio, w of x.", 7.0),
        ("Decode it: w of x equals q-X of x over p-X of x, the deployment density divided by the calibration density at that patient's features.", 10.0),
        ("Features common at the new site but rare in calibration get up-weighted; the reverse get down-weighted.", 8.5),
        ("Because the part that broke, the feature distribution, is observable, and the part you trust, the conditional risk, is held fixed.", 9.0),
    ],
    # S3 — Weighted conformal
    "S3_Weighted": [
        ("Weighted conformal prediction puts that idea to work. Tibshirani, Barber, Candes and Ramdas, two thousand nineteen.", 9.0),
        ("Plain conformal gives every calibration patient an equal vote, the uniform weight one over n-plus-one.", 8.5),
        ("Weighted conformal replaces those with normalized weights p-i: each patient's w divided by the total w over all n-plus-one points.", 9.5),
        ("The new patient gets its own share too, p sub n-plus-one, the test weight w of x over that same total.", 8.5),
        ("The weighted quantile q-hat-w is the smallest threshold where the weighted mass of calibration scores at or below it, plus p n-plus-one, reaches one-minus-alpha.", 10.5),
        ("Why it works: under covariate shift the chance the test point lands at rank k is no longer uniform; it is p-k, weighted by how representative point k is.", 10.0),
        ("Run the same below-the-threshold calculation with those non-uniform rank probabilities, and the one-minus-alpha floor comes back out.", 9.5),
        ("When w is identically one, no shift, every p-i collapses to one over n-plus-one and we recover plain split conformal exactly.", 9.0),
        ("So if the weights are truly known, coverage is restored: Pr under Q that the new patient is covered is at least one-minus-alpha.", 9.0),
    ],
    # S4 — When weights are unknown
    "S4_Unknown": [
        ("Now the honest caveat. In practice you do not know the weights; you estimate q-X over p-X from the data.", 9.0),
        ("Estimation error in w degrades the guarantee, and worst exactly when the two densities barely overlap.", 8.5),
        ("Then a handful of calibration patients carry almost all the weight, and the effective sample size collapses toward one.", 9.0),
        ("So report it: the effective n is the sum of weights squared, over the sum of the squared weights.", 9.0),
        ("If that number is a single digit, your restored coverage is one or two patients of evidence wearing a theorem.", 9.0),
        ("And there is a deeper limit. Weighted conformal fixes covariate shift only. It does nothing for label shift.", 8.5),
        ("Label shift is when the rule itself moves: the same features carry a different risk, P of Y given X is no longer the same.", 9.5),
        ("For a changed conditional there is no free lunch. No reweighting of features recovers a rule you no longer know. Get new-regime data.", 9.5),
    ],
    # S5 — Tie to permutation tests
    "S5_Tie": [
        ("Step back, because this is the same lesson we met across the whole series.", 7.0),
        ("Conformal coverage rests on exchangeability: the n-plus-one patients are shuffleable without changing the joint law.", 9.0),
        ("Permutation inference, the engine of the earlier volumes, rests on the very same symmetry under a null.", 8.5),
        ("In both, a symmetry license lets you reason about ranks, and from ranks comes the guarantee.", 8.0),
        ("Break the symmetry and you lose the guarantee. A distribution shift here is the wrong permutation scheme there.", 9.0),
        ("Same crack, two faces: in conformal the fix is calibration; in permutation the fix is the right exchangeable null.", 9.0),
        ("So the order of operations holds. Measure the shift first, then repair only what is covariate and known.", 8.5),
        ("Honor the symmetry and the promise is exact. Break it quietly and the number is just a costume. That is the whole series in one line.", 9.5),
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
