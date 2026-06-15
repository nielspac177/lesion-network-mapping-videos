"""v0603_jackknife_cv — "Jackknife+ and CV+".

Five narrated scenes. Split conformal wastes data on a held-out calibration set;
jackknife+ leaves each patient out once, refits, and combines the N leave-out
models, each with its own center and radius. The worst-case floor drops from
one minus alpha to one minus two alpha. CV+ is the K-fold budget version with the
same floor. Close with the split vs jackknife+/CV+ trade-off.

All equations/numbers are from:
  volumes/vol6_conformal/chapters/03_jackknife_cv.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0603_jackknife_cv ./render.sh \
      chapters/v0603_jackknife_cv/scenes.py -q ql \
      S1_Waste S2_JackknifePlus S3_Floor S4_CVPlus S5_Tradeoff
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Splitting wastes data
# ----------------------------------------------------------------------
class S1_Waste(NarratedScene):
    scene_key = "S1_Waste"

    def construct(self):
        self.header("Splitting wastes data")

        # beat 1 — recall split conformal
        title = Text("Split conformal, recalled", font_size=30, color=WHITE).shift(UP * 2.4)
        split = VGroup(
            self._chip("training set", VAR, 3.4),
            self._chip("calibration set", EIG, 3.4),
        ).arrange(RIGHT, buff=0.5).next_to(title, DOWN, buff=0.5)
        cap = Text("fit once on training, score the held-out calibration patients",
                   font_size=22, color=DIM).next_to(split, DOWN, buff=0.35)
        self.play_beat(FadeIn(title), FadeIn(split, lag_ratio=0.3), FadeIn(cap))   # beat 1

        # beat 2 — it works exactly
        cov = MathTex(r"\big[\,1-\alpha,\ \ 1-\alpha+\tfrac{1}{n+1}\,\big)").scale(1.1)
        cov.set_color(BACK)
        cov.next_to(cap, DOWN, buff=0.5)
        cov_cap = Text("coverage lands here — exactly. so why not stop?",
                       font_size=22, color=DIM).next_to(cov, DOWN, buff=0.25)
        self.play_beat(Write(cov), FadeIn(cov_cap))                                # beat 2

        # beat 3 — the small-cohort arithmetic
        self.play(FadeOut(VGroup(title, split, cap, cov, cov_cap)), run_time=0.5)
        setup = VGroup(
            MathTex("N", "=", "36", r"\ \text{patients}").scale(1.0),
            MathTex(r"\text{AE rate}", r"\approx", r"\tfrac{1}{6}",
                    r"\ \Rightarrow\ \sim 6\ \text{AE+}").scale(1.0),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.4)
        setup[0][0].set_color(VAR); setup[0][2].set_color(VAR)
        setup[1][3].set_color(BAD)
        self.play_beat(FadeIn(setup, lag_ratio=0.3))                               # beat 3

        # beat 4 — split it, three AE+ scores
        spl = MathTex(r"18\ \text{train}", r"\ \ |\ \ ", r"18\ \text{calibrate}",
                      r"\ \Rightarrow\ ", r"\sim 3\ \text{AE+ scores}").scale(0.95)
        spl[4].set_color(BAD)
        spl.next_to(setup, DOWN, buff=0.6)
        self.play_beat(Write(spl))                                                 # beat 4

        # beat 5 — the index runs off the end
        idx = MathTex(r"\big\lceil (1-\alpha)(n_{\text{AE+}}+1)\big\rceil",
                      "=", r"\lceil 0.9\times 4\rceil", "=", "4").scale(0.95)
        idx[4].set_color(BAD)
        idx.next_to(spl, DOWN, buff=0.5)
        warn = Text("index 4 in a 3-element list — no 90% threshold exists",
                    font_size=22, color=BAD).next_to(idx, DOWN, buff=0.25)
        self.play_beat(Write(idx), FadeIn(warn))                                   # beat 5

        # beat 6 — the goal
        self.play(FadeOut(VGroup(setup, spl, idx, warn)), run_time=0.5)
        goal = VGroup(
            Text("Goal:", font_size=28, color=RES),
            Text("use ALL the data to calibrate", font_size=26, color=WHITE),
            Text("while keeping honest coverage", font_size=26, color=WHITE),
            Text("→  leave each patient out, one at a time", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).shift(UP * 0.4)
        self.play_beat(FadeIn(goal, lag_ratio=0.2))                                # beat 6

        # beat 7 — the constraint
        rule = Text("but: a patient's score must come from a model\nthat NEVER trained on them",
                    font_size=25, color=BAD, line_spacing=0.8).next_to(goal, DOWN, buff=0.6)
        self.play_beat(FadeIn(rule, shift=UP * 0.2))                               # beat 7

    def _chip(self, label, color, width):
        box = RoundedRectangle(width=width, height=0.75, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=22, color=color).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 2 — Jackknife+
# ----------------------------------------------------------------------
class S2_JackknifePlus(NarratedScene):
    scene_key = "S2_JackknifePlus"

    def construct(self):
        self.header("Jackknife+  (Barber, Candès, Ramdas & Tibshirani 2021)")

        # beat 1 — the leave-i-out fit
        loo = MathTex(r"\hat\mu_{-i}").scale(1.5).shift(UP * 1.8)
        loo.set_color(VAR)
        loo_b = Brace(loo, DOWN, color=VAR)
        loo_lab = Text("model refit on every patient EXCEPT i",
                       font_size=24, color=VAR).next_to(loo_b, DOWN, buff=0.2)
        self.play_beat(Write(loo), GrowFromCenter(loo_b), FadeIn(loo_lab))         # beat 1

        # beat 2 — the residual
        self.play(FadeOut(VGroup(loo_b, loo_lab)),
                  loo.animate.scale(0.7).to_edge(UP, buff=1.1), run_time=0.5)
        res = MathTex(r"R_i^{\text{LOO}}", "=",
                      r"\big|\,", "Y_i", "-", r"\hat\mu_{-i}(X_i)", r"\,\big|").scale(1.15)
        res[0].set_color(EIG); res[3].set_color(VAR); res[5].set_color(VAR)
        res.shift(UP * 0.8)
        res_b = Brace(res[2:7], DOWN, color=DIM)
        res_lab = Text("absolute residual: how badly the leave-i-out model\nmisses the patient it never saw",
                       font_size=22, color=DIM, line_spacing=0.8).next_to(res_b, DOWN, buff=0.2)
        self.play_beat(Write(res), GrowFromCenter(res_b), FadeIn(res_lab))         # beat 2

        # beat 3 — do it for all N
        alln = Text("do it for all N  →  every patient calibrates,\nno score from a model that trained on it",
                    font_size=24, color=BACK, line_spacing=0.8).next_to(res_lab, DOWN, buff=0.45)
        self.play_beat(FadeIn(alln, shift=UP * 0.2))                               # beat 3

        # beat 4 — N leave-out models, use all of them
        self.play(FadeOut(VGroup(loo, res, res_b, res_lab, alln)), run_time=0.5)
        many = VGroup(
            Text("a new patient: no single model —", font_size=26, color=WHITE),
            MathTex(r"\hat\mu_{-1},\ \hat\mu_{-2},\ \dots,\ \hat\mu_{-N}").scale(1.1),
            Text("jackknife+ uses ALL N of them", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.0)
        many[1].set_color(VAR)
        self.play_beat(FadeIn(many, lag_ratio=0.25))                               # beat 4

        # beat 5 — pad each prediction: lower & upper edge
        self.play(FadeOut(many), run_time=0.4)
        edge = MathTex(r"\big[\,", r"\hat\mu_{-i}(X_{n+1})", "-", r"R_i^{\text{LOO}}",
                       r"\ ,\ ", r"\hat\mu_{-i}(X_{n+1})", "+", r"R_i^{\text{LOO}}", r"\,\big]").scale(0.95)
        edge[1].set_color(VAR); edge[5].set_color(VAR)
        edge[3].set_color(EIG); edge[7].set_color(EIG)
        edge.shift(UP * 1.3)
        eb_lo = Brace(edge[1:4], DOWN, color=DIM)
        lo_lab = Text("lower edge", font_size=20, color=DIM).next_to(eb_lo, DOWN, buff=0.15)
        eb_hi = Brace(edge[5:8], UP, color=DIM)
        hi_lab = Text("upper edge", font_size=20, color=DIM).next_to(eb_hi, UP, buff=0.15)
        self.play_beat(Write(edge), GrowFromCenter(eb_lo), FadeIn(lo_lab),
                       GrowFromCenter(eb_hi), FadeIn(hi_lab))                       # beat 5

        # beat 6 — the set: too many exclusions
        self.play(FadeOut(VGroup(eb_lo, lo_lab, eb_hi, hi_lab)),
                  edge.animate.scale(0.8).to_edge(UP, buff=1.2), run_time=0.5)
        rule = Text("candidate y stays in the set unless TOO MANY\npadded intervals exclude it on the same side",
                    font_size=25, color=WHITE, line_spacing=0.8).shift(UP * 0.4)
        self.play_beat(FadeIn(rule, shift=UP * 0.2))                               # beat 6

        # beat 7 — the quantile index
        idx = MathTex(r"\text{too many}", "=", r"\big\lceil (1-\alpha)(n+1)\big\rceil").scale(1.0)
        idx[2].set_color(RES)
        idx.next_to(rule, DOWN, buff=0.6)
        idx_cap = Text("the same quantile index as the split proof",
                       font_size=22, color=DIM).next_to(idx, DOWN, buff=0.25)
        self.play_beat(Write(idx), FadeIn(idx_cap))                                # beat 7

        # beat 8 — the "+" = own center AND own radius
        plus = VGroup(
            Text("each comparison uses its OWN center", font_size=24, color=VAR),
            Text("and its OWN radius", font_size=24, color=EIG),
            Text("= what the \"+\" denotes, and what the proof needs",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.2).next_to(idx_cap, DOWN, buff=0.4)
        self.play_beat(FadeIn(plus, lag_ratio=0.3))                                # beat 8


# ----------------------------------------------------------------------
# Scene 3 — The 1-2alpha floor
# ----------------------------------------------------------------------
class S3_Floor(NarratedScene):
    scene_key = "S3_Floor"

    def construct(self):
        self.header("The 1 − 2α floor")

        # beat 1 — the theorem
        thm = MathTex(r"\Pr\big(", "Y_{n+1}", r"\in", r"C_\alpha(X_{n+1})", r"\big)",
                      r"\ \geq\ ", "1-2\\alpha").scale(1.25).shift(UP * 1.4)
        thm[1].set_color(VAR); thm[3].set_color(BACK); thm[6].set_color(RES)
        cap = Text("under exchangeability, for any symmetric base model",
                   font_size=23, color=DIM).next_to(thm, DOWN, buff=0.3)
        self.play_beat(Write(thm), FadeIn(cap))                                    # beat 1

        # beat 2 — not 1-alpha; picture the residual matrix
        note = Text("one minus TWO alpha — not one minus alpha.\nwhere does the factor of two come from?",
                    font_size=25, color=BAD, line_spacing=0.8).next_to(cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(note, shift=UP * 0.2))                               # beat 2

        # beat 3 — R_ij matrix definition
        self.play(FadeOut(VGroup(thm, cap, note)), run_time=0.5)
        rij = MathTex("R_{ij}", "=", r"\text{miss of the model trained on all}", r"\ \text{except } j,",
                      r"\ \text{at point } i").scale(0.8)
        rij[0].set_color(EIG)
        rij.shift(UP * 2.1)
        grid = self._matrix_grid().next_to(rij, DOWN, buff=0.4)
        diag_lab = Text("diagonal i = j  →  ordinary leave-one-out residual",
                        font_size=22, color=DIM).next_to(grid, DOWN, buff=0.35)
        self.play_beat(Write(rij), Create(grid), FadeIn(diag_lab))                 # beat 3

        # beat 4 — exchangeability => row/col symmetry
        sym = Text("exchangeability ⇒ invariant under swapping\nrows and columns together",
                   font_size=24, color=BACK, line_spacing=0.8).next_to(diag_lab, DOWN, buff=0.4)
        self.play_beat(FadeIn(sym, shift=UP * 0.2))                                # beat 4

        # beat 5 — counting argument
        self.play(FadeOut(VGroup(rij, grid, diag_lab, sym)), run_time=0.5)
        count = VGroup(
            Text("a counting argument over the \"strange pairs\"", font_size=25, color=WHITE),
            Text("bounds how many patients can be left uncovered", font_size=25, color=WHITE),
            Text("→  translating that count to a probability gives the floor",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.28).shift(UP * 1.0)
        self.play_beat(FadeIn(count, lag_ratio=0.25))                              # beat 5

        # beat 6 — the factor of two
        two = VGroup(
            Text("the factor of 2 = comparing against N different", font_size=24, color=WHITE),
            Text("leave-out models instead of one fixed model", font_size=24, color=WHITE),
            Text("each comparison can be unlucky in two directions", font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.22).next_to(count, DOWN, buff=0.5)
        self.play_beat(FadeIn(two, lag_ratio=0.25))                                # beat 6

        # beat 7 — guarantee, not prediction
        self.play(FadeOut(VGroup(count, two)), run_time=0.5)
        gp = VGroup(
            MathTex(r"1-2\alpha", r"\ :\ \text{worst-case GUARANTEE}").scale(1.0),
            MathTex(r"\approx 1-\alpha", r"\ :\ \text{coverage in PRACTICE}").scale(1.0),
        ).arrange(DOWN, buff=0.45).shift(UP * 0.9)
        gp[0][0].set_color(RES); gp[1][0].set_color(BACK)
        self.play_beat(FadeIn(gp, lag_ratio=0.3))                                  # beat 7

        # beat 8 — report it honestly
        honest = MathTex(r"\alpha = 0.05", r"\ \Rightarrow\ ", "1-2\\alpha", "=",
                         r"0.90\ \ (\geq 90\%)").scale(1.0)
        honest[2].set_color(RES); honest[4].set_color(RES)
        honest.next_to(gp, DOWN, buff=0.7)
        dont = Text("don't quote one minus alpha as if it were guaranteed",
                    font_size=23, color=BAD).next_to(honest, DOWN, buff=0.3)
        self.play_beat(Write(honest), FadeIn(dont))                                # beat 8

    def _matrix_grid(self):
        cells = VGroup()
        n = 4
        for r in range(n):
            for c in range(n):
                col = EIG if r == c else DIM
                op = 0.22 if r == c else 0.08
                sq = Square(side_length=0.55, stroke_color=col, stroke_width=1.5,
                            fill_color=col, fill_opacity=op)
                sq.move_to(RIGHT * c * 0.6 + DOWN * r * 0.6)
                cells.add(sq)
        cells.move_to(ORIGIN)
        return cells


# ----------------------------------------------------------------------
# Scene 4 — CV+
# ----------------------------------------------------------------------
class S4_CVPlus(NarratedScene):
    scene_key = "S4_CVPlus"

    def construct(self):
        self.header("CV+  (the K-fold cousin)")

        # beat 1 — motivation: N refits is a lot
        motiv = VGroup(
            Text("N refits is a lot when each fit is a", font_size=26, color=WHITE),
            Text("voxelwise regression", font_size=26, color=DIM),
            Text("CV+ : the same idea with K folds instead of N", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.6)
        self.play_beat(FadeIn(motiv, lag_ratio=0.25))                              # beat 1

        # beat 2 — partition into K folds
        self.play(FadeOut(motiv), run_time=0.4)
        folds = VGroup(*[self._fold(k) for k in range(5)]).arrange(RIGHT, buff=0.3)
        folds.shift(UP * 1.4)
        fold_cap = Text("partition into K equal folds; refit K times,\neach time leaving out one whole fold",
                        font_size=23, color=DIM, line_spacing=0.8).next_to(folds, DOWN, buff=0.4)
        self.play_beat(FadeIn(folds, lag_ratio=0.2), FadeIn(fold_cap))             # beat 2

        # beat 3 — N scores from K fits
        deal = MathTex(r"N\ \text{honest scores}", r"\ \ \text{from only}\ \ ",
                       r"K\ \text{fits}").scale(1.05)
        deal[0].set_color(BACK); deal[2].set_color(RES)
        deal.next_to(fold_cap, DOWN, buff=0.5)
        self.play_beat(Write(deal))                                                # beat 3

        # beat 4 — formal score
        self.play(FadeOut(VGroup(folds, fold_cap, deal)), run_time=0.5)
        sc = MathTex(r"R_i^{\text{CV}}", "=",
                     "s\\big(", "X_i,", "Y_i", ";", r"\hat\mu_{-S_{k(i)}}", r"\big)").scale(1.05)
        sc[0].set_color(EIG); sc[3].set_color(VAR); sc[4].set_color(VAR); sc[6].set_color(VAR)
        sc.shift(UP * 1.2)
        sc_b = Brace(sc[6], DOWN, color=VAR)
        sc_lab = Text("model fit on all folds EXCEPT the one containing i",
                      font_size=22, color=VAR).next_to(sc_b, DOWN, buff=0.2)
        self.play_beat(Write(sc), GrowFromCenter(sc_b), FadeIn(sc_lab))            # beat 4

        # beat 5 — structurally identical set
        same = Text("the prediction set is structurally identical to jackknife+\n"
                    "swap the leave-one-out fit for the leave-one-fold-out fit",
                    font_size=24, color=WHITE, line_spacing=0.8).next_to(sc_lab, DOWN, buff=0.5)
        self.play_beat(FadeIn(same, shift=UP * 0.2))                               # beat 5

        # beat 6 — same guarantee
        self.play(FadeOut(VGroup(sc, sc_b, sc_lab, same)), run_time=0.5)
        thm = MathTex(r"\Pr\big(", "Y_{n+1}", r"\in", r"C_\alpha", r"\big)",
                      r"\ \geq\ ", "1-2\\alpha").scale(1.2).shift(UP * 0.9)
        thm[1].set_color(VAR); thm[3].set_color(BACK); thm[6].set_color(RES)
        thm_cap = Text("the SAME floor as jackknife+ — shares its theorem",
                       font_size=24, color=DIM).next_to(thm, DOWN, buff=0.35)
        self.play_beat(Write(thm), FadeIn(thm_cap))                                # beat 6

        # beat 7 — K=N vs K=10
        tradeoff = VGroup(
            MathTex(r"K = N", r"\ \Rightarrow\ \text{recover jackknife+}").scale(0.95),
            MathTex(r"K = 10", r"\ \Rightarrow\ \text{a tenth of the work, little sharpness lost}").scale(0.95),
        ).arrange(DOWN, buff=0.4).next_to(thm_cap, DOWN, buff=0.6)
        tradeoff[0][0].set_color(VAR); tradeoff[1][0].set_color(RES)
        self.play_beat(FadeIn(tradeoff, lag_ratio=0.3))                            # beat 7

    def _fold(self, k):
        box = RoundedRectangle(width=1.0, height=0.7, corner_radius=0.1,
                               stroke_color=VAR, stroke_width=2,
                               fill_color=VAR, fill_opacity=0.12)
        t = Text(f"S{k+1}", font_size=20, color=VAR).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 5 — The trade-off
# ----------------------------------------------------------------------
class S5_Tradeoff(NarratedScene):
    scene_key = "S5_Tradeoff"

    def construct(self):
        self.header("The trade-off")

        # beat 1 — split is cheap, exact 1-alpha
        col_split = VGroup(
            Text("SPLIT", font_size=28, color=EIG),
            Text("one fit — cheap", font_size=22, color=DIM),
            MathTex(r"\text{exact } 1-\alpha").scale(0.9).set_color(BACK),
        ).arrange(DOWN, buff=0.22).shift(LEFT * 3.3 + UP * 1.0)
        self.play_beat(FadeIn(col_split, lag_ratio=0.3))                           # beat 1

        # beat 2 — but data-hungry
        hungry = Text("but data-hungry: spends a calibration set,\nand at rare-event sizes spends the WRONG data",
                      font_size=23, color=BAD, line_spacing=0.8)
        hungry.next_to(col_split, DOWN, buff=0.5).shift(RIGHT * 3.3)
        self.play_beat(FadeIn(hungry, shift=UP * 0.2))                             # beat 2

        # beat 3 — jackknife+/CV+ use all N
        self.play(FadeOut(hungry), run_time=0.4)
        col_jk = VGroup(
            Text("JACKKNIFE+ / CV+", font_size=26, color=RES),
            Text("uses ALL N patients", font_size=22, color=BACK),
            Text("the outlier widens the set,\nrather than being discarded",
                 font_size=21, color=DIM, line_spacing=0.8),
        ).arrange(DOWN, buff=0.22).shift(RIGHT * 3.3 + UP * 1.0)
        self.play_beat(FadeIn(col_jk, lag_ratio=0.3))                              # beat 3

        # beat 4 — the price
        price = MathTex(r"\text{floor } 1-2\alpha", r"\ \ (\text{not } 1-\alpha),",
                        r"\ \ N\ \text{or}\ K\ \text{fits}").scale(0.95)
        price[0].set_color(RES)
        price.next_to(VGroup(col_split, col_jk), DOWN, buff=0.7)
        self.play_beat(Write(price))                                               # beat 4

        # beat 5 — when to use split
        self.play(FadeOut(VGroup(col_split, col_jk, price)), run_time=0.5)
        use_split = VGroup(
            Text("Use SPLIT when:", font_size=27, color=EIG),
            Text("N is comfortably large", font_size=25, color=WHITE),
            Text("AND the event-positive count is adequate", font_size=25, color=WHITE),
            Text("→  exact statement + low cost win", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT).shift(UP * 0.6)
        self.play_beat(FadeIn(use_split, lag_ratio=0.2))                           # beat 5

        # beat 6 — otherwise jackknife+/CV+
        self.play(FadeOut(use_split), run_time=0.4)
        use_jk = VGroup(
            Text("Otherwise (the sizes we face):", font_size=27, color=RES),
            Text("jackknife+, or CV+ with K = 10", font_size=25, color=WHITE),
            MathTex(r"\text{same guarantee: } 1-2\alpha").scale(0.95).set_color(RES),
        ).arrange(DOWN, buff=0.28).shift(UP * 0.8)
        self.play_beat(FadeIn(use_jk, lag_ratio=0.25))                             # beat 6

        # beat 7 — don't cross the wires
        wires = VGroup(
            Text("Don't cross the wires:", font_size=25, color=BAD),
            MathTex(r"1-2\alpha", r"\ :\ \text{the RESIDUAL theorem}").scale(0.9),
            MathTex(r"1-\alpha", r"\ :\ \text{still exact for a split CLASSIFICATION score}").scale(0.9),
        ).arrange(DOWN, buff=0.25).next_to(use_jk, DOWN, buff=0.6)
        wires[1][0].set_color(RES); wires[2][0].set_color(BACK)
        self.play_beat(FadeIn(wires, lag_ratio=0.25))                              # beat 7
