"""Narration for c0201_spectral_decomposition — "The connectome has a spectrum".

Each scene maps to an ordered list of (text, seconds) beats. The text is shown as
a subtitle in manim AND spoken by the TTS pass; `seconds` is the on-screen target
duration. The count of beats here MUST equal the number of play_beat()/wait_beat()
calls in the matching scene class in scenes.py (the beat-count contract).

Source material (quoted / paraphrased):
  responses/lnm_critique/sections/02_what_is_entailed.md
    - C = sum_j lambda_j u_j u_j^T  with  lambda_1 >= lambda_2 >= ... >= 0
    - m_i = C ell_i = sum_j lambda_j (u_j^T ell_i) u_j
    - the leading term lambda_1 c_1 u_1 ; the backbone u_1
    - the cos^2 angle bound toward u_1 as lambda_2 / lambda_1 -> 0
  Worked 3x3 numbers (the 3-voxel C and its spectrum) are the source's:
    eigenvalues lambda = (4.0, 0.3, 0.1).
"""

SCENES = {
    # S1 — Motivation: why decompose C at all.
    "S1_Motivation": [
        ("We have the map operator: m equals C times ell. Every map the method makes is a column-combination of one fixed matrix, the connectome C.", 9.0),
        ("So if we want to understand the maps, we must understand C. And a matrix this size, written as a grid of numbers, hides its structure completely.", 9.0),
        ("There is a better coordinate system. C is symmetric, and a symmetric matrix can be taken apart into a set of natural patterns, each with a weight.", 9.5),
        ("That decomposition is the spectrum. It will tell us, before any patient is seen, which directions C amplifies and which it barely touches.", 9.0),
        ("And it is the cleanest way to see why so many different lesions produced nearly the same map. The answer is hiding in the spectrum of C.", 9.0),
    ],

    # S2 — The eigen-equation C u_j = lambda_j u_j.
    "S2_Eigen": [
        ("Here is the central equation. C applied to a special vector u-j returns the very same vector, just rescaled by a number lambda-j.", 9.0),
        ("The vector u-j is an eigenvector of C. We call it a connectome pattern: a fixed brain-wide shape that C does not rotate, only stretches.", 9.5),
        ("The number lambda-j is its eigenvalue. It measures how much of C that pattern carries: how strongly C amplifies anything pointing along u-j.", 9.5),
        ("We choose these patterns to be orthonormal. Each u-j has unit length, and any two different patterns are perpendicular: their inner product is zero.", 9.5),
        ("Orthonormal means they form a clean set of axes. We can write any lesion, and any map, as a combination of these patterns with no overlap between them.", 9.5),
        ("So read the equation as a sorting machine. Feed C a pattern, and out comes the same pattern with a price tag, lambda-j, stamped on it.", 9.0),
    ],

    # S3 — The full decomposition C = sum_j lambda_j u_j u_j^T.
    "S3_Decomposition": [
        ("Collect every pattern and its weight, and you can rebuild C entirely. C equals the sum over j of lambda-j times u-j u-j transpose.", 9.5),
        ("Look first at that outer product, u-j times u-j transpose. A column vector times a row vector is not a number, it is a whole matrix.", 9.0),
        ("And it is the simplest kind of matrix: rank one. Every one of its columns is just a rescaled copy of the single pattern u-j.", 9.0),
        ("So each term lambda-j u-j u-j transpose is one rank-one layer: the pure pattern u-j, with intensity set by its eigenvalue lambda-j.", 9.5),
        ("Add the layers and they reassemble the connectome. C is not a grid of arbitrary numbers; it is a short stack of weighted patterns.", 9.0),
        ("This is the spectral decomposition. It is exact, it loses nothing, and it works for any symmetric matrix, so it always applies to C.", 9.0),
    ],

    # S4 — Ordering lambda_1 >= lambda_2 >= ... >= 0 and what "dominant" means.
    "S4_Ordering": [
        ("Now order the weights. We list the eigenvalues from largest to smallest: lambda-one is at least lambda-two, at least lambda-three, and so on, down to zero.", 9.5),
        ("Because C is built from connectivity, these weights are never negative. C is what we call positive semidefinite: every lambda is greater than or equal to zero.", 9.5),
        ("The first pattern, u-one, carries the largest weight, lambda-one. It is the loudest layer in the stack, the one that dominates the sum.", 9.0),
        ("How dominant it is, we read from the spectral gap: the ratio lambda-two over lambda-one. When that ratio is small, the second pattern is a whisper next to the first.", 9.5),
        ("Dominant has a precise meaning here. If lambda-one dwarfs the rest, then anything C touches comes out leaning heavily toward the first pattern, u-one.", 9.5),
        ("That is a property of the matrix alone. The ordering of the spectrum is fixed before a single lesion is chosen, before the disease gets a vote.", 9.0),
    ],

    # S5 — A concrete 3x3 example with eigenvalues 4.0, 0.3, 0.1.
    "S5_Example": [
        ("Make it concrete with the source's three-voxel connectome. We do not have to imagine the spectrum; we can compute it.", 8.5),
        ("Its three eigenvalues are four point zero, zero point three, and zero point one. Already ordered, largest to smallest, and all non-negative.", 9.0),
        ("One eigenvalue towers over the others. Four point zero against zero point three and zero point one: the first pattern carries the overwhelming share of C.", 9.5),
        ("The spectral gap makes it stark. Lambda-two over lambda-one is zero point three over four, under one tenth. The second layer is faint beside the first.", 9.5),
        ("So even this tiny matrix is, for practical purposes, nearly rank one. To a good approximation C is just lambda-one times u-one u-one transpose.", 9.5),
        ("And that single tall eigenvalue is exactly why two lesions in different voxels gave maps only a few degrees apart. They both inherited u-one.", 9.5),
    ],

    # S6 — Name the leading pattern u_1 the backbone; preview the maps lean on it.
    "S6_Backbone": [
        ("The leading pattern earns a name. We will call u-one the backbone of the connectome: the single dominant direction baked into C.", 9.0),
        ("Write any map in the spectral basis: m equals C ell equals the sum of lambda-j times the loading u-j transpose ell, along each pattern u-j.", 9.5),
        ("That loading, u-j transpose ell, is just how much the lesion points along pattern j. The inner product of the lesion with that connectome shape.", 9.5),
        ("The leading term, lambda-one times the backbone loading times u-one, is the largest by far, because lambda-one is the largest weight.", 9.5),
        ("So every average map gets dragged toward the backbone. That is geometry, a fact about the spectrum of C, not yet a verdict on the method.", 9.5),
        ("It explains why average maps look alike. It says nothing yet about whether a symptom contrast carries signal. That contrast is the next chapter's question.", 9.5),
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
