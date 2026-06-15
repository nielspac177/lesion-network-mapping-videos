"""Narration for c0703_shared_backbone_inflation — "Shared-backbone inflation".

Source: responses/lnm_critique/sections/05_the_convergence_trap.md

The convergence (sign-agreement) map feels like discovery: many independently
derived maps agreeing on the same circuit. We show that under R1's
backbone-sharing model r_k = mu + eps_k, near-total agreement is the DEFAULT,
not a finding. The independent-coins yardstick is 2^(1-K) (K=8 -> 0.8%); the
honest yardstick is p^K + (1-p)^K, which -> 1 as the backbone dominates the sign.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — a shared-backbone model:  r_k = mu + eps_k
    "S1_Model": [
        ("A convergence map keeps the voxels where several lesion maps all point the same way. Agreement feels like discovery. Let us model it.", 9.5),
        ("Following R1, write each cohort's map as r sub k equals mu plus epsilon sub k. One shared part, plus a cohort-specific wobble.", 9.0),
        ("Mu of v is the shared backbone value at voxel v: roughly lambda one times the loading, times u sub one of v, the dominant component of C.", 9.5),
        ("The crucial feature is that mu is common to all K maps. It carries no subscript k. It is the same cheat sheet copied into every map.", 9.0),
        ("Epsilon sub k of v is the cohort-specific deviation, independent across cohorts, with some noise scale sigma. This part does carry a k.", 9.0),
        ("Now fix a voxel and define p: the probability that one map recovers the backbone's sign. The chance a single map matches mu's sign here.", 9.0),
        ("Where the backbone dominates the noise, p is close to one. Where mu is small and noise rules, p drifts toward one half. Hold on to p.", 9.0),
    ],
    # S2 — Pr[all K agree] = p^K + (1-p)^K, vs independent 2^(1-K)
    "S2_Derive": [
        ("We want the probability that all K maps agree in sign at this voxel. Agreement is an intersection, so let us count the ways it happens.", 9.0),
        ("All K agree in exactly two disjoint ways: every map lands on the backbone sign, or every map lands on the opposite sign. Just those two.", 9.0),
        ("Each map matches the backbone sign with probability p, independently, so all K matching has probability p to the power K.", 8.5),
        ("Each map takes the opposite sign with probability one minus p, so all K opposing has probability one minus p, to the power K.", 8.5),
        ("The two events are disjoint, so add them. The probability that all K agree is p to the K plus one minus p to the K.", 8.5),
        ("Contrast the honest yardstick almost nobody uses: if the signs were independent fair coins, agreement would be two to the one minus K.", 9.0),
        ("That independent baseline shrinks geometrically: it halves with every extra map. Our backbone formula, as we will see, does not.", 8.5),
    ],
    # S3 — as p -> 1, p^K + (1-p)^K -> 1 for every K
    "S3_Limit": [
        ("Now push the backbone to dominate. Let p approach one: each map almost surely recovers the backbone's sign.", 8.0),
        ("Then p to the K approaches one, and one minus p to the K approaches zero. The sum approaches one, for every value of K.", 8.5),
        ("Watch what that kills. The number of maps K no longer protects you. Agreement becomes near-certain no matter how many studies you stack.", 9.0),
        ("On the curve, as p climbs from one half toward one, the agreement probability rises and presses up against one. It saturates.", 8.5),
        ("And the derivative confirms it: on the interval one half to one, K p to the K minus one minus K times one minus p to the K minus one is positive.", 9.5),
        ("So the function only increases as p approaches one, where it equals one exactly. The agreement is driven entirely by mu, the shared backbone.", 9.0),
        ("Not by any disease-specific effect. The same connectome, written into every map, manufactures the agreement all by itself.", 8.5),
    ],
    # S4 — the baseline collapses: 0.8% for K=8 becomes ~100%
    "S4_Collapse": [
        ("Put numbers on it and the collapse is stark. Take eight cohorts, K equals eight.", 7.0),
        ("Under independent coins, two to the one minus eight is two to the minus seven: about zero point eight percent of the brain. Impressively rare.", 9.0),
        ("That tiny baseline is the world where convergence is informative. A large agreement set across eight cohorts would be wildly improbable.", 9.0),
        ("But the maps are not independent coins. They share a backbone, which R1 says they always do. So use the right formula.", 8.5),
        ("Take p equals zero point nine, K equals four. Independent gives twelve point five percent. The shared backbone gives about sixty-six percent.", 9.5),
        ("Same K, same operator, more than a fivefold jump. As p climbs toward one the eight-cohort number runs from zero point eight percent up to nearly one hundred.", 9.5),
        ("So the evidence evaporates. Agreement is the default, not a discovery. A big convergence set is exactly what the backbone alone predicts.", 9.0),
    ],
    # S5 — moral: convergence certifies the funnel, not a disease network
    "S5_Moral": [
        ("Step back to the moral. A large convergence map is consistent with two completely different worlds, and it cannot tell them apart.", 9.0),
        ("World one: the disorders share a real, disease-specific circuit. World two: the maps merely share the connectome backbone and nothing else.", 9.0),
        ("Both worlds produce big agreement sets. The raw convergence map cannot separate them, because the backbone-only null produces agreement readily.", 9.5),
        ("And evidence has to be something the null would not readily produce. This null produces it readily, so convergence is not that evidence.", 9.0),
        ("Cross-study convergence therefore certifies the shared backbone, the funnel that every seed falls into. It does not certify a disease network.", 9.0),
        ("It is the same lesson as the average map, now wearing the costume of agreement. The average described the funnel; convergence redraws it.", 9.0),
        ("So never headline a convergence map. The inference lives in the backbone-calibrated contrast, not in agreement that the connectome gave you for free.", 9.5),
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
