"""Narration for c0402_location_null — "The location null".

Source: responses/lnm_critique/sections/03_the_right_null.md  (first half)
        responses/lnm_critique/papers/P2_nullmodels.md         (the procedure)

This chapter states ONE of the two nulls precisely: the random-lesion / location
null. It asks "is THIS lesion location special compared to an ensemble R of other
locations?" We define R, the test statistic (backbone shape), the permutation
procedure, and exactly what the null can and cannot answer. The symptom-label null
is Part 5; this chapter only sets up the location question fairly and fully.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — what the location null asks
    "S1_Question": [
        ("A null model is really a question in disguise. Get the question wrong, and a perfectly good test hands you a useless answer.", 9.0),
        ("So before computing anything, ask exactly what the first candidate, the random-lesion null, is testing.", 8.0),
        ("It asks one thing: is THIS lesion location special, compared to an ensemble of other locations we could have drawn?", 9.0),
        ("Call that ensemble script-R: a cloud of alternative lesion placements, random blobs, synthetic seeds, or real lesions reshuffled to new spots.", 10.0),
        ("Now type the hypothesis. H-naught-loc says the observed lesion location is exchangeable with locations drawn from script-R.", 9.5),
        ("Exchangeable means swappable: under the null, your real placement is just one more draw from that same cloud, no more special than the fakes.", 9.5),
        ("So rejecting H-naught-loc would mean: this location produces a more extreme map than a typical location would. That, and only that.", 9.5),
    ],
    # S2 — the reference ensemble R
    "S2_Ensemble": [
        ("Let us draw the ensemble script-R itself, because everything downstream is a comparison against it.", 8.0),
        ("Each member is a fake lesion placement: random, scattered, and, by construction, non-overlapping across the brain.", 9.0),
        ("Push each placement through lesion network mapping. A real lesion at location ell becomes the map m-ell equals C times ell.", 9.5),
        ("Here C is the fixed normative connectome and ell marks the lesion's voxels, so every placement yields one whole-brain map.", 9.5),
        ("Do that for the observed lesions, and again for every fake draw in script-R. Now we have one real map and a whole crowd of null maps.", 9.5),
        ("Special would mean the observed map stands out from that crowd: more backbone-shaped, or less, than the typical fake placement.", 9.5),
        ("So the entire test reduces to a single comparison: where does the real map fall inside the cloud of maps from script-R?", 9.0),
    ],
    # S3 — the test statistic is backbone shape
    "S3_Statistic": [
        ("To compare maps we need one number per map, a summary statistic. For a single average map the natural choice is its backbone shape.", 9.5),
        ("Concretely, take T to be the cosine similarity between your map and the pooled connectome map: how backbone-shaped is this map.", 9.5),
        ("Apply it to the observed lesions and you get T-obs, one scalar that scores how much the real map points along the backbone.", 9.0),
        ("Now run the same recipe on the ensemble. For each draw b in script-R, the map m-ell-b gives a null value T-super-b.", 9.5),
        ("Collect all those T-super-b values and you have the null distribution: the spread of backbone-shape scores you would see by chance.", 9.5),
        ("T-obs is the single dot we drop onto that distribution. The whole question is whether the dot sits out in the tail, or buried in the bulk.", 9.5),
        ("Hold that picture: one observed statistic, T-obs, against a histogram of ensemble statistics, T-super-b. That is the location test.", 9.0),
    ],
    # S4 — the procedure
    "S4_Procedure": [
        ("Now the procedure, step by step, exactly as the responders spell it out in their Comment.", 8.0),
        ("Step one: take one draw b from script-R, that is, reposition the lesions randomly throughout the brain.", 8.5),
        ("Step two: recompute lesion network mapping for those randomized lesions, giving a full null map.", 8.0),
        ("Step three: retain a single number from that map. They keep the maximum voxel-wise value, T-super-b, as one sample from the null.", 9.5),
        ("Repeat those three steps many times, five thousand permutations or more, so the histogram of T-super-b values fills in.", 9.0),
        ("Then the p-value is just a fraction: averaging over all B draws, count one each time a draw beats the observed T-obs, zero otherwise. That share is the p-value.", 9.5),
        ("In their voxel version, a voxel is significant if its real value exceeds the ninety-fifth percentile of the null, controlling family-wise error at five percent.", 10.0),
        ("Every symbol is now defined: script-R the ensemble, T-super-b each null draw, T-obs the real statistic, and p its right-tail rank.", 9.5),
    ],
    # S5 — what it can and cannot answer
    "S5_WhatItAsks": [
        ("Step back and read the fine print, because this is where nulls get misused.", 7.5),
        ("This null asks one question only: is the lesion location special? Nothing more is encoded in H-naught-loc.", 8.5),
        ("So it is exactly the right tool IF your scientific claim is genuinely about location: lesions here rather than there produce this map.", 9.5),
        ("When the claim is about place, a small p-value is real evidence that the location, not chance geography, drives the map.", 9.0),
        ("But it cannot speak to a symptom-label relationship. It never looks at who was impaired and who was spared.", 9.0),
        ("Asking whether the symptom tracks the lesions is a different question, and it needs a different null, the symptom-label null of Part five.", 9.5),
        ("Same data, two questions. Today we only built the location question, cleanly and fully. The symptom question is the next chapter.", 9.0),
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
