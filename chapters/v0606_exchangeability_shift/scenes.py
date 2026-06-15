"""v0606_exchangeability_shift — "Exchangeability and distribution shift".

Five narrated scenes for Volume 6 (Conformal Prediction for CircuitPyPer):
  S1_Assumption  exchangeability is load-bearing; uniform rank => coverage; break it
  S2_Covariate   covariate shift P(X) moves, P(Y|X) fixed; the weight w(x)=q/p
  S3_Weighted    weighted conformal: normalized p_i, the weighted quantile, coverage restored
  S4_Unknown     weights estimated => effective N collapses; label shift has no free lunch
  S5_Tie         conformal & permutation both rest on a symmetry; break it, lose the guarantee

All equations/claims come from:
  volumes/vol6_conformal/chapters/06_exchangeability_shift.md
  (weighted conformal: Tibshirani, Barber, Candes & Ramdas 2019)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0606_exchangeability_shift ./render.sh \
      chapters/v0606_exchangeability_shift/scenes.py -q ql \
      S1_Assumption S2_Covariate S3_Weighted S4_Unknown S5_Tie
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Exchangeability is load-bearing
# ----------------------------------------------------------------------
class S1_Assumption(NarratedScene):
    scene_key = "S1_Assumption"

    def construct(self):
        self.header("Exchangeability is load-bearing")

        intro = Text("every guarantee here rested on ONE word",
                     font_size=28, color=DIM).shift(UP * 2.5)
        word = Text("exchangeability", font_size=40, color=RES)\
            .next_to(intro, DOWN, buff=0.35)
        self.play_beat(FadeIn(intro), Write(word))                          # beat 1

        # the patient pair Z_i = (X_i, Y_i)
        self.play(FadeOut(VGroup(intro, word)), run_time=0.4)
        zi = MathTex("Z_i", "=", "(", "X_i", ",", "Y_i", ")").scale(1.3).shift(UP * 1.7)
        zi[0].set_color(VAR); zi[3].set_color(VAR); zi[5].set_color(EIG)
        brace_x = Brace(zi[3], DOWN, color=VAR)
        x_lab = Text("features: lesion size, position, covariates",
                     font_size=20, color=VAR).next_to(brace_x, DOWN, buff=0.15)
        brace_y = Brace(zi[5], UP, color=EIG)
        y_lab = Text("outcome:  AE-minus  or  AE-plus",
                     font_size=20, color=EIG).next_to(brace_y, UP, buff=0.15)
        self.play_beat(Write(zi), GrowFromCenter(brace_x), FadeIn(x_lab),
                       GrowFromCenter(brace_y), FadeIn(y_lab))               # beat 2

        # exchangeability: invariance under permutation
        self.play(FadeOut(VGroup(brace_x, x_lab, brace_y, y_lab)),
                  zi.animate.scale(0.6).to_edge(UP, buff=1.0), run_time=0.5)
        exch = MathTex(r"(Z_1,\dots,Z_{n+1})", r"\;\stackrel{d}{=}\;",
                       r"(Z_{\pi(1)},\dots,Z_{\pi(n+1)})").scale(1.0).shift(UP * 0.7)
        exch[0].set_color(VAR); exch[2].set_color(VAR)
        exch_cap = Text("the joint law is invariant under every permutation pi",
                        font_size=23, color=DIM).next_to(exch, DOWN, buff=0.3)
        self.play_beat(Write(exch), FadeIn(exch_cap))                       # beat 3

        # uniform rank  (label s_{n+1}: the strangeness / nonconformity score)
        rank = MathTex(r"\text{rank}(s_{n+1})", r"\ \sim\ ",
                       r"\text{Uniform}\{1,\dots,n+1\}").scale(0.95)
        rank[0].set_color(VAR); rank[2].set_color(BACK)
        rank.next_to(exch_cap, DOWN, buff=0.6)
        b_s = Brace(rank[0], DOWN, color=VAR)
        s_lab = Text("s : the new patient's strangeness (nonconformity) score",
                     font_size=19, color=VAR).next_to(b_s, DOWN, buff=0.12)
        self.play_beat(Write(rank), GrowFromCenter(b_s), FadeIn(s_lab))     # beat 4

        # the coverage band that follows  (label alpha: the miscoverage level)
        self.play(FadeOut(VGroup(b_s, s_lab)), run_time=0.3)
        band = MathTex(r"1-\alpha", r"\ \le\ ",
                       r"\Pr\big(Y_{n+1}\in C(X_{n+1})\big)", r"\ <\ ",
                       r"1-\alpha+\tfrac{1}{n+1}").scale(0.85)
        band[0].set_color(RES); band[2].set_color(WHITE); band[4].set_color(RES)
        band.next_to(rank, DOWN, buff=0.45)
        box = SurroundingRectangle(band, color=RES, buff=0.16)
        a_lab = Text("alpha : the miscoverage level (alpha = 0.1 gives the 90% target)",
                     font_size=18, color=DIM).next_to(box, DOWN, buff=0.15)
        self.play_beat(Write(band), Create(box), FadeIn(a_lab))            # beat 5

        # break it: a stranger new patient
        self.play(FadeOut(VGroup(zi, exch, exch_cap, rank, band, box, a_lab)),
                  run_time=0.5)
        break1 = VGroup(
            Text("calibrate at a GENTLE site,  deploy where lesions are BIGGER",
                 font_size=25, color=WHITE),
            Text("the next patient is systematically STRANGER",
                 font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.4)
        self.play_beat(FadeIn(break1[0]), FadeIn(break1[1], shift=UP * 0.2))  # beat 6

        broken = MathTex(r"\text{rank not uniform}", r"\ \Rightarrow\ ",
                         r"1-\alpha\ \text{lost}", r"\ \Rightarrow\ ",
                         r"\text{coverage} \in [0,1]").scale(0.85)
        broken[0].set_color(BAD); broken[2].set_color(BAD); broken[4].set_color(BAD)
        broken.next_to(break1, DOWN, buff=0.6)
        self.play_beat(Write(broken))                                      # beat 7

        silent = VGroup(
            Text("nothing crashes — the sets still print,", font_size=25, color=DIM),
            Text("calibration still says 90%.  the failure is SILENT.",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.25).next_to(broken, DOWN, buff=0.55)
        self.play_beat(FadeIn(silent, lag_ratio=0.3))                      # beat 8


# ----------------------------------------------------------------------
# Scene 2 — Covariate shift
# ----------------------------------------------------------------------
class S2_Covariate(NarratedScene):
    scene_key = "S2_Covariate"

    def construct(self):
        self.header("Covariate shift")

        intro = Text("two distinct things can shift — name them apart",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # P(X) changes, P(Y|X) fixed
        defn = MathTex(r"P(X)", r"\ \text{changes,}\quad", r"P(Y\mid X)",
                       r"\ \text{fixed}").scale(1.15).shift(UP * 1.2)
        defn[0].set_color(BAD); defn[2].set_color(BACK)
        b_px = Brace(defn[0], DOWN, color=BAD)
        px_lab = Text("the feature mixture moves", font_size=21, color=BAD)\
            .next_to(b_px, DOWN, buff=0.15)
        b_pyx = Brace(defn[2], DOWN, color=BACK)
        pyx_lab = Text("the rule features->risk holds", font_size=21, color=BACK)\
            .next_to(b_pyx, DOWN, buff=0.15)
        self.play_beat(Write(defn), intro.animate.set_opacity(0.4))        # beat 2

        self.play_beat(GrowFromCenter(b_px), FadeIn(px_lab),
                       GrowFromCenter(b_pyx), FadeIn(pyx_lab))             # beat 3

        # wrong mixture
        self.play(FadeOut(VGroup(intro, defn, b_px, px_lab, b_pyx, pyx_lab)),
                  run_time=0.5)
        wrong = VGroup(
            Text("so your calibration set is the WRONG mixture:",
                 font_size=26, color=WHITE),
            Text("too many small lesions, too few big ones",
                 font_size=26, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.7)
        self.play_beat(FadeIn(wrong[0]), FadeIn(wrong[1], shift=UP * 0.2))  # beat 4

        # the repair: w(x)
        repair = Text("repair: reweight each calibration patient by  w(x)",
                      font_size=26, color=RES).next_to(wrong, DOWN, buff=0.5)
        self.play_beat(FadeIn(repair))                                     # beat 5

        # decode w(x) = q/p
        wx = MathTex("w", "(", "x", ")", "=", r"\frac{q_X(x)}{p_X(x)}")\
            .scale(1.4).next_to(repair, DOWN, buff=0.55)
        wx[0].set_color(RES)
        b_q = Brace(wx[5], RIGHT, color=BACK)
        q_lab = VGroup(
            Text("q : deployment density", font_size=20, color=BACK),
            Text("p : calibration density", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).next_to(b_q, RIGHT, buff=0.15)
        self.play_beat(Write(wx), GrowFromCenter(b_q), FadeIn(q_lab))      # beat 6

        # up/down weight
        ud = VGroup(
            Text("common at the new site, rare in calibration  ->  UP-weight",
                 font_size=23, color=BACK),
            Text("the reverse  ->  DOWN-weight",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(wx, DOWN, buff=0.55)
        self.play_beat(FadeIn(ud[0]), FadeIn(ud[1]))                       # beat 7

        # why it is repairable
        self.play(FadeOut(VGroup(wrong, repair, wx, b_q, q_lab, ud)),
                  run_time=0.5)
        why = VGroup(
            Text("repairable BECAUSE:", font_size=27, color=RES),
            Text("the part that broke (the feature distribution) is observable",
                 font_size=25, color=WHITE),
            Text("the part you trust (the conditional risk) is held fixed",
                 font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.play_beat(FadeIn(why, lag_ratio=0.3))                        # beat 8


# ----------------------------------------------------------------------
# Scene 3 — Weighted conformal
# ----------------------------------------------------------------------
class S3_Weighted(NarratedScene):
    scene_key = "S3_Weighted"

    def construct(self):
        self.header("Weighted conformal  (Tibshirani et al. 2019)")

        intro = Text("weighted conformal prediction puts that idea to work",
                     font_size=27, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # uniform weight
        unif = MathTex(r"\text{plain:}\quad", r"\text{every vote}", "=",
                       r"\tfrac{1}{n+1}").scale(1.1).shift(UP * 1.5)
        unif[1].set_color(DIM); unif[3].set_color(DIM)
        self.play_beat(Write(unif), intro.animate.set_opacity(0.4))        # beat 2

        # normalized weights p_i
        pi = MathTex("p_i", "=", r"\frac{w(X_i)}{\sum_{j=1}^{n} w(X_j) + w(x)}")\
            .scale(1.15).next_to(unif, DOWN, buff=0.6)
        pi[0].set_color(RES)
        b_pi = Brace(pi[2], DOWN, color=RES)
        pi_lab = Text("each patient's weight over the total weight",
                      font_size=21, color=RES).next_to(b_pi, DOWN, buff=0.15)
        self.play_beat(Write(pi), GrowFromCenter(b_pi), FadeIn(pi_lab))    # beat 3

        # the new patient's own share
        self.play(FadeOut(VGroup(b_pi, pi_lab)), run_time=0.3)
        pnp = MathTex("p_{n+1}", "=", r"\frac{w(x)}{\sum_{j=1}^{n} w(X_j) + w(x)}")\
            .scale(1.05).next_to(pi, DOWN, buff=0.5)
        pnp[0].set_color(EIG)
        self.play_beat(Write(pnp))                                        # beat 4

        # weighted quantile
        self.play(FadeOut(VGroup(intro, unif, pi, pnp)), run_time=0.5)
        qhat = MathTex(r"\hat q_w(x)", "=",
                       r"\inf\Big\{t:\ \sum_{i=1}^{n} p_i\,\mathbf 1\{s_i\le t\}",
                       r"\ \ge\ ", r"1-\alpha - p_{n+1}\Big\}").scale(0.85)\
            .shift(UP * 1.5)
        qhat[0].set_color(RES); qhat[4].set_color(EIG)
        qcap = Text("smallest threshold whose weighted score-mass, plus p(n+1),\nreaches one-minus-alpha",
                    font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(qhat, DOWN, buff=0.35)
        sym = Text("s_i : calibration score    1{s_i <= t} : 1 if that score is at or below the threshold t",
                   font_size=18, color=DIM).next_to(qcap, DOWN, buff=0.2)
        self.play_beat(Write(qhat), FadeIn(qcap), FadeIn(sym))            # beat 5

        # why: rank-k probability is p_k
        rankp = MathTex(r"\Pr(\text{test at rank } k)", "=", "p_k")\
            .scale(1.05).next_to(qcap, DOWN, buff=0.6)
        rankp[0].set_color(VAR); rankp[2].set_color(RES)
        rcap = Text("not uniform — weighted by how representative point k is",
                    font_size=22, color=DIM).next_to(rankp, DOWN, buff=0.25)
        self.play_beat(Write(rankp), FadeIn(rcap))                        # beat 6

        # floor comes back
        self.play(FadeOut(VGroup(qhat, qcap, rankp, rcap, sym)), run_time=0.5)
        floor = Text("run the same below-threshold calculation with those\nnon-uniform rank probabilities  ->  the floor comes back",
                     font_size=26, color=WHITE, line_spacing=0.8).shift(UP * 1.4)
        self.play_beat(FadeIn(floor, shift=UP * 0.2))                     # beat 7

        # collapse to plain conformal
        collapse = MathTex(r"w\equiv 1", r"\ \Rightarrow\ ",
                           r"p_i = \tfrac{1}{n+1}", r"\ \Rightarrow\ ",
                           r"\text{plain split conformal}").scale(0.9)
        collapse[0].set_color(DIM); collapse[2].set_color(DIM); collapse[4].set_color(BACK)
        collapse.next_to(floor, DOWN, buff=0.6)
        self.play_beat(Write(collapse))                                   # beat 8

        # the guarantee
        guar = MathTex(r"\Pr_{Q}\big(Y_{n+1}\in C(X_{n+1})\big)", r"\ \ge\ ",
                       r"1-\alpha").scale(1.05).next_to(collapse, DOWN, buff=0.55)
        guar[0].set_color(WHITE); guar[2].set_color(RES)
        gbox = SurroundingRectangle(guar, color=RES, buff=0.18)
        self.play_beat(Write(guar), Create(gbox))                         # beat 9


# ----------------------------------------------------------------------
# Scene 4 — When weights are unknown
# ----------------------------------------------------------------------
class S4_Unknown(NarratedScene):
    scene_key = "S4_Unknown"

    def construct(self):
        self.header("When weights are unknown")

        caveat = VGroup(
            Text("the honest caveat:", font_size=28, color=RES),
            Text("you do not KNOW w — you estimate q over p from data",
                 font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.25).shift(UP * 2.0)
        self.play_beat(FadeIn(caveat[0]), FadeIn(caveat[1], shift=UP * 0.2))  # beat 1

        degrade = Text("estimation error in w degrades the guarantee —\nworst when the two densities barely overlap",
                       font_size=25, color=BAD, line_spacing=0.8)\
            .next_to(caveat, DOWN, buff=0.5)
        self.play_beat(FadeIn(degrade))                                   # beat 2

        collapse = Text("then a few patients carry almost all the weight,\nand the effective sample size collapses toward 1",
                        font_size=25, color=BAD, line_spacing=0.8)\
            .next_to(degrade, DOWN, buff=0.45)
        self.play_beat(FadeIn(collapse, shift=UP * 0.2))                  # beat 3

        # the effective N formula
        self.play(FadeOut(VGroup(caveat, degrade, collapse)), run_time=0.5)
        neff = MathTex(r"n_{\text{eff}}", "=",
                       r"\frac{\big(\sum_i w(X_i)\big)^2}{\sum_i w(X_i)^2}")\
            .scale(1.3).shift(UP * 1.3)
        neff[0].set_color(RES)
        self.play_beat(Write(neff))                                       # beat 4

        single = Text("a single-digit effective N  =  one or two patients\nof evidence wearing a theorem",
                      font_size=25, color=BAD, line_spacing=0.8)\
            .next_to(neff, DOWN, buff=0.55)
        self.play_beat(FadeIn(single, shift=UP * 0.2))                    # beat 5

        # the deeper limit: label shift
        self.play(FadeOut(VGroup(neff, single)), run_time=0.5)
        limit = VGroup(
            Text("a deeper limit:", font_size=28, color=RES),
            Text("weighted conformal fixes COVARIATE shift only —",
                 font_size=26, color=WHITE),
            Text("it does nothing for LABEL shift",
                 font_size=26, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.6)
        self.play_beat(FadeIn(limit, lag_ratio=0.3))                      # beat 6

        labelshift = MathTex(r"\text{label shift:}\quad", r"P(Y\mid X)",
                             r"\ \neq\ ", r"Q(Y\mid X)").scale(1.0)
        labelshift[1].set_color(BAD); labelshift[3].set_color(BAD)
        labelshift.next_to(limit, DOWN, buff=0.55)
        ls_cap = Text("the same features carry a DIFFERENT risk — the rule moved",
                      font_size=22, color=DIM).next_to(labelshift, DOWN, buff=0.25)
        self.play_beat(Write(labelshift), FadeIn(ls_cap))                 # beat 7

        nfl = Text("no free lunch: no reweighting recovers a rule you no longer\nknow.  get new-regime data.",
                   font_size=26, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.6)
        self.play_beat(FadeIn(nfl, shift=UP * 0.2))                       # beat 8


# ----------------------------------------------------------------------
# Scene 5 — Tie to permutation tests
# ----------------------------------------------------------------------
class S5_Tie(NarratedScene):
    scene_key = "S5_Tie"

    def construct(self):
        self.header("Tie to permutation tests")

        intro = Text("the same lesson we met across the whole series",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # conformal rests on exchangeability
        conf = VGroup(
            Text("CONFORMAL", font_size=26, color=VAR),
            Text("the n+1 patients are shuffleable\nwithout changing the joint law",
                 font_size=23, color=WHITE, line_spacing=0.8),
        ).arrange(DOWN, buff=0.2).shift(LEFT * 3.4 + UP * 0.8)
        self.play_beat(FadeIn(conf, shift=UP * 0.2))                      # beat 2

        # permutation rests on the same symmetry
        perm = VGroup(
            Text("PERMUTATION", font_size=26, color=BACK),
            Text("the labels are exchangeable\nunder the null",
                 font_size=23, color=WHITE, line_spacing=0.8),
        ).arrange(DOWN, buff=0.2).shift(RIGHT * 3.4 + UP * 0.8)
        link = MathTex(r"\Longleftrightarrow", color=RES).scale(1.2)\
            .move_to(midpoint(conf.get_right(), perm.get_left()))
        self.play_beat(FadeIn(perm, shift=UP * 0.2), Write(link))         # beat 3

        # ranks -> guarantee
        ranks = Text("in both: a symmetry license lets you reason about RANKS,\nand from ranks comes the guarantee",
                     font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(VGroup(conf, perm), DOWN, buff=0.7)
        self.play_beat(FadeIn(ranks, shift=UP * 0.2))                     # beat 4

        # break the symmetry, lose the guarantee
        self.play(FadeOut(VGroup(intro, conf, perm, link, ranks)),
                  run_time=0.5)
        breakit = VGroup(
            Text("break the symmetry  ->  lose the guarantee", font_size=30, color=BAD),
            Text("a distribution shift HERE  =  the wrong permutation scheme THERE",
                 font_size=25, color=DIM),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.5)
        self.play_beat(FadeIn(breakit[0]), FadeIn(breakit[1], shift=UP * 0.2))  # beat 5

        # same crack two faces
        faces = VGroup(
            Text("same crack, two faces:", font_size=26, color=RES),
            Text("conformal  ->  the fix is calibration", font_size=24, color=VAR),
            Text("permutation  ->  the fix is the right exchangeable null",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).next_to(breakit, DOWN, buff=0.55)
        self.play_beat(FadeIn(faces, lag_ratio=0.3))                      # beat 6

        # order of operations
        self.play(FadeOut(VGroup(breakit, faces)), run_time=0.5)
        order = Text("order of operations: MEASURE the shift first,\nthen repair only what is covariate and known",
                     font_size=27, color=WHITE, line_spacing=0.8).shift(UP * 1.2)
        self.play_beat(FadeIn(order, shift=UP * 0.2))                     # beat 7

        moral = VGroup(
            Text("Honor the symmetry — the promise is exact.", font_size=28, color=BACK),
            Text("Break it quietly — the number is just a costume.", font_size=28, color=BAD),
        ).arrange(DOWN, buff=0.35).next_to(order, DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, lag_ratio=0.4))                      # beat 8
