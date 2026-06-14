"""Narration for c0505_freedman_lane — "Freedman-Lane and the size nuisance".

Source: responses/lnm_critique/sections/03_the_right_null.md
        responses/lnm_critique/papers/REBUTTAL_sound.md

Lesion volume is a confound: it correlates with both the map magnitude (larger
lesions project more strongly onto the backbone, beta_i correlates with volume)
and often the symptom. A naive raw-label shuffle can leak that size effect as
false signal. Freedman-Lane fixes this: regress the outcome on the nuisance,
take the covariate-adjusted residuals, and permute THOSE, not the raw labels.
Permuting residuals holds the size effect fixed while testing only the
symptom-map link, and the backbone cancellation from Part 5 still holds in
residual space. We keep the source's honesty flag: whether the published
responses used Freedman-Lane or a raw shuffle is not settled from the abstracts
[verify against primary source]; the size-protection recommendation is ours.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — lesion volume is a confound; define the nuisance covariate s_i
    "S1_Nuisance": [
        ("There is one nuisance we cannot ignore in lesion network mapping: the sheer size of the lesion.", 7.5),
        ("Lesion volume correlates with the map magnitude. The backbone loading beta sub i equals lambda one times u sub one dotted with the lesion mask ell sub i, so a larger lesion projects more strongly onto the backbone direction u sub one.", 11.0),
        ("It often correlates with the symptom too. Bigger lesions tend to cause more, or more severe, deficits.", 8.0),
        ("So volume is a label-correlated nuisance. It is tied to both sides at once: to the map, and to the outcome we are testing.", 9.0),
        ("Let us name it. Write s sub i for the lesion volume of patient i, a single number per patient.", 8.0),
        ("Here is the danger. A naive shuffle of the raw symptom labels can leak that size effect, and dress it up as false signal.", 9.0),
        ("If we do not protect s sub i, the test may reject not because the symptom tracks the wiring, but merely because it tracks lesion size.", 9.5),
    ],
    # S2 — Freedman-Lane: regress out nuisance, permute the residuals
    "S2_Residualize": [
        ("The fix has a name: Freedman and Lane. The idea is to permute the part of the data the nuisance does not already explain.", 9.0),
        ("Step one. Regress the outcome y on the nuisance s. Fit the straight-line relationship between symptom and lesion volume.", 8.5),
        ("Step two. Take the residuals. The residual e sub i is the outcome minus its size-predicted part: what y has left after size is accounted for.", 9.5),
        ("Step three. Permute those residuals across patients, not the raw outcome. Shuffle e, the size-adjusted part, and only that.", 9.0),
        ("The contrast between the two: a naive shuffle permutes y itself, carrying the size effect along. Freedman and Lane permutes e, with size already removed.", 10.0),
        ("So the recipe is three short moves. Fit y on s. Take the residuals e. Shuffle the residuals to build the null.", 8.5),
    ],
    # S3 — why residual space: size held fixed, backbone still cancels
    "S3_WhyResidual": [
        ("Why permute in residual space at all? Because residualizing holds the size effect fixed while we test only the symptom-to-map link.", 9.5),
        ("Write each patient's residual as e sub i equals y sub i minus the fitted line, b times s sub i. The b times s sub i piece is the nuisance prediction.", 9.5),
        ("That nuisance piece is the same in every permutation. We never reshuffle it, so the size effect cannot move from one shuffle to the next.", 9.0),
        ("What is left to permute, e sub i, is by construction uncorrelated with the volume s sub i. Size has been projected out.", 9.0),
        ("Now recall the backbone split from before. Each map x sub i is beta sub i times u sub one, the label-free backbone, plus a residual r sub i.", 9.5),
        ("The backbone loading beta sub i correlates with lesion volume, so once we regress on s, that size-correlated backbone variance is removed.", 9.5),
        ("Whatever backbone variation is left is orthogonal to size and still label-independent. So the cancellation from Part five holds in residual space too.", 10.0),
    ],
    # S4 — an honest caveat: FL vs raw shuffle not fully settled here
    "S4_OpenQuestion": [
        ("Now an honest caveat, because the source insists on one. We must not overclaim what the published responses actually did.", 8.5),
        ("The rebuttal describes a symptom-label permutation: shuffle each patient's clinical symptom with a different patient's network map.", 9.0),
        ("But whether that is exactly Freedman and Lane, permuting size-adjusted residuals, or a plain raw-label shuffle, is not settled from the abstracts alone.", 10.0),
        ("In fact the wording of the rebuttal reads closer to a raw-data shuffle. Verify against the primary source before asserting otherwise.", 9.0),
        ("The math we prove, exact validity and backbone cancellation, holds either way, given exchangeability of the labels.", 8.5),
        ("We recommend Freedman and Lane specifically, because lesion size is a label-correlated nuisance a raw shuffle does not protect. That recommendation is ours.", 9.5),
        ("So keep the caveat plainly in view. Take the size-protected recipe as our advice, not as a claim about what the preprints already did.", 9.0),
    ],
    # S5 — takeaway: the recipe
    "S5_Takeaway": [
        ("Let us gather the takeaway. Size-protected permutation gives a valid test even when lesion volume confounds both the map and the symptom.", 9.5),
        ("The recipe in four words. First, residualize the nuisance: regress the outcome on lesion volume and keep what is left over.", 9.0),
        ("Second, permute the residuals, not the raw labels. This holds the size effect fixed across every shuffle of the null.", 8.5),
        ("Third, the backbone still cancels. It is label-free and size-correlated, so it drops out in residual space exactly as it did before.", 9.5),
        ("Fourth, the signal survives. Only genuine, size-independent, label-dependent structure can move the statistic and reject the null.", 9.0),
        ("Residualize the nuisance, permute the residuals, the backbone cancels, the signal survives. That is a test that is honest about size.", 9.5),
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
