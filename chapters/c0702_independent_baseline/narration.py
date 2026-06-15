"""Narration for c0702_independent_baseline — "The independent baseline".

Source: responses/lnm_critique/sections/05_the_convergence_trap.md
        (Baseline 1: "if the maps were independent coins, agreement would be rare")

This chapter builds the FAIR yardstick for convergence maps: if the K cohort
maps' signs at a voxel were independent fair coins, then Pr[all K agree] is
exactly 2^(1-K). We derive it, read off K=2, 4, 8, and note that in THIS world a
big agreement set really would be impressive evidence. The catch — handed to the
next chapter — is that LNM maps are NOT independent; they share the connectome
backbone, so the coin model is the wrong null.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — set up the independent fair-coin model
    "S1_Setup": [
        ("To judge a convergence map we need a yardstick: how much agreement should we expect by chance? Let us build the simplest one.", 9.5),
        ("Fix a single voxel. Across capital-K studies, each study's map has a sign there, either plus or minus, pointing one way or the other.", 9.5),
        ("Now make the cleanest possible assumption. Suppose those signs were independent fair coin flips, with no shared structure at all.", 9.0),
        ("So for each study k, the sign is plus with probability one-half, and minus with probability one-half.", 8.0),
        ("And crucially, independent across k: knowing study one's sign tells you nothing about study two's. Pure, separate coins.", 8.5),
        ("This is the picture where every map was derived on its own, with no common cheat sheet. Hold onto it; it is the honest baseline.", 9.0),
    ],
    # S2 — derive Pr[all K agree] = 2^(1-K)
    "S2_Derive": [
        ("The convergence map keeps a voxel only where all capital-K signs match. So we want the probability that all K agree.", 8.5),
        ("All K agree means one of two clean events: either every coin came up plus, or every coin came up minus.", 8.0),
        ("Fix the reference, study one. The other K minus one studies must each match it, and each matches with probability one-half.", 9.0),
        ("Multiply those independent one-halves: K minus one of them give one-half to the power K minus one. That is the all-plus block, and equally the all-minus block.", 9.5),
        ("The all-plus and all-minus events are disjoint, so we add them. Two copies of one-half to the K, which is two to the one minus K.", 9.5),
        ("Decode that exponent. The one in front is from doubling, plus or minus. The minus K is the cost of demanding all K coins line up.", 9.0),
        ("So under independence, the expected fraction of the brain that converges is exactly two to the one minus K. It shrinks geometrically.", 9.0),
    ],
    # S3 — the numbers, the curve drops fast
    "S3_Numbers": [
        ("Put real numbers in. With K equals two maps, two to the one minus two is one-half. Two coins agree fifty percent of the time.", 9.0),
        ("With K equals four, it is two to the minus three, one-eighth, twelve-point-five percent. Already much rarer.", 8.5),
        ("With K equals eight, it is two to the minus seven, about zero-point-eight percent. Less than one voxel in a hundred.", 9.0),
        ("Plot it and the curve plunges. Each extra independent study roughly halves the agreement you would expect by chance.", 8.5),
        ("So in the independent world, unanimous agreement across many studies is genuinely rare, and genuinely impressive.", 8.5),
        ("Observing a big convergence set here would be wildly improbable under chance, so it would be a real signal worth reporting.", 9.0),
    ],
    # S4 — so agreement looks like strong evidence
    "S4_SoFar": [
        ("Step back and say what we have earned. If the independence model held, a lit-up convergence map would be strong evidence.", 9.0),
        ("Many maps, separately derived, all pointing the same way at the same voxels, would beat the tiny two-to-the-one-minus-K baseline.", 9.5),
        ("That is the intuition almost everyone runs on. A striking agreement map feels like the disease network shining through.", 8.5),
        ("And it is exactly this independence model, usually unspoken, that licenses reading convergence as validation of a real circuit.", 9.0),
        ("So the whole inference quietly rests on one assumption: that the maps are independent coins. Make that assumption explicit.", 9.0),
        ("Because the moment we name it, we can ask the only question that matters: is it actually true for lesion network maps?", 9.0),
    ],
    # S5 — the catch: not independent, they share the backbone
    "S5_Catch": [
        ("Here is the catch, and it dismantles the whole baseline. Lesion network maps are not independent coins.", 8.5),
        ("Every map is computed against the same fixed connectome. They share its dominant structure, the backbone we called u-sub-one.", 9.0),
        ("Think of a classroom where every student copied the same cheat sheet before the exam. Now they all match almost everywhere.", 9.0),
        ("And the matches tell you nothing about whether anyone understood the material; they tell you they shared a cheat sheet.", 8.5),
        ("So the two-to-the-one-minus-K yardstick is the wrong null. It assumes a separateness the maps simply do not have.", 9.0),
        ("Next we replace the coin-flip model with a shared-backbone model. Here r-sub-k-of-v, cohort k's map value at voxel v, equals the common backbone mu-of-v plus a little cohort wobble epsilon-sub-k.", 10.5),
        ("Under that model agreement is large by construction, and a striking convergence map becomes the default, not a discovery.", 9.0),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:12s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':12s} target={grand:5.1f}s ({grand/60:.1f} min)")
