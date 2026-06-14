"""c0503_backbone_cancellation — "Backbone cancellation (the algebra)".

Five narrated scenes. The load-bearing algebra of the whole response: decompose
each patient map x_i = b_i + r_i with the backbone piece
b_i = lambda_1 (u_1^T l_i) u_1; show that b_i is label-blind; form the symptom
contrast t_v ∝ (bbar^1 - bbar^0) u_{1,v} + (rbar^1 - rbar^0); strike the backbone
piece out under permutation; and conclude that only the label-correlated residual
survives. Camera vs court, made algebraic.

All equations/numbers are sourced from:
  responses/lnm_critique/sections/03_the_right_null.md  (backbone-cancellation)
  responses/lnm_critique/sections/02_what_is_entailed.md (the contrast Delta)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0503_backbone_cancellation ./render.sh \
      chapters/c0503_backbone_cancellation/scenes.py -q ql \
      S1_Decompose S2_BackboneLabelFree S3_Contrast S4_Cancel S5_Moral
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — split each map: x_i = b_i + r_i,  b_i = lambda_1 (u_1^T l_i) u_1
# ----------------------------------------------------------------------
class S1_Decompose(NarratedScene):
    scene_key = "S1_Decompose"

    def construct(self):
        self.header("Split each map")

        intro = Text("one map per patient — split each into two pieces",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                       # beat 1

        # x_i = b_i + r_i
        eq = MathTex("x_i", "=", "b_i", "+", "r_i").scale(1.5).shift(UP * 1.0)
        eq[0].set_color(VAR); eq[2].set_color(BACK); eq[4].set_color(RES)
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4))          # beat 2

        # expand b_i = lambda_1 (u_1^T l_i) u_1
        bdef = MathTex("b_i", "=", r"\lambda_1", r"\,\big(", "u_1^{\\top} \\ell_i",
                       r"\big)\,", "u_1").scale(1.25).shift(DOWN * 0.4)
        bdef[0].set_color(BACK); bdef[2].set_color(EIG)
        bdef[4].set_color(VAR); bdef[6].set_color(BACK)
        self.play_beat(Write(bdef), eq.animate.scale(0.8).to_edge(UP, buff=1.1))  # beat 3

        # annotate lambda_1 and u_1 together (the connectome's dominant axis)
        brace_u = Brace(bdef[6], DOWN, color=BACK)
        u_lab = Text("u-one: the connectome's dominant hub axis (the backbone)",
                     font_size=22, color=BACK).next_to(brace_u, DOWN, buff=0.18)
        brace_lam = Brace(bdef[2], UP, color=EIG)
        lam_lab = Text("lambda-one: how strongly that axis dominates",
                       font_size=22, color=EIG).next_to(brace_lam, UP, buff=0.18)
        self.play_beat(GrowFromCenter(brace_u), FadeIn(u_lab),
                       GrowFromCenter(brace_lam), FadeIn(lam_lab))          # beat 4

        # annotate the overlap u_1^T l_i (one scalar)
        self.play(FadeOut(VGroup(brace_u, u_lab, brace_lam, lam_lab)), run_time=0.4)
        brace_ov = Brace(bdef[4], DOWN, color=VAR)
        ov_lab = Text("a single number: how much lesion l-i projects onto the backbone",
                      font_size=22, color=VAR).next_to(brace_ov, DOWN, buff=0.18)
        self.play_beat(GrowFromCenter(brace_ov), FadeIn(ov_lab))           # beat 5

        # b_i = backbone axis scaled by that overlap — a property of location
        self.play(FadeOut(VGroup(brace_ov, ov_lab)), run_time=0.4)
        bsum = Text("b-i = the backbone axis, scaled by how hard this lesion hits it",
                    font_size=24, color=BACK).next_to(bdef, DOWN, buff=0.7)
        bsum2 = Text("a label-free property of where the lesion sits",
                     font_size=22, color=DIM).next_to(bsum, DOWN, buff=0.2)
        self.play_beat(FadeIn(bsum, shift=UP * 0.2), FadeIn(bsum2))         # beat 6

        # r_i = the residual, everything off the backbone
        self.play(FadeOut(VGroup(bsum, bsum2)), run_time=0.4)
        rdef = VGroup(
            MathTex("r_i", r"=\;x_i - b_i", color=RES).scale(1.1),
            Text("the residual: the part of the map that points OFF the backbone,",
                 font_size=23, color=WHITE),
            Text("into the finer components u-two, u-three, and beyond",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.22).next_to(bdef, DOWN, buff=0.7)
        rdef[0][0].set_color(RES)
        self.play_beat(FadeIn(rdef, lag_ratio=0.3))                        # beat 7


# ----------------------------------------------------------------------
# Scene 2 — the backbone is label-blind:  b_i depends on l_i and C, not y_i
# ----------------------------------------------------------------------
class S2_BackboneLabelFree(NarratedScene):
    scene_key = "S2_BackboneLabelFree"

    def construct(self):
        self.header("The backbone is label-blind")

        # b_i front and center
        bdef = MathTex("b_i", "=", r"\lambda_1", r"\,\big(", "u_1^{\\top} \\ell_i",
                       r"\big)\,", "u_1").scale(1.4).shift(UP * 1.6)
        bdef[0].set_color(BACK); bdef[2].set_color(EIG)
        bdef[4].set_color(VAR); bdef[6].set_color(BACK)
        self.play_beat(Write(bdef))                                        # beat 1

        # what it depends on: l_i (lesion) and C (connectome)
        dep = VGroup(
            MathTex(r"\ell_i", r"\ \text{— the lesion}", color=VAR).scale(0.95),
            MathTex(r"\lambda_1, u_1", r"\ \text{— from the fixed connectome } C",
                    color=EIG).scale(0.95),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).shift(DOWN * 0.2)
        dep[1][1].set_color(WHITE)
        self.play_beat(FadeIn(dep, lag_ratio=0.3))                         # beat 2

        # NOT y_i — the label never enters
        noty = MathTex(r"b_i", r"\ \text{does NOT depend on}\ ", "y_i").scale(1.1)
        noty[0].set_color(BACK); noty[2].set_color(BAD)
        noty.next_to(dep, DOWN, buff=0.7)
        box = SurroundingRectangle(noty, color=BAD, buff=0.2)
        ylab = Text("y-i = the symptom label (impaired = 1, spared = 0)",
                    font_size=22, color=DIM).next_to(box, DOWN, buff=0.22)
        self.play_beat(Write(noty), Create(box), FadeIn(ylab))             # beat 3

        # shuffle labels -> b_i unmoved
        self.play(FadeOut(VGroup(dep, noty, box, ylab)),
                  bdef.animate.scale(0.7).to_edge(UP, buff=1.1), run_time=0.5)
        shuffle = VGroup(
            Text("shuffle the labels  (who is impaired / spared)",
                 font_size=26, color=BAD),
            Text("↓", font_size=30, color=DIM),
            Text("every backbone piece b-i stays exactly where it was",
                 font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.4)
        self.play_beat(LaggedStart(*[FadeIn(s) for s in shuffle],
                                   lag_ratio=0.3))                         # beat 4

        # so bbar^1 and bbar^0 are draws from one pool
        self.play(FadeOut(shuffle), run_time=0.4)
        pool = MathTex(r"\bar b^{\,1}", r"\ \text{and}\ ", r"\bar b^{\,0}",
                       r"\ \text{— two draws from the SAME pool}").scale(1.0)
        pool[0].set_color(BACK); pool[2].set_color(BACK)
        pool.shift(UP * 0.3)
        cap = Text("b-bar-one: backbone mean of the impaired   "
                   "b-bar-zero: backbone mean of the spared",
                   font_size=21, color=DIM).next_to(pool, DOWN, buff=0.35)
        self.play_beat(Write(pool), FadeIn(cap))                           # beat 5

        # interchangeable under label shuffling
        inter = Text("interchangeable under label shuffling —\n"
                     "one population, sliced by labels the backbone cannot feel",
                     font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(cap, DOWN, buff=0.6)
        self.play_beat(FadeIn(inter, shift=UP * 0.2))                      # beat 6


# ----------------------------------------------------------------------
# Scene 3 — form the contrast:  t_v ∝ (bbar^1 - bbar^0) u_{1,v} + (rbar^1 - rbar^0)
# ----------------------------------------------------------------------
class S3_Contrast(NarratedScene):
    scene_key = "S3_Contrast"

    def construct(self):
        self.header("Form the contrast")

        intro = Text("never the average — the CONTRAST between the two groups",
                     font_size=27, color=RES).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # t_v ∝ xbar^1_v - xbar^0_v
        eq = MathTex("t_v", r"\;\propto\;", r"\bar x^{\,1}_v", "-", r"\bar x^{\,0}_v")\
            .scale(1.35).shift(UP * 1.1)
        eq[0].set_color(RES); eq[2].set_color(VAR); eq[4].set_color(VAR)
        cap = Text("t-v: how strongly voxel v separates impaired from spared",
                   font_size=22, color=DIM).next_to(eq, DOWN, buff=0.3)
        self.play_beat(Write(eq), FadeIn(cap), intro.animate.set_opacity(0.4))  # beat 2

        # substitute x = b + r
        self.play(FadeOut(cap), eq.animate.scale(0.7).to_edge(UP, buff=1.1),
                  run_time=0.5)
        sub = Text("substitute  x = b + r  into the difference of means",
                   font_size=25, color=DIM).shift(UP * 1.6)
        full = MathTex("t_v", r"\;\propto\;",
                       r"\big(\bar b^{\,1}-\bar b^{\,0}\big)\,u_{1,v}",
                       "+",
                       r"\big(\bar r^{\,1}_v-\bar r^{\,0}_v\big)").scale(1.1).shift(UP * 0.3)
        full[0].set_color(RES); full[2].set_color(BACK); full[4].set_color(RES)
        self.play_beat(FadeIn(sub), Write(full))                           # beat 3

        # piece 1: the backbone term
        brace_b = Brace(full[2], DOWN, color=BACK)
        b_lab = Text("BACKBONE piece: the gap in backbone means, "
                     "along u-one at voxel v",
                     font_size=22, color=BACK).next_to(brace_b, DOWN, buff=0.18)
        self.play_beat(GrowFromCenter(brace_b), FadeIn(b_lab),
                       sub.animate.set_opacity(0.3))                       # beat 4

        # piece 2: the residual term
        self.play(FadeOut(VGroup(brace_b, b_lab)), run_time=0.4)
        brace_r = Brace(full[4], DOWN, color=RES)
        r_lab = Text("RESIDUAL piece: the gap in the off-backbone parts at voxel v",
                     font_size=22, color=RES).next_to(brace_r, DOWN, buff=0.18)
        self.play_beat(GrowFromCenter(brace_r), FadeIn(r_lab))             # beat 5

        # two terms — which carries the signal?
        self.play(FadeOut(VGroup(brace_r, r_lab, sub)), run_time=0.4)
        ask = VGroup(
            Text("the whole contrast = a backbone piece  +  a residual piece",
                 font_size=25, color=WHITE),
            Text("which one carries the symptom signal?",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3).to_edge(DOWN, buff=1.0)
        self.play_beat(FadeIn(ask, lag_ratio=0.3))                         # beat 6


# ----------------------------------------------------------------------
# Scene 4 — the backbone piece drops out (THE load-bearing step)
# ----------------------------------------------------------------------
class S4_Cancel(NarratedScene):
    scene_key = "S4_Cancel"

    def construct(self):
        self.header("The backbone piece drops out")

        # the full contrast at top, backbone term highlighted
        full = MathTex("t_v", r"\;\propto\;",
                       r"\big(\bar b^{\,1}-\bar b^{\,0}\big)\,u_{1,v}",
                       "+",
                       r"\big(\bar r^{\,1}_v-\bar r^{\,0}_v\big)").scale(1.2).shift(UP * 1.7)
        full[0].set_color(RES); full[2].set_color(BACK); full[4].set_color(RES)
        focus = SurroundingRectangle(full[2], color=BACK, buff=0.12)
        self.play_beat(Write(full), Create(focus))                        # beat 1

        # under permutation the backbone term has the same law
        law = Text("backbone loadings are never relabeled — only the labels move,\n"
                   "so this term has the SAME law in every permutation",
                   font_size=24, color=WHITE, line_spacing=0.8).shift(UP * 0.3)
        self.play_beat(FadeIn(law, shift=UP * 0.2))                       # beat 2

        # label-independent
        ind = MathTex(r"\big(\bar b^{\,1}-\bar b^{\,0}\big)",
                      r"\ \text{is label-independent}").scale(1.0)
        ind[0].set_color(BACK); ind[1].set_color(DIM)
        ind.next_to(law, DOWN, buff=0.5)
        self.play_beat(FadeIn(ind))                                       # beat 3

        # in expectation -> 0
        self.play(FadeOut(VGroup(law, ind)), run_time=0.4)
        toZero = MathTex(r"\mathbb{E}\big[\,\bar b^{\,1}-\bar b^{\,0}\,\big]",
                         r"\;\longrightarrow\;", "0").scale(1.4).shift(UP * 0.4)
        toZero[0].set_color(BACK); toZero[2].set_color(BAD)
        zcap = Text("two backbone means from the same pool — their gap averages out",
                    font_size=23, color=DIM).next_to(toZero, DOWN, buff=0.3)
        self.play_beat(Write(toZero), FadeIn(zcap))                       # beat 4

        # sits identically in observed and permuted -> cannot shift the rank
        same = Text("it sits identically in the observed statistic and in every\n"
                    "permuted one — so it cannot shift the rank of the test",
                    font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(zcap, DOWN, buff=0.5)
        self.play_beat(FadeIn(same, shift=UP * 0.2))                      # beat 5

        # STRIKE IT OUT
        self.play(FadeOut(VGroup(toZero, zcap, same)), run_time=0.4)
        strike = Line(full[2].get_left(), full[2].get_right(),
                      color=BAD, stroke_width=8)
        gone = Text("contributes nothing to the permutation distribution",
                    font_size=24, color=BAD).next_to(full, DOWN, buff=0.9)
        self.play_beat(Create(strike), full[2].animate.set_opacity(0.35),
                       FadeIn(gone))                                      # beat 6

        # the cancellation, on the algebra
        moral = VGroup(
            Text("THE CANCELLATION, on the algebra:", font_size=25, color=RES),
            Text("the huge offset that dominated any average map",
                 font_size=24, color=WHITE),
            Text("drops out of the contrast exactly.",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                      # beat 7


# ----------------------------------------------------------------------
# Scene 5 — what survives is signal; camera vs court, made algebraic
# ----------------------------------------------------------------------
class S5_Moral(NarratedScene):
    scene_key = "S5_Moral"

    def construct(self):
        self.header("What survives is signal")

        intro = Text("after the backbone strikes out, one term is left standing",
                     font_size=27, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # only the residual survives
        eq = MathTex("t_v", r"\;\propto\;",
                     r"\bar r^{\,1}_v - \bar r^{\,0}_v").scale(1.5).shift(UP * 1.1)
        eq[0].set_color(RES); eq[2].set_color(RES)
        cap = Text("only the label-correlated residual — the part that tracks the symptom",
                   font_size=23, color=DIM).next_to(eq, DOWN, buff=0.3)
        self.play_beat(Write(eq), FadeIn(cap), intro.animate.set_opacity(0.4))  # beat 2

        # one mechanism, opposite fates
        self.play(FadeOut(VGroup(cap, intro)),
                  eq.animate.scale(0.7).to_edge(UP, buff=1.0), run_time=0.5)
        twofate = VGroup(
            Text("same hub structure, opposite fates:", font_size=26, color=WHITE),
        ).shift(UP * 1.3)
        self.play_beat(FadeIn(twofate))                                   # beat 3

        # villain in average, vanishes in contrast
        split = VGroup(
            VGroup(
                Text("in the AVERAGE", font_size=25, color=BAD),
                Text("the villain that", font_size=22, color=DIM),
                Text("buries the signal", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.12),
            MathTex(r"\Big|", color=DIM).scale(2.2),
            VGroup(
                Text("in the CONTRAST", font_size=25, color=BACK),
                Text("a label-free constant", font_size=22, color=DIM),
                Text("that simply vanishes", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.12),
        ).arrange(RIGHT, buff=0.9).next_to(twofate, DOWN, buff=0.5)
        self.play_beat(FadeIn(split, lag_ratio=0.2))                      # beat 4

        # camera vs court, made algebraic
        self.play(FadeOut(VGroup(twofate, split)), run_time=0.4)
        cc = VGroup(
            Text("camera vs court, made algebraic:", font_size=27, color=RES),
            Text("the average PHOTOGRAPHS the backbone", font_size=25, color=DIM),
            Text("the contrast JUDGES the residual", font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.0)
        self.play_beat(FadeIn(cc, lag_ratio=0.3))                         # beat 5

        # the numbers: same-symptom r=0.44
        self.play(FadeOut(cc), run_time=0.4)
        r1 = MathTex(r"\text{same-symptom}", r"\quad r = 0.44").scale(1.1).shift(UP * 1.3)
        r1[1].set_color(BACK)
        self.play_beat(Write(r1))                                         # beat 6

        # different r=0.09, degree r=0.16
        r2 = MathTex(r"\text{different-symptom}", r"\quad r = 0.09").scale(1.0)
        r2[1].set_color(DIM)
        r3 = MathTex(r"\text{degree map}", r"\qquad\quad r = 0.16").scale(1.0)
        r3[1].set_color(BAD)
        rows = VGroup(r2, r3).arrange(DOWN, buff=0.3).next_to(r1, DOWN, buff=0.4)
        self.play_beat(Write(r2), Write(r3))                              # beat 7

        # the witness: 0 false positives / 1000 at t>10
        witness = MathTex(r"t > 10:\quad", r"0\ \text{false positives}",
                          r"\ /\ 1000\ \text{iterations}").scale(1.05)
        witness[1].set_color(RES)
        witness.to_edge(DOWN, buff=0.9)
        wcap = Text("the backbone made no ghosts", font_size=22, color=DIM)\
            .next_to(witness, DOWN, buff=0.2)
        self.play_beat(Write(witness), FadeIn(wcap))                      # beat 8
