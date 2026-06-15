"""Narration for c0704_p1_curve — "P1's own convergence curve".

Source: responses/lnm_critique/sections/05_the_convergence_trap.md
        responses/lnm_critique/papers/P1_critique.md

This chapter walks P1's own published conjunction simulation: as between-lesion
Dice overlap rises, the fraction of lesion sets returning a "significant"
convergence result climbs steeply (Dice 0.08 -> 10%, 0.16 -> 64%, >0.25 -> 97%;
P1 p.1243). The moral is the shared-backbone inflation bound p^K + (1-p)^K -> 1:
agreement is the default under shared structure, so a lit convergence map is
uninformative about a disease-specific network. The honest fix is to test against
a shared-backbone null (or residualize first), tying to Part 6 and the symptom
null — a recipe, not nihilism.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — The Dice experiment: define Dice between lesion masks
    "S1_Experiment": [
        ("The critique did not just argue. It ran a conjunction simulation, and we are going to walk its own published curve.", 9.0),
        ("They generated roughly five hundred thousand simulated lesions across the atlas, and built convergence maps from them.", 9.0),
        ("Then they turned one knob: how much the lesions in a set overlap each other. They measured overlap with the Dice coefficient.", 9.5),
        ("The Dice coefficient between two lesion masks A and B is twice the size of their intersection, over the sum of their sizes.", 9.0),
        ("Twice the shared voxels on top; the total voxels of both masks on the bottom. Zero means no overlap, one means identical masks.", 9.5),
        ("And on the other axis they measured the fraction of voxels reaching significance: how much of the convergence map lights up.", 9.0),
        ("Sensitivity used a threshold of t above seven; specificity, the stricter t above ten. Hold those thresholds; vary only overlap.", 9.5),
    ],
    # S2 — The curve: 0.08->10%, 0.16->64%, 0.25->97%
    "S2_Curve": [
        ("Here is what they found, three points on one curve. The horizontal axis is between-lesion Dice; the vertical is fraction significant.", 9.5),
        ("At a Dice of zero-point-zero-eight, marginal overlap, already about ten percent of lesion sets returned a significant conjunction.", 9.5),
        ("Nudge overlap up to a Dice of zero-point-one-six, and the fraction jumps to roughly sixty-four percent. A steep rise.", 9.0),
        ("And beyond a Dice of about zero-point-two-five, it reaches about ninety-seven percent. Almost every set is now significant.", 9.0),
        ("Plot the three points and the shape is unmistakable: agreement rises steeply, almost a cliff, as overlap grows.", 9.0),
        ("These are not our numbers. They are van den Heuvel and colleagues, page twelve forty-three. The critique's own demonstration.", 9.0),
        ("The lesions barely have to overlap before significant convergence becomes the default outcome, not a discovery.", 8.5),
    ],
    # S3 — What drives significance: overlap -> shared backbone -> agreement
    "S3_Interpret": [
        ("So what is the curve really measuring? Why does a little overlap manufacture so much significance?", 8.0),
        ("Recall the backbone result. Every lesion's map is the same shared component, mu, plus a little cohort-specific noise, epsilon.", 9.0),
        ("More overlap between lesions means they sample the same rows of the connectome, so their maps share even more of that mu.", 9.0),
        ("And where maps share a strong common part, they agree in sign almost everywhere that part is strong. Agreement is an intersection.", 9.5),
        ("Make it a formula. If each map recovers the backbone sign with probability p, all K agree with probability p to the K plus one-minus-p to the K.", 10.0),
        ("As p rises toward one, that whole expression rises to one, for every K. Near-total agreement, driven entirely by the shared mu.", 9.5),
        ("So the convergence is a function of overlap, of shared backbone. It is not a function of disease specificity at all.", 9.0),
    ],
    # S4 — Agreement is the default
    "S4_Default": [
        ("Step back and compare two worlds at the same K, say four maps each landing on the backbone sign nine times in ten.", 9.0),
        ("If the maps were independent coins, agreement would be rare: two to the one-minus-K, just twelve-and-a-half percent at K equals four.", 9.5),
        ("But under a shared backbone, nine-tenths to the fourth plus one-tenth to the fourth is about sixty-five percent. A fivefold jump.", 9.5),
        ("Same operator, same K. The only thing that changed is that the maps now share a backbone, which the backbone result says they always do.", 9.5),
        ("So at realistic overlaps, near-total agreement is exactly what you expect under the null of shared structure alone.", 9.0),
        ("The map being lit is therefore uninformative about a disease network. A big convergence set is the default, not a finding.", 9.0),
        ("Anything you got for free cannot pay for an inference. The convergence map hands you agreement for free, and free is the tell.", 9.0),
    ],
    # S5 — How to test convergence honestly
    "S5_Resolution": [
        ("This is not nihilism. The curve does not say convergence is meaningless; it says convergence needs the right yardstick.", 9.0),
        ("The wrong yardstick is independence, the two-to-the-one-minus-K coins. That comparison makes any agreement look spectacular.", 9.5),
        ("The honest yardstick is the shared-backbone null: ask whether agreement exceeds what p to the K plus one-minus-p to the K already predicts.", 10.0),
        ("Or residualize first. Strip the shared backbone out of each map, then build the convergence on what remains. Tie to Part six.", 9.0),
        ("Then the agreement that survives is the part the backbone could not manufacture. That is the symptom null doing real work.", 9.0),
        ("So the recipe is concrete. Report convergence as a description if at all, against the backbone baseline, never as the headline.", 9.0),
        ("And let the inferential claim ride on the contrast under a symptom-label null. Honest convergence is earned, not free.", 9.0),
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
