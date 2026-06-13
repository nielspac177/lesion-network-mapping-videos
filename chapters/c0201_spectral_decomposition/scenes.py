"""c0201_spectral_decomposition — "The connectome has a spectrum".

Mini-video of the LNM series. We take the fixed connectome C apart into its
spectrum: the eigen-equation C u_j = lambda_j u_j, the full spectral decomposition
C = sum_j lambda_j u_j u_j^T (each term a rank-one pattern), the ordering
lambda_1 >= lambda_2 >= ... >= 0, a concrete 3x3 example with one big eigenvalue,
and finally we name the leading pattern u_1 the BACKBONE.

All math comes from responses/lnm_critique/sections/02_what_is_entailed.md:
  C = sum_j lambda_j u_j u_j^T,  lambda_1 >= lambda_2 >= ... >= 0,
  m_i = C ell_i = sum_j lambda_j (u_j^T ell_i) u_j, leading term lambda_1 c_1 u_1.
The 3-voxel spectrum (4.0, 0.3, 0.1) is the source's own worked connectome.

BALANCED FRAMING: the backbone is geometry, a property of C's spectrum. It explains
why AVERAGE maps look alike; it says nothing yet about whether a symptom CONTRAST
carries signal. No verdict on the method here.

Render:
  MEDIA=$HOME/lnm_media/c0201_spectral_decomposition ./render.sh \
      chapters/c0201_spectral_decomposition/scenes.py -q ql \
      S1_Motivation S2_Eigen S3_Decomposition S4_Ordering S5_Example S6_Backbone
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES

# The source's 3-voxel connectome (sections/01 / 02) and its spectrum.
C3 = [["2.635", "1.488", "1.054"],
      ["1.488", "1.225", "0.597"],
      ["1.054", "0.597", "0.540"]]
SPECTRUM = ["4.0", "0.3", "0.1"]   # eigenvalues of C3, ordered (source's numbers)


# ----------------------------------------------------------------------
# S1 — Motivation: why decompose C at all.
# ----------------------------------------------------------------------
class S1_Motivation(NarratedScene):
    scene_key = "S1_Motivation"

    def construct(self):
        title = Text("The connectome has a spectrum", font_size=44, color=WHITE)
        sub = Text("taking the fixed matrix C apart, pattern by pattern",
                   font_size=24, color=DIM).next_to(title, DOWN, buff=0.3)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.35),
                  FadeOut(sub), run_time=0.6)

        # every map is a column-combination of one fixed C
        eq = MathTex("m", "=", "C", r"\ell").scale(1.7).shift(UP * 1.6)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        only = Text("every map the method makes is built from one fixed matrix C",
                    font_size=25, color=DIM).next_to(eq, DOWN, buff=0.5)
        self.play_beat(Write(eq), FadeIn(only))

        # a grid of numbers hides the structure
        self.play(FadeOut(VGroup(eq, only)), run_time=0.4)
        Cmat = Matrix(C3, h_buff=1.5, v_buff=0.9, bracket_h_buff=0.16)\
            .scale(0.85).shift(LEFT * 1.2)
        Clab = MathTex("C", color=WHITE).scale(1.3).next_to(Cmat, LEFT, buff=0.45)
        hide = Text("a grid of numbers hides its structure",
                    font_size=25, color=DIM).next_to(Cmat, DOWN, buff=0.5)
        self.play_beat(FadeIn(Cmat), Write(Clab), FadeIn(hide))

        # better coordinates: patterns + weights (C symmetric)
        self.play(FadeOut(VGroup(Cmat, Clab, hide)), run_time=0.4)
        better = VGroup(
            Text("C is symmetric — so it splits into natural patterns,",
                 font_size=28, color=WHITE),
            Text("each pattern carrying a weight.", font_size=28, color=BACK),
        ).arrange(DOWN, buff=0.35).shift(UP * 0.3)
        self.play_beat(FadeIn(better[0]), FadeIn(better[1], shift=UP * 0.15))

        # the spectrum: what it tells us
        self.play(FadeOut(better), run_time=0.4)
        spec = VGroup(
            Text("That decomposition is the SPECTRUM.", font_size=30, color=RES),
            Text("Before any patient: which directions C amplifies,",
                 font_size=26, color=DIM),
            Text("and the cleanest way to see why different lesions",
                 font_size=26, color=DIM),
            Text("produced nearly the same map.", font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(LaggedStart(*[FadeIn(s, shift=UP * 0.12) for s in spec],
                                   lag_ratio=0.3))


# ----------------------------------------------------------------------
# S2 — The eigen-equation C u_j = lambda_j u_j.
# ----------------------------------------------------------------------
class S2_Eigen(NarratedScene):
    scene_key = "S2_Eigen"

    def construct(self):
        self.header("The eigen-equation")

        eq = MathTex("C", r"\,u_j", "=", r"\lambda_j", r"\,u_j").scale(1.8).shift(UP * 1.7)
        eq[0].set_color(WHITE); eq[1].set_color(BACK)
        eq[3].set_color(EIG); eq[4].set_color(BACK)
        same = Text("C returns the same vector — only rescaled",
                    font_size=26, color=DIM).next_to(eq, DOWN, buff=0.5)
        self.play_beat(Write(eq), FadeIn(same))

        # u_j = eigenvector = a connectome pattern
        self.play(FadeOut(same), run_time=0.3)
        br_u = Brace(eq[1], DOWN, color=BACK)
        u_lab = br_u.get_text("eigenvector").set_color(BACK).scale(0.85)
        u_gloss = Text("a connectome pattern: a fixed brain-wide shape\n"
                       "that C does not rotate, only stretches",
                       font_size=23, color=BACK, line_spacing=0.9)\
            .next_to(br_u, DOWN, buff=0.4)
        self.play_beat(GrowFromCenter(br_u), FadeIn(u_lab), FadeIn(u_gloss))

        # lambda_j = eigenvalue = how much of C the pattern carries
        self.play(FadeOut(VGroup(br_u, u_lab, u_gloss)), run_time=0.3)
        br_l = Brace(eq[3], DOWN, color=EIG)
        l_lab = br_l.get_text("eigenvalue").set_color(EIG).scale(0.85)
        l_gloss = Text("how much of C this pattern carries:\n"
                       "how strongly C amplifies anything along u-j",
                       font_size=23, color=EIG, line_spacing=0.9)\
            .next_to(br_l, DOWN, buff=0.4)
        self.play_beat(GrowFromCenter(br_l), FadeIn(l_lab), FadeIn(l_gloss))

        # orthonormal: unit length + perpendicular (inner product zero)
        self.play(FadeOut(VGroup(eq, br_l, l_lab, l_gloss)), run_time=0.4)
        ortho = MathTex(r"u_j^\top u_k", "=",
                        r"\begin{cases} 1 & j = k\\ 0 & j \ne k\end{cases}")\
            .scale(1.1).shift(UP * 1.3)
        ortho[0].set_color(BACK)
        ocap = VGroup(
            Text("orthonormal patterns:", font_size=26, color=WHITE),
            Text("each u-j has unit length; different patterns are perpendicular,",
                 font_size=24, color=DIM),
            Text("their inner product is zero.", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(ortho, DOWN, buff=0.5)
        self.play_beat(Write(ortho), FadeIn(ocap[0]))

        # clean set of axes
        axes = Text("a clean set of axes — any lesion or map is a\n"
                    "combination of these patterns, with no overlap",
                    font_size=24, color=BACK, line_spacing=0.9)\
            .to_edge(DOWN, buff=0.6)
        self.play_beat(FadeIn(ocap[1]), FadeIn(ocap[2]), FadeIn(axes))

        # the sorting-machine reading
        self.play(FadeOut(VGroup(ortho, ocap, axes)), run_time=0.4)
        sort = VGroup(
            Text("Read the equation as a sorting machine:", font_size=29, color=WHITE),
            Text("feed C a pattern, out comes the same pattern", font_size=27, color=DIM),
            Text("with a price tag  lambda-j  stamped on it.", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(LaggedStart(*[FadeIn(s, shift=RIGHT * 0.15) for s in sort],
                                   lag_ratio=0.35))


# ----------------------------------------------------------------------
# S3 — The full decomposition C = sum_j lambda_j u_j u_j^T.
# ----------------------------------------------------------------------
class S3_Decomposition(NarratedScene):
    scene_key = "S3_Decomposition"

    def construct(self):
        self.header(r"The spectral decomposition")

        eq = MathTex("C", "=", r"\sum_j", r"\lambda_j", r"\,u_j", r"u_j^\top")\
            .scale(1.5).shift(UP * 1.9)
        eq[0].set_color(WHITE); eq[3].set_color(EIG)
        eq[4].set_color(BACK); eq[5].set_color(BACK)
        rebuild = Text("collect every pattern and its weight — and you rebuild C",
                       font_size=25, color=DIM).next_to(eq, DOWN, buff=0.45)
        self.play_beat(Write(eq), FadeIn(rebuild))

        # the outer product u_j u_j^T is a MATRIX
        self.play(FadeOut(rebuild), run_time=0.3)
        br_op = Brace(eq[4:6], DOWN, color=BACK)
        op_lab = br_op.get_text("outer product").set_color(BACK).scale(0.85)
        op_gloss = MathTex(r"u_j\, u_j^\top", r"\ =\ ",
                           r"(\text{column}) \times (\text{row}) \ =\ \text{a matrix}")\
            .scale(0.85).next_to(br_op, DOWN, buff=0.45)
        op_gloss[0].set_color(BACK)
        self.play_beat(GrowFromCenter(br_op), FadeIn(op_lab), Write(op_gloss))

        # it is rank one
        self.play(FadeOut(VGroup(br_op, op_lab, op_gloss)), run_time=0.3)
        rankone = VGroup(
            Text("the simplest matrix there is:  RANK ONE", font_size=28, color=RES),
            Text("every column is just a rescaled copy of the one pattern u-j",
                 font_size=25, color=DIM),
        ).arrange(DOWN, buff=0.35).next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(rankone[0]), FadeIn(rankone[1], shift=UP * 0.12))

        # each term is one rank-one layer with intensity lambda_j
        self.play(FadeOut(rankone), run_time=0.3)
        layer = MathTex(r"\lambda_j", r"\,u_j u_j^\top").scale(1.4)\
            .next_to(eq, DOWN, buff=0.7)
        layer[0].set_color(EIG); layer[1].set_color(BACK)
        lcap = VGroup(
            Text("one rank-one LAYER:", font_size=26, color=WHITE),
            Text("the pure pattern u-j, intensity set by its eigenvalue lambda-j",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(layer, DOWN, buff=0.45)
        self.play_beat(Write(layer), FadeIn(lcap))

        # add the layers -> short stack of weighted patterns
        self.play(FadeOut(VGroup(layer, lcap)), run_time=0.3)
        stack = VGroup(
            Text("add the layers and they reassemble the connectome.",
                 font_size=27, color=WHITE),
            Text("C is not a grid of arbitrary numbers —", font_size=26, color=DIM),
            Text("it is a short stack of weighted patterns.", font_size=27, color=BACK),
        ).arrange(DOWN, buff=0.3).next_to(eq, DOWN, buff=0.7)
        self.play_beat(LaggedStart(*[FadeIn(s, shift=UP * 0.12) for s in stack],
                                   lag_ratio=0.3))

        # exact, lossless, any symmetric matrix
        self.play(FadeOut(stack), run_time=0.3)
        exact = VGroup(
            Text("This is the spectral decomposition.", font_size=29, color=RES),
            Text("Exact. Lossless. Valid for any symmetric matrix —",
                 font_size=25, color=DIM),
            Text("so it always applies to C.", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.3).next_to(eq, DOWN, buff=0.7)
        self.play_beat(LaggedStart(*[FadeIn(s) for s in exact], lag_ratio=0.3))


# ----------------------------------------------------------------------
# S4 — Ordering lambda_1 >= lambda_2 >= ... >= 0 and "dominant".
# ----------------------------------------------------------------------
class S4_Ordering(NarratedScene):
    scene_key = "S4_Ordering"

    def construct(self):
        self.header("Ordering the spectrum")

        order = MathTex(r"\lambda_1", r"\ \ge\ ", r"\lambda_2", r"\ \ge\ ",
                        r"\lambda_3", r"\ \ge\ \cdots\ \ge\ ", "0")\
            .scale(1.5).shift(UP * 1.7)
        for i in (0, 2, 4):
            order[i].set_color(EIG)
        order[6].set_color(WHITE)
        ocap = Text("list the eigenvalues from largest to smallest",
                    font_size=25, color=DIM).next_to(order, DOWN, buff=0.45)
        self.play_beat(Write(order), FadeIn(ocap))

        # positive semidefinite: every lambda >= 0
        self.play(FadeOut(ocap), run_time=0.3)
        psd = MathTex(r"\lambda_j", r"\ \ge\ ", "0",
                      r"\quad\text{for all } j").scale(1.1).next_to(order, DOWN, buff=0.6)
        psd[0].set_color(EIG); psd[2].set_color(WHITE)
        psdcap = Text("C is built from connectivity — positive semidefinite:\n"
                      "the weights are never negative",
                      font_size=24, color=DIM, line_spacing=0.9)\
            .next_to(psd, DOWN, buff=0.4)
        self.play_beat(Write(psd), FadeIn(psdcap))

        # lambda_1 / u_1 is the loudest layer
        self.play(FadeOut(VGroup(psd, psdcap)), run_time=0.3)
        loud = MathTex(r"\lambda_1", r"\,u_1 u_1^\top").scale(1.3)\
            .next_to(order, DOWN, buff=0.6)
        loud[0].set_color(EIG); loud[1].set_color(BACK)
        loudcap = Text("the first pattern u-1 carries the largest weight lambda-1:\n"
                       "the loudest layer in the stack",
                       font_size=24, color=BACK, line_spacing=0.9)\
            .next_to(loud, DOWN, buff=0.4)
        self.play_beat(Write(loud), FadeIn(loudcap))

        # the spectral gap lambda_2 / lambda_1
        self.play(FadeOut(VGroup(loud, loudcap)), run_time=0.3)
        gap = MathTex(r"\text{spectral gap}", r"\ =\ ",
                      r"\frac{\lambda_2}{\lambda_1}").scale(1.2)\
            .next_to(order, DOWN, buff=0.6)
        gap[2].set_color(EIG)
        gapcap = Text("small ratio  ->  the second pattern is a whisper\n"
                      "next to the first",
                      font_size=24, color=DIM, line_spacing=0.9)\
            .next_to(gap, DOWN, buff=0.4)
        self.play_beat(Write(gap), FadeIn(gapcap))

        # what "dominant" means precisely
        self.play(FadeOut(VGroup(gap, gapcap)), run_time=0.3)
        dom = VGroup(
            Text("DOMINANT, precisely:", font_size=28, color=RES),
            Text("if lambda-1 dwarfs the rest, then anything C touches", font_size=25, color=DIM),
            Text("comes out leaning heavily toward u-1.", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.3).next_to(order, DOWN, buff=0.6)
        self.play_beat(LaggedStart(*[FadeIn(s, shift=UP * 0.12) for s in dom],
                                   lag_ratio=0.3))

        # property of the matrix alone — before the disease votes
        self.play(FadeOut(dom), run_time=0.3)
        prop = VGroup(
            Text("This ordering is a property of the matrix alone.",
                 font_size=27, color=WHITE),
            Text("It is fixed before a single lesion is chosen —", font_size=25, color=DIM),
            Text("before the disease gets a vote.", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.3).next_to(order, DOWN, buff=0.6)
        self.play_beat(LaggedStart(*[FadeIn(s) for s in prop], lag_ratio=0.3))


# ----------------------------------------------------------------------
# S5 — A concrete 3x3 example with eigenvalues 4.0, 0.3, 0.1.
# ----------------------------------------------------------------------
class S5_Example(NarratedScene):
    scene_key = "S5_Example"

    def construct(self):
        self.header("A concrete 3x3 spectrum")

        # C3 and a note that we can compute its spectrum
        Cmat = Matrix(C3, h_buff=1.4, v_buff=0.85, bracket_h_buff=0.16)\
            .scale(0.75).shift(LEFT * 3.0 + UP * 0.4)
        Clab = MathTex("C", color=WHITE).scale(1.1).next_to(Cmat, UP, buff=0.2)
        note = Text("the source's three-voxel connectome —\n"
                    "we can compute its spectrum",
                    font_size=23, color=DIM, line_spacing=0.9)\
            .next_to(Cmat, RIGHT, buff=0.7)
        self.play_beat(FadeIn(Cmat), Write(Clab), FadeIn(note))

        # the three eigenvalues, ordered
        self.play(FadeOut(note), run_time=0.3)
        spec = MathTex(r"\lambda_1 = 4.0", r",\quad",
                       r"\lambda_2 = 0.3", r",\quad",
                       r"\lambda_3 = 0.1").scale(0.95)\
            .next_to(Cmat, RIGHT, buff=0.7)
        spec[0].set_color(EIG); spec[2].set_color(EIG); spec[4].set_color(EIG)
        speccap = Text("already ordered, all non-negative", font_size=22, color=DIM)\
            .next_to(spec, DOWN, buff=0.35)
        self.play_beat(Write(spec), FadeIn(speccap))

        # one eigenvalue towers — bar chart
        self.play(FadeOut(VGroup(Cmat, Clab, spec, speccap)),
                  run_time=0.4)
        vals = [4.0, 0.3, 0.1]
        bars = VGroup()
        labs = VGroup()
        for i, v in enumerate(vals):
            bar = Rectangle(width=0.9, height=max(v, 0.05) * 1.0,
                            fill_color=(BACK if i == 0 else DIM),
                            fill_opacity=0.9, stroke_width=0)
            bars.add(bar)
        bars.arrange(RIGHT, buff=0.9, aligned_edge=DOWN).shift(DOWN * 0.6)
        for i, (v, bar) in enumerate(zip(vals, bars)):
            lab = MathTex(rf"\lambda_{i+1} = {v}", color=EIG).scale(0.65)\
                .next_to(bar, UP, buff=0.15)
            labs.add(lab)
        towers = Text("one eigenvalue towers over the others",
                      font_size=26, color=RES).to_edge(UP, buff=1.1)
        self.play_beat(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars],
                                   lag_ratio=0.25),
                       *[FadeIn(l) for l in labs], FadeIn(towers))

        # the spectral gap < 1/10
        gap = MathTex(r"\frac{\lambda_2}{\lambda_1}", "=",
                      r"\frac{0.3}{4.0}", r"\approx", "0.075")\
            .scale(0.95).to_edge(DOWN, buff=0.8)
        gap[0].set_color(EIG); gap[2].set_color(EIG); gap[4].set_color(RES)
        self.play_beat(Write(gap))

        # nearly rank one  C ~ lambda_1 u_1 u_1^T
        self.play(FadeOut(VGroup(bars, labs, towers, gap)), run_time=0.4)
        approx = MathTex("C", r"\ \approx\ ", r"\lambda_1", r"\,u_1 u_1^\top")\
            .scale(1.3).shift(UP * 0.6)
        approx[0].set_color(WHITE); approx[2].set_color(EIG); approx[3].set_color(BACK)
        acap = Text("for practical purposes, nearly rank one",
                    font_size=26, color=DIM).next_to(approx, DOWN, buff=0.5)
        self.play_beat(Write(approx), FadeIn(acap))

        # this is why different-voxel lesions gave near-parallel maps
        self.play(FadeOut(VGroup(approx, acap)), run_time=0.3)
        why = VGroup(
            Text("This single tall eigenvalue is exactly why", font_size=27, color=WHITE),
            Text("two lesions in different voxels gave maps", font_size=27, color=DIM),
            Text("only a few degrees apart — both inherited u-1.",
                 font_size=27, color=BACK),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(LaggedStart(*[FadeIn(s, shift=UP * 0.12) for s in why],
                                   lag_ratio=0.3))


# ----------------------------------------------------------------------
# S6 — Name u_1 the backbone; preview that maps lean on it (balanced).
# ----------------------------------------------------------------------
class S6_Backbone(NarratedScene):
    scene_key = "S6_Backbone"

    def construct(self):
        self.header("The backbone")

        name = VGroup(
            MathTex("u_1", color=BACK).scale(2.0),
            Text("the BACKBONE of the connectome", font_size=30, color=BACK),
            Text("the single dominant direction baked into C", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.35).shift(UP * 0.6)
        self.play_beat(FadeIn(name[0], scale=1.2), FadeIn(name[1], shift=UP * 0.15),
                       FadeIn(name[2]))

        # write any map in the spectral basis
        self.play(FadeOut(name), run_time=0.4)
        spec = MathTex("m", "=", "C", r"\ell", "=",
                       r"\sum_j", r"\lambda_j", r"(u_j^\top \ell)", r"\,u_j")\
            .scale(1.2).shift(UP * 1.7)
        spec[0].set_color(VAR); spec[2].set_color(WHITE); spec[3].set_color(VAR)
        spec[6].set_color(EIG); spec[7].set_color(VAR); spec[8].set_color(BACK)
        self.play_beat(Write(spec))

        # the loading u_j^T ell = inner product
        br = Brace(spec[7], DOWN, color=VAR)
        br_lab = br.get_text("loading").set_color(VAR).scale(0.85)
        gloss = Text("how much the lesion points along pattern j —\n"
                     "the inner product of the lesion with that connectome shape",
                     font_size=23, color=DIM, line_spacing=0.9)\
            .next_to(br, DOWN, buff=0.4)
        self.play_beat(GrowFromCenter(br), FadeIn(br_lab), FadeIn(gloss))

        # the leading term is largest because lambda_1 is largest
        self.play(FadeOut(VGroup(br, br_lab, gloss)), run_time=0.3)
        lead = MathTex(r"\lambda_1", r"\,(u_1^\top \ell)", r"\,u_1")\
            .scale(1.3).next_to(spec, DOWN, buff=0.7)
        lead[0].set_color(EIG); lead[1].set_color(VAR); lead[2].set_color(BACK)
        leadcap = Text("the leading term — largest by far, because lambda-1 is the largest weight",
                       font_size=23, color=DIM).next_to(lead, DOWN, buff=0.4)
        self.play_beat(Write(lead), FadeIn(leadcap))

        # so average maps get dragged toward the backbone (geometry, not verdict)
        self.play(FadeOut(VGroup(spec, lead, leadcap)), run_time=0.4)
        drag = VGroup(
            Text("So every AVERAGE map is dragged toward the backbone.",
                 font_size=28, color=WHITE),
            Text("That is geometry — a fact about the spectrum of C —",
                 font_size=25, color=DIM),
            Text("not yet a verdict on the method.", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.4)
        self.play_beat(LaggedStart(*[FadeIn(s, shift=UP * 0.12) for s in drag],
                                   lag_ratio=0.3))

        # balanced preview: average vs contrast
        self.play(drag.animate.scale(0.7).to_edge(UP, buff=1.2), run_time=0.4)
        preview = VGroup(
            Text("It explains why AVERAGE maps look alike.", font_size=27, color=BACK),
            Text("It says nothing yet about whether a symptom", font_size=26, color=WHITE),
            Text("CONTRAST carries signal.", font_size=27, color=VAR),
            Text("That contrast is the next chapter's question.", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.28)
        self.play_beat(LaggedStart(*[FadeIn(s, shift=UP * 0.1) for s in preview],
                                   lag_ratio=0.3))
