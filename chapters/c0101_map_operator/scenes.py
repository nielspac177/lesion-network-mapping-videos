"""c0101_map_operator — The Map Operator, symbol by symbol.

Mini-video #1 of the LNM series. We introduce the seed-based LNM map operator
m = C ell exactly as the source defines it (sections/01_the_charge_formalized.md,
"Definition — the LNM map operator"), decode every symbol on screen, work a tiny
numeric example with the source's 3-voxel connectome, and pose the convergence
mystery as an OPEN question (no pre-concession of the critique).

All numbers come from the source .md files:
  3-voxel C = [[2.635,1.488,1.054],[1.488,1.225,0.597],[1.054,0.597,0.540]]
  eigenvalues lambda = (4.0, 0.3, 0.1); single-voxel lesion -> column of C;
  e_1 map (2.635,1.488,1.054), e_3 map (1.054,0.597,0.540), within ~7 degrees.

Render:
  MEDIA=$HOME/lnm_media/c0101_map_operator ./render.sh \
      chapters/c0101_map_operator/scenes.py -q ql \
      S1_Motivation S2_Connectome S3_Lesion S4_Product S5_WorkedExample S6_Mystery
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES

# The source's 3-voxel connectome (sections/01_the_charge_formalized.md).
C3 = [["2.635", "1.488", "1.054"],
      ["1.488", "1.225", "0.597"],
      ["1.054", "0.597", "0.540"]]


# ----------------------------------------------------------------------
# S1 — Motivation: what LNM asks.
# ----------------------------------------------------------------------
class S1_Motivation(NarratedScene):
    scene_key = "S1_Motivation"

    def construct(self):
        title = Text("The Map Operator", font_size=46, color=WHITE)
        sub = Text("lesion network mapping, symbol by symbol",
                   font_size=24, color=DIM).next_to(title, DOWN, buff=0.3)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))
        self.play(title.animate.scale(0.55).to_edge(UP, buff=0.35),
                  FadeOut(sub), run_time=0.6)

        # patient -> lesion + symptom (location alone is not enough)
        q1 = Text("a lesion, and a symptom", font_size=30, color=VAR).shift(UP * 1.4)
        q1b = Text("location alone is unreliable: scattered lesions, same deficit",
                   font_size=23, color=DIM).next_to(q1, DOWN, buff=0.3)
        self.play_beat(FadeIn(q1, shift=UP * 0.2), FadeIn(q1b))

        # the connectivity question
        self.play(FadeOut(VGroup(q1, q1b)), run_time=0.4)
        ask = Text("Ask instead:  what is the damaged tissue WIRED to?",
                   font_size=30, color=BACK).shift(UP * 1.5)
        atlas = Text("look it up in a normative connectome — a group-averaged atlas\n"
                     "of how every region connects to every other, from healthy controls",
                     font_size=23, color=DIM, line_spacing=0.9).next_to(ask, DOWN, buff=0.45)
        self.play_beat(FadeIn(ask, shift=UP * 0.2), FadeIn(atlas))

        # pool + average -> the circuit
        self.play(FadeOut(VGroup(ask, atlas)), run_time=0.4)
        pool = VGroup(
            Text("pool many patients, same symptom", font_size=27, color=WHITE),
            Text("average their maps", font_size=27, color=WHITE),
            Text("= the circuit whose disruption tends to produce the symptom",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(LaggedStart(*[FadeIn(p, shift=UP * 0.15) for p in pool],
                                   lag_ratio=0.4))

        # the promise: one matrix, one product
        self.play(FadeOut(pool), run_time=0.4)
        eq = MathTex("m", "=", "C", r"\ell").scale(2.0)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        promise = Text("one matrix, one lesion, one product — built symbol by symbol",
                       font_size=25, color=DIM).next_to(eq, DOWN, buff=0.6)
        self.play_beat(Write(eq), FadeIn(promise))


# ----------------------------------------------------------------------
# S2 — The connectome C, symbol by symbol.
# ----------------------------------------------------------------------
class S2_Connectome(NarratedScene):
    scene_key = "S2_Connectome"

    def construct(self):
        self.header("The connectome  C")

        # C is V x V, a row/column per voxel
        sq = MathTex("C", r"\in", r"\mathbb{R}^{\,V\times V}").scale(1.4).shift(UP * 1.7)
        sq[0].set_color(WHITE)
        cap = Text("one row and one column per voxel", font_size=24, color=DIM)\
            .next_to(sq, DOWN, buff=0.4)
        self.play_beat(Write(sq), FadeIn(cap))

        # entry C_ab = normative FC between voxel a and b
        entry = MathTex("C_{ab}", "=", r"\text{FC}(a, b)").scale(1.2).next_to(cap, DOWN, buff=0.6)
        entry[0].set_color(WHITE)
        egloss = Text("normative functional connectivity: how strongly voxels a and b\n"
                      "co-activate in healthy brains",
                      font_size=23, color=DIM, line_spacing=0.9).next_to(entry, DOWN, buff=0.35)
        self.play_beat(Write(entry), FadeIn(egloss))

        # fact 1: symmetric
        self.play(FadeOut(VGroup(sq, cap, entry, egloss)), run_time=0.4)
        sym = MathTex("C_{ab}", "=", "C_{ba}").scale(1.4).shift(UP * 1.9)
        sym.set_color(WHITE)
        symcap = Text("symmetric:  wiring from a to b equals wiring from b to a",
                      font_size=25, color=BACK).next_to(sym, DOWN, buff=0.35)
        self.play_beat(Write(sym), FadeIn(symcap))

        # fact 2: low-rank, one dominant pattern = backbone
        lowrank = VGroup(
            Text("normalized, roughly low-rank: a few patterns explain most of it",
                 font_size=25, color=WHITE),
            Text("the one dominant pattern is the hub / degree pattern  =  the BACKBONE",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.35).next_to(symcap, DOWN, buff=0.6)
        self.play_beat(FadeIn(lowrank[0]), FadeIn(lowrank[1], shift=UP * 0.15))

        # the 3-voxel C appears
        self.play(FadeOut(VGroup(sym, symcap, lowrank)), run_time=0.4)
        Cmat = Matrix(C3, h_buff=1.6, v_buff=1.0,
                      bracket_h_buff=0.18).scale(0.9).shift(LEFT * 1.4)
        Clab = MathTex("C", color=WHITE).scale(1.5).next_to(Cmat, LEFT, buff=0.5)
        smallcap = Text("smallest example that shows the mechanism\n"
                        "(3 voxels; every number checkable by hand)",
                        font_size=22, color=DIM, line_spacing=0.9)\
            .next_to(Cmat, DOWN, buff=0.5)
        self.play_beat(FadeIn(Cmat), Write(Clab), FadeIn(smallcap))

        # annotate: hub on diagonal, symmetry across diagonal
        ent = Cmat.get_entries()
        # diagonal entries: 0, 4, 8 ; (0,0)=2.635 hub
        hub_box = SurroundingRectangle(ent[0], color=BACK, buff=0.12)
        hub_lab = Text("hub: voxel 1", font_size=20, color=BACK)\
            .next_to(Cmat, UP, buff=0.25)
        # mirror pair: (0,1)=1.488 and (1,0)=1.488 -> entries index 1 and 3
        m1 = SurroundingRectangle(ent[1], color=VAR, buff=0.10)
        m2 = SurroundingRectangle(ent[3], color=VAR, buff=0.10)
        mlab = MathTex(r"C_{12}=C_{21}=1.488", color=VAR).scale(0.7)\
            .next_to(smallcap, DOWN, buff=0.3)
        self.play_beat(Create(hub_box), FadeIn(hub_lab),
                       Create(m1), Create(m2), FadeIn(mlab), lag_ratio=0.2)


# ----------------------------------------------------------------------
# S3 — The lesion ell.
# ----------------------------------------------------------------------
class S3_Lesion(NarratedScene):
    scene_key = "S3_Lesion"

    def construct(self):
        self.header(r"The lesion  ℓ")

        # ell is a column vector, one entry per voxel
        decl = MathTex(r"\ell", r"\in", r"\{0,1\}^{\,V}").scale(1.5).shift(UP * 1.8)
        decl[0].set_color(VAR)
        decl_cap = Text("a column vector — one entry per voxel", font_size=25, color=DIM)\
            .next_to(decl, DOWN, buff=0.4)
        self.play_beat(Write(decl), FadeIn(decl_cap))

        # the indicator rule
        rule = MathTex(r"\ell_b", "=",
                       r"\begin{cases} 1 & \text{voxel } b \text{ destroyed}\\"
                       r"0 & \text{voxel } b \text{ spared}\end{cases}").scale(1.1)
        rule.next_to(decl_cap, DOWN, buff=0.6)
        rule[0].set_color(VAR)
        self.play_beat(Write(rule))

        # pure geometry, not a strength
        geom = Text("not a strength, not a measurement — pure geometry:\n"
                    "it only marks WHICH voxels the lesion occupies",
                    font_size=25, color=BACK, line_spacing=0.9)\
            .next_to(rule, DOWN, buff=0.5)
        self.play_beat(FadeIn(geom))

        # a concrete 1,0,1 lesion
        self.play(FadeOut(VGroup(decl, decl_cap, rule, geom)), run_time=0.4)
        lvec = Matrix([["1"], ["0"], ["1"]], v_buff=0.9).scale(1.0).shift(LEFT * 2.0)
        lvec.get_entries().set_color(VAR)
        llab = MathTex(r"\ell", color=VAR).scale(1.4).next_to(lvec, LEFT, buff=0.5)
        labels = VGroup(
            Text("voxel 1: destroyed", font_size=22, color=VAR),
            Text("voxel 2: spared", font_size=22, color=DIM),
            Text("voxel 3: destroyed", font_size=22, color=VAR),
        ).arrange(DOWN, buff=0.55, aligned_edge=LEFT).next_to(lvec, RIGHT, buff=0.8)
        self.play_beat(FadeIn(lvec), Write(llab),
                       LaggedStart(*[FadeIn(t) for t in labels], lag_ratio=0.3))

        # the connectome never saw this patient
        note = Text("the entire input from the patient — and C never saw this patient;\n"
                    "only ℓ does.   (remember this.)",
                    font_size=24, color=RES, line_spacing=0.9)\
            .to_edge(DOWN, buff=0.6)
        self.play_beat(FadeIn(note, shift=UP * 0.15))


# ----------------------------------------------------------------------
# S4 — The product m = C ell, unpacked term by term.
# ----------------------------------------------------------------------
class S4_Product(NarratedScene):
    scene_key = "S4_Product"

    def construct(self):
        self.header(r"The product  m = Cℓ")

        eq = MathTex("m", "=", "C", r"\ell").scale(2.0).shift(UP * 1.6)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        self.play_beat(Write(eq))

        # m is the output, lives in R^V
        mdesc = MathTex("m", r"\in", r"\mathbb{R}^{\,V}").scale(1.2).next_to(eq, DOWN, buff=0.6)
        mdesc[0].set_color(VAR)
        mcap = Text("the lesion network map: one number per voxel,\n"
                    "the same shape as a single column of C",
                    font_size=24, color=DIM, line_spacing=0.9).next_to(mdesc, DOWN, buff=0.4)
        self.play_beat(Write(mdesc), FadeIn(mcap))

        # the readout formula
        self.play(FadeOut(VGroup(mdesc, mcap)),
                  eq.animate.scale(0.7).to_edge(UP, buff=1.0), run_time=0.5)
        readout = MathTex(r"(C\ell)_a", "=", r"\sum_b", "C_{ab}", r"\,\ell_b").scale(1.5)
        readout[0].set_color(VAR); readout[3].set_color(WHITE); readout[4].set_color(VAR)
        self.play_beat(Write(readout))

        # brace the row sweep
        br_row = Brace(readout[3], DOWN, color=DIM)
        row_lab = br_row.get_text("row a of C").set_color(WHITE)
        row_lab.scale(0.8)
        br_les = Brace(readout[4], DOWN, color=DIM)
        les_lab = br_les.get_text("lesion 0/1").set_color(VAR)
        les_lab.scale(0.8)
        sweep = Text("march across row a; against each entry, the lesion's 0 or 1",
                     font_size=23, color=DIM).to_edge(DOWN, buff=1.0)
        self.play_beat(GrowFromCenter(br_row), FadeIn(row_lab),
                       GrowFromCenter(br_les), FadeIn(les_lab), FadeIn(sweep))

        # the two cases: 0 kills the term, 1 keeps C_ab
        self.play(FadeOut(VGroup(br_row, row_lab, br_les, les_lab, sweep)), run_time=0.4)
        case0 = MathTex(r"\ell_b = 0", r"\ \Rightarrow\ ", r"C_{ab}\cdot 0 = 0").scale(1.0)
        case0[0].set_color(VAR); case0[2].set_color(DIM)
        case1 = MathTex(r"\ell_b = 1", r"\ \Rightarrow\ ", r"C_{ab}\cdot 1 = C_{ab}").scale(1.0)
        case1[0].set_color(VAR); case1[2].set_color(WHITE)
        cases = VGroup(case0, case1).arrange(DOWN, buff=0.5).next_to(readout, DOWN, buff=0.8)
        c0cap = Text("spared voxel contributes nothing", font_size=21, color=DIM)\
            .next_to(case0, RIGHT, buff=0.5)
        c1cap = Text("damaged voxel contributes a's connectivity to it",
                     font_size=21, color=BACK).next_to(case1, RIGHT, buff=0.5)
        self.play_beat(Write(case0), FadeIn(c0cap), Write(case1), FadeIn(c1cap),
                       lag_ratio=0.3)

        # the meaning: total wiring into the wound
        self.play(FadeOut(VGroup(case0, case1, c0cap, c1cap)), run_time=0.4)
        meaning = MathTex(r"(C\ell)_a", "=", r"\sum_{b:\ \ell_b=1} C_{ab}").scale(1.3)\
            .next_to(readout, DOWN, buff=0.8)
        meaning[0].set_color(VAR); meaning[2].set_color(BACK)
        gloss = Text("the total wiring from voxel a into the wound",
                     font_size=28, color=RES).next_to(meaning, DOWN, buff=0.5)
        self.play_beat(Write(meaning), FadeIn(gloss))

        # full decode summary
        self.play(FadeOut(VGroup(meaning, gloss)), run_time=0.4)
        summary = VGroup(
            Text("C: the wiring", font_size=26, color=WHITE),
            Text("ℓ: selects the damaged columns", font_size=26, color=VAR),
            Text("Σ: totals the connectivity into the lesion", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.35).next_to(readout, DOWN, buff=0.8)
        self.play_beat(LaggedStart(*[FadeIn(s, shift=RIGHT * 0.2) for s in summary],
                                   lag_ratio=0.35))


# ----------------------------------------------------------------------
# S5 — Tiny numeric worked example: single-voxel lesion -> column of C.
# ----------------------------------------------------------------------
class S5_WorkedExample(NarratedScene):
    scene_key = "S5_WorkedExample"

    def construct(self):
        self.header("Worked example: a single-voxel lesion")

        # C and the lesion e_1
        Cmat = Matrix(C3, h_buff=1.5, v_buff=0.9, bracket_h_buff=0.16)\
            .scale(0.75).shift(LEFT * 3.2 + UP * 0.3)
        Clab = MathTex("C", color=WHITE).scale(1.0).next_to(Cmat, UP, buff=0.2)
        lvec = Matrix([["1"], ["0"], ["0"]], v_buff=0.8).scale(0.75)\
            .next_to(Cmat, RIGHT, buff=0.5)
        lvec.get_entries().set_color(VAR)
        llab = MathTex(r"\ell", color=VAR).scale(1.0).next_to(lvec, UP, buff=0.2)
        lcap = Text("lesion only voxel 1", font_size=22, color=VAR)\
            .next_to(lvec, DOWN, buff=0.4)
        self.play_beat(FadeIn(Cmat), Write(Clab), FadeIn(lvec), Write(llab), FadeIn(lcap))

        # only the ell_b=1 term survives
        surv = MathTex(r"(C\ell)_a", "=", r"\sum_b C_{ab}\,\ell_b", "=",
                       r"C_{a1}\cdot 1").scale(0.85)
        surv[0].set_color(VAR); surv[4].set_color(WHITE)
        surv.next_to(Cmat, DOWN, buff=0.9).shift(RIGHT * 1.4)
        killed = Text("every other term × 0 vanishes", font_size=22, color=DIM)\
            .next_to(surv, DOWN, buff=0.3)
        self.play_beat(Write(surv), FadeIn(killed))

        # => the first column of C
        self.play(FadeOut(VGroup(surv, killed)), run_time=0.4)
        # highlight column 1 of C: entries 0,3,6
        ent = Cmat.get_entries()
        col_box = SurroundingRectangle(VGroup(ent[0], ent[3], ent[6]),
                                       color=BACK, buff=0.12)
        col_claim = MathTex(r"m = C\ell = \text{column 1 of } C", color=BACK).scale(0.95)\
            .next_to(Cmat, DOWN, buff=0.9).shift(RIGHT * 1.0)
        self.play_beat(Create(col_box), Write(col_claim))

        # read off the numbers
        mvec = Matrix([["2.635"], ["1.488"], ["1.054"]], v_buff=0.8)\
            .scale(0.75).next_to(col_claim, DOWN, buff=0.5).shift(LEFT * 1.0)
        mvec.get_entries().set_color(RES)
        mlab = MathTex("m", color=VAR).scale(1.0).next_to(mvec, LEFT, buff=0.4)
        self.play_beat(FadeIn(mvec), Write(mlab))

        # the clean fact
        self.play(FadeOut(VGroup(Cmat, Clab, lvec, llab, lcap, col_box, col_claim,
                                 mvec, mlab)), run_time=0.5)
        fact = VGroup(
            Text("A single-voxel lesion hands back that voxel's column of C.",
                 font_size=30, color=WHITE),
            Text("The lesion selects;  the connectome speaks.",
                 font_size=28, color=RES),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.5)
        self.play_beat(FadeIn(fact[0], shift=UP * 0.2), FadeIn(fact[1], shift=UP * 0.2))

        # hub consequence
        self.play(fact.animate.scale(0.8).to_edge(UP, buff=1.3), run_time=0.4)
        hub = Text("voxel 1 is the hub → its column is large and hub-shaped.\n"
                   "Any lesion touching voxel 1 inherits that hub shape.",
                   font_size=26, color=BACK, line_spacing=0.9)
        self.play_beat(FadeIn(hub))


# ----------------------------------------------------------------------
# S6 — The mystery, posed as an open question.
# ----------------------------------------------------------------------
class S6_Mystery(NarratedScene):
    scene_key = "S6_Mystery"

    def construct(self):
        self.header("A mystery to investigate")

        intro = Text("Here a real fight broke out in 2026.",
                     font_size=30, color=WHITE).shift(UP * 2.3)
        self.play_beat(FadeIn(intro, shift=UP * 0.15))

        # lesion voxel 1 -> column 1
        c1 = MathTex(r"\ell = e_1", r"\ \Rightarrow\ ",
                     r"m = (2.635,\ 1.488,\ 1.054)").scale(0.95)
        c1[0].set_color(VAR); c1[2].set_color(RES)
        c1.next_to(intro, DOWN, buff=0.7)
        self.play_beat(Write(c1))

        # lesion voxel 3 -> column 3 (different place)
        c3 = MathTex(r"\ell = e_3", r"\ \Rightarrow\ ",
                     r"m = (1.054,\ 0.597,\ 0.540)").scale(0.95)
        c3[0].set_color(VAR); c3[2].set_color(BAD)
        c3.next_to(c1, DOWN, buff=0.5)
        diffplace = Text("a completely different place", font_size=22, color=DIM)\
            .next_to(c3, DOWN, buff=0.25)
        self.play_beat(Write(c3), FadeIn(diffplace))

        # same direction, ~7 degrees apart
        self.play(FadeOut(VGroup(diffplace)), run_time=0.3)
        angle = MathTex(r"\angle(m_{e_1},\, m_{e_3}) \approx 7^\circ").scale(1.1)\
            .next_to(c3, DOWN, buff=0.7)
        angle.set_color(RES)
        acap = Text("smaller numbers, but the same shape", font_size=23, color=DIM)\
            .next_to(angle, DOWN, buff=0.3)
        self.play_beat(Write(angle), FadeIn(acap))

        # the open question
        self.play(FadeOut(VGroup(intro, c1, c3, angle, acap)), run_time=0.5)
        question = VGroup(
            Text("Different lesions, different places — nearly the same map.",
                 font_size=30, color=WHITE),
            Text("Why?", font_size=44, color=RES),
            Text("Is the map about the lesion, or about the matrix?",
                 font_size=28, color=VAR),
        ).arrange(DOWN, buff=0.45)
        self.play_beat(FadeIn(question[0]), FadeIn(question[1], scale=1.2),
                       FadeIn(question[2]))

        # keep it open — no verdict yet
        self.play(question.animate.scale(0.75).to_edge(UP, buff=1.2), run_time=0.4)
        open_q = Text("Hold the question open. We have not yet earned an answer —\n"
                      "that is the debate the next chapters take up.\n"
                      "For now: we have the operator, and its mystery.",
                      font_size=26, color=DIM, line_spacing=1.0)
        self.play_beat(FadeIn(open_q, shift=UP * 0.15))
