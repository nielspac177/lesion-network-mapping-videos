"""Narration for c0203_alignment_bound — "Theorem R1: the alignment bound".

A full, long-form proof chapter. We state the per-seed alignment bound

    tan(theta_ell)  <=  (lambda_2 / lambda_1) * ( ||ell_perp|| / |u_1^T ell| ),

where theta_ell is the angle between the seed map m_ell = C ell and the backbone
u_1, and ell_perp is the off-backbone part of the seed. We give the pre-proof
strategy (work backward from the angle: tangent = opposite over adjacent in the
spectral coordinates), the proof step by step with words between every step,
decode every symbol, draw the moral (the spectral gap is a funnel), and close on
the balanced caveat (this bounds the AVERAGE / description, not the CONTRAST).

Each scene maps to an ordered list of (text, seconds) beats. The COUNT of beats
here MUST equal the number of play_beat()/wait_beat() calls in the matching scene
class in scenes.py (the beat-count contract enforced by tests/test_sync.py).

Source material (quoted / numbers taken verbatim):
  responses/lnm_critique/sections/02_what_is_entailed.md
    - C = sum_j lambda_j u_j u_j^T,  lambda_1 >= lambda_2 >= ... >= 0
    - m_i = C ell_i = sum_j lambda_j (u_j^T ell_i) u_j
    - cos^2 angle(mbar, u_1) = lambda_1^2 cbar_1^2 / sum_j lambda_j^2 cbar_j^2
      >= lambda_1^2 cbar_1^2 / (lambda_1^2 cbar_1^2 + lambda_2^2 sum_{j>=2} cbar_j^2)
    - as lambda_2/lambda_1 -> 0 the map aligns with u_1
    - worked check: lambda_1 = 10, lambda_2 = 1
    - the contrast Delta = mbar^+ - mbar^- is where signal survives; the
      average / description being backbone-dominated places NO bound on Delta.
  responses/lnm_critique/sections/01_the_charge_formalized.md (via c0101)
    - 3-voxel C eigenvalues lambda = (4.0, 0.3, 0.1); two single-voxel maps
      land within about seven degrees of one another.
"""

SCENES = {
    # ------------------------------------------------------------------
    # S1 — Statement of Theorem R1: the alignment bound.
    # ------------------------------------------------------------------
    "S1_Statement": [
        ("We have met the operator. A lesion seed ell becomes a brain-wide map by one product, m-ell equals C times ell. Now we ask a sharper question. Which way does that map point?", 10.0),
        ("Here is the theorem we will prove. Call theta-ell the angle between the seed's map m-ell and the backbone direction u-one, the leading eigenvector of the connectome.", 9.5),
        ("The claim. The tangent of that angle is at most the spectral gap lambda-two over lambda-one, times the perpendicular seed mass over the backbone seed mass.", 10.0),
        ("Two pieces on the right. Lambda-two over lambda-one is a property of the connectome alone, the ratio of its second to its first eigenvalue. It does not know which patient you have.", 9.5),
        ("The other piece is the seed. Split ell into its component along u-one and the rest. That leftover off-backbone part we name ell-perp; its length is the perpendicular seed mass in the numerator.", 10.5),
        ("Read the shape of the bound. A small spectral gap multiplies whatever the seed brings, forcing the angle theta-ell small. The map is pulled toward u-one almost no matter where the lesion sat.", 10.0),
    ],

    # ------------------------------------------------------------------
    # S2 — Pre-proof strategy: work backward from the angle.
    # ------------------------------------------------------------------
    "S2_Strategy": [
        ("Before any algebra, the strategy. We work backward from the angle itself. An angle is set by a right triangle, so let us find the triangle hiding inside the map.", 9.5),
        ("Expand the map in the eigenbasis. m-ell equals the sum over j of lambda-j, times the loading u-j-transpose-ell, times the eigenvector u-j. Each eigenvector is a clean coordinate axis.", 10.0),
        ("In those coordinates the map splits in two. One piece lies exactly along u-one, the backbone. Everything else lies in the space orthogonal to u-one. Backbone, and off-backbone.", 9.5),
        ("That is the triangle. The along-u-one piece is the adjacent side; the off-backbone piece is the opposite side; and the angle between the map and u-one sits at the corner.", 10.0),
        ("Tangent is opposite over adjacent. So tan theta-ell is the length of the off-backbone piece divided by the length of the backbone piece. The whole proof is now bookkeeping on those two lengths.", 10.5),
        ("Our plan. Compute the adjacent length exactly. Bound the opposite length from above using the second eigenvalue. Divide. The spectral gap lambda-two over lambda-one falls out on its own.", 10.0),
    ],

    # ------------------------------------------------------------------
    # S3 — The proof, step by step.
    # ------------------------------------------------------------------
    "S3_Proof": [
        ("Step one. Write the connectome by its spectrum. C equals the sum over j of lambda-j times u-j u-j-transpose, with the eigenvalues ordered, lambda-one at least lambda-two and so on down to zero.", 10.5),
        ("Step two. Apply C to the seed. Because the u-j are orthonormal, every cross term dies, and m-ell becomes the sum over j of lambda-j, times the loading c-j equals u-j-transpose-ell, times u-j.", 10.5),
        ("Step three. Peel off the leading term. The backbone part of the map is lambda-one times c-one times u-one. Its signed length along u-one is exactly lambda-one times c-one. That is the adjacent side.", 10.5),
        ("Step four. Collect the rest. The off-backbone part is the sum from j equals two onward of lambda-j times c-j times u-j. It lives entirely in the space orthogonal to u-one. That is the opposite side.", 10.5),
        ("Step five. Its squared length, by orthonormality, is the sum from j equals two of lambda-j squared times c-j squared. Pythagoras in the eigenbasis: no cross terms, just a sum of squares.", 10.0),
        ("Step six, the one inequality. Every lambda-j with j at least two is at most lambda-two, since the eigenvalues are ordered. Pull lambda-two squared out of the sum and bound the rest.", 10.0),
        ("What remains inside is the sum from j equals two of c-j squared. That is exactly the squared length of the off-backbone seed, the vector we named ell-perp. So the opposite side is at most lambda-two times the norm of ell-perp.", 10.5),
        ("Step seven. Take the ratio, opposite over adjacent. Tan theta-ell equals that off-backbone length over the absolute value of lambda-one c-one, which is at most lambda-two over lambda-one, times norm ell-perp over the size of c-one.", 11.0),
        ("And c-one is u-one-transpose-ell, the backbone loading of the seed. Substitute it back and the theorem stands: tan theta-ell is at most the spectral gap times norm ell-perp over the absolute backbone loading. Q E D.", 11.0),
    ],

    # ------------------------------------------------------------------
    # S4 — Every symbol explained.
    # ------------------------------------------------------------------
    "S4_Symbols": [
        ("Now decode every symbol, so nothing is taken on faith. Six of them carry the whole statement.", 7.0),
        ("Lambda-one and lambda-two are the top two eigenvalues of the connectome C: the strengths of its two leading patterns. Their ratio lambda-two over lambda-one is the spectral gap.", 10.0),
        ("U-one is the leading eigenvector, the backbone: the single dominant hub pattern that the connectome repeats. It is the direction maps tend to collapse toward.", 9.5),
        ("The loading u-one-transpose-ell is one number: how much of the seed already points along the backbone. Big when the lesion sits on the hub system, small when it sits off it.", 10.0),
        ("Ell-perp is the off-backbone part of the seed, what is left of ell after you subtract its u-one component. Its norm is the perpendicular seed mass, the numerator of the bound.", 10.0),
        ("And theta-ell is the angle between the map m-ell and u-one. Tangent small means the map hugs the backbone; tangent large means it has escaped it. That is the quantity the theorem controls.", 10.5),
    ],

    # ------------------------------------------------------------------
    # S5 — The moral: the spectral gap is a funnel.
    # ------------------------------------------------------------------
    "S5_Moral": [
        ("Now the moral, the reason this theorem matters. The spectral gap is a funnel.", 6.5),
        ("Look again at the right side. The seed's own geometry, the ratio of off-backbone to on-backbone mass, can be anything. The connectome multiplies it by the gap lambda-two over lambda-one.", 10.0),
        ("When that gap is small, when lambda-one towers over lambda-two, the product is small whatever the seed does. Every seed's angle to the backbone is squeezed toward zero.", 9.5),
        ("In the source's worked numbers, lambda-one is ten and lambda-two is one: a gap of one tenth. And in the tiny three-voxel connectome, eigenvalues four, zero point three, zero point one, two very different single-voxel lesions land within about seven degrees of u-one.", 11.5),
        ("So the convergence of maps toward u-one is not a coincidence and not a flaw introduced by anyone. It is a property of the connectome's spectrum, geometry, funnelling many seeds into one direction.", 10.5),
        ("That is why an addiction average, a depression average, and even a bag of random seeds look alike. They all fall through the same funnel and land on the same backbone u-one.", 10.0),
    ],

    # ------------------------------------------------------------------
    # S6 — Caveat: this bounds the description, not the contrast.
    # ------------------------------------------------------------------
    "S6_Caveat": [
        ("One caveat, and it is the whole balance of the argument. Be precise about what this theorem does and does not say.", 8.0),
        ("What it bounds is a description. The angle of a single seed's map, and therefore of the group average m-bar, the picture you get by pooling and averaging symptomatic patients. The funnel governs that average.", 10.5),
        ("It says nothing yet about the contrast. Take the symptomatic average minus the asymptomatic average, Delta. In Delta the shared backbone term subtracts away; the backbone loadings are roughly equal, so the leading u-one piece cancels.", 11.0),
        ("And the theorem places no upper bound on Delta. It controls how far each average leans on u-one; it is silent on the difference between two such averages, where the symptom signal actually lives.", 10.5),
        ("So read this as geometry, not a verdict. A small spectral gap explains why average maps look alike. It does not show that a symptom contrast carries no signal. The method is not debunked here, only described.", 11.0),
        ("That gap, between a true statement about the average and a claim about the contrast, is exactly where the next chapters work. The funnel is real. What survives it is the question we keep open.", 10.5),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:16s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words:3d}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':16s} target={grand:6.1f}s ({grand/60:.1f} min)")
