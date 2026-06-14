"""Narration for c0403_specificity_collapse — "Why specificity collapses".

Source:
  responses/lnm_critique/sections/03_the_right_null.md  (the location null, "why it's mis-aimed")
  responses/lnm_critique/sections/02_what_is_entailed.md (backbone domination, scope bound)
  responses/lnm_critique/papers/P1_critique.md           (70/78, 71/78 null-model failures)

This chapter follows ONE failing question, the random-lesion / location null, down to
its collapse. We do NOT pre-concede LNM. The collapse is shown to indict exactly one
object: the GROUP-AVERAGE map under UNIFORM, NON-OVERLAPPING sampling. The symptom
CONTRAST under a label null is a different object and is left untouched.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the text is
the subtitle in manim AND the spoken line. The number of play_beat()/wait_beat() calls
in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — preview the whole logical chain
    "S1_Chain": [
        ("Let us watch specificity collapse, but as a chain of linked claims, so you can see exactly where each link bites.", 9.0),
        ("Link one is the alignment bound, R one. It says every lesion map is pulled close to the backbone direction u sub one.", 9.0),
        ("Link two: because of that, every random seed we draw also lands near u sub one, so every fake is backbone-shaped too.", 9.0),
        ("Link three: so the fake statistic, T super b, sits right on top of the observed statistic, T observed.", 8.5),
        ("Link four: when fakes match the observed value, the location null can never reject. The p-value is large by construction.", 9.5),
        ("Link five, the conclusion: specificity collapses, but only for the location null on the average map. Hold onto that scope.", 9.5),
    ],
    # S2 — recall R1, the alignment bound
    "S2_R1Recall": [
        ("Start at link one by recalling theorem R one, the alignment bound we proved earlier.", 7.5),
        ("It bounds the tangent of theta-sub-ell, the angle between a lesion's map and the backbone u sub one.", 8.5),
        ("Tangent theta-sub-ell is at most lambda-two over lambda-one, times the norm of ell-perp over the size of u-one-transpose-ell.", 9.5),
        ("Lambda-one and lambda-two are the top two eigenvalues of the connectome C. Their ratio is the spectral gap.", 8.5),
        ("Ell-perp is the part of the lesion off the backbone; u-one-transpose-ell is its overlap with the backbone.", 8.5),
        ("Here is the punchline. When the spectral gap is small, lambda-two over lambda-one is tiny, so the whole bound is tiny.", 9.0),
        ("A tiny tangent means a tiny angle: every lesion map sits in a narrow cone hugging u sub one. That is link one.", 9.0),
    ],
    # S3 — fakes reproduce the map; T^(b) ~ T_obs
    "S3_FakesMatch": [
        ("Now link two. The location null builds fakes by drawing random seeds, ell super one through ell super capital B.", 9.0),
        ("But random blobs overlap the hub structure u sub one just like real lesions do, so each fake obeys R one as well.", 9.5),
        ("Push each fake through the map operator and it, too, lands in the narrow cone around the backbone.", 8.5),
        ("So every fake map is as backbone-shaped as the real one. Watch them pile onto the observed map.", 8.5),
        ("Now summarize each map by one number, T, that measures how backbone-shaped it is.", 7.5),
        ("Because every fake hugs u sub one, its score T super b comes out close to the observed score, T observed.", 9.0),
        ("The whole crowd of fakes reproduces the map. That is link two: T super b is approximately T observed for nearly every b.", 9.5),
    ],
    # S4 — nothing rejects; p-value large by construction
    "S4_NoRejection": [
        ("Link three. The p-value averages an indicator over the B fakes: one over B, sum over b, of one when T super b is at least T observed. That is the right-tail rank of T observed among the fakes.", 11.0),
        ("But we just saw the fakes pile up exactly where the observed value sits. The null distribution is glued to T observed.", 9.0),
        ("So the observed map is not extreme against the crowd. Its rank is unremarkable, and the p-value comes out large.", 9.0),
        ("It is large by construction, not by accident. The backbone made every location alike, so none can stand out.", 9.0),
        ("Read carefully: the location null cannot tell a real average map from a fake average map. That is the collapse.", 9.0),
        ("Specificity, the power to reject when the location really is special, falls toward the floor for this null.", 8.5),
    ],
    # S5 — P1's own numbers; scope
    "S5_Evidence": [
        ("Link four needs a witness, and the critique supplies it from its own re-analysis. Page twelve forty-four.", 8.5),
        ("Seventy of seventy-eight maps failed a random synthetic-lesion null, at a liberal uncorrected alpha of zero point zero five.", 9.5),
        ("And seventy-one of seventy-eight failed a location-permutation null that even preserves modular prevalence.", 9.0),
        ("Almost nothing rejects. Exactly what the chain predicted: the fakes match, so the null cannot fire.", 8.5),
        ("But here is the scope, and it is everything. This indicts the location null on the group-average map.", 9.0),
        ("It does not touch the symptom contrast under a label null, where the backbone cancels instead of dominating. Different object, different verdict.", 10.0),
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
