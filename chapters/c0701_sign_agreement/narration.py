"""Narration for c0701_sign_agreement — "Sign-agreement convergence maps".

Source: responses/lnm_critique/sections/05_the_convergence_trap.md

This chapter DEFINES the convergence map (the sign-agreement operator) and states
the convergence claim fairly, then poses the question that c0702 answers with the
2^(1-K) baseline. It does NOT yet rebut; it sets the object up honestly.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — What a convergence map is
    "S1_Idea": [
        ("A convergence map is built from several lesion network maps at once. You keep only the voxels where they all point the same way.", 9.5),
        ("When that happens it feels like discovery: many maps, independently derived, agreeing on the same circuit.", 8.5),
        ("To make it precise, fix the brain as a grid of voxels, and write little-v for one voxel.", 7.5),
        ("Let r-sub-k of v be the value of study k's map at voxel v: its connectivity, or its Fisher-z correlation, at that spot.", 9.0),
        ("We have K studies in all, so over the same voxels we hold K maps: r-one, r-two, all the way to r-sub-K.", 8.5),
        ("The one tool we need is the sign. Sign of r is plus one if the value is positive, minus one if it is negative, and zero if it is exactly zero.", 9.5),
        ("So each map, at each voxel, casts a vote: pointing up, pointing down, or staying silent. The convergence map asks where the votes agree.", 9.0),
    ],
    # S2 — The agreement statistic
    "S2_Formula": [
        ("Here is the agreement statistic, voxel by voxel. Capital-A of v, the sign-agreement operator.", 8.0),
        ("Pick one map as the reference, say map one. Its sign at this voxel, sign of r-one of v, is the shared sign we will record.", 9.0),
        ("Inside, for each study k, we test one thing: does sign of r-sub-k of v equal sign of r-one of v?", 8.5),
        ("That test is the indicator, the one in blackboard brackets. It is one when the signs match, and zero when they do not.", 8.5),
        ("Now the big wedge: the logical AND, taken over all K studies from k equals one to K. It is one only if every single map matches the reference.", 9.5),
        ("Finally multiply that AND by the reference sign itself. So A of v inherits the shared plus or minus, but only when everyone agrees.", 9.0),
        ("Read the whole thing as a value in the set minus one, zero, plus one. The agreement, and its direction, in a single number per voxel.", 9.0),
    ],
    # S3 — Reading the map
    "S3_Meaning": [
        ("So what does A of v actually equal? It is plus one or minus one only where all K studies share map one's sign. Everywhere else it is zero.", 9.5),
        ("Picture a small grid of voxels, each holding three studies' signs stacked together. We light a cell only when the stack agrees.", 9.0),
        ("Where all three arrows point up, the cell turns plus one. Where all three point down, it turns minus one.", 8.0),
        ("But mix even one disagreeing arrow into the stack, and the AND collapses to zero. The cell goes dark.", 8.0),
        ("The lit cells are the convergence support: the set of voxels where A of v is not zero. People report that support, and how big it is.", 9.5),
        ("It is meant to look like cross-study consensus: independent maps converging on the same circuit, drawn for the eye.", 8.5),
        ("Equivalently, the support is where all maps are positive, joined with where all maps are negative. Agreement is an intersection of half-spaces.", 9.0),
    ],
    # S4 — The convergence claim
    "S4_Claim": [
        ("Now the claim that papers attach to this picture. Let us state it as strongly and as fairly as it deserves.", 8.0),
        ("Many maps, derived independently from different cohorts, all agree on the same voxels. Surely that is the disease network shining through.", 9.0),
        ("The reading is: widespread agreement is independent convergence onto a real, disease-specific network in the brain.", 8.5),
        ("And there is an honest case for it. If several disorders all implicate one hub, that recurrence is real and might matter clinically.", 9.0),
        ("A convergence map is a perfectly good description of which connectome features keep recurring across conditions.", 8.0),
        ("So we grant the interpretation full standing. A big agreement set is consistent with a shared disease-specific circuit. Hold that thought.", 9.0),
    ],
    # S5 — The question to ask
    "S5_Question": [
        ("Before we believe agreement is a finding, there is one question every convergence map must face. Is the agreement actually surprising?", 9.0),
        ("Surprise is not absolute. It is measured against a baseline: how often would these K maps agree just by chance, with no shared circuit?", 9.5),
        ("Striking against what? A third of the brain agreeing across six cohorts sounds impressive only relative to some yardstick.", 8.5),
        ("So the next step is to compute that yardstick. Suppose the K signs were independent coins, each plus or minus with probability one-half.", 9.0),
        ("Then the chance that all K agree is two to the power one minus K. That is the independent-signs baseline we build next.", 8.5),
        ("If the observed agreement merely matches that baseline, it is not evidence. Only agreement that beats the right baseline can be.", 8.5),
        ("That is the whole question we carry forward: agreement is cheap until you show it is more than the baseline gives you for free.", 9.0),
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
