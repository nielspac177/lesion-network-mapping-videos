"""Narration for c0601_backbone_subspace — "The backbone subspace and projector".

Source: responses/lnm_critique/sections/04_removing_the_backbone.md

This chapter is the linear-algebra setup for residualization (c0602). It recalls
the spectral decomposition of C, defines the backbone subspace B as the span of
the leading eigenvectors, builds the orthogonal projector Pi_B onto it, forms the
complementary projector onto the residual subspace, and motivates the whole
construction with the camera-versus-court framing: strip the shared backbone,
keep the discriminative remainder.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — recall the spectrum of C
    "S1_Recall": [
        ("Before we remove the backbone, we have to name it precisely. So recall the spectral picture of the connectome.", 8.5),
        ("The normative connectome C is a symmetric matrix over V voxels. Symmetric matrices split into a clean sum.", 8.5),
        ("C equals the sum over j of lambda-j times u-j u-j-transpose. Let us decode every piece of that line.", 8.0),
        ("Lambda-j is the j-th eigenvalue, a single number: how much weight that mode carries. We order them, lambda-one at least lambda-two, and on down.", 9.5),
        ("u-j is the j-th eigenvector, a unit-length direction in voxel space. These directions are orthonormal: each unit length, every pair perpendicular.", 9.5),
        ("u-j u-j-transpose is an outer product: a column times a row, giving a V-by-V matrix that projects onto the single direction u-j.", 9.0),
        ("So C is a weighted stack of one-dimensional projectors, each scaled by its eigenvalue lambda-j. That is the whole content of the spectrum.", 9.0),
        ("And the leading few modes carry the backbone: u-one is the dominant degree mode, the shared skeleton every seed lights up.", 8.5),
    ],
    # S2 — the backbone subspace B
    "S2_Subspace": [
        ("Now we collect the leading modes into one object. Pick a rank r, the number of top modes you judge to be backbone.", 8.5),
        ("Define the backbone subspace B as the span of u-one through u-r: every direction you can build from those r eigenvectors.", 9.0),
        ("Span means all linear combinations. Take any weights c-one through c-r, form c-one u-one plus dot dot dot plus c-r u-r; the set of all such vectors is B.", 10.0),
        ("Because the u-j are orthonormal, these r directions are independent. So B is an honest r-dimensional subspace sitting inside the V-dimensional voxel space.", 9.5),
        ("Geometrically, B is the flat that contains the backbone. Every map that is pure backbone lives entirely inside it.", 8.5),
        ("How do we choose r? Plot the eigenvalues lambda-j and look for the elbow, the gap where the values drop from huge to ordinary.", 9.0),
        ("R-one's threat lives in those few huge, flat eigenvalues. Take r up to that elbow: the modes shared by every seed, no more.", 9.0),
        ("And r is chosen from C alone, before any patient label is seen. That label-blindness is what keeps the later inference honest.", 8.5),
    ],
    # S3 — the projector Pi_B
    "S3_Projector": [
        ("With the subspace named, we build the operator that lands a vector on it. Meet the projector onto B, written Pi-sub-B.", 8.5),
        ("Pi-B equals the sum over j from one to r of u-j u-j-transpose: exactly the leading r outer products from the spectrum, with the lambdas dropped.", 9.5),
        ("Each u-j u-j-transpose projects onto one backbone direction. Add the first r of them and you project onto the whole backbone subspace B.", 9.0),
        ("Apply it to any vector v. Pi-B v keeps the part of v that lies inside B, and discards everything pointing out of it.", 8.5),
        ("A projector earns its name through two properties. First, idempotent: apply it twice and nothing new happens. Pi-B times Pi-B equals Pi-B.", 9.5),
        ("That is geometry, not algebra-trivia: once you have landed inside B, projecting again leaves you put. You are already there.", 8.0),
        ("Second, symmetric: Pi-B transposed equals Pi-B. That makes it an orthogonal projector, dropping v straight down onto B at a right angle.", 9.0),
        ("So Pi-B is a fixed, label-independent linear operator, known the moment C is known. That fixedness is the source of every good property to come.", 9.5),
    ],
    # S4 — the orthogonal complement
    "S4_Complement": [
        ("We have the operator that keeps the backbone. Now we want its mirror image: the operator that throws the backbone away and keeps the rest.", 9.0),
        ("Write it Pi-B-perp, the complementary projector. It equals I minus Pi-B, the identity matrix minus the backbone projector.", 9.0),
        ("I is the identity: the do-nothing operator. I times v returns v unchanged, leaving every voxel exactly as it was.", 8.5),
        ("So I minus Pi-B says: take the whole vector, then subtract off its backbone part. What remains is everything orthogonal to the backbone.", 9.0),
        ("Pi-B-perp projects onto the residual subspace, the orthogonal complement of B, spanned by the trailing modes u-r-plus-one onward.", 9.0),
        ("And the two projectors split any vector cleanly. Pi-B v plus Pi-B-perp v equals v, because Pi-B plus the identity-minus-Pi-B is just the identity.", 9.5),
        ("The two pieces are perpendicular: the backbone part and the residual part meet at a right angle and share nothing.", 8.0),
        ("So every map decomposes, with no overlap and no leftover, into a backbone half inside B and a residual half outside it.", 8.5),
    ],
    # S5 — why build this machinery
    "S5_Why": [
        ("Step back and ask what all this machinery is for. The goal is one clean operator that removes exactly the backbone and keeps exactly the rest.", 9.0),
        ("Pi-B-perp is that operator. Hand it a lesion map and it deletes the shared skeleton in one stroke, with no estimation and no tuning beyond r.", 9.0),
        ("And it deletes the right thing. The group-average backbone is what R-one proved is shared across disorders, so it cannot be where a disease-specific signal lives.", 9.5),
        ("Think of the camera versus the court. A photo of any room is mostly the room, shared by every photo. The face you want is the thin part that differs.", 9.5),
        ("The backbone is the room. Pi-B-perp strips the shared part away so the discriminative part, the part that could carry a disorder, stands out.", 9.0),
        ("In the next chapter we apply this operator to the maps themselves: the residualized map, m-tilde equals Pi-B-perp times C times the seed.", 9.0),
        ("That residual is where every honest contrast will be run. Here we built the operator. Next, we put it to work.", 8.0),
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
