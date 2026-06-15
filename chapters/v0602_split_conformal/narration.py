"""Narration for v0602_split_conformal — "Split conformal, and why it works exactly".

Source: volumes/vol6_conformal/chapters/02_split_conformal.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — Split the data
    "S1_Split": [
        ("Split conformal is the simplest machine that delivers a coverage guarantee, and it starts by cutting your patients in two.", 9.0),
        ("Take all the patients whose true adverse-event outcome you already know, and split them into two disjoint piles.", 9.0),
        ("The first pile is the proper training set. On it you fit any model you like, call it f-hat. Any algorithm at all.", 9.0),
        ("The second pile is the calibration set. Its size is n, and the model is never allowed to see it during fitting.", 9.0),
        ("Why hold calibration out? Because the model treats a point it trained on differently from a fresh one. That breaks the symmetry we will need.", 9.5),
        ("Kept disjoint, the calibration patients and a future test patient are interchangeable to the model. That interchangeability is the whole engine.", 9.5),
    ],
    # S2 — The nonconformity score
    "S2_Score": [
        ("Next we need a number that says how strange a patient looks to the fitted model. That number is the nonconformity score, s of x and y.", 9.5),
        ("Here x is the patient's features, lesion size and within-VIM position, and y is the candidate label, adverse event present or absent.", 9.5),
        ("The canonical score is one minus p-hat sub y of x, where p-hat sub y of x is the model's predicted probability for the label y.", 10.0),
        ("So a confident, correct call gives a small s; a confident, wrong call gives a large s. Big score means the point conforms poorly.", 9.0),
        ("Now run it on every calibration patient, using their true label. Score s sub i equals one minus p-hat sub y-i of x-i, for i from one to n.", 10.0),
        ("That leaves us with n strangeness numbers, one per held-out patient. The model entered only here; everything after is just counting.", 9.0),
    ],
    # S3 — The quantile
    "S3_Quantile": [
        ("Now sort those n calibration scores from least strange to most strange, and pick a single cutoff, q-hat.", 8.5),
        ("The rank we want is k equals the ceiling of one minus alpha, times n plus one. Let us decode every piece of that.", 9.0),
        ("One minus alpha is your target coverage, say zero point nine for ninety percent. Alpha is the miss rate you allow.", 8.5),
        ("The n plus one is the finite-sample correction. You are really after the quantile of n plus one scores, including the test point you cannot see.", 10.0),
        ("So you reach one rank higher than the naive n-th-of-n quantile, to pay for that one missing point. Use n plus one, never just n.", 9.5),
        ("The ceiling rounds up to the smallest whole rank at or above the target, because a rank must be an integer. Then q-hat is the k-th smallest score.", 10.0),
        ("Concrete case: n equals nine, alpha zero point one. k is the ceiling of zero point nine times ten, which is nine. So q-hat is the largest calibration score.", 10.0),
    ],
    # S4 — Build the prediction set
    "S4_Set": [
        ("With the threshold q-hat in hand, a brand-new patient walks in, and we build their prediction set, C of x.", 8.5),
        ("The set is every label y whose score does not exceed the cutoff: C of x equals the set of y with s of x, y less than or equal to q-hat.", 10.0),
        ("For binary adverse-event risk we test two candidates. Present is in the set when one minus p-hat-one is at or below q-hat.", 9.0),
        ("Absent is in the set when one minus p-hat-zero is at or below q-hat. The set can be just one, just zero, both, or rarely empty.", 9.5),
        ("For regression with score absolute y minus y-hat, the same rule becomes a band: y-hat of x, plus or minus q-hat.", 9.0),
        ("Picture the band: the prediction y-hat as a center line, and q-hat as a fixed half-width drawn above and below it.", 9.0),
        ("Validity comes from the rank; sharpness comes from the model. A tighter model narrows the band, but the guarantee does not move.", 9.0),
    ],
    # S5 — Why coverage holds
    "S5_Coverage": [
        ("Now the proof, and it turns on a single idea. We want the probability that the true outcome lands in the set to be at least one minus alpha.", 9.5),
        ("Strategy: the truth is covered exactly when the test score, s sub n plus one, is at or below q-hat. We turn that into a statement about a rank.", 10.0),
        ("Step one. Drop the test score into the pool of all n plus one scores and let R be its rank, one being smallest. Then the test score at or below q-hat means R at or below k.", 11.0),
        ("Step two, the load-bearing step. The score is a fixed function fitted on the separate training set, so it treats all n plus one points identically.", 10.5),
        ("So if the points are exchangeable, the scores are exchangeable, and the test score is equally likely to be any rank. R is uniform on one through n plus one.", 10.0),
        ("Probability R equals any particular r is exactly one over n plus one. The test score has no privileged position in the sorted pool.", 9.0),
        ("Step three, just count. The probability of coverage equals the probability that R is at most k, which equals k over n plus one.", 9.5),
        ("The ceiling is at least its argument, so this is at least one minus alpha. And the ceiling is below its argument plus one, so it stays under one minus alpha, plus one over n plus one. Done.", 11.5),
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
