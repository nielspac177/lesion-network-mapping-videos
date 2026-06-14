"""Narration for c0602_residualization — "Removing the backbone: degree / PC1 residualization".

Source: responses/lnm_critique/sections/04_removing_the_backbone.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — define the residualized map
    "S1_Define": [
        ("Recall every lesion map. Take a seed ell, multiply by the normative connectome C, and you get m sub ell equals C ell.", 9.0),
        ("R one proved that map is mostly one shared pattern, the backbone, the connectome's hub and degree structure.", 8.5),
        ("So here is the cure. Pick a rank r, the leading modes you judge to be backbone, and define the orthogonal projector pi-perp onto everything else.", 10.0),
        ("The residualized map, m-tilde sub ell, is pi-B-perp applied to m sub ell. We subtract the backbone part and keep the rest.", 9.0),
        ("Because the u sub j are eigenvectors of C, this has a clean closed form: a sum over j greater than r of lambda-j times u-j-transpose-ell, times u-j.", 10.0),
        ("Lambda-j is the j-th eigenvalue. U-j is the j-th connectome mode. And u-j-transpose-ell is how strongly the seed loads on that mode.", 9.5),
        ("So residualizing against the leading r modes is identical to discarding the first r terms of the spectral expansion. The shared term is gone, exactly, by construction.", 10.5),
    ],
    # S2 — zeroing the leading coefficients
    "S2_Zeroing": [
        ("Let us look at the spectrum, term by term. The raw map m sub ell is a sum over all j of lambda-j times u-j-transpose-ell, times u-j.", 9.5),
        ("Each term is one connectome mode u-j, scaled by two numbers: its eigenvalue lambda-j, and the coefficient u-j-transpose-ell.", 9.0),
        ("That coefficient, u-j-transpose-ell, is just the projection of the seed onto mode j. It measures how much of mode j the lesion switches on.", 9.5),
        ("Residualization sets every term with j less than or equal to r to zero. We literally cross out the leading coefficients.", 9.0),
        ("The first mode u-one is the all-positive degree mode. Any non-empty seed loads on it, so the first term is huge and shared by everyone.", 9.5),
        ("Drop that top term, and the loud common chord disappears. What remains is the tail, where one seed differs from another.", 9.0),
        ("That tail, the sum from j equals r plus one onward, is the only place a disorder-specific signal could ever live.", 9.0),
    ],
    # S3 — the backbone fraction
    "S3_Fraction": [
        ("How much of a raw map actually lives in the backbone? Define the backbone fraction, rho-B of ell.", 8.0),
        ("It is the squared norm of pi-B m sub ell, the backbone part, divided by the squared norm of the whole map m sub ell.", 9.0),
        ("Written in the spectrum, the numerator sums lambda-j-squared times u-j-transpose-ell-squared over the leading modes, j up to r.", 9.5),
        ("The denominator sums the same quantity over all modes. So rho-B is simply the share of map energy sitting in the backbone.", 9.0),
        ("R one's whole content is that rho-B is close to one for almost every seed, because lambda-one dwarfs the rest and every seed loads on u-one.", 10.0),
        ("And here is the symmetry. The energy the residual keeps is exactly one minus rho-B. What R one calls nonspecific is exactly what we delete.", 9.5),
        ("High rho-B means the raw map is almost all hub. That is not a worry for us. It is precisely the regime where projecting the backbone out costs little and clarifies much.", 10.5),
    ],
    # S4 — geometric picture
    "S4_Picture": [
        ("Now picture it geometrically. Take the R one toy: three voxels, one dominant mode u-one, the all-positive degree direction.", 9.0),
        ("Two different seeds, ell-A and ell-B. Both load on u-one, so both maps point almost straight along the backbone axis.", 9.0),
        ("Their raw correlation is near one. Two different seeds, looking nearly identical. That is R one's convergence, but only for the group average under uniform, non-overlapping sampling. Real symptom lesions overlap and are non-random.", 11.0),
        ("Residualization projects each map onto the plane orthogonal to u-one. It knocks out the shared backbone component entirely.", 9.0),
        ("What is left is the off-backbone tilt. Because ell-A and ell-B load differently on the lower modes, their residuals are no longer parallel.", 9.5),
        ("The correlation that was near one drops to whatever the seeds genuinely share off the backbone, the only correlation that could encode a disorder. Empirically that contrast holds: same-symptom maps correlate at zero point four four versus zero point one six to the degree map.", 11.5),
        ("Same arithmetic, scaled to a hundred thousand voxels and the real connectome elbow at a handful of modes, is the actual procedure.", 9.5),
    ],
    # S5 — does it actually help? (bridge to c0603)
    "S5_Bridge": [
        ("So the geometry is clean. But does removing variance actually help? That is the load-bearing claim, and it needs care.", 9.0),
        ("The claim to prove next, R five: residualization raises the signal-to-noise ratio of the group contrast. It is signal-preserving and noise-reducing.", 9.5),
        ("Signal-preserving, because under one assumption the backbone carries no between-group mean difference, so all the signal sits in the residual.", 9.5),
        ("That assumption is backbone-sharing: the backbone's distribution is the same in the labelled and unlabelled groups. It needs only the few leading shared modes to carry no label difference, which uniform coverage of those modes makes plausible even when the off-backbone tail does not.", 11.5),
        ("Noise-reducing, because the within-group variance of the raw map is dominated by the big lambda-one backbone term. Kill it, and the t-statistic's denominator shrinks.", 10.0),
        ("But heed the caveat. Residualization only helps if the signal is off-backbone. If the disease shifts the backbone itself, projecting it out would delete the signal.", 10.0),
        ("So next we prove the signal-to-noise inequality precisely, and state the exact condition under which the backbone is free to remove.", 9.5),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:28s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':28s} target={grand:5.1f}s ({grand/60:.1f} min)")
