"""
The Mathematics of Lesion Network Mapping — Critique, Specificity, Convergence.

Seven narrated scenes. Each visual "beat" is tied to one narration line in
narration.py so that subtitles (and the synthesized voiceover) stay in sync.

Render:  manim -ql script.py Scene1_TheMap Scene2_Backbone ...
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — what LNM computes
# ----------------------------------------------------------------------
class Scene1_TheMap(NarratedScene):
    scene_key = "Scene1_TheMap"

    def construct(self):
        title = Text("Lesion Network Mapping", font_size=44, color=WHITE)
        sub = Text("one matrix, one lesion, one product",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP*0.2))
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub), run_time=0.6)

        # connectome matrix C (hub-dominated, symmetric)
        Cmat = Matrix(
            [["2.6", "1.5", "1.1"],
             ["1.5", "1.2", "0.6"],
             ["1.1", "0.6", "0.5"]],
            h_buff=1.1, bracket_h_buff=0.15,
        ).scale(0.85).shift(LEFT * 3.4 + DOWN * 0.4)
        Clab = MathTex("C", color=WHITE).scale(1.1).next_to(Cmat, UP, buff=0.2)
        Ccap = Text("normative connectome", font_size=22, color=DIM).next_to(Cmat, DOWN)
        self.play_beat(FadeIn(Cmat), Write(Clab), FadeIn(Ccap))

        # lesion vector
        lvec = Matrix([["1"], ["0"], ["1"]]).scale(0.85).shift(LEFT * 0.4 + DOWN * 0.4)
        lvec.get_entries().set_color(VAR)
        llab = MathTex(r"\ell", color=VAR).scale(1.1).next_to(lvec, UP, buff=0.2)
        lcap = Text("lesion (0/1)", font_size=22, color=DIM).next_to(lvec, DOWN)
        self.play_beat(FadeIn(lvec), Write(llab), FadeIn(lcap))

        # m = C ell
        eq = MathTex("m", "=", "C", r"\ell").scale(1.4).shift(RIGHT * 3.6 + DOWN * 0.3)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        mcap = Text("the lesion network map", font_size=22, color=DIM).next_to(eq, DOWN)
        self.play_beat(Write(eq), FadeIn(mcap))

        # the readout formula
        self.play(
            FadeOut(VGroup(Cmat, Clab, Ccap, lvec, llab, lcap, mcap)),
            eq.animate.scale(0.8).to_edge(UP, buff=1.2),
            run_time=0.6,
        )
        readout = MathTex(r"(C\ell)_a", "=", r"\sum_b", "C_{ab}", r"\,\ell_b").scale(1.2)
        readout[0].set_color(VAR); readout[3].set_color(WHITE); readout[4].set_color(VAR)
        gloss = Text("total wiring from voxel a into the wound",
                     font_size=24, color=BACK).next_to(readout, DOWN, buff=0.5)
        self.play_beat(Write(readout), FadeIn(gloss))

        # the mystery: two different lesions -> similar maps
        self.play(FadeOut(VGroup(readout, gloss, eq)), run_time=0.5)
        mystery = Text("Different lesions → nearly the same map.   Why?",
                       font_size=30, color=RES)
        l1 = self._mini_map([0.9, 0.55, 0.35, 0.2], LEFT * 3.5 + DOWN * 1.2, "lesion A", VAR)
        l2 = self._mini_map([0.85, 0.6, 0.3, 0.25], RIGHT * 3.5 + DOWN * 1.2, "lesion B", BAD)
        self.play_beat(
            FadeIn(mystery.shift(UP * 1.4)),
            *[FadeIn(m) for m in l1], *[FadeIn(m) for m in l2],
            lag_ratio=0.05,
        )

    def _mini_map(self, vals, center, label, color):
        bars = VGroup()
        for i, v in enumerate(vals):
            r = Rectangle(width=0.35, height=max(0.05, v) * 1.4,
                          fill_color=color, fill_opacity=0.9, stroke_width=0)
            r.move_to(center + RIGHT * (i * 0.42) + UP * (v * 0.7))
            bars.add(r)
        cap = Text(label, font_size=20, color=DIM).next_to(bars, DOWN, buff=0.25)
        return [bars, cap]


# ----------------------------------------------------------------------
# Scene 2 — spectral backbone & convergence
# ----------------------------------------------------------------------
class Scene2_Backbone(NarratedScene):
    scene_key = "Scene2_Backbone"

    def construct(self):
        self.header("The backbone: why maps converge")

        spec = MathTex("C", "=", r"\sum_{j}", r"\lambda_j", "u_j", "u_j^{\\top}").scale(1.2)
        spec[3].set_color(EIG); spec[4].set_color(BACK); spec[5].set_color(BACK)
        spec.shift(UP * 1.6)
        ord_ = MathTex(r"\lambda_1", r"\ge", r"\lambda_2", r"\ge", r"\cdots", r"\ge", "0")\
            .scale(0.9).set_color(EIG).next_to(spec, DOWN, buff=0.4)
        self.play_beat(Write(spec), FadeIn(ord_))

        mapeq = MathTex("m_\\ell", "=", r"\sum_j", r"\lambda_j", r"(u_j^{\top}\ell)", "u_j")\
            .scale(1.15)
        mapeq[0].set_color(VAR); mapeq[3].set_color(EIG)
        mapeq[4].set_color(VAR); mapeq[5].set_color(BACK)
        mapeq.next_to(ord_, DOWN, buff=0.6)
        self.play_beat(Write(mapeq))

        # backbone term highlighted
        bb = MathTex("m_\\ell^{\\mathrm{bb}}", "=", r"\lambda_1", r"(u_1^{\top}\ell)", "u_1")\
            .scale(1.15)
        bb[0].set_color(BACK); bb[2].set_color(EIG)
        bb[3].set_color(VAR); bb[4].set_color(BACK)
        bb.next_to(mapeq, DOWN, buff=0.6)
        gap = Text("λ₁ towers over the rest → one term dominates",
                   font_size=24, color=DIM).next_to(bb, DOWN, buff=0.3)
        self.play_beat(Write(bb), FadeIn(gap))
        self.play_beat(Indicate(bb, color=BACK, scale_factor=1.15))  # "one term dominates"

        # the alignment bound
        self.play(FadeOut(VGroup(spec, ord_, mapeq, bb, gap)), run_time=0.5)
        thm = MathTex(r"\tan\theta_\ell", r"\le",
                      r"\frac{\lambda_2}{\lambda_1}", r"\cdot",
                      r"\frac{\|\ell_\perp\|}{|u_1^{\top}\ell|}").scale(1.25).shift(UP * 1.7)
        thm[0].set_color(RES); thm[2].set_color(EIG)
        box = SurroundingRectangle(thm, color=RES, buff=0.2)
        cap = Text("angle to the backbone is capped by the spectral ratio",
                   font_size=24, color=DIM).next_to(box, DOWN, buff=0.3)
        self.play_beat(Write(thm), Create(box), FadeIn(cap))

        ex = MathTex(r"\lambda = (4.0,\ 0.3,\ 0.1)", r"\quad\Rightarrow\quad",
                     r"\frac{\lambda_2}{\lambda_1} = 0.075").scale(0.95)
        ex.set_color(EIG).next_to(cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(ex))

        # convergence picture
        self.play(FadeOut(VGroup(thm, box, cap, ex)), run_time=0.5)
        self._convergence_fan()

    def _convergence_fan(self):
        origin = LEFT * 1.0 + DOWN * 0.5
        base_angle = 60 * DEGREES
        u1 = Arrow(origin, origin + 4.2 * np.array([np.cos(base_angle), np.sin(base_angle), 0]),
                   buff=0, color=BACK, stroke_width=8)
        u1lab = MathTex("u_1", color=BACK).scale(1.1).next_to(u1.get_end(), UP, buff=0.1)

        maps = VGroup()
        info = [(2.9, "e_1"), (-5.5, "e_3"), (7.6, "e_2")]
        for ang_deg, name in info:
            a = base_angle + ang_deg * DEGREES
            arr = Arrow(origin, origin + 3.6 * np.array([np.cos(a), np.sin(a), 0]),
                        buff=0, color=VAR, stroke_width=5)
            maps.add(arr)

        wedge = Text("all within ~7°", font_size=26, color=RES)\
            .move_to(origin + RIGHT * 3.6 + UP * 1.2)
        caption = Text("three different lesions → one direction",
                       font_size=24, color=DIM).to_edge(DOWN, buff=0.5)

        self.play_beat(GrowArrow(u1), Write(u1lab),
                       *[GrowArrow(a) for a in maps], FadeIn(wedge), FadeIn(caption),
                       lag_ratio=0.12)


# ----------------------------------------------------------------------
# Scene 3 — the critique
# ----------------------------------------------------------------------
class Scene3_Critique(NarratedScene):
    scene_key = "Scene3_Critique"

    def construct(self):
        self.header("The critique (van den Heuvel et al., 2026)")

        eq = MathTex(r"\mathrm{LNM}", "=", r"\textstyle\sum (M \times C)").scale(1.2).shift(UP*1.8)
        eq[0].set_color(VAR)
        self.play_beat(Write(eq))

        conv = MathTex(r"M \to \text{uniform}", r"\quad\Longrightarrow\quad",
                       r"\mathrm{LNM} \to \deg(C)").scale(1.05)
        conv[2].set_color(BAD)
        conv.next_to(eq, DOWN, buff=0.5)
        degcap = Text("the average map → the hub (degree) map",
                      font_size=24, color=DIM).next_to(conv, DOWN, buff=0.25)
        self.play_beat(Write(conv), FadeIn(degcap))

        s = MathTex(r"\mathrm{sLNM} \to \mathrm{PC1}(C)", r",\quad",
                    r"r_{\,\mathrm{PC1},\deg} = 0.82").scale(1.0)
        s[0].set_color(BAD)
        s.next_to(degcap, DOWN, buff=0.5)
        self.play_beat(FadeIn(s))

        # the damning numbers
        self.play(FadeOut(VGroup(eq, conv, degcap, s)), run_time=0.5)
        facts = VGroup(
            Text("random / shuffled lesions reproduce published networks",
                 font_size=26, color=WHITE),
            MathTex(r"r = 0.73 \;-\; 0.95", color=BAD).scale(1.1),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.5)
        self.play_beat(FadeIn(facts[0]), Write(facts[1]))

        bar = self._variance_bar(0.93).shift(DOWN * 0.6)
        self.play_beat(*[FadeIn(m) for m in bar.submobjects], lag_ratio=0.1)

        trap = Text("The convergence trap:  the average map is the hub map.",
                    font_size=28, color=RES).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(trap, shift=UP * 0.2))

    def _variance_bar(self, frac):
        w = 8.0
        full = Rectangle(width=w, height=0.6, stroke_color=WHITE, stroke_width=2,
                         fill_opacity=0)
        filled = Rectangle(width=w * frac, height=0.6, stroke_width=0,
                           fill_color=BAD, fill_opacity=0.85)
        filled.align_to(full, LEFT)
        bar = VGroup(full, filled)
        lab = MathTex(r"93\%", color=BAD).scale(1.0).next_to(full, UP, buff=0.2)
        cap = Text("of LNM-map variance explained by basic connectome properties",
                   font_size=22, color=DIM).next_to(full, DOWN, buff=0.2)
        return VGroup(bar, lab, cap).move_to(ORIGIN)


# ----------------------------------------------------------------------
# Scene 4 — sensitivity, specificity, the wrong null
# ----------------------------------------------------------------------
class Scene4_Specificity(NarratedScene):
    scene_key = "Scene4_Specificity"

    def construct(self):
        self.header("Sensitivity, specificity, and the wrong question")
        cm = self._confusion_matrix()
        self.play_beat(*[Create(x) if isinstance(x, (Line,)) else FadeIn(x) for x in cm["all"]],
                       lag_ratio=0.03)

        # sensitivity
        sens = MathTex(r"\text{Sensitivity}", "=", r"\frac{TP}{TP+FN}").scale(0.95)
        sens.to_edge(RIGHT, buff=0.7).shift(UP * 1.1)
        sens[0].set_color(BACK)
        self.play_beat(Write(sens), Indicate(cm["TP"], color=BACK))

        spec = MathTex(r"\text{Specificity}", "=", r"\frac{TN}{TN+FP}").scale(0.95)
        spec.next_to(sens, DOWN, buff=0.7).align_to(sens, LEFT)
        spec[0].set_color(RES)
        self.play_beat(Write(spec), Indicate(cm["TN"], color=RES))

        # the location null
        self.play(FadeOut(VGroup(*cm["group"], sens, spec)), run_time=0.5)
        q = MathTex(r"H_0^{\mathrm{loc}}:\ ", r"\text{is this \emph{location} special?}").scale(1.0)
        q.shift(UP * 1.8); q[0].set_color(WHITE)
        self.play_beat(Write(q))

        # backbone makes fakes match -> false positives
        chain = VGroup(
            Text("backbone → every map looks alike", font_size=26, color=BACK),
            Text("↓", font_size=30, color=DIM),
            Text("random fakes reproduce the real map", font_size=26, color=WHITE),
            Text("↓", font_size=30, color=DIM),
            Text("the test fires on noise  =  FALSE POSITIVES", font_size=28, color=BAD),
        ).arrange(DOWN, buff=0.22).next_to(q, DOWN, buff=0.5)
        self.play_beat(LaggedStart(*[FadeIn(c) for c in chain], lag_ratio=0.25))

        verdict = MathTex(r"70 \;/\; 78", r"\ \text{maps fail this null}").scale(1.0)
        verdict[0].set_color(BAD)
        verdict.to_edge(DOWN, buff=0.6)
        spec_low = Text("specificity collapses — but the question was wrong",
                        font_size=24, color=RES).next_to(verdict, UP, buff=0.25)
        self.play_beat(Write(verdict), FadeIn(spec_low))

    def _confusion_matrix(self):
        cell = 1.4
        tl = LEFT * 0.7 + UP * 0.4
        grid = VGroup()
        positions = {
            "TP": (0, 0, "TP", BACK), "FN": (1, 0, "FN", BAD),
            "FP": (0, 1, "FP", BAD), "TN": (1, 1, "TN", RES),
        }
        cells = {}
        for key, (col, row, txt, color) in positions.items():
            sq = Square(side_length=cell, stroke_color=WHITE, stroke_width=2,
                        fill_color=color, fill_opacity=0.18)
            sq.move_to(tl + RIGHT * (col * cell) + DOWN * (row * cell))
            label = Text(txt, font_size=26, color=color).move_to(sq)
            cells[key] = VGroup(sq, label)
            grid.add(cells[key])
        # axis labels
        pred = Text("predicted", font_size=20, color=DIM).next_to(grid, UP, buff=0.5)
        actual = Text("actual", font_size=20, color=DIM).rotate(PI / 2).next_to(grid, LEFT, buff=0.5)
        grp = VGroup(grid, pred, actual).move_to(LEFT * 3.0 + DOWN * 0.2)
        allm = [grid, pred, actual]
        return {"all": allm, "group": [grp], "TP": cells["TP"], "TN": cells["TN"], "grid": grid}


# ----------------------------------------------------------------------
# Scene 5 — the right null & backbone cancellation
# ----------------------------------------------------------------------
class Scene5_Cancellation(NarratedScene):
    scene_key = "Scene5_Cancellation"

    def construct(self):
        self.header("The right null: shuffle the symptom, not the lesion")

        setup = VGroup(
            Text("fix the lesions • fix the connectome", font_size=26, color=DIM),
            Text("shuffle only the labels: impaired vs spared", font_size=28, color=VAR),
        ).arrange(DOWN, buff=0.3).shift(UP * 2.0)
        self.play_beat(FadeIn(setup[0]), FadeIn(setup[1], shift=UP * 0.2))

        exact = MathTex(r"p = \frac{1}{|G|}\sum_{\pi}\mathbf{1}\!\left[T(y_\pi)\ge T(y_{\mathrm{id}})\right]",
                        r"\ \Rightarrow\ ", r"\Pr(p\le\alpha)\le\alpha").scale(0.9)
        exact[2].set_color(RES)
        exact.next_to(setup, DOWN, buff=0.5)
        exlab = Text("exact in finite samples — no distributional assumptions",
                     font_size=22, color=DIM).next_to(exact, DOWN, buff=0.25)
        self.play_beat(Write(exact), FadeIn(exlab))

        # decomposition
        self.play(FadeOut(VGroup(setup, exact, exlab)), run_time=0.5)
        decomp = MathTex("x_i", "=", r"\underbrace{\lambda_1(u_1^{\top}\ell_i)\,u_1}_{b_i}",
                         "+", "r_i").scale(1.05).shift(UP * 1.9)
        decomp[0].set_color(VAR); decomp[2].set_color(BACK); decomp[4].set_color(RES)
        dcap = Text("backbone bᵢ depends on the lesion, never on the label",
                    font_size=23, color=DIM).next_to(decomp, DOWN, buff=0.3)
        self.play_beat(Write(decomp), FadeIn(dcap))

        contrast = MathTex(
            "t_v", r"\propto",
            r"\big(\bar b^{(1)}-\bar b^{(0)}\big)\,u_{1,v}",
            "+", r"\big(\bar r^{(1)}-\bar r^{(0)}\big)",
        ).scale(1.0).next_to(dcap, DOWN, buff=0.5)
        contrast[2].set_color(BACK); contrast[4].set_color(RES)
        # strike out the backbone term (same beat as writing the contrast)
        strike = Line(contrast[2].get_left(), contrast[2].get_right(),
                      color=BAD, stroke_width=6)
        cancels = Text("same in every shuffle → cancels", font_size=24, color=BAD)\
            .next_to(contrast, DOWN, buff=0.4)
        self.play_beat(Write(contrast), Create(strike), FadeIn(cancels), lag_ratio=0.45)

        # worked four-patient table
        self.play(FadeOut(VGroup(decomp, dcap, contrast, strike, cancels)), run_time=0.5)
        table = self._four_patient_table().shift(UP * 0.2)
        self.play_beat(FadeIn(table), lag_ratio=0.05)

        tobs = MathTex(r"T_{\mathrm{obs}} = 12 - 8 = 4", color=RES).scale(0.95)
        tobs.next_to(table, DOWN, buff=0.4)
        self.play_beat(Write(tobs))

        punch = VGroup(
            MathTex(r"p = \tfrac{1}{6}\ \text{— the backbone 10 is never seen}").scale(0.9),
            Text("swap 10 → 10,000:  nothing changes.   t>10: 0 false positives / 1000",
                 font_size=23, color=BACK),
        ).arrange(DOWN, buff=0.3)
        punch[0].set_color(RES)
        punch.next_to(tobs, DOWN, buff=0.35)
        self.play_beat(FadeIn(punch[0]), FadeIn(punch[1]))

    def _four_patient_table(self):
        rows = [
            (r"b_i", r"r_i", r"x_i", r"y_i"),
            ("10", "+2", "12", "1"),
            ("10", "+2", "12", "1"),
            ("10", "-2", "8", "0"),
            ("10", "-2", "8", "0"),
        ]
        t = MathTable(
            [list(r) for r in rows[1:]],
            col_labels=[MathTex("b_i", color=BACK), MathTex("r_i", color=RES),
                        MathTex("x_i", color=VAR), MathTex("y_i", color=WHITE)],
            include_outer_lines=True,
        ).scale(0.55)
        return t


# ----------------------------------------------------------------------
# Scene 6 — convergence maps & the triviality bound
# ----------------------------------------------------------------------
class Scene6_ConvergenceMaps(NarratedScene):
    scene_key = "Scene6_ConvergenceMaps"

    def construct(self):
        self.header("Agreement maps: convergence is nearly free")

        op = MathTex(r"A(v) = \mathrm{sign\text{-}agreement\ across\ }K\ \text{patients}")\
            .scale(0.85).shift(UP * 2.0)
        op.set_color(VAR)
        self.play_beat(FadeIn(op))

        indep = MathTex(r"\Pr[\text{all } K \text{ agree}]", "=", "2^{\\,1-K}").scale(1.05)
        indep[2].set_color(BACK)
        indep.next_to(op, DOWN, buff=0.5)
        tbl = MathTex(r"K=2:\ 50\%\qquad K=4:\ 12.5\%\qquad K=8:\ 0.8\%")\
            .scale(0.8).set_color(DIM).next_to(indep, DOWN, buff=0.3)
        self.play_beat(Write(indep), FadeIn(tbl))

        shared = MathTex(r"\Pr[\text{all } K \text{ agree}]", "=", "p^{K}", "+", "(1-p)^{K}")\
            .scale(1.05)
        shared[2].set_color(BAD); shared[4].set_color(BAD)
        shared.next_to(tbl, DOWN, buff=0.6)
        self.play_beat(Write(shared))

        limit = MathTex(r"p \to 1", r"\ \Rightarrow\ ", r"\Pr \to 1",
                        r"\ \text{(independent of } K)").scale(0.95)
        limit[2].set_color(BAD)
        limit.next_to(shared, DOWN, buff=0.4)
        self.play_beat(Write(limit))

        # the empirical curve
        self.play(FadeOut(VGroup(op, indep, tbl, shared, limit)), run_time=0.5)
        self._dice_curve()

    def _dice_curve(self):
        ax = Axes(
            x_range=[0, 0.30, 0.05], y_range=[0, 100, 25],
            x_length=8, y_length=4.2,
            axis_config={"include_tip": True, "color": DIM},
        ).shift(DOWN * 0.3)
        xl = Text("between-lesion Dice overlap", font_size=22, color=DIM)\
            .next_to(ax, DOWN, buff=0.3)
        yl = Text("% 'significant' agreement", font_size=22, color=DIM)\
            .rotate(PI / 2).next_to(ax, LEFT, buff=0.2)
        pts = [(0.08, 10), (0.16, 64), (0.25, 97)]
        dots = VGroup(*[Dot(ax.c2p(x, y), color=BAD, radius=0.08) for x, y in pts])
        curve = ax.plot(lambda x: 100 * (1 / (1 + np.exp(-35 * (x - 0.155)))),
                        x_range=[0.04, 0.28], color=BAD, stroke_width=4)
        labels = VGroup(*[
            Text(f"{y}%", font_size=20, color=BAD).next_to(ax.c2p(x, y), UP, buff=0.15)
            for x, y in pts
        ])
        self.play_beat(Create(ax), FadeIn(xl), FadeIn(yl),
                       Create(curve), *[FadeIn(d) for d in dots],
                       *[FadeIn(l) for l in labels], lag_ratio=0.08)


# ----------------------------------------------------------------------
# Scene 7 — camera vs court, resolution
# ----------------------------------------------------------------------
class Scene7_Resolution(NarratedScene):
    scene_key = "Scene7_Resolution"

    def construct(self):
        self.header("Resolution: the camera and the court")

        divider = DashedLine(UP * 2.5, DOWN * 2.8, color=DIM)
        cam_t = Text("CAMERA  (description)", font_size=26, color=DIM)\
            .move_to(LEFT * 3.5 + UP * 2.6)
        court_t = Text("COURT  (inference)", font_size=26, color=RES)\
            .move_to(RIGHT * 3.5 + UP * 2.6)
        self.play_beat(Create(divider), FadeIn(cam_t), FadeIn(court_t))

        cam_eq = MathTex(r"\bar m", "=", r"\tfrac{1}{n}\textstyle\sum_i m_i").scale(0.95)
        cam_eq.move_to(LEFT * 3.5 + UP * 1.2); cam_eq[0].set_color(VAR)
        cam_note = Text("backbone-dominated → nonspecific\n(the critique is right)",
                        font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(cam_eq, DOWN, buff=0.4)
        self.play_beat(Write(cam_eq), FadeIn(cam_note))

        court_eq = MathTex(r"\Delta", "=", r"\bar m^{+}-\bar m^{-}").scale(0.95)
        court_eq.move_to(RIGHT * 3.5 + UP * 1.2); court_eq[0].set_color(RES)
        court_note = Text("backbone cancels → signal survives",
                          font_size=22, color=BACK).next_to(court_eq, DOWN, buff=0.4)
        self.play_beat(Write(court_eq), FadeIn(court_note))

        # residualization
        self.play(FadeOut(VGroup(divider, cam_t, court_t, cam_eq, cam_note,
                                 court_eq, court_note)), run_time=0.5)
        resid = MathTex(r"\tilde m_\ell", "=", r"\Pi_B^{\perp} m_\ell", "=",
                        r"\sum_{j>r}\lambda_j (u_j^{\top}\ell)\,u_j").scale(1.0).shift(UP * 1.6)
        resid[0].set_color(BACK); resid[2].set_color(BACK)
        snr = MathTex(r"\mathrm{SNR}(\tilde m)\ \ge\ \mathrm{SNR}(m)").scale(1.0)
        snr.set_color(RES).next_to(resid, DOWN, buff=0.4)
        self.play_beat(Write(resid), FadeIn(snr))

        data = VGroup(
            Text("same-symptom maps", font_size=22, color=DIM),
            MathTex("r = 0.44", color=BACK).scale(1.0),
            Text("different-symptom", font_size=22, color=DIM),
            MathTex("r = 0.09", color=DIM).scale(1.0),
            Text("degree map", font_size=22, color=DIM),
            MathTex("r = 0.16", color=BAD).scale(1.0),
        ).arrange_in_grid(rows=3, cols=2, buff=(0.5, 0.25))
        data.next_to(snr, DOWN, buff=0.5)
        self.play_beat(FadeIn(data), lag_ratio=0.05)

        self.play(FadeOut(VGroup(resid, snr, data)), run_time=0.5)
        moral = VGroup(
            Text("One matrix.  Two operations.  Opposite verdicts.",
                 font_size=30, color=WHITE),
            Text("A failed null is a failed question — not a failed method.",
                 font_size=28, color=RES),
        ).arrange(DOWN, buff=0.4)
        self.play_beat(FadeIn(moral[0], shift=UP * 0.2), FadeIn(moral[1], shift=UP * 0.2))
