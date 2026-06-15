"""v0506_universal_inference — "Universal inference".

Five narrated scenes on the split likelihood ratio (universal inference; result
E6, Wasserman, Ramdas and Balakrishnan, 2020). When classical asymptotics fail
(mixtures, boundary nulls), split the data, fit the alternative on one half, and
score the split likelihood ratio e-value on the other. It is a valid e-value with
NO regularity conditions; the price is sample-splitting.

All equations/numbers are quoted from:
  volumes/vol5_evalues/chapters/06_universal_inference.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0506_universal_inference ./render.sh \
      chapters/v0506_universal_inference/scenes.py -q ql \
      S1_Hard S2_SplitLR S3_Valid S4_Price S5_Use
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — When the null is hard
# ----------------------------------------------------------------------
class S1_Hard(NarratedScene):
    scene_key = "S1_Hard"

    def construct(self):
        title = Text("When the null is hard", font_size=44, color=WHITE)
        sub = Text("where no clean test statistic exists",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))            # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # the irregular nulls: mixtures, boundary, constrained
        problem = VGroup(
            Text("null = a model with parameters to estimate", font_size=27, color=WHITE),
            Text("mixtures   •   variance pinned at the boundary   •   constrained space",
                 font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.4)
        self.play_beat(FadeIn(problem[0]), FadeIn(problem[1], shift=UP * 0.2))  # beat 2

        # the classical statistic: best free over best null
        lam = MathTex(r"\Lambda", "=",
                      r"\frac{\sup_{\theta\in\Theta} L(\theta;\,\text{data})}"
                      r"{\sup_{\theta\in\Theta_0} L(\theta;\,\text{data})}")\
            .scale(1.15).next_to(problem, DOWN, buff=0.7)
        lam[0].set_color(VAR)
        bf = Text("best free fit", font_size=20, color=DIM).next_to(lam, RIGHT, buff=0.6).shift(UP * 0.35)
        bn = Text("best null-allowed fit", font_size=20, color=DIM).next_to(lam, RIGHT, buff=0.6).shift(DOWN * 0.35)
        # decode the symbols: L is the likelihood; Theta_0 is the null-allowed set
        ldef = MathTex(r"L(\theta;S)=\prod_{i\in S} f_\theta(X_i)",
                       r"\quad\theta\in\Theta_0:\ \text{null-allowed values}")\
            .scale(0.6).set_color(DIM).next_to(lam, DOWN, buff=0.45)
        self.play_beat(Write(lam), FadeIn(bf), FadeIn(bn), FadeIn(ldef))     # beat 3

        # Wilks
        self.play(FadeOut(VGroup(problem, bf, bn, ldef)),
                  lam.animate.scale(0.8).to_edge(UP, buff=1.1), run_time=0.5)
        wilks = MathTex(r"2\log\Lambda", r"\ \approx\ ", r"\chi^2",
                        r"\quad\text{under } H_0").scale(1.1).shift(UP * 0.5)
        wilks[0].set_color(VAR); wilks[2].set_color(EIG)
        wcap = Text("Wilks' theorem  →  a p-value", font_size=24, color=DIM)\
            .next_to(wilks, DOWN, buff=0.3)
        self.play_beat(Write(wilks), FadeIn(wcap))                          # beat 4

        # the assumptions
        assume = VGroup(
            Text("but only IF:", font_size=24, color=RES),
            Text("the likelihood is smooth in theta", font_size=23, color=WHITE),
            Text("the true theta is not on the edge of the allowed region", font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(wcap, DOWN, buff=0.5)
        self.play_beat(FadeIn(assume, lag_ratio=0.3))                       # beat 5

        # break it -> wrong reference
        self.play(FadeOut(VGroup(wilks, wcap, assume)), run_time=0.5)
        broke = VGroup(
            Text("break any of those  →  chi-square is the WRONG reference",
                 font_size=26, color=BAD),
            Text("the table still prints a number — just the wrong one",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.4)
        self.play_beat(FadeIn(broke[0]), FadeIn(broke[1], shift=UP * 0.2))  # beat 6

        engine = Text("a conversion table printed for one engine;\nmixtures and boundary nulls are different engines",
                      font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(broke, DOWN, buff=0.6)
        self.play_beat(FadeIn(engine, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 2 — The split likelihood ratio
# ----------------------------------------------------------------------
class S2_SplitLR(NarratedScene):
    scene_key = "S2_SplitLR"

    def construct(self):
        self.header("The split likelihood ratio  (E6)")

        # split into two halves
        full = RoundedRectangle(width=6.0, height=0.8, corner_radius=0.1,
                                stroke_color=DIM, stroke_width=2,
                                fill_color=DIM, fill_opacity=0.1).shift(UP * 2.2)
        full_lab = Text("full sample", font_size=22, color=DIM).next_to(full, UP, buff=0.15)
        self.play_beat(FadeIn(full), FadeIn(full_lab))                      # beat 1

        d1 = self._chip("D_1   (fit)", VAR).shift(UP * 0.9 + LEFT * 2.0)
        d0 = self._chip("D_0   (score)", BACK).shift(UP * 0.9 + RIGHT * 2.0)
        a1 = Arrow(full.get_bottom() + LEFT * 1.5, d1.get_top(), color=DIM, buff=0.1)
        a0 = Arrow(full.get_bottom() + RIGHT * 1.5, d0.get_top(), color=DIM, buff=0.1)
        fit = Text("fit any estimator on D-one  →  theta-hat-one",
                   font_size=23, color=VAR).next_to(d1, DOWN, buff=0.4).shift(RIGHT * 2.0)
        self.play_beat(GrowArrow(a1), GrowArrow(a0), FadeIn(d1), FadeIn(d0),
                       FadeIn(fit))                                         # beat 2

        # freeze it
        freeze = MathTex(r"\hat\theta_1", r"\ \text{FROZEN: a fixed number, no peek at } D_0")\
            .scale(0.85).next_to(fit, DOWN, buff=0.4)
        freeze[0].set_color(VAR)
        self.play_beat(Write(freeze))                                      # beat 3

        # the ratio U
        self.play(FadeOut(VGroup(full, full_lab, a1, a0, fit, freeze)),
                  d1.animate.scale(0.85).shift(UP * 0.3),
                  d0.animate.scale(0.85).shift(UP * 0.3), run_time=0.5)
        U = MathTex("U", "=",
                    r"\frac{L(\hat\theta_1;\,D_0)}{\sup_{\theta\in\Theta_0} L(\theta;\,D_0)}")\
            .scale(1.25).shift(DOWN * 0.3)
        U[0].set_color(RES); U[2].set_color(WHITE)
        # numerator brace
        num_b = Brace(U[2], UP, color=VAR)
        num_l = Text("frozen alternative, scored on the held-out half",
                     font_size=21, color=VAR).next_to(num_b, UP, buff=0.15)
        self.play_beat(Write(U), GrowFromCenter(num_b), FadeIn(num_l))      # beat 4

        # denominator brace
        self.play(FadeOut(VGroup(num_b, num_l)), run_time=0.35)
        den_b = Brace(U[2], DOWN, color=BACK)
        den_l = Text("best the null can do, optimizing freely on the same half",
                     font_size=21, color=BACK).next_to(den_b, DOWN, buff=0.15)
        self.play_beat(GrowFromCenter(den_b), FadeIn(den_l))               # beat 5

        # the asymmetry
        self.play(FadeOut(VGroup(den_b, den_l)), run_time=0.35)
        asym = VGroup(
            Text("alternative: FROZEN, cross-fitted", font_size=24, color=VAR),
            Text("null: free to OPTIMIZE on the scoring half", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.9)
        self.play_beat(FadeIn(asym[0]), FadeIn(asym[1], shift=UP * 0.2))    # beat 6

        # betting picture
        self.play(FadeOut(asym), run_time=0.35)
        bet = MathTex(r"\text{stake }\$1:\ ", r"\hat\theta_1",
                      r"\ \text{beats any null on fresh } D_0\ \Rightarrow\ ",
                      "U", r"\ \text{is the payout}")\
            .scale(0.78).to_edge(DOWN, buff=1.0)
        bet[1].set_color(VAR); bet[3].set_color(RES)
        self.play_beat(Write(bet))                                         # beat 7

        # rejection rule
        rule = MathTex(r"\text{reject } H_0", r"\iff", "U", r"\geq", r"\tfrac{1}{\alpha}")\
            .scale(1.1).next_to(U, UP, buff=0.7)
        rule[2].set_color(RES); rule[4].set_color(EIG)
        self.play_beat(Write(rule))                                        # beat 8

    def _chip(self, label, color):
        box = RoundedRectangle(width=2.6, height=0.7, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=21, color=color).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 3 — Always a valid e-value (the proof)
# ----------------------------------------------------------------------
class S3_Valid(NarratedScene):
    scene_key = "S3_Valid"

    def construct(self):
        self.header("Always a valid e-value  —  no regularity conditions")

        # the claim
        claim = MathTex(r"\theta^\star\in\Theta_0", r"\ \Longrightarrow\ ",
                        r"\mathbb{E}[U]", r"\leq", "1").scale(1.25).shift(UP * 2.2)
        claim[0].set_color(BACK); claim[2].set_color(RES); claim[4].set_color(EIG)
        cl = Text("so U is an e-value — no chi-square, no large-n limit",
                  font_size=22, color=DIM).next_to(claim, DOWN, buff=0.25)
        self.play_beat(Write(claim), FadeIn(cl))                           # beat 1

        # Step 1 — condition on D1
        self.play(FadeOut(cl), claim.animate.scale(0.7).to_edge(UP, buff=1.0),
                  run_time=0.5)
        s1 = VGroup(
            Text("Step 1.  condition on D-one, freeze the alternative",
                 font_size=24, color=WHITE),
            MathTex(r"\hat\theta_1 \to \theta_1\ \text{(a constant)}").scale(0.9).set_color(VAR),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.7)
        self.play_beat(FadeIn(s1[0]), Write(s1[1]))                        # beat 2

        # independence
        indep = MathTex(r"D_0", r"\perp", r"D_1",
                        r"\quad\Rightarrow\quad D_0\ \text{is a fresh i.i.d. sample}")\
            .scale(0.9).next_to(s1, DOWN, buff=0.5)
        indep[0].set_color(BACK); indep[2].set_color(VAR)
        self.play_beat(Write(indep))                                       # beat 3

        # Step 2 — sup dominates the truth
        self.play(FadeOut(VGroup(s1, indep)), run_time=0.45)
        s2 = VGroup(
            Text("Step 2.  the truth lives in the null set", font_size=24, color=WHITE),
            MathTex(r"\sup_{\theta\in\Theta_0} L(\theta;D_0)",
                    r"\ \geq\ ", r"L(\theta^\star;D_0)").scale(0.95),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.7)
        s2[1][2].set_color(BACK)
        self.play_beat(FadeIn(s2[0]), Write(s2[1]))                        # beat 4

        # bound U
        bound = MathTex("U", r"\ \leq\ ",
                        r"\frac{L(\theta_1;D_0)}{L(\theta^\star;D_0)}")\
            .scale(1.05).next_to(s2, DOWN, buff=0.5)
        bound[0].set_color(RES); bound[2].set_color(WHITE)
        bcap = Text("a plain ratio of two fixed parameters: alt on top, truth on bottom",
                    font_size=21, color=DIM).next_to(bound, DOWN, buff=0.25)
        self.play_beat(Write(bound), FadeIn(bcap))                         # beat 5

        # Step 3 — cancellation
        self.play(FadeOut(VGroup(s2, bound, bcap)), run_time=0.45)
        s3 = MathTex(r"\mathbb{E}\!\left[\frac{L(\theta_1;D_0)}{L(\theta^\star;D_0)}"
                     r"\,\Big|\,D_1\right]",
                     "=", r"\int \prod_{i} f_{\theta_1}(x_i)\,dx", r"\ \leq\ ", "1")\
            .scale(0.95).shift(UP * 0.5)
        s3[4].set_color(EIG)
        s3cap = Text("the true density cancels the sampling density;\nwhat is left integrates to at most one",
                     font_size=22, color=DIM, line_spacing=0.8).next_to(s3, DOWN, buff=0.4)
        self.play_beat(Write(s3), FadeIn(s3cap))                           # beat 6

        # Step 4 — tower rule
        self.play(FadeOut(VGroup(s3, s3cap)), run_time=0.45)
        tower = MathTex(r"\mathbb{E}[U]", "=",
                        r"\mathbb{E}\big[\mathbb{E}[U\mid D_1]\big]",
                        r"\ \leq\ ", r"\mathbb{E}[1]", "=", "1")\
            .scale(1.0).shift(UP * 0.4)
        tower[0].set_color(RES); tower[6].set_color(EIG)
        tcap = Text("Step 4.  tower rule — average over D-one. Done.",
                    font_size=24, color=WHITE).next_to(tower, DOWN, buff=0.35)
        self.play_beat(Write(tower), FadeIn(tcap))                         # beat 7

        # the moral: universal
        self.play(FadeOut(VGroup(tower, tcap)), run_time=0.45)
        moral = VGroup(
            Text("never used:", font_size=24, color=DIM),
            Text("no smoothness  •  no interior point  •  no central limit theorem",
                 font_size=24, color=WHITE),
            Text("→  UNIVERSAL: any likelihood model you can write down",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 8


# ----------------------------------------------------------------------
# Scene 4 — The price
# ----------------------------------------------------------------------
class S4_Price(NarratedScene):
    scene_key = "S4_Price"

    def construct(self):
        self.header("The price  —  sample-splitting")

        head = Text("nothing is free: the data is spent twice over",
                    font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(head))                                       # beat 1

        # half fits, half scores
        left = self._half("D_1  fits the model", "never votes on the evidence", VAR)\
            .shift(LEFT * 3.2 + UP * 0.4)
        right = self._half("D_0  scores the evidence", "never improved the fit", BACK)\
            .shift(RIGHT * 3.2 + UP * 0.4)
        self.play_beat(FadeIn(left, shift=UP * 0.2),
                       FadeIn(right, shift=UP * 0.2))                       # beat 2

        # classical uses all
        cls = Text("the classical test uses every patient for BOTH jobs",
                   font_size=25, color=WHITE).to_edge(DOWN, buff=1.4)
        n = Text("with N in the dozens, losing half can sink any honest test",
                 font_size=23, color=BAD).next_to(cls, DOWN, buff=0.25)
        self.play_beat(FadeIn(cls), FadeIn(n))                             # beat 3

        # valid but underpowered
        self.play(FadeOut(VGroup(head, left, right, cls, n)), run_time=0.5)
        trade = VGroup(
            Text("the honest trade:", font_size=26, color=RES),
            Text("VALID with no regularity   vs   some POWER LOST", font_size=26, color=WHITE),
            Text("at small N: valid but underpowered to the point of uselessness",
                 font_size=23, color=BAD),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.7)
        self.play_beat(FadeIn(trade, lag_ratio=0.3))                       # beat 4

        slogan = Text("Validity is free.   Power you have to earn.",
                      font_size=30, color=RES).next_to(trade, DOWN, buff=0.6)
        self.play_beat(Write(slogan))                                      # beat 5

        # mitigation: cross-fit average
        self.play(FadeOut(VGroup(trade, slogan)), run_time=0.45)
        cf = VGroup(
            Text("some relief: run the split BOTH ways, then average",
                 font_size=25, color=WHITE),
            MathTex(r"\bar U", "=", r"\tfrac12\,(U_a + U_b)").scale(1.1),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.6)
        cf[1][0].set_color(RES)
        self.play_beat(FadeIn(cf[0]), Write(cf[1]))                        # beat 6

        warn = VGroup(
            Text("the splits share a partition  →  they are DEPENDENT", font_size=24, color=BAD),
            Text("average, NEVER multiply — a product can blow past one", font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.25).next_to(cf, DOWN, buff=0.6)
        self.play_beat(FadeIn(warn[0]), FadeIn(warn[1], shift=UP * 0.2))    # beat 7

    def _half(self, top, bottom, color):
        box = RoundedRectangle(width=4.6, height=1.5, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.1)
        t = Text(top, font_size=22, color=color)
        b = Text(bottom, font_size=20, color=DIM)
        VGroup(t, b).arrange(DOWN, buff=0.2).move_to(box)
        return VGroup(box, t, b)


# ----------------------------------------------------------------------
# Scene 5 — Why it is remarkable
# ----------------------------------------------------------------------
class S5_Use(NarratedScene):
    scene_key = "S5_Use"

    def construct(self):
        self.header("Why it is remarkable")

        head = Text("one recipe  →  a valid test where nothing else works",
                    font_size=29, color=RES).shift(UP * 2.5)
        self.play_beat(FadeIn(head))                                       # beat 1

        # mixtures
        m = VGroup(
            Text("✓ mixtures", font_size=25, color=BACK),
            MathTex(r"k\ \text{vs}\ k+1\ \text{components: extra one unidentified, Wilks fails}")
            .scale(0.7).set_color(WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 1.3)
        self.play_beat(FadeIn(m, shift=UP * 0.2))                          # beat 2

        # boundary / constrained
        b = VGroup(
            Text("✓ boundary / constrained nulls", font_size=25, color=BACK),
            Text("variance pinned at zero  •  ordered parameter  •  one-sided edge",
                 font_size=21, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(m, DOWN, buff=0.5)
        self.play_beat(FadeIn(b, shift=UP * 0.2))                          # beat 3

        # no provable regularity
        r = VGroup(
            Text("✓ likelihood you can compute but cannot prove regular",
                 font_size=25, color=BACK),
            Text("still a valid e-value, exact at finite n", font_size=21, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(b, DOWN, buff=0.5)
        self.play_beat(FadeIn(r, shift=UP * 0.2))                          # beat 4

        # drops into the machinery
        self.play(FadeOut(VGroup(m, b, r)), run_time=0.5)
        wire = VGroup(
            Text("the one e-value drops into the machinery we built:",
                 font_size=25, color=WHITE),
            Text("one input to e-BH across a sweep  (Ch. 4)", font_size=23, color=VAR),
            Text("one summand accumulating across cohorts  (Ch. 5)", font_size=23, color=VAR),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.9)
        self.play_beat(FadeIn(wire, lag_ratio=0.3))                        # beat 5

        # but: irregularity, not confounding
        self.play(FadeOut(wire), run_time=0.4)
        caveat = VGroup(
            Text("it fixes IRREGULARITY, not CONFOUNDING", font_size=26, color=BAD),
            Text("if lesion size confounds the effect, U faithfully measures\nevidence against the WRONG null",
                 font_size=23, color=WHITE, line_spacing=0.8),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.8)
        self.play_beat(FadeIn(caveat[0]), FadeIn(caveat[1], shift=UP * 0.2))  # beat 6

        sep = VGroup(
            Text("validity of the bet  ≠  validity of the question", font_size=26, color=RES),
            Text("universal inference guarantees the first, and only the first",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(caveat, DOWN, buff=0.6)
        self.play_beat(FadeIn(sep[0]), FadeIn(sep[1], shift=UP * 0.2))      # beat 7

        # closing
        self.play(FadeOut(VGroup(caveat, sep, head)), run_time=0.5)
        close = VGroup(
            Text("For messy, irregular, real-world models,", font_size=30, color=WHITE),
            Text("one recipe extends honest inference", font_size=30, color=WHITE),
            Text("to exactly the cases where the textbook table lies.",
                 font_size=30, color=RES),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(FadeIn(close, lag_ratio=0.3))                       # beat 8
