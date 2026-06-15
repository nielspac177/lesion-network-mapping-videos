"""Narration for c1002_camera_vs_court_settled — "Camera vs court, settled".

The closing chapter of the series. One connectome C, two operations: the average
(the camera) and the contrast (the court). The camera is conceded broken; the
court is shown to still stand; the unifying slogan is stated; and the synthesis is
laid out — average is nonspecific (critique right), contrast can carry signal
(rebuttal right), the model class is limited (P3 right).

Sources (page-cited, no invented constants):
  responses/lnm_critique/sections/08_recipe.md
  responses/lnm_critique/sections/00_abstract_intro.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — one matrix, two operations
    "S1_OneMatrix": [
        ("This is where the whole series lands. Everything turned on one matrix, the normative connectome C, and on two ways of reading it.", 9.5),
        ("Operation one is the average. Pool a symptomatic group's lesion maps and take their mean. Call this the camera.", 8.5),
        ("Operation two is the contrast. Compare who has the symptom against who does not, after the shared backbone is subtracted. Call this the court.", 9.5),
        ("Same data, same connectome C, the very same lesions feeding in. The only difference is which operation you apply to them.", 9.0),
        ("And yet the two operations meet opposite fates. The camera is conceded broken; the court is shown to still stand.", 8.5),
        ("So the verdict is not who wins. It is a clean separation: a description that fails, and an inference that survives.", 8.5),
    ],
    # S2 — the camera is broken
    "S2_Camera": [
        ("Start with the camera, the average map. We concede it cleanly, because the math is the critique's, and the math is right.", 9.0),
        ("Write the operation as L N M equals the sum over patients of M times C: the lesion matrix M selecting and averaging rows of the connectome C.", 9.5),
("But notice the scope. Only when M approaches the identity, meaning uniform, non-overlapping coverage, does that average converge on the row-sum of C, its node degree. The hub map.", 10.5),
        ("So the photograph is mostly a picture of the camera. A regression on basic connectome properties explains ninety-three percent of map variance.", 9.5),
        ("It is nonspecific by construction. Real lesions, synthetic blobs, even random seeds funnel into the same hub-shaped cone.", 9.0),
        ("This is the critique's central, correct claim, and we grant it in full. The camera is broken. There is nothing to defend here.", 9.0),
    ],
    # S3 — the court still stands
    "S3_Court": [
        ("Now the court, the contrast. The signal, if there is one, was never in the average. It lives in the difference, after the backbone is removed.", 10.0),
        ("Test that contrast by shuffling the clinical labels, not the lesions. The connectome and the lesion geometry stay fixed; only the label-to-map link breaks.", 10.0),
        ("Here is why it stands. The backbone comes from C, which never saw the symptom. So it is label-independent.", 8.5),
        ("It therefore appears identically in the real statistic and in every shuffled one. It cancels from the contrast and cannot manufacture significance.", 9.5),
        ("That makes the test exact and distribution-free: valid under exchangeability, by the permutation-exactness theorem, with no model of the data assumed.", 9.5),
        ("And it is not empty. Same-symptom maps correlate at zero-point-four-four, different-symptom at zero-point-zero-nine, the degree map only zero-point-one-six.", 9.5),
        ("The witness is decisive. At threshold t above ten, zero false positives in a thousand iterations. The court still stands.", 9.0),
    ],
    # S4 — a failed null is a failed question
    "S4_Slogan": [
        ("Step back for the slogan that unifies everything. A null that finds nothing may simply be the wrong question.", 8.5),
        ("The location null asks: is this lesion location special? But every location gives back the same backbone, so almost nothing survives it.", 9.5),
        ("That is not LNM failing. That is a mis-aimed question producing a confident, empty answer.", 8.0),
        ("Swap the question. The label null asks: does the symptom track the map at all? That question has an exact, backbone-immune answer.", 9.5),
        ("So a failed null is a failed question, not a closed door. The critique broke a question, not the possibility of inference.", 9.0),
        ("Read every dead result this way before you trust it. Ask whether the null even pointed at the signal you were hunting.", 8.5),
    ],
    # S5 — what is settled
    "S5_Settled": [
        ("So what, finally, is settled. Not a winner. Three claims, each true in its own scope, held together.", 8.5),
        ("Settled one: the average is nonspecific. The critique, van den Heuvel and colleagues, is right about the object it actually measured.", 9.0),
        ("Settled two: the contrast can carry signal. The rebuttal is right that specificity survives a correct, label-permuting test.", 9.0),
        ("Settled three: the model class is limited. P three is right that a static connectome C is blind to dynamic, higher-order reorganization.", 9.5),
        ("These do not cancel. The first is about a description, the second about an inference, the third about the model. Different axes, all standing.", 9.5),
        ("Camera versus court is settled as a synthesis, not a verdict. One matrix, two operations, three truths. That is where the series rests.", 9.5),
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
