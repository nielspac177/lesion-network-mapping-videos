"""Narration for c0304_convergence_trap_stated — "The convergence trap, stated".

Part 3, the stated form of the convergence trap. Every seed — real, synthetic,
random — projects onto the same backbone u-one of C, so any AVERAGED map lands in
one cone. The group-average map is, by construction, the hub map: nonspecific. We
concede the camera completely: as a one-sample description, convergence is trivial,
and the rebuttal (Siddiqi et al.) agrees the average converges to the degree map.
But the CONTRAST under a symptom-label null is a different camera: it subtracts the
shared backbone away algebraically, the hub cancels, and the witness is zero false
positives in one thousand iterations at threshold t above ten. Bridge to Parts 4-5:
a failed null is often a failed question.

Sources (quote/number-cited):
  responses/lnm_critique/sections/05_the_convergence_trap.md
  responses/lnm_critique/papers/P1_critique.md  (Eq. 3; r=0.44; 0/1000 at t>10;
    same-symptom 0.44 / different 0.09 / degree 0.16; Dice curve p.1243)

Each beat is (text, seconds): shown as subtitle and spoken by the TTS pass. The
number of play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # ------------------------------------------------------------------
    # S1 — the funnel: every seed points along the backbone u_1
    # ------------------------------------------------------------------
    "S1_Funnel": [
        ("Here is the trap, stated cleanly. Every lesion seed you can hand to the method points in nearly the same direction.", 9.0),
        ("Recall the geometry. The connectome C has one giant pattern, the backbone u-one, scaled by its huge eigenvalue lambda-one. Every map m equals C times ell inherits it.", 11.0),
        ("So take three completely different seeds. A real symptom lesion. A synthetic blob. A purely random set of voxels.", 8.5),
        ("Each one gets multiplied by C, and each one comes out tilted toward the same backbone u-one. Three arrows, one cone.", 9.0),
        ("That is the funnel. The connectome is a single fixed matrix, so whatever you pour in, the leading component lambda-one u-one is what pours out.", 10.0),
        ("And here is the consequence that does all the damage. If you average any pile of these maps, the average lands inside the cone too, pointing along u-one.", 10.0),
        ("It does not matter whether the seeds were addiction lesions or coin-flip noise. The averaged direction is owned by lambda-one, a property of C alone.", 9.5),
    ],
    # ------------------------------------------------------------------
    # S2 — the average IS the hub map, by construction
    # ------------------------------------------------------------------
    "S2_AverageIsHub": [
        ("Let us name what sits at the bottom of that funnel. The group-average map equals the hub map, and it is nonspecific by construction.", 10.0),
        ("Write the critique's own bookkeeping. L N M equals the sum over patients of M times C. This is their equation three.", 9.0),
        ("M is the lesion matrix, rows are patients, columns are regions, a one where a lesion covers a region. C is the fixed connectome. Summing the selected rows is just averaging them.", 11.0),
        ("As coverage fills in and M approaches the identity, the averaging copies C, and the row-sum of C is its degree. That degree vector is the hub map.", 10.5),
        ("So the endpoint of the funnel has a name: degree, the row-sum of the connectome. Well-connected hubs dominate it, regardless of disease.", 9.5),
        ("And it arrives fast. Just ten or more heterogeneous lesions already correlate above zero-point-four-four with degree. Twenty to twenty-five push it past zero-point-six-two.", 10.5),
        ("So a shared endpoint certifies the funnel, not the lesion. When many maps agree, they are agreeing on u-one, the part of C every seed had in common.", 10.0),
        ("The convergence map, the place people read agreement as discovery, is the descriptive shadow of this backbone. It redraws the hub. It does not reveal a circuit the disease carved.", 11.0),
    ],
    # ------------------------------------------------------------------
    # S3 — concede the camera: as a description, it is broken
    # ------------------------------------------------------------------
    "S3_ConcedeCamera": [
        ("Now we concede, fully and without hedging. As a description, the camera is broken.", 7.5),
        ("Treat the group-average as a one-sample photograph of the stack, and convergence is trivial. Of course every average lands on the backbone. That was forced by C.", 10.5),
        ("So a significant convergence map, by itself, is not evidence of a disease-specific network. The agreement was almost free, and anything you got for free cannot pay for an inference.", 11.0),
        ("And the rebuttal, Siddiqi and colleagues, says so out loud. They agree the averaging will converge on the row-summation vector of C, the degree map.", 10.0),
        ("They write, we fully agree with this, assuming the connectome is sampled randomly. So under uniform random sampling, both sides agree the camera converges to degree. There is no fight left about that average.", 11.0),
        ("So we give the critique its narrow conclusion in full. Under uniform, non-overlapping sampling, the one-sample average map of a symptomatic group is backbone-dominated, hence nonspecific. Conceded.", 11.0),
        ("Hold onto exactly what was conceded, though. It is a fact about one object, the average, built by one machine, the camera. Nothing yet has been said about any other machine.", 11.0),
    ],
    # ------------------------------------------------------------------
    # S4 — but the contrast is a different camera
    # ------------------------------------------------------------------
    "S4_ButContrast": [
        ("But there is a second camera, and it photographs a different thing. The court does not average. It contrasts.", 9.0),
        ("The object is the contrast under a symptom null. Take the average over patients who have the symptom, subtract the average over those who do not, and shuffle only the labels to test it.", 11.0),
        ("Split every map into two pieces. A backbone piece, b, which is lambda-one times the lesion's overlap with u-one, times u-one. And a residual, r, everything left over.", 11.0),
        ("Here is the single load-bearing fact. The backbone piece b depends on where the lesion sits in the connectome. It does not depend on the symptom label the patient carries.", 10.5),
        ("So when you subtract the impaired side from the spared side, the backbone is present identically on both sides, and it cancels. The hub subtracts away algebraically.", 10.5),
        ("The very thing that made the camera nonspecific, the backbone in every map, is the thing that makes it inert in the court. One mechanism, opposite fates.", 10.0),
        ("And the witness is hard. With the right label-shuffling null, at threshold t above ten, the contrast returns zero false positives in one thousand iterations.", 10.0),
        ("So the same connectome that funnels every average onto the hub lets the contrast carry genuine, label-linked signal. The backbone is the confound for one camera and inert for the other.", 11.0),
    ],
    # ------------------------------------------------------------------
    # S5 — bridge to sensitivity and specificity (Parts 4-5)
    # ------------------------------------------------------------------
    "S5_Bridge": [
        ("Step back and look at what we have. Two cameras pointed at the very same maps, and opposite fates.", 8.5),
        ("The average is dominated by the backbone and is nonspecific. The contrast, under the label null, has the backbone subtracted away by construction. Same matrix C, opposite verdicts.", 11.0),
        ("So the lesson is sharp. A failed null is often a failed question, not a failed method. Convergence failed because the average asked the wrong thing.", 10.0),
        ("That is why the next two parts split the question in two. Sensitivity asks: does a real effect light the map up at all?", 9.0),
        ("Specificity asks the harder thing: does it light up more for this symptom than for a shuffled label? That is the test where the backbone must cancel.", 10.0),
        ("So we will build the symptom-label permutation explicitly, and watch the backbone term, lambda-one times the loading difference, vanish from the contrast.", 10.0),
        ("Two cameras, opposite fates. The camera is conceded. The court is what comes next.", 7.5),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:20s} beats={len(beats):2d}  target={total:6.1f}s  "
              f"words={words:3d}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':20s} target={grand:6.1f}s ({grand/60:.1f} min)")
