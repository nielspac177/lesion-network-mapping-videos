"""c0203_alignment_bound — Theorem R1: the alignment bound.

Mini-video #c0203 of the LNM series. A full, long-form proof that every seed
map m_ell = C ell is pulled toward the connectome backbone u_1, quantified by

    tan(theta_ell)  <=  (lambda_2 / lambda_1) * ( ||ell_perp|| / |u_1^T ell| ).

Built directly on the spectral identities of
  responses/lnm_critique/sections/02_what_is_entailed.md
    C = sum_j lambda_j u_j u_j^T,  lambda_1 >= lambda_2 >= ... >= 0,
    m = C ell = sum_j lambda_j (u_j^T ell) u_j,
and the worked numbers lambda_1 = 10, lambda_2 = 1 (sec. 02) and the 3-voxel
eigenvalues lambda = (4.0, 0.3, 0.1) with two single-voxel maps within ~7 deg
(sec. 01 / c0101). No invented constants.

Scenes: S1_Statement S2_Strategy S3_Proof S4_Symbols S5_Moral S6_Caveat.

Render:
  MEDIA=$HOME/lnm_media/c0203_alignment_bound ./render.sh \
      chapters/c0203_alignment_bound/scenes.py -q ql \
      S1_Statement S2_Strategy S3_Proof S4_Symbols S5_Moral S6_Caveat
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# S1 — Statement of Theorem R1: the alignment bound.
# ----------------------------------------------------------------------
class S1_Statement(NarratedScene):
    scene_key = "S1_Statement"

    def construct(self):
        # Title + the operator recall.
        title = Text("Theorem R1: the alignment bound", font_size=42, color=RES)
        op = MathTex("m_\\ell", "=", "C", "\\ell").scale(1.5)
        op[0].set_color(VAR); op[2].set_color(WHITE); op[3].set_color(VAR)
        op.next_to(title, DOWN, buff=0.6)
        recall = Text("which way does the seed's map point?",
                      font_size=24, color=DIM).next_to(op, DOWN, buff=0.4)
        self.play_beat(Write(title), FadeIn(op, shift=UP * 0.2), FadeIn(recall))

        # Define theta_ell: angle between m_ell and u_1.
        self.play(FadeOut(VGroup(op, recall)),
                  title.animate.scale(0.62).to_edge(UP, buff=0.35), run_time=0.5)
        defn = MathTex(r"\theta_\ell", "=", r"\angle\big(", "m_\\ell", ",\ ", "u_1", r"\big)").scale(1.2)
        defn[0].set_color(RES); defn[3].set_color(VAR); defn[5].set_color(BACK)
        defn.shift(UP * 1.6)
        dcap = Text("u_1 = leading eigenvector of C = the backbone",
                    font_size=24, color=BACK).next_to(defn, DOWN, buff=0.4)
        self.play_beat(Write(defn), FadeIn(dcap))

        # The bound itself.
        bound = MathTex(r"\tan", r"\theta_\ell", r"\ \le\ ",
                        r"\frac{\lambda_2}{\lambda_1}",
                        r"\cdot",
                        r"\frac{\lVert \ell_\perp \rVert}{\lvert u_1^{\top}\ell \rvert}").scale(1.25)
        bound[1].set_color(RES); bound[3].set_color(EIG)
        bound[5].set_color(VAR)
        bound.next_to(dcap, DOWN, buff=0.7)
        self.play_beat(Write(bound))

        # Annotate the spectral gap.
        br_gap = Brace(bound[3], DOWN, color=EIG)
        gap_lab = br_gap.get_text("spectral gap: a property of C alone").set_color(EIG)
        gap_lab.scale(0.62)
        self.play_beat(GrowFromCenter(br_gap), FadeIn(gap_lab))

        # Annotate the seed ratio + name ell_perp.
        self.play(FadeOut(VGroup(br_gap, gap_lab)), run_time=0.35)
        br_seed = Brace(bound[5], DOWN, color=VAR)
        seed_lab = br_seed.get_text("perp seed mass / backbone seed mass").set_color(VAR)
        seed_lab.scale(0.62)
        split = MathTex(r"\ell", "=", r"(u_1^{\top}\ell)\,u_1", "+", r"\ell_\perp").scale(0.85)
        split[0].set_color(VAR); split[2].set_color(BACK); split[4].set_color(VAR)
        split.next_to(seed_lab, DOWN, buff=0.4)
        self.play_beat(GrowFromCenter(br_seed), FadeIn(seed_lab), Write(split))

        # Read the shape of the bound.
        self.play(FadeOut(VGroup(br_seed, seed_lab, split)), run_time=0.35)
        shape = Text("small gap  x  whatever the seed brings  =  small angle\n"
                     "the map is pulled toward u_1 almost regardless of the lesion",
                     font_size=24, color=RES, line_spacing=0.9).next_to(bound, DOWN, buff=0.7)
        self.play_beat(FadeIn(shape, shift=UP * 0.15))


# ----------------------------------------------------------------------
# S2 — Pre-proof strategy: work backward from the angle.
# ----------------------------------------------------------------------
class S2_Strategy(NarratedScene):
    scene_key = "S2_Strategy"

    def construct(self):
        self.header("Strategy: work backward from the angle")

        # Find the triangle hiding in the map.
        idea = Text("an angle comes from a right triangle —\n"
                    "find the triangle hiding inside the map",
                    font_size=28, color=WHITE, line_spacing=0.9).shift(UP * 2.2)
        self.play_beat(FadeIn(idea, shift=UP * 0.15))

        # Eigenbasis expansion.
        expand = MathTex("m_\\ell", "=", r"\sum_j", r"\lambda_j", r"\,(u_j^{\top}\ell)\,", "u_j").scale(1.1)
        expand[0].set_color(VAR); expand[3].set_color(EIG); expand[5].set_color(BACK)
        expand.next_to(idea, DOWN, buff=0.6)
        ecap = Text("each u_j is a clean coordinate axis", font_size=22, color=DIM)\
            .next_to(expand, DOWN, buff=0.3)
        self.play_beat(Write(expand), FadeIn(ecap))

        # Split: backbone vs off-backbone.
        self.play(FadeOut(VGroup(idea, expand, ecap)), run_time=0.4)
        twop = MathTex("m_\\ell", "=",
                       r"\underbrace{\lambda_1 (u_1^{\top}\ell)\,u_1}_{\text{along } u_1}",
                       "+",
                       r"\underbrace{\sum_{j\ge 2}\lambda_j (u_j^{\top}\ell)\,u_j}_{\perp\, u_1}").scale(0.95)
        twop[0].set_color(VAR); twop[2].set_color(BACK); twop[4].set_color(DIM)
        twop.shift(UP * 1.6)
        self.play_beat(Write(twop))

        # Draw the literal triangle.
        O = LEFT * 3.0 + DOWN * 1.4
        adj = 3.4
        opp = 1.5
        A = O
        B = O + RIGHT * adj
        Cpt = B + UP * opp
        tri = Polygon(A, B, Cpt, color=WHITE, stroke_width=3)
        adj_line = Line(A, B, color=BACK, stroke_width=6)
        opp_line = Line(B, Cpt, color=DIM, stroke_width=6)
        hyp_line = Line(A, Cpt, color=VAR, stroke_width=6)
        adj_l = Text("adjacent: along u_1", font_size=20, color=BACK).next_to(adj_line, DOWN, buff=0.2)
        opp_l = Text("opposite:\noff-backbone", font_size=20, color=DIM, line_spacing=0.85)\
            .next_to(opp_line, RIGHT, buff=0.2)
        hyp_l = MathTex("m_\\ell", color=VAR).scale(0.8).next_to(hyp_line.get_center(), UP * 0.4 + LEFT * 0.4)
        th = MathTex(r"\theta_\ell", color=RES).scale(0.8).next_to(A, RIGHT, buff=0.45).shift(UP * 0.18)
        self.play_beat(Create(tri), Create(adj_line), Create(opp_line), Create(hyp_line),
                       FadeIn(adj_l), FadeIn(opp_l), FadeIn(hyp_l), FadeIn(th), lag_ratio=0.15)

        # Tangent = opposite / adjacent.
        tan_eq = MathTex(r"\tan", r"\theta_\ell", "=",
                         r"\frac{\text{opposite}}{\text{adjacent}}", "=",
                         r"\frac{\lVert \text{off-backbone}\rVert}{\lVert \text{along } u_1\rVert}").scale(0.85)
        tan_eq[1].set_color(RES)
        tan_eq.to_edge(RIGHT, buff=0.4).shift(DOWN * 0.3)
        self.play_beat(Write(tan_eq))

        # The plan.
        self.play(FadeOut(VGroup(tri, adj_line, opp_line, hyp_line, adj_l, opp_l,
                                 hyp_l, th, twop, tan_eq)), run_time=0.4)
        plan = VGroup(
            Text("1.  adjacent length — compute it exactly", font_size=26, color=BACK),
            Text("2.  opposite length — bound it above by lambda_2", font_size=26, color=DIM),
            Text("3.  divide — the gap lambda_2/lambda_1 falls out", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        self.play_beat(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.2) for p in plan],
                                   lag_ratio=0.35))


# ----------------------------------------------------------------------
# S3 — The proof, step by step (9 beats).
# ----------------------------------------------------------------------
class S3_Proof(NarratedScene):
    scene_key = "S3_Proof"

    def construct(self):
        self.header("Proof")

        # Step 1: spectral decomposition.
        s1 = Text("Step 1.  spectrum of C", font_size=24, color=DIM).to_edge(UP, buff=0.9).to_edge(LEFT, buff=0.6)
        spec = MathTex("C", "=", r"\sum_j", r"\lambda_j", r"\,u_j u_j^{\top}", ",\quad",
                       r"\lambda_1 \ge \lambda_2 \ge \cdots \ge 0").scale(1.0)
        spec[0].set_color(WHITE); spec[3].set_color(EIG); spec[4].set_color(BACK); spec[6].set_color(EIG)
        spec.next_to(s1, DOWN, buff=0.5).to_edge(LEFT, buff=0.6)
        self.play_beat(FadeIn(s1), Write(spec))

        # Step 2: apply to seed.
        self.play(spec.animate.scale(0.8).to_edge(UP, buff=1.4), FadeOut(s1), run_time=0.45)
        s2 = MathTex("m_\\ell", "=", "C\\ell", "=", r"\sum_j", r"\lambda_j", r"\,c_j\,", "u_j",
                     r",\quad c_j := u_j^{\top}\ell").scale(0.95)
        s2[0].set_color(VAR); s2[5].set_color(EIG); s2[7].set_color(BACK); s2[8].set_color(VAR)
        s2.next_to(spec, DOWN, buff=0.6)
        s2cap = Text("orthonormal u_j: every cross term dies", font_size=22, color=DIM)\
            .next_to(s2, DOWN, buff=0.3)
        self.play_beat(Write(s2), FadeIn(s2cap))

        # Step 3: leading term = adjacent.
        self.play(FadeOut(VGroup(spec, s2cap)),
                  s2.animate.scale(0.85).to_edge(UP, buff=1.2), run_time=0.45)
        adj = MathTex(r"\text{adjacent}", "=", r"\lambda_1 c_1\, u_1",
                      r"\ \Rightarrow\ ", r"\text{length}", "=", r"\lambda_1 c_1").scale(0.95)
        adj[2].set_color(BACK); adj[6].set_color(BACK)
        adj.shift(UP * 0.6)
        adjcap = Text("the backbone part: its signed length along u_1 is exactly lambda_1 c_1",
                      font_size=22, color=BACK).next_to(adj, DOWN, buff=0.35)
        self.play_beat(Write(adj), FadeIn(adjcap))

        # Step 4: the rest = opposite.
        self.play(FadeOut(VGroup(adj, adjcap)), run_time=0.35)
        opp = MathTex(r"\text{opposite}", "=", r"\sum_{j\ge 2}", r"\lambda_j", r"\,c_j\,", "u_j").scale(1.0)
        opp[3].set_color(EIG); opp[5].set_color(DIM)
        opp.shift(UP * 0.6)
        oppcap = Text("everything off the backbone — lives entirely in the space orthogonal to u_1",
                      font_size=22, color=DIM).next_to(opp, DOWN, buff=0.35)
        self.play_beat(Write(opp), FadeIn(oppcap))

        # Step 5: squared length by orthonormality.
        self.play(FadeOut(VGroup(opp, oppcap)), run_time=0.35)
        sq = MathTex(r"\lVert \text{opposite}\rVert^2", "=",
                     r"\sum_{j\ge 2}", r"\lambda_j^2", r"\,c_j^2").scale(1.05)
        sq[3].set_color(EIG)
        sq.shift(UP * 0.6)
        sqcap = Text("Pythagoras in the eigenbasis: no cross terms, just a sum of squares",
                     font_size=22, color=DIM).next_to(sq, DOWN, buff=0.35)
        self.play_beat(Write(sq), FadeIn(sqcap))

        # Step 6: the single inequality, lambda_j <= lambda_2.
        self.play(FadeOut(sqcap), sq.animate.to_edge(UP, buff=1.5), run_time=0.4)
        ineq = MathTex(r"\lambda_j \le \lambda_2\ (j\ge 2)",
                       r"\ \Rightarrow\ ",
                       r"\sum_{j\ge 2}\lambda_j^2 c_j^2",
                       r"\ \le\ ",
                       r"\lambda_2^2 \sum_{j\ge 2} c_j^2").scale(0.95)
        ineq[0].set_color(EIG); ineq[4].set_color(EIG)
        ineq.shift(UP * 0.2)
        self.play_beat(Write(ineq))

        # Step 7: the remaining sum = ||ell_perp||^2.
        perp = MathTex(r"\sum_{j\ge 2} c_j^2", "=",
                       r"\lVert \ell_\perp \rVert^2",
                       r"\ \Rightarrow\ ",
                       r"\lVert \text{opposite}\rVert \le \lambda_2 \lVert \ell_\perp \rVert").scale(0.92)
        perp[2].set_color(VAR); perp[4].set_color(EIG)
        perp.next_to(ineq, DOWN, buff=0.6)
        self.play_beat(Write(perp))

        # Step 8: take the ratio.
        self.play(FadeOut(VGroup(sq, ineq, perp)), run_time=0.4)
        ratio = MathTex(r"\tan\theta_\ell", "=",
                        r"\frac{\lVert \text{opposite}\rVert}{\lvert \lambda_1 c_1\rvert}",
                        r"\ \le\ ",
                        r"\frac{\lambda_2 \lVert \ell_\perp\rVert}{\lambda_1 \lvert c_1\rvert}").scale(1.0)
        ratio[0].set_color(RES); ratio[4].set_color(EIG)
        ratio.shift(UP * 0.5)
        self.play_beat(Write(ratio))

        # Step 9: substitute c_1 = u_1^T ell -> QED.
        qed = MathTex(r"\tan\theta_\ell", r"\ \le\ ",
                      r"\frac{\lambda_2}{\lambda_1}",
                      r"\cdot",
                      r"\frac{\lVert \ell_\perp \rVert}{\lvert u_1^{\top}\ell \rvert}").scale(1.15)
        qed[0].set_color(RES); qed[2].set_color(EIG); qed[4].set_color(VAR)
        qed.next_to(ratio, DOWN, buff=0.7)
        box = SurroundingRectangle(qed, color=RES, buff=0.2)
        qmark = Text("Q.E.D.", font_size=26, color=RES).next_to(box, RIGHT, buff=0.4)
        self.play_beat(Write(qed), Create(box), FadeIn(qmark))


# ----------------------------------------------------------------------
# S4 — Every symbol explained (6 beats).
# ----------------------------------------------------------------------
class S4_Symbols(NarratedScene):
    scene_key = "S4_Symbols"

    def construct(self):
        self.header("Every symbol decoded")

        bound = MathTex(r"\tan", r"\theta_\ell", r"\ \le\ ",
                        r"\frac{\lambda_2}{\lambda_1}",
                        r"\cdot",
                        r"\frac{\lVert \ell_\perp \rVert}{\lvert u_1^{\top}\ell \rvert}").scale(1.3)
        bound[1].set_color(RES); bound[3].set_color(EIG); bound[5].set_color(VAR)
        bound.to_edge(UP, buff=1.4)
        self.play_beat(FadeIn(bound))

        # lambda_1, lambda_2 + the gap.
        g1 = MathTex(r"\lambda_1 \ge \lambda_2", color=EIG).scale(0.9)
        t1 = Text("top two eigenvalues of C — strengths of its two leading patterns",
                  font_size=23, color=DIM)
        row1 = VGroup(g1, t1).arrange(RIGHT, buff=0.5).shift(UP * 0.7)
        self.play_beat(FadeIn(g1, shift=RIGHT * 0.2), FadeIn(t1))

        # u_1 = backbone.
        g2 = MathTex("u_1", color=BACK).scale(1.0)
        t2 = Text("leading eigenvector = the BACKBONE, the dominant hub pattern",
                  font_size=23, color=BACK)
        row2 = VGroup(g2, t2).arrange(RIGHT, buff=0.5).next_to(row1, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play_beat(FadeIn(g2, shift=RIGHT * 0.2), FadeIn(t2))

        # u_1^T ell = backbone loading.
        g3 = MathTex(r"u_1^{\top}\ell", color=VAR).scale(0.9)
        t3 = Text("backbone loading: how much of the seed already points along u_1",
                  font_size=23, color=DIM)
        row3 = VGroup(g3, t3).arrange(RIGHT, buff=0.5).next_to(row2, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play_beat(FadeIn(g3, shift=RIGHT * 0.2), FadeIn(t3))

        # ell_perp = off-backbone seed.
        g4 = MathTex(r"\ell_\perp", color=VAR).scale(1.0)
        t4 = Text("off-backbone seed: ell minus its u_1 component; its norm = perp mass",
                  font_size=23, color=DIM)
        row4 = VGroup(g4, t4).arrange(RIGHT, buff=0.5).next_to(row3, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play_beat(FadeIn(g4, shift=RIGHT * 0.2), FadeIn(t4))

        # theta_ell = angle controlled.
        g5 = MathTex(r"\theta_\ell", color=RES).scale(1.0)
        t5 = Text("angle of the map to u_1 — small tan hugs the backbone; large tan escapes it",
                  font_size=23, color=RES)
        row5 = VGroup(g5, t5).arrange(RIGHT, buff=0.5).next_to(row4, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play_beat(FadeIn(g5, shift=RIGHT * 0.2), FadeIn(t5))


# ----------------------------------------------------------------------
# S5 — The moral: the spectral gap is a funnel (6 beats).
# ----------------------------------------------------------------------
class S5_Moral(NarratedScene):
    scene_key = "S5_Moral"

    def construct(self):
        self.header("The moral: the spectral gap is a funnel")

        head = Text("The spectral gap is a funnel.", font_size=36, color=RES).shift(UP * 2.5)
        self.play_beat(FadeIn(head, shift=UP * 0.15))

        # the right side: seed geometry x gap.
        rhs = MathTex(r"\tan\theta_\ell", r"\ \le\ ",
                      r"\frac{\lambda_2}{\lambda_1}", r"\cdot",
                      r"\underbrace{\frac{\lVert \ell_\perp\rVert}{\lvert u_1^{\top}\ell\rvert}}_{\text{seed: anything}}").scale(1.0)
        rhs[0].set_color(RES); rhs[2].set_color(EIG); rhs[4].set_color(VAR)
        rhs.next_to(head, DOWN, buff=0.7)
        self.play_beat(Write(rhs))

        # small gap squeezes the angle.
        squeeze = MathTex(r"\frac{\lambda_2}{\lambda_1}\to 0",
                          r"\ \Rightarrow\ ",
                          r"\theta_\ell \to 0").scale(1.1)
        squeeze[0].set_color(EIG); squeeze[2].set_color(RES)
        squeeze.next_to(rhs, DOWN, buff=0.6)
        scap = Text("lambda_1 towers over lambda_2 -> every seed's angle squeezed toward zero",
                    font_size=22, color=DIM).next_to(squeeze, DOWN, buff=0.3)
        self.play_beat(Write(squeeze), FadeIn(scap))

        # the source numbers.
        self.play(FadeOut(VGroup(rhs, squeeze, scap)), run_time=0.4)
        nums = VGroup(
            MathTex(r"\lambda_1 = 10,\ \ \lambda_2 = 1\quad(\text{gap }= \tfrac{1}{10})", color=EIG).scale(0.95),
            MathTex(r"\text{3-voxel } C:\ \ \lambda = (4.0,\ 0.3,\ 0.1)", color=EIG).scale(0.95),
            Text("two very different single-voxel lesions land within ~7 degrees of u_1",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.45).next_to(head, DOWN, buff=0.8)
        self.play_beat(LaggedStart(*[FadeIn(n, shift=UP * 0.12) for n in nums], lag_ratio=0.35))

        # not a flaw, a property of the spectrum.
        self.play(FadeOut(nums), run_time=0.35)
        prop = Text("convergence toward u_1 is not a coincidence, not a flaw —\n"
                    "it is a property of the connectome's spectrum: geometry funnelling\n"
                    "many seeds into one direction",
                    font_size=26, color=WHITE, line_spacing=0.95).next_to(head, DOWN, buff=0.8)
        self.play_beat(FadeIn(prop, shift=UP * 0.15))

        # why disparate averages look alike.
        self.play(FadeOut(prop), run_time=0.35)
        why = Text("addiction average, depression average, a bag of random seeds —\n"
                   "they fall through the same funnel and land on the same backbone u_1",
                   font_size=26, color=RES, line_spacing=0.95).next_to(head, DOWN, buff=0.8)
        self.play_beat(FadeIn(why, shift=UP * 0.15))


# ----------------------------------------------------------------------
# S6 — Caveat: bounds the description, not the contrast (6 beats).
# ----------------------------------------------------------------------
class S6_Caveat(NarratedScene):
    scene_key = "S6_Caveat"

    def construct(self):
        self.header("Caveat: this bounds the description, not the contrast")

        head = Text("Be precise: what this theorem does, and does not, say.",
                    font_size=30, color=WHITE).shift(UP * 2.5)
        self.play_beat(FadeIn(head, shift=UP * 0.15))

        # what it bounds: the average (camera).
        camera = MathTex(r"\bar m", "=", r"\frac{1}{n}\sum_i C\ell_i",
                         r"\ \longrightarrow\ ", "u_1").scale(1.0)
        camera[0].set_color(VAR); camera[4].set_color(BACK)
        camera.next_to(head, DOWN, buff=0.7)
        ccap = Text("a DESCRIPTION: each seed's map, and so the group average — the funnel governs this",
                    font_size=22, color=DIM).next_to(camera, DOWN, buff=0.3)
        self.play_beat(Write(camera), FadeIn(ccap))

        # the contrast: backbone cancels.
        self.play(FadeOut(VGroup(camera, ccap)), run_time=0.35)
        contrast = MathTex(r"\Delta", "=", r"\bar m^{+}", "-", r"\bar m^{-}", "=",
                           r"\sum_j \lambda_j(\bar c_j^{+}-\bar c_j^{-})\,u_j").scale(0.9)
        contrast[0].set_color(RES); contrast[2].set_color(VAR); contrast[4].set_color(VAR)
        contrast.next_to(head, DOWN, buff=0.7)
        cancel = MathTex(r"\bar c_1^{+}\approx \bar c_1^{-}",
                         r"\ \Rightarrow\ ",
                         r"\lambda_1(\bar c_1^{+}-\bar c_1^{-})\,u_1 \approx 0").scale(0.85)
        cancel[2].set_color(BAD)
        cancel.next_to(contrast, DOWN, buff=0.45)
        cccap = Text("the shared backbone term subtracts away — the leading u_1 piece cancels",
                     font_size=22, color=DIM).next_to(cancel, DOWN, buff=0.3)
        self.play_beat(Write(contrast), Write(cancel), FadeIn(cccap))

        # no upper bound on Delta.
        self.play(FadeOut(VGroup(contrast, cancel, cccap)), run_time=0.35)
        nobound = VGroup(
            Text("the theorem places NO upper bound on the contrast Delta",
                 font_size=28, color=RES),
            Text("it controls how far each AVERAGE leans on u_1;\n"
                 "it is silent on the DIFFERENCE — where the symptom signal lives",
                 font_size=24, color=WHITE, line_spacing=0.95),
        ).arrange(DOWN, buff=0.45).next_to(head, DOWN, buff=0.8)
        self.play_beat(FadeIn(nobound[0], shift=UP * 0.15), FadeIn(nobound[1]))

        # geometry, not a verdict.
        self.play(FadeOut(nobound), run_time=0.35)
        verdict = Text("Read this as geometry, not a verdict.\n"
                       "A small gap explains why average maps look alike.\n"
                       "It does NOT show a symptom contrast carries no signal —\n"
                       "the method is not debunked here, only described.",
                       font_size=25, color=RES, line_spacing=1.0).next_to(head, DOWN, buff=0.8)
        self.play_beat(FadeIn(verdict, shift=UP * 0.15))

        # where the next chapters go.
        self.play(FadeOut(verdict), run_time=0.35)
        nxt = Text("The gap between a true claim about the average\n"
                   "and a claim about the contrast is where the next chapters work.\n"
                   "The funnel is real. What survives it is the open question.",
                   font_size=25, color=DIM, line_spacing=1.0).next_to(head, DOWN, buff=0.8)
        self.play_beat(FadeIn(nxt, shift=UP * 0.15))
