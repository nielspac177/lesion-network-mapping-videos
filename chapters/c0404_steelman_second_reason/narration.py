"""Narration for c0404_steelman_second_reason — "Steelman, and the second reason".

Source: responses/lnm_critique/sections/03_the_right_null.md
        responses/lnm_critique/papers/REBUTTAL_sound.md

We first steelman the location null: for a claim genuinely ABOUT location, the
location null is the correct referee and the LNM average map honestly fails it.
Then we give the rebuttal full standing via a SECOND, independent reason
(Siddiqi et al. p.5): a random, non-overlapping ensemble is the wrong reference
class for real symptom-causing lesions, which overlap and are spatially
non-random. Both reasons push the same direction. Then we bridge to the symptom
null: change the question and the reference, the backbone cancels, signal
survives, zero false positives in a thousand iterations at t above ten.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — steelman the critique: for a LOCATION claim, the location null is right
    "S1_Steelman": [
        ("Before we defend lesion network mapping, we owe the critique its strongest form. Let us build that steelman honestly.", 8.5),
        ("A null model is a question. The random-lesion null asks one precise thing: is the location of these lesions special?", 8.5),
        ("You scatter fake lesions, push each through L N M, and ask whether the real map stands out from that crowd of fakes.", 8.5),
        ("Now suppose a paper's claim genuinely is about location: lesions here, rather than there, produce this network.", 8.0),
        ("For that claim, the location null is exactly the right referee. It is a valid test of the location hypothesis.", 8.0),
        ("And on that question the L N M average maps genuinely fail. Van den Heuvel and colleagues report seventy of seventy-eight maps failing a random synthetic-lesion null.", 9.5),
        ("Seventy-one of seventy-eight also fail a location-permutation null that preserves modular prevalence. We concede this fully.", 8.5),
    ],
    # S2 — the right tool for the right claim; the error is using it to certify symptom
    "S2_RightToolWhen": [
        ("So the location null is not broken. It is a valid, well-aimed test, as long as the scientific claim really is about location.", 9.0),
        ("If a paper says this location is special, the location null is the correct judge, and for scattered cortical lesions it correctly says no.", 9.5),
        ("The backbone model is why. A seed's map, m sub ell, is roughly lambda one times the projection u one transpose ell, all along one fixed direction, u sub one.", 9.5),
        ("So the fake maps and the real map look alike. The observed value sits dead center in the null. Nothing rejects, and rightly so.", 9.0),
        ("That is honest failure of a real claim. The error is not in the null; it is in what people do with the verdict.", 8.5),
        ("The over-reach is using that same location verdict to certify, or to deny, a symptom relationship. That is a different claim entirely.", 9.0),
        ("A non-significant location test gets read as L N M does not work. But it only means the location question was the wrong one to ask.", 9.0),
    ],
    # S3 — second, independent reason: wrong reference class (the rebuttal's escape hatch)
    "S3_WrongReference": [
        ("Now the second reason the location null is mis-aimed, and this one is not ours. It belongs to the responders, Siddiqi and colleagues.", 9.0),
        ("The random ensemble scatters lesions randomly and non-overlapping across the brain. That is its built-in reference population.", 8.5),
        ("But real lesions that cause a specific symptom overlap, and their spatial distributions are not random. Quote, page five.", 8.5),
        ("Lesions causing amnesia repeatedly sample the hippocampus and its connected regions, and are far less likely to sample the motor cortex.", 9.0),
        ("So a null that resamples random, non-overlapping blobs discounts exactly the structure that makes a symptom-causing lesion set special.", 9.0),
        ("It models an impossible population: scattered, independent lesions that no real disease produces. The reference class is simply wrong.", 9.0),
        ("The rebuttal even traces the headline false-positive rate to this. The high rate came from a simulation assuming high lesion overlap.", 9.0),
        ("With low overlap, the regime of randomly drawn real lesions, that false-positive rate collapses. We will witness the number shortly.", 8.5),
    ],
    # S4 — two reasons, same direction
    "S4_TwoReasons": [
        ("Step back and put the two reasons side by side. They are independent, and they push the location null in the very same direction.", 9.0),
        ("Reason one is about the question. The backbone blurs all locations alike, so a test asking is this place special can never reject.", 9.0),
        ("That reason is ours, and it is a statement about the location-versus-symptom question. Wrong question, guaranteed non-rejection.", 8.5),
        ("Reason two is about the reference class. A random, non-overlapping ensemble is the wrong comparison population for real lesions.", 8.5),
        ("That reason is theirs, and it is a statement about random versus real. The null models a population that does not exist.", 8.5),
        ("Either one alone already makes the location null the wrong question. Together they make it the obviously wrong one.", 8.0),
        ("And both point the same way: on average, the location null under-rejects. It will not find a true lesion-symptom signal even when one is there.", 9.5),
    ],
    # S5 — bridge to the symptom null
    "S5_Bridge": [
        ("So how do we fix it? Two moves. Change the question, and change the reference class. That is the bridge to Part five.", 8.5),
        ("Change the question from a location claim to a symptom-label contrast: do these labels track these fixed lesions more than chance allows?", 9.5),
        ("Change the reference from random blobs to label permutations. Keep every lesion exactly in place; only shuffle who is impaired and who is spared.", 9.5),
        ("Now the backbone, the same direction u sub one that broke the location null, becomes a label-free constant sitting on both sides of the contrast.", 9.5),
        ("It is independent of the symptom label, so it cancels out of the difference, exactly. The backbone vanishes; only label-dependent signal survives.", 9.5),
        ("And the witness is concrete: zero false positives in one thousand iterations at the standard specificity threshold, t above ten.", 9.0),
        ("Leakage of four point six percent appears only when the threshold is dropped to a sub-standard t of three. Part five proves all of this.", 9.0),
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
