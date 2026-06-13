"""Narration for c0202_backbone_term — "The map in the spectral basis".

Mini-video (Vol 2, ch 2) of the LNM series. We rewrite the seed map m = C ell in
the eigenbasis of the connectome, isolate the backbone term lambda_1 (u_1^T ell) u_1,
read the spectral gap lambda_2/lambda_1, separate the off-backbone remainder, run a
numeric check with the source's eigenvalues lambda = (4.0, 0.3, 0.1), and close with
the careful caveat: this is about the MAP'S DIRECTION, not yet about disease signal.

Each scene maps to an ordered list of (text, seconds) beats. The count here MUST
equal the number of play_beat()/wait_beat() calls in the matching scene class in
scenes.py (the beat-count contract enforced by lnm_engine and tests/test_sync.py).

Source material (quoted / paraphrased):
  responses/lnm_critique/sections/02_what_is_entailed.md
    - m_i = C ell_i = sum_j lambda_j (u_j^T ell_i) u_j        (the spectral expansion)
    - the leading term lambda_1 c-bar_1 u_1, "the direction is fixed before the
      disease gets a vote"
    - cos^2 angle(m-bar, u_1) = lambda_1^2 c_1^2 / sum_j lambda_j^2 c_j^2 -> 1 as
      lambda_2 / lambda_1 -> 0
  eigenvalues lambda = (4.0, 0.3, 0.1) for C are the source's 3-voxel spectrum
  (sections/01_the_charge_formalized.md, used in c0101_map_operator).
"""

SCENES = {
    # S1 — Push a lesion through C in the spectral basis.
    "S1_Spectral": [
        ("We already know the seed map is one product: m equals C times ell. Now we look at it through the right lens, the eigenbasis of the connectome.", 9.0),
        ("Because C is symmetric, it has a spectral decomposition. It is the sum over j of an eigenvalue lambda-j times the outer product of its eigenvector u-j with itself.", 9.5),
        ("The lambda-j are the eigenvalues, the strengths, ordered largest first: lambda-one at least lambda-two and so on down. The u-j are the eigenvectors, the connectome's natural patterns.", 10.0),
        ("Push the lesion through. The map becomes a sum over j of lambda-j, times the scalar u-j transpose ell, times the pattern u-j itself.", 9.0),
        ("Look hard at that middle factor, u-j transpose ell. It is an inner product, a single number. It measures how much the lesion overlaps pattern j: how aligned the wound is with the j-th natural pattern of the brain.", 10.5),
        ("So the map is a recipe. Each pattern u-j is poured in, weighted by its strength lambda-j and by how much the lesion overlaps it. Three patterns, three weighted ingredients.", 10.0),
    ],

    # S2 — Isolate the backbone term.
    "S2_Backbone": [
        ("Pull out just the first term in that sum, the term for j equals one. We will call it the backbone term.", 7.5),
        ("It is lambda-one, times u-one transpose ell, times the leading pattern u-one. One eigenvalue, one overlap, one direction.", 8.5),
        ("Each piece earns its place. Lambda-one is the largest eigenvalue, so this term gets the biggest strength of all.", 8.0),
        ("U-one transpose ell is the lesion's overlap with the top pattern. The source notes there is no reason a wound that sits anywhere broad in the network has zero overlap here, so this number is generically non-zero.", 10.5),
        ("And u-one is the backbone itself: the dominant, hub-shaped pattern of the connectome. The direction this term points.", 8.5),
        ("Hold this term apart from the rest. The question of the whole chapter is simple: when does this single ingredient drown out all the others?", 9.0),
    ],

    # S3 — The spectral gap.
    "S3_Gap": [
        ("The answer is one number: the spectral gap, the ratio lambda-two over lambda-one.", 7.0),
        ("It compares the second-strongest pattern to the first. When it is small, lambda-two is tiny next to lambda-one, and we say the gap is large.", 9.0),
        ("Why does a large gap make one term dominate? Because every term past the first is capped by its eigenvalue, and those eigenvalues have already collapsed.", 9.0),
        ("The source makes this exact, with the squared cosine of the angle between the map and the backbone u-one.", 8.5),
        ("It equals lambda-one squared times c-one squared, divided by the sum over all j of lambda-j squared times c-j squared, where c-j is the overlap u-j transpose ell.", 10.5),
        ("Now send the gap lambda-two over lambda-one to zero. Every competing term in the denominator is held down by lambda-two squared, so it vanishes, and the squared cosine tends to one.", 10.5),
        ("A cosine of one means the angle is zero. The map aligns with the backbone u-one, the source says, regardless of which voxels the lesions marked.", 9.5),
    ],

    # S4 — The off-backbone remainder.
    "S4_Remainder": [
        ("But the map is not only its backbone term. Split it honestly into two pieces.", 7.0),
        ("The backbone term, j equals one, plus the remainder: the sum from j equals two onward of lambda-j times c-j times u-j.", 9.0),
        ("This remainder is everything off the backbone. It lives in the directions u-two, u-three, and below, the connectome's subtler patterns.", 8.5),
        ("Its size is bounded by the lagging eigenvalues. Each off-backbone term carries a lambda-j with j at least two, and those are exactly the small ones.", 9.0),
        ("So a large spectral gap does two things at once. It inflates the backbone term and it starves the remainder. The map tilts hard toward u-one.", 9.5),
        ("But keep the remainder in view. It is small in the average, yet it is precisely where, later, the symptom contrast will turn out to live.", 9.5),
    ],

    # S5 — Numeric with lambda = (4.0, 0.3, 0.1).
    "S5_Numeric": [
        ("Let us put numbers on it, with the source's three-voxel spectrum: lambda equals four point zero, zero point three, zero point one.", 8.5),
        ("Take a lesion whose overlaps with the three patterns are all equal, each one, so we are not stacking the deck with the lesion. The coefficients c-one, c-two, c-three are one, one, one.", 10.0),
        ("Now the backbone coefficient is lambda-one times c-one, which is four point zero. The next is lambda-two times c-two, zero point three. The last is lambda-three times c-three, zero point one.", 10.5),
        ("Four point zero against zero point three against zero point one. The backbone coefficient dwarfs the rest before the lesion has said anything specific.", 9.5),
        ("Feed these into the squared cosine. Sixteen on top, from four squared; on the bottom sixteen plus zero point zero nine plus zero point zero one. That is about ninety-nine point four percent.", 11.0),
        ("So the map sits within about four and a half degrees of the backbone. The gap of zero point three over four did the work, exactly as the bound predicts.", 9.5),
    ],

    # S6 — Takeaway and the careful caveat.
    "S6_Takeaway": [
        ("Step back. We showed the map points almost entirely along the backbone u-one whenever the spectral gap is large.", 8.0),
        ("And this is geometry, the source insists, not a verdict on the method. The direction is owned by the eigenvalues lambda-j, which are a property of C alone.", 9.5),
        ("That is precisely why average maps look alike: an addiction average, a depression average, even random seeds all share u-one, and u-one is doing the talking.", 9.5),
        ("But notice the careful word. We have only pinned down the map's direction. We have said nothing yet about whether a symptom contrast carries signal.", 9.0),
        ("Convergence toward u-one is a fact about the spectrum of C. It explains the look of the average. It does not, on its own, debunk lesion network mapping.", 9.5),
        ("The backbone is geometry, not a verdict. The next chapter takes the contrast, the difference between groups, and asks what survives once this backbone term cancels.", 10.0),
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
