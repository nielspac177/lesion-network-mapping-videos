"""v0602_split_conformal — "Split conformal, and why it works exactly".

Five narrated scenes building the split-conformal procedure and proving its
coverage band, from volumes/vol6_conformal/chapters/02_split_conformal.md:

  S1_Split     Split the data: proper training set + held-out calibration set.
  S2_Score     The nonconformity score s(x,y) = 1 - p_hat_y(x); score calibration.
  S3_Quantile  q-hat = the ceil((1-alpha)(n+1))-th smallest score; decode n+1, ceil.
  S4_Set       C(x) = { y : s(x,y) <= q-hat }; regression band y-hat +/- q-hat.
  S5_Coverage  Exchangeable -> test rank uniform on {1..n+1} -> coverage >= 1-alpha.

All equations/numbers are cited to chapter 02 of the conformal volume.

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0602_split_conformal ./render.sh \
      chapters/v0602_split_conformal/scenes.py -q ql \
      S1_Split S2_Score S3_Quantile S4_Set S5_Coverage
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Split the data
# ----------------------------------------------------------------------
class S1_Split(NarratedScene):
    scene_key = "S1_Split"

    def construct(self):
        self.header("Split the data  (ch.2, the construction)")

        title = Text("the simplest machine with a coverage guarantee",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(title))                                      # beat 1

        # the full pool of labelled patients
        pool = self._pool_box("All patients with known AE labels", WHITE)\
            .shift(UP * 1.2)
        self.play_beat(FadeIn(pool, shift=DOWN * 0.2))                     # beat 2

        # split into two piles
        train = self._pool_box("Proper training set", BACK)\
            .scale(0.85).shift(LEFT * 3.3 + DOWN * 0.7)
        calib = self._pool_box("Calibration set", VAR)\
            .scale(0.85).shift(RIGHT * 3.3 + DOWN * 0.7)
        a_tr = Arrow(pool.get_bottom(), train.get_top(), color=DIM, buff=0.15)
        a_ca = Arrow(pool.get_bottom(), calib.get_top(), color=DIM, buff=0.15)

        fit = Text("fit any model  f-hat", font_size=22, color=BACK)\
            .next_to(train, DOWN, buff=0.3)
        self.play_beat(GrowArrow(a_tr), FadeIn(train),
                       FadeIn(fit, shift=UP * 0.2))                        # beat 3

        size = MathTex(r"\text{size } = n", color=VAR).scale(0.9)\
            .next_to(calib, DOWN, buff=0.3)
        hide = Text("never seen during fitting", font_size=20, color=DIM)\
            .next_to(size, DOWN, buff=0.2)
        self.play_beat(GrowArrow(a_ca), FadeIn(calib),
                       FadeIn(size), FadeIn(hide))                         # beat 4

        # why hold it out
        self.play(FadeOut(VGroup(title, pool, a_tr, a_ca, train, fit)),
                  run_time=0.5)
        why = VGroup(
            Text("A model treats a point it trained on", font_size=25, color=WHITE),
            Text("differently from a fresh one.", font_size=25, color=WHITE),
            Text("That would break the symmetry we need.", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.2)
        self.play_beat(FadeIn(why, lag_ratio=0.3))                        # beat 5

        moral = VGroup(
            Text("Kept disjoint:", font_size=26, color=RES),
            Text("calibration patients and a future test patient",
                 font_size=25, color=WHITE),
            Text("are INTERCHANGEABLE — the whole engine.",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.2).next_to(why, DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 6

    def _pool_box(self, label, color):
        box = RoundedRectangle(width=4.6, height=0.8, corner_radius=0.12,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.10)
        t = Text(label, font_size=22, color=color).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 2 — The nonconformity score
# ----------------------------------------------------------------------
class S2_Score(NarratedScene):
    scene_key = "S2_Score"

    def construct(self):
        self.header("The nonconformity score")

        intro = Text("how strange does a patient look to the fitted model?",
                     font_size=27, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # s(x,y), decode x and y
        sxy = MathTex("s", "(", "x", ",", "y", ")").scale(1.5).shift(UP * 1.2)
        sxy[0].set_color(RES); sxy[2].set_color(VAR); sxy[4].set_color(EIG)
        bx = Brace(sxy[2], DOWN, color=VAR)
        bx_l = Text("features: lesion size, within-VIM position",
                    font_size=20, color=VAR).next_to(bx, DOWN, buff=0.15)
        by = Brace(sxy[4], UP, color=EIG)
        by_l = Text("candidate label: AE present or absent",
                    font_size=20, color=EIG).next_to(by, UP, buff=0.15)
        self.play_beat(Write(sxy), GrowFromCenter(bx), FadeIn(bx_l),
                       GrowFromCenter(by), FadeIn(by_l))                  # beat 2

        # the canonical score
        self.play(FadeOut(VGroup(bx, bx_l, by, by_l)), run_time=0.4)
        eq = MathTex("s", "(", "x", ",", "y", ")", "=",
                     "1", "-", r"\hat p_y(x)").scale(1.25).shift(UP * 0.3)
        eq[0].set_color(RES); eq[2].set_color(VAR); eq[4].set_color(EIG)
        eq[9].set_color(BACK)
        br = Brace(eq[9], DOWN, color=BACK)
        br_l = Text("model's predicted probability for label y",
                    font_size=21, color=BACK).next_to(br, DOWN, buff=0.2)
        self.play_beat(Write(eq), GrowFromCenter(br), FadeIn(br_l))      # beat 3

        # big = conforms poorly
        rule = VGroup(
            Text("confident & correct  →  small s", font_size=24, color=BACK),
            Text("confident & wrong    →  large s", font_size=24, color=BAD),
            Text("big score = the point conforms poorly", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.2).next_to(br_l, DOWN, buff=0.45)
        self.play_beat(FadeIn(rule, lag_ratio=0.3))                      # beat 4

        # score every calibration patient
        self.play(FadeOut(VGroup(intro, eq, br, br_l, rule)), run_time=0.5)
        cal = MathTex("s_i", "=", "s(X_i, Y_i)", "=",
                      r"1 - \hat p_{Y_i}(X_i),", r"\quad i = 1,\dots,n")\
            .scale(1.05).shift(UP * 0.9)
        cal[0].set_color(RES); cal[2].set_color(WHITE); cal[4].set_color(BACK)
        usetrue = Text("apply to every calibration patient, using their TRUE label",
                       font_size=23, color=DIM).next_to(cal, DOWN, buff=0.4)
        self.play_beat(Write(cal), FadeIn(usetrue))                      # beat 5

        out = VGroup(
            Text("n strangeness numbers — one per held-out patient",
                 font_size=24, color=VAR),
            Text("the model entered only here; the rest is counting",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.25).next_to(usetrue, DOWN, buff=0.6)
        self.play_beat(FadeIn(out, lag_ratio=0.3))                       # beat 6


# ----------------------------------------------------------------------
# Scene 3 — The quantile
# ----------------------------------------------------------------------
class S3_Quantile(NarratedScene):
    scene_key = "S3_Quantile"

    def construct(self):
        self.header("The quantile  (the finite-sample index)")

        # sorted dots
        scores = [0.04, 0.07, 0.11, 0.15, 0.22, 0.28, 0.41, 0.55, 0.68]
        row = self._score_row(scores).shift(UP * 1.9)
        self.play_beat(FadeIn(row, lag_ratio=0.12))                      # beat 1

        # the index formula
        eq = MathTex("k", "=", r"\Big\lceil", r"(1-\alpha)", "(", "n+1", ")",
                     r"\Big\rceil").scale(1.3).shift(UP * 0.4)
        eq[0].set_color(RES); eq[3].set_color(EIG); eq[5].set_color(VAR)
        self.play_beat(Write(eq))                                        # beat 2

        # decode 1-alpha
        b1 = Brace(eq[3], DOWN, color=EIG)
        b1_l = VGroup(
            Text("target coverage, e.g. 0.9", font_size=21, color=EIG),
            Text("alpha = the miss rate you allow", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.12).next_to(b1, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(b1), FadeIn(b1_l))                 # beat 3

        # decode n+1
        self.play(FadeOut(VGroup(b1, b1_l)), run_time=0.4)
        b2 = Brace(eq[5], DOWN, color=VAR)
        b2_l = VGroup(
            Text("finite-sample correction:", font_size=21, color=VAR),
            Text("quantile of n+1 scores, including the unseen test point",
                 font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.12).next_to(b2, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(b2), FadeIn(b2_l))                 # beat 4

        warn = Text("reach ONE rank higher than the naive n-of-n quantile —"
                    "  use n+1, never just n",
                    font_size=22, color=BAD).next_to(b2_l, DOWN, buff=0.4)
        self.play_beat(FadeIn(warn))                                     # beat 5

        # decode ceiling
        self.play(FadeOut(VGroup(b2, b2_l, warn)), run_time=0.4)
        ceil_l = VGroup(
            Text("ceiling rounds UP to the smallest whole rank",
                 font_size=23, color=WHITE),
            Text("at or above the target (a rank must be an integer)",
                 font_size=23, color=DIM),
            MathTex(r"\hat q = \text{the } k\text{-th smallest score}")
            .set_color(RES).scale(0.95),
        ).arrange(DOWN, buff=0.22).next_to(eq, DOWN, buff=0.6)
        self.play_beat(FadeIn(ceil_l, lag_ratio=0.3))                    # beat 6

        # worked n=9 case
        self.play(FadeOut(VGroup(ceil_l, eq)), run_time=0.5)
        case = MathTex("k", "=", r"\big\lceil", "0.9", r"\times", "10",
                       r"\big\rceil", "=", r"\big\lceil", "9.0", r"\big\rceil",
                       "=", "9").scale(1.1).shift(UP * 0.5)
        case[0].set_color(RES); case[3].set_color(EIG); case[5].set_color(VAR)
        case[12].set_color(RES)
        cap = Text("n = 9,  alpha = 0.1  →  q-hat is the LARGEST calibration score",
                   font_size=23, color=DIM).next_to(case, DOWN, buff=0.5)
        # highlight the max dot in the still-present row
        hl = SurroundingRectangle(row[-1], color=RES, buff=0.08)
        self.play_beat(Write(case), FadeIn(cap), Create(hl))             # beat 7

    def _score_row(self, vals):
        grp = VGroup()
        for v in vals:
            dot = Dot(radius=0.10, color=VAR)
            lab = MathTex(f"{v:.2f}", color=DIM).scale(0.5).next_to(dot, DOWN, buff=0.12)
            grp.add(VGroup(dot, lab))
        grp.arrange(RIGHT, buff=0.55)
        return grp


# ----------------------------------------------------------------------
# Scene 4 — Build the prediction set
# ----------------------------------------------------------------------
class S4_Set(NarratedScene):
    scene_key = "S4_Set"

    def construct(self):
        self.header("Build the prediction set")

        intro = Text("a brand-new patient arrives:  X_(n+1)",
                     font_size=27, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                    # beat 1

        # the set definition
        eq = MathTex("C", "(", "x", ")", "=", r"\big\{", "y", ":",
                     "s(x,y)", r"\le", r"\hat q", r"\big\}")\
            .scale(1.25).shift(UP * 1.2)
        eq[0].set_color(VAR); eq[2].set_color(VAR); eq[6].set_color(EIG)
        eq[8].set_color(RES); eq[10].set_color(RES)
        br = Brace(eq[10], DOWN, color=RES)
        br_l = Text("the threshold from the calibration scores",
                    font_size=21, color=RES).next_to(br, DOWN, buff=0.2)
        self.play_beat(Write(eq), GrowFromCenter(br), FadeIn(br_l))      # beat 2

        # binary candidate 1
        self.play(FadeOut(VGroup(br, br_l)), run_time=0.4)
        c1 = MathTex(r"\text{present:}", r"\ 1 - \hat p_1(X_{n+1})",
                     r"\le", r"\hat q").scale(1.0).next_to(eq, DOWN, buff=0.7)
        c1[3].set_color(RES)
        self.play_beat(FadeIn(c1, shift=UP * 0.2))                       # beat 3

        c0 = MathTex(r"\text{absent:}", r"\ 1 - \hat p_0(X_{n+1})",
                     r"\le", r"\hat q").scale(1.0).next_to(c1, DOWN, buff=0.35)
        c0[3].set_color(RES)
        outcomes = MathTex(r"C \in \{\,\{1\},\ \{0\},\ \{0,1\},\ \varnothing\,\}")\
            .scale(0.9).set_color(DIM).next_to(c0, DOWN, buff=0.4)
        self.play_beat(FadeIn(c0, shift=UP * 0.2), FadeIn(outcomes))     # beat 4

        # regression -> band
        self.play(FadeOut(VGroup(intro, eq, c1, c0, outcomes)), run_time=0.5)
        reg = MathTex(r"s(x,y) = |\,y - \hat y(x)\,|", r"\ \Longrightarrow\ ",
                      r"C(x) = \hat y(x) \pm \hat q").scale(1.05).shift(UP * 1.8)
        reg[2].set_color(RES)
        self.play_beat(Write(reg))                                       # beat 5

        # draw the band
        band = self._band().shift(DOWN * 0.6)
        self.play_beat(FadeIn(band, lag_ratio=0.1))                      # beat 6

        moral = VGroup(
            Text("validity comes from the RANK", font_size=24, color=RES),
            Text("sharpness comes from the MODEL", font_size=24, color=BACK),
            Text("a tighter model narrows the band; the guarantee does not move",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.18).to_edge(DOWN, buff=0.4)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                     # beat 7

    def _band(self):
        ax = Axes(x_range=[0, 6, 1], y_range=[0, 4, 1], x_length=7.5,
                  y_length=2.6, tips=False,
                  axis_config={"include_numbers": False, "color": DIM})
        line = ax.plot(lambda x: 0.45 * x + 0.6, color=VAR, x_range=[0.2, 5.8])
        upper = ax.plot(lambda x: 0.45 * x + 0.6 + 0.9, color=RES,
                        x_range=[0.2, 5.8])
        lower = ax.plot(lambda x: 0.45 * x + 0.6 - 0.9, color=RES,
                        x_range=[0.2, 5.8])
        fill = ax.get_area(upper, [0.2, 5.8], bounded_graph=lower,
                           color=RES, opacity=0.12)
        yh = MathTex(r"\hat y(x)", color=VAR).scale(0.7).next_to(
            ax.c2p(5.8, 0.45 * 5.8 + 0.6), RIGHT, buff=0.1)
        qh = MathTex(r"\pm\,\hat q", color=RES).scale(0.7).next_to(
            ax.c2p(3.0, 0.45 * 3.0 + 0.6 + 0.9), UP, buff=0.1)
        return VGroup(ax, fill, upper, lower, line, yh, qh)


# ----------------------------------------------------------------------
# Scene 5 — Why coverage holds (the rank argument)
# ----------------------------------------------------------------------
class S5_Coverage(NarratedScene):
    scene_key = "S5_Coverage"

    def construct(self):
        self.header("Why coverage holds  (the rank argument)")

        # what we'll show
        goal = MathTex(r"\Pr\big(Y_{n+1} \in C(X_{n+1})\big)",
                       r"\ \ge\ ", r"1-\alpha").scale(1.05).shift(UP * 2.4)
        goal[0].set_color(VAR); goal[2].set_color(RES)
        self.play_beat(Write(goal))                                      # beat 1

        # strategy: covered <=> test score <= q-hat
        strat = MathTex(r"Y_{n+1} \in C(X_{n+1})", r"\iff",
                        r"s_{n+1} \le \hat q").scale(1.05).shift(UP * 1.3)
        strat[0].set_color(VAR); strat[2].set_color(WHITE)
        strat[2][:6].set_color(EIG)
        self.play_beat(Write(strat))                                     # beat 2

        # step 1: rank R
        s1 = MathTex(r"R = \text{rank of } s_{n+1} \text{ in the pool of } n+1",
                     r"\ \Rightarrow\ ", r"s_{n+1} \le \hat q \iff R \le k")\
            .scale(0.85).shift(UP * 0.4)
        s1[0].set_color(WHITE); s1[2].set_color(WHITE)
        s1_t = Text("Step 1:  coverage is a statement about the test score's rank",
                    font_size=21, color=DIM).next_to(s1, UP, buff=0.25)
        self.play_beat(FadeIn(s1_t), Write(s1))                          # beat 3

        # step 2a: fixed function
        self.play(FadeOut(VGroup(goal, strat, s1, s1_t)), run_time=0.5)
        s2t = Text("Step 2:  the load-bearing step", font_size=23, color=RES)\
            .shift(UP * 2.4)
        s2a = VGroup(
            Text("the score is a FIXED function, fitted on the separate",
                 font_size=23, color=WHITE),
            Text("training set, so it treats all n+1 points identically",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.18).next_to(s2t, DOWN, buff=0.4)
        self.play_beat(FadeIn(s2t), FadeIn(s2a, lag_ratio=0.3))          # beat 4

        # step 2b: exchangeable -> uniform rank
        s2b = VGroup(
            Text("exchangeable points  →  exchangeable scores", font_size=23, color=BACK),
            Text("→  the test score is equally likely to be ANY rank", font_size=23, color=BACK),
            MathTex(r"R \sim \text{Uniform}\{1,2,\dots,n+1\}", color=RES).scale(0.95),
        ).arrange(DOWN, buff=0.2).next_to(s2a, DOWN, buff=0.5)
        self.play_beat(FadeIn(s2b, lag_ratio=0.3))                       # beat 5

        unif = MathTex(r"\Pr(R = r)", "=", r"\frac{1}{\,n+1\,}",
                       r"\quad r = 1,\dots,n+1").scale(1.0)\
            .next_to(s2b, DOWN, buff=0.45)
        unif[2].set_color(RES)
        nopriv = Text("no privileged position in the sorted pool",
                      font_size=21, color=DIM).next_to(unif, DOWN, buff=0.2)
        self.play_beat(Write(unif), FadeIn(nopriv))                      # beat 6

        # step 3: count
        self.play(FadeOut(VGroup(s2t, s2a, s2b, unif, nopriv)), run_time=0.5)
        s3t = Text("Step 3:  just count", font_size=23, color=RES).shift(UP * 2.5)
        count = MathTex(r"\Pr(\text{covered})", "=", r"\Pr(R \le k)", "=",
                        r"\frac{k}{\,n+1\,}").scale(1.1).shift(UP * 1.3)
        count[0].set_color(VAR); count[4].set_color(RES)
        self.play_beat(FadeIn(s3t), Write(count))                       # beat 7

        bound = MathTex(r"1-\alpha", r"\ \le\ ", r"\frac{k}{n+1}",
                        r"\ <\ ", r"1-\alpha + \frac{1}{\,n+1\,}")\
            .scale(1.05).next_to(count, DOWN, buff=0.7)
        bound[0].set_color(RES); bound[2].set_color(RES); bound[4].set_color(RES)
        box = SurroundingRectangle(bound, color=RES, buff=0.25)
        why = VGroup(
            Text("ceiling ≥ its argument  →  lower bound", font_size=20, color=DIM),
            Text("ceiling < argument + 1  →  upper bound", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.12).next_to(box, DOWN, buff=0.35)
        self.play_beat(Write(bound), Create(box), FadeIn(why))          # beat 8
