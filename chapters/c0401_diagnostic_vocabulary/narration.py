"""Narration for c0401_diagnostic_vocabulary — "Sensitivity, specificity, and what a null is".

Source: responses/lnm_critique/sections/03_the_right_null.md

This chapter builds the diagnostic-test vocabulary the later argument needs:
the 2x2 confusion matrix, sensitivity, specificity, the ROC trade-off, and the
thesis that a null hypothesis is a QUESTION — so "found nothing" can mean the
answer is no OR the question was wrong. That thesis is the source file's opening
line: "A null model is a question. Get the question wrong and a perfectly good
test gives you a useless answer."

Numbers / claims quoted from the source (03_the_right_null.md):
  - "A null model is a question." (opening line, and section heading
    "A failed null is a failed *question*, not a failed method.")
  - the location null H_loc ("is this location special?") vs the symptom-label
    null H_sym ("does the symptom track these lesions more than chance?") — two
    questions of the same data, "Same patients ... opposite fate."
  - zero false positives in one thousand iterations at threshold t > 10
    (REBUTTAL p.3), with leakage (4.6%) only at the sub-standard t = 3.0.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the confusion matrix (7 beats)
    "S1_Confusion": [
        ("Before we argue about which test is right, we need the vocabulary of testing. It all starts with one little table.", 8.5),
        ("Down the side runs the TRUTH: either there really is a signal, or there is none. We never get to see this column directly.", 9.0),
        ("Across the top runs our TEST's verdict: we either reject the null and claim an effect, or we keep the null and stay silent.", 9.0),
        ("Truth says signal, and we reject: that is a true positive. We caught a real effect. Call it T-P, the top-left cell.", 8.5),
        ("Truth says no signal, but we reject anyway: a false positive. We cried wolf. F-P, bottom-left, and this one is the villain.", 9.0),
        ("Truth says signal, but we kept the null: a false negative. We missed it. F-N, top-right.", 8.0),
        ("And truth says no signal, and we correctly stayed silent: a true negative. T-N, bottom-right. Four cells, the whole game.", 9.0),
    ],
    # S2 — sensitivity (7 beats)
    "S2_Sensitivity": [
        ("Now we squeeze numbers out of that table. The first is sensitivity, sometimes called the true-positive rate.", 8.0),
        ("Sensitivity equals T-P divided by the quantity T-P plus F-N. Let us read every symbol on the right.", 8.5),
        ("The denominator, T-P plus F-N, is everything in the top row: all the cases where truth really had a signal.", 8.5),
        ("The numerator, T-P alone, is just the ones in that row we actually caught by rejecting.", 7.5),
        ("So sensitivity asks: of the real effects out there, what fraction did we catch? A high number means we miss very little.", 9.0),
        ("A perfectly sensitive test never lets a real effect slip past. Its false negatives, F-N, drop to zero.", 8.0),
        ("Sensitivity is the power of the test. It is the easy virtue to chase, because catching things is the part everyone wants.", 8.5),
    ],
    # S3 — specificity (7 beats)
    "S3_Specificity": [
        ("The second number is specificity, and it is the conscience of the test, the part that keeps it honest.", 8.0),
        ("Specificity equals T-N divided by the quantity T-N plus F-P. Again, let us decode the right-hand side.", 8.5),
        ("The denominator, T-N plus F-P, is the bottom row: every case where truth had NO signal at all.", 8.5),
        ("The numerator, T-N alone, is the ones among those we correctly cleared by keeping the null.", 7.5),
        ("So specificity asks: of the nulls, the genuinely empty cases, what fraction did we correctly clear?", 8.0),
        ("The enemy here is F-P, the false positive: a null we wrongly flagged as real. Every false positive eats your specificity.", 8.5),
        ("And this is the number that will matter for lesion mapping, because the connectome backbone manufactures false positives if you let it.", 9.0),
    ],
    # S4 — the trade-off (ROC) (7 beats)
    "S4_ROC": [
        ("Here is the cruel part. You cannot freely maximize both. Sensitivity and specificity are tied together by a threshold.", 8.5),
        ("Picture a dial: the threshold at which the test decides to reject. Slide it one way, and you reject more often.", 8.0),
        ("Reject more often and you catch more real effects, so sensitivity rises. But you also flag more empty cases, so specificity falls.", 9.0),
        ("Sweep that dial from one extreme to the other and you trace a curve: the receiver-operating-characteristic, the R-O-C curve.", 8.5),
        ("Push the dial to always reject. Now you catch every real effect: sensitivity is a perfect one. But you clear no nulls: specificity is zero.", 9.5),
        ("A test that always says yes is perfectly sensitive and completely worthless. The art is buying sensitivity without giving away specificity.", 9.0),
        ("And for lesion network mapping, specificity is the hard one, because the backbone makes almost every map look real. Catching is easy; clearing is not.", 9.5),
    ],
    # S5 — a null is a question (8 beats)
    "S5_NullIsQuestion": [
        ("Now the thesis that runs through this whole series. A null hypothesis is not just a baseline. It is a QUESTION.", 8.5),
        ("In the words of our source: a null model is a question. Get the question wrong, and a perfectly good test gives you a useless answer.", 9.0),
        ("So when an experiment finds nothing, there are two very different reasons, and the table alone cannot tell them apart.", 8.5),
        ("Reason one: the answer really is no. There was no signal, and the test correctly stayed silent.", 8.0),
        ("Reason two: the question was wrong. You asked the wrong null, so even a real signal had nowhere to show up.", 8.5),
        ("And that is exactly the trap ahead. The same lesion data can be fed two different nulls, which ask two different questions.", 9.0),
        ("One null asks: is this lesion LOCATION special? The other asks: does the SYMPTOM track these lesions more than chance?", 9.0),
        ("Same patients, same connectome, opposite fates. Next we will see why one question fails and the other one cannot.", 8.5),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:22s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':22s} target={grand:5.1f}s ({grand/60:.1f} min)")
