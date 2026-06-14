"""c0506_same_data_opposite_verdicts — "Same data, opposite verdicts".

Five narrated scenes. Take ONE tiny dataset — the four-patient, one-voxel worked
example from sections/03_the_right_null.md — and run the LOCATION null and the
SYMPTOM null on it side by side. The location null finds nothing (every map is
backbone-shaped, T-b ~ T_obs, p large). The symptom null finds T_obs = 4, p = 1/6
because the backbone (b_i = 10) cancels in every group-mean difference and only
the residuals r_i survive. Nothing changed but the null — the QUESTION. Then the
rebuttal's empirical witness: 0 false positives / 1000 iterations at t > 10, with
4.6% leakage only at the lenient t = 3.0.

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/03_the_right_null.md   (worked example, p.116-147)
  responses/lnm_critique/papers/REBUTTAL_sound.md        (FPR numbers, p.3)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0506_same_data_opposite_verdicts ./render.sh \
      chapters/c0506_same_data_opposite_verdicts/scenes.py -q ql \
      S1_TwoNulls S2_LocationFinds S3_SymptomFinds S4_Difference S5_Witness
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — two nulls, one dataset: build the four-patient table
# ----------------------------------------------------------------------
class S1_TwoNulls(NarratedScene):
    scene_key = "S1_TwoNulls"

    def construct(self):
        self.header("Two nulls, one dataset")

        intro = Text("one tiny dataset, judged by two different courts",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # four patients, one voxel; the bare decomposition equation
        decomp = MathTex("x_i", "=", "b_i", "+", "r_i").scale(1.3).shift(UP * 1.3)
        decomp[0].set_color(VAR); decomp[2].set_color(BACK); decomp[4].set_color(RES)
        cap = Text("4 patients,  one voxel of map value each  (V = 1)",
                   font_size=24, color=WHITE).next_to(decomp, DOWN, buff=0.35)
        self.play_beat(Write(decomp), FadeIn(cap))                        # beat 2

        # annotate b_i = backbone offset of 10
        brace_b = Brace(decomp[2], DOWN, color=BACK)
        b_lab = Text("backbone piece: same offset b_i = 10 for everyone",
                     font_size=23, color=BACK).next_to(brace_b, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_b), FadeIn(b_lab),
                       intro.animate.set_opacity(0.35))                   # beat 3

        # annotate r_i = residual, the only thing the symptom can track
        self.play(FadeOut(VGroup(brace_b, b_lab)), run_time=0.4)
        brace_r = Brace(decomp[4], DOWN, color=RES)
        r_lab = Text("residual r_i:  +2, +2, -2, -2  —  the only symptom-trackable part",
                     font_size=22, color=RES).next_to(brace_r, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_r), FadeIn(r_lab))            # beat 4

        # the full table x_i = b_i + r_i with labels
        self.play(FadeOut(VGroup(intro, cap, decomp, brace_r, r_lab)),
                  run_time=0.5)
        table = self._patient_table().shift(DOWN * 0.2)
        self.play_beat(FadeIn(table, lag_ratio=0.05))                    # beat 5

        # question 1: the location null
        self.play(table.animate.scale(0.8).to_edge(LEFT, buff=0.6),
                  run_time=0.5)
        q_loc = VGroup(
            Text("LOCATION null", font_size=26, color=BAD),
            Text("is this PLACE special?", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.18).shift(RIGHT * 3.3 + UP * 1.2)
        self.play_beat(FadeIn(q_loc, shift=UP * 0.2))                    # beat 6

        # question 2: the symptom null
        q_sym = VGroup(
            Text("SYMPTOM null", font_size=26, color=BACK),
            Text("do the LABELS track these fixed lesions?", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.18).shift(RIGHT * 3.3 + DOWN * 1.0)
        self.play_beat(FadeIn(q_sym, shift=UP * 0.2))                    # beat 7

    def _patient_table(self):
        rows = [
            ("Patient", "b_i", "r_i", "x_i", "y_i"),
            ("1", "10", "+2", "12", "1 (impaired)"),
            ("2", "10", "+2", "12", "1 (impaired)"),
            ("3", "10", "-2", "8", "0 (spared)"),
            ("4", "10", "-2", "8", "0 (spared)"),
        ]
        col_colors = [WHITE, BACK, RES, VAR, EIG]
        grid = VGroup()
        for ri, row in enumerate(rows):
            for ci, cell in enumerate(row):
                col = DIM if ri == 0 else col_colors[ci]
                fs = 22 if ri == 0 else 24
                t = Text(cell, font_size=fs, color=col)
                t.move_to([ci * 1.9 - 3.8, 1.0 - ri * 0.55, 0])
                grid.add(t)
        return grid


# ----------------------------------------------------------------------
# Scene 2 — the location null finds nothing
# ----------------------------------------------------------------------
class S2_LocationFinds(NarratedScene):
    scene_key = "S2_LocationFinds"

    def construct(self):
        self.header("The location null finds nothing")

        intro = Text("compare the observed map against random seeds from an ensemble",
                     font_size=25, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # recall R1: every map ~ a scalar multiple of u_1
        r1 = MathTex(r"m_\ell", r"\approx", r"\lambda_1", r"(u_1^\top \ell)\,", "u_1")\
            .scale(1.15).shift(UP * 1.4)
        r1[0].set_color(VAR); r1[2].set_color(EIG); r1[4].set_color(BACK)
        r1_cap = Text("R1: every seed's map is nearly a scalar multiple of one direction u_1",
                      font_size=22, color=DIM).next_to(r1, DOWN, buff=0.3)
        self.play_beat(Write(r1), FadeIn(r1_cap),
                       intro.animate.set_opacity(0.35))                  # beat 2

        # decode each symbol of R1: map, top eigenvalue, scalar overlap, direction
        br_m = Brace(r1[0], UP, color=VAR)
        m_lab = Text("m_ell: the seed's map", font_size=20, color=VAR)\
            .next_to(br_m, UP, buff=0.12)
        br_lam = Brace(r1[2], DOWN, color=EIG)
        lam_lab = Text("lambda_1: top eigenvalue", font_size=20, color=EIG)\
            .next_to(br_lam, DOWN, buff=0.12)
        br_load = Brace(r1[3], DOWN, color=DIM)
        load_lab = Text("u_1^T ell: scalar overlap (one number)", font_size=20, color=DIM)\
            .next_to(br_load, DOWN, buff=0.12).shift(RIGHT * 0.9)
        self.play_beat(GrowFromCenter(br_m), FadeIn(m_lab),
                       GrowFromCenter(br_lam), FadeIn(lam_lab),
                       GrowFromCenter(br_load), FadeIn(load_lab))        # beat 3

        # fakes ~ 10 and reals ~ 10: the crowd looks like the data
        self.play(FadeOut(VGroup(intro, r1, r1_cap, br_m, m_lab,
                                 br_lam, lam_lab, br_load, load_lab)),
                  run_time=0.4)
        cloud = self._value_cloud().shift(UP * 0.5)
        self.play_beat(FadeIn(cloud, lag_ratio=0.04))                    # beat 4

        # T(b) ~ T_obs for nearly every b
        tline = MathTex("T^{(b)}", r"\approx", "T_{\\text{obs}}",
                        r"\quad\text{for almost every } b").scale(1.05)
        tline[0].set_color(BAD); tline[2].set_color(VAR)
        tline.next_to(cloud, DOWN, buff=0.6)
        self.play_beat(Write(tline))                                     # beat 5

        # observed sits dead-center; p large; nothing rejects
        self.play(FadeOut(VGroup(cloud, tline)), run_time=0.4)
        verdict = VGroup(
            Text("T_obs sits dead-center in the null", font_size=26, color=WHITE),
            MathTex(r"p\ \text{large}", r"\ \Rightarrow\ ",
                    r"\text{nothing rejects}").scale(1.05),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.7)
        verdict[1][0].set_color(BAD); verdict[1][2].set_color(BAD)
        self.play_beat(FadeIn(verdict[0]), Write(verdict[1]))            # beat 6

        # not miscalibrated: a valid test of an irrelevant question
        valid = Text("not miscalibrated — a valid test of a question the backbone blurs",
                     font_size=24, color=DIM).next_to(verdict, DOWN, buff=0.6)
        self.play_beat(FadeIn(valid))                                    # beat 7

        # moral
        moral = Text("a non-significant result here is the WRONG QUESTION,\ncorrectly answered — not proof of no signal",
                     font_size=25, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                    # beat 8

    def _value_cloud(self):
        grp = VGroup()
        # fakes (random seeds), all ~ 10
        import random
        random.seed(7)
        for k in range(9):
            v = 10 + random.uniform(-0.4, 0.4)
            dot = Dot(color=DIM, radius=0.07)
            dot.move_to([k * 0.85 - 3.4, (v - 10) * 1.2, 0])
            grp.add(dot)
        # the observed real map, also ~ 10
        obs = Dot(color=VAR, radius=0.11).move_to([0.4, 0.0, 0])
        obs_lab = Text("T_obs", font_size=20, color=VAR).next_to(obs, UP, buff=0.15)
        baseline = DashedLine([-3.8, 0, 0], [4.2, 0, 0], color=BACK, stroke_width=2)
        base_lab = Text("all maps  ~ 10  (backbone)", font_size=21, color=BACK)\
            .next_to(baseline, DOWN, buff=0.2).to_edge(LEFT, buff=0.8)
        return VGroup(baseline, base_lab, grp, obs, obs_lab)


# ----------------------------------------------------------------------
# Scene 3 — the symptom null finds T = 4
# ----------------------------------------------------------------------
class S3_SymptomFinds(NarratedScene):
    scene_key = "S3_SymptomFinds"

    def construct(self):
        self.header("The symptom null finds  T = 4")

        intro = Text("keep every lesion fixed; only shuffle who is labelled impaired",
                     font_size=25, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # the statistic and the observed value
        stat = MathTex("T", "=", r"\bar{x}^{(1)}", "-", r"\bar{x}^{(0)}",
                       "=", "12", "-", "8", "=", "4").scale(1.1).shift(UP * 1.4)
        stat[0].set_color(VAR); stat[2].set_color(BAD); stat[4].set_color(BACK)
        stat[10].set_color(RES)
        stat_cap = Text("difference in group means: impaired minus spared",
                        font_size=22, color=DIM).next_to(stat, DOWN, buff=0.3)
        self.play_beat(Write(stat), FadeIn(stat_cap),
                       intro.animate.set_opacity(0.35))                  # beat 2

        # six labelings
        self.play(FadeOut(VGroup(intro, stat, stat_cap)), run_time=0.4)
        count = MathTex(r"\binom{4}{2}", "=", "6",
                        r"\ \text{equally-likely labelings}").scale(1.0)\
            .shift(UP * 2.4)
        count[2].set_color(RES)
        self.play_beat(Write(count))                                     # beat 3

        table = self._perm_table().shift(DOWN * 0.4)
        # backbone-cancellation callout
        cancel = Text("offset 10 is identical on both sides → cancels in every row",
                      font_size=22, color=BACK).next_to(table, DOWN, buff=0.35)
        self.play_beat(FadeIn(table, lag_ratio=0.05), FadeIn(cancel))    # beat 4

        # T depends only on residuals: the six values
        self.play(FadeOut(VGroup(count, cancel)), run_time=0.4)
        vals = MathTex(r"\{T\}", "=", r"\{\,+4,\ -4,\ 0,\ 0,\ 0,\ 0\,\}")\
            .scale(1.05).to_edge(UP, buff=1.0)
        vals[0].set_color(VAR); vals[2].set_color(WHITE)
        self.play_beat(Write(vals), table.animate.scale(0.85).shift(DOWN * 0.2))  # beat 5

        # the p-value
        pval = MathTex("p", "=", r"\frac{1}{6}", r"\approx", "0.167").scale(1.15)\
            .to_edge(DOWN, buff=1.3)
        pval[0].set_color(VAR); pval[2].set_color(RES); pval[4].set_color(RES)
        pbox = SurroundingRectangle(pval, color=RES, buff=0.2)
        self.play_beat(Write(pval), Create(pbox))                        # beat 6

        # robustness: came from counting, not distribution
        robust = Text("p came from COUNTING labelings — swap 10 for 10,000, nothing changes",
                      font_size=22, color=DIM).next_to(pval, UP, buff=0.5)
        self.play_beat(FadeIn(robust))                                   # beat 7

        # the moral: same data, a real effect surfaces
        self.play(FadeOut(VGroup(vals, table, pval, pbox, robust)),
                  run_time=0.5)
        moral = VGroup(
            Text("the SAME data that rejected nothing under location", font_size=26, color=WHITE),
            Text("surfaces a real effect:  T = 4 tops its null", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                    # beat 8

    def _perm_table(self):
        rows = [
            ("labeling", "impaired x", "spared x", "T"),
            ("{1,2} obs", "12, 12", "8, 8", "+4"),
            ("{3,4}", "8, 8", "12, 12", "-4"),
            ("{1,3}", "12, 8", "12, 8", "0"),
            ("{1,4}", "12, 8", "12, 8", "0"),
            ("{2,3}", "12, 8", "12, 8", "0"),
            ("{2,4}", "12, 8", "12, 8", "0"),
        ]
        grid = VGroup()
        for ri, row in enumerate(rows):
            for ci, cell in enumerate(row):
                if ri == 0:
                    col = DIM
                elif ci == 3:
                    col = RES if cell == "+4" else (BAD if cell == "-4" else DIM)
                else:
                    col = WHITE
                fs = 21 if ri == 0 else 22
                t = Text(cell, font_size=fs, color=col)
                t.move_to([ci * 2.4 - 3.6, 1.0 - ri * 0.45, 0])
                grid.add(t)
        return grid


# ----------------------------------------------------------------------
# Scene 4 — the difference is the question
# ----------------------------------------------------------------------
class S4_Difference(NarratedScene):
    scene_key = "S4_Difference"

    def construct(self):
        self.header("The difference is the question")

        intro = Text("same patients, same connectome, same maps — opposite fate",
                     font_size=26, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # side-by-side verdicts
        left = VGroup(
            Text("LOCATION null", font_size=26, color=BAD),
            Text("T_obs unremarkable", font_size=24, color=WHITE),
            Text("finds NOTHING", font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.22).shift(LEFT * 3.3 + UP * 0.9)
        right = VGroup(
            Text("SYMPTOM null", font_size=26, color=BACK),
            Text("T = 4 tops its null", font_size=24, color=WHITE),
            Text("finds a REAL effect", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.22).shift(RIGHT * 3.3 + UP * 0.9)
        divider = DashedLine(UP * 1.9, DOWN * 0.4, color=DIM, stroke_width=2)
        self.play_beat(FadeIn(left), FadeIn(right), Create(divider),
                       intro.animate.set_opacity(0.35))                  # beat 2

        # only the null changed
        changed = Text("nothing changed but the NULL HYPOTHESIS — the QUESTION",
                       font_size=26, color=RES).to_edge(DOWN, buff=1.4)
        self.play_beat(FadeIn(changed, shift=UP * 0.2))                  # beat 3

        # opposite hypotheses
        self.play(FadeOut(VGroup(intro, left, right, divider, changed)),
                  run_time=0.5)
        hyps = VGroup(
            MathTex(r"H_0^{\text{loc}}", r":\ \text{is the PLACE special?}").scale(1.0),
            MathTex(r"H_0^{\text{sym}}", r":\ \text{does the LABEL track the place?}").scale(1.0),
        ).arrange(DOWN, buff=0.5).shift(UP * 1.2)
        hyps[0][0].set_color(BAD); hyps[1][0].set_color(BACK)
        self.play_beat(Write(hyps[0]), Write(hyps[1]))                   # beat 4

        # the backbone's opposite fate
        fate = VGroup(
            Text("backbone = the VILLAIN that swamps the location null", font_size=24, color=BAD),
            Text("backbone = a NON-ENTITY that cancels in the symptom null", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.3).next_to(hyps, DOWN, buff=0.7)
        self.play_beat(FadeIn(fate[0]), FadeIn(fate[1], shift=UP * 0.2))  # beat 5

        # the thesis line
        self.play(FadeOut(VGroup(hyps, fate)), run_time=0.5)
        thesis = VGroup(
            Text("A failed null was a failed QUESTION,", font_size=30, color=WHITE),
            Text("not proof of no signal.", font_size=30, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.6)
        self.play_beat(FadeIn(thesis, lag_ratio=0.3))                    # beat 6

        close = Text("the thesis of the series, demonstrated on numbers you can check by hand",
                     font_size=24, color=DIM).next_to(thesis, DOWN, buff=0.7)
        self.play_beat(FadeIn(close))                                    # beat 7


# ----------------------------------------------------------------------
# Scene 5 — the empirical witness
# ----------------------------------------------------------------------
class S5_Witness(NarratedScene):
    scene_key = "S5_Witness"

    def construct(self):
        self.header("The empirical witness  (REBUTTAL p.3)")

        intro = Text("the hand example shows the mechanism — now the witness at scale",
                     font_size=25, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # the database
        db = VGroup(
            MathTex(r"1090", r"\ \text{lesion locations}").scale(1.0),
            MathTex(r"34", r"\ \text{symptoms},\ 34\ \text{prior LNM studies}").scale(1.0),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.3)
        db[0][0].set_color(VAR); db[1][0].set_color(VAR)
        self.play_beat(FadeIn(db), intro.animate.set_opacity(0.35))      # beat 2

        # the FPR procedure
        proc = MathTex(r"50\ \text{lesions}", r"\ \text{vs}\ ",
                       r"1040", r"\ \text{remaining},\ ", r"1000\ \text{iterations}")\
            .scale(0.95).next_to(db, DOWN, buff=0.6)
        proc[0].set_color(VAR); proc[2].set_color(VAR); proc[4].set_color(DIM)
        self.play_beat(Write(proc))                                      # beat 3

        # the headline: 0 / 1000 at t > 10
        self.play(FadeOut(VGroup(intro, db, proc)), run_time=0.5)
        head = MathTex(r"t > 10:\quad", r"0\ \text{false positives}",
                       r"\ /\ 1000\ \text{iterations}").scale(1.1).shift(UP * 1.3)
        head[1].set_color(RES)
        head_cap = Text("standard thresholds:  sensitivity 75%,  specificity t > 10",
                        font_size=23, color=DIM).next_to(head, DOWN, buff=0.3)
        hbox = SurroundingRectangle(head, color=RES, buff=0.2)
        self.play_beat(Write(head), Create(hbox), FadeIn(head_cap))      # beat 4

        # leakage only at lenient t = 3.0
        leak = MathTex(r"t = 3.0:\quad", r"4.6\%", r"\ \text{of permutations}")\
            .scale(1.0).next_to(head_cap, DOWN, buff=0.7)
        leak[1].set_color(BAD)
        leak_cap = Text("leakage emerges only BELOW the standard threshold",
                        font_size=22, color=DIM).next_to(leak, DOWN, buff=0.25)
        self.play_beat(Write(leak), FadeIn(leak_cap))                    # beat 5

        # controls error where it matters
        where = Text("the symptom-label null controls error exactly where it matters —\nat the thresholds real LNM studies actually use",
                     font_size=24, color=RES, line_spacing=0.8)\
            .next_to(leak_cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(where, shift=UP * 0.2))                    # beat 6

        # closing
        self.play(FadeOut(VGroup(head, hbox, head_cap, leak, leak_cap, where)),
                  run_time=0.5)
        close = VGroup(
            Text("Same data, opposite verdicts.", font_size=30, color=WHITE),
            Text("Location asks the wrong question.", font_size=28, color=BAD),
            Text("The symptom null asks the right one — and it holds.", font_size=28, color=RES),
        ).arrange(DOWN, buff=0.32)
        self.play_beat(FadeIn(close, lag_ratio=0.3))                     # beat 7
