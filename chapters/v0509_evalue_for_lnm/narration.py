"""Narration for v0509_evalue_for_lnm — "An e-value version of the LNM symptom null".

Sources:
  volumes/vol5_evalues/chapters/01_what_is_an_evalue.md
  responses/lnm_critique/sections/03_the_right_null.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

This chapter is an ILLUSTRATIVE construction. Where the exact estimator used by
the published responses is not settled from the sources, we carry the
[verify against primary source] caveat (see Scene 6).
"""

SCENES = {
    # S1 — recall the symptom-label permutation null
    "S1_Recall": [
        ("Back in Part five we built the symptom-label permutation null. Let us recall it, because we are about to make an e-value twin of it.", 9.0),
        ("The setup. There are n patients. Patient i has a fixed lesion-connectivity map x-sub-i, and a symptom label y-sub-i, impaired or spared.", 9.5),
        ("The null hypothesis H-zero-sym says the labels are exchangeable given the fixed maps and covariates. The symptom carries no information about the wiring.", 9.5),
        ("So we keep every lesion and the connectome fixed, and only shuffle the labels. Each shuffle is a permutation pi from the group G of relabelings.", 9.5),
        ("We recompute the contrast statistic T of y-pi for every pi, and form the permutation p-value: the fraction of relabelings whose T is at least the observed T.", 10.0),
        ("By permutation exactness, that p-value is exact in finite samples. No distributional assumption, just counting labelings. That is our anchor.", 9.0),
        ("Now we ask a new question. Can we report this same evidence not as a p-value, but as a fair bet against the null? That is the e-value.", 9.0),
    ],
    # S2 — betting on the contrast
    "S2_BetOnContrast": [
        ("From Volume five: an e-value is the payout of a one-dollar bet rigged to be fair when the null is true. Non-negative, and expected value at most one under H-zero.", 10.0),
        ("So let us bet on the contrast. Our wager: the observed contrast T of the identity labeling beats a randomly relabeled T. If the symptom tracks the wiring, it should.", 10.0),
        ("Here is the cleanest e-value you can mint from a permutation test. Let the size of the group be the number of relabelings, big-N. Define E as follows.", 9.0),
        ("E equals big-N times the indicator that the observed T lands at the very top of all the permuted T's. You win big-N dollars only if you topped the field.", 9.5),
        ("Why is this fair under the null? Under exchangeability the observed labeling is just one of the N equally likely labelings, so it is the top one with probability one over N.", 10.0),
        ("So the expected payout is big-N times one over N, which is exactly one. Staked a dollar, expect a dollar back. A valid e-value, the calibrator E equals one over alpha times an indicator.", 10.0),
        ("Read it as evidence. Top of a thousand relabelings pays a thousand dollars: the null is in serious trouble. Mid-pack pays zero: you learned nothing. The payout is the evidence.", 10.0),
    ],
    # S3 — the backbone still cancels
    "S3_BackboneStill": [
        ("Here is the reassuring part. This e-value is built on the very same label-shuffle contrast T. So everything we proved about that contrast it simply inherits.", 9.5),
        ("Recall the decomposition. Each map x-sub-i splits into a backbone piece b-sub-i, which is u-one times a loading, plus a residual r-sub-i.", 9.0),
        ("The backbone loading depends only on where the lesion sits in the connectome. It does not depend on the symptom label y-sub-i. It is label-free.", 9.0),
        ("In the difference of group means, that label-free backbone is the same constant on both sides. It subtracts off. The contrast T sees only the residuals.", 9.5),
        ("And because the backbone loadings are never relabeled, only the symptom labels are, the backbone enters the observed T and every permuted T identically.", 9.5),
        ("So the e-value inherits the cancellation for free. It is a deterministic function of T, and T already does not notice the backbone.", 9.0),
        ("The mechanism that detonated the location null, the backbone in every map, is inert here, in the p-value and in its e-value twin alike.", 9.0),
    ],
    # S4 — why an e-value here: sequential / anytime-valid
    "S4_Sequential": [
        ("So why bother turning an exact p-value into an e-value? Because of one thing a p-value cannot do cleanly: arithmetic across analyses.", 9.0),
        ("The load-bearing fact from Volume five. Honest e-values multiply. If two bets are run on independent data, the product is still a valid e-value.", 9.5),
        ("Picture patients arriving over time. Cohort one gives an e-value E-one. A new cohort arrives and gives E-two, on fresh, independent patients.", 9.5),
        ("You do not re-run anything. You just multiply: the running product E-one times E-two times E-three, and so on, accumulates the evidence for a lesion-symptom link.", 10.0),
        ("This product is a test martingale. Under the null its expected value stays at most one, no matter when you stop looking. That is anytime-valid inference.", 9.5),
        ("So you can watch a slowly accruing surgical cohort and stop the moment the product is large, with no peeking penalty and no pre-fixed sample size.", 9.5),
        ("One flip of a fair coin barely moves the needle. Ten heads in a row, multiplied, give about fifty-seven. Stacking is exactly where the power comes from.", 9.5),
    ],
    # S5 — across voxels with e-BH
    "S5_MultipleVoxels": [
        ("Now widen the lens from one contrast to a whole brain map. A lesion network map is tens of thousands of voxels, each with its own symptom contrast.", 9.5),
        ("Test them all and you face a multiplicity problem. The classic Benjamini-Hochberg procedure controls the false discovery rate, but it leans on the p-values behaving.", 9.5),
        ("And brain maps have heavy spatial dependence: neighboring voxels are highly correlated. That dependence breaks many p-value-based guarantees.", 9.5),
        ("Mint one e-value per voxel, by the calibration we just built, and run e-B-H, the e-value version of Benjamini-Hochberg, across all the voxels.", 9.5),
        ("The key property: e-B-H controls the false discovery rate under arbitrary dependence. No spatial-dependence model needed. The heavy correlation simply does not matter.", 10.0),
        ("So the recipe is one common currency end to end. Each voxel's symptom contrast becomes a fair bet, and e-B-H stacks them into honest map-wide error control.", 10.0),
    ],
    # S6 — caveat and scope
    "S6_Caveat": [
        ("A blunt caveat before you take any of this to a clinic. This chapter is an illustrative construction, to show the machinery, not a validated estimator.", 9.5),
        ("The exact e-value the published responses would report is not settled from our sources. So carry the flag: verify against the primary source for the exact estimator.", 10.0),
        ("What does not change is the question. This e-value answers the same symptom question as the Part five permutation test, just now sequentially and across analyses.", 9.5),
        ("And here is the boundary Volume five draws loudest. A valid e-value of the wrong null is worthless. E-values own accumulation and multiplicity, not correctness of the question.", 10.0),
        ("So if lesion size belongs in the null and you left it out, no amount of betting fixes that. The design and Freedman-Lane own confounding. A wrong null is still wrong.", 10.0),
        ("The e-value does not change that. It only lets a right null speak in a richer currency: evidence you can accumulate as patients arrive and control across a whole map.", 9.5),
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
