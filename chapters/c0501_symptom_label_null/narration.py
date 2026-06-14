"""Narration for c0501_symptom_label_null — "The symptom-label null".

Source: responses/lnm_critique/sections/03_the_right_null.md

This chapter introduces the symptom-label null H0^sym: holding the lesions and
the connectome FIXED, shuffle the impaired/spared LABELS and recompute the
contrast each time. It contrasts this with the location null H0^loc, defines the
contrast statistic T, previews why the backbone cancels, and sets up the two
claims to be proved next (exactness in c0502, cancellation in c0503).

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — a different question
    "S1_Question": [
        ("A null model is really just a question. Get the question wrong, and a perfectly good test gives you a useless answer.", 9.0),
        ("The location null asked: is the place of these lesions special? And the backbone made that question impossible to win.", 9.0),
        ("So we change the question. Hold the lesions fixed. Hold the connectome C fixed. Let only one thing vary: the symptom label.", 9.5),
        ("Each patient carries a label, y sub i: impaired, or spared. The new null asks whether those labels track the lesions.", 9.0),
        ("In symbols: H-naught-sym says the labels are exchangeable, given the fixed maps and covariates. The symptom carries no extra information.", 9.5),
        ("Notice what moves. In the location null the lesion moved. Here the lesion never moves. Only the label is reshuffled.", 9.0),
        ("Same data, two completely different questions. The critique's machinery breaks the first. It leaves this second one untouched.", 9.0),
    ],
    # S2 — shuffle the labels
    "S2_Procedure": [
        ("Here is the procedure, step by step. Start with the things we are forbidden to touch.", 7.0),
        ("Fix every lesion, l sub i, exactly where it is. Fix the normative connectome C exactly as it is. These never change.", 9.0),
        ("Each patient i also has a symptom label, y sub i: a one if impaired, a zero if spared. This is the only movable part.", 9.5),
        ("From the fixed maps and the labels we compute a single number, the contrast statistic T. It measures how sharply the labels split the maps.", 9.5),
        ("Now permute. Apply a permutation pi to the labels, sending y to y-pi, a reshuffling of who is called impaired and who is called spared.", 9.5),
        ("Recompute T on the shuffled labels. Do this for every permutation pi in the group. The maps and C are identical every single time.", 9.5),
        ("If the real T is sharper than nearly all the shuffled ones, the symptom genuinely tracks the lesions. If not, it does not.", 9.0),
    ],
    # S3 — the contrast statistic
    "S3_Contrast": [
        ("Let us type out the contrast statistic, one symbol at a time, so nothing is hidden.", 7.0),
        ("First, each patient's map. m sub i equals C times l sub i: push the lesion l sub i through the connectome C.", 9.0),
        ("The labels sort the patients into two groups. Group one, the impaired with y equal to one. Group zero, the spared with y equal to zero.", 9.5),
        ("Average the maps inside each group. m-bar-one is the mean map of the impaired. m-bar-zero is the mean map of the spared.", 9.0),
        ("The contrast is their difference. Delta equals m-bar-one minus m-bar-zero: how far the impaired mean sits from the spared mean.", 9.0),
        ("In practice we sharpen Delta into a t-statistic per voxel, then summarize the whole map by its largest value, the max-statistic T.", 9.5),
        ("So T is one scalar verdict: the size of the gap that the symptom label opens between the two groups of maps.", 9.0),
    ],
    # S4 — why this question has an answer
    "S4_WhyItWorks": [
        ("Why should this question even have an answer, when the location null had none? Look at what is shared.", 8.5),
        ("Because the lesions are held fixed, the same backbone sits inside every map, in both label groups, identically.", 9.0),
        ("Write each map as two pieces: a backbone part, beta sub i times u sub one, plus a residual r sub i left over.", 9.0),
        ("The backbone part depends on where the lesion sits in the connectome. It does not depend on which label the patient carries.", 9.0),
        ("So when we subtract group means, the backbone enters both sides equally and cancels. It is everywhere, so in the contrast it is nowhere.", 9.5),
        ("What survives the subtraction is only the residual difference, the part of the map that the symptom label could actually track.", 9.0),
        ("The very thing that detonated the location null, the backbone in every map, is the thing that goes inert under label permutation.", 9.5),
    ],
    # S5 — what we must prove
    "S5_Bridge": [
        ("We have a question worth asking and a clean procedure. But two claims are still promises, not proofs.", 8.5),
        ("Claim one: this permutation test is exact. Its p-value controls the error rate in finite samples, with no distributional assumption.", 9.5),
        ("That is a counting argument over the n-factorial labelings. The observed statistic's rank is uniform, so the test is honest by construction.", 9.5),
        ("Claim two: the backbone really cancels, algebraically, not just in spirit. Beta sub i times u sub one must drop out of the contrast.", 9.5),
        ("Because beta sub i is label-independent, its distribution is identical in the observed and every shuffled labeling. So it has no leverage.", 9.5),
        ("Nail both and the symptom null is immune to the backbone by construction. We prove exactness next, then cancellation after it.", 9.0),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:28s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':28s} target={grand:5.1f}s ({grand/60:.1f} min)")
