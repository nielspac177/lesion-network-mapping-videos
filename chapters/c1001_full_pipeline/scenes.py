"""c1001_full_pipeline — "The full recommended pipeline".

Five narrated scenes. Collect the whole series into ONE auditable pipeline:
  1. contrast under H0^sym   (don't report the average; report a contrast)
  2. Freedman-Lane           (size-protected label permutation)
  3. residualize backbone    (project out the leading modes with Pi_B^perp)
  4. degree+size baseline    (beat it out-of-sample) + max-statistic FWE
  5. why each step earns its place (the pipeline IS the critique, answered)

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/08_recipe.md
  responses/lnm_critique/sections/04_removing_the_backbone.md  (the projector)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c1001_full_pipeline ./render.sh \
      chapters/c1001_full_pipeline/scenes.py -q ql \
      S1_Overview S2_NullAndFL S3_Residualize S4_BaselineFWE S5_Why
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the recipe, one diagram (the full five-box flow)
# ----------------------------------------------------------------------
class S1_Overview(NarratedScene):
    scene_key = "S1_Overview"

    def construct(self):
        title = Text("The recipe, one diagram", font_size=42, color=WHITE)
        sub = Text("five boxes; each shuts down one charge",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # five boxes laid out as a vertical flow on the left, labels filled in
        b1 = self._box(r"\text{1.\ \ contrast under }H_0^{\text{sym}}", VAR)
        b2 = self._box(r"\text{2.\ \ Freedman--Lane}", EIG)
        b3 = self._box(r"\text{3.\ \ residualize }\Pi_{\mathcal B}^{\perp}", BACK)
        b4 = self._box(r"\text{4.\ \ beat degree+size baseline}", RES)
        b5 = self._box(r"\text{5.\ \ FWE max-statistic}", BAD)
        flow = VGroup(b1, b2, b3, b4, b5).arrange(DOWN, buff=0.32)
        flow.scale(0.92).move_to(ORIGIN + DOWN * 0.1)
        arrows = VGroup(*[
            Arrow(a.get_bottom(), b.get_top(), buff=0.06,
                  color=DIM, stroke_width=3, max_tip_length_to_length_ratio=0.18)
            for a, b in zip(flow.submobjects[:-1], flow.submobjects[1:])
        ])
        self.play_beat(FadeIn(flow, lag_ratio=0.0), GrowArrow(arrows[0]))   # beat 2

        # spotlight each box in turn, one narration beat per box
        self.play_beat(self._spot(b1), GrowArrow(arrows[1]))               # beat 3
        self.play_beat(self._spot(b2))                                     # beat 4
        self.play_beat(self._spot(b3), GrowArrow(arrows[2]))              # beat 5
        self.play_beat(self._spot(b4), GrowArrow(arrows[3]))             # beat 6
        self.play_beat(self._spot(b5))                                    # beat 7

        moral = Text("walk the column; each box names the failure it shuts down",
                     font_size=24, color=DIM).to_edge(DOWN, buff=0.4)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 8

    def _box(self, label, color):
        box = RoundedRectangle(width=5.4, height=0.78, corner_radius=0.12,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.10)
        t = MathTex(label, color=color).scale(0.6).move_to(box)
        return VGroup(box, t)

    def _spot(self, box):
        return box.animate.set_stroke(width=5).scale(1.04)


# ----------------------------------------------------------------------
# Scene 2 — symptom null + Freedman-Lane  (steps 1-2)
# ----------------------------------------------------------------------
class S2_NullAndFL(NarratedScene):
    scene_key = "S2_NullAndFL"

    def construct(self):
        self.header("Symptom null + Freedman--Lane   (08_recipe, C1)")

        intro = Text("the first two boxes: what you ask, and how you calibrate it",
                     font_size=26, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # step 1: the per-patient data
        data = MathTex(r"\text{patient } i:", r"\ \ \tilde m_{\ell_i}", r",\ \ ",
                       "y_i", r"\in\{0,1\}").scale(1.0).shift(UP * 1.4)
        data[1].set_color(VAR); data[3].set_color(EIG)
        b_m = Brace(data[1], DOWN, color=VAR)
        m_lab = Text("residualized map", font_size=20, color=VAR)\
            .next_to(b_m, DOWN, buff=0.15)
        b_y = Brace(data[3], UP, color=EIG)
        y_lab = Text("symptom label", font_size=20, color=EIG)\
            .next_to(b_y, UP, buff=0.15)
        self.play_beat(Write(data), GrowFromCenter(b_m), FadeIn(m_lab),
                       GrowFromCenter(b_y), FadeIn(y_lab))                 # beat 2

        # the contrast statistic
        self.play(FadeOut(VGroup(b_m, m_lab, b_y, y_lab)), run_time=0.4)
        stat = MathTex(r"T(v)", "=", r"\bar{\tilde m}(v\mid y{=}1)", "-",
                       r"\bar{\tilde m}(v\mid y{=}0)").scale(0.95)
        stat[0].set_color(VAR); stat[2].set_color(VAR); stat[4].set_color(DIM)
        stat.next_to(data, DOWN, buff=0.7)
        cap = Text("the group difference at every voxel  v  (never the average)",
                   font_size=22, color=WHITE).next_to(stat, DOWN, buff=0.3)
        self.play_beat(Write(stat), FadeIn(cap))                          # beat 3

        # the null: shuffle labels not lesions
        self.play(FadeOut(VGroup(intro, data, stat, cap)), run_time=0.4)
        null = MathTex(r"H_0^{\text{sym}}:", r"\ \ \{y_i\}",
                       r"\ \text{exchangeable given fixed }", r"\{\ell_i\}")\
            .scale(0.9).shift(UP * 1.6)
        null[1].set_color(EIG); null[3].set_color(VAR)
        shuffle = Text("shuffle the symptom labels, NOT the lesions",
                       font_size=26, color=RES).next_to(null, DOWN, buff=0.4)
        self.play_beat(Write(null), FadeIn(shuffle))                      # beat 4

        # why labels: backbone cancels
        cancel = VGroup(
            Text("the backbone is identical in every patient", font_size=24, color=DIM),
            Text("→ fixed in the observed AND every shuffled statistic", font_size=24, color=WHITE),
            Text("→ it cancels from the contrast; cannot fake a result", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(shuffle, DOWN, buff=0.45)
        self.play_beat(LaggedStart(*[FadeIn(c) for c in cancel], lag_ratio=0.25))  # beat 5

        # step 2: Freedman-Lane, size protection
        self.play(FadeOut(VGroup(null, shuffle, cancel)), run_time=0.45)
        fl_head = Text("Step 2 — protect against lesion size (the dominant nuisance)",
                       font_size=25, color=WHITE).shift(UP * 1.9)
        fl = MathTex(r"\text{Freedman--Lane:}").scale(0.95)\
            .next_to(fl_head, DOWN, buff=0.4)
        self.play_beat(FadeIn(fl_head), Write(fl))                        # beat 6

        # FL recipe in words + symbols
        steps = VGroup(
            MathTex(r"1.\ \ \text{fit } y \sim \text{size},\ \ \text{get residuals } e").scale(0.8),
            MathTex(r"2.\ \ \text{permute only } e \ \ (\text{hold size fixed})").scale(0.8),
            MathTex(r"3.\ \ \text{re-test on the permuted residuals}").scale(0.8),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).next_to(fl, DOWN, buff=0.4)
        steps[0].set_color(WHITE); steps[1].set_color(EIG); steps[2].set_color(WHITE)
        self.play_beat(LaggedStart(*[FadeIn(s) for s in steps], lag_ratio=0.25))  # beat 7

        moral = Text("valid AND size-protected — the right question, an unbiased null",
                     font_size=24, color=RES).to_edge(DOWN, buff=0.45)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 8


# ----------------------------------------------------------------------
# Scene 3 — residualize the backbone  (step 3; recall the projector)
# ----------------------------------------------------------------------
class S3_Residualize(NarratedScene):
    scene_key = "S3_Residualize"

    def construct(self):
        self.header("Residualize the backbone   (04_removing_the_backbone)")

        intro = Text("the null made the test valid; this makes it powerful & specific",
                     font_size=25, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # spectral decomposition of C
        spec = MathTex("C", "=", r"\sum_{j} \lambda_j", "u_j", "u_j^{\\top}")\
            .scale(1.1).shift(UP * 1.5)
        spec[0].set_color(WHITE); spec[2].set_color(EIG); spec[3].set_color(BACK)
        b_u = Brace(spec[3], DOWN, color=BACK)
        u_lab = Text("j-th eigenvector (a connectome mode)",
                     font_size=21, color=BACK).next_to(b_u, DOWN, buff=0.15)
        self.play_beat(Write(spec), GrowFromCenter(b_u), FadeIn(u_lab))    # beat 2

        # the backbone subspace
        self.play(FadeOut(VGroup(b_u, u_lab)), run_time=0.4)
        sub = MathTex(r"\mathcal{B}", "=", r"\mathrm{span}",
                      r"\{u_1,\dots,u_r\}").scale(1.0).next_to(spec, DOWN, buff=0.6)
        sub[0].set_color(BACK); sub[3].set_color(BACK)
        sub_cap = Text("the backbone: the dominant skeleton every seed lights up",
                       font_size=22, color=WHITE).next_to(sub, DOWN, buff=0.3)
        self.play_beat(Write(sub), FadeIn(sub_cap))                       # beat 3

        # the projector
        self.play(FadeOut(VGroup(intro, spec, sub, sub_cap)), run_time=0.45)
        proj = MathTex(r"\Pi_{\mathcal B}", "=",
                       r"\sum_{j=1}^{r}", "u_j", "u_j^{\\top}")\
            .scale(1.15).shift(UP * 1.6)
        proj[0].set_color(BACK); proj[3].set_color(BACK)
        proj_cap = MathTex(r"\Pi_{\mathcal B}\,x", r"=\ \text{the part of }x\text{ in the backbone}")\
            .scale(0.85).next_to(proj, DOWN, buff=0.4)
        proj_cap[0].set_color(BACK)
        self.play_beat(Write(proj), FadeIn(proj_cap))                     # beat 4

        # the complement
        comp = MathTex(r"\Pi_{\mathcal B}^{\perp}", "=", "I", "-",
                       r"\Pi_{\mathcal B}").scale(1.05).next_to(proj_cap, DOWN, buff=0.55)
        comp[0].set_color(VAR); comp[2].set_color(EIG); comp[4].set_color(BACK)
        comp_cap = Text("keeps everything orthogonal to the leading modes",
                        font_size=22, color=DIM).next_to(comp, DOWN, buff=0.3)
        self.play_beat(Write(comp), FadeIn(comp_cap))                     # beat 5

        # the residualized map
        self.play(FadeOut(VGroup(proj, proj_cap, comp, comp_cap)), run_time=0.45)
        res = MathTex(r"\tilde m_\ell", "=", r"m_\ell", "-",
                      r"\Pi_{\mathcal B}\, m_\ell", "=",
                      r"\Pi_{\mathcal B}^{\perp} m_\ell")\
            .scale(1.05).shift(UP * 1.3)
        res[0].set_color(VAR); res[2].set_color(VAR)
        res[4].set_color(BACK); res[6].set_color(VAR)
        tail = MathTex(r"=\ \sum_{j>r} \lambda_j (u_j^{\top}\ell)\, u_j")\
            .scale(0.9).set_color(DIM).next_to(res, DOWN, buff=0.35)
        tail_cap = Text("subtract the backbone; keep the tail of the spectrum",
                        font_size=22, color=WHITE).next_to(tail, DOWN, buff=0.3)
        self.play_beat(Write(res), FadeIn(tail), FadeIn(tail_cap))        # beat 6

        # costs no signal
        self.play(FadeOut(VGroup(tail, tail_cap)), run_time=0.4)
        free = VGroup(
            Text("under backbone-sharing the backbone is label-independent",
                 font_size=23, color=DIM),
            Text("→ all the between-group difference lives in the residual",
                 font_size=23, color=BACK),
            Text("→ signal preserved, nonspecific noise removed",
                 font_size=23, color=RES),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(res, DOWN, buff=0.6)
        self.play_beat(LaggedStart(*[FadeIn(c) for c in free], lag_ratio=0.25))  # beat 7

        self.play(FadeOut(VGroup(res, free)), run_time=0.45)
        moral = VGroup(
            Text("the test now sees OFF-BACKBONE signal alone", font_size=27, color=WHITE),
            Text("what P1 says is shared, and what we remove,", font_size=25, color=DIM),
            Text("are one and the same object.", font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.25)
        self.play_beat(FadeIn(moral, lag_ratio=0.2))                      # beat 8


# ----------------------------------------------------------------------
# Scene 4 — degree+size baseline + FWE max-statistic  (steps 4-5)
# ----------------------------------------------------------------------
class S4_BaselineFWE(NarratedScene):
    scene_key = "S4_BaselineFWE"

    def construct(self):
        self.header("Degree baseline + FWE   (08_recipe, C8 / P2 p.1025)")

        intro = Text("the last two boxes set the bar for belief",
                     font_size=26, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # step 4: out-of-sample prediction
        oos = VGroup(
            Text("Step 4 — out-of-sample prediction", font_size=26, color=RES),
            Text("train on cohort A  →  predict graded outcome in held-out cohort B",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.5)
        self.play_beat(FadeIn(oos[0]), FadeIn(oos[1], shift=UP * 0.2))     # beat 2

        # beat a degree+size baseline
        base = MathTex(r"\text{prediction}(\tilde m)", ">",
                       r"\text{prediction}(\deg(C)+\text{size})")\
            .scale(0.85).next_to(oos, DOWN, buff=0.5)
        base[0].set_color(VAR); base[2].set_color(BAD)
        base_cap = Text("the rebuttal's actual control (p.3)",
                        font_size=21, color=DIM).next_to(base, DOWN, buff=0.25)
        self.play_beat(Write(base), FadeIn(base_cap))                     # beat 3

        # the entailment
        why = Text("if the map were only the backbone, degree would predict just as well;\nbeating it is the proof that something beyond the backbone works",
                   font_size=23, color=WHITE, line_spacing=0.85)\
            .next_to(base_cap, DOWN, buff=0.4)
        self.play_beat(FadeIn(why, shift=UP * 0.2))                       # beat 4

        # step 5: max-statistic null
        self.play(FadeOut(VGroup(intro, oos, base, base_cap, why)), run_time=0.5)
        fwe_head = Text("Step 5 — family-wise error by the permutation max-statistic",
                        font_size=25, color=WHITE).shift(UP * 2.0)
        maxstat = MathTex(r"M^{(b)}", "=", r"\max_{v}", r"\ T^{(b)}(v)")\
            .scale(1.05).next_to(fwe_head, DOWN, buff=0.45)
        maxstat[0].set_color(BAD); maxstat[2].set_color(BAD)
        ms_cap = Text("each shuffle b: record the single largest voxel statistic",
                      font_size=22, color=DIM).next_to(maxstat, DOWN, buff=0.3)
        self.play_beat(FadeIn(fwe_head), Write(maxstat), FadeIn(ms_cap))  # beat 5

        # threshold = 95th percentile
        thr = MathTex(r"t^\star", "=", r"\text{95th percentile of }",
                      r"\{M^{(b)}\}").scale(0.95).next_to(ms_cap, DOWN, buff=0.5)
        thr[0].set_color(RES); thr[3].set_color(BAD)
        thr_cap = Text("≥ 5000 permutations;  family-wise error controlled at 5%",
                       font_size=22, color=BACK).next_to(thr, DOWN, buff=0.25)
        self.play_beat(Write(thr), FadeIn(thr_cap))                       # beat 6

        # why it controls FWE
        self.play(FadeOut(VGroup(fwe_head, maxstat, ms_cap, thr, thr_cap)),
                  run_time=0.5)
        ctrl = Text("comparing against the MAXIMUM makes survivors significant\nacross the whole family at once — sweeps cannot inflate false positives",
                    font_size=24, color=WHITE, line_spacing=0.85).shift(UP * 0.9)
        self.play_beat(FadeIn(ctrl, shift=UP * 0.2))                      # beat 7

        witness = MathTex(r"t > 10:\quad", r"0\ \text{false positives}",
                          r"\ /\ 1000\ \text{iterations}").scale(1.0)
        witness[1].set_color(RES)
        witness.next_to(ctrl, DOWN, buff=0.7)
        self.play_beat(Write(witness))                                    # beat 8


# ----------------------------------------------------------------------
# Scene 5 — why each step earns its place (the pipeline IS the critique)
# ----------------------------------------------------------------------
class S5_Why(NarratedScene):
    scene_key = "S5_Why"

    def construct(self):
        self.header("Why each step earns its place")

        intro = Text("read the pipeline as an argument: one box per failure",
                     font_size=27, color=DIM).shift(UP * 2.8)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # build the charge -> fix ledger, one row per beat
        rows = VGroup(
            self._row("wrong question", r"\text{symptom-label contrast}", VAR),
            self._row("size confound", r"\text{Freedman--Lane}", EIG),
            self._row("backbone dominance", r"\text{residualize }\Pi_{\mathcal B}^{\perp}", BACK),
            self._row("hub baseline", r"\text{beat degree out-of-sample}", RES),
            self._row("multiple comparisons", r"\text{FWE max-statistic}", BAD),
        ).arrange(DOWN, buff=0.3).scale(0.9).shift(DOWN * 0.2)

        self.play_beat(FadeIn(rows[0], shift=RIGHT * 0.2))                # beat 2
        self.play_beat(FadeIn(rows[1], shift=RIGHT * 0.2))               # beat 3
        self.play_beat(FadeIn(rows[2], shift=RIGHT * 0.2))              # beat 4
        self.play_beat(FadeIn(rows[3], shift=RIGHT * 0.2))             # beat 5
        self.play_beat(FadeIn(rows[4], shift=RIGHT * 0.2))            # beat 6

        # the single theme
        self.play(FadeOut(VGroup(intro, rows)), run_time=0.5)
        theme = VGroup(
            Text("one theme, three moves:", font_size=28, color=WHITE),
            Text("make the backbone CANCEL", font_size=25, color=BACK),
            Text("SUBTRACT the backbone", font_size=25, color=BACK),
            Text("refuse to read its SHADOW as a result", font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.25)
        self.play_beat(FadeIn(theme, lag_ratio=0.2))                     # beat 7

        self.play(FadeOut(theme), run_time=0.45)
        moral = VGroup(
            Text("The pipeline is the critique, answered point by point.",
                 font_size=28, color=WHITE),
            Text("The premises are true.", font_size=26, color=DIM),
            Text("Only the leap to \"LNM is hopeless\" over-shoots —",
                 font_size=26, color=RES),
            Text("once these five moves are in place.", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.28)
        self.play_beat(FadeIn(moral, lag_ratio=0.25))                    # beat 8

    def _row(self, charge, fix, color):
        c = Text(charge, font_size=24, color=BAD)
        arr = MathTex(r"\longrightarrow", color=DIM).scale(0.9)
        f = MathTex(fix, color=color).scale(0.62)
        grp = VGroup(c, arr, f).arrange(RIGHT, buff=0.45)
        return grp
