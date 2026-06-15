"""v0501_what_is_an_evalue — "What is an e-value".

Five narrated scenes introducing the testing-by-betting e-value (Shafer, Vovk,
Ramdas, Wang, Grunwald): the realized payout of a one-dollar bet rigged to be
fair against the null. NOT the causal-inference E-value (VanderWeele & Ding).

All equations/numbers come from:
  volumes/vol5_evalues/chapters/01_what_is_an_evalue.md
  volumes/vol5_evalues/VOLUME.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0501_what_is_an_evalue ./render.sh \
      chapters/v0501_what_is_an_evalue/scenes.py -q ql \
      S1_Betting S2_Definition S3_Markov S4_LR S5_Reading
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — evidence as betting: the casino picture
# ----------------------------------------------------------------------
class S1_Betting(NarratedScene):
    scene_key = "S1_Betting"

    def construct(self):
        self.header("Evidence as betting")

        # set the table
        null = VGroup(
            Text("the null hypothesis  H_0", font_size=30, color=WHITE),
            Text("\"nothing is going on\"", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.5)
        self.play_beat(FadeIn(null[0]), FadeIn(null[1]))                   # beat 1

        # stake $1, collect E
        stake = MathTex(r"\text{stake } \$1", r"\ \longrightarrow\ ",
                        r"\text{payout } ", "E").scale(1.2).shift(DOWN * 0.3)
        stake[3].set_color(VAR)
        self.play_beat(Write(stake), null.animate.set_opacity(0.5))        # beat 2

        # three payouts
        cases = VGroup(
            MathTex("E", "=", "3", r"\ \Rightarrow\ \text{tripled}"),
            MathTex("E", "=", "0.2", r"\ \Rightarrow\ \text{lost most}"),
            MathTex("E", "=", "0", r"\ \Rightarrow\ \text{wiped out}"),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(stake, DOWN, buff=0.6)
        for c in cases:
            c[0].set_color(VAR)
        cases[2][2].set_color(BAD)
        self.play_beat(FadeIn(cases, lag_ratio=0.3))                       # beat 3

        # rule 1
        self.play(FadeOut(VGroup(null, stake, cases)), run_time=0.5)
        r1 = VGroup(
            Text("Rule 1   never owe money", font_size=28, color=BACK),
            MathTex("E", r"\geq", "0").scale(1.4),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.1)
        r1[1][0].set_color(VAR); r1[1][2].set_color(EIG)
        self.play_beat(FadeIn(r1[0]), Write(r1[1]))                        # beat 4

        # rule 2
        r2 = VGroup(
            Text("Rule 2   no profit under the null on average", font_size=28, color=BACK),
            MathTex(r"\mathbb{E}_{H_0}", r"\!\left[", "E", r"\right]", r"\leq", "1").scale(1.4),
        ).arrange(DOWN, buff=0.35).next_to(r1, DOWN, buff=0.7)
        r2[1][2].set_color(VAR); r2[1][5].set_color(EIG)
        self.play_beat(FadeIn(r2[0]), Write(r2[1]))                        # beat 5

        # decode the expectation
        self.play(FadeOut(r1), r2.animate.shift(UP * 1.3), run_time=0.5)
        brace = Brace(r2[1][0], DOWN, color=DIM)
        elab = Text("average payout if the null were the truth\n(the long-run average over the null)",
                    font_size=23, color=DIM, line_spacing=0.8).next_to(brace, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace), FadeIn(elab))                # beat 6

        # flip the logic: E=40
        self.play(FadeOut(VGroup(r2, brace, elab)), run_time=0.5)
        flip = MathTex("E", "=", "40").scale(1.6).shift(UP * 1.0)
        flip[0].set_color(VAR); flip[2].set_color(RES)
        flip_cap = Text("rigged fair  →  this should not happen under the null",
                        font_size=25, color=WHITE).next_to(flip, DOWN, buff=0.4)
        self.play_beat(Write(flip), FadeIn(flip_cap))                      # beat 7

        moral = Text("big payout  =  evidence against the null\nsize of payout  =  strength of evidence",
                     font_size=27, color=RES, line_spacing=0.9).next_to(flip_cap, DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 8


# ----------------------------------------------------------------------
# Scene 2 — the formal definition
# ----------------------------------------------------------------------
class S2_Definition(NarratedScene):
    scene_key = "S2_Definition"

    def construct(self):
        self.header("The formal definition")

        intro = Text("every symbol is a piece of the bet",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # the null as a set
        nullset = VGroup(
            MathTex("H_0", r"=", r"\{\,P\,\}").scale(1.3),
            Text("a SET of distributions: every P with nothing going on",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.3)
        nullset[0][0].set_color(WHITE); nullset[0][2].set_color(BACK)
        self.play_beat(Write(nullset[0]), FadeIn(nullset[1]))             # beat 2

        # data X and payout E(X)
        data = MathTex("E", "=", "E(", "X", ")").scale(1.3).next_to(nullset, DOWN, buff=0.6)
        data[0].set_color(VAR); data[3].set_color(EIG)
        dbrace = Brace(data[3], DOWN, color=EIG)
        dlab = Text("X = the data;   E(X) = the payout, a function of it",
                    font_size=23, color=DIM).next_to(dbrace, DOWN, buff=0.2)
        self.play_beat(Write(data), GrowFromCenter(dbrace), FadeIn(dlab))  # beat 3

        # the definition, line by line
        self.play(FadeOut(VGroup(intro, nullset, data, dbrace, dlab)), run_time=0.5)
        title = Text("An e-variable for H_0:", font_size=28, color=RES).shift(UP * 2.2)
        self.play(FadeIn(title), run_time=0.4)

        line1 = MathTex("E", r"=", "E(", "X", ")", r"\geq", "0").scale(1.3).shift(UP * 0.9)
        line1[0].set_color(VAR); line1[3].set_color(EIG); line1[6].set_color(EIG)
        b1 = Brace(line1, DOWN, color=BACK)
        l1 = Text("Rule 1: never owe money", font_size=24, color=BACK).next_to(b1, DOWN, buff=0.15)
        self.play_beat(Write(line1), GrowFromCenter(b1), FadeIn(l1))       # beat 4

        line2 = MathTex(r"\mathbb{E}_{P}", r"\!\left[", "E", r"\right]", r"\leq", "1",
                        r"\quad \text{for every } P \in H_0").scale(1.1)
        line2.next_to(l1, DOWN, buff=0.7)
        line2[2].set_color(VAR); line2[5].set_color(EIG)
        b2 = Brace(line2, DOWN, color=BACK)
        l2 = Text("Rule 2: no profit under EVERY null distribution",
                  font_size=24, color=BACK).next_to(b2, DOWN, buff=0.15)
        self.play_beat(Write(line2), GrowFromCenter(b2), FadeIn(l2))       # beat 5

        # <= 1 not = 1
        self.play(FadeOut(VGroup(title, line1, b1, l1, b2, l2)),
                  line2.animate.to_edge(UP, buff=1.2), run_time=0.5)
        cons = VGroup(
            Text("≤ 1, not = 1", font_size=30, color=RES),
            Text("a conservative bet that leaves money on the table is still valid",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.2)
        self.play_beat(FadeIn(cons[0]), FadeIn(cons[1]))                  # beat 6

        # binds only under the null
        bind = VGroup(
            Text("the constraint binds ONLY under the null", font_size=26, color=WHITE),
            MathTex(r"\text{under the alternative:}\quad", r"\mathbb{E}[E] > 1").scale(1.0),
        ).arrange(DOWN, buff=0.3).next_to(cons, DOWN, buff=0.6)
        bind[1][1].set_color(RES)
        self.play_beat(FadeIn(bind[0]), Write(bind[1]))                   # beat 7

        # e-value = realized value, big E = surprising
        self.play(FadeOut(VGroup(line2, cons, bind)), run_time=0.5)
        final = VGroup(
            Text("a realized value of E  =  an e-value", font_size=28, color=VAR),
            Text("big E  =  surprising under the null  =  evidence against it",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.4)
        self.play_beat(FadeIn(final, lag_ratio=0.3))                     # beat 8


# ----------------------------------------------------------------------
# Scene 3 — Markov gives validity
# ----------------------------------------------------------------------
class S3_Markov(NarratedScene):
    scene_key = "S3_Markov"

    def construct(self):
        self.header("Markov gives validity")

        intro = Text("a non-negative quantity with a small average\ncannot be large very often",
                     font_size=28, color=DIM, line_spacing=0.85).shift(UP * 2.3)
        self.play_beat(FadeIn(intro))                                     # beat 1

        name = Text("Markov's inequality, one line",
                    font_size=28, color=RES).next_to(intro, DOWN, buff=0.5)
        self.play_beat(FadeIn(name), intro.animate.set_opacity(0.5))      # beat 2

        # define c and the indicator
        self.play(FadeOut(VGroup(intro, name)), run_time=0.4)
        defs = VGroup(
            MathTex("c", r"> 0", r"\quad\text{the threshold}").scale(1.0),
            MathTex(r"\mathbf{1}[E \geq c]", r"=", r"\begin{cases}1 & E\geq c\\ 0 & E<c\end{cases}").scale(0.9),
        ).arrange(DOWN, buff=0.5).shift(UP * 1.4)
        defs[0][0].set_color(EIG)
        defs[1][0].set_color(BACK)
        self.play_beat(Write(defs[0]), Write(defs[1]))                    # beat 3

        # step 1: flooring
        self.play(defs.animate.scale(0.7).to_edge(UP, buff=1.0), run_time=0.5)
        s1 = MathTex("E", r"\;\geq\;", "c", r"\cdot", r"\mathbf{1}[E \geq c]").scale(1.2)
        s1.shift(UP * 0.6)
        s1[0].set_color(VAR); s1[2].set_color(EIG); s1[4].set_color(BACK)
        s1cap = Text("Step 1  true outcome by outcome  (uses E ≥ 0)",
                     font_size=23, color=DIM).next_to(s1, DOWN, buff=0.25)
        self.play_beat(Write(s1), FadeIn(s1cap))                          # beat 4

        # step 2: expectations
        s2 = MathTex(r"\mathbb{E}_{H_0}[E]", r"\;\geq\;", "c", r"\cdot",
                     r"\Pr_{H_0}(E \geq c)").scale(1.0).next_to(s1cap, DOWN, buff=0.5)
        s2[0].set_color(VAR); s2[2].set_color(EIG); s2[4].set_color(BACK)
        self.play_beat(Write(s2))                                         # beat 5

        # step 3: divide by c, use <=1
        s3 = MathTex(r"\Pr_{H_0}(E \geq c)", r"\;\leq\;",
                     r"\frac{\mathbb{E}_{H_0}[E]}{c}", r"\;\leq\;",
                     r"\frac{1}{c}").scale(1.0).next_to(s2, DOWN, buff=0.5)
        s3[0].set_color(BACK); s3[4].set_color(RES)
        self.play_beat(Write(s3))                                         # beat 6

        # set c = 1/alpha
        self.play(FadeOut(VGroup(defs, s1, s1cap, s2)),
                  s3.animate.to_edge(UP, buff=1.1), run_time=0.5)
        alpha = MathTex(r"c = \tfrac{1}{\alpha}", r"\ \Rightarrow\ ",
                        r"\Pr_{H_0}\!\left(E \geq \tfrac{1}{\alpha}\right)",
                        r"\;\leq\;", r"\alpha").scale(1.1).shift(UP * 0.3)
        alpha[2].set_color(BACK); alpha[4].set_color(RES)
        self.play_beat(Write(alpha))                                      # beat 7

        # the headline
        head = VGroup(
            Text("reject when E ≥ 1/α  =  a valid level-α test",
                 font_size=27, color=RES),
            Text("a 5% test: reject when your dollar grew to $20",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.3).next_to(alpha, DOWN, buff=0.7)
        box = SurroundingRectangle(head[0], color=RES, buff=0.2)
        self.play_beat(FadeIn(head[0]), Create(box), FadeIn(head[1]))     # beat 8


# ----------------------------------------------------------------------
# Scene 4 — the likelihood-ratio e-value
# ----------------------------------------------------------------------
class S4_LR(NarratedScene):
    scene_key = "S4_LR"

    def construct(self):
        self.header("The likelihood-ratio e-value")

        intro = Text("the cleanest source of e-variables:\na likelihood ratio",
                     font_size=28, color=DIM, line_spacing=0.85).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # p and q
        densities = VGroup(
            MathTex("p", r"\ :\ \text{null density}").scale(1.05),
            MathTex("q", r"\ :\ \text{rival / alternative density}").scale(1.05),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).shift(UP * 1.0)
        densities[0][0].set_color(WHITE)
        densities[1][0].set_color(VAR)
        self.play_beat(Write(densities[0]), Write(densities[1]))          # beat 2

        # the bet E = q/p
        eq = MathTex("E", "=", r"\frac{q(X)}{p(X)}").scale(1.5).shift(DOWN * 0.6)
        eq[0].set_color(VAR)
        eq[2][0:2].set_color(VAR)       # q( in numerator
        self.play_beat(Write(eq), densities.animate.scale(0.8).to_edge(UP, buff=1.0))  # beat 3

        # read the ratio
        read = VGroup(
            Text("data look like q  →  ratio big  →  cash in", font_size=24, color=RES),
            Text("data look like p  →  ratio small  →  lose stake", font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.25).next_to(eq, DOWN, buff=0.6)
        self.play_beat(FadeIn(read[0]), FadeIn(read[1]))                  # beat 4

        # why fair: average = 1
        self.play(FadeOut(VGroup(densities, read)),
                  eq.animate.scale(0.7).to_edge(UP, buff=1.1), run_time=0.5)
        claim = Text("under the null, the average of q/p is exactly 1",
                     font_size=27, color=WHITE).shift(UP * 1.1)
        self.play_beat(FadeIn(claim))                                     # beat 5

        # the integral with cancellation
        integ = MathTex(r"\mathbb{E}_p\!\left[\frac{q(X)}{p(X)}\right]", "=",
                        r"\int \frac{q(x)}{p(x)}\, p(x)\, dx").scale(1.0)
        integ.next_to(claim, DOWN, buff=0.6)
        cancel = Text("the p in the denominator cancels the p weight",
                      font_size=23, color=BAD).next_to(integ, DOWN, buff=0.3)
        self.play_beat(Write(integ), FadeIn(cancel))                     # beat 6

        # = integral q = 1
        result = MathTex("=", r"\int q(x)\, dx", "=", "1").scale(1.2).next_to(cancel, DOWN, buff=0.5)
        result[1].set_color(VAR); result[3].set_color(RES)
        rcap = Text("q integrates to 1: it is a probability density. No slack.",
                    font_size=23, color=DIM).next_to(result, DOWN, buff=0.25)
        self.play_beat(Write(result), FadeIn(rcap))                      # beat 7

        # moral
        self.play(FadeOut(VGroup(claim, integ, cancel, result, rcap)), run_time=0.5)
        moral = Text("e-values are likelihood ratios in disguise",
                     font_size=32, color=RES).shift(UP * 0.2)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                    # beat 8


# ----------------------------------------------------------------------
# Scene 5 — reading an e-value
# ----------------------------------------------------------------------
class S5_Reading(NarratedScene):
    scene_key = "S5_Reading"

    def construct(self):
        self.header("Reading an e-value")

        # E = 20
        big = MathTex("E", "=", "20").scale(1.8).shift(UP * 1.4)
        big[0].set_color(VAR); big[2].set_color(RES)
        cap = Text("your dollar became twenty dollars",
                   font_size=26, color=WHITE).next_to(big, DOWN, buff=0.4)
        self.play_beat(Write(big), FadeIn(cap))                          # beat 1

        strong = Text("rigged fair  →  no business making $20 under the null\n→  strong evidence",
                      font_size=25, color=RES, line_spacing=0.85).next_to(cap, DOWN, buff=0.6)
        self.play_beat(FadeIn(strong, shift=UP * 0.2))                   # beat 2

        # the scale
        self.play(FadeOut(VGroup(big, cap, strong)), run_time=0.5)
        scale = VGroup(
            MathTex("E", r"\approx", "1", r"\ :\ \text{learned nothing}"),
            MathTex("E", "=", "20", r"\ :\ \text{the null is in trouble}"),
            MathTex("E", "=", "40", r"\ :\ \text{in serious trouble}"),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).shift(UP * 0.6)
        for s in scale:
            s[0].set_color(VAR)
        scale[0][2].set_color(DIM)
        scale[1][2].set_color(RES)
        scale[2][2].set_color(RES)
        self.play_beat(FadeIn(scale, lag_ratio=0.3))                     # beat 3

        contrast = Text("the payout IS the evidence — one number, read off directly\n(a p-value never quite gives you this)",
                        font_size=24, color=WHITE, line_spacing=0.85).next_to(scale, DOWN, buff=0.6)
        self.play_beat(FadeIn(contrast))                                 # beat 4

        # accrued evidence you can multiply
        self.play(FadeOut(VGroup(scale, contrast)), run_time=0.5)
        mult = Text("unlike a p-value, an e-value is ACCRUED evidence\nyou can keep multiplying",
                    font_size=27, color=RES, line_spacing=0.85).shift(UP * 1.3)
        self.play_beat(FadeIn(mult, shift=UP * 0.2))                     # beat 5

        # compounding coin
        compound = MathTex(r"1.5^{10}", r"\approx", "57.7").scale(1.3).next_to(mult, DOWN, buff=0.6)
        compound[0].set_color(VAR); compound[2].set_color(RES)
        ccap = Text("ten biased-coin flips: multiply each ratio onto the last",
                    font_size=23, color=DIM).next_to(compound, DOWN, buff=0.25)
        self.play_beat(Write(compound), FadeIn(ccap))                    # beat 6

        # optional stopping
        stop = Text("peek whenever you like  •  stop when evidence is strong\nno penalty for looking",
                    font_size=25, color=WHITE, line_spacing=0.85).next_to(ccap, DOWN, buff=0.5)
        self.play_beat(FadeIn(stop, shift=UP * 0.2))                     # beat 7

        # sets up next chapter
        self.play(FadeOut(VGroup(mult, compound, ccap, stop)), run_time=0.5)
        nxt = VGroup(
            Text("optional stopping", font_size=30, color=RES),
            Text("where the real power lives — the next chapter", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(nxt, lag_ratio=0.3))                       # beat 8
