"""Narration for c0802_outcome_label_perm — "Move 1: outcome-label permutation".

Source: responses/lnm_critique/sections/06_single_target.md
        responses/lnm_critique/sections/03_the_right_null.md

Move 1 of the single-target defeat. In focused-ultrasound thalamotomy every lesion
sits in one tiny target, so each patient's map splits as m_i = C l_0 + C delta_i:
a shared VIM fingerprint C l_0 plus a small patient-specific part C delta_i. We
want to know whether the patient-specific connectivity relates to the clinical
OUTCOME (tremor relief). Move 1 tests that link by permuting the outcomes, with
Freedman-Lane protecting the lesion-size nuisance, so neither the shared backbone
nor lesion size can manufacture a result.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the goal: does the per-patient map relate to outcome?
    "S1_Goal": [
        ("Move one. We want one clean question, and a valid way to answer it, even with a single tiny target.", 8.5),
        ("The question is this: does each patient's lesion map relate to the clinical outcome, the tremor relief?", 8.5),
        ("Write y sub i for patient i's outcome. It can be binary, relief or no relief, or a graded score.", 8.5),
        ("And m sub i is patient i's map: the lesion l sub i pushed through the connectome C, that is C times l sub i.", 9.0),
        ("In one tiny target every lesion sits on the same spot, so the map splits in two. A shared part, C times l zero.", 9.0),
        ("Plus a small patient-specific part, C times delta sub i. C l zero is the target's own fingerprint, identical for everyone.", 9.0),
        ("So the genuine outcome signal, if there is any, can only live in that small piece, C delta sub i. That is what we must test.", 9.5),
    ],
    # S2 — permute the outcomes; the shared map is held fixed
    "S2_Permute": [
        ("To get a null, we shuffle. We keep every lesion and every map exactly where it is, and reassign the outcomes across patients.", 9.5),
        ("Each shuffle pairs a patient's map with someone else's outcome, then we recompute the map-versus-outcome association.", 9.0),
        ("Do that many times. The real association is meaningful only if it beats almost every shuffled one.", 8.5),
        ("Now watch the shared map. C l zero is the same constant in every patient's map, observed and shuffled alike.", 8.5),
        ("Shuffling outcomes never moves it. So it contributes identically to the real statistic and to every null statistic.", 8.5),
        ("Present on both sides of the contrast in every labeling, it has no leverage. It cancels, and cannot fake an association.", 9.0),
        ("That is the same cancellation we proved for the scattered case in chapter five. Nothing about it needed scattered lesions.", 8.5),
    ],
    # S3 — Freedman-Lane protects size
    "S3_SizeProtect": [
        ("There is one more nuisance, and here it is the dangerous one. Lesion size correlates with outcome.", 8.0),
        ("Write s sub i for size: the number of destroyed voxels, the count of ones in l sub i. Bigger ablation, different relief.", 9.0),
        ("And in a single target, size is most of what delta sub i is. It is both the main confound and the main source of variance.", 9.0),
        ("So a naive shuffle of the raw outcome is not enough. It would scramble the size effect and the map effect together.", 8.5),
        ("Freedman-Lane fixes this. First regress the outcome on the nuisances, size, age, baseline severity, and keep the residuals.", 9.0),
        ("Then permute only those residuals, add them back, and refit. The size effect, gamma times s sub i, stays put.", 9.0),
        ("So both C l zero and the size effect are held fixed. The shuffle disturbs only the outcome-to-map link. That, and nothing else, is tested.", 10.0),
    ],
    # S4 — why it is valid here
    "S4_Valid": [
        ("Why is this test valid, even with one target and patients in the tens? Two reasons, and we have proved both.", 8.5),
        ("First, exchangeability. Under the null the outcome labels are interchangeable across the fixed maps.", 8.0),
        ("And by permutation exactness, recall chapter five, counting labelings gives an exact test, with no distributional assumption.", 9.0),
        ("It does not matter that the maps are ugly, low-rank, or backbone-dominated. Exactness cares only that the labels are exchangeable.", 9.0),
        ("Second, the two things that could cheat are controlled. The shared backbone cancels; the size effect is held fixed by Freedman-Lane.", 9.5),
        ("So the single target, far from breaking the test, makes it cleaner. There is one location, not a confusing scatter.", 9.0),
        ("The question is exactly answerable: given these fixed lesions, does the outcome track the patient-specific connectivity more than chance.", 9.5),
    ],
    # S5 — takeaway
    "S5_Takeaway": [
        ("So here is move one in one breath. It turns a single-target study into a valid inference about the outcome.", 8.5),
        ("Shuffle the outcomes; the shared target map C l zero, being label-independent, drops out of the contrast.", 8.5),
        ("Protect size with Freedman-Lane, so the dominant dose confound cannot masquerade as a network effect.", 8.5),
        ("What is left is an exact, finite-sample test of the only thing that can carry genuine signal, C delta sub i against outcome.", 9.5),
        ("The result is immune to the shared-target map and to the size confound, the two threats this geometry actually has.", 9.0),
        ("Move one fixes calibration: the null cannot lie. Next moves strip the backbone for power, and demand out-of-sample proof.", 9.0),
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
