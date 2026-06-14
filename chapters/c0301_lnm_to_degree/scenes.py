"""c0301_lnm_to_degree — "LNM converges to the degree map".

Five narrated scenes. State P1's convergence claim, derive it step by step, and
fence its exact scope. The group-average LNM map = sum(M x C); under uniform,
non-overlapping sampling M -> I, so the average column -> row-sum of C = degree =
the fixed, lesion-independent hub map (the villain). Final scene: real symptom
lesions overlap and are non-random, sampling a STRUCTURED subset of rows; the
CONTRAST, not the average, carries signal. Do not over-claim LNM is hopeless.

All equations/numbers are page-cited in:
  responses/lnm_critique/papers/P1_critique.md
  responses/lnm_critique/sections/01_the_charge_formalized.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0301_lnm_to_degree ./render.sh \
      chapters/c0301_lnm_to_degree/scenes.py -q ql \
      S1_Claim S2_RowSelection S3_Limit S4_Degree S5_Scope
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the convergence claim, stated; LNM = sum(M x C); define M and C
# ----------------------------------------------------------------------
class S1_Claim(NarratedScene):
    scene_key = "S1_Claim"

    def construct(self):
        title = Text("The convergence claim", font_size=42, color=WHITE)
        self.play_beat(Write(title))                                        # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP, buff=0.3), run_time=0.6)

        claim = VGroup(
            Text("coverage becomes uniform", font_size=27, color=VAR),
            Text("↓", font_size=30, color=DIM),
            Text("group-average LNM map", font_size=27, color=WHITE),
            Text("→  degree of the connectome", font_size=27, color=BAD),
        ).arrange(DOWN, buff=0.18).shift(UP * 0.9)
        self.play_beat(LaggedStart(*[FadeIn(c) for c in claim], lag_ratio=0.3))  # beat 2

        # the compressed matrix expression: LNM = sum_s (M x C), Eq. 3
        self.play(FadeOut(claim), run_time=0.4)
        eq = MathTex(r"\mathrm{LNM}", "=", r"\textstyle\sum_{s}", "M", r"\times", "C")\
            .scale(1.5).shift(UP * 1.2)
        eq[0].set_color(VAR); eq[3].set_color(VAR); eq[5].set_color(WHITE)
        eq3 = Text("(P1, equation 3)", font_size=22, color=DIM)\
            .next_to(eq, DOWN, buff=0.3)
        self.play_beat(Write(eq), FadeIn(eq3))                              # beat 3

        # annotate M — what it is
        brace_M = Brace(eq[3], UP, color=VAR)
        m_head = Text("M : lesion matrix", font_size=24, color=VAR)\
            .next_to(brace_M, UP, buff=0.15)
        m_dims = Text("rows = patients   ·   columns = regions",
                      font_size=22, color=DIM).next_to(m_head, UP, buff=0.15)
        self.play_beat(GrowFromCenter(brace_M), FadeIn(m_head), FadeIn(m_dims))  # beat 4

        # annotate M — entries are 0/1
        m_entry = MathTex("M", "_{ab}", "=", "1", r"\ \text{if lesion covers region}, \ ",
                          "0", r"\ \text{else}").scale(0.85)
        m_entry[0].set_color(VAR); m_entry[3].set_color(EIG); m_entry[5].set_color(EIG)
        m_entry.next_to(eq3, DOWN, buff=0.7)
        self.play_beat(Write(m_entry))                                      # beat 5

        # annotate C
        self.play(FadeOut(VGroup(brace_M, m_head, m_dims)), run_time=0.4)
        brace_C = Brace(eq[5], DOWN, color=WHITE)
        c_lab = MathTex("C", "_{bv}", r"=\ \text{connectivity of region } b \text{ to } v")\
            .scale(0.85)
        c_lab[0].set_color(WHITE)
        c_lab.next_to(brace_C, DOWN, buff=0.15)
        c_sub = Text("fixed normative connectome, same for every patient",
                     font_size=21, color=DIM).next_to(c_lab, DOWN, buff=0.15)
        self.play_beat(GrowFromCenter(brace_C),
                       FadeOut(m_entry), FadeIn(c_lab), FadeIn(c_sub))      # beat 6

        # only M changes; C is fixed
        moral = Text("only M changes patient to patient  —  C never moves",
                     font_size=26, color=RES).to_edge(DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                       # beat 7


# ----------------------------------------------------------------------
# Scene 2 — what M x C does: a row of M selects rows of C
# ----------------------------------------------------------------------
class S2_RowSelection(NarratedScene):
    scene_key = "S2_RowSelection"

    def construct(self):
        self.header("What  M × C  does")

        intro = Text("one patient at a time", font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                       # beat 1

        # patient a's row of M: a string of 0/1
        row_lab = MathTex("M", "_{a\\,\\cdot}", r"=\ ").scale(1.0)
        row_lab[0].set_color(VAR)
        bits = MathTex("(", "0", ",", "1", ",", "0", ",", "1", ",", "1", ")").scale(1.0)
        for i in (3, 7, 9):
            bits[i].set_color(EIG)
        row = VGroup(row_lab, bits).arrange(RIGHT, buff=0.15).shift(UP * 1.0)
        a_brace = Brace(row_lab[1], DOWN, color=VAR)
        a_lab = Text("patient a", font_size=22, color=VAR).next_to(a_brace, DOWN, buff=0.12)
        self.play_beat(Write(row), GrowFromCenter(a_brace), FadeIn(a_lab))  # beat 2

        # the product (M C)_{av} = sum_b M_ab C_bv
        self.play(FadeOut(VGroup(a_brace, a_lab)), run_time=0.3)
        prod = MathTex(r"(M\,C)", "_{av}", "=", r"\sum_{b}", "M", "_{ab}",
                       r"\,C", "_{bv}").scale(1.2)
        prod[0].set_color(VAR); prod[4].set_color(VAR); prod[6].set_color(WHITE)
        prod.next_to(row, DOWN, buff=0.8)
        self.play_beat(Write(prod))                                        # beat 3

        # annotate indices a, b, v
        idx = VGroup(
            MathTex("a", r"\ :\ \text{patient (which row of } M\text{)}").scale(0.8),
            MathTex("b", r"\ :\ \text{region that could be hit (summed over)}").scale(0.8),
            MathTex("v", r"\ :\ \text{target region we are scoring}").scale(0.8),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        idx[0][0].set_color(VAR); idx[1][0].set_color(EIG); idx[2][0].set_color(BACK)
        idx.next_to(prod, DOWN, buff=0.6)
        self.play_beat(LaggedStart(*[FadeIn(i) for i in idx], lag_ratio=0.3))  # beat 4

        # 0 kills the term, 1 pulls in the whole row
        self.play(FadeOut(idx), run_time=0.3)
        rule = VGroup(
            MathTex("M", "_{ab}", "=", "0", r"\ \Rightarrow\ \text{term vanishes}").scale(0.9),
            MathTex("M", "_{ab}", "=", "1", r"\ \Rightarrow\ \text{row } C", "_{b\\cdot}",
                    r"\text{ pulled in}").scale(0.9),
        ).arrange(DOWN, buff=0.3)
        rule[0][0].set_color(VAR); rule[0][3].set_color(BAD)
        rule[1][0].set_color(VAR); rule[1][3].set_color(EIG); rule[1][4].set_color(WHITE)
        rule.next_to(prod, DOWN, buff=0.6)
        self.play_beat(Write(rule[0]), Write(rule[1]))                     # beat 5

        # a row of M selects rows of C
        self.play(FadeOut(VGroup(rule, prod, row, intro)), run_time=0.5)
        sel = Text("a row of M selects which rows of C get summed",
                   font_size=30, color=RES).shift(UP * 0.5)
        self.play_beat(FadeIn(sel, shift=UP * 0.2))                        # beat 6

        moral = Text("a single lesion's map = a structured pick of rows of C, then summed",
                     font_size=25, color=WHITE).next_to(sel, DOWN, buff=0.6)
        self.play_beat(FadeIn(moral))                                      # beat 7


# ----------------------------------------------------------------------
# Scene 3 — the uniform-coverage limit: M -> I, average column -> row-sum
# ----------------------------------------------------------------------
class S3_Limit(NarratedScene):
    scene_key = "S3_Limit"

    def construct(self):
        self.header("The uniform-coverage limit")

        intro = Text("push coverage to uniform across all regions",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # empirical row-average over N patients
        avg = MathTex(r"\bar{M}", r"=\ \frac{1}{N}\sum_{a=1}^{N}", "M", "_{a\\,\\cdot}")\
            .scale(1.1).shift(UP * 1.2)
        avg[0].set_color(VAR); avg[2].set_color(VAR)
        avg_cap = Text("every region hit equally often  →  flat weights",
                       font_size=23, color=DIM).next_to(avg, DOWN, buff=0.3)
        self.play_beat(Write(avg), FadeIn(avg_cap))                        # beat 2

        # M -> I (up to a constant)
        toI = MathTex(r"\bar{M}", r"\ \longrightarrow\ ", "I",
                      r"\quad(\text{one unit of coverage per region})").scale(1.0)
        toI[0].set_color(VAR); toI[2].set_color(EIG)
        toI.next_to(avg_cap, DOWN, buff=0.5)
        self.play_beat(Write(toI))                                         # beat 3

        # M -> I => M C copies C
        copy = MathTex(r"\bar{M}", r"\,C", r"\ \longrightarrow\ ", "I", r"\,C", "=", "C")\
            .scale(1.1)
        copy[0].set_color(VAR); copy[3].set_color(EIG); copy[6].set_color(WHITE)
        copy.next_to(toI, DOWN, buff=0.5)
        copy_cap = Text("selection stops selecting — returns every row",
                        font_size=23, color=DIM).next_to(copy, DOWN, buff=0.25)
        self.play_beat(Write(copy), FadeIn(copy_cap))                      # beat 4

        # the average column -> (1/N) sum over all rows
        self.play(FadeOut(VGroup(avg, avg_cap, toI, copy, copy_cap, intro)),
                  run_time=0.5)
        col = MathTex(r"(\bar{M}\,C)", "_{v}", r"\ \longrightarrow\ ",
                      r"\frac{1}{N}", r"\sum_{b=1}^{R}", "C", "_{bv}")\
            .scale(1.2).shift(UP * 1.0)
        col[0].set_color(VAR); col[5].set_color(WHITE)
        brace = Brace(col[4:7], DOWN, color=WHITE)
        brace_lab = Text("sum over ALL rows b  (R = number of regions)",
                         font_size=23, color=WHITE).next_to(brace, DOWN, buff=0.15)
        self.play_beat(Write(col), GrowFromCenter(brace), FadeIn(brace_lab))  # beat 5

        # that is the row-sum of C (C symmetric => column-sum = row-sum)
        rowsum = MathTex(r"=\ \frac{1}{N}\,", r"\big(\text{row-sum of } C\big)", "_{v}")\
            .scale(1.1)
        rowsum[1].set_color(BAD)
        rowsum.next_to(brace_lab, DOWN, buff=0.5)
        sym = Text("C symmetric  ⇒  column-sum = row-sum",
                   font_size=22, color=DIM).next_to(rowsum, DOWN, buff=0.25)
        self.play_beat(Write(rowsum), FadeIn(sym))                         # beat 6

        moral = Text("lesions wash out — the same vector survives for every disorder",
                     font_size=25, color=RES).to_edge(DOWN, buff=0.5)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 4 — row-sum = degree = hub map; fixed, lesion-independent, villain
# ----------------------------------------------------------------------
class S4_Degree(NarratedScene):
    scene_key = "S4_Degree"

    def construct(self):
        self.header("Row-sum = degree = the hub map")

        # the naming chain
        chain = MathTex(r"\text{row-sum of } C", "=", r"\deg(C)", "=",
                        r"\text{the hub map}").scale(1.15).shift(UP * 1.6)
        chain[0].set_color(WHITE); chain[2].set_color(BAD); chain[4].set_color(BAD)
        self.play_beat(Write(chain))                                       # beat 1

        # degree defined
        deg = MathTex(r"\deg(C)", "_{v}", "=", r"\sum_{b}", "C", "_{bv}")\
            .scale(1.1).next_to(chain, DOWN, buff=0.6)
        deg[0].set_color(BAD); deg[4].set_color(WHITE)
        deg_cap = Text("total connectivity of region v to the whole brain",
                       font_size=23, color=DIM).next_to(deg, DOWN, buff=0.25)
        self.play_beat(Write(deg), FadeIn(deg_cap))                        # beat 2

        # hubs -> hub map (a little bar chart of degrees)
        self.play(FadeOut(VGroup(deg, deg_cap)), run_time=0.4)
        bars = self._degree_bars().next_to(chain, DOWN, buff=0.7)
        self.play_beat(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars.submobjects],
                                   lag_ratio=0.12))                        # beat 3

        # depends only on C — lesion-independent
        indep = MathTex(r"\deg(C)", r"\ \ \text{depends on}\ \ ", "C",
                        r"\ \ \text{alone}").scale(1.05)
        indep[0].set_color(BAD); indep[2].set_color(WHITE)
        indep.next_to(bars, DOWN, buff=0.6)
        indep_cap = Text("lesion-independent — it does not know the disorder",
                         font_size=23, color=BAD).next_to(indep, DOWN, buff=0.2)
        self.play_beat(Write(indep), FadeIn(indep_cap))                    # beat 4

        # any seed lands on it
        self.play(FadeOut(VGroup(bars, indep, indep_cap)), run_time=0.4)
        seeds = VGroup(
            Text("addiction", font_size=24, color=VAR),
            Text("depression", font_size=24, color=VAR),
            Text("random blobs", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3).shift(LEFT * 3.4 + DOWN * 0.4)
        arrow = Arrow(LEFT * 1.0 + DOWN * 0.4, RIGHT * 1.0 + DOWN * 0.4,
                      color=DIM, buff=0.1)
        target = Text("ONE fixed\nhub map", font_size=26, color=BAD,
                      line_spacing=0.8).shift(RIGHT * 3.2 + DOWN * 0.4)
        self.play_beat(FadeIn(seeds, lag_ratio=0.2), GrowArrow(arrow), FadeIn(target))  # beat 5

        # the villain, named
        villain = Text("a single, disease-blind object the average keeps reconstructing",
                       font_size=25, color=BAD).to_edge(DOWN, buff=0.9)
        box = SurroundingRectangle(villain, color=BAD, buff=0.2)
        self.play_beat(FadeIn(villain), Create(box))                       # beat 6

        # arrives fast: >=10 lesions -> r > 0.44
        self.play(FadeOut(VGroup(seeds, arrow, target, villain, box, chain)),
                  run_time=0.5)
        fast = MathTex(r"\geq 10\ \text{heterogeneous lesions}", r"\ \Rightarrow\ ",
                       "r > 0.44", r"\ \text{to degree}").scale(1.0)
        fast[2].set_color(BAD)
        fast_cap = Text("(P1, p.1241; 10,000 runs, P_spin < 0.05)",
                        font_size=22, color=DIM).next_to(fast, DOWN, buff=0.3)
        VGroup(fast, fast_cap).move_to(ORIGIN)
        self.play_beat(Write(fast), FadeIn(fast_cap))                      # beat 7

    def _degree_bars(self):
        heights = [1.7, 0.6, 1.2, 0.4, 0.9, 1.5]
        bars = VGroup()
        for i, h in enumerate(heights):
            col = BAD if h > 1.3 else DIM
            r = Rectangle(width=0.5, height=h, stroke_width=0,
                          fill_color=col, fill_opacity=0.85)
            bars.add(r)
        bars.arrange(RIGHT, buff=0.18, aligned_edge=DOWN)
        return bars


# ----------------------------------------------------------------------
# Scene 5 — the exact scope: group-average + uniform/non-overlapping ONLY
# ----------------------------------------------------------------------
class S5_Scope(NarratedScene):
    scene_key = "S5_Scope"

    def construct(self):
        self.header("The exact scope of the claim")

        head = Text("its power is also its limit — fence it precisely",
                    font_size=28, color=RES).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                       # beat 1

        # the conditional
        cond = VGroup(
            Text("holds for the GROUP-AVERAGE map", font_size=27, color=WHITE),
            Text("under UNIFORM, NON-OVERLAPPING sampling", font_size=27, color=BACK),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.2)
        self.play_beat(FadeIn(cond[0]), FadeIn(cond[1], shift=UP * 0.2))    # beat 2

        # that null is what makes M -> I
        why = MathTex(r"\text{uniform null}", r"\ \Longrightarrow\ ", r"\bar{M}", r"\to", "I")\
            .scale(1.0)
        why[2].set_color(VAR); why[4].set_color(EIG)
        why.next_to(cond, DOWN, buff=0.5)
        why_cap = Text("the one assumption the whole convergence rests on",
                       font_size=23, color=DIM).next_to(why, DOWN, buff=0.25)
        self.play_beat(Write(why), FadeIn(why_cap))                        # beat 3

        # real lesions break it: overlap, non-random
        self.play(FadeOut(VGroup(head, cond, why, why_cap)), run_time=0.5)
        real = VGroup(
            Text("real symptom lesions OVERLAP and are NON-RANDOM",
                 font_size=27, color=WHITE),
            Text("they re-hit the same region (e.g. amnesia → hippocampus)",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.9)
        self.play_beat(FadeIn(real[0]), FadeIn(real[1], shift=UP * 0.2))    # beat 4

        # structured subset of rows -> the goal, not a flaw
        subset = MathTex(r"\Rightarrow\ \text{sample a STRUCTURED subset of rows of } C")\
            .scale(0.9).set_color(BACK).next_to(real, DOWN, buff=0.5)
        goal = Text("the rebuttal calls this the GOAL of LNM — not a flaw",
                    font_size=24, color=BACK).next_to(subset, DOWN, buff=0.25)
        self.play_beat(Write(subset), FadeIn(goal))                        # beat 5

        # average vs contrast — a different object
        self.play(FadeOut(VGroup(real, subset, goal)), run_time=0.5)
        split = VGroup(
            VGroup(
                Text("AVERAGE", font_size=27, color=DIM),
                Text("a description", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.12),
            MathTex(r"\neq", color=RES).scale(1.4),
            VGroup(
                Text("CONTRAST", font_size=27, color=RES),
                Text("carries the signal", font_size=22, color=RES),
            ).arrange(DOWN, buff=0.12),
        ).arrange(RIGHT, buff=1.0).shift(UP * 1.5)
        self.play_beat(FadeIn(split, lag_ratio=0.2))                       # beat 6

        # the data
        data = VGroup(
            Text("same-symptom", font_size=23, color=BACK),
            MathTex("r = 0.44", color=BACK).scale(1.0),
            Text("different-symptom", font_size=23, color=DIM),
            MathTex("r = 0.09", color=DIM).scale(1.0),
            Text("degree map", font_size=23, color=BAD),
            MathTex("r = 0.16", color=BAD).scale(1.0),
        ).arrange_in_grid(rows=3, cols=2, buff=(0.6, 0.22))
        data.next_to(split, DOWN, buff=0.5)
        self.play_beat(FadeIn(data, lag_ratio=0.1))                        # beat 7

        # the witness; do not over-claim
        self.play(FadeOut(VGroup(split, data)), run_time=0.4)
        witness = MathTex(r"t > 10:\quad", "0", r"\ \text{false positives}",
                          r"\ /\ 1000\ \text{iterations}").scale(1.05).shift(UP * 0.4)
        witness[1].set_color(RES); witness[2].set_color(RES)
        warn = Text("do not over-claim that LNM is hopeless",
                    font_size=26, color=WHITE).next_to(witness, DOWN, buff=0.6)
        self.play_beat(Write(witness), FadeIn(warn, shift=UP * 0.2))        # beat 8
