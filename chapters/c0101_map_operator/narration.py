"""Narration for c0101_map_operator — "The Map Operator, symbol by symbol".

Each scene maps to an ordered list of (text, seconds) beats. The text is shown as
a subtitle in manim AND spoken by the TTS pass; `seconds` is the on-screen target
duration. The count of beats here MUST equal the number of play_beat()/wait_beat()
calls in the matching scene class in scenes.py (the beat-count contract).

Source material (quoted / paraphrased, page-cited where the .md does):
  responses/lnm_critique/sections/00_abstract_intro.md
  responses/lnm_critique/sections/01_the_charge_formalized.md   (C definition, 3-voxel C, eigenvalues, columns)
  responses/lnm_critique/sections/02_what_is_entailed.md
"""

SCENES = {
    # S1 — Motivation: what LNM asks.
    "S1_Motivation": [
        ("You have a patient with a brain lesion and a symptom. You do not trust the lesion's location alone, because lesions in scattered places can produce the very same deficit.", 9.5),
        ("So you ask a connectivity question instead. What is this damaged tissue wired to?", 6.5),
        ("To answer it, you do not scan the patient. You look the lesion up in a normative connectome: a group-averaged atlas of how every brain region connects to every other, built once from healthy controls.", 10.5),
        ("The lesion's network is the set of regions that atlas says it touches. Pool many patients with the same symptom, average their maps, and you get the circuit whose disruption tends to produce it.", 10.0),
        ("This whole machine is one matrix and one product. Let us build it symbol by symbol, so nothing is hidden.", 7.5),
    ],

    # S2 — The connectome C, symbol by symbol.
    "S2_Connectome": [
        ("First, the connectome. C is a square matrix, V by V: one row and one column for every voxel in the atlas.", 8.5),
        ("Its entry C-a-b is the normative functional connectivity between voxel a and voxel b. How strongly those two voxels co-activate in healthy brains.", 9.0),
        ("Two facts about real connectomes drive everything that follows. First, C is symmetric: the wiring from a to b equals the wiring from b to a, so C-a-b equals C-b-a.", 9.5),
        ("Second, it is normalized and roughly low-rank: a handful of patterns explain most of it, and one dominant pattern is the hub, or degree, pattern. We will call it the backbone.", 10.0),
        ("Here is the smallest example that shows the mechanism, taken straight from the source: a three-voxel C, every number checkable by hand.", 8.5),
        ("Read the diagonal: voxel one is the strongly connected hub, at two point six three five. Read off-diagonal, and notice it mirrors across: one point four eight eight sits in both the a-b and the b-a slot.", 10.5),
    ],

    # S3 — The lesion ell.
    "S3_Lesion": [
        ("Now the lesion. We write it as ell, a column vector with one entry per voxel.", 7.0),
        ("Every entry is either zero or one. It is an indicator. Ell-b equals one when voxel b was destroyed, and zero when it was spared.", 9.0),
        ("So ell is not a strength and not a measurement. It is pure geometry: it simply marks which voxels the lesion occupies.", 8.0),
        ("Here a lesion hits voxels one and three but spares voxel two. Ell is one, zero, one.", 7.0),
        ("That is the entire input from the patient. The connectome C never saw this patient; only ell does. Hold that thought, because it matters later.", 8.5),
    ],

    # S4 — The product m = C ell, unpacked term by term.
    "S4_Product": [
        ("The lesion network map is one matrix-vector product. m equals C times ell.", 6.5),
        ("m is the output: a brain-wide map, one number per voxel. It lives in the same V-dimensional space as a single column of C.", 8.5),
        ("To see what it means, read out a single voxel a. The a-th entry of C ell is the sum over b of C-a-b times ell-b.", 9.0),
        ("Walk the terms. We march across row a of C, and against each entry we place the lesion's zero or one.", 8.0),
        ("Where the lesion is zero, the whole term is zero: that voxel contributes nothing. Where the lesion is one, the term is exactly C-a-b: voxel a's connectivity to that damaged voxel.", 10.0),
        ("So the sum keeps only the connectivity from voxel a into the damaged set. The a-th map value is the total wiring from voxel a into the wound.", 9.5),
        ("That is the operator, fully decoded. C provides the wiring, ell selects the damaged columns, and the sum totals the connectivity into the lesion.", 9.0),
    ],

    # S5 — Tiny numeric worked example: single-voxel lesion picks a column.
    "S5_WorkedExample": [
        ("Now do it with numbers. Take the simplest lesion of all: a single voxel. Lesion only voxel one, so ell is one, zero, zero.", 9.0),
        ("In the sum over b, only the term where ell is one survives. The b-equals-one term. Every other term is multiplied by zero and vanishes.", 9.5),
        ("So each map entry collapses to C-a-one, times one. The map is exactly the first column of C.", 8.5),
        ("Read it straight off: m equals two point six three five, one point four eight eight, one point zero five four. That is column one, unchanged.", 9.0),
        ("This is the clean fact to keep. A single-voxel lesion just hands you back that voxel's column of the connectome. The lesion selects; the connectome speaks.", 9.5),
        ("And because voxel one is the hub, its column is large and hub-shaped. Any lesion that touches voxel one inherits that same hub shape.", 9.0),
    ],

    # S6 — The mystery, posed as an open question (no pre-concession).
    "S6_Mystery": [
        ("Here is where it gets strange, and where a real fight broke out in twenty twenty-six.", 6.0),
        ("Lesion voxel one alone and you get its column: two point six three five, one point four eight eight, one point zero five four.", 8.5),
        ("Now lesion voxel three instead, a completely different place. Its column is one point zero five four, zero point five nine seven, zero point five four zero.", 9.0),
        ("Smaller numbers, but point them in the same direction and the shapes are strikingly alike. In the source's three-voxel example, both maps land within about seven degrees of one another.", 10.0),
        ("Different lesions, in different places, producing nearly the same map. Why would that happen? Is the map telling us about the lesion, or about the matrix?", 9.5),
        ("Hold that question open. We have not yet earned an answer; that is the debate the next chapters take up. For now, we have only built the operator and met its mystery.", 10.0),
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
