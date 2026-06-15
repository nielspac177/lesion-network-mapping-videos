"""Narration for c0901_first_order_disconnection — "First-order disconnection only".

Source: responses/lnm_critique/sections/07_biological_limits.md
        responses/lnm_critique/papers/P3_biolimits.md

This chapter states P3's biological-limitations charge at its STRONGEST: a static,
first-order normative connectome C models only direct (one-hop) disconnection, and
is structurally blind to dynamics, plasticity, higher-order interaction, and
nonlinearity. This is a ceiling on the MODEL CLASS, distinct from the group-average
critique (P1) — even a perfect symptom contrast inherits the limits of a static
linear C. The chapter sets up the empirical ceiling that c0902 quantifies.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the text
is the subtitle in manim AND the spoken line. The number of play_beat()/wait_beat()
calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — what the linear model assumes
    "S1_Model": [
        ("Every lesion network map starts from one modeling choice: the brain is a static, linear connectome.", 8.5),
        ("In symbols, the map equals C times l. The map m, on the left, is what each lesion projects across the brain.", 9.0),
        ("C is the connectome: a fixed, region-by-region matrix of typical wiring, the same for every patient.", 9.0),
        ("And l is the lesion: a vector that is one where the injury sits, and zero everywhere it does not.", 8.5),
        ("So C times l reads off, for each region, how strongly the lesioned tissue connects to it through the average wiring.", 9.5),
        ("That linearity buys a lot: it is fast, transparent, and one matrix multiply gives you a whole-brain fingerprint.", 9.0),
        ("But notice what we have already committed to. C is frozen, C is shared, and the only operation is a single product.", 9.0),
    ],
    # S2 — only direct disconnection
    "S2_FirstOrder": [
        ("Look closely at what C times l can actually represent. It captures first-order disconnection, and only that.", 9.0),
        ("First-order means direct: which regions lose their input because they were wired straight to the lesioned tissue.", 9.0),
        ("Picture the lesion as a source. C times l lights up its immediate neighbors, the regions one hop away.", 8.5),
        ("It is a single step out from the injury, weighted by the strength of each direct connection in C.", 8.5),
        ("This is P3's first axis: the strength of direct disconnection between the lesion and the rest of the brain.", 9.0),
        ("And P3 are blunt about it. This first axis is the only one lesion network mapping captures.", 8.0),
        ("Everything that happens beyond that one hop, the model simply does not see.", 7.0),
    ],
    # S3 — what it cannot represent
    "S3_Missing": [
        ("So let us name, concretely, what a static linear C leaves out. There are four omissions, and each is biological.", 9.0),
        ("No dynamics. C is a single snapshot, so it cannot represent how network states evolve in time after an injury.", 9.0),
        ("No plasticity. The brain rewires, sprouts axons, and remaps to the other hemisphere; a frozen C cannot model that recovery.", 9.5),
        ("No higher-order interaction. Effects ripple through regions the lesion never directly touched; C stops at one hop.", 9.0),
        ("No nonlinearity. The response is not a proportional loss. Networks swing between hyperconnected and hypoconnected.", 9.0),
        ("P3 put it sharply: by construction, the model cannot tell hyperconnected from hypoconnected or transitioning networks.", 9.0),
        ("Time, compensation, and cascades: three things a static linear map cannot express, no matter how it is fit.", 8.5),
    ],
    # S4 — a model-class limit
    "S4_Scope": [
        ("Here is the crucial point about scope. This limit is not the group-average critique we answered earlier.", 8.5),
        ("That earlier charge was narrow: it was about the average of the per-lesion maps collapsing to the connectome's degree, and only under uniform, non-overlapping sampling.", 9.5),
        ("This one is different. It is a ceiling on the entire model family, the family of static, linear maps m equals C l.", 9.5),
        ("It holds for any C, and for any way you read out the result, average or contrast alike.", 8.0),
        ("So even a perfect symptom contrast, one that cancels the backbone exactly, still lives inside this family.", 9.0),
        ("It inherits the limits of a static linear C, because no operation on C recovers a dimension C never contained.", 9.5),
        ("You cannot residualize, reweight, or contrast your way into time, plasticity, or higher-order cascades.", 9.0),
    ],
    # S5 — bridge to the ceiling
    "S5_Bridge": [
        ("That raises the natural question. How much does this model-class limit actually bound real prediction?", 8.5),
        ("A ceiling on what a model can represent only matters if it shows up as a ceiling on what it can predict.", 9.0),
        ("P3 supply the sobering benchmark. In one hundred thirty-two first-stroke patients, the explained variance was low.", 9.0),
        ("Across cognitive domains, R-squared ranged from just zero-point-zero-one to zero-point-one-eight.", 8.0),
        ("And the tell: refining the anatomy, restricting to cleaner voxels, did not improve prediction at all.", 8.5),
        ("If cleaning the anatomy does not help, the ceiling is not noise you can scrub. It is intrinsic to the model class.", 9.5),
        ("Those numbers, and what they bound, are the next chapter. Here we have only fixed the ceiling's foundation.", 9.0),
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
