"""Narration for v0609_conformal_for_lnm — "Conformal prediction for lesion-to-outcome".

Closes the series. E-values (Vol 5) gave anytime-valid evidence for a lesion-symptom
LINK; conformal (Vol 6) gives calibrated prediction SETS for an individual outcome.
Both ride on top of the same LNM machinery: m_i = C l_i.

Sources (quote only; invent no constants):
  volumes/vol6_conformal/chapters/01_the_guarantee.md
  responses/lnm_critique/sections/06_single_target.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the prediction task
    "S1_Task": [
        ("To close the series, we ask the question the clinic actually asks at the bedside: what is this one patient's outcome, and how much should I trust the number?", 10.0),
        ("Recall the single-target setup. Patient i has a lesion indicator l-sub-i, a zero-one vector marking which voxels were destroyed.", 9.0),
        ("Push that seed through the normative connectome C and you get the patient's lesion network map, m-sub-i equals C times l-sub-i.", 9.0),
        ("Each patient is a pair: features x-sub-i, built from the map, and an outcome y-sub-i, say ataxia after thalamotomy.", 8.5),
        ("A plain predictor hands back a point estimate, like ataxia probability zero-point-two-three. At a cohort of a few dozen, that number leans on an asymptotic story your sample size cannot honor.", 10.0),
        ("So we want more than a point. We want a prediction set with a coverage guarantee: a set of answers the truth lands inside a stated fraction of the time.", 9.5),
    ],
    # S2 — a nonconformity score for outcomes
    "S2_Score": [
        ("Conformal prediction builds that set from a nonconformity score, a single number measuring how strange each patient looks to the model.", 9.0),
        ("For a continuous outcome the natural choice is the absolute residual: s-sub-i equals the size of y-sub-i minus y-hat of m-sub-i.", 9.0),
        ("Decode it. y-sub-i is the true outcome. y-hat of m-sub-i is whatever the model predicted from that patient's map. The bars take the absolute value.", 9.5),
        ("A small score means the model nailed that patient. A large score means the patient is surprising. The score just ranks patients by surprise.", 8.5),
        ("Here is the crucial part. y-hat can be any L N M predictor at all, even the residualized-map model that strips the backbone before fitting.", 9.0),
        ("Validity does not require the model to be correct. The guarantee comes from how the scores rank, not from believing the predictor. You do not have to trust the model.", 9.5),
    ],
    # S3 — the outcome prediction set
    "S3_Set": [
        ("Split conformal turns those scores into a set. Hold out a calibration batch, score every calibration patient, and take a high quantile of the scores. Call it q-hat.", 10.0),
        ("Then for a new patient the prediction set is simply y-hat of m-test, plus or minus q-hat. An interval centered on the model's guess.", 9.0),
        ("The radius q-hat is the calibration quantile: it is exactly as wide as the model's typical mistake on patients it had not seen.", 9.0),
        ("The promise, K-one, is this. The probability that the true outcome y lies in that set is at least one minus alpha.", 8.5),
        ("Pick alpha equal to zero-point-one and you are promising ninety percent coverage. It is distribution-free, finite-sample, and holds for any model.", 9.5),
        ("And the bound is two-sided: coverage lands between one minus alpha and one minus alpha plus one over n plus one. At least ninety percent, and not wastefully more.", 10.0),
        ("So the wider the set, the less the model knew. The set itself carries the honesty the point estimate hid.", 8.0),
    ],
    # S4 — compare against the degree baseline
    "S4_BeatBaseline": [
        ("Now the move that makes this useful, not just valid. A predictor that always returns the whole real line is valid and worthless. Coverage alone can be gamed by refusing to commit.", 10.0),
        ("So we report a second number, sharpness: how small the sets are. The honest report is coverage and mean set width together.", 8.5),
        ("That gives us a clean contest. Conformalize two models to the same coverage, then compare their set widths. The sharper model wins.", 9.0),
        ("Model one is the residualized-map predictor, which uses the patient-specific connectivity fingerprint after the backbone is stripped.", 9.0),
        ("Model two is the degree-and-size baseline: predict outcome from u-one transpose l, the seed's loading on the leading connectome component, plus lesion size s-sub-i.", 10.0),
        ("This is exactly Part eight, Move three: make degree the thing to beat. The critique's worry was that maps only recover degree, so we put degree in the baseline.", 10.0),
        ("If the fingerprint model produces genuinely tighter intervals at the same coverage, it found signal the backbone alone cannot give. Sharpness is the discriminator. The rebuttal already clears degree: same-symptom r equals zero-point-four-four versus zero-point-one-six to degree.", 11.0),
    ],
    # S5 — the exchangeability caveat
    "S5_Exchange": [
        ("Every guarantee has a price, and conformal's price is exactly one assumption: exchangeability of the patients.", 8.5),
        ("Exchangeability means order carries no information. The joint law of the patient pairs Z is unchanged under any reordering pi. Shuffle the patients and the world looks the same; no patient is special by when they arrived.", 11.0),
        ("It is weaker than independent and identically distributed, and crucially it must include the new patient. The promise covers the test patient only because it is just another draw from the same pot.", 10.0),
        ("So the moment the new patient comes from a different pot, the assumption breaks. A new scanner, a sicker site, a drifted technique. That is distribution shift.", 9.5),
        ("This is the failure we measured back in Vol six chapter six. Coverage degrades, and conformal will not warn you. It is fragile, and it is about your data, not your model.", 9.5),
        ("So the honest clinical scope is leave-one-site-out coverage. Report how well the guarantee survives a genuinely new cohort, never just the pooled number.", 9.5),
    ],
    # S6 — synthesis, close the series
    "S6_Synthesis": [
        ("Step back and see the whole architecture. Everything in this series stands on one object: the map m-sub-i equals C times l-sub-i.", 9.0),
        ("On top of that one machinery we built two complementary guarantees, answering two different questions.", 8.0),
        ("E-values, from Vol five, give anytime-valid evidence for a lesion-symptom link. They keep the whole sweep of analyses honest, with no fixed stopping time.", 9.5),
        ("Conformal, from Vol six, gives calibrated prediction sets for one individual outcome. It says nothing about why; it just covers the truth at the stated rate.", 9.5),
        ("They are complementary, not interchangeable. Inference names the link; conformal predicts the next patient. Neither one fixes confounding, and we have been blunt about that.", 9.5),
        ("And the witness is real. With the right tools the ataxia map survived at sixteen thousand nine hundred twenty-six F-W-E voxels where the matched cohort survived at one. The method is sound; the answer depends on N.", 10.5),
        ("Two honest guarantees on one honest object. That is where the series ends, and where a dose-controlled study can begin.", 8.5),
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
