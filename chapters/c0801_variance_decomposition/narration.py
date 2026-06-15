"""Narration for c0801_variance_decomposition — "Single-target variance decomposition".

Source: responses/lnm_critique/sections/06_single_target.md

Every equation and number here is pulled from that section. The single-target
(FUS-VIM thalamotomy) geometry: every patient is lesioned at nearly the same
target l_0, plus a small per-patient offset delta_i. The map decomposes as
m_i = C l_0 + C delta_i; the constant C l_0 has zero across-patient variance, so
the critique's scattered-location mechanism cannot operate. Then preview three
moves toward a clean test.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — One target, many patients
    "S1_Setup": [
        ("Every prior section fought the critique on scattered lesions, strewn across the cortex. Now we move to the case the project actually lives in.", 9.0),
        ("Focused-ultrasound thalamotomy. Every patient gets a tiny ball of ablated tissue in the same structure, the ventral intermediate nucleus of the thalamus, a few millimeters across.", 10.0),
        ("So the seeds do not roam the brain. To first approximation, they sit right on top of each other. One location, not many.", 8.5),
        ("Write each patient's lesion l-sub-i as a shared target l-zero plus a small patient-specific offset delta-sub-i.", 8.0),
        ("Here l-zero is the common VIM core, the voxels essentially every ablation destroys. It is the same for every patient.", 8.5),
        ("And delta-sub-i is the patient-specific part: a few extra voxels at the rim because patient i got a bigger lesion, or a slight shift in where the focus landed.", 9.5),
        ("Patients differ here by lesion size and position-within-target, not by location-across-the-brain. The critique was built for the second kind of difference.", 9.0),
    ],
    # S2 — The maps
    "S2_Maps": [
        ("Now push that decomposition through the connectome. Patient i's map m-sub-i is C times l-sub-i.", 8.0),
        ("C is the fixed normative connectivity matrix, V voxels by V voxels, the same C as everywhere in this paper.", 8.5),
        ("Substitute l-sub-i equals l-zero plus delta-sub-i, and C distributes over the sum.", 7.5),
        ("So m-sub-i splits into two pieces: C l-zero plus C delta-sub-i.", 7.0),
        ("The first piece, C l-zero, is the connectivity fingerprint of the VIM itself. It is identical for everyone, the shared target map.", 9.0),
        ("The second piece, C delta-sub-i, is the only thing that varies from patient to patient. It carries the consequences of size and within-target position.", 9.5),
        ("Read that off the equation: between-patient differences in the maps come entirely from the small term, C delta-sub-i.", 8.5),
    ],
    # S3 — Variance kills the common term
    "S3_Variance": [
        ("Make that precise with variance. Var-sub-i means the spread of a quantity as we look across patients i.", 8.5),
        ("Take the across-patient variance of m-sub-i. It equals the variance of C l-zero plus C delta-sub-i.", 8.0),
        ("But C l-zero is a constant. It does not depend on i at all. Every patient contributes exactly the same C l-zero.", 8.5),
        ("And a constant has zero variance. Adding the same number to every patient shifts the whole cloud but never spreads it.", 8.5),
        ("So the shared term drops out. Var-sub-i of m-sub-i equals Var-sub-i of C delta-sub-i, full stop.", 8.0),
        ("All between-patient variance lives in the small term. And delta-sub-i is dominated by lesion size, plus a small position offset.", 9.0),
        ("This is the mutation in one line. Different-locations-sampling-one-C is replaced by graded-perturbation-of-one-seed.", 8.5),
    ],
    # S4 — The scattered-locations mechanism vanishes
    "S4_Mechanism": [
        ("Now watch the critique's engine try to turn. P1's mechanism needs many different lesion locations, all sampling the same C.", 9.0),
        ("Those scattered locations all project onto the leading connectome components, so the one-sample average converges on the backbone, no matter where the damage sits.", 10.0),
        ("That demonstration needs a population of scattered seeds to produce. Its premise is variance in lesion location.", 8.5),
        ("Here there is no scatter. There is one location, dosed at different sizes. Take the scatter away and you take away the demonstration.", 9.0),
        ("So the scattered-locations mechanism does not merely weaken. Its premise is simply gone. It cannot operate.", 8.5),
        ("What is left is a different object: a graded dose, size and position, mapped to a graded outcome. The single-target case is genuinely different.", 9.5),
    ],
    # S5 — Three moves for a clean test
    "S5_Plan": [
        ("Removing the scattered-lesion threat does not make this case safe. One threat survives the mutation: the shared backbone, C l-zero.", 9.0),
        ("Because the average single-target map is C l-zero, and that fingerprint is itself dominated by the connectome's hub structure. So the average is, once again, mostly backbone.", 10.0),
        ("Our job is to test the small part, C delta-sub-i, without letting the large shared part manufacture significance. Three moves do it.", 9.0),
        ("Move one: outcome-label permutation, size-protected. Shuffle the outcomes, with lesion size held fixed as a nuisance, so neither the backbone nor size can fake a result.", 10.0),
        ("Move two: strip the backbone. Project each map off the leading connectome subspace before testing, removing the shared C l-zero and lifting the small signal up.", 10.0),
        ("Move three: beat a degree baseline. Predict held-out outcomes and check you beat a model that uses only how hub-connected the lesion is.", 9.5),
        ("Move one fixes calibration, move two improves power, move three is the credibility bar. Together they set up the next three chapters.", 9.0),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:16s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':16s} target={grand:5.1f}s ({grand/60:.1f} min)")
