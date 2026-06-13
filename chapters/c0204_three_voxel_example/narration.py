"""Narration for c0204_three_voxel_example — "Three lesions, one direction".

The worked example behind the backbone-convergence claim. We take the source's
three-voxel connectome, read off its spectrum, and watch three completely
different single-voxel lesions funnel into nearly the same direction — because
the spectral gap is wide. Geometry, not biology.

Each scene maps to an ordered list of (text, seconds) beats. The text is shown as
a subtitle in manim AND spoken by the TTS pass; `seconds` is the on-screen target
duration. The count of beats here MUST equal the number of play_beat()/wait_beat()
calls in the matching scene class in scenes.py (the beat-count contract).

Source material (quoted / paraphrased):
  responses/lnm_critique/sections/02_what_is_entailed.md
    - C = sum_j lambda_j u_j u_j^T ; m_i = C ell_i = sum_j lambda_j (u_j^T ell_i) u_j
    - cos^2 angle(m, u_1) = lambda_1^2 c_1^2 / sum_j lambda_j^2 c_j^2
    - "As lambda_2/lambda_1 -> 0, this tends to 1: the average map aligns with u_1
       regardless of which voxels the lesions marked."
  Numbers (three-voxel C, eigenvalues 4.0/0.3/0.1, ratio 0.075, u_1 ~ (0.80,0.50,0.33),
  single-voxel angles ~2.9, 5.5, 7.6 degrees) per the chapter spec; every number is
  checkable against C by hand.
"""

SCENES = {
    # S1 — The three-voxel connectome and its spectrum.
    "S1_Spectrum": [
        ("We have argued that an average lesion map drifts toward one fixed direction, the backbone. Now let us watch it happen, with numbers small enough to check by hand.", 10.0),
        ("Here is the source's three-voxel connectome C. A symmetric, three by three matrix: one row and one column for each of three voxels.", 9.0),
        ("Voxel one is the hub. Read the diagonal: two point six three five for voxel one, far larger than one point two two five and zero point five four zero. It connects to everything.", 10.0),
        ("Every symmetric matrix can be rewritten through its eigenvalues and eigenvectors: C equals the sum over j of lambda-j times u-j, u-j transpose. Each lambda is a strength; each u-j is a direction.", 10.5),
        ("This C has eigenvalues four point zero, zero point three, and zero point one. One direction dominates: the first eigenvalue is more than ten times the second.", 9.5),
        ("That ratio, lambda-two over lambda-one, is the spectral gap. Here it is zero point zero seven five. A wide gap. The top eigenvector u-one is roughly zero point eight zero, zero point five zero, zero point three three: the backbone direction.", 11.0),
    ],

    # S2 — One single-voxel lesion -> a column of C -> its angle to u_1.
    "S2_OneLesion": [
        ("Take the simplest possible lesion: destroy a single voxel. The lesion vector ell is one in that slot and zero elsewhere.", 8.5),
        ("Run it through the operator. m equals C times ell, and a single-voxel lesion just selects a column of C. Lesion voxel one and the map is the first column: two point six three five, one point four eight eight, one point zero five four.", 11.0),
        ("Now compare that map's direction to the backbone u-one. The tool is the angle theta, through the cosine: u-one dotted with m, divided by the two lengths.", 10.0),
        ("Geometrically, theta asks how far the map points away from the backbone. Zero degrees means perfectly aligned; ninety degrees means orthogonal, fully off the backbone.", 9.5),
        ("For this first column the angle is tiny: about two point nine degrees. The map from a single-voxel lesion already sits almost exactly on the backbone.", 9.5),
    ],

    # S3 — All three single-voxel lesions; three angles.
    "S3_AllThree": [
        ("Now do it for all three voxels. Each single-voxel lesion picks out a different column of C, so we get three different maps.", 9.0),
        ("Lesion voxel one gives the column two point six three five, one point four eight eight, one point zero five four. Its angle to the backbone is about two point nine degrees.", 9.5),
        ("Lesion voxel two gives a different column entirely, one point four eight eight, one point two two five, zero point five nine seven. Different numbers, different place. Its angle is about five point five degrees.", 10.5),
        ("Lesion voxel three gives a third column, one point zero five four, zero point five nine seven, zero point five four zero. Smaller still. Its angle is about seven point six degrees.", 10.0),
        ("Three lesions, in three different voxels, with three visibly different maps. Yet every one of them lands within about eight degrees of the same backbone direction.", 10.0),
    ],

    # S4 — Three arrows funnelling toward u_1.
    "S4_Funnel": [
        ("Picture the three maps as arrows. Each starts pointing its own way, set by its own column of C.", 8.0),
        ("But watch where they end up. All three swing into a narrow cone, hugging the backbone u-one.", 8.5),
        ("Two point nine, five point five, and seven point six degrees: the whole fan is squeezed into under eight degrees of arc.", 9.0),
        ("Why so tight? Go back to the cosine-squared bound. The angle to u-one shrinks toward zero exactly as the gap lambda-two over lambda-one shrinks toward zero.", 10.0),
        ("Our gap is zero point zero seven five, already small, so every map is pulled hard onto the backbone before its own identity gets a say.", 9.5),
    ],

    # S5 — The moral: geometry, not biology.
    "S5_Moral": [
        ("Here is the point, stated carefully. Completely different lesions produce nearly the same direction. Not because they share biology, but because C has one wide spectral gap.", 10.5),
        ("It is geometry, not biology. The eigenvalues own the direction; the lesion enters only through its loadings, and the loadings barely move the answer when one eigenvalue dominates.", 10.5),
        ("So this explains exactly one thing: why average maps, across very different conditions, look so alike. That convergence is a property of the connectome's spectrum.", 10.0),
        ("It does not say the method is broken. It says nothing yet about whether a symptom contrast carries signal, because the backbone that crowds every map can cancel from a difference of maps.", 10.5),
        ("We have shown why the camera always photographs the same hubs. Whether the court can still convict, on the contrast, is the question the next chapters take up.", 10.0),
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
