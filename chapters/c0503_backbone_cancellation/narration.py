"""Narration for c0503_backbone_cancellation — "Backbone cancellation (the algebra)".

Source: responses/lnm_critique/sections/03_the_right_null.md  (second half, the
        backbone-cancellation derivation and the worked four-patient example)
        responses/lnm_critique/sections/02_what_is_entailed.md  (the contrast Delta
        = bar m+ - bar m-, leading term lambda_1 (c1+ - c1-) u_1, cancellation)

This is the load-bearing algebra of the whole response: the same backbone that
wrecks the average map is exactly the term that cancels out of the symptom
contrast. We build it symbol by symbol.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — split each patient map into backbone plus residual
    "S1_Decompose": [
        ("We have one patient map per patient. Let us split each of them into two clean pieces.", 8.0),
        ("Write x sub i, patient i's lesion-network map, as b sub i plus r sub i. A backbone piece plus a residual.", 9.0),
        ("The backbone piece b sub i equals lambda one, times the overlap u-one-transpose l sub i, times the direction u sub one.", 9.5),
        ("Decode it. u sub one is the connectome's dominant axis, its hub backbone. lambda one is how strongly that axis dominates.", 9.0),
        ("The overlap u-one-transpose l sub i is a single number: how much patient i's lesion projects onto that backbone axis.", 9.5),
        ("So b sub i is that whole backbone axis, scaled by how hard this particular lesion hits it. A label-free property of location.", 9.5),
        ("And r sub i is everything else, the residual, the part of the map that points off the backbone, into the finer components.", 9.0),
    ],
    # S2 — the backbone is label-blind
    "S2_BackboneLabelFree": [
        ("Now the pivot of the whole argument. Look hard at what b sub i actually depends on.", 8.0),
        ("It depends on the lesion l sub i, and on the fixed connectome that gives us lambda one and u sub one. Nothing else.", 9.0),
        ("In particular, b sub i does not depend on the symptom label y sub i. Whether the patient is impaired or spared never enters it.", 9.5),
        ("So if we shuffle the labels, who is impaired and who is spared, every backbone piece b sub i stays exactly where it was.", 9.0),
        ("That means the two group means of the backbone, b-bar one for the impaired and b-bar zero for the spared, are draws from one pool.", 9.5),
        ("Under label shuffling they are interchangeable. Same population, sliced two ways by labels that the backbone cannot feel.", 9.0),
    ],
    # S3 — form the contrast, split into backbone piece and residual piece
    "S3_Contrast": [
        ("To detect signal we never use the average. We use the contrast, the difference between the two groups, voxel by voxel.", 9.0),
        ("At voxel v, the test statistic t sub v is proportional to the impaired group mean minus the spared group mean, at that voxel.", 9.0),
        ("Substitute the split x equals b plus r, and the contrast falls into two pieces that we can read separately.", 8.5),
        ("First piece: the backbone term. b-bar-one minus b-bar-zero, the gap in backbone means, times u sub one at voxel v.", 9.5),
        ("Second piece: the residual term. r-bar-one at voxel v minus r-bar-zero at voxel v. The gap in the off-backbone parts.", 9.5),
        ("So the whole contrast is a backbone piece plus a residual piece. Two terms. We now ask which one carries the signal.", 9.0),
    ],
    # S4 — the backbone piece drops out (THE load-bearing step)
    "S4_Cancel": [
        ("Here is the load-bearing step. Watch the backbone piece, b-bar-one minus b-bar-zero, under label permutation.", 8.5),
        ("Because the backbone loadings are never relabeled, only the symptom labels move, this gap has the same law in every permutation.", 9.5),
        ("It is label-independent. So whatever value it takes in the real data, it takes the same kind of value in every shuffled world.", 9.0),
        ("In expectation, b-bar-one minus b-bar-zero goes to zero. The two backbone means are draws from the same pool, so their gap averages out.", 10.0),
        ("That means the backbone term sits identically in the observed statistic and in every permuted one. It cannot shift the rank.", 9.5),
        ("So it contributes nothing to the permutation distribution. Strike it out. The backbone piece is gone from the contrast.", 9.0),
        ("This is the cancellation, on the algebra. The huge offset that dominated any average map drops out of the contrast exactly.", 9.5),
    ],
    # S5 — what survives is signal; camera vs court made algebraic
    "S5_Moral": [
        ("After the backbone strikes out, exactly one term is left standing in the contrast.", 7.5),
        ("Only r-bar-one minus r-bar-zero survives. The label-correlated residual. The part of the map that actually tracks the symptom.", 9.5),
        ("So the same hub structure that wrecked the average map is precisely what the contrast cancels. One mechanism, opposite fates.", 9.5),
        ("In the average it is the villain that buries the signal. In the contrast it is a label-free constant that simply vanishes.", 9.0),
        ("This is the camera versus the court, made algebraic. The average photographs the backbone; the contrast judges the residual.", 9.5),
        ("And the residual is where the numbers live. Same-symptom maps correlate at zero point four four.", 8.0),
        ("Different-symptom only zero point zero nine, and the degree map only zero point one six. The contrast separates them cleanly.", 9.0),
        ("The witness: at threshold t above ten, zero false positives in a thousand iterations. The backbone made no ghosts.", 9.0),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:24s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':24s} target={grand:5.1f}s ({grand/60:.1f} min)")
