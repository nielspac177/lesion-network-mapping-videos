"""Narration for v0508_test_martingales — "Test martingales, Ville, and optional
stopping (deep dive)".

Source: volumes/vol5_evalues/chapters/03_anytime_validity.md
        volumes/vol5_evalues/chapters/01_what_is_an_evalue.md

Each scene maps to an ordered list of beats. Each beat is (text, seconds): the
text is the subtitle in manim AND the spoken line. The number of
play_beat()/wait_beat() calls in the matching scene MUST equal len(beats).

Numbers are spelled out for the text-to-speech engine.
"""

SCENES = {
    # S1 — wealth as a martingale
    "S1_Wealth": [
        ("Picture a casino. You walk in with exactly one dollar, and the house claims a coin is fair. That fair coin is our null hypothesis: nothing is going on.", 10.0),
        ("You disagree, so you bet. We will track your wealth after t rounds, written W sub t, and you start at W sub zero equals one.", 9.0),
        ("Each round you stake your whole pile, so your wealth just multiplies by that round's factor. Wealth is the running product of the multipliers.", 9.5),
        ("Here is the central object. Under the null, the wealth is a martingale: the expected next value, given everything seen so far, equals the current value.", 10.0),
        ("Decode that. E of W sub t, conditioned on the past, equals W sub t minus one. A fair game. On average, given what you know, your money does not move.", 10.5),
        ("And it is non-negative: you can lose your dollar but never owe. A non-negative martingale starting at one. Remember those three words.", 9.0),
        ("So if your one dollar ever becomes twenty, that is hard to do against a true null. Getting rich is evidence the null was wrong.", 9.0),
    ],
    # S2 — the test martingale
    "S2_TestMartingale": [
        ("A test martingale is exactly this wealth process, built from one fair bet at a time. Let us name every piece.", 8.5),
        ("Index the rounds by s. Write F sub s minus one for the filtration: everything known after round s minus one, the full record of data so far.", 9.5),
        ("Each round you place a bet, the multiplier B sub s, a non-negative number computed from the data. B sub s equals one point three grows your pile thirty percent.", 10.0),
        ("The wealth is the product over s up to t of these bets. That product, starting from one dollar, is the test martingale W sub t.", 9.0),
        ("The one rule that makes a bet fair: under the null, E of B sub s given the past F sub s minus one is at most one. Conditionally break-even.", 10.0),
        ("A concrete bet. Test whether a mean is mu-naught by staking B sub s equals one plus lambda sub s, times the quantity X sub s minus mu-naught.", 10.0),
        ("Decode the bet fraction lambda sub s: how hard you bet this round, chosen from the past. The factor stays non-negative and fair when the data match the null.", 10.0),
        ("Multiply conditionally-fair bets and the product is a non-negative process with expectation at most one at every fixed round. That is the test martingale.", 9.5),
    ],
    # S3 — Ville's inequality, carefully
    "S3_VilleProof": [
        ("Now the theorem that makes peeking safe. Markov bounds the wealth at one fixed moment. Ville bounds it over its entire history at once.", 9.5),
        ("Ville's inequality: for a non-negative martingale with W sub zero equals one, the probability the supremum over all t of W sub t reaches one over alpha is at most alpha.", 11.0),
        ("Decode the supremum: the largest value the wealth ever takes across the whole sequence. Getting twenty-fold rich, ever, has probability at most one twentieth.", 10.0),
        ("Here is the gist. Define the stopping time tau as the first round the wealth crosses one over alpha, or infinity if it never does.", 9.5),
        ("The event that the supremum reaches the line is exactly the event that tau is finite: a supremum is crossed if and only if there is a first crossing.", 9.5),
        ("Optional stopping says the stopped wealth still has expectation at most one. But on the crossing, the wealth is at least one over alpha.", 9.5),
        ("So one is at least one over alpha times the probability tau is at most t. Rearrange: that probability is at most alpha, for every t.", 9.5),
        ("Let t go to infinity and the chance of ever crossing is at most alpha. That is Ville, and non-negativity is the hinge it turns on.", 9.0),
    ],
    # S4 — supermartingales and composite nulls
    "S4_Supermartingale": [
        ("In real problems the null is rarely a single distribution. It is composite: a whole set of distributions, all consistent with nothing going on.", 9.5),
        ("To stay fair against every member of that set, each bet only promises at most one, not exactly one. The inequality, not the equality.", 9.5),
        ("That turns the wealth from a martingale into a supermartingale: the expected next value is no larger than the current value. A game that, on average, cannot grow.", 10.5),
        ("Decode the prefix super: above. The current wealth sits above its expected future. E of W sub t given the past is at most W sub t minus one.", 10.0),
        ("Why composite nulls force this direction? Because a single conservative bet, fair against many distributions at once, can only leave money on the table, never demand more.", 10.5),
        ("Here is the gift. Pull the known W sub t minus one out of the conditional expectation, apply fairness to the bet, and the supermartingale property drops out.", 10.0),
        ("And Ville still holds. The theorem was stated for non-negative supermartingales, so composite nulls cost nothing. The same constant alpha controls the running maximum.", 10.0),
    ],
    # S5 — optional stopping theorem
    "S5_Stopping": [
        ("We leaned on optional stopping inside Ville. Now let us state it as the engine in its own right.", 8.0),
        ("Optional stopping: for a non-negative supermartingale, at any stopping time tau, the expected wealth E of W sub tau is at most one.", 9.5),
        ("Decode a stopping time: a rule for when to quit that uses only the past, never the future. Stop when funding ends, the cohort closes, or the wealth crosses the line.", 10.5),
        ("So the expectation bound that held at every fixed round still holds at a round you choose by watching the data. The bet stays valid when you stop on the evidence.", 10.5),
        ("That is the whole payoff. Reject the null the first time the wealth reaches one over alpha, otherwise keep watching, and stop whenever you like.", 10.0),
        ("Tie it together. Martingale gives the fair game. Ville bounds the running maximum. Optional stopping makes the chosen stop honest.", 9.5),
        ("One picture: anytime-validity. Your type-one error stays at most alpha no matter when or how often you look. Safe peeking, in one theorem.", 9.5),
    ],
    # S6 — why this is the engine
    "S6_Why": [
        ("Step back and see what we have built. One structure underwrites this entire volume on e-values.", 8.0),
        ("Every single bet is an e-value, conditionally: non-negative, with expectation at most one given the past. The atom of evidence is the fair bet.", 9.5),
        ("Multiply those atoms through time and you get the test martingale, a non-negative supermartingale with expectation at most one at every round.", 9.5),
        ("Ville's inequality converts that into a time-uniform guarantee, controlling the running maximum, not just one slice of the trajectory.", 9.0),
        ("And optional stopping lets you cash that guarantee at a moment you choose by watching. Anytime-valid inference, from one clean structure.", 9.5),
        ("So every e-value guarantee downstream, combining cohorts, controlling false discovery, accumulating as patients arrive, is a corollary of martingale plus Ville.", 10.0),
        ("Name it plainly. The martingale and Ville structure is the mathematical engine of anytime-valid inference. Everything else is bookkeeping on top of it.", 9.5),
    ],
}


if __name__ == "__main__":
    for name, beats in SCENES.items():
        total = sum(d for _, d in beats)
        words = sum(len(t.split()) for t, _ in beats)
        print(f"{name:22s} beats={len(beats):2d}  target={total:5.1f}s  "
              f"words={words}  wps={words/total:.2f}")
    grand = sum(d for beats in SCENES.values() for _, d in beats)
    print(f"{'TOTAL':22s} target={grand:5.1f}s ({grand/60:.1f} min)")
