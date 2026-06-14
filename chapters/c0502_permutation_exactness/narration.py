"""Narration for c0502_permutation_exactness — "Permutation exactness (full proof)".

Source: responses/lnm_critique/sections/03_the_right_null.md  (the symptom-label
        null; the boxed theorem "Permutation exactness (Vol 4, T4), specialized",
        lines 75-82, and its proof sketch)
        responses/lnm_critique/papers/REBUTTAL_sound.md  (the symptom-label
        permutation null endorsed by the rebuttal; the zero-false-positive result)

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

Numbers are written as words for TTS.
"""

SCENES = {
    # S1 — the exactness claim, every symbol named
    "S1_Statement": [
        ("We have argued that the symptom-label null is the right question to ask. Now we earn the word that makes it powerful: exact.", 9.0),
        ("Here is the claim in full. The permutation p-value, p, equals one over the size of G, times the sum over pi in G of an indicator.", 9.5),
        ("That indicator is one when the statistic on the relabeled data, T of y-sub-pi, is at least the statistic on the observed data, T of y-sub-id.", 9.5),
        ("G is a subgroup of S-n, the symmetric group of all n-factorial label permutations. G keeps those relabelings under which the null leaves the data's law unchanged.", 9.5),
        ("The size of G, written with the vertical bars, counts how many relabelings there are. For two impaired and two spared out of four, that is six.", 9.0),
        ("y-sub-id is the identity labeling, the one we actually observed. y-sub-pi is what you get after applying the permutation pi to the labels.", 9.0),
        ("The claim: under the null, the probability that p is at most alpha is itself at most alpha, in finite samples, with no distributional assumption.", 9.5),
        ("Distribution-free, exact, finite-sample. No normality, no large-n. We now prove it from one idea: exchangeability.", 8.5),
    ],
    # S2 — pre-proof strategy
    "S2_Strategy": [
        ("Before the proof, the strategy, so every step has a destination. The whole argument rides on one word from the null: exchangeable.", 9.0),
        ("Exchangeable means that under the null, any assignment of the observed labels to the observed patients is equally likely. No labeling is special.", 9.5),
        ("So the observed statistic T of y-sub-id is not privileged. It is just one draw from the bag of values you get by relabeling.", 9.0),
        ("Picture the orbit: the set of all statistics T of y-sub-pi as pi ranges over G. Exchangeability makes every element of that set equally likely.", 9.5),
        ("If every element is equally likely, then where the observed value lands in the sorted orbit, its rank, is uniform. No position is favored.", 9.5),
        ("And a uniform rank is all we need. The chance of landing in the top alpha fraction of a uniform draw is at most alpha. That is the finish line.", 9.5),
        ("So the plan is three moves: exchangeability gives identical distribution, identical distribution gives a uniform rank, a uniform rank gives the bound.", 9.5),
        ("Notice what is missing from that plan: any model for the maps. The validity will come from symmetry, not from an assumed distribution.", 9.0),
    ],
    # S3 — the proof
    "S3_Proof": [
        ("Now the proof, one step at a time, with words between every line. Assume the symptom null holds, so the labels are exchangeable over G.", 9.0),
        ("Step one. Exchangeability says y is equal in distribution to y-sub-pi for every pi in G. The labels permuted look statistically identical to the originals.", 9.5),
        ("Step two. Apply the same fixed function T to both sides. If y and y-sub-pi share a distribution, then T of y and T of y-sub-pi do too.", 9.5),
        ("So the values in the orbit, T of y-sub-pi for pi in G, are identically distributed. The observed T of y-sub-id is exchangeable with all of them.", 9.5),
        ("Step three. Among the size-of-G values in that orbit, the rank of the observed value is uniform on the integers one through the size of G.", 9.5),
        ("Step four. The p-value counts the fraction of permutations whose statistic is at least the observed. That fraction is exactly the upper-tail rank.", 9.5),
        ("Because the rank is uniform, the probability that this fraction is at most alpha is at most alpha. Ties only push p larger, making it more conservative.", 9.5),
        ("Therefore the probability that p is at most alpha is at most alpha, for every alpha. That is the claim. The proof is pure counting.", 9.0),
    ],
    # S4 — every symbol decoded, tied back to the formula
    "S4_Symbols": [
        ("Let us slow down and name every symbol once more, against the formula itself, so nothing on screen is a black box.", 8.5),
        ("G is the relabeling group: the set of permutations of the symptom labels that the null treats as equivalent. Often a covariate-respecting subgroup.", 9.5),
        ("The vertical bars around G are its size, the count of relabelings. For n patients with n-one impaired, it is n factorial over n-one factorial n-zero factorial.", 9.5),
        ("pi is a single permutation, one rule for shuffling who is labeled impaired and who is spared. y-sub-pi is the label vector after applying pi.", 9.5),
        ("The indicator, the one in brackets, is a yes-no counter: it returns one when the permuted statistic meets or beats the observed, and zero otherwise.", 9.5),
        ("The rank is where the observed statistic sits in the sorted orbit; under the null it is uniform, and the p-value is just its upper-tail position.", 9.5),
        ("And alpha is the level we chose in advance, our tolerance for a false alarm. The theorem promises the true error never exceeds it.", 9.0),
        ("Read the formula again with those names and it says exactly: count the relabelings at least as extreme as what we saw, then divide by how many there are.", 9.5),
    ],
    # S5 — the moral
    "S5_Moral": [
        ("So step back and take the moral. The exactness was purely combinatorial. It never asked the maps to be normal, or the sample to be large.", 9.0),
        ("It did not care that each map is backbone-dominated, ugly, low-dimensional, or shared across disorders. It cared only that the labels are exchangeable.", 9.5),
        ("The validity comes from the symmetry of the null, not from a model of the data. That is what distribution-free and finite-sample really mean.", 9.0),
        ("And this is exactly why the symptom null can be trusted where the location null could not. The location null asked whether a place was special.", 9.0),
        ("The backbone made every place look alike, so that null was glued to the observed value. No symmetry it could lean on, nothing to reject.", 9.0),
        ("The symptom null instead leans on label exchangeability, a symmetry the backbone cannot break, because the backbone is label-free and cancels in the contrast.", 9.5),
        ("So the witness lands clean: with the right null and standard thresholds, the rebuttal found zero false positives in a thousand iterations at t above ten.", 9.5),
        ("One assumption, defended honestly, buys an exact test. That is the whole worth of asking the right question.", 8.0),
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
