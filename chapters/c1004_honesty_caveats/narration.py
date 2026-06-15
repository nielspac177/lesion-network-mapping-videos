"""Narration for c1004_honesty_caveats — "Honesty caveats".

Source: responses/lnm_critique/sections/09_references_caveats.md
        responses/lnm_critique/papers/_papers_verified.md

The closing honesty chapter of the LNM series. It draws a clean line between
three epistemic categories that the source file makes load-bearing:
  - the MATH WE PROVE (R1 alignment, backbone cancellation, permutation
    exactness, R5 SNR) plus the page-cited critique numbers  -> verified;
  - the empirical figures we could only read at abstract level, and the
    author's unpublished FUS-VIM numbers  -> marked [verify against primary
    source] / flagged unpublished;
  - one genuinely open methods question (Freedman-Lane vs raw label-shuffle).

The closing stance: take the critique seriously, give the rebuttal full
standing, label the uncertainty. The goal is understanding the math, not
winning the argument.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — why a caveats chapter exists at all
    "S1_Why": [
        ("A position paper that accuses a field of over-reading its evidence has no business over-reading its own.", 8.5),
        ("So before we close, we show our hands. We flag, plainly, what is verified and what is not.", 8.0),
        ("There are two kinds of claim in this series, answering to two different standards.", 7.5),
        ("Some of what we said is us doing math: theorems we can prove on the page, and so we own them fully.", 8.5),
        ("Some of what we said is us reporting what other people found. There we can only be as sure as our sources.", 8.5),
        ("This chapter keeps those two kinds visibly apart, so you never mistake a proof for a report.", 8.0),
    ],
    # S2 — what is verified
    "S2_Verified": [
        ("First, the verified column. The mathematical spine of the series stands on its own.", 8.0),
        ("The alignment result: a lesion map is C times little-ell, and it leans on the leading eigenvector u-sub-one.", 9.0),
        ("The backbone cancellation: the label-independent backbone subtracts out of a symptom contrast.", 8.5),
        ("Permutation exactness: shuffling the symptom labels gives an exactly valid null under exchangeability.", 8.5),
        ("And the signal-to-noise result of residualization: remove the low-rank backbone, the contrast survives.", 8.5),
        ("You do not have to trust us on any of these. You have to check the algebra, and it closes on the page.", 8.5),
        ("Also verified: the page-cited critique numbers, read from the full texts of the four core papers.", 8.5),
        ("Same-symptom correlation zero-point-four-four, degree only zero-point-one-six, zero false positives in a thousand at t above ten. Solid.", 9.5),
    ],
    # S3 — what is marked pending
    "S3_Pending": [
        ("Now the pending column. Not everything here is settled, and we tag the gaps in plain sight.", 8.0),
        ("Two response-side preprints we hold only at abstract level. Their internal numbers carry a flag.", 8.5),
        ("The dimensionality-reduction accuracies: zero-point-five-one for schizophrenia, up to zero-point-six-one for epilepsy.", 9.0),
        ("And Petersen and colleagues' cross-domain similarities, across two thousand nine hundred and fifty stroke patients.", 9.0),
        ("On screen, each of those wears the same tag: verify against primary source.", 7.5),
        ("Separate again: the author's own unpublished FUS-VIM numbers, from essential tremor and Parkinson's.", 8.5),
        ("Sensitivity backbone near zero-point-nine-nine, specificity near minus zero-point-two-one. In progress, not peer reviewed.", 9.0),
        ("They are a worked example from the author's desk, an illustration of the mechanism, never a datum that settles anything.", 9.0),
    ],
    # S4 — an open methods question
    "S4_OpenQuestion": [
        ("There is also one honest open question, and we will not pretend it is decided.", 7.5),
        ("Our symptom-label null can be built two ways. The choice is not fully settled for this exact statistic.", 8.5),
        ("Scheme one is the raw label shuffle, Manly style: swap each patient's symptom with another patient's map.", 9.0),
        ("This is what the rebuttal actually uses: shuffle each patient's symptom with a different patient's network map.", 8.5),
        ("Scheme two is Freedman and Lane: residualize on the nuisance covariates, permute, then refit.", 8.5),
        ("Both cancel the backbone, because the backbone is label-independent. But only Freedman-Lane stays exact when covariates are present.", 9.5),
        ("Which is right for this precise statistic is genuinely open. We argue our case holds under either, and we leave the seam visible.", 9.5),
    ],
    # S5 — the honest stance
    "S5_Stance": [
        ("So here is the stance we close on, and it is the spine of our honesty.", 7.5),
        ("Take the critique seriously. Its strongest form is page-cited, and we concede the true part verbatim.", 8.5),
        ("The averaging argument is real: under uniform, non-overlapping sampling, the average converges to the degree of C.", 9.0),
        ("Give the rebuttal full standing too. Real symptom lesions overlap and are non-random; the contrast carries the signal.", 9.0),
        ("And label the uncertainty. Proven math in one column, pending figures in another, the open question named.", 8.5),
        ("The goal was never to win the argument. The goal is to understand the math, cleanly enough that you can audit it yourself.", 9.0),
        ("That is where we leave it: the premises true, the narrow conclusion true, and every hedge shown in the open.", 9.0),
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
