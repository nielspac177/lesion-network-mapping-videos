"""Camera vs Court — description versus inference on the same lesion maps.

Five narrated scenes (S1..S5). Each visual beat is tied to one narration line
in narration.py so subtitles and the synthesized voiceover stay in sync.

Source: responses/lnm_critique/sections/02_what_is_entailed.md and
        responses/lnm_critique/sections/03_the_right_null.md

Render:
  MEDIA=$HOME/lnm_media/c0104_camera_vs_court ./render.sh \
      chapters/c0104_camera_vs_court/scenes.py -q ql \
      S1_TwoQuestions S2_Camera S3_Court S4_WhyItCancels S5_Moral
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# S1 — two questions of the same maps
# ----------------------------------------------------------------------
class S1_TwoQuestions(NarratedScene):
    scene_key = "S1_TwoQuestions"

    def construct(self):
        title = Text("Camera vs Court", font_size=46, color=WHITE)
        sub = Text("two questions of the same maps", font_size=24, color=DIM)\
            .next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.3),
                  FadeOut(sub), run_time=0.6)

        # the stack: m = C ell
        eq = MathTex("m", "=", "C", r"\ell").scale(1.3).shift(UP * 1.7)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        bm = Brace(eq[0], DOWN, buff=0.15)
        bm_t = bm.get_text("each patient's map").scale(0.7)
        bm_t.set_color(DIM)
        bC = Brace(eq[2], UP, buff=0.12)
        bC_t = bC.get_text("fixed connectome").scale(0.65); bC_t.set_color(DIM)
        bl = Brace(eq[3], DOWN, buff=0.15)
        bl_t = bl.get_text("lesion (0/1)").scale(0.65); bl_t.set_color(DIM)
        self.play_beat(Write(eq),
                       GrowFromCenter(bC), FadeIn(bC_t),
                       GrowFromCenter(bm), FadeIn(bm_t),
                       GrowFromCenter(bl), FadeIn(bl_t), lag_ratio=0.15)

        self.play(FadeOut(VGroup(bm, bm_t, bC, bC_t, bl, bl_t)),
                  eq.animate.scale(0.7).next_to(title, DOWN, buff=0.2), run_time=0.5)

        # split screen: camera vs court
        divider = DashedLine(UP * 2.0, DOWN * 3.0, color=DIM)

        # Q1 — the camera (left)
        cam_q = Text("Q1  (description)", font_size=24, color=DIM)\
            .move_to(LEFT * 3.6 + UP * 1.4)
        cam_eq = MathTex(r"\bar m", "=", r"\tfrac{1}{n}\sum_i m_i").scale(1.0)
        cam_eq[0].set_color(VAR)
        cam_eq.next_to(cam_q, DOWN, buff=0.45)
        cam_ask = Text("what does the typical map\nlook like?", font_size=21,
                       color=DIM, line_spacing=0.8).next_to(cam_eq, DOWN, buff=0.4)
        self.play_beat(FadeIn(cam_q), Write(cam_eq), FadeIn(cam_ask))

        # Q2 — the court (right)
        court_q = Text("Q2  (inference)", font_size=24, color=RES)\
            .move_to(RIGHT * 3.6 + UP * 1.4)
        court_eq = MathTex(r"\Delta", "=", r"\bar m^{+}", "-", r"\bar m^{-}").scale(1.0)
        court_eq[0].set_color(RES); court_eq[2].set_color(VAR); court_eq[4].set_color(VAR)
        court_eq.next_to(court_q, DOWN, buff=0.45)
        court_ask = Text("is impaired vs spared\nmore than chance?", font_size=21,
                         color=DIM, line_spacing=0.8).next_to(court_eq, DOWN, buff=0.4)
        self.play_beat(Create(divider), FadeIn(court_q),
                       Write(court_eq), FadeIn(court_ask))

        # name the machines
        cam_lab = Text("CAMERA", font_size=26, color=DIM)\
            .move_to(LEFT * 3.6 + DOWN * 2.4)
        court_lab = Text("COURT", font_size=26, color=RES)\
            .move_to(RIGHT * 3.6 + DOWN * 2.4)
        self.play_beat(FadeIn(cam_lab, shift=UP * 0.2),
                       FadeIn(court_lab, shift=UP * 0.2),
                       Indicate(cam_eq, color=VAR, scale_factor=1.1),
                       Indicate(court_eq, color=RES, scale_factor=1.1))

        # the thesis
        thesis = Text("The critique is right about the camera —\n"
                      "and says nothing about the court.",
                      font_size=27, color=WHITE, line_spacing=0.85)\
            .move_to(DOWN * 0.4)
        self.play_beat(
            FadeOut(VGroup(cam_q, cam_eq, cam_ask, court_q, court_eq, court_ask,
                           cam_lab, court_lab, divider, eq, title)),
            FadeIn(thesis, shift=UP * 0.2))


# ----------------------------------------------------------------------
# S2 — the camera: the average map is backbone-dominated
# ----------------------------------------------------------------------
class S2_Camera(NarratedScene):
    scene_key = "S2_Camera"

    def construct(self):
        self.header("The camera: the average map is backbone-dominated")

        intro = Text("Give the critique its strongest form.",
                     font_size=30, color=DIM).shift(UP * 0.3)
        self.play_beat(FadeIn(intro))
        self.play(FadeOut(intro), run_time=0.4)

        # spectral decomposition of C
        spec = MathTex("C", "=", r"\sum_j", r"\lambda_j", "u_j", "u_j^{\\top}").scale(1.15)
        spec[3].set_color(EIG); spec[4].set_color(BACK); spec[5].set_color(BACK)
        spec.shift(UP * 2.0)
        ordering = MathTex(r"\lambda_1", r"\gg", r"\lambda_2", r"\ge", r"\cdots")\
            .scale(0.9).set_color(EIG).next_to(spec, DOWN, buff=0.35)
        bb_lab = Text("u₁ = the backbone", font_size=24, color=BACK)\
            .next_to(ordering, DOWN, buff=0.3)
        self.play_beat(Write(spec), FadeIn(ordering), FadeIn(bb_lab))

        # each map as a weighted sum of components
        mapeq = MathTex("m_i", "=", r"\sum_j", r"\lambda_j",
                        r"(u_j^{\top}\ell_i)", "u_j").scale(1.1)
        mapeq[0].set_color(VAR); mapeq[3].set_color(EIG)
        mapeq[4].set_color(VAR); mapeq[5].set_color(BACK)
        mapeq.next_to(bb_lab, DOWN, buff=0.5)
        ovlap = Brace(mapeq[4], DOWN, buff=0.12)
        ovlap_t = ovlap.get_text("lesion's overlap with pattern j").scale(0.6)
        ovlap_t.set_color(DIM)
        self.play_beat(Write(mapeq), GrowFromCenter(ovlap), FadeIn(ovlap_t))

        # the average
        self.play(FadeOut(VGroup(spec, ordering, bb_lab, mapeq, ovlap, ovlap_t)),
                  run_time=0.5)
        avg = MathTex(r"\bar m", "=", r"\sum_j", r"\lambda_j", r"\bar c_j", "u_j")\
            .scale(1.2).shift(UP * 1.9)
        avg[0].set_color(VAR); avg[3].set_color(EIG)
        avg[4].set_color(RES); avg[5].set_color(BACK)
        cbar = Brace(avg[4], DOWN, buff=0.12)
        cbar_t = cbar.get_text("group's average loading on component j").scale(0.6)
        cbar_t.set_color(DIM)
        self.play_beat(Write(avg), GrowFromCenter(cbar), FadeIn(cbar_t))

        # leading term dominates
        lead = MathTex(r"\bar m", r"\approx", r"\lambda_1", r"\bar c_1", "u_1")\
            .scale(1.2).next_to(cbar_t, DOWN, buff=0.7)
        lead[0].set_color(VAR); lead[2].set_color(EIG)
        lead[3].set_color(RES); lead[4].set_color(BACK)
        box = SurroundingRectangle(lead, color=BACK, buff=0.2)
        align = Text("aligns with the backbone, whatever the lesions marked",
                     font_size=23, color=DIM).next_to(box, DOWN, buff=0.3)
        self.play_beat(Write(lead), Create(box), FadeIn(align))

        # the convergence trap (concede it)
        trap = Text("addiction ≈ depression ≈ random seeds  —  all land on u₁",
                    font_size=26, color=BAD).next_to(align, DOWN, buff=0.5)
        self.play_beat(FadeIn(trap, shift=UP * 0.2),
                       Indicate(lead, color=BACK, scale_factor=1.1))

        # but: disease only enters through c-bar; geometry owned by lambda
        self.play(FadeOut(VGroup(avg, cbar, cbar_t, lead, box, align, trap)),
                  run_time=0.5)
        owned = VGroup(
            MathTex(r"\text{disease enters only via } \bar c_j", color=RES),
            MathTex(r"\text{the direction is owned by } \lambda_j "
                    r"\ \text{— a property of } C \text{ alone}", color=EIG),
        ).arrange(DOWN, buff=0.5).scale(0.95).shift(UP * 0.2)
        self.play_beat(FadeIn(owned[0]), FadeIn(owned[1]))


# ----------------------------------------------------------------------
# S3 — the court: the contrast under the symptom-label null
# ----------------------------------------------------------------------
class S3_Court(NarratedScene):
    scene_key = "S3_Court"

    def construct(self):
        self.header("The court: the contrast under a symptom-label null")

        plain = Text("The signal was never in the average.\n"
                     "It is in the difference: symptom vs no symptom.",
                     font_size=28, color=WHITE, line_spacing=0.85).shift(UP * 0.3)
        self.play_beat(FadeIn(plain))
        self.play(FadeOut(plain), run_time=0.4)

        # the two group averages
        plus = MathTex(r"\bar m^{+}", "=", r"\sum_j", r"\lambda_j",
                       r"\bar c_j^{+}", "u_j").scale(1.0).shift(UP * 1.9 + LEFT * 0.0)
        plus[0].set_color(VAR); plus[3].set_color(EIG)
        plus[4].set_color(RES); plus[5].set_color(BACK)
        minus = MathTex(r"\bar m^{-}", "=", r"\sum_j", r"\lambda_j",
                        r"\bar c_j^{-}", "u_j").scale(1.0)
        minus[0].set_color(VAR); minus[3].set_color(EIG)
        minus[4].set_color(RES); minus[5].set_color(BACK)
        minus.next_to(plus, DOWN, buff=0.45)
        grp_cap = Text("+ : impaired group      − : spared group   "
                       "(each still dragged to u₁)",
                       font_size=22, color=DIM).next_to(minus, DOWN, buff=0.4)
        self.play_beat(Write(plus), Write(minus), FadeIn(grp_cap))

        # the contrast
        self.play(FadeOut(VGroup(plus, minus, grp_cap)), run_time=0.5)
        delta = MathTex(r"\Delta", "=", r"\bar m^{+}", "-", r"\bar m^{-}",
                        "=", r"\sum_j", r"\lambda_j",
                        r"(\bar c_j^{+}-\bar c_j^{-})", "u_j").scale(0.95).shift(UP * 2.0)
        delta[0].set_color(RES); delta[2].set_color(VAR); delta[4].set_color(VAR)
        delta[7].set_color(EIG); delta[8].set_color(RES); delta[9].set_color(BACK)
        self.play_beat(Write(delta))

        # the leading backbone term, scaled by the loading DIFFERENCE
        lead = MathTex(r"\lambda_1", r"(\bar c_1^{+}-\bar c_1^{-})", "u_1")\
            .scale(1.15).next_to(delta, DOWN, buff=0.6)
        lead[0].set_color(EIG); lead[1].set_color(RES); lead[2].set_color(BACK)
        diffbrace = Brace(lead[1], DOWN, buff=0.12)
        diff_t = diffbrace.get_text("difference in backbone loadings").scale(0.6)
        diff_t.set_color(DIM)
        self.play_beat(Write(lead), GrowFromCenter(diffbrace), FadeIn(diff_t))

        # the null: shuffle labels, hold everything else fixed
        null_t = VGroup(
            Text("Null: shuffle only the symptom labels.",
                 font_size=25, color=VAR),
            Text("Every lesion, the whole connectome — held fixed.",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(diff_t, DOWN, buff=0.45)
        self.play_beat(FadeIn(null_t[0]), FadeIn(null_t[1]))

        # cancellation in expectation
        cancel = MathTex(r"\bar c_1^{+}", r"\approx", r"\bar c_1^{-}",
                         r"\ \Rightarrow\ ", r"\lambda_1(\bar c_1^{+}-\bar c_1^{-})",
                         r"\approx", "0").scale(0.95).next_to(null_t, DOWN, buff=0.4)
        cancel[4].set_color(BAD); cancel[6].set_color(BAD)
        strike = Line(lead[0].get_left(), lead.get_right(),
                      color=BAD, stroke_width=6)
        survive = Text("what survives: u₂, u₃, …  weighted by real group differences",
                       font_size=21, color=BACK).next_to(cancel, DOWN, buff=0.3)
        self.play_beat(Write(cancel), Create(strike), FadeIn(survive))

        # the data cooperates
        self.play(FadeOut(VGroup(delta, lead, diffbrace, diff_t, null_t,
                                 cancel, strike, survive)), run_time=0.5)
        data = VGroup(
            self._datum("same-symptom maps", "r = 0.44", BACK),
            self._datum("different-symptom", "r = 0.09", DIM),
            self._datum("degree (hub) map", "r = 0.16", BAD),
        ).arrange(DOWN, buff=0.5).shift(UP * 0.1)
        cap = Text("the contrast carries what the average buried",
                   font_size=24, color=RES).next_to(data, DOWN, buff=0.5)
        self.play_beat(FadeIn(data, lag_ratio=0.2), FadeIn(cap))

    def _datum(self, label, value, color):
        lab = Text(label, font_size=24, color=DIM)
        val = MathTex(value, color=color).scale(1.1).next_to(lab, RIGHT, buff=0.6)
        return VGroup(lab, val)


# ----------------------------------------------------------------------
# S4 — why the backbone cancels: x_i = b_i + r_i
# ----------------------------------------------------------------------
class S4_WhyItCancels(NarratedScene):
    scene_key = "S4_WhyItCancels"

    def construct(self):
        self.header("Why the backbone cancels  (full algebra: a later part)")

        intro = Text("The mechanism fits on one line.",
                     font_size=30, color=DIM).shift(UP * 0.3)
        self.play_beat(FadeIn(intro))
        self.play(FadeOut(intro), run_time=0.4)

        # decomposition x_i = b_i + r_i
        decomp = MathTex("x_i", "=",
                         r"\underbrace{\lambda_1(u_1^{\top}\ell_i)\,u_1}_{b_i}",
                         "+", "r_i").scale(1.1).shift(UP * 1.9)
        decomp[0].set_color(VAR); decomp[2].set_color(BACK); decomp[4].set_color(RES)
        bcap = Text("bᵢ : backbone piece", font_size=22, color=BACK)\
            .next_to(decomp, DOWN, buff=0.4).shift(LEFT * 2.3)
        rcap = Text("rᵢ : residual", font_size=22, color=RES)\
            .next_to(decomp, DOWN, buff=0.4).shift(RIGHT * 2.6)
        self.play_beat(Write(decomp), FadeIn(bcap), FadeIn(rcap))

        # the load-bearing fact
        fact = MathTex(r"b_i", r"\ \text{depends on the lesion,}\ ",
                       r"\ \text{never on the label } y_i").scale(0.95)
        fact[0].set_color(BACK)
        fact.next_to(rcap, DOWN, buff=0.6).shift(LEFT * 0.15)
        factbox = SurroundingRectangle(fact, color=BACK, buff=0.2)
        self.play_beat(Write(fact), Create(factbox))

        # therefore identical on both sides of the contrast
        same = Text("→ same distribution among impaired and spared,\n"
                    "    in the real labeling and in every shuffle",
                    font_size=24, color=DIM, line_spacing=0.85)\
            .next_to(factbox, DOWN, buff=0.5)
        self.play_beat(FadeIn(same))

        # four-patient table
        self.play(FadeOut(VGroup(decomp, bcap, rcap, fact, factbox, same)),
                  run_time=0.5)
        table = self._four_patient_table().shift(UP * 1.1)
        tobs = MathTex(r"T_{\mathrm{obs}} = ", r"\bar x^{(1)}", "-", r"\bar x^{(0)}",
                       "=", "12", "-", "8", "=", "4").scale(0.9)
        tobs.set_color(WHITE); tobs[9].set_color(RES)
        tobs.next_to(table, DOWN, buff=0.5)
        self.play_beat(FadeIn(table), Write(tobs), lag_ratio=0.1)

        # all six relabelings: the 10 always subtracts away
        punch = VGroup(
            MathTex(r"\text{across all } \tbinom{4}{2}=6 \text{ relabelings: }"
                    r"\ b_i=10 \text{ cancels every time}").scale(0.8),
            MathTex(r"p = \tfrac{1}{6}\ \text{— the null never sees the backbone}")
            .scale(0.85),
        ).arrange(DOWN, buff=0.3)
        punch[0].set_color(BACK); punch[1].set_color(RES)
        punch.next_to(tobs, DOWN, buff=0.4)
        swap = Text("swap 10 → 10,000:  not one number changes",
                    font_size=23, color=BAD).next_to(punch, DOWN, buff=0.3)
        self.play_beat(FadeIn(punch[0]), FadeIn(punch[1]), FadeIn(swap))

        # the moral of the mechanism
        self.play(FadeOut(VGroup(table, tobs, punch, swap)), run_time=0.5)
        moral = Text("The backbone makes the camera nonspecific\n"
                     "and makes itself inert in the court.\n"
                     "One mechanism, opposite consequences.",
                     font_size=28, color=WHITE, line_spacing=0.85)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))

    def _four_patient_table(self):
        rows = [
            ("10", "+2", "12", "1"),
            ("10", "+2", "12", "1"),
            ("10", "-2", "8", "0"),
            ("10", "-2", "8", "0"),
        ]
        t = MathTable(
            [list(r) for r in rows],
            col_labels=[MathTex("b_i", color=BACK), MathTex("r_i", color=RES),
                        MathTex("x_i", color=VAR), MathTex("y_i", color=WHITE)],
            include_outer_lines=True,
        ).scale(0.55)
        return t


# ----------------------------------------------------------------------
# S5 — the moral, stated as a question to be proved
# ----------------------------------------------------------------------
class S5_Moral(NarratedScene):
    scene_key = "S5_Moral"

    def construct(self):
        self.header("Same matrix C, two operations, opposite verdicts")

        # the shared object
        shared = MathTex("C", r"\ \text{and the maps}\ ", "m_i",
                         r"\ \text{— identical for both}").scale(0.95).shift(UP * 2.2)
        shared[0].set_color(WHITE); shared[2].set_color(VAR)
        self.play_beat(Write(shared))

        divider = DashedLine(UP * 1.6, DOWN * 2.6, color=DIM)

        # camera column
        cam_h = Text("CAMERA", font_size=26, color=DIM)\
            .move_to(LEFT * 3.6 + UP * 1.1)
        cam_eq = MathTex(r"\bar m").scale(1.2).set_color(VAR)\
            .next_to(cam_h, DOWN, buff=0.35)
        cam_note = Text("backbone dominates\n→ nonspecific\n(the critique is right)",
                        font_size=21, color=DIM, line_spacing=0.85)\
            .next_to(cam_eq, DOWN, buff=0.4)
        self.play_beat(FadeIn(cam_h), Write(cam_eq), FadeIn(cam_note))

        # court column
        court_h = Text("COURT", font_size=26, color=RES)\
            .move_to(RIGHT * 3.6 + UP * 1.1)
        court_eq = MathTex(r"\Delta = \bar m^{+}-\bar m^{-}").scale(0.95).set_color(RES)\
            .next_to(court_h, DOWN, buff=0.35)
        court_note = Text("backbone cancels\nunder the label null\n→ signal survives",
                          font_size=21, color=BACK, line_spacing=0.85)\
            .next_to(court_eq, DOWN, buff=0.4)
        self.play_beat(Create(divider), FadeIn(court_h),
                       Write(court_eq), FadeIn(court_note))

        # opposite verdicts
        verdict = VGroup(
            Text("“nothing but hubs”", font_size=24, color=DIM)
            .move_to(LEFT * 3.6 + DOWN * 2.2),
            Text("“here is the symptom\ndirection, cleanly”", font_size=24,
                 color=RES, line_spacing=0.85).move_to(RIGHT * 3.6 + DOWN * 2.15),
        )
        self.play_beat(FadeIn(verdict[0], shift=UP * 0.2),
                       FadeIn(verdict[1], shift=UP * 0.2))

        # why the rebuttal can be right
        self.play(FadeOut(VGroup(shared, divider, cam_h, cam_eq, cam_note,
                                 court_h, court_eq, court_note, verdict)),
                  run_time=0.5)
        why = Text("This is why the rebuttal can be right\n"
                   "even though the critique's average-map fact is true:\n"
                   "different objects, different machines.",
                   font_size=27, color=WHITE, line_spacing=0.85).shift(UP * 0.5)
        self.play_beat(FadeIn(why, shift=UP * 0.2))

        # the question left to prove
        toprove = MathTex(r"\text{To prove next: }\ ",
                          r"\lambda_1(\bar c_1^{+}-\bar c_1^{-})",
                          r"\ \text{cancels from } \Delta").scale(0.9)
        toprove[1].set_color(BAD)
        toprove.next_to(why, DOWN, buff=0.7)
        tag = Text("A failed null is a failed question, not a failed method.",
                   font_size=24, color=RES).next_to(toprove, DOWN, buff=0.4)
        self.play_beat(Write(toprove), FadeIn(tag))
