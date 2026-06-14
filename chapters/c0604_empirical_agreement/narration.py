"""Narration for c0604_empirical_agreement — "Empirical agreement: strip the backbone".

Source: responses/lnm_critique/sections/04_removing_the_backbone.md
        responses/lnm_critique/papers/P1_critique.md
        responses/lnm_critique/papers/P3_biolimits.md

The thesis of this chapter is the rare empirical agreement between the critique and
the rebuttal-adjacent work: BOTH sides agree that a low-rank "backbone" dominates
every LNM map, and BOTH prescriptions converge on removing it. The critique (P1)
measures that backbone at ninety-three percent of map variance; the biological-limits
Comment (P3) measures it at five-to-seven principal components capturing over ninety
percent. Residualization deletes exactly that agreed-upon nuisance. The remaining
disagreement is only whether anything SURVIVES the stripping — and that is an
empirical question settled by the contrast under the symptom-label null, where
same-symptom maps correlate at zero-point-four-four versus zero-point-one-six to
degree, with zero false positives in a thousand iterations at threshold above ten.

Numbers (all page-cited in the sources above):
  - P1: 93% (s.d. 5.0%) of LNM-map variance, basic connectome properties (P1 p.1243).
  - P1: 79% (s.d. 10.2%) of sLNM-map variance.  PC1 overlaps degree at r = 0.82.
  - P3: 5-7 principal components account for >90% of LNM-map variance (P3 p.1).
  - Rebuttal: same-symptom r = 0.44 vs different-symptom 0.09 vs degree 0.16;
              0 false positives / 1000 iterations at specificity threshold t > 10.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the text
is the subtitle in manim AND the spoken line. The number of play_beat()/wait_beat()
calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — Two camps, one prescription
    "S1_Converge": [
        ("In a debate this sharp, agreement is rare. So when both camps prescribe the very same remedy, that agreement is worth pausing on.", 9.0),
        ("On one side stands the critique: van den Heuvel and colleagues, who say lesion network mapping is dominated by one fixed object, the connectome's backbone.", 9.5),
        ("On the other side stands the rebuttal-adjacent work, which says the disease-specific signal, if any, lives off that backbone, not in it.", 9.0),
        ("These two sides disagree about almost everything. But on the cure they shake hands. Strip the backbone out before you test anything.", 9.0),
        ("The critic strips it because the backbone is all there is. The defender strips it to reveal whatever sits on top. Same scalpel, opposite hope.", 9.5),
        ("So this chapter is about that rare overlap. We will show the agreement is not rhetorical: both sides put a number on the backbone, and the numbers nearly match.", 9.5),
    ],
    # S2 — P1: 93 percent is connectome
    "S2_P1": [
        ("Start with the critique's own measurement. How big is the backbone? Van den Heuvel and colleagues answer with a regression.", 8.5),
        ("They predict each lesion network map from basic connectome properties alone: sub-cortical and cortical degree, four modular-degree terms, and three functional gradients.", 9.5),
        ("No disease label enters that regression. Only generic geometry of the connectome. And it explains ninety-three percent of the variance in the maps.", 9.5),
        ("Ninety-three percent, with a standard deviation of five percent. That is on page one-two-four-three of the critique. For the symptom-weighted variant it is seventy-nine percent.", 9.5),
        ("Read that as a fraction of energy. Ninety-three percent of what an L N M map is, is just connectome backbone, shared across every disorder.", 9.0),
        ("And here is the hinge. That ninety-three percent is exactly what residualization removes. Project out the leading connectome modes and you delete that shared bulk by construction.", 10.0),
        ("So the critique's headline number is not an objection to stripping. It is the size of the thing both sides agree should be stripped.", 9.0),
    ],
    # S3 — P3: 5 to 7 PCs over 90 percent
    "S3_P3": [
        ("Now a second, independent measurement, from a completely different paper. Pini, Salvalaggio, and Corbetta, the biological-limits Comment, call this P-three.", 9.0),
        ("They invoke a principal-component analysis. Write each map, m sub ell, as a weighted sum of fixed components: u sub k are the principal components, the eigenvectors of C, and c sub k says how much of each. The question is how many of them, capital K, you need to rebuild the maps.", 11.0),
        ("Their answer, on page one: just five to seven principal components account for more than ninety percent of the variance in L N M maps.", 9.5),
        ("Five to seven directions out of a hundred thousand voxels. The maps are almost flat, almost low-dimensional. That low-dimensional shell is the backbone.", 9.5),
        ("Notice the convergence of the two numbers. The critique says ninety-three percent is generic connectome properties; P-three says ninety percent lives in a handful of components.", 10.0),
        ("Two papers, two methods, one verdict: a low-rank backbone dominates. Strip those leading components, and whatever survives is where specificity could possibly live.", 9.5),
        ("And critically, P-three's own conclusion is that nothing it cares about survives. That is exactly the empirical claim we are about to test, not assume.", 9.5),
    ],
    # S4 — The synthesis
    "S4_Synthesis": [
        ("So both sides agree the backbone exists and dominates, and both prescribe removing it. Where, then, is the actual disagreement?", 8.5),
        ("It is not about whether to strip. It is about what is left after you strip. Does any disease-specific signal survive into the residual?", 9.0),
        ("The critique says no: every permutation of lesions lands back on degree, so the residual is empty. P-three says no for a deeper, biological reason.", 9.5),
        ("The rebuttal says yes: real lesions for a given symptom overlap and are non-random, so they sample a structured subset of rows, not a uniform sweep.", 9.5),
        ("That is a question of fact, not of philosophy. And a question of fact needs a test. The test is the contrast under the symptom-label null.", 9.0),
        ("Permute the symptom labels, recompute the contrast on the residual, and see if the real labeling stands out from its own shuffled copies.", 9.0),
        ("Under that null the answer is measured, not asserted. Same-symptom maps correlate at zero-point-four-four, versus only zero-point-one-six to the degree backbone.", 9.5),
        ("And at specificity threshold t above ten, zero false positives in a thousand iterations. So something does survive the stripping. The disagreement is settled by data.", 9.5),
    ],
    # S5 — Takeaway
    "S5_Takeaway": [
        ("Here is the takeaway to carry out of this chapter. Residualization is not a trick to manufacture signal out of noise.", 8.0),
        ("It removes a known nuisance that both sides of the debate agree dominates the map: ninety-three percent by the critique, over ninety percent in five-to-seven components by P-three.", 10.0),
        ("Removing a shared, label-independent component cannot invent a between-group difference, because the two groups share that component by construction.", 9.0),
        ("What it can do is stop that shared chord from drowning out a faint, genuine hum. The signal-to-noise rises because we delete noise, not signal.", 9.0),
        ("So whether off-backbone signal actually exists becomes a clean, separate, empirical question. Not a matter of opinion, but a matter for the symptom null.", 9.0),
        ("And when that null is run honestly, the residual is not always empty. Same-symptom specificity survives at zero-point-four-four, with zero false positives in a thousand iterations above threshold ten.", 10.0),
        ("Strip the agreed-upon backbone. Then let the symptom null decide what is left. That is the whole synthesis, and both camps already hold the scalpel.", 9.5),
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
