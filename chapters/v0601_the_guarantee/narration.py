"""Narration for v0601_the_guarantee — "The conformal coverage guarantee".

Source: volumes/vol6_conformal/chapters/01_the_guarantee.md
        volumes/vol6_conformal/VOLUME.md

Five narrated scenes. State the conformal coverage promise (K1), name its one
price (exchangeability), establish that it is distribution-free / finite-sample /
model-free, flag the marginal-not-conditional catch, and preview the rank
mechanism that makes it work — setting up split conformal in v0602.

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).
"""

SCENES = {
    # S1 — the promise: a SET that covers the truth at least 1 - alpha
    "S1_Promise": [
        ("Conformal prediction makes one promise, and we had better get it exactly right. Instead of a single number, it hands you a set.", 9.0),
        ("For a binary adverse event, that set is one of three things: just no-event, just event, or the hedge containing both labels.", 9.0),
        ("Here is the guarantee. The probability that the true label Y lands inside the predicted set C-of-X is at least one minus alpha.", 9.5),
        ("Decode the pieces. Y is the true label, no-event or event. C-of-X is the prediction set the procedure outputs for a new patient with features X: a set of candidate labels, not a point.", 9.5),
        ("Alpha is the miscoverage level you choose. Pick alpha equals zero-point-one, and one minus alpha is zero-point-nine: your target is ninety percent coverage.", 9.5),
        ("And the probability is over the whole draw of patients. The promise: at least ninety percent of the time, the truth is inside the set you reported.", 9.0),
        ("You aim for ninety, you get at least ninety. That floor is the headline of this whole volume. Call it K-one.", 8.0),
    ],
    # S2 — the one assumption: exchangeability
    "S2_Exchangeable": [
        ("So what does this cost? Coverage normally costs distributional faith. Conformal charges exactly one assumption, and it is about your data, not your model.", 9.5),
        ("The price is exchangeability. In plain words: if you shuffle the order of your patients, the world looks the same. Order carries no information.", 9.5),
        ("Write each patient as a pair Z-i, the features X-i and the outcome Y-i. You have n calibration patients and one new patient, Z-n-plus-one.", 9.5),
        ("Formally, the patients are exchangeable if their joint distribution is invariant under permutation: any reordering pi gives the same distribution.", 9.5),
        ("The symbol equals-with-a-d on top means has the same distribution as. So every ordering of the n-plus-one patients is equally likely.", 9.0),
        ("This is weaker than the usual i-i-d. Independent-and-identically-distributed data are automatically exchangeable, but you can be exchangeable without being independent.", 9.5),
        ("A shared, unknown cohort effect that nudges every patient the same way is fine. What matters is symmetry, that no patient is singled out by position.", 9.0),
        ("And notice: the new patient must be in the exchangeable bunch too. Same pot, same draw. You do not have to believe your model. You believe this.", 9.0),
    ],
    # S3 — distribution-free, model-free, finite-sample
    "S3_Distribution": [
        ("Now look at what the guarantee does not require, because that is what makes it remarkable. Three words in the promise each buy you something rare.", 9.0),
        ("Any model. You can wrap a logistic regression, a gradient-boosted tree, a neural net, or a coin flip. The coverage floor survives a broken model.", 9.5),
        ("A bad model does not lose coverage. It just makes the sets bigger, hedging more often to keep its word. Model quality buys sharpness, not validity.", 9.5),
        ("Any distribution. No assume-the-residuals-are-Gaussian, no assume-the-link-is-correct. The promise is distribution-free: it holds for any law of the data.", 9.5),
        ("And at the actual n. Not eventually, as n grows large. A finite-sample guarantee. At n equals forty it is exactly as true as at n equals forty-thousand.", 9.5),
        ("Contrast a Wald confidence interval. It needs asymptotic normality, a correctly-specified model, and a large sample. Three distributional I-O-Us.", 9.5),
        ("Conformal pays none of them. It moves the bet: not that the world is Gaussian, only that your patients are interchangeable. That one bet buys the rest.", 9.5),
    ],
    # S4 — marginal, not conditional
    "S4_Marginal": [
        ("Here is where careful readers get burned, so we go slowly. The coverage is marginal, and marginal is a precise word that bites in the clinic.", 9.5),
        ("Marginal means averaged over patients. The probability that Y is in C-of-X, at least one minus alpha, averages over the features X too.", 9.0),
        ("Conditional coverage would be the stronger promise: the probability the truth is covered, given X equals a specific x, is at least one minus alpha, for every x.", 9.5),
        ("That per-patient promise is provably impossible to guarantee distribution-free at finite n. Conformal gives the honest marginal one and does not fake the conditional.", 9.5),
        ("Watch the gap concretely. Say ninety percent of patients are easy and covered ninety-nine percent of the time; ten percent are hard and covered nine percent.", 9.5),
        ("Pooled, that is zero-point-nine times zero-point-nine-nine plus zero-point-one times zero-point-zero-nine, which equals exactly zero-point-nine. A clean ninety percent.", 9.5),
        ("Marginal coverage hits the target. But the hard ten percent, the large-lesion patients you most need to be right about, are covered only nine percent of the time.", 9.5),
        ("The promise is kept on average and broken exactly where it matters. Marginal is not per-patient, and that difference can be a patient's outcome.", 9.0),
    ],
    # S5 — why it works at all: the rank preview
    "S5_Why": [
        ("Why should counting give a guarantee with no distributional faith at all? Here is the mechanism, which the next chapter proves in full.", 9.0),
        ("Hold out a set of calibration patients whose true outcome you already know. Score each one: how strange does the fitted model find that patient?", 9.5),
        ("A natural score is one minus the probability the model put on the true label. A confident, correct call is small; a confident, wrong call is large.", 9.5),
        ("Now the new patient is just one more draw from the same exchangeable pool. Its strangeness has no privileged position among the calibration scores.", 9.5),
        ("So drop the new score into the sorted pile of n-plus-one scores and ask its rank. Under exchangeability, every rank is equally likely: the rank is uniform.", 9.5),
        ("Asking does the new score land in the bottom ninety percent is asking does a uniform rank fall low enough. It does, about ninety percent of the time.", 9.5),
        ("That is the whole engine: a uniform rank, distribution-free, because counting positions never used the values, only their order. This sets up split conformal.", 9.5),
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
