"""c0302_slnm_to_pc1 — "Symptom-weighted LNM converges to PC1".

Five narrated scenes. The symptom-weighted variant sLNM = s_v x (M x C) (P1 Eq.
4) looks like it injects disease signal, but because s_v reweights a nearly
low-rank, backbone-dominated matrix, it converges to PC1 of C — the leading
eigenvector u1. PC1 overlaps the degree map at r = 0.82, so symptom-weighting
lands almost where plain averaging does. The rebuttal's resolution: the symptom
CONTRAST (difference of conditional means) is a different object the average
throws away (same-symptom r=0.44 vs different r=0.09 vs degree r=0.16).

All equations/numbers are page-cited in:
  responses/lnm_critique/papers/P1_critique.md          (Eq. 4; r=0.82, p.1241)
  responses/lnm_critique/sections/01_the_charge_formalized.md (rebuttal r values)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0302_slnm_to_pc1 ./render.sh \
      chapters/c0302_slnm_to_pc1/scenes.py -q ql \
      S1_Def S2_LowRank S3_PC1 S4_Correlation S5_BothRoads
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the symptom-weighted variant: sLNM = s_v x (M x C)
# ----------------------------------------------------------------------
class S1_Def(NarratedScene):
    scene_key = "S1_Def"

    def construct(self):
        self.header("The symptom-weighted variant  (P1, Eq. 4)")

        intro = Text("plain LNM averages; the symptom variant re-weights",
                     font_size=28, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # sLNM = s_v x (M x C)
        eq = MathTex(r"\mathrm{sLNM}", "=", "s_v", r"\times", r"(M \times C)")\
            .scale(1.3).shift(UP * 0.9)
        eq[0].set_color(BAD); eq[2].set_color(EIG); eq[4].set_color(VAR)
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4))          # beat 2

        # annotate M x C: selects rows of fixed C
        brace_mc = Brace(eq[4], DOWN, color=VAR)
        mc_lab = Text("M selects rows of the fixed connectome C\n(one row per region the lesion hit)",
                      font_size=22, color=VAR, line_spacing=0.8)\
            .next_to(brace_mc, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_mc), FadeIn(mc_lab))           # beat 3

        # annotate s_v: standardized symptom vector
        self.play(FadeOut(VGroup(brace_mc, mc_lab)), run_time=0.4)
        brace_sv = Brace(eq[2], UP, color=EIG)
        sv_lab = Text("s_v : standardized symptom vector\none number per patient, centered and scaled",
                      font_size=22, color=EIG, line_spacing=0.8)\
            .next_to(brace_sv, UP, buff=0.2)
        self.play_beat(GrowFromCenter(brace_sv), FadeIn(sv_lab))           # beat 4

        # contrast: plain LNM (flat weight) vs sLNM (symptom weight)
        self.play(FadeOut(VGroup(brace_sv, sv_lab, intro)), run_time=0.4)
        contrast = VGroup(
            MathTex(r"\mathrm{LNM}", r"=", r"\textstyle\sum_s", r"(M \times C)",
                    r"\quad\text{flat weight: an average}").scale(0.85),
            MathTex(r"\mathrm{sLNM}", r"=", r"s_v", r"\times", r"(M \times C)",
                    r"\quad\text{symptom sets the weight}").scale(0.85),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).next_to(eq, DOWN, buff=0.7)
        contrast[0][0].set_color(VAR)
        contrast[1][0].set_color(BAD); contrast[1][2].set_color(EIG)
        self.play_beat(FadeIn(contrast, lag_ratio=0.3))                    # beat 5

        # why it seems to inject disease signal
        seem = Text("the symptom scores are real clinical numbers —\nso the weighted map seems to carry the disease",
                    font_size=25, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(seem, shift=UP * 0.2))                       # beat 6

        # tease the answer
        self.play(FadeOut(VGroup(eq, contrast, seem)), run_time=0.5)
        tease = VGroup(
            Text("Where does the symptom weighting actually land?",
                 font_size=28, color=WHITE),
            Text("not where you would hope", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(tease, lag_ratio=0.3))                       # beat 7


# ----------------------------------------------------------------------
# Scene 2 — M x C is structured and nearly low-rank
# ----------------------------------------------------------------------
class S2_LowRank(NarratedScene):
    scene_key = "S2_LowRank"

    def construct(self):
        self.header("M × C is nearly low-rank")

        focus = MathTex(r"M \times C").scale(1.5).shift(UP * 2.2)
        focus[0].set_color(VAR)
        self.play_beat(Write(focus))                                       # beat 1

        # not noise — structured because C is nearly low-rank
        struct = Text("not arbitrary noise — structured,\nbecause C itself is nearly low-rank",
                      font_size=27, color=WHITE, line_spacing=0.8).shift(UP * 0.9)
        self.play_beat(FadeIn(struct))                                     # beat 2

        # nearly low-rank meaning
        meaning = Text("nearly low-rank:  a few patterns explain almost all of C",
                       font_size=25, color=DIM).next_to(struct, DOWN, buff=0.45)
        self.play_beat(FadeIn(meaning))                                    # beat 3

        # one pattern dominates: the backbone
        self.play(FadeOut(VGroup(struct, meaning)), run_time=0.4)
        bars = self._spectrum_bars().next_to(focus, DOWN, buff=0.7)
        bb = Text("the biggest direction = the degree / hub pattern = the BACKBONE",
                  font_size=23, color=BACK).next_to(bars, DOWN, buff=0.35)
        self.play_beat(*[GrowFromEdge(b, DOWN) for b in bars.submobjects],
                       FadeIn(bb), lag_ratio=0.15)                         # beat 4

        # spectral form, lambda_1 >> lambda_2
        self.play(FadeOut(VGroup(bars, bb, focus)), run_time=0.4)
        spec = MathTex("C", "=", r"\sum_{j}", r"\lambda_j", "u_j", "u_j^\\top")\
            .scale(1.2).shift(UP * 1.4)
        spec[3].set_color(EIG); spec[4].set_color(BACK); spec[5].set_color(BACK)
        gap = MathTex(r"\lambda_1", r"\;\gg\;", r"\lambda_2")\
            .scale(1.2).next_to(spec, DOWN, buff=0.5)
        gap[0].set_color(EIG); gap[2].set_color(EIG)
        gap_lab = Text("sum over patterns u-j; each scaled by eigenvalue λ-j;\n"
                       "u-j times u-j-transpose is the outer product — a pattern;  λ-1 ≫ λ-2",
                       font_size=20, color=DIM, line_spacing=0.8)\
            .next_to(gap, DOWN, buff=0.35)
        self.play_beat(Write(spec), Write(gap), FadeIn(gap_lab))           # beat 5

        # one factor dominates -> reweighting steers to it
        steer = Text("one factor dominates → any reweighting is steered toward it",
                     font_size=25, color=WHITE).next_to(gap_lab, DOWN, buff=0.5)
        self.play_beat(FadeIn(steer, shift=UP * 0.2))                      # beat 6

        # conclusion: s_v aligns with the dominant factor
        self.play(FadeOut(VGroup(spec, gap, gap_lab, steer)), run_time=0.5)
        concl = VGroup(
            Text("whatever s_v does,", font_size=27, color=EIG),
            Text("multiplying a backbone-dominated matrix",
                 font_size=27, color=WHITE),
            Text("forces alignment with the one dominant factor",
                 font_size=27, color=BACK),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(concl, lag_ratio=0.3))                       # beat 7

    def _spectrum_bars(self):
        heights = [2.6, 0.5, 0.32, 0.22, 0.16, 0.12]
        colors = [BACK, DIM, DIM, DIM, DIM, DIM]
        bars = VGroup()
        for i, (h, c) in enumerate(zip(heights, colors)):
            b = Rectangle(width=0.45, height=h, stroke_width=0,
                          fill_color=c, fill_opacity=0.9)
            b.align_to(ORIGIN, DOWN).shift(RIGHT * i * 0.62)
            bars.add(b)
        bars.move_to(ORIGIN, aligned_edge=DOWN)
        return bars


# ----------------------------------------------------------------------
# Scene 3 — sLNM -> PC1(C), the first principal component
# ----------------------------------------------------------------------
class S3_PC1(NarratedScene):
    scene_key = "S3_PC1"

    def construct(self):
        self.header("Convergence to the first principal component")

        # name PC1
        name = MathTex(r"\text{dominant factor}", "=", r"\mathrm{PC1}(C)")\
            .scale(1.2).shift(UP * 2.2)
        name[2].set_color(BACK)
        self.play_beat(Write(name))                                        # beat 1

        # PC1 = direction of max variance
        maxvar = Text("PC1 = the direction of MAXIMUM variance\n(the axis along which the rows of C spread the most)",
                      font_size=25, color=WHITE, line_spacing=0.8).shift(UP * 0.9)
        self.play_beat(FadeIn(maxvar))                                     # beat 2

        # PC1 = u_1, the leading eigenvector / backbone
        equ = MathTex(r"\mathrm{PC1}(C)", "=", "u_1",
                      r"\ \ (\text{leading eigenvector} = \text{backbone})")\
            .scale(0.95).next_to(maxvar, DOWN, buff=0.55)
        equ[0].set_color(BACK); equ[2].set_color(BACK)
        self.play_beat(Write(equ))                                         # beat 3

        # the arrow: sLNM -> PC1(C)
        self.play(FadeOut(VGroup(maxvar, equ, name)), run_time=0.5)
        arrow = MathTex(r"\mathrm{sLNM}", r"\;\longrightarrow\;",
                        r"\mathrm{PC1}(C)").scale(1.4).shift(UP * 1.4)
        arrow[0].set_color(BAD); arrow[2].set_color(BACK)
        cap = Text("for any standardized symptom vector s_v",
                   font_size=24, color=DIM).next_to(arrow, DOWN, buff=0.3)
        self.play_beat(Write(arrow), FadeIn(cap))                          # beat 4

        # decode every symbol
        legend = VGroup(
            self._row(r"\mathrm{sLNM}", BAD, "the symptom-weighted map"),
            self._row(r"\mathrm{PC1}(C)", BACK, "top variance direction of C"),
            self._row("u_1", BACK, "its eigenvector — the backbone"),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).next_to(cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(legend, lag_ratio=0.2))                      # beat 5

        # regardless of clinically informed or random
        self.play(FadeOut(legend), run_time=0.4)
        regardless = Text("\"...regardless of whether the lesions or symptom\nscores are clinically informed or random\"  (P1, p.1241)",
                          font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(cap, DOWN, buff=0.6)
        self.play_beat(FadeIn(regardless, shift=UP * 0.2))                 # beat 6

        # the trap
        trap = Text("→  random and real symptom numbers steer sLNM\nonto the SAME fixed direction, PC1",
                    font_size=25, color=BAD, line_spacing=0.8)\
            .next_to(regardless, DOWN, buff=0.45)
        self.play_beat(FadeIn(trap, shift=UP * 0.2))                       # beat 7

    def _row(self, sym, color, words):
        s = MathTex(sym).scale(0.85).set_color(color)
        w = Text("  " + words, font_size=22, color=DIM)
        g = VGroup(s, w).arrange(RIGHT, buff=0.25, aligned_edge=DOWN)
        return g


# ----------------------------------------------------------------------
# Scene 4 — PC1 is almost the degree map: r = 0.82
# ----------------------------------------------------------------------
class S4_Correlation(NarratedScene):
    scene_key = "S4_Correlation"

    def construct(self):
        self.header("PC1 is almost the degree map")

        # the two destinations
        dests = VGroup(
            MathTex(r"\text{averaging}", r"\;\to\;", r"\deg(C)").scale(1.0),
            MathTex(r"\text{symptom-weighting}", r"\;\to\;", r"\mathrm{PC1}(C)").scale(1.0),
        ).arrange(DOWN, buff=0.4).shift(UP * 1.9)
        dests[0][2].set_color(BAD)
        dests[1][2].set_color(BACK)
        q = Text("same place?", font_size=26, color=DIM)\
            .next_to(dests, DOWN, buff=0.4)
        self.play_beat(FadeIn(dests, lag_ratio=0.3), FadeIn(q))            # beat 1

        # the number r = 0.82
        self.play(FadeOut(q), dests.animate.scale(0.8).to_edge(UP, buff=1.1),
                  run_time=0.5)
        catch = MathTex(r"r\big(", r"\mathrm{PC1}(C)", ",", r"\deg(C)", r"\big)",
                        "=", "0.82").scale(1.3).shift(UP * 0.5)
        catch[1].set_color(BACK); catch[3].set_color(BAD); catch[6].set_color(RES)
        self.play_beat(Write(catch))                                       # beat 2

        # decode r
        brace = Brace(catch[:5], DOWN, color=DIM)
        rlab = Text("correlation across the brain's regions\nbetween PC1 and the degree (row-sum of C)",
                    font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(brace, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace), FadeIn(rlab))                # beat 3

        # 0.82 is high
        self.play(FadeOut(VGroup(brace, rlab)), run_time=0.4)
        high = Text("0.82 is a very high overlap —\nPC1 is essentially the degree map in a different hat",
                    font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(catch, DOWN, buff=0.6)
        self.play_beat(FadeIn(high, shift=UP * 0.2))                       # beat 4

        # both roads same place
        self.play(FadeOut(high), run_time=0.4)
        both = Text("symptom-weighting lands almost exactly\nwhere plain averaging does",
                    font_size=26, color=BACK, line_spacing=0.8)\
            .next_to(catch, DOWN, buff=0.6)
        self.play_beat(FadeIn(both, shift=UP * 0.2))                       # beat 5

        # box the result
        box = SurroundingRectangle(catch, color=RES, buff=0.22)
        result = Text("the result of this chapter", font_size=22, color=RES)\
            .next_to(box, DOWN, buff=0.25)
        self.play_beat(Create(box), FadeIn(result), both.animate.set_opacity(0.3))  # beat 6


# ----------------------------------------------------------------------
# Scene 5 — both roads, one hub place; but the contrast is different
# ----------------------------------------------------------------------
class S5_BothRoads(NarratedScene):
    scene_key = "S5_BothRoads"

    def construct(self):
        self.header("Both roads, one hub place")

        # two recipes -> one object
        recipes = VGroup(
            self._chip("averaging", VAR),
            self._chip("symptom-weighting", BAD),
        ).arrange(DOWN, buff=0.6).shift(LEFT * 3.6 + UP * 0.3)
        arrow = Arrow(LEFT * 1.0 + UP * 0.3, RIGHT * 1.0 + UP * 0.3,
                      color=DIM, buff=0.1)
        hub = VGroup(
            Text("a HUB-shaped", font_size=26, color=BACK),
            Text("object", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.1).shift(RIGHT * 3.2 + UP * 0.3)
        self.play_beat(FadeIn(recipes, lag_ratio=0.2), GrowArrow(arrow),
                       FadeIn(hub))                                        # beat 1

        # name the destinations + r=0.82
        names = MathTex(r"\deg(C)", r"\ \overset{r=0.82}{\approx}\ ",
                        r"\mathrm{PC1}(C)").scale(1.0).to_edge(DOWN, buff=1.0)
        names[0].set_color(VAR); names[2].set_color(BAD)
        names[1][1:].set_color(RES)
        self.play_beat(FadeIn(names, shift=UP * 0.2))                      # beat 2

        # if that were the whole story -> hopeless
        self.play(FadeOut(VGroup(recipes, arrow, hub, names)), run_time=0.5)
        hopeless = Text("if that were the whole story, sLNM would be hopeless:\nthe symptom would just repaint the backbone",
                        font_size=26, color=DIM, line_spacing=0.8).shift(UP * 2.2)
        self.play_beat(FadeIn(hopeless))                                   # beat 3

        # BUT: the contrast — what the average throws away
        but = VGroup(
            Text("BUT one object neither road computes —", font_size=27, color=RES),
            Text("and the average actively throws away:", font_size=27, color=RES),
            Text("the symptom CONTRAST", font_size=30, color=RES),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.3)
        self.play_beat(hopeless.animate.set_opacity(0.3),
                       FadeIn(but, shift=UP * 0.2))                        # beat 4

        # define the contrast: difference of conditional means
        self.play(FadeOut(VGroup(hopeless, but)), run_time=0.5)
        contrast = MathTex(r"\Delta", "=",
                           r"\overline{m}_{\text{symptom}}", "-",
                           r"\overline{m}_{\text{no symptom}}")\
            .scale(1.1).shift(UP * 1.6)
        contrast[0].set_color(RES)
        contrast[2].set_color(VAR); contrast[4].set_color(DIM)
        cdef = Text("difference of conditional means:\nmean map WITH the symptom  −  mean map WITHOUT",
                    font_size=23, color=DIM, line_spacing=0.8)\
            .next_to(contrast, DOWN, buff=0.35)
        self.play_beat(Write(contrast), FadeIn(cdef))                      # beat 5

        # subtraction cancels the backbone
        cancel = Text("the shared backbone is in BOTH groups → it cancels,\nleaving the part that knows the symptom",
                      font_size=25, color=BACK, line_spacing=0.8)\
            .next_to(cdef, DOWN, buff=0.5)
        self.play_beat(FadeIn(cancel, shift=UP * 0.2))                     # beat 6

        # the rebuttal numbers
        self.play(FadeOut(VGroup(contrast, cdef, cancel)), run_time=0.5)
        data = VGroup(
            self._stat("same-symptom", "0.44", BACK),
            self._stat("different-symptom", "0.09", DIM),
            self._stat("degree map", "0.16", BAD),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.7)
        cite = Text("the contrast behaves  (REBUTTAL p.3)",
                    font_size=22, color=DIM).next_to(data, UP, buff=0.4)
        self.play_beat(FadeIn(cite), FadeIn(data, lag_ratio=0.2))          # beat 7

        # the moral
        moral = Text("the symptom-weighted AVERAGE lands on the backbone —\nbut the CONTRAST is a different object, and it carries the signal",
                     font_size=24, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 8

    def _chip(self, label, color):
        box = RoundedRectangle(width=3.4, height=0.75, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=23, color=color).move_to(box)
        return VGroup(box, t)

    def _stat(self, label, value, color):
        lab = Text(label, font_size=24, color=DIM)
        val = MathTex("r", "=", value).scale(1.0).set_color(color)
        return VGroup(lab, val).arrange(RIGHT, buff=0.5)
