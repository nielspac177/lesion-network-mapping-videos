"""c0504_four_patient_example — "The four-patient worked example".

Five narrated scenes that walk the tiny worked example from
responses/lnm_critique/sections/03_the_right_null.md by hand:

  Four patients, one voxel each. x_i = b_i + r_i with b_i = 10 (backbone, same
  for all) and r_i = +/-2 (residual). Two impaired (y=1), two spared (y=0).
  Contrast T = mean(impaired) - mean(spared).

  S1  the setup and the table; define T_obs.
  S2  T_obs = 4 by explicit arithmetic; the backbone 10 cancels.
  S3  all six relabelings; T in {+4, -4, 0, 0, 0, 0}.
  S4  p = 1/6 by counting T >= T_obs (exactly one).
  S5  swap 10 -> 10,000; T_obs, the six T's, and p = 1/6 are unchanged.

All numbers are quoted from the source's worked-example tables. No invented
constants.

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0504_four_patient_example ./render.sh \
      chapters/c0504_four_patient_example/scenes.py -q ql \
      S1_Setup S2_Tobs S3_AllSix S4_Pvalue S5_Invariance
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Four patients: the setup and the table
# ----------------------------------------------------------------------
class S1_Setup(NarratedScene):
    scene_key = "S1_Setup"

    def construct(self):
        self.header("Four patients")

        intro = Text("four patients  ·  one voxel of map value each",
                     font_size=28, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # the decomposition x_i = b_i + r_i
        decomp = MathTex("x_i", "=", "b_i", "+", "r_i").scale(1.4).shift(UP * 1.4)
        decomp[0].set_color(VAR); decomp[2].set_color(BACK); decomp[4].set_color(RES)
        b_lab = Text("backbone", font_size=22, color=BACK)
        r_lab = Text("residual", font_size=22, color=RES)
        b_brace = Brace(decomp[2], DOWN, color=BACK)
        r_brace = Brace(decomp[4], DOWN, color=RES)
        b_lab.next_to(b_brace, DOWN, buff=0.15)
        r_lab.next_to(r_brace, DOWN, buff=0.15)
        self.play_beat(Write(decomp),
                       GrowFromCenter(b_brace), GrowFromCenter(r_brace),
                       FadeIn(b_lab), FadeIn(r_lab))                       # beat 2

        # backbone = 10 for everyone
        bb = MathTex("b_i", "=", "10", r"\quad\text{(same offset for all four)}")\
            .scale(1.0)
        bb[0].set_color(BACK); bb[2].set_color(BACK)
        bb.next_to(VGroup(b_lab, r_lab), DOWN, buff=0.55)
        self.play_beat(Write(bb))                                         # beat 3

        # residual = +/- 2
        rr = MathTex("r_i", r"\in", r"\{\,+2,\ -2\,\}").scale(1.0)
        rr[0].set_color(RES); rr[2].set_color(RES)
        rr.next_to(bb, DOWN, buff=0.35)
        self.play_beat(Write(rr))                                         # beat 4

        # clear and build the table
        self.play(FadeOut(VGroup(intro, decomp, b_brace, r_brace,
                                 b_lab, r_lab, bb, rr)), run_time=0.5)
        table = self._table()
        table.shift(DOWN * 0.2)
        # reveal the b/r/x columns (values) first
        self.play_beat(FadeIn(table))                                     # beat 5

        # highlight the label column
        self.play_beat(Indicate(self._label_col, color=VAR,
                                scale_factor=1.08))                       # beat 6

        # define T_obs
        tdef = MathTex("T", "=", r"\bar x^{(1)}", "-", r"\bar x^{(0)}").scale(1.05)
        tdef[0].set_color(EIG)
        tdef[2].set_color(BAD)
        tdef[4].set_color(DIM)
        tdef.to_edge(DOWN, buff=0.55)
        tcap = Text("impaired group mean  -  spared group mean",
                    font_size=21, color=DIM).next_to(tdef, UP, buff=0.2)
        self.play_beat(Write(tdef), FadeIn(tcap))                         # beat 7

    def _table(self):
        """Build the 4-patient table as a VGroup; store the label column."""
        headers = ["patient", "b_i", "r_i", "x_i", "y_i"]
        rows = [
            ["1", "10", "+2", "12", "1  impaired"],
            ["2", "10", "+2", "12", "1  impaired"],
            ["3", "10", "-2", "8",  "0  spared"],
            ["4", "10", "-2", "8",  "0  spared"],
        ]
        col_x = [-4.6, -2.9, -1.4, 0.1, 2.4]
        col_color = [DIM, BACK, RES, VAR, VAR]
        grp = VGroup()
        # header row
        hrow = VGroup()
        for j, h in enumerate(headers):
            t = Text(h, font_size=24, color=WHITE).move_to([col_x[j], 1.55, 0])
            hrow.add(t)
        grp.add(hrow)
        rule = Line([-5.4, 1.25, 0], [3.6, 1.25, 0], color=DIM, stroke_width=1.5)
        grp.add(rule)
        label_cells = VGroup()
        for i, r in enumerate(rows):
            y = 0.85 - i * 0.62
            for j, val in enumerate(r):
                t = Text(val, font_size=23, color=col_color[j]).move_to([col_x[j], y, 0])
                grp.add(t)
                if j == 4:
                    label_cells.add(t)
        self._label_col = label_cells
        return grp


# ----------------------------------------------------------------------
# Scene 2 — The observed statistic: T_obs = 4
# ----------------------------------------------------------------------
class S2_Tobs(NarratedScene):
    scene_key = "S2_Tobs"

    def construct(self):
        self.header("The observed statistic")

        # impaired mean
        imp = MathTex(r"\bar x^{(1)}", "=", r"\frac{12 + 12}{2}", "=", "12")\
            .scale(1.15).shift(UP * 2.1)
        imp[0].set_color(BAD); imp[4].set_color(BAD)
        imp_cap = Text("impaired:  patients 1 and 2",
                       font_size=22, color=DIM).next_to(imp, UP, buff=0.2)
        self.play_beat(Write(imp), FadeIn(imp_cap))                       # beat 1

        # spared mean
        spa = MathTex(r"\bar x^{(0)}", "=", r"\frac{8 + 8}{2}", "=", "8")\
            .scale(1.15).next_to(imp, DOWN, buff=0.9)
        spa[0].set_color(DIM); spa[4].set_color(DIM)
        spa_cap = Text("spared:  patients 3 and 4",
                       font_size=22, color=DIM).next_to(spa, UP, buff=0.2)
        self.play_beat(Write(spa), FadeIn(spa_cap))                       # beat 2

        # T_obs = 4
        tobs = MathTex(r"T_{\text{obs}}", "=", "12", "-", "8", "=", "4")\
            .scale(1.25).next_to(spa, DOWN, buff=0.9)
        tobs[0].set_color(EIG); tobs[6].set_color(RES)
        box = SurroundingRectangle(tobs[6], color=RES, buff=0.15)
        self.play_beat(Write(tobs), Create(box))                          # beat 3

        # now show the cancellation: rewrite each mean as 10 +/- 2
        self.play(FadeOut(VGroup(imp, imp_cap, spa, spa_cap, tobs, box)),
                  run_time=0.5)
        split = MathTex(r"T_{\text{obs}}", "=",
                        r"(\,10 + 2\,)", "-", r"(\,10 - 2\,)").scale(1.1).shift(UP * 1.2)
        split[0].set_color(EIG)
        # color the backbone 10s and residuals inside the parenthesized args
        split[2].set_color(WHITE); split[4].set_color(WHITE)
        cap = Text("impaired = backbone 10 + residual; spared = backbone 10 - residual",
                   font_size=21, color=DIM).next_to(split, UP, buff=0.3)
        self.play_beat(Write(split), FadeIn(cap))                         # beat 4

        # the backbone cancels: 10 - 10 = 0
        cancel = MathTex(r"\underbrace{10 - 10}_{=\,0}", "+",
                         r"\big(\,2 - (-2)\,\big)").scale(1.05)\
            .next_to(split, DOWN, buff=0.9)
        cancel[0].set_color(BACK)
        cancel_cap = Text("the backbone 10 sits on both sides  ->  it cancels exactly",
                          font_size=22, color=BACK).next_to(cancel, DOWN, buff=0.35)
        self.play_beat(Write(cancel), FadeIn(cancel_cap))                 # beat 5

        # what survives = residuals = 4
        survive = MathTex(r"T_{\text{obs}}", "=", "2", "-", "(-2)", "=", "4")\
            .scale(1.2).to_edge(DOWN, buff=0.9)
        survive[0].set_color(EIG); survive[6].set_color(RES)
        survive_cap = Text("only the residuals survive  ·  the huge offset contributes nothing",
                           font_size=21, color=RES).next_to(survive, UP, buff=0.3)
        self.play_beat(Write(survive), FadeIn(survive_cap))               # beat 6


# ----------------------------------------------------------------------
# Scene 3 — All six relabelings
# ----------------------------------------------------------------------
class S3_AllSix(NarratedScene):
    scene_key = "S3_AllSix"

    def construct(self):
        self.header("All six relabelings")

        intro = Text("keep every map fixed  ·  only reshuffle who is labeled impaired",
                     font_size=25, color=DIM).shift(UP * 2.8)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # 4 choose 2 = 6
        count = MathTex(r"\binom{4}{2}", "=", "6", r"\ \text{ways to assign the labels}")\
            .scale(1.05).shift(UP * 1.9)
        count[0].set_color(VAR); count[2].set_color(RES)
        self.play_beat(Write(count))                                      # beat 2

        # build the six-row table; reveal observed row
        table, rows = self._six_table()
        table.shift(DOWN * 0.45)
        self.play(FadeOut(intro), count.animate.scale(0.8).to_edge(UP, buff=1.05),
                  run_time=0.5)
        self.add(table[0], table[1])  # header + rule, no beat
        self.play_beat(FadeIn(rows[0]))                                   # beat 3  observed {1,2} -> +4

        self.play_beat(FadeIn(rows[1]))                                   # beat 4  {3,4} -> -4

        # the remaining four split one 12 and one 8 into each group
        self.play_beat(FadeIn(rows[2]), FadeIn(rows[3]), lag_ratio=0.3)   # beat 5  {1,3},{1,4} start

        self.play_beat(FadeIn(rows[4]), FadeIn(rows[5]), lag_ratio=0.3)   # beat 6  {2,3},{2,4} -> all 0

        # the permutation distribution as six values
        dist = MathTex(r"\{\,", "+4", ",\,", "-4", ",\,", "0", ",\,",
                       "0", ",\,", "0", ",\,", "0", r"\,\}").scale(1.0)
        dist[1].set_color(RES); dist[3].set_color(BAD)
        dist.to_edge(DOWN, buff=1.05)
        dist_cap = Text("the permutation distribution",
                        font_size=21, color=DIM).next_to(dist, UP, buff=0.2)
        self.play_beat(Write(dist), FadeIn(dist_cap))                     # beat 7

        # the backbone vanished from the whole table
        note = Text("the backbone 10 vanished from every row  -  it cancels in every difference",
                    font_size=22, color=BACK).next_to(dist, DOWN, buff=0.3)
        self.play_beat(FadeIn(note, shift=UP * 0.2))                      # beat 8

    def _six_table(self):
        headers = ["impaired set", "impaired x", "spared x", "T"]
        data = [
            ["{1,2}  (observed)", "12, 12", "8, 8", "+4"],
            ["{3,4}", "8, 8", "12, 12", "-4"],
            ["{1,3}", "12, 8", "12, 8", "0"],
            ["{1,4}", "12, 8", "12, 8", "0"],
            ["{2,3}", "12, 8", "12, 8", "0"],
            ["{2,4}", "12, 8", "12, 8", "0"],
        ]
        col_x = [-4.3, -1.3, 0.9, 3.2]
        grp = VGroup()
        hrow = VGroup()
        for j, h in enumerate(headers):
            hrow.add(Text(h, font_size=23, color=WHITE).move_to([col_x[j], 1.35, 0]))
        grp.add(hrow)
        grp.add(Line([-5.5, 1.05, 0], [4.4, 1.05, 0], color=DIM, stroke_width=1.5))
        rows = []
        for i, d in enumerate(data):
            y = 0.6 - i * 0.5
            tcol = RES if d[3] == "+4" else (BAD if d[3] == "-4" else DIM)
            rowg = VGroup()
            for j, val in enumerate(d):
                c = tcol if j == 3 else (DIM if j == 0 else VAR)
                rowg.add(Text(val, font_size=22, color=c).move_to([col_x[j], y, 0]))
            rows.append(rowg)
            grp.add(rowg)
        return grp, rows


# ----------------------------------------------------------------------
# Scene 4 — The p-value
# ----------------------------------------------------------------------
class S4_Pvalue(NarratedScene):
    scene_key = "S4_Pvalue"

    def construct(self):
        self.header("The p-value")

        intro = Text("read a p-value straight off the table  ·  by counting",
                     font_size=26, color=DIM).shift(UP * 2.8)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # the permutation p-value definition
        pdef = MathTex(r"p", "=",
                       r"\frac{\#\{\,\text{labelings with } T \ge T_{\text{obs}}\,\}}{6}")\
            .scale(1.0).shift(UP * 1.6)
        pdef[0].set_color(RES); pdef[2].set_color(WHITE)
        self.play_beat(Write(pdef))                                       # beat 2

        # the six values, lined up to be scanned; T_obs = 4
        vals = MathTex(r"\{\,", "+4", ",\,", "-4", ",\,", "0", ",\,",
                       "0", ",\,", "0", ",\,", "0", r"\,\}").scale(1.1)
        vals[1].set_color(RES); vals[3].set_color(BAD)
        vals.shift(UP * 0.1)
        thresh = MathTex(r"T_{\text{obs}} = 4").scale(0.9)
        thresh[0].set_color(EIG)
        thresh.next_to(vals, UP, buff=0.4)
        self.play_beat(Write(vals), FadeIn(thresh))                       # beat 3

        # exactly one reaches >= 4: the observed itself
        hit = SurroundingRectangle(vals[1], color=RES, buff=0.12)
        cap = Text("exactly one value reaches 4 or higher: the observed labeling",
                   font_size=23, color=RES).next_to(vals, DOWN, buff=0.5)
        self.play_beat(Create(hit), FadeIn(cap))                          # beat 4

        # p = 1/6
        self.play(FadeOut(VGroup(intro, pdef, vals, thresh, hit, cap)),
                  run_time=0.5)
        pval = MathTex(r"p", "=", r"\frac{1}{6}", r"\approx", "0.167")\
            .scale(1.4).shift(UP * 0.9)
        pval[0].set_color(RES); pval[2].set_color(RES); pval[4].set_color(RES)
        box = SurroundingRectangle(pval, color=RES, buff=0.25)
        pcap = Text("the rank of the observed among all six equally likely labelings",
                    font_size=22, color=DIM).next_to(box, DOWN, buff=0.35)
        self.play_beat(Write(pval), Create(box), FadeIn(pcap))            # beat 5

        # can't beat 1/6 with four patients
        floor = Text("with only four patients you cannot beat one-sixth  -  honest resolution",
                     font_size=23, color=WHITE).next_to(pcap, DOWN, buff=0.45)
        self.play_beat(FadeIn(floor, shift=UP * 0.2))                     # beat 6

        # came from counting, not from any distributional assumption
        moral = Text("the p-value came from COUNTING labelings,\nnot from any assumption about the map values",
                     font_size=24, color=BACK, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 7


# ----------------------------------------------------------------------
# Scene 5 — Swap 10 for 10,000
# ----------------------------------------------------------------------
class S5_Invariance(NarratedScene):
    scene_key = "S5_Invariance"

    def construct(self):
        self.header("Swap 10 for 10,000")

        head = MathTex(r"b_i", ":", "10", r"\ \longrightarrow\ ", "10{,}000")\
            .scale(1.25).shift(UP * 2.4)
        head[0].set_color(BACK); head[2].set_color(BACK); head[4].set_color(BACK)
        self.play_beat(Write(head))                                       # beat 1

        # new map values
        newx = MathTex(r"x^{(1)}", "=", "10{,}002", r"\qquad", r"x^{(0)}", "=", "9{,}998")\
            .scale(1.0).shift(UP * 1.2)
        newx[0].set_color(BAD); newx[2].set_color(BAD)
        newx[4].set_color(DIM); newx[6].set_color(DIM)
        newx_cap = Text("impaired = 10,000 + 2 ;  spared = 10,000 - 2",
                        font_size=22, color=DIM).next_to(newx, UP, buff=0.25)
        self.play_beat(Write(newx), FadeIn(newx_cap))                     # beat 2

        # recompute T_obs
        rec = MathTex(r"T_{\text{obs}}", "=", "10{,}002", "-", "9{,}998", "=", "4")\
            .scale(1.05).next_to(newx, DOWN, buff=0.8)
        rec[0].set_color(EIG); rec[6].set_color(RES)
        self.play_beat(Write(rec))                                        # beat 3

        # the 10,000 cancels
        cancel = MathTex(r"\underbrace{10{,}000 - 10{,}000}_{=\,0}", "+",
                         r"\big(\,2 - (-2)\,\big)", "=", "4").scale(0.95)
        cancel[0].set_color(BACK); cancel[4].set_color(RES)
        cancel.next_to(rec, DOWN, buff=0.55)
        self.play_beat(Write(cancel))                                     # beat 4

        # the whole table is identical
        self.play(FadeOut(VGroup(head, newx, newx_cap, rec, cancel)),
                  run_time=0.5)
        dist = MathTex(r"\{\,", "+4", ",\,", "-4", ",\,", "0", ",\,",
                       "0", ",\,", "0", ",\,", "0", r"\,\}").scale(1.15).shift(UP * 1.1)
        dist[1].set_color(RES); dist[3].set_color(BAD)
        dist_cap = Text("every entry identical to the 10-backbone table",
                        font_size=23, color=DIM).next_to(dist, UP, buff=0.3)
        self.play_beat(Write(dist), FadeIn(dist_cap))                     # beat 5

        # p still 1/6
        pval = MathTex(r"p", "=", r"\frac{1}{6}", r"\quad\text{(unchanged)}")\
            .scale(1.25).next_to(dist, DOWN, buff=0.7)
        pval[0].set_color(RES); pval[2].set_color(RES)
        pcap = Text("the null never noticed the backbone  -  because the contrast never did",
                    font_size=22, color=BACK).next_to(pval, DOWN, buff=0.35)
        self.play_beat(Write(pval), FadeIn(pcap))                         # beat 6

        # the moral
        moral = Text("the backbone magnitude is irrelevant to the test:\nit could be 10, or 10,000, or anything at all",
                     font_size=25, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 7
