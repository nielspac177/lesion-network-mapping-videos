"""v0609_conformal_for_lnm — "Conformal prediction for lesion-to-outcome".

Six narrated scenes. Closes the LNM series. Conformal prediction wraps any L N M
predictor and returns a prediction SET for one patient's outcome y_i, with a
distribution-free, finite-sample coverage guarantee (K1). We decode the
nonconformity score, draw the split-conformal set, race the residualized-map
predictor against the degree+size baseline on SHARPNESS (Part 8 Move 3), then
state the one price (exchangeability / distribution shift) and synthesize with
the e-value guarantee from Vol 5.

All equations/numbers are quoted from:
  volumes/vol6_conformal/chapters/01_the_guarantee.md
  responses/lnm_critique/sections/06_single_target.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0609_conformal_for_lnm ./render.sh \
      chapters/v0609_conformal_for_lnm/scenes.py -q ql \
      S1_Task S2_Score S3_Set S4_BeatBaseline S5_Exchange S6_Synthesis
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the prediction task
# ----------------------------------------------------------------------
class S1_Task(NarratedScene):
    scene_key = "S1_Task"

    def construct(self):
        self.header("The prediction task")

        ask = VGroup(
            Text("The bedside question:", font_size=28, color=RES),
            Text("what is THIS patient's outcome,", font_size=26, color=WHITE),
            Text("and how much should I trust the number?", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.4)
        self.play_beat(FadeIn(ask, lag_ratio=0.3))                          # beat 1
        self.play(FadeOut(ask), run_time=0.4)

        # lesion indicator l_i
        ell = MathTex(r"\ell_i", r"\in", r"\{0,1\}^{V}").scale(1.3).shift(UP * 1.4)
        ell[0].set_color(VAR)
        brace_l = Brace(ell, DOWN, color=VAR)
        l_lab = Text("lesion indicator: 1 at destroyed voxels, else 0",
                     font_size=22, color=VAR).next_to(brace_l, DOWN, buff=0.2)
        self.play_beat(Write(ell), GrowFromCenter(brace_l), FadeIn(l_lab))  # beat 2

        # m_i = C l_i
        self.play(FadeOut(VGroup(brace_l, l_lab)),
                  ell.animate.scale(0.7).to_edge(UP, buff=1.05), run_time=0.5)
        m_eq = MathTex("m_i", "=", "C", r"\ell_i").scale(1.4).shift(UP * 0.7)
        m_eq[0].set_color(VAR); m_eq[2].set_color(WHITE); m_eq[3].set_color(VAR)
        m_cap = Text("the seed pushed through the normative connectome C\n= patient i's lesion network map",
                     font_size=22, color=DIM, line_spacing=0.8).next_to(m_eq, DOWN, buff=0.4)
        self.play_beat(Write(m_eq), FadeIn(m_cap))                          # beat 3

        # the pair Z_i = (x_i, y_i)
        self.play(FadeOut(VGroup(m_cap, ell)),
                  m_eq.animate.scale(0.7).to_edge(UP, buff=1.05), run_time=0.5)
        pair = MathTex("Z_i", "=", "(", "x_i", ",", "y_i", ")").scale(1.3).shift(UP * 0.8)
        pair[3].set_color(VAR); pair[5].set_color(EIG)
        bx = Brace(pair[3], DOWN, color=VAR)
        bx_l = Text("features from the map", font_size=20, color=VAR).next_to(bx, DOWN, buff=0.15)
        by = Brace(pair[5], DOWN, color=EIG)
        by_l = Text("outcome: e.g. ataxia", font_size=20, color=EIG).next_to(by, DOWN, buff=0.15)
        by_l.shift(RIGHT * 0.1)
        self.play_beat(Write(pair), GrowFromCenter(bx), FadeIn(bx_l),
                       GrowFromCenter(by), FadeIn(by_l))                    # beat 4

        # point estimate is weak
        self.play(FadeOut(VGroup(bx, bx_l, by, by_l)), run_time=0.4)
        pt = VGroup(
            Text("A plain predictor returns a POINT:", font_size=25, color=WHITE),
            MathTex(r"\hat{y} = 0.23", color=DIM).scale(1.1),
            Text("at N in the tens, that number leans on an\nasymptotic story your sample cannot honor",
                 font_size=22, color=BAD, line_spacing=0.8),
        ).arrange(DOWN, buff=0.25).next_to(pair, DOWN, buff=0.6)
        self.play_beat(FadeIn(pt, lag_ratio=0.3))                          # beat 5

        # we want a SET with a guarantee
        self.play(FadeOut(VGroup(pair, pt)), run_time=0.5)
        want = VGroup(
            Text("We want a prediction SET", font_size=30, color=RES),
            Text("with a coverage guarantee", font_size=30, color=RES),
            Text("the truth lands inside it a stated fraction of the time",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.28)
        self.play_beat(FadeIn(want, lag_ratio=0.3))                        # beat 6


# ----------------------------------------------------------------------
# Scene 2 — a nonconformity score for outcomes
# ----------------------------------------------------------------------
class S2_Score(NarratedScene):
    scene_key = "S2_Score"

    def construct(self):
        self.header("A nonconformity score for outcomes")

        intro = Text("a single number: how STRANGE each patient looks",
                     font_size=27, color=DIM).shift(UP * 2.3)
        self.play_beat(FadeIn(intro))                                      # beat 1

        score = MathTex("s_i", "=", r"\big|", "y_i", "-", r"\hat{y}(m_i)", r"\big|")\
            .scale(1.4).shift(UP * 0.8)
        score[0].set_color(RES); score[3].set_color(EIG); score[5].set_color(VAR)
        self.play_beat(Write(score), intro.animate.set_opacity(0.4))       # beat 2

        # decode each symbol
        b_y = Brace(score[3], DOWN, color=EIG)
        y_l = Text("true outcome", font_size=21, color=EIG).next_to(b_y, DOWN, buff=0.15)
        b_yh = Brace(score[5], DOWN, color=VAR)
        yh_l = Text("model's prediction from the map", font_size=21, color=VAR)\
            .next_to(b_yh, DOWN, buff=0.15)
        self.play_beat(GrowFromCenter(b_y), FadeIn(y_l),
                       GrowFromCenter(b_yh), FadeIn(yh_l))                  # beat 3

        # small vs large
        self.play(FadeOut(VGroup(b_y, y_l, b_yh, yh_l, intro)), run_time=0.4)
        rng = VGroup(
            Text("small  s  →  model nailed it", font_size=25, color=BACK),
            Text("large  s  →  patient is surprising", font_size=25, color=BAD),
            Text("the score just RANKS patients by surprise", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.25).next_to(score, DOWN, buff=0.7)
        self.play_beat(FadeIn(rng, lag_ratio=0.3))                         # beat 4

        # y-hat can be any model
        self.play(FadeOut(rng), score.animate.scale(0.75).to_edge(UP, buff=1.05),
                  run_time=0.5)
        anymod = VGroup(
            MathTex(r"\hat{y}", r"=", r"\text{ANY L N M predictor}").scale(1.1),
            Text("even the residualized-map model\n(backbone stripped before fitting)",
                 font_size=23, color=DIM, line_spacing=0.8),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.5)
        anymod[0][0].set_color(VAR); anymod[0][2].set_color(WHITE)
        self.play_beat(FadeIn(anymod, lag_ratio=0.3))                      # beat 5

        valid = VGroup(
            Text("Validity does NOT require the model to be correct.",
                 font_size=26, color=RES),
            Text("the guarantee comes from how the scores RANK",
                 font_size=24, color=WHITE),
            Text("you do not have to trust the model", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.25).next_to(anymod, DOWN, buff=0.6)
        self.play_beat(FadeIn(valid, lag_ratio=0.3))                       # beat 6


# ----------------------------------------------------------------------
# Scene 3 — the outcome prediction set
# ----------------------------------------------------------------------
class S3_Set(NarratedScene):
    scene_key = "S3_Set"

    def construct(self):
        self.header("The outcome prediction set")

        # q-hat as a calibration quantile
        step = VGroup(
            Text("Split conformal:", font_size=27, color=RES),
            Text("score every held-out calibration patient,", font_size=24, color=WHITE),
            Text("take a high quantile of the scores  →  q-hat", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.0)
        qh = MathTex(r"\hat{q}", r"=", r"\text{quantile of }\{s_i\}").scale(1.0)\
            .next_to(step, DOWN, buff=0.5)
        qh[0].set_color(RES); qh[2].set_color(DIM)
        self.play_beat(FadeIn(step, lag_ratio=0.3), Write(qh))             # beat 1

        # the set
        self.play(FadeOut(VGroup(step, qh)), run_time=0.4)
        cset = MathTex("C(", "m_{\\text{test}}", ")", "=",
                       r"\hat{y}(m_{\text{test}})", r"\;\pm\;", r"\hat{q}")\
            .scale(1.3).shift(UP * 1.3)
        cset[1].set_color(VAR); cset[4].set_color(VAR); cset[6].set_color(RES)
        self.play_beat(Write(cset))                                        # beat 2

        # number line picture of the set
        line = NumberLine(x_range=[-3, 3, 1], length=8, include_numbers=False,
                          color=DIM).shift(DOWN * 0.6)
        center = Dot(line.n2p(0), color=VAR, radius=0.09)
        c_lab = MathTex(r"\hat{y}", color=VAR).scale(0.9).next_to(center, UP, buff=0.2)
        lo, hi = line.n2p(-1.6), line.n2p(1.6)
        band = Line(lo, hi, color=RES, stroke_width=10).set_opacity(0.55)
        cap_lo = Line(lo + DOWN * 0.18, lo + UP * 0.18, color=RES, stroke_width=4)
        cap_hi = Line(hi + DOWN * 0.18, hi + UP * 0.18, color=RES, stroke_width=4)
        rad = MathTex(r"\hat{q}", color=RES).scale(0.85).next_to(hi, DOWN, buff=0.25)
        self.play_beat(Create(line), FadeIn(band), FadeIn(center), FadeIn(c_lab),
                       Create(cap_lo), Create(cap_hi), FadeIn(rad))        # beat 3

        # radius = typical mistake (kept on the line picture) -> wait beat
        radcap = Text("q-hat = the model's typical mistake on unseen patients",
                      font_size=22, color=DIM).next_to(line, DOWN, buff=0.9)
        self.add(radcap)
        self.wait_beat()                                                   # beat 4

        # the guarantee K1
        self.play(FadeOut(VGroup(cset, line, band, center, c_lab, cap_lo,
                                 cap_hi, rad, radcap)), run_time=0.5)
        k1 = MathTex(r"\Pr\big(", "y", r"\in", "C(m_{\\text{test}})", r"\big)",
                     r"\;\geq\;", "1-\\alpha").scale(1.25).shift(UP * 0.9)
        k1[1].set_color(EIG); k1[3].set_color(RES); k1[6].set_color(BACK)
        k1cap = Text("K1: the true outcome lies in the set\nwith probability at least one minus alpha",
                     font_size=23, color=WHITE, line_spacing=0.8).next_to(k1, DOWN, buff=0.4)
        self.play_beat(Write(k1), FadeIn(k1cap))                           # beat 5

        # alpha = 0.1, distribution-free, two-sided bound
        self.play(FadeOut(k1cap), k1.animate.scale(0.8).to_edge(UP, buff=1.1),
                  run_time=0.5)
        props = VGroup(
            MathTex(r"\alpha = 0.1 \;\Rightarrow\; 90\%\ \text{coverage}").scale(1.0),
            Text("distribution-free   ·   finite-sample   ·   any model",
                 font_size=23, color=BACK),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.2)
        props[0].set_color(WHITE)
        bound = MathTex("1-\\alpha", r"\;\leq\;", r"\text{coverage}", r"\;<\;",
                        "1-\\alpha+\\tfrac{1}{n+1}").scale(0.95)\
            .next_to(props, DOWN, buff=0.5)
        bound[0].set_color(BACK); bound[4].set_color(RES)
        self.play_beat(FadeIn(props, lag_ratio=0.2), Write(bound))         # beat 6

        moral = Text("the wider the set, the less the model knew —\nthe set carries the honesty the point hid",
                     font_size=24, color=RES, line_spacing=0.8).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 4 — compare against the degree baseline (Part 8, Move 3)
# ----------------------------------------------------------------------
class S4_BeatBaseline(NarratedScene):
    scene_key = "S4_BeatBaseline"

    def construct(self):
        self.header("Compare against the degree baseline")

        # valid can be useless
        gamed = VGroup(
            Text("A predictor that returns the WHOLE line", font_size=26, color=WHITE),
            Text("is valid  (truth always inside)  and worthless", font_size=25, color=BAD),
            Text("coverage alone can be gamed by refusing to commit",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.6)
        self.play_beat(FadeIn(gamed, lag_ratio=0.3))                       # beat 1

        # sharpness
        self.play(FadeOut(gamed), run_time=0.4)
        sharp = VGroup(
            Text("So report a SECOND number:", font_size=27, color=RES),
            Text("SHARPNESS  =  how small the sets are", font_size=27, color=RES),
            Text("the honest report is coverage AND mean set width",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.24)
        self.play_beat(FadeIn(sharp, lag_ratio=0.3))                       # beat 2

        # the contest
        self.play(FadeOut(sharp), run_time=0.4)
        contest = VGroup(
            Text("Conformalize BOTH to the same coverage,", font_size=26, color=WHITE),
            Text("then compare set widths — the SHARPER model wins",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.25).to_edge(UP, buff=1.0)
        self.play_beat(FadeIn(contest, lag_ratio=0.3))                     # beat 3

        # model 1 box
        m1 = self._model_box("Model 1 — residualized map",
                             "patient-specific fingerprint,\nbackbone stripped", BACK)
        m1.shift(LEFT * 3.3 + DOWN * 0.6)
        self.play_beat(FadeIn(m1, shift=UP * 0.2))                         # beat 4

        # model 2 box: degree + size baseline
        deg = MathTex(r"\hat{y}^{\,\mathrm{deg}}_i", "=",
                      "a", "+", "b\\,(u_1^\\top \\ell_i)", "+", "c\\,s_i").scale(0.62)
        deg[0].set_color(BAD); deg[4].set_color(BAD); deg[6].set_color(VAR)
        m2 = self._model_box("Model 2 — degree + size", None, BAD, eq=deg)
        m2.shift(RIGHT * 3.3 + DOWN * 0.6)
        self.play_beat(FadeIn(m2, shift=UP * 0.2))                         # beat 5

        # Part 8 Move 3 tie-in
        self.play(FadeOut(VGroup(contest, m1, m2)), run_time=0.5)
        tie = VGroup(
            Text("This is Part 8, Move 3:", font_size=27, color=RES),
            Text("make DEGREE the thing to beat", font_size=27, color=WHITE),
            Text("the critique's worry was maps only recover degree —\nso put degree IN the baseline",
                 font_size=23, color=DIM, line_spacing=0.8),
        ).arrange(DOWN, buff=0.24).shift(UP * 0.3)
        self.play_beat(FadeIn(tie, lag_ratio=0.3))                         # beat 6

        # verdict + rebuttal numbers
        self.play(FadeOut(tie), run_time=0.4)
        verdict = VGroup(
            Text("Tighter intervals at the same coverage", font_size=25, color=WHITE),
            Text("⇒  signal the backbone alone cannot give", font_size=25, color=BACK),
            Text("SHARPNESS is the discriminator", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.1)
        nums = MathTex(r"\text{same-symptom } r=0.44", r"\quad\text{vs}\quad",
                       r"r=0.16 \text{ to degree}").scale(0.85)
        nums[0].set_color(BACK); nums[2].set_color(BAD)
        nums.next_to(verdict, DOWN, buff=0.55)
        ncap = Text("the rebuttal too makes degree the thing to clear",
                    font_size=21, color=DIM).next_to(nums, DOWN, buff=0.25)
        self.play_beat(FadeIn(verdict, lag_ratio=0.3), Write(nums), FadeIn(ncap))  # beat 7

    def _model_box(self, title, body, color, eq=None):
        box = RoundedRectangle(width=5.4, height=2.2, corner_radius=0.15,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.10)
        t = Text(title, font_size=22, color=color).next_to(box.get_top(), DOWN, buff=0.25)
        inner = eq if eq is not None else Text(body, font_size=20, color=WHITE,
                                               line_spacing=0.8)
        inner.move_to(box).shift(DOWN * 0.2)
        return VGroup(box, t, inner)


# ----------------------------------------------------------------------
# Scene 5 — the exchangeability caveat
# ----------------------------------------------------------------------
class S5_Exchange(NarratedScene):
    scene_key = "S5_Exchange"

    def construct(self):
        self.header("The exchangeability caveat")

        price = VGroup(
            Text("Every guarantee has a price.", font_size=28, color=WHITE),
            Text("Conformal's price is exactly ONE assumption:", font_size=26, color=WHITE),
            Text("exchangeability of the patients", font_size=30, color=RES),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.4)
        self.play_beat(FadeIn(price, lag_ratio=0.3))                       # beat 1
        self.play(FadeOut(price), run_time=0.4)

        # order carries no information
        ex = MathTex(r"(Z_1,\dots,Z_{n+1})", r"\;\stackrel{d}{=}\;",
                     r"(Z_{\pi(1)},\dots,Z_{\pi(n+1)})").scale(0.95).shift(UP * 1.3)
        ex[0].set_color(VAR); ex[2].set_color(VAR)
        ex_cap = Text("order carries NO information:\nshuffle the patients, the world looks the same",
                      font_size=23, color=WHITE, line_spacing=0.8).next_to(ex, DOWN, buff=0.4)
        self.play_beat(Write(ex), FadeIn(ex_cap))                          # beat 2

        # includes the new patient, weaker than iid
        self.play(FadeOut(VGroup(ex, ex_cap)), run_time=0.4)
        notes = VGroup(
            Text("weaker than i.i.d.", font_size=25, color=BACK),
            Text("and it must include the NEW patient", font_size=25, color=RES),
            Text("covered only because it is another draw\nfrom the same pot",
                 font_size=23, color=WHITE, line_spacing=0.8),
        ).arrange(DOWN, buff=0.24)
        self.play_beat(FadeIn(notes, lag_ratio=0.3))                       # beat 3

        # different pot = distribution shift
        self.play(FadeOut(notes), run_time=0.4)
        shift = VGroup(
            Text("Different pot  →  assumption BREAKS", font_size=27, color=BAD),
            Text("new scanner   ·   sicker site   ·   drifted technique",
                 font_size=23, color=DIM),
            Text("= distribution shift", font_size=26, color=BAD),
        ).arrange(DOWN, buff=0.24).shift(UP * 0.3)
        self.play_beat(FadeIn(shift, lag_ratio=0.3))                       # beat 4

        # recall v0606
        self.play(FadeOut(shift), run_time=0.4)
        recall = VGroup(
            Text("This is the failure we measured in Vol 6, Ch. 6.", font_size=25, color=WHITE),
            Text("coverage degrades, and conformal will NOT warn you", font_size=24, color=BAD),
            Text("fragile — and about your DATA, not your model", font_size=24, color=RES),
        ).arrange(DOWN, buff=0.24)
        self.play_beat(FadeIn(recall, lag_ratio=0.3))                      # beat 5

        # honest clinical scope
        self.play(FadeOut(recall), run_time=0.4)
        scope = VGroup(
            Text("Honest clinical scope:", font_size=28, color=RES),
            Text("leave-one-site-out coverage", font_size=28, color=WHITE),
            Text("how well does the guarantee survive a genuinely\nnew cohort? — never just the pooled number",
                 font_size=23, color=DIM, line_spacing=0.8),
        ).arrange(DOWN, buff=0.24)
        self.play_beat(FadeIn(scope, lag_ratio=0.3))                       # beat 6


# ----------------------------------------------------------------------
# Scene 6 — synthesis, close the series
# ----------------------------------------------------------------------
class S6_Synthesis(NarratedScene):
    scene_key = "S6_Synthesis"

    def construct(self):
        self.header("Synthesis")

        # one object underneath
        base = MathTex("m_i", "=", "C", r"\ell_i").scale(1.4).shift(UP * 1.4)
        base[0].set_color(VAR); base[2].set_color(WHITE); base[3].set_color(VAR)
        base_cap = Text("everything in the series stands on ONE object",
                        font_size=25, color=DIM).next_to(base, DOWN, buff=0.4)
        self.play_beat(Write(base), FadeIn(base_cap))                      # beat 1

        # two guarantees on top
        self.play(base.animate.scale(0.7).to_edge(UP, buff=1.05),
                  FadeOut(base_cap), run_time=0.5)
        head = Text("two complementary guarantees, two questions",
                    font_size=26, color=WHITE).shift(UP * 0.9)
        self.play_beat(FadeIn(head))                                       # beat 2

        # e-values
        ev = self._pillar("E-values  (Vol 5)",
                          "anytime-valid evidence\nfor a lesion-symptom LINK",
                          "keeps the whole sweep honest", BACK)
        ev.shift(LEFT * 3.4 + DOWN * 0.8)
        self.play_beat(FadeIn(ev, shift=UP * 0.2))                         # beat 3

        # conformal
        cf = self._pillar("Conformal  (Vol 6)",
                          "calibrated prediction SETS\nfor one individual outcome",
                          "covers the truth, says nothing of WHY", RES)
        cf.shift(RIGHT * 3.4 + DOWN * 0.8)
        self.play_beat(FadeIn(cf, shift=UP * 0.2))                         # beat 4

        # complementary not interchangeable
        self.play(FadeOut(VGroup(head, ev, cf)), run_time=0.5)
        comp = VGroup(
            Text("complementary, not interchangeable", font_size=27, color=RES),
            Text("inference NAMES the link  ·  conformal PREDICTS the patient",
                 font_size=24, color=WHITE),
            Text("neither one fixes confounding", font_size=23, color=BAD),
        ).arrange(DOWN, buff=0.24).shift(UP * 0.3)
        self.play_beat(FadeIn(comp, lag_ratio=0.3))                        # beat 5

        # the witness
        self.play(FadeOut(comp), base.animate.set_opacity(0.0), run_time=0.5)
        wit = MathTex(r"\text{ataxia map: }", "16{,}926", r"\ \text{FWE voxels}",
                      r"\quad\text{vs}\quad", "1").scale(0.95).shift(UP * 0.9)
        wit[1].set_color(BACK); wit[4].set_color(BAD)
        wcap = Text("with the right tools the signal survives where a\nmatched cohort gives one voxel — sound method, N-limited answer",
                    font_size=23, color=WHITE, line_spacing=0.8).next_to(wit, DOWN, buff=0.45)
        self.play_beat(Write(wit), FadeIn(wcap))                           # beat 6

        # close
        self.play(FadeOut(VGroup(wit, wcap)), run_time=0.5)
        close = VGroup(
            Text("Two honest guarantees", font_size=32, color=WHITE),
            Text("on one honest object.", font_size=32, color=WHITE),
            Text("Where the series ends — and a dose-controlled study begins.",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(close, lag_ratio=0.3))                       # beat 7

    def _pillar(self, title, body, foot, color):
        box = RoundedRectangle(width=5.2, height=2.6, corner_radius=0.15,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.10)
        t = Text(title, font_size=23, color=color).next_to(box.get_top(), DOWN, buff=0.22)
        b = Text(body, font_size=20, color=WHITE, line_spacing=0.85).move_to(box)
        f = Text(foot, font_size=18, color=DIM).next_to(box.get_bottom(), UP, buff=0.22)
        return VGroup(box, t, b, f)
