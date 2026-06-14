"""Narration for c0603_theorem_r5_snr — "Theorem R5: residualization improves SNR (proof)".

Source: responses/lnm_critique/sections/04_removing_the_backbone.md

R5 is the load-bearing claim: under the backbone-sharing assumption, removing the
shared backbone subspace from every map weakly raises the per-voxel signal-to-noise
ratio of a between-group contrast, with strict inequality exactly when the backbone
carries within-group variance but no between-group signal.

All equations/numbers are quoted from section 04 (the "[!math] Residualization is
signal-preserving and noise-reducing" block, and the backbone-sharing [!IMPORTANT]).

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the text
is the subtitle in manim AND the spoken line. The number of play_beat()/wait_beat()
calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the R5 statement
    "S1_Statement": [
        ("Here is theorem R five, the load-bearing claim of this whole section. Removing variance can actually raise signal-to-noise.", 9.0),
        ("First we need a clean definition. The signal-to-noise ratio is the between-group signal squared, divided by the within-group noise.", 9.0),
        ("The signal is delta of v: at each voxel v, the difference in the average map between the labelled group and the unlabelled group.", 9.5),
        ("The noise is the variance of the map at that voxel, the spread of values across patients within a group.", 8.5),
        ("R five says: under backbone-sharing, the residualized map m-tilde has signal-to-noise at least as large as the raw map m.", 9.5),
        ("And the inequality is strict, genuinely better, exactly when the backbone carries within-group variance but no between-group signal.", 9.5),
        ("In words: stripping the shared structure can only help, and it strictly helps whenever that structure is pure noise for the contrast.", 9.0),
    ],
    # S2 — the signal model
    "S2_Model": [
        ("To prove it we need a model of where the signal lives. Split every patient's map into two orthogonal pieces.", 8.5),
        ("Each map m equals the backbone part, Pi-B times m, plus the residual part, m-tilde. The shared bulk plus the sliver on top.", 9.5),
        ("Pi-B is the projector onto the backbone subspace, the span of the leading connectome modes u-one through u-r. It is fixed before any patient is seen.", 10.0),
        ("Now write the map as a population mean plus structure. There is mu, the shared backbone that every group has in common.", 9.0),
        ("There is delta-tilde, the discriminative signal, the part that actually differs between groups, and it lives off the backbone, in the residual.", 9.5),
        ("And there is noise, the within-group variability of each map across patients, which has a backbone share and a residual share.", 9.0),
        ("So the question becomes sharp. Does residualizing, keeping only m-tilde, throw away any of delta-tilde? The model says no.", 9.0),
    ],
    # S3 — pre-proof strategy
    "S3_Strategy": [
        ("Before the algebra, the strategy in one breath. We will show the numerator is untouched and the denominator can only shrink.", 9.0),
        ("The engine is the backbone-sharing assumption, and it is not an extra hope. It is just P one's own convergence claim, read at the population level.", 9.5),
        ("P one proved that averaging M times C, the stacked lesion seeds times the connectome, over a heterogeneous set, converges on the degree of C, the backbone every set lands on.", 10.0),
        ("If that is true, the backbone has the same mean in both groups. It carries no between-group difference. It is common to everyone.", 9.0),
        ("Scope it honestly: that convergence holds only for uniform, non-overlapping lesions. Real symptom lesions overlap and are non-random, and there the contrast carries signal. But backbone-sharing needs only the few leading shared modes to have no label difference, so removing them strips pure noise, not signal.", 11.0),
        ("Meanwhile the discriminative signal lives off the backbone, orthogonal to it, so the subtraction never touches it.", 8.5),
        ("Numerator fixed, noise removed: the ratio can only go up. That is the entire shape of the proof, before we write a single line.", 9.0),
    ],
    # S4 — the proof
    "S4_Proof": [
        ("Now the proof, with words between every step. Start with the between-group difference delta of v, and split it along the backbone.", 9.0),
        ("Delta splits into two brackets. The first is the difference in the backbone part between groups; the second is the difference in the residual.", 9.5),
        ("By backbone-sharing, the first bracket is exactly zero: the backbone has the same mean in both groups. So all the signal sits in the second bracket.", 10.0),
        ("Call that surviving signal delta-tilde. We have just shown delta equals delta-tilde. The numerator of the ratio is unchanged by residualizing.", 9.5),
        ("Now the denominator. The variance of the raw map splits into backbone variance, plus residual variance, plus twice their cross-patient covariance.", 9.5),
        ("Residualizing deletes the backbone variance term, the one weighted by the huge eigenvalue lambda-one squared. The dominant chunk of the noise is gone.", 9.5),
        ("This shrinks the denominator whenever the leftover covariance is non-negative, the removed and retained parts not anti-correlated across patients.", 9.5),
        ("Same numerator, smaller denominator. So the signal-to-noise of m-tilde is at least that of m, strict when the backbone held real variance. R five is proved.", 10.0),
    ],
    # S5 — moral and limits
    "S5_Moral": [
        ("The moral is simple enough to keep. Strip the shared structure to see the difference. Cancel the chord, and the hum becomes audible.", 9.0),
        ("Two choirs sing the same loud chord, each with one person humming a different note. To tell the choirs apart, the chord is useless. Remove it.", 9.5),
        ("But honesty demands the scope. The whole result rests on one assumption: that the real signal does not live in the backbone.", 9.0),
        ("If the disease genuinely shifts the backbone, more or fewer hubs, then Pi-B carries signal, and residualizing would delete it. It would hurt.", 9.5),
        ("So residualization is a hypothesis about where the signal lives, and the good news is that it is testable.", 8.5),
        ("Compare the backbone projections across groups before discarding them. If they differ, do not residualize that mode. The assumption is checkable, not assumed away.", 9.5),
        ("One last limit we do not solve: a static connectome cannot recover higher-order or dynamic effects it never encoded. R five is honest about its own scope.", 9.5),
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
