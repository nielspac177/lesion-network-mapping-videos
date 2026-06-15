"""Narration for c0903_different_critique — "A different critique than P1".

This chapter contrasts two attacks on lesion network mapping:
  P1 (van den Heuvel et al.)  — the INFERENCE charge: the group-average prior is
       nonspecific, converging to the connectome's degree.
  P3 (Pini, Salvalaggio & Corbetta) — the MODEL-CLASS charge: a single static,
       first-order connectome C is biologically impoverished. It carries two
       sub-charges:
         (a) C is a misspecified static estimate  — answerable with statistics.
         (b) a static, first-order C is missing whole dimensions (higher-order
             reorganization, hyper-/hypoconnectivity dynamics) — NOT answerable
             by any statistic.

Source:
  responses/lnm_critique/papers/P3_biolimits.md
  responses/lnm_critique/sections/07_biological_limits.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

Numbers are written as words for text-to-speech.
"""

SCENES = {
    # S1 — two different attacks
    "S1_TwoCritiques": [
        ("We have spent this course answering one critique. Now meet a second one that aims somewhere completely different.", 8.5),
        ("The first attack, P one, van den Heuvel and colleagues, is about the prior. The group-average map is nonspecific; it collapses to the connectome's degree.", 10.0),
        ("That is a charge against the inference: what you read off the map describes the backbone, not the disease.", 8.5),
        ("The second attack, P three, Pini, Salvalaggio and Corbetta, does not touch the inference at all.", 8.0),
        ("Their charge is that the whole model class is biologically impoverished. The map m is the lesion seed ell pushed through a single static, first-order connectome C.", 9.5),
        ("Static means frozen at one moment. First-order means only the direct wiring cut, the regions the lesion is directly connected to.", 9.0),
        ("So the two critiques hit different targets. P one says the answer is generic. P three says the question itself is too small.", 9.0),
    ],
    # S2 — orthogonal axes
    "S2_Orthogonal": [
        ("Let us draw the two critiques as axes, because they really are orthogonal. One is about inference; the other is about the model class.", 9.5),
        ("On the horizontal axis, P one: description versus contrast. Do you report the average map, or a symptom contrast against a label null?", 9.5),
        ("Move right along that axis and P one is answered. The backbone cancels in the contrast, and genuine symptom signal survives.", 9.0),
        ("On the vertical axis, P three: the model class. Is C a single static, first-order matrix, or something richer and dynamic?", 9.5),
        ("And here is the key point. Moving right on the inference axis does nothing to move up the model-class axis.", 8.5),
        ("A perfectly clean contrast is still computed through the same static C. You can fix P one and leave P three exactly where it was.", 9.5),
        ("One axis can be fixed by the symptom null. The other cannot. No statistic moves you up the model-class axis. They are orthogonal.", 9.5),
    ],
    # S3 — how they compose with R1 through R5
    "S3_Compose": [
        ("Now let us compose these critiques with our results. R one through R five were built to answer P one, and they do.", 9.0),
        ("R one showed the average map is the backbone. R four showed a symptom-label permutation is exact and cancels that backbone.", 9.5),
        ("R five residualizes onto the leading components, sharpening whatever real contrast remains. Together they defeat P one.", 9.0),
        ("But sit with the quiet phrase under every one of those results: given C. The connectome was always an input we never questioned.", 9.5),
        ("P three questions exactly that input. Even a perfectly clean, backbone-cancelled contrast still lives inside a static, first-order C.", 9.5),
        ("So R one through R five do not answer P three. They make the inference honest given C; they cannot enlarge what C can represent.", 9.5),
        ("You cannot residualize, reweight, or permute your way to a dimension your model does not contain. That is the composition, stated plainly.", 9.5),
    ],
    # S4 — the combined picture
    "S4_Together": [
        ("So what does the honest, combined response look like? It is both moves at once, not one or the other.", 8.5),
        ("Move one, against P one: use the symptom-label null and residualize the backbone. This beats the nonspecificity charge cleanly.", 9.5),
        ("Move two, against P three: report the model-class ceiling honestly. State that a static, first-order C is blind to two whole axes.", 9.5),
        ("P three actually carries two sub-charges. Charge a: C is a misspecified static estimate. That one is a statistics problem.", 9.0),
        ("You answer charge a with sensitivity analysis: run the contrast through at least two defensible connectomes and report its stability.", 9.5),
        ("Charge b is harder. A static, first-order C is missing whole dimensions: higher-order reorganization and hyper- versus hypoconnectivity dynamics.", 9.5),
        ("Charge b you concede. No operation on a static C recovers an axis it lacks. The remedy is a different model class, not a better null.", 9.5),
        ("So the combined picture is: beat P one, partly answer P three, and concede the rest out loud. Both, never either.", 9.0),
    ],
    # S5 — takeaway
    "S5_Takeaway": [
        ("Here is the takeaway, and it is the most uncomfortable line in the whole exchange.", 7.5),
        ("P three is the most durable critique, because no statistic fixes a model class. Our entire toolkit conditions on C.", 9.0),
        ("The chance that the permutation p-value falls below the significance level alpha, given C, stays at most alpha — for any C, even the wrong kind of object. Exactness is a statement about the null given the model.", 10.5),
        ("Getting the right answer to the wrong question is still the wrong answer. The error is not in the inference; it is in the referent.", 9.5),
        ("But notice what does not follow. From C is approximate, you cannot conclude that LNM recovers nothing. That is a quantifier error.", 9.5),
        ("There exists a way C can be wrong does not become for all analyses C destroys the result. Concede the existential; deny the universal.", 9.5),
        ("So the right response to P three is humility about effect size, not abandonment of valid inference.", 8.0),
        ("Beat P one with the symptom null. Bound charge a with sensitivity analysis. Name charge b as the open frontier. That is the honest stance.", 9.5),
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
