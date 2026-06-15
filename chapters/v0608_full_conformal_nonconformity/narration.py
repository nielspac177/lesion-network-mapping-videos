"""Narration for v0608_full_conformal_nonconformity —
"Full conformal and nonconformity-score design (deep dive)".

Source: volumes/vol6_conformal/chapters/02_split_conformal.md
        volumes/vol6_conformal/chapters/01_the_guarantee.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

Numbers are spelled out for the text-to-speech engine.
"""

SCENES = {
    # S1 — why full conformal at all
    "S1_Why": [
        ("Split conformal works by holding out a calibration pile, but that very split is its weakness. Let us see why, and what full conformal offers instead.", 10.0),
        ("Recall the recipe. You divide your patients into two disjoint piles: a training pile to fit the model, and a calibration pile of size n, never seen during fitting.", 10.0),
        ("That carves your data in half. The model only learns from the training pile, and the threshold only sees the calibration pile. Neither uses all the information you have.", 10.0),
        ("At the tiny n a focused-ultrasound cohort actually has, that waste bites. At n equals nine with ninety percent coverage, the threshold q-hat is the single worst calibration patient.", 10.5),
        ("So one weird case sets your whole bar. The estimate is noisy, and it depends on exactly which random split you happened to draw.", 9.0),
        ("Full conformal, also called transductive conformal, refuses to waste a point. Every patient takes part in both fitting and calibration. The promise: more stable sets from the same data.", 10.5),
        ("The price is compute, and it is steep. We will pay it in scene five. First, the procedure that earns the every-point ideal.", 9.0),
    ],
    # S2 — the transductive procedure
    "S2_Procedure": [
        ("Here is the transductive procedure. We have features x test for the new patient, but we do not know its true label, so we try every candidate label in turn.", 10.0),
        ("Fix a candidate label y. We pretend it is the truth, and we add the augmented pair, x test and y, to all the data we already hold.", 9.5),
        ("Now refit the model on this augmented dataset of n plus one points. Call the fitted model f-hat-y, because it depends on the candidate y we plugged in.", 10.0),
        ("With that model, score all n plus one points, including the test point. The score s of x and y measures how strange that pair looks; higher means stranger.", 10.0),
        ("Let r be the rank of the test score s sub test among all n plus one scores, where rank one is the smallest, least strange.", 9.5),
        ("Include the candidate y in the prediction set if its rank is not extreme: if r is at most the threshold rank k, where k is the ceiling of one minus alpha times n plus one.", 10.5),
        ("Then loop. Repeat the refit and the rank check for every candidate label, and collect the keepers. That set of keepers is the full conformal prediction set.", 10.0),
        ("Notice the loop refits once per candidate label. The model is no longer fixed, it is re-trained with the test point in the pool. That is the whole transductive idea.", 10.0),
    ],
    # S3 — coverage by symmetry
    "S3_Coverage": [
        ("Why does this cover the truth at least one minus alpha of the time? The answer is symmetry, and it is the same rank argument as split conformal, now using every point.", 10.0),
        ("Run the loop at the candidate that happens to be the true label, y test. Then the augmented set is the real data: the n calibration points plus the genuine test point.", 10.0),
        ("Those n plus one points are exchangeable: their joint distribution is unchanged by any reordering. Order carries no information about which point is the test point.", 10.0),
        ("And the score is computed by one fixed, symmetric function of the whole augmented set. Because the refit used all points together, it has no privileged view of the test point.", 10.5),
        ("Exchangeable points give exchangeable scores, and exchangeable scores give an exchangeable rank. So the test score s sub test is equally likely to land in any of the n plus one positions.", 10.5),
        ("That makes the rank r uniform on one through n plus one. The probability that r equals any particular position is exactly one over n plus one.", 9.5),
        ("Coverage is then just counting. The truth is kept when r is at most k, so the probability of coverage is k over n plus one, the ceiling of one minus alpha times n plus one, over n plus one.", 10.5),
        ("That fraction is at least one minus alpha, because the ceiling is at least its argument. Exact finite-sample coverage, distribution-free, using all of the data. That is the payoff.", 10.0),
    ],
    # S4 — designing the score
    "S4_ScoreDesign": [
        ("The proof never touched the values of the scores, only their order. So we are free to design the nonconformity score, and validity holds no matter which we pick.", 10.0),
        ("The plainest score for regression is the absolute residual: s equals the absolute value of y minus y-hat, the gap between the truth and the model's point prediction.", 10.0),
        ("Sort those residuals, take the threshold q-hat, and the set becomes y-hat plus or minus q-hat: a band of constant width around the prediction, the same width for every patient.", 10.5),
        ("That constant width is crude. A patient in an easy region of feature space deserves a tight band, a patient in a hard region a wide one. The normalized score buys that.", 10.0),
        ("Divide by a local scale: s equals the absolute value of y minus y-hat, all over sigma-hat of x, a learned estimate of the noise at this patient's features. Now the band breathes with difficulty.", 11.0),
        ("For regression there is also conformalized quantile regression. Fit a low and a high quantile, then the signed C-Q-R score measures how far outside that pair the truth fell, on whichever side.", 10.5),
        ("Each score shapes the set differently: constant bands, locally adaptive bands, or asymmetric quantile bands. But every one of them inherits the exact same coverage guarantee.", 10.0),
        ("That separation is the whole design. The score controls sharpness, how small and well-shaped the set is. The rank controls validity. Swap the score freely; the guarantee does not move.", 10.5),
    ],
    # S5 — the compute cost
    "S5_Cost": [
        ("Now the bill. Full conformal pays it in refits, and the count is brutal. Let us multiply it out.", 8.5),
        ("For one test patient, you refit the model once for every candidate label you consider. For a binary adverse event that is two refits, for a fine regression grid it can be hundreds.", 10.5),
        ("Multiply by the number of test patients you must predict, and the refits stack up. A model that takes a minute to fit becomes hours, or days, across a whole grid and a whole cohort.", 10.5),
        ("That is often simply infeasible, which is why full conformal is rarely run as written. Split conformal refits once, period, and pays only one held-out partition for it.", 10.0),
        ("The middle ground is cross-validation plus, C-V plus and jackknife plus. They refit only a handful of times, once per fold, and let every patient calibrate out of fold.", 10.5),
        ("So the trade is plainly stated. Full conformal spends compute to recover statistical efficiency: every point informs both the fit and the calibration.", 9.5),
        ("It is worth that price when data is scarce and precious, the model is cheap to refit, and you cannot afford to throw away a single calibration patient. That is exactly the small-cohort regime.", 11.0),
    ],
    # S6 — takeaway and the hierarchy
    "S6_Takeaway": [
        ("Step back and name what we built. Full conformal is the purest form of the method, the ideal the others approximate.", 8.5),
        ("It uses all the data, with no held-out pile wasted, since every point joins both the fit and the calibration.", 8.5),
        ("It delivers exact finite-sample coverage, at least one minus alpha, distribution-free, for any model you wrap.", 8.5),
        ("And it admits any nonconformity score: absolute residual, normalized residual, signed C-Q-R. Validity rides on the rank, sharpness on the score.", 9.5),
        ("Split conformal and C-V plus are not different methods so much as practical approximations of this ideal, trading a little efficiency for an enormous saving in compute.", 10.0),
        ("So name the hierarchy. Full conformal sits at the top: all data, exact coverage, any score. C-V plus and jackknife plus sit in the middle. Split conformal, the cheapest, sits at the base.", 10.5),
        ("Choose by your budget. When compute is tight, split. When data is precious and the model is cheap, climb toward full. The guarantee is the same at every rung.", 10.0),
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
