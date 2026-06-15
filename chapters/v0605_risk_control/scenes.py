"""v0605_risk_control — "Conformal risk control".

Five narrated scenes. Generalize from coverage (a 0/1 miscoverage loss) to any
monotone, bounded loss; define the risk R(lambda) = E[L_lambda] and its
monotonicity; state the conformal-risk-control selection rule with the finite-
sample cushion (Angelopoulos, Bates, Fisch, Lei & Schuster, ICLR 2024); state the
guarantee E[L_lambda-hat] <= alpha with coverage as the special case; and work the
FNR operating-point example by hand.

All equations/numbers are quoted from:
  volumes/vol6_conformal/chapters/05_risk_control.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0605_risk_control ./render.sh \
      chapters/v0605_risk_control/scenes.py -q ql \
      S1_Beyond S2_RiskFn S3_Calibrate S4_Guarantee S5_FNR
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Beyond miscoverage
# ----------------------------------------------------------------------
class S1_Beyond(NarratedScene):
    scene_key = "S1_Beyond"

    def construct(self):
        self.header("Beyond miscoverage")

        intro = Text("so far: every guarantee is about COVERAGE",
                     font_size=28, color=DIM).shift(UP * 2.4)
        cov = MathTex(r"\Pr\big(", "Y", r"\in", "C(X)", r"\big)", r"\geq",
                      r"1-\alpha").scale(1.1).next_to(intro, DOWN, buff=0.45)
        cov[1].set_color(VAR); cov[3].set_color(BACK); cov[6].set_color(EIG)
        self.play_beat(FadeIn(intro), Write(cov))                          # beat 1

        # coverage is secretly a 0/1 loss
        loss01 = MathTex(r"L^{\mathrm{cov}}", "=",
                         r"\mathbf 1\{", "Y", r"\notin", "C(X)", r"\}")\
            .scale(1.0).next_to(cov, DOWN, buff=0.6)
        loss01[0].set_color(RES); loss01[3].set_color(VAR); loss01[5].set_color(BACK)
        zo = Text("a 0/1 loss:  1 if truth is OUTSIDE the set, else 0",
                  font_size=22, color=DIM).next_to(loss01, DOWN, buff=0.25)
        self.play_beat(Write(loss01), FadeIn(zo))                          # beat 2

        # but the clinic wants a flag, not a set
        self.play(FadeOut(VGroup(intro, cov, loss01, zo)), run_time=0.5)
        ask = VGroup(
            Text("the clinic does not want a SET", font_size=28, color=WHITE),
            Text("it wants a FLAG:  yes / no", font_size=28, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.4)
        self.play_beat(FadeIn(ask[0]), FadeIn(ask[1], shift=UP * 0.2))      # beat 3

        # the two errors are not symmetric
        asym = VGroup(
            VGroup(
                Text("false ALARM", font_size=24, color=DIM),
                Text("one extra cautious talk", font_size=21, color=DIM),
            ).arrange(DOWN, buff=0.12),
            MathTex(r"\ll", color=BAD).scale(1.3),
            VGroup(
                Text("MISSED event", font_size=24, color=BAD),
                Text("patient walks out unwarned", font_size=21, color=BAD),
            ).arrange(DOWN, buff=0.12),
        ).arrange(RIGHT, buff=0.9).next_to(ask, DOWN, buff=0.7)
        self.play_beat(FadeIn(asym, lag_ratio=0.2))                        # beat 4

        # generalize: control any expected loss
        self.play(FadeOut(VGroup(ask, asym)), run_time=0.5)
        gen = MathTex(r"\text{control}\quad", r"\mathbb E\big[", "L_\\lambda",
                      r"\big]").scale(1.2).shift(UP * 1.3)
        gen[1].set_color(WHITE); gen[2].set_color(RES)
        gen_cap = Text("replace the 0/1 coverage loss with ANY loss we care about",
                       font_size=24, color=DIM).next_to(gen, DOWN, buff=0.3)
        self.play_beat(Write(gen), FadeIn(gen_cap))                        # beat 5

        # the running example: FNR
        fnr = VGroup(
            Text("running example:  false-negative rate (FNR)", font_size=25, color=WHITE),
            Text("of all patients who TRULY have the event,", font_size=23, color=DIM),
            Text("what fraction do we MISS?", font_size=23, color=BAD),
        ).arrange(DOWN, buff=0.2).next_to(gen_cap, DOWN, buff=0.55)
        self.play_beat(FadeIn(fnr, lag_ratio=0.2))                         # beat 6

        # the goal: hold E[FNR] <= alpha
        goal = MathTex(r"\mathbb E[\mathrm{FNR}]", r"\leq", r"\alpha")\
            .scale(1.2).to_edge(DOWN, buff=0.7)
        goal[0].set_color(RES); goal[2].set_color(EIG)
        self.play_beat(Write(goal))                                        # beat 7


# ----------------------------------------------------------------------
# Scene 2 — The risk function
# ----------------------------------------------------------------------
class S2_RiskFn(NarratedScene):
    scene_key = "S2_RiskFn"

    def construct(self):
        self.header("The risk function")

        # the knob lambda
        knob = MathTex(r"\lambda", r"\in", "[0,1]").scale(1.4).shift(UP * 2.3)
        knob[0].set_color(EIG)
        knob_cap = Text("the flag THRESHOLD — the one knob",
                        font_size=24, color=DIM).next_to(knob, DOWN, buff=0.3)
        self.play_beat(Write(knob), FadeIn(knob_cap))                      # beat 1

        # the flag rule
        rule = MathTex("T_\\lambda(x)", "=", r"\mathbf 1\{", r"\hat p(x)",
                       r"\geq", r"\lambda", r"\}").scale(1.1).shift(UP * 0.9)
        rule[0].set_color(VAR); rule[3].set_color(WHITE); rule[5].set_color(EIG)
        br = Brace(rule[3], DOWN, color=WHITE)
        p_lab = Text("base model's predicted event probability",
                     font_size=22, color=WHITE).next_to(br, DOWN, buff=0.2)
        self.play_beat(Write(rule), GrowFromCenter(br), FadeIn(p_lab))     # beat 2

        # lambda down -> flag more ; up -> flag fewer
        self.play(FadeOut(VGroup(br, p_lab, knob, knob_cap)), run_time=0.4)
        slide = VGroup(
            MathTex(r"\lambda \downarrow", r"\ \Rightarrow\ ",
                    r"\text{flag MORE}").scale(0.95),
            MathTex(r"\lambda \uparrow", r"\ \Rightarrow\ ",
                    r"\text{flag FEWER}").scale(0.95),
        ).arrange(DOWN, buff=0.3).next_to(rule, DOWN, buff=0.6)
        slide[0][0].set_color(EIG); slide[1][0].set_color(EIG)
        self.play_beat(FadeIn(slide, lag_ratio=0.3))                       # beat 3

        # the loss
        self.play(FadeOut(slide), rule.animate.scale(0.75).to_edge(UP, buff=1.1),
                  run_time=0.5)
        loss = MathTex("L_\\lambda(x,y)", "=", r"\mathbf 1\{", "y=1",
                       r"\ \text{and}\ ", r"\hat p(x) < \lambda", r"\}")\
            .scale(0.95).shift(UP * 0.9)
        loss[0].set_color(RES); loss[3].set_color(VAR); loss[5].set_color(EIG)
        loss_cap = Text("1 exactly when the event happened but we FAILED to flag it",
                        font_size=22, color=DIM).next_to(loss, DOWN, buff=0.3)
        self.play_beat(Write(loss), FadeIn(loss_cap))                      # beat 4

        # averaged over true positives = FNR
        avg = MathTex(r"\text{averaged over }", "y=1", r"\text{ patients}",
                      r"\ \Longrightarrow\ ", r"\mathrm{FNR}")\
            .scale(0.9).next_to(loss_cap, DOWN, buff=0.5)
        avg[1].set_color(VAR); avg[4].set_color(BAD)
        self.play_beat(Write(avg))                                         # beat 5

        # the risk function
        self.play(FadeOut(VGroup(rule, loss, loss_cap, avg)), run_time=0.5)
        risk = MathTex("R(\\lambda)", "=", r"\mathbb E\big[", "L_\\lambda(X,Y)",
                       r"\big]").scale(1.25).shift(UP * 1.2)
        risk[0].set_color(RES); risk[3].set_color(RES)
        risk_cap = Text("the RISK:  expected loss over a random patient",
                        font_size=24, color=DIM).next_to(risk, DOWN, buff=0.3)
        self.play_beat(Write(risk), FadeIn(risk_cap))                      # beat 6

        # monotonicity, per patient
        mono = MathTex(r"\lambda \leq \lambda'", r"\ \Longrightarrow\ ",
                       "L_\\lambda(x,y)", r"\leq", "L_{\\lambda'}(x,y)")\
            .scale(0.95).next_to(risk_cap, DOWN, buff=0.55)
        mono[2].set_color(RES); mono[4].set_color(RES)
        mono_cap = Text("raise lambda → flag fewer → miss MORE (or the same)",
                        font_size=22, color=BAD).next_to(mono, DOWN, buff=0.25)
        self.play_beat(Write(mono), FadeIn(mono_cap))                      # beat 7

        # therefore R is monotone
        Rmono = MathTex(r"\Rightarrow\quad", "R(\\lambda)",
                        r"\ \text{is non-decreasing in}\ ", r"\lambda")\
            .scale(1.0).to_edge(DOWN, buff=0.7)
        Rmono[1].set_color(RES); Rmono[3].set_color(EIG)
        box = SurroundingRectangle(Rmono, color=RES, buff=0.2)
        self.play_beat(Write(Rmono), Create(box))                          # beat 8


# ----------------------------------------------------------------------
# Scene 3 — Calibrating the threshold
# ----------------------------------------------------------------------
class S3_Calibrate(NarratedScene):
    scene_key = "S3_Calibrate"

    def construct(self):
        self.header("Calibrating the threshold  (Angelopoulos et al., ICLR 2024)")

        setup = VGroup(
            Text("n calibration patients", font_size=26, color=WHITE),
            Text("each:  truth  +  out-of-fold predicted risk  p-hat",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).shift(UP * 2.3)
        self.play_beat(FadeIn(setup, lag_ratio=0.2))                       # beat 1

        # empirical risk
        emp = MathTex(r"\hat R_n(\lambda)", "=", r"\frac{1}{n}",
                      r"\sum_{i=1}^{n}", "L_\\lambda(x_i, y_i)")\
            .scale(1.05).shift(UP * 0.9)
        emp[0].set_color(RES); emp[4].set_color(RES)
        emp_cap = Text("empirical risk: average loss over calibration",
                       font_size=23, color=DIM).next_to(emp, DOWN, buff=0.3)
        self.play_beat(Write(emp), FadeIn(emp_cap))                        # beat 2

        # want largest lambda we can certify
        want = Text("want the LARGEST (strictest) lambda we can certify safe",
                    font_size=24, color=WHITE).next_to(emp_cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(want, shift=UP * 0.2))                       # beat 3

        # but it's noisy
        self.play(FadeOut(VGroup(setup, want)),
                  emp.animate.scale(0.8).to_edge(UP, buff=1.1),
                  emp_cap.animate.scale(0.8).next_to(emp, DOWN, buff=0.2)
                  .set_y(emp.get_y() - 0.7),
                  run_time=0.5)
        noisy = VGroup(
            Text("but  R-hat-n  is a NOISY estimate of the true risk",
                 font_size=25, color=BAD),
            Text("stop where it just equals alpha → overshoot ~half the time",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.4)
        self.play_beat(FadeIn(noisy[0]), FadeIn(noisy[1], shift=UP * 0.2)) # beat 4

        # the cushion ~ 1/n
        cushion = MathTex(r"\text{cushion}", "=", r"\frac{1-\alpha}{n}",
                          r"\ \sim\ ", r"\frac{1}{n}").scale(1.05)\
            .next_to(noisy, DOWN, buff=0.55)
        cushion[2].set_color(BACK); cushion[4].set_color(BACK)
        self.play_beat(Write(cushion))                                     # beat 5

        # the selection rule
        self.play(FadeOut(VGroup(noisy, cushion)), run_time=0.5)
        rule = MathTex(r"\hat\lambda", "=", r"\sup\Big\{",
                       r"\lambda", ":", r"\hat R_n(\lambda)", r"\leq",
                       r"\alpha - \tfrac{1-\alpha}{n}", r"\Big\}")\
            .scale(0.95).shift(UP * 0.2)
        rule[0].set_color(EIG); rule[3].set_color(EIG); rule[5].set_color(RES)
        rule[7].set_color(BACK)
        br = Brace(rule[7], DOWN, color=BACK)
        br_lab = Text("conservative target = alpha minus the cushion",
                      font_size=22, color=BACK).next_to(br, DOWN, buff=0.2)
        self.play_beat(Write(rule), GrowFromCenter(br), FadeIn(br_lab))    # beat 6

        # the cushion is the price of honesty
        self.play(FadeOut(VGroup(br, br_lab)), run_time=0.4)
        price = VGroup(
            Text("the cushion is the PRICE OF HONESTY", font_size=25, color=RES),
            Text("at n = 10 it is real;  at n = 100 it nearly vanishes",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.22).next_to(rule, DOWN, buff=0.8)
        self.play_beat(FadeIn(price[0]), FadeIn(price[1], shift=UP * 0.2)) # beat 7

        # drop it and you fool yourself
        self.play(FadeOut(price), run_time=0.4)
        drop = VGroup(
            Text("drop the cushion → tune to calibration NOISE", font_size=24, color=BAD),
            Text("reported miss rate sits at alpha, true rate drifts ABOVE it",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.22).next_to(rule, DOWN, buff=0.8)
        self.play_beat(FadeIn(drop[0]), FadeIn(drop[1], shift=UP * 0.2))   # beat 8


# ----------------------------------------------------------------------
# Scene 4 — The guarantee
# ----------------------------------------------------------------------
class S4_Guarantee(NarratedScene):
    scene_key = "S4_Guarantee"

    def construct(self):
        self.header("The guarantee  (K6)")

        intro = Text("what the cushion buys: a statement about the NEXT patient",
                     font_size=27, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # exchangeability assumption
        exch = MathTex(r"(x_1,y_1),\dots,(x_n,y_n),", "(x_{n+1},y_{n+1})")\
            .scale(0.95).shift(UP * 1.3)
        exch[1].set_color(VAR)
        exch_lab = Text("EXCHANGEABLE — interchangeable in order",
                        font_size=24, color=BACK).next_to(exch, DOWN, buff=0.3)
        only = Text("(the only assumption beyond a monotone, bounded loss)",
                    font_size=21, color=DIM).next_to(exch_lab, DOWN, buff=0.2)
        self.play_beat(Write(exch), FadeIn(exch_lab), FadeIn(only))        # beat 2

        # the theorem
        self.play(FadeOut(VGroup(intro, exch, exch_lab, only)), run_time=0.5)
        thm = MathTex(r"\mathbb E\big[", "L_{\\hat\\lambda}", "(X_{n+1}, Y_{n+1})",
                      r"\big]", r"\leq", r"\alpha").scale(1.25).shift(UP * 1.0)
        thm[1].set_color(RES); thm[2].set_color(VAR); thm[5].set_color(EIG)
        box = SurroundingRectangle(thm, color=RES, buff=0.25)
        self.play_beat(Write(thm), Create(box))                            # beat 3

        # decode the expectation
        br = Brace(thm[0:4], DOWN, color=WHITE)
        br_lab = Text("expectation over the calibration draw AND the new patient",
                      font_size=22, color=WHITE).next_to(br, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(br), FadeIn(br_lab))                 # beat 4

        # tight to O(1/n)
        self.play(FadeOut(VGroup(br, br_lab)), run_time=0.4)
        tight = MathTex(r"\alpha", r"\ \leq\ ", r"\mathbb E[L_{\hat\lambda}]",
                        r"\ \leq\ ", r"\alpha + O\!\left(\tfrac{1}{n}\right)")\
            .scale(1.0).next_to(box, DOWN, buff=0.6)
        tight[0].set_color(EIG); tight[2].set_color(RES); tight[4].set_color(BACK)
        tight_cap = Text("tight to order one over n",
                         font_size=23, color=DIM).next_to(tight, DOWN, buff=0.25)
        self.play_beat(Write(tight), FadeIn(tight_cap))                    # beat 5

        # no distributional assumption
        free = VGroup(
            Text("no distributional assumption", font_size=24, color=WHITE),
            Text("any base model  p-hat  ·  holds at the actual n",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(tight_cap, DOWN, buff=0.45)
        self.play_beat(FadeIn(free, lag_ratio=0.3))                        # beat 6

        # coverage is the special case
        self.play(FadeOut(VGroup(thm, box, tight, tight_cap, free)), run_time=0.5)
        spec = MathTex("L_\\lambda", "=", r"\mathbf 1\{", "Y", r"\notin",
                       "C(X)", r"\}").scale(1.05).shift(UP * 1.1)
        spec[0].set_color(RES); spec[3].set_color(VAR); spec[5].set_color(BACK)
        spec_cap = Text("coverage = the special case:  the miscoverage indicator",
                        font_size=24, color=DIM).next_to(spec, DOWN, buff=0.3)
        self.play_beat(Write(spec), FadeIn(spec_cap))                      # beat 7

        # so controlling its E at alpha = coverage
        red = MathTex(r"\mathbb E[L_\lambda]", r"\leq", r"\alpha",
                      r"\ \Longleftrightarrow\ ",
                      r"\Pr\big(Y \in C(X)\big) \geq 1-\alpha")\
            .scale(0.85).next_to(spec_cap, DOWN, buff=0.55)
        red[0].set_color(RES); red[2].set_color(EIG); red[4].set_color(BACK)
        self.play_beat(Write(red))                                         # beat 8


# ----------------------------------------------------------------------
# Scene 5 — Example: FNR control
# ----------------------------------------------------------------------
class S5_FNR(NarratedScene):
    scene_key = "S5_FNR"

    def construct(self):
        self.header("Example: FNR control")

        intro = VGroup(
            Text("control the FNR of a multilabel flag", font_size=27, color=WHITE),
            Text("gait ataxia after FUS-VIM thalamotomy", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).shift(UP * 2.5)
        self.play_beat(FadeIn(intro, lag_ratio=0.2))                       # beat 1

        # the 10 sorted scores
        scores = MathTex(r"\hat p = (",
                         "0.12", ",", "0.21", ",", "0.28", ",", "0.35", ",",
                         "0.44", ",", "0.51", ",", "0.60", ",", "0.67", ",",
                         "0.78", ",", "0.90", ")").scale(0.78).shift(UP * 1.3)
        scores.set_color(WHITE)
        scores[1].set_color(VAR)   # 0.12 (lowest)
        scores[3].set_color(EIG)   # 0.21 (the threshold-to-be)
        n_cap = Text("10 patients who TRULY had the event (y = 1)",
                     font_size=23, color=DIM).next_to(scores, DOWN, buff=0.3)
        self.play_beat(Write(scores), FadeIn(n_cap))                       # beat 2

        # choose alpha
        alpha = MathTex(r"\alpha", "=", "0.2").scale(1.2)\
            .next_to(n_cap, DOWN, buff=0.5)
        alpha[0].set_color(EIG); alpha[2].set_color(EIG)
        a_cap = Text("willing to miss at most 20% of true events",
                     font_size=23, color=DIM).next_to(alpha, DOWN, buff=0.25)
        self.play_beat(Write(alpha), FadeIn(a_cap))                        # beat 3

        # the cushion -> conservative target
        self.play(FadeOut(VGroup(intro, alpha, a_cap)),
                  scores.animate.scale(0.85).to_edge(UP, buff=1.0),
                  n_cap.animate.scale(0.85).next_to(scores, DOWN, buff=0.2)
                  .set_y(scores.get_y() - 0.55),
                  run_time=0.5)
        cush = MathTex(r"\frac{1-0.2}{10}", "=", "0.08", r"\ \Rightarrow\ ",
                       r"\text{target} = 0.2 - 0.08 = 0.12")\
            .scale(0.9).shift(UP * 0.4)
        cush[0].set_color(BACK); cush[2].set_color(BACK); cush[4].set_color(RES)
        self.play_beat(Write(cush))                                        # beat 4

        # each miss = 0.1 -> at most 1 miss
        miss = MathTex(r"\text{each miss} = 0.1", r"\ \Rightarrow\ ",
                       r"\text{target } 0.12 \Rightarrow \text{at most ONE miss}")\
            .scale(0.85).next_to(cush, DOWN, buff=0.55)
        miss[2].set_color(RES)
        self.play_beat(Write(miss))                                        # beat 5

        # sweep lambda -> strictest missing one is 0.21
        self.play(FadeOut(VGroup(cush, miss)), run_time=0.4)
        sweep = VGroup(
            MathTex(r"\lambda \in (0.12,\, 0.21]", r":\ ",
                    r"\text{miss 1}", r"\ \to\ \mathrm{FNR}=0.1\ \checkmark").scale(0.85),
            MathTex(r"\lambda > 0.21", r":\ ",
                    r"\text{miss 2}", r"\ \to\ \mathrm{FNR}=0.2\ \times").scale(0.85),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.4)
        sweep[0][3].set_color(BACK); sweep[1][3].set_color(BAD)
        self.play_beat(FadeIn(sweep, lag_ratio=0.3))                       # beat 6

        # lambda-hat = 0.21
        self.play(FadeOut(sweep), run_time=0.4)
        lamhat = MathTex(r"\hat\lambda", "=", "0.21").scale(1.4).shift(UP * 0.5)
        lamhat[0].set_color(EIG); lamhat[2].set_color(RES)
        box = SurroundingRectangle(lamhat, color=RES, buff=0.25)
        op = Text("flag any patient with  p-hat ≥ 0.21  as high-risk",
                  font_size=24, color=WHITE).next_to(box, DOWN, buff=0.4)
        self.play_beat(Write(lamhat), Create(box), FadeIn(op))             # beat 7

        # closing: tighter ceiling -> set grows
        self.play(FadeOut(VGroup(lamhat, box, op, scores, n_cap)), run_time=0.5)
        close = VGroup(
            Text("tighten the ceiling alpha", font_size=26, color=EIG),
            Text("↓", font_size=28, color=DIM),
            Text("threshold drops to catch more people", font_size=26, color=WHITE),
            Text("↓", font_size=28, color=DIM),
            Text("the flagged set GROWS to meet the lower miss rate",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.18)
        self.play_beat(LaggedStart(*[FadeIn(c) for c in close], lag_ratio=0.25))  # beat 8


# Quick self-check of beat counts when run directly (not under manim).
if __name__ == "__main__":
    expected = {
        "S1_Beyond": 7, "S2_RiskFn": 8, "S3_Calibrate": 8,
        "S4_Guarantee": 8, "S5_FNR": 8,
    }
    for k, v in expected.items():
        print(f"{k:14s} scenes-expects={v:2d}  narration={len(SCENES[k]):2d}  "
              f"{'OK' if v == len(SCENES[k]) else 'MISMATCH'}")
