"""Narration for c0205_convergence_geometry — "Why convergence is not validation".

Each scene maps to an ordered list of (text, seconds) beats. The text is shown as
a subtitle in manim AND spoken by the TTS pass; `seconds` is the on-screen target
duration. The count of beats here MUST equal the number of play_beat()/wait_beat()
calls in the matching scene class in scenes.py (the beat-count contract).

Source material (quoted / paraphrased, page-cited where the .md does):
  responses/lnm_critique/sections/02_what_is_entailed.md
    - the cos^2 alignment bound for the one-sample average,
    - the symptomatic/asymptomatic split and the contrast Delta,
    - the cancellation box ("the backbone cancels from the contrast"),
    - the worked check (lambda_1=10, lambda_2=1; loadings (2.0, +/-0.5)),
    - the camera-vs-court framing and the WARNING about residual leakage,
    - the bridge to R3-R5 (which null you test).

Balanced framing: convergence toward u_1 is a property of C's spectrum. It
explains why AVERAGE maps look alike, and says nothing yet about whether a
CONTRAST carries signal. This is geometry, not a verdict on the method.
"""

SCENES = {
    # S1 — Restate: every seed's map points near the backbone u_1.
    "S1_Restate": [
        ("We earned one fact in the last chapter, and we restate it cleanly here. Write the connectome in its own natural axes: C is the sum over j of lambda-j, times u-j, u-j transpose.", 10.5),
        ("The u-j are the eigenvectors, the brain-wide patterns C is built from. The lambda-j are the eigenvalues, ordered largest first: lambda-one is at least lambda-two, and so on down.", 10.0),
        ("Push any seed lesion ell through C and it lands as a weighted sum of those patterns. Map equals the sum over j of lambda-j, times the loading u-j transpose ell, times u-j.", 10.0),
        ("That inner product, u-j transpose ell, is just the loading: how much of pattern j the lesion happens to mark. It is the only place the lesion gets a vote.", 9.0),
        ("Now look at the squared cosine of the angle between the map and the backbone u-one. It is lambda-one squared, times that loading squared, divided by the same sum over every component.", 10.0),
        ("And here is the lever: the spectral gap, lambda-two over lambda-one. As that ratio goes to zero, lambda-one swamps the rest, and the cosine squared goes to one.", 9.5),
        ("So every single seed's map points very nearly along u-one. Not because the lesions agree, but because lambda-one was always going to win the tug-of-war.", 9.0),
    ],

    # S2 — The funnel: a cone around u_1 that almost all maps fall into.
    "S2_Funnel": [
        ("Let us draw what that bound means geometrically. Put the backbone u-one as a single fixed direction in the high-dimensional map space.", 8.0),
        ("Around it, the spectral gap carves out a narrow cone. The smaller lambda-two over lambda-one is, the tighter the cone closes around u-one.", 9.0),
        ("Now fire seeds at it. Lesions from anywhere in the brain, marking completely different voxels, sending their maps off in what should be different directions.", 9.0),
        ("But each map is pulled in. The lambda-one term is so heavy that almost every seed map, whatever voxels it marked, falls inside the same cone.", 9.5),
        ("This is the funnel. Different lesions enter from different mouths, and they all drain toward one outlet: the backbone u-one.", 8.5),
        ("Crucially, the funnel was shaped before any patient arrived. Its walls are the eigenvalues of C, which know nothing about lesions, symptoms, or disease.", 9.5),
        ("So convergence here is real, and it is exactly what the critique observed. The question is what a shared endpoint can, and cannot, certify.", 9.0),
    ],

    # S3 — A shared endpoint certifies the funnel, not the lesion or the disease.
    "S3_Certifies": [
        ("Suppose two cohorts, two diseases, even a bag of random lesions, all average out to nearly the same map near u-one. What has that actually proven?", 9.5),
        ("It proves the funnel exists. A shared endpoint certifies the geometry of C, its dominant backbone u-one, and nothing more.", 9.0),
        ("It does not certify the lesion. The voxels each cohort marked were thrown away the moment lambda-one dragged every map into the cone.", 9.0),
        ("And it does not certify the disease. Addiction, depression, and random seeds converge for the same reason: they share u-one, and u-one is doing all the talking.", 10.0),
        ("This is the source's concession, made loudly and in full. The one-sample average map is nonspecific. It is backbone-dominated, it converges across disorders, and random seeds reproduce it. Denying this is denying arithmetic.", 11.0),
        ("But notice the careful shape of the claim. Convergence is a true statement about the average map, and only about the average map.", 8.5),
        ("It is a property of C's spectrum, not a verdict on the method. To turn it into a verdict, you would need it to say something about a different object entirely.", 9.5),
    ],

    # S4 — The gap: the critique's leverage on AVERAGE maps; why a CONTRAST recovers signal. Both sides.
    "S4_ContrastVsAverage": [
        ("Here is exactly where the critique gets its leverage, and exactly where it runs out. Split the cohort: symptomatic seeds, and asymptomatic seeds.", 9.0),
        ("Average each group on its own. Both averages get dragged toward u-one, because both load on the backbone. Both are nonspecific. The critique is completely right about each one.", 10.0),
        ("But the object that carries the symptom is not either average. It is the contrast: Delta equals the symptomatic average minus the asymptomatic average.", 9.0),
        ("Subtract, component by component. The leading term is lambda-one, times the difference in backbone loadings, c-one-plus minus c-one-minus, along u-one.", 9.5),
        ("And generically those two groups load on the backbone the same way. Symptom status alone gives no reason to sit on the hubs differently. So that difference is near zero, and the u-one term cancels.", 11.0),
        ("What survives the cancellation are the higher patterns, u-two, u-three, and on, weighted by genuine group differences. The backbone that poisoned the average is cleansed from the contrast by construction.", 10.5),
        ("Take the source's worked check. Lambda-one is ten, lambda-two is one. Both groups load two on the backbone; they load plus and minus one half on the second pattern.", 9.5),
        ("Each average is about ninety-nine point nine percent backbone, nonspecific, just as charged. But the contrast is pure u-two: the backbone has vanished, and the symptom direction stands clean.", 10.0),
        ("Be fair in both directions, though. This cancellation is exact only in expectation. If the two groups really do load on hubs differently, from selection or lesion-size, a residual u-one term leaks through and can masquerade as signal.", 11.0),
        ("That residual is precisely what the right null and explicit backbone removal are built to kill. The point here is narrower: the contrast is where signal can survive, and the critique never tested it.", 10.0),
    ],

    # S5 — Bridge to specificity: which null you test. Sets up Parts 4 and 5.
    "S5_Bridge": [
        ("So convergence toward u-one is not validation, and it is not refutation either. It is geometry, and the geometry has handed us a sharper question.", 9.5),
        ("The question is no longer is the average map specific. We have conceded it is not. The question is which null do you test the contrast against.", 9.5),
        ("Test it against the wrong null and the leaked backbone can fake a result. Test it against the right null, shuffle the symptom labels while holding lesion geometry fixed, and u-one cancels by construction.", 11.0),
        ("Under a label-shuffling null, the backbone is label-independent. It appears identically in the observed statistic and in every permuted one, so it simply cannot inflate a p-value. That is an exact guarantee.", 10.5),
        ("That is the next move. Part four builds that null and asks which of the candidate nulls actually targets the symptom hypothesis.", 8.5),
        ("Part five removes the residual backbone leakage explicitly, so what is left in the contrast is symptom signal and not the cone. Convergence set the question; specificity will answer it.", 10.0),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:22s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':22s} target={grand:5.1f}s ({grand/60:.1f} min)")
