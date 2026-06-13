"""c0204_three_voxel_example — Three lesions, one direction.

The worked example behind the backbone-convergence claim of
sections/02_what_is_entailed.md. We take the source's three-voxel connectome,
read off its spectrum (eigenvalues 4.0, 0.3, 0.1; gap 0.075; u_1 ~ (0.80,0.50,0.33)),
then show that three completely different single-voxel lesions — each just a column
of C — funnel to within about 8 degrees of u_1. The reason is the wide spectral
gap, via the cosine-squared bound. Geometry, not biology.

BALANCED FRAMING: convergence of maps toward u_1 is a property of C's spectrum. It
explains why AVERAGE maps look alike; it does NOT say a symptom CONTRAST carries no
signal (the backbone cancels from a difference of maps). The method is not debunked.

All numbers come from the source / chapter spec:
  C = [[2.635,1.488,1.054],[1.488,1.225,0.597],[1.054,0.597,0.540]]
  eigenvalues lambda = (4.0, 0.3, 0.1);  ratio lambda_2/lambda_1 = 0.075
  u_1 ~ (0.80, 0.50, 0.33)
  single-voxel lesions -> columns of C ; angles to u_1 ~ 2.9, 5.5, 7.6 degrees.

Render:
  MEDIA=$HOME/lnm_media/c0204_three_voxel_example ./render.sh \
      chapters/c0204_three_voxel_example/scenes.py -q ql \
      S1_Spectrum S2_OneLesion S3_AllThree S4_Funnel S5_Moral
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES

# The source's 3-voxel connectome (sections/01_the_charge_formalized.md, reused here).
C3 = [["2.635", "1.488", "1.054"],
      ["1.488", "1.225", "0.597"],
      ["1.054", "0.597", "0.540"]]

# Columns of C (a single-voxel lesion hands back a column) and their angles to u_1.
COL1 = ["2.635", "1.488", "1.054"]
COL2 = ["1.488", "1.225", "0.597"]
COL3 = ["1.054", "0.597", "0.540"]
ANG1, ANG2, ANG3 = r"2.9^\circ", r"5.5^\circ", r"7.6^\circ"


# ----------------------------------------------------------------------
# S1 — The three-voxel connectome and its spectrum.
# ----------------------------------------------------------------------
class S1_Spectrum(NarratedScene):
    scene_key = "S1_Spectrum"

    def construct(self):
        title = Text("Three lesions, one direction", font_size=44, color=WHITE)
        sub = Text("the backbone-convergence example, by hand",
                   font_size=24, color=DIM).next_to(title, DOWN, buff=0.3)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))
        self.play(FadeOut(VGroup(title, sub)), run_time=0.5)

        # The 3-voxel C.
        self.header("The connectome  C  (3 voxels)")
        Cmat = Matrix(C3, h_buff=1.6, v_buff=1.0, bracket_h_buff=0.18)\
            .scale(0.9).shift(LEFT * 1.2 + UP * 0.2)
        Clab = MathTex("C", color=WHITE).scale(1.5).next_to(Cmat, LEFT, buff=0.5)
        ccap = Text("symmetric, 3 by 3: one row and column per voxel",
                    font_size=23, color=DIM).next_to(Cmat, DOWN, buff=0.5)
        self.play_beat(FadeIn(Cmat), Write(Clab), FadeIn(ccap))

        # Voxel 1 is the hub: diagonal.
        ent = Cmat.get_entries()  # row-major: 0,1,2 / 3,4,5 / 6,7,8
        hub_box = SurroundingRectangle(ent[0], color=BACK, buff=0.12)
        hub_lab = Text("hub: voxel 1", font_size=21, color=BACK)\
            .next_to(Cmat, UP, buff=0.25)
        diag_box = VGroup(
            SurroundingRectangle(ent[4], color=DIM, buff=0.10),
            SurroundingRectangle(ent[8], color=DIM, buff=0.10),
        )
        self.play_beat(Create(hub_box), FadeIn(hub_lab), Create(diag_box))

        # Eigendecomposition: C = sum_j lambda_j u_j u_j^T.
        self.play(FadeOut(VGroup(Cmat, Clab, ccap, hub_box, hub_lab, diag_box)),
                  run_time=0.4)
        eig = MathTex("C", "=", r"\sum_j", r"\lambda_j", r"\,u_j", r"u_j^{\top}")\
            .scale(1.4).shift(UP * 1.7)
        eig[0].set_color(WHITE); eig[3].set_color(EIG); eig[4].set_color(BACK)
        eig[5].set_color(BACK)
        br_l = Brace(eig[3], DOWN, color=DIM)
        l_lab = br_l.get_text("eigenvalue: a strength").set_color(EIG).scale(0.7)
        br_u = Brace(VGroup(eig[4], eig[5]), DOWN, color=DIM)
        u_lab = br_u.get_text("eigenvector: a direction").set_color(BACK).scale(0.7)
        self.play_beat(Write(eig), GrowFromCenter(br_l), FadeIn(l_lab),
                       GrowFromCenter(br_u), FadeIn(u_lab), lag_ratio=0.2)

        # The three eigenvalues; one dominates.
        self.play(FadeOut(VGroup(br_l, l_lab, br_u, u_lab)),
                  eig.animate.scale(0.7).to_edge(UP, buff=1.1), run_time=0.5)
        lams = MathTex(r"\lambda_1 = 4.0", r"\quad", r"\lambda_2 = 0.3",
                       r"\quad", r"\lambda_3 = 0.1").scale(1.1)
        lams[0].set_color(EIG); lams[2].set_color(EIG); lams[4].set_color(EIG)
        lams.shift(UP * 0.3)
        dom = Text("one direction dominates:  lambda 1  is more than 10x  lambda 2",
                   font_size=26, color=RES).next_to(lams, DOWN, buff=0.6)
        self.play_beat(Write(lams), FadeIn(dom))

        # The spectral gap and u_1 (the backbone).
        self.play(FadeOut(VGroup(lams, dom)), run_time=0.4)
        gap = MathTex(r"\frac{\lambda_2}{\lambda_1}", "=", r"\frac{0.3}{4.0}",
                      "=", "0.075").scale(1.2).shift(UP * 0.6)
        gap[0].set_color(EIG); gap[4].set_color(RES)
        gap_lab = Text("the spectral gap — small means a wide gap",
                       font_size=24, color=DIM).next_to(gap, DOWN, buff=0.4)
        u1 = MathTex(r"u_1", r"\approx", r"(0.80,\ 0.50,\ 0.33)").scale(1.1)\
            .next_to(gap_lab, DOWN, buff=0.6)
        u1[0].set_color(BACK); u1[2].set_color(BACK)
        u1cap = Text("the backbone direction", font_size=23, color=BACK)\
            .next_to(u1, DOWN, buff=0.3)
        self.play_beat(Write(gap), FadeIn(gap_lab), Write(u1), FadeIn(u1cap))


# ----------------------------------------------------------------------
# S2 — One single-voxel lesion -> a column of C -> its angle to u_1.
# ----------------------------------------------------------------------
class S2_OneLesion(NarratedScene):
    scene_key = "S2_OneLesion"

    def construct(self):
        self.header("One lesion: a column of  C")

        # The single-voxel lesion ell = e_1.
        lvec = Matrix([["1"], ["0"], ["0"]], v_buff=0.8).scale(0.8)\
            .shift(LEFT * 3.4 + UP * 0.6)
        lvec.get_entries().set_color(VAR)
        llab = MathTex(r"\ell", color=VAR).scale(1.2).next_to(lvec, UP, buff=0.2)
        lcap = Text("destroy a single voxel\n(here, voxel 1)", font_size=21,
                    color=VAR, line_spacing=0.9).next_to(lvec, DOWN, buff=0.4)
        self.play_beat(FadeIn(lvec), Write(llab), FadeIn(lcap))

        # m = C ell selects column 1.
        eq = MathTex("m", "=", "C", r"\ell", "=", r"\text{col}_1(C)")\
            .scale(1.0).next_to(lvec, RIGHT, buff=0.9).shift(UP * 0.2)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        eq[5].set_color(BACK)
        mvec = Matrix([COL1[0:1], COL1[1:2], COL1[2:3]], v_buff=0.8)\
            .scale(0.8).next_to(eq, DOWN, buff=0.5)
        mvec.get_entries().set_color(RES)
        self.play_beat(Write(eq), FadeIn(mvec))

        # The angle theta to u_1, via the cosine.
        self.play(FadeOut(VGroup(lvec, llab, lcap, eq, mvec)), run_time=0.5)
        cos = MathTex(r"\cos\theta", "=",
                      r"\frac{u_1^{\top} m}{\|u_1\|\,\|m\|}").scale(1.3).shift(UP * 1.2)
        cos[0].set_color(RES)
        br_num = Brace(cos[2][0:5], UP, color=DIM)
        num_lab = br_num.get_text("inner product: overlap of m with the backbone")\
            .set_color(BACK).scale(0.6)
        br_den = Brace(cos[2][6:], DOWN, color=DIM)
        den_lab = br_den.get_text("the two lengths").set_color(DIM).scale(0.65)
        self.play_beat(Write(cos), GrowFromCenter(br_num), FadeIn(num_lab),
                       GrowFromCenter(br_den), FadeIn(den_lab), lag_ratio=0.2)

        # What theta means geometrically.
        self.play(FadeOut(VGroup(br_num, num_lab, br_den, den_lab)), run_time=0.3)
        scale_grp = VGroup(
            MathTex(r"\theta = 0^\circ", r"\ \to\ ", r"\text{on the backbone}"),
            MathTex(r"\theta = 90^\circ", r"\ \to\ ", r"\text{off it entirely}"),
        ).arrange(DOWN, buff=0.4).next_to(cos, DOWN, buff=0.7)
        scale_grp[0][0].set_color(BACK); scale_grp[0][2].set_color(BACK)
        scale_grp[1][0].set_color(BAD); scale_grp[1][2].set_color(BAD)
        self.play_beat(Write(scale_grp[0]), Write(scale_grp[1]), lag_ratio=0.3)

        # The actual angle: ~2.9 degrees.
        self.play(FadeOut(VGroup(cos, scale_grp)), run_time=0.4)
        ans = MathTex(r"\theta", r"\approx", ANG1).scale(1.6)
        ans[0].set_color(RES); ans[2].set_color(RES)
        anscap = Text("the single-voxel map already sits almost on the backbone",
                      font_size=25, color=BACK).next_to(ans, DOWN, buff=0.6)
        self.play_beat(Write(ans), FadeIn(anscap))


# ----------------------------------------------------------------------
# S3 — All three single-voxel lesions; three angles.
# ----------------------------------------------------------------------
class S3_AllThree(NarratedScene):
    scene_key = "S3_AllThree"

    def construct(self):
        self.header("All three single-voxel lesions")

        intro = Text("each single-voxel lesion picks a different column of C",
                     font_size=26, color=DIM).to_edge(UP, buff=1.1)
        self.play_beat(FadeIn(intro))

        # Build three column cards, each tagged with its angle.
        def col_card(label, col, ang, color):
            vec = Matrix([col[0:1], col[1:2], col[2:3]], v_buff=0.7).scale(0.62)
            vec.get_entries().set_color(color)
            tag = MathTex(r"\ell = e_" + label, color=VAR).scale(0.8)\
                .next_to(vec, UP, buff=0.25)
            a = MathTex(r"\theta \approx " + ang, color=RES).scale(0.8)\
                .next_to(vec, DOWN, buff=0.3)
            return VGroup(tag, vec, a)

        c1 = col_card("1", COL1, ANG1, RES)
        c2 = col_card("2", COL2, ANG2, VAR)
        c3 = col_card("3", COL3, ANG3, BAD)
        cards = VGroup(c1, c2, c3).arrange(RIGHT, buff=1.0).shift(DOWN * 0.3)

        # Reveal each card on its own beat.
        self.play_beat(FadeIn(c1, shift=UP * 0.2))
        self.play_beat(FadeIn(c2, shift=UP * 0.2))
        self.play_beat(FadeIn(c3, shift=UP * 0.2))

        # The punchline: all within ~8 degrees.
        band = SurroundingRectangle(cards, color=BACK, buff=0.3)
        within = Text("three different maps — all within about 8 degrees of the backbone",
                      font_size=25, color=BACK).to_edge(DOWN, buff=0.7)
        self.play_beat(Create(band), FadeIn(within, shift=UP * 0.15))


# ----------------------------------------------------------------------
# S4 — Three arrows funnelling toward u_1.
# ----------------------------------------------------------------------
class S4_Funnel(NarratedScene):
    scene_key = "S4_Funnel"

    def construct(self):
        self.header("A narrow cone around the backbone")

        # A 2D schematic: u_1 backbone direction, three map arrows near it.
        origin = LEFT * 3.2 + DOWN * 1.6
        # Backbone u_1 (long, BACK).
        u1_dir = np.array([0.80, 0.62, 0.0])
        u1_dir = u1_dir / np.linalg.norm(u1_dir)
        u1_arrow = Arrow(origin, origin + u1_dir * 5.2, color=BACK,
                         buff=0, stroke_width=7)
        u1_lab = MathTex(r"u_1", color=BACK).scale(1.1)\
            .next_to(u1_arrow.get_end(), UP, buff=0.2)

        # Three map arrows, each a few degrees off u_1 (illustrative angles).
        def rot(vec, deg):
            r = np.deg2rad(deg)
            c, s = np.cos(r), np.sin(r)
            return np.array([c * vec[0] - s * vec[1],
                             s * vec[0] + c * vec[1], 0.0])

        a1 = Arrow(origin, origin + rot(u1_dir, -2.9) * 4.6, color=RES,
                   buff=0, stroke_width=5)
        a2 = Arrow(origin, origin + rot(u1_dir, 5.5) * 4.3, color=VAR,
                   buff=0, stroke_width=5)
        a3 = Arrow(origin, origin + rot(u1_dir, -7.6) * 4.0, color=BAD,
                   buff=0, stroke_width=5)
        m1l = MathTex(r"m_{e_1}", color=RES).scale(0.7).next_to(a1.get_end(), RIGHT, buff=0.1)
        m2l = MathTex(r"m_{e_2}", color=VAR).scale(0.7).next_to(a2.get_end(), UP, buff=0.1)
        m3l = MathTex(r"m_{e_3}", color=BAD).scale(0.7).next_to(a3.get_end(), DOWN, buff=0.1)

        # Beat 1: the three arrows pointing their own way.
        self.play_beat(GrowArrow(a1), GrowArrow(a2), GrowArrow(a3),
                       FadeIn(m1l), FadeIn(m2l), FadeIn(m3l), lag_ratio=0.3)

        # Beat 2: the backbone appears; the cone hugs it.
        cone = Polygon(origin, origin + rot(u1_dir, -8.5) * 5.0,
                       origin + rot(u1_dir, 6.5) * 5.0,
                       color=BACK, fill_opacity=0.12, stroke_width=0)
        self.play_beat(GrowArrow(u1_arrow), FadeIn(u1_lab), FadeIn(cone))

        # Beat 3: the three angle labels collected.
        angs = VGroup(
            MathTex(ANG1, color=RES).scale(0.9),
            MathTex(ANG2, color=VAR).scale(0.9),
            MathTex(ANG3, color=BAD).scale(0.9),
        ).arrange(RIGHT, buff=0.6).to_edge(RIGHT, buff=1.0).shift(UP * 1.2)
        squeezed = Text("the whole fan: under 8 degrees of arc",
                        font_size=24, color=DIM).next_to(angs, DOWN, buff=0.4)
        self.play_beat(FadeIn(angs, shift=UP * 0.15), FadeIn(squeezed))

        # Beat 4: the cos^2 bound — why it tightens with the gap.
        bound = MathTex(r"\cos^2\!\angle(m, u_1)", "=",
                        r"\frac{\lambda_1^2 \bar c_1^2}{\sum_j \lambda_j^2 \bar c_j^2}")\
            .scale(0.9).to_edge(RIGHT, buff=0.7).shift(DOWN * 0.4)
        bound[0].set_color(RES); bound[2].set_color(EIG)
        toone = MathTex(r"\frac{\lambda_2}{\lambda_1} \to 0",
                        r"\ \Rightarrow\ ", r"\theta \to 0").scale(0.85)\
            .next_to(bound, DOWN, buff=0.4)
        toone[0].set_color(EIG); toone[2].set_color(RES)
        self.play_beat(Write(bound), Write(toone))

        # Beat 5: our gap is already small.
        ours = MathTex(r"\frac{\lambda_2}{\lambda_1} = 0.075", color=RES).scale(0.95)\
            .next_to(toone, DOWN, buff=0.45)
        ourscap = Text("already small: maps pulled onto u1\nbefore their own identity counts",
                       font_size=20, color=DIM, line_spacing=0.9)\
            .next_to(ours, DOWN, buff=0.3)
        self.play_beat(Write(ours), FadeIn(ourscap))


# ----------------------------------------------------------------------
# S5 — The moral: geometry, not biology. (Balanced framing.)
# ----------------------------------------------------------------------
class S5_Moral(NarratedScene):
    scene_key = "S5_Moral"

    def construct(self):
        self.header("Geometry, not biology")

        # The headline.
        head = VGroup(
            Text("Completely different lesions, nearly the same direction.",
                 font_size=29, color=WHITE),
            Text("Not shared biology — one wide spectral gap in C.",
                 font_size=28, color=RES),
        ).arrange(DOWN, buff=0.4).shift(UP * 1.6)
        self.play_beat(FadeIn(head[0], shift=UP * 0.15),
                       FadeIn(head[1], shift=UP * 0.15))

        # Eigenvalues own the direction; the lesion only loads.
        own = MathTex(r"m = \sum_j", r"\lambda_j", r"(u_j^{\top}\ell)", r"\,u_j")\
            .scale(1.1).next_to(head, DOWN, buff=0.7)
        own[1].set_color(EIG); own[2].set_color(VAR); own[3].set_color(BACK)
        br1 = Brace(own[1], DOWN, color=DIM)
        l1 = br1.get_text("owns the direction").set_color(EIG).scale(0.65)
        br2 = Brace(own[2], DOWN, color=DIM)
        l2 = br2.get_text("the lesion's loading").set_color(VAR).scale(0.65)
        self.play_beat(Write(own), GrowFromCenter(br1), FadeIn(l1),
                       GrowFromCenter(br2), FadeIn(l2), lag_ratio=0.2)

        # What this explains: average maps converge. (Scope.)
        self.play(FadeOut(VGroup(head, own, br1, l1, br2, l2)), run_time=0.5)
        scope = VGroup(
            Text("This explains exactly ONE thing:", font_size=28, color=WHITE),
            Text("why AVERAGE maps, across very different conditions, look alike.",
                 font_size=27, color=BACK),
            Text("That convergence is a property of C's spectrum.",
                 font_size=25, color=DIM),
        ).arrange(DOWN, buff=0.35).shift(UP * 0.5)
        self.play_beat(LaggedStart(*[FadeIn(s, shift=UP * 0.15) for s in scope],
                                   lag_ratio=0.35))

        # What it does NOT say: the contrast can still carry signal.
        self.play(scope.animate.scale(0.7).to_edge(UP, buff=1.1), run_time=0.4)
        notdebunk = VGroup(
            Text("It does NOT debunk the method.", font_size=28, color=RES),
            MathTex(r"\Delta = \bar m^{+} - \bar m^{-}", color=VAR).scale(1.0),
            Text("the backbone crowds every map — but it can CANCEL\nfrom a difference of maps",
                 font_size=24, color=DIM, line_spacing=0.9),
        ).arrange(DOWN, buff=0.35).shift(DOWN * 0.4)
        self.play_beat(FadeIn(notdebunk[0]), Write(notdebunk[1]),
                       FadeIn(notdebunk[2]))

        # Camera vs court — handoff to next chapters.
        self.play(FadeOut(VGroup(scope, notdebunk)), run_time=0.5)
        handoff = VGroup(
            Text("The camera always photographs the same hubs.",
                 font_size=29, color=WHITE),
            Text("Whether the court can still convict — on the contrast —",
                 font_size=27, color=VAR),
            Text("is the question the next chapters take up.",
                 font_size=27, color=DIM),
        ).arrange(DOWN, buff=0.4)
        self.play_beat(LaggedStart(*[FadeIn(h, shift=UP * 0.15) for h in handoff],
                                   lag_ratio=0.35))
