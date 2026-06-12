"""
From the operator to a real LNM pipeline (c0102_real_pipeline).

Five narrated scenes. We show what a real lesion network mapping pipeline
computes — seed -> normative connectome -> per-subject map -> group t-map —
and pin down exactly where the clean operator m = C ell is exact and where it
idealizes (Fisher-z, thresholding, averaging). Source-grounded in
responses/lnm_critique/sections/00_abstract_intro.md and 01_the_charge_formalized.md.

Every visual beat is tied to one narration line in narration.py for sync.
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the seed: lesion voxels become the 0/1 indicator ell
# ----------------------------------------------------------------------
class S1_Seed(NarratedScene):
    scene_key = "S1_Seed"

    def construct(self):
        # the clean operator, parked at top
        op = MathTex("m", "=", "C", r"\ell").scale(1.5)
        op[0].set_color(VAR); op[2].set_color(WHITE); op[3].set_color(VAR)
        q = Text("...but where does ℓ come from?", font_size=26, color=DIM)\
            .next_to(op, DOWN, buff=0.5)
        self.play_beat(Write(op), FadeIn(q, shift=UP * 0.2))
        self.play(op.animate.scale(0.6).to_edge(UP, buff=0.4),
                  FadeOut(q), run_time=0.6)

        # a brain "scan" with a traced lesion blob
        brain = Ellipse(width=4.2, height=3.0, color=DIM, stroke_width=3)\
            .shift(LEFT * 3.4 + DOWN * 0.3)
        lesion = Circle(radius=0.55, color=BAD, fill_color=BAD, fill_opacity=0.6,
                        stroke_width=3).move_to(brain.get_center() + LEFT * 0.7 + UP * 0.4)
        scan_cap = Text("traced lesion on a scan", font_size=22, color=DIM)\
            .next_to(brain, DOWN, buff=0.25)
        self.play_beat(Create(brain), FadeIn(lesion), FadeIn(scan_cap))

        # the seed vector ell of 0/1, with the lesioned rows = 1
        entries = ["0", "1", "1", "0", "1", "0"]
        lvec = Matrix([[e] for e in entries]).scale(0.7)\
            .shift(RIGHT * 1.0 + DOWN * 0.3)
        for i, e in enumerate(entries):
            lvec.get_entries()[i].set_color(VAR if e == "1" else DIM)
        llab = MathTex(r"\ell", color=VAR).scale(1.2).next_to(lvec, UP, buff=0.2)
        lcap = Text("seed: 1 inside, 0 outside", font_size=22, color=DIM)\
            .next_to(lvec, DOWN, buff=0.25)
        # arrow from lesion to the vector
        arr = Arrow(lesion.get_right(), lvec.get_left(), buff=0.3,
                    color=VAR, stroke_width=4)
        self.play_beat(GrowArrow(arr), FadeIn(lvec), Write(llab), FadeIn(lcap))

        # ell is literally a column of 0/1, one per voxel
        defn = MathTex(r"\ell", r"\in", r"\{0,1\}^{V}").scale(1.2)\
            .shift(RIGHT * 4.0 + DOWN * 0.3)
        defn[0].set_color(VAR)
        defn_cap = Text("one entry per voxel", font_size=22, color=DIM)\
            .next_to(defn, DOWN, buff=0.25)
        self.play_beat(Write(defn), FadeIn(defn_cap))

        # real lesions are blobs -> many ones at once; grow the blob
        bigger = Circle(radius=0.95, color=BAD, fill_color=BAD, fill_opacity=0.55,
                        stroke_width=3).move_to(lesion.get_center())
        many = Text("hundreds of voxels → many 1's at once",
                    font_size=24, color=BACK).to_edge(DOWN, buff=0.55)
        self.play_beat(Transform(lesion, bigger), FadeIn(many, shift=UP * 0.2))

        # the seed is the patient's only contribution: which rows light up
        self.play(FadeOut(VGroup(brain, lesion, scan_cap, arr, lvec, llab, lcap,
                                 defn, defn_cap, many)), run_time=0.5)
        moral = VGroup(
            Text("The patient contributes one thing:", font_size=30, color=WHITE),
            Text("which rows of the brain are marked.", font_size=30, color=VAR),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(FadeIn(moral[0], shift=UP * 0.2),
                       FadeIn(moral[1], shift=UP * 0.2))


# ----------------------------------------------------------------------
# Scene 2 — the normative connectome: group connectome C, m = C ell
# ----------------------------------------------------------------------
class S2_Connectome(NarratedScene):
    scene_key = "S2_Connectome"

    def construct(self):
        self.header("The normative connectome: one matrix, built once")

        # NOT the patient's own connections
        contrast = VGroup(
            Text("not this patient's connections", font_size=28, color=BAD),
            Text("a normative connectome from healthy subjects", font_size=28, color=BACK),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.4)
        self.play_beat(FadeIn(contrast[0]), FadeIn(contrast[1], shift=UP * 0.2))

        # the matrix C, symmetric & hub-dominated (values from the 3-voxel example)
        self.play(FadeOut(contrast), run_time=0.4)
        Cmat = Matrix(
            [["2.6", "1.5", "1.1"],
             ["1.5", "1.2", "0.6"],
             ["1.1", "0.6", "0.5"]],
            h_buff=1.1, bracket_h_buff=0.15,
        ).scale(0.8).shift(LEFT * 3.6 + DOWN * 0.2)
        Clab = MathTex("C", color=WHITE).scale(1.3).next_to(Cmat, UP, buff=0.2)
        ab = MathTex(r"C_{ab}", r"=", r"\text{FC}(a,b)").scale(0.85)\
            .set_color(WHITE).next_to(Cmat, DOWN, buff=0.3)
        ab[0].set_color(WHITE)
        ccap = Text("connectivity of voxel a to voxel b", font_size=20, color=DIM)\
            .next_to(ab, DOWN, buff=0.2)
        self.play_beat(FadeIn(Cmat), Write(Clab), Write(ab), FadeIn(ccap))

        # symmetry: highlight mirror entries
        sym = MathTex(r"C_{ab}", "=", r"C_{ba}").scale(1.0)\
            .shift(RIGHT * 3.4 + UP * 1.6)
        sym[0].set_color(WHITE); sym[2].set_color(WHITE)
        symcap = Text("symmetric: mirror across the diagonal",
                      font_size=22, color=DIM).next_to(sym, DOWN, buff=0.25)
        self.play_beat(Write(sym), FadeIn(symcap))

        # the product m = C ell
        prod = MathTex("m", "=", "C", r"\ell").scale(1.4)\
            .shift(RIGHT * 3.4 + DOWN * 0.6)
        prod[0].set_color(VAR); prod[2].set_color(WHITE); prod[3].set_color(VAR)
        pcap = Text("the per-patient lesion network map",
                    font_size=22, color=DIM).next_to(prod, DOWN, buff=0.3)
        self.play_beat(Write(prod), FadeIn(pcap))

        # read out one voxel: (C ell)_a = sum_b C_ab ell_b
        self.play(FadeOut(VGroup(Cmat, Clab, ab, ccap, sym, symcap, prod, pcap)),
                  run_time=0.5)
        readout = MathTex(r"(C\ell)_a", "=", r"\sum_b", "C_{ab}", r"\,\ell_b")\
            .scale(1.3).shift(UP * 1.2)
        readout[0].set_color(VAR); readout[3].set_color(WHITE); readout[4].set_color(VAR)
        b_a = Brace(readout[0], DOWN, color=DIM)
        b_a_t = b_a.get_text("voxel a of the map").scale(0.6)
        b_sum = Brace(VGroup(readout[2], readout[3], readout[4]), DOWN, color=DIM)
        b_sum_t = b_sum.get_text("sum over every voxel b").scale(0.6)
        self.play_beat(Write(readout), GrowFromCenter(b_a), FadeIn(b_a_t),
                       GrowFromCenter(b_sum), FadeIn(b_sum_t))

        # ell_b is 0/1 -> sum collapses to the lesioned b's only
        collapse = MathTex(r"\ell_b \in \{0,1\}", r"\;\Rightarrow\;",
                           r"(C\ell)_a = \sum_{b \in \text{lesion}} C_{ab}")\
            .scale(0.95).to_edge(DOWN, buff=0.7)
        collapse[0].set_color(VAR); collapse[2].set_color(BACK)
        gloss = Text("total wiring from voxel a into the wound",
                     font_size=24, color=BACK).next_to(collapse, UP, buff=0.35)
        self.play_beat(Write(collapse), FadeIn(gloss))

        # do that at every a -> one per-patient map
        self.play(FadeOut(VGroup(readout, b_a, b_a_t, b_sum, b_sum_t,
                                 collapse, gloss)), run_time=0.5)
        mapstrip = self._map_strip().shift(UP * 0.3)
        mapcap = Text("one map per patient: each voxel scored by wiring to the wound",
                      font_size=24, color=VAR).next_to(mapstrip, DOWN, buff=0.55)
        self.play_beat(FadeIn(mapstrip, lag_ratio=0.1), FadeIn(mapcap, shift=UP * 0.2))

    def _map_strip(self):
        vals = [0.25, 0.55, 0.9, 0.65, 0.35, 0.8, 0.45, 0.2]
        bars = VGroup()
        for i, v in enumerate(vals):
            col = interpolate_color(ManimColor(BG), ManimColor(VAR), v)
            r = Rectangle(width=0.55, height=0.9, fill_color=col,
                          fill_opacity=1.0, stroke_color=DIM, stroke_width=1)
            r.move_to(RIGHT * (i * 0.57))
            bars.add(r)
        bars.move_to(ORIGIN)
        lab = MathTex(r"m = C\ell", color=VAR).scale(0.85).next_to(bars, LEFT, buff=0.3)
        return VGroup(bars, lab)


# ----------------------------------------------------------------------
# Scene 3 — per-subject seed map, then the group t-map; define t
# ----------------------------------------------------------------------
class S3_GroupTmap(NarratedScene):
    scene_key = "S3_GroupTmap"

    def construct(self):
        self.header("From one map to a group t-map")

        # one patient, one map -> proves nothing
        one = VGroup(
            MathTex("m", "=", "C", r"\ell").scale(1.2),
            Text("one patient → one map → proves nothing",
                 font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.4).shift(UP * 1.6)
        one[0][0].set_color(VAR); one[0][2].set_color(WHITE); one[0][3].set_color(VAR)
        self.play_beat(Write(one[0]), FadeIn(one[1]))

        # n patients, each ell_i -> m_i
        self.play(FadeOut(one), run_time=0.4)
        stack = MathTex(r"m_i", "=", "C", r"\ell_i", r",\quad", "i = 1,\dots,n")\
            .scale(1.15).shift(UP * 1.7)
        stack[0].set_color(VAR); stack[2].set_color(WHITE); stack[3].set_color(VAR)
        stack[5].set_color(BACK)
        scap = Text("n patients sharing the symptom, n stacked maps",
                    font_size=23, color=DIM).next_to(stack, DOWN, buff=0.3)
        self.play_beat(Write(stack), FadeIn(scap))

        # at each voxel: n numbers, signal vs noise?
        self.play(FadeOut(VGroup(stack, scap)), run_time=0.4)
        voxq = VGroup(
            Text("at voxel v: n values, one per patient", font_size=26, color=VAR),
            Text("reliably connected, or just noise?", font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.7)
        # a little row of n sample values
        vals = VGroup(*[
            Text(s, font_size=24, color=BACK)
            for s in ["0.8", "0.6", "0.9", "0.5", "0.7"]
        ]).arrange(RIGHT, buff=0.55).next_to(voxq, DOWN, buff=0.4)
        self.play_beat(FadeIn(voxq[0]), FadeIn(voxq[1]), FadeIn(vals, lag_ratio=0.2))

        # the t statistic, symbol by symbol
        self.play(FadeOut(VGroup(voxq, vals)), run_time=0.4)
        tstat = MathTex("t_v", "=", r"\frac{\bar{x}_v}{\mathrm{SE}_v}").scale(1.6)\
            .shift(UP * 1.2)
        tstat[0].set_color(RES)
        tcap = Text("the t statistic at voxel v: mean over standard error",
                    font_size=24, color=DIM).next_to(tstat, DOWN, buff=0.4)
        self.play_beat(Write(tstat), FadeIn(tcap))

        # mean numerator
        self.play(FadeOut(tcap), tstat.animate.shift(UP * 0.3 + LEFT * 3.2), run_time=0.5)
        mean = MathTex(r"\bar{x}_v", "=", r"\frac{1}{n}", r"\sum_{i=1}^{n}", "m_{i,v}")\
            .scale(1.0).shift(RIGHT * 1.2 + UP * 1.1)
        mean[0].set_color(VAR); mean[4].set_color(VAR)
        mean_cap = Text("mean: average map value at v, the signal",
                        font_size=22, color=VAR).next_to(mean, DOWN, buff=0.3)
        self.play_beat(Write(mean), FadeIn(mean_cap))

        # standard error denominator
        se = MathTex(r"\mathrm{SE}_v", "=", r"\frac{s_v}{\sqrt{n}}").scale(1.0)\
            .shift(RIGHT * 1.2 + DOWN * 0.9)
        se[0].set_color(BAD)
        se_cap = Text("standard error: spread ÷ √n, the noise",
                      font_size=22, color=BAD).next_to(se, DOWN, buff=0.3)
        self.play_beat(Write(se), FadeIn(se_cap))

        # t = signal over noise
        self.play(FadeOut(VGroup(tstat, mean, mean_cap, se, se_cap)), run_time=0.5)
        sn = MathTex("t_v", "=", r"\frac{\text{signal}}{\text{noise}}",
                     "=", r"\frac{\bar{x}_v}{\mathrm{SE}_v}").scale(1.3).shift(UP * 1.4)
        sn[0].set_color(RES); sn[2].set_color(RES)
        snmoral = Text("big t = consistently connected, not lucky once",
                       font_size=26, color=BACK).next_to(sn, DOWN, buff=0.5)
        self.play_beat(Write(sn), FadeIn(snmoral))

        # the group t-map is the published network
        self.play(FadeOut(VGroup(sn, snmoral)), run_time=0.5)
        tmap = self._tmap_strip().shift(UP * 0.4)
        verdict = Text("the group t-map IS the published lesion network",
                       font_size=28, color=RES).next_to(tmap, DOWN, buff=0.6)
        self.play_beat(FadeIn(tmap, lag_ratio=0.1), FadeIn(verdict, shift=UP * 0.2))

    def _tmap_strip(self):
        vals = [0.3, 0.6, 0.95, 0.7, 0.4, 0.85, 0.5, 0.2]
        bars = VGroup()
        for i, v in enumerate(vals):
            col = interpolate_color(ManimColor(BG), ManimColor(RES), v)
            r = Rectangle(width=0.55, height=0.9, fill_color=col,
                          fill_opacity=1.0, stroke_color=DIM, stroke_width=1)
            r.move_to(RIGHT * (i * 0.57))
            bars.add(r)
        bars.move_to(ORIGIN)
        lab = MathTex("t_v", color=RES).scale(0.9).next_to(bars, LEFT, buff=0.3)
        return VGroup(bars, lab)


# ----------------------------------------------------------------------
# Scene 4 — where m = C ell is exact vs an idealization
# ----------------------------------------------------------------------
class S4_Idealization(NarratedScene):
    scene_key = "S4_Idealization"

    def construct(self):
        self.header("Where m = Cℓ is exact, and where it idealizes")

        op = MathTex("m", "=", "C", r"\ell").scale(1.5).shift(UP * 1.6)
        op[0].set_color(VAR); op[2].set_color(WHITE); op[3].set_color(VAR)
        q = Text("exact in one place, simplified in three",
                 font_size=26, color=DIM).next_to(op, DOWN, buff=0.4)
        self.play_beat(Write(op), FadeIn(q))

        # the exact core
        self.play(FadeOut(VGroup(op, q)), run_time=0.4)
        exact = VGroup(
            Text("EXACT — the core", font_size=28, color=RES),
            MathTex(r"\ell \in \{0,1\}^V", r"\;\cdot\;",
                    r"\text{one fixed } C", r"\;\cdot\;", r"\;m = C\ell").scale(0.9),
        ).arrange(DOWN, buff=0.4).shift(UP * 1.3)
        exact[1][0].set_color(VAR); exact[1][2].set_color(WHITE); exact[1][4].set_color(VAR)
        ecap = Text("seed, connectome, and product: no approximation",
                    font_size=23, color=DIM).next_to(exact, DOWN, buff=0.4)
        self.play_beat(FadeIn(exact[0]), Write(exact[1]), FadeIn(ecap))

        # idealization 1: Fisher-z
        self.play(FadeOut(VGroup(exact, ecap)), run_time=0.4)
        fz = MathTex(r"C_{ab}", r"\;\longmapsto\;", r"\mathrm{arctanh}(C_{ab})")\
            .scale(1.1).shift(UP * 1.3)
        fz[0].set_color(WHITE); fz[2].set_color(EIG)
        fzcap = VGroup(
            Text("Idealization 1 — Fisher-z", font_size=26, color=EIG),
            Text("a monotone re-scaling: bends numbers, not leading geometry",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(fz, DOWN, buff=0.5)
        self.play_beat(Write(fz), FadeIn(fzcap[0]), FadeIn(fzcap[1]))

        # idealization 2: thresholding -> direction survives
        self.play(FadeOut(VGroup(fz, fzcap)), run_time=0.4)
        thr = MathTex(r"\alpha\, m \;\;\text{and}\;\; m",
                      r"\;\to\;", r"\text{same thresholded picture}")\
            .scale(0.95).shift(UP * 1.3)
        thr[0].set_color(VAR); thr[2].set_color(BACK)
        thrcap = VGroup(
            Text("Idealization 2 — thresholding", font_size=26, color=EIG),
            Text("scalar multiples agree: direction survives, and Cℓ sets direction",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(thr, DOWN, buff=0.5)
        self.play_beat(Write(thr), FadeIn(thrcap[0]), FadeIn(thrcap[1]))

        # idealization 3: averaging / t-map folded into linear operator
        self.play(FadeOut(VGroup(thr, thrcap)), run_time=0.4)
        avg = MathTex(r"t_v = \frac{\bar{x}_v}{\mathrm{SE}_v}",
                      r"\;\;\Longleftarrow\;\;", r"\{m_i = C\ell_i\}")\
            .scale(1.0).shift(UP * 1.3)
        avg[0].set_color(RES); avg[2].set_color(VAR)
        avgcap = VGroup(
            Text("Idealization 3 — averaging / the t-map", font_size=26, color=EIG),
            Text("we fold the group statistic into one linear operator on the maps",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(avg, DOWN, buff=0.5)
        self.play_beat(Write(avg), FadeIn(avgcap[0]), FadeIn(avgcap[1]))

        # none touches the engine: backbone survives
        self.play(FadeOut(VGroup(avg, avgcap)), run_time=0.4)
        moral = VGroup(
            Text("Fisher-z, thresholds, the t-map:", font_size=28, color=DIM),
            Text("monotone reshapings on one matrix multiply.", font_size=28, color=WHITE),
            Text("The shared backbone of C survives all of them.",
                 font_size=28, color=BACK),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral[0]), FadeIn(moral[1]), FadeIn(moral[2]))


# ----------------------------------------------------------------------
# Scene 5 — recap: the faithful abstraction; the live debate ahead
# ----------------------------------------------------------------------
class S5_Recap(NarratedScene):
    scene_key = "S5_Recap"

    def construct(self):
        self.header("The abstraction we will reason about")

        # the pipeline in one breath: three steps
        steps = VGroup(
            self._step("1", r"\ell", "trace lesion → seed", VAR),
            self._step("2", r"m = C\ell", "multiply by group C", WHITE),
            self._step("3", r"t = \frac{\bar{x}}{\mathrm{SE}}", "pool n → t-map", RES),
        ).arrange(RIGHT, buff=0.9).shift(UP * 1.2)
        arrows = VGroup(
            Arrow(steps[0].get_right(), steps[1].get_left(), buff=0.15, color=DIM),
            Arrow(steps[1].get_right(), steps[2].get_left(), buff=0.15, color=DIM),
        )
        self.play_beat(FadeIn(steps, lag_ratio=0.3),
                       *[GrowArrow(a) for a in arrows])

        # one matrix, sampled over and over
        self.play(FadeOut(VGroup(steps, arrows)), run_time=0.4)
        oneC = VGroup(
            Text("every patient, every study:", font_size=28, color=DIM),
            Text("reads from the same one matrix C", font_size=30, color=WHITE),
            Text("each lesion just selects some rows", font_size=28, color=VAR),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.2)
        self.play_beat(FadeIn(oneC[0]), FadeIn(oneC[1]), FadeIn(oneC[2]))

        # why m = C ell is faithful
        self.play(FadeOut(oneC), run_time=0.4)
        faith = VGroup(
            MathTex("m", "=", "C", r"\ell").scale(1.4),
            Text("keeps the one object the critique attacks:", font_size=26, color=DIM),
            Text("a single fixed connectome, sampled by many lesions",
                 font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.9)
        faith[0][0].set_color(VAR); faith[0][2].set_color(WHITE); faith[0][3].set_color(VAR)
        self.play_beat(Write(faith[0]), FadeIn(faith[1]), FadeIn(faith[2]))

        # the live debate: critique is right in a narrow regime
        self.play(FadeOut(faith), run_time=0.4)
        crit = VGroup(
            Text("CRITIQUE (van den Heuvel et al.)", font_size=26, color=BAD),
            MathTex(r"\overline{\mathrm{LNM}}", r"\;\longrightarrow\;", r"\deg(C)")
            .scale(1.1),
            Text("under UNIFORM, NON-OVERLAPPING sampling — and here, right",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.0)
        crit[1][0].set_color(VAR); crit[1][2].set_color(BAD)
        self.play_beat(FadeIn(crit[0]), Write(crit[1]), FadeIn(crit[2]))

        # the rebuttal: real lesions overlap, non-random -> contrast carries signal
        self.play(FadeOut(crit), run_time=0.4)
        reb = VGroup(
            Text("but real symptom lesions OVERLAP and are NON-RANDOM",
                 font_size=25, color=BACK),
            Text("they hit the same region → sample only specific rows of C",
                 font_size=24, color=VAR),
            Text("so the CONTRAST, not the average, can carry signal",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.9)
        self.play_beat(FadeIn(reb[0]), FadeIn(reb[1]), FadeIn(reb[2]))

        # the data bite back
        self.play(FadeOut(reb), run_time=0.4)
        data = VGroup(
            self._datum("same-symptom maps", "r = 0.44", BACK),
            self._datum("different-symptom", "r = 0.09", DIM),
            self._datum("degree map", "r = 0.16", BAD),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.8)
        fp = MathTex(r"t > 10:\;\; 0 \text{ false positives} / 1000 \text{ iterations}")\
            .scale(0.9).set_color(RES).next_to(data, DOWN, buff=0.5)
        self.play_beat(FadeIn(data, lag_ratio=0.2), Write(fp))

        # hold the tension
        self.play(FadeOut(VGroup(data, fp)), run_time=0.5)
        moral = VGroup(
            Text("One matrix, sampled by many lesions.", font_size=30, color=WHITE),
            Text("The average is nonspecific;", font_size=28, color=BAD),
            Text("the calibrated contrast need not be.", font_size=28, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral[0], shift=UP * 0.2),
                       FadeIn(moral[1]), FadeIn(moral[2]))

    def _step(self, n, tex, label, color):
        num = Text(n, font_size=22, color=DIM)
        eq = MathTex(tex).scale(0.95).set_color(color)
        lab = Text(label, font_size=18, color=DIM)
        box = VGroup(num, eq, lab).arrange(DOWN, buff=0.2)
        return box

    def _datum(self, label, val, color):
        lab = Text(label, font_size=24, color=DIM)
        v = MathTex(val, color=color).scale(1.05)
        return VGroup(lab, v).arrange(RIGHT, buff=0.6)
