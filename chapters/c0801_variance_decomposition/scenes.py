"""c0801_variance_decomposition — "Single-target variance decomposition".

Five narrated scenes for the FUS-VIM thalamotomy geometry. Every patient is
lesioned at nearly the same target, so the lesion splits as l_i = l_0 + delta_i,
the map splits as m_i = C l_0 + C delta_i, the shared constant C l_0 has zero
across-patient variance, and the critique's scattered-location mechanism cannot
operate. Closes by previewing three moves (c0802-c0804) toward a clean test.

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/06_single_target.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0801_variance_decomposition ./render.sh \
      chapters/c0801_variance_decomposition/scenes.py -q ql \
      S1_Setup S2_Maps S3_Variance S4_Mechanism S5_Plan
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — One target, many patients
# ----------------------------------------------------------------------
class S1_Setup(NarratedScene):
    scene_key = "S1_Setup"

    def construct(self):
        title = Text("One target, many patients", font_size=42, color=WHITE)
        self.play_beat(Write(title))                                        # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), run_time=0.6)

        # the FUS-VIM picture: many patients, one tiny target
        target = Dot(point=ORIGIN, radius=0.18, color=BACK)
        tlab = Text("VIM target  (a few mm across)", font_size=22, color=BACK)\
            .next_to(target, DOWN, buff=0.35)
        ring = Circle(radius=0.55, color=BACK, stroke_width=2).move_to(target)
        self.play_beat(FadeIn(target), Create(ring), FadeIn(tlab))          # beat 2

        # seeds sit on top of each other (slightly jittered dots)
        seeds = VGroup(*[
            Dot(point=ORIGIN + 0.13 * np.array([np.cos(a), np.sin(a), 0]),
                radius=0.05, color=VAR)
            for a in np.linspace(0, 2 * np.pi, 8, endpoint=False)
        ])
        stacked = Text("every patient's seed lands here", font_size=22, color=VAR)\
            .next_to(ring, UP, buff=0.35)
        self.play_beat(FadeIn(seeds, lag_ratio=0.15), FadeIn(stacked))      # beat 3

        # the decomposition l_i = l_0 + delta_i
        self.play(FadeOut(VGroup(target, ring, tlab, seeds, stacked)),
                  run_time=0.5)
        eq = MathTex(r"\ell_i", "=", r"\ell_0", "+", r"\delta_i").scale(1.6)
        eq[0].set_color(VAR); eq[2].set_color(BACK); eq[4].set_color(VAR)
        self.play_beat(Write(eq))                                          # beat 4

        # decode l_0
        eq.generate_target(); eq.target.shift(UP * 1.4)
        self.play(MoveToTarget(eq), run_time=0.5)
        br0 = Brace(eq[2], DOWN, color=BACK)
        l0 = Text("shared VIM core: voxels essentially\nevery ablation hits — same for everyone",
                  font_size=24, color=BACK, line_spacing=0.8)\
            .next_to(br0, DOWN, buff=0.25)
        self.play_beat(GrowFromCenter(br0), FadeIn(l0))                    # beat 5

        # decode delta_i
        self.play(FadeOut(VGroup(br0, l0)), run_time=0.4)
        brd = Brace(eq[4], DOWN, color=VAR)
        di = Text("patient-specific offset: a few rim voxels\n(bigger lesion) or a slight shift of the focus",
                  font_size=24, color=VAR, line_spacing=0.8)\
            .next_to(brd, DOWN, buff=0.25)
        self.play_beat(GrowFromCenter(brd), FadeIn(di))                    # beat 6

        # the moral: size & position, not location
        self.play(FadeOut(VGroup(brd, di)), run_time=0.4)
        moral = VGroup(
            Text("patients differ by SIZE and position-within-target",
                 font_size=26, color=WHITE),
            Text("not by location-across-the-brain", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.25).next_to(eq, DOWN, buff=0.9)
        self.play_beat(FadeIn(moral[0]), FadeIn(moral[1], shift=UP * 0.2)) # beat 7


# ----------------------------------------------------------------------
# Scene 2 — The maps
# ----------------------------------------------------------------------
class S2_Maps(NarratedScene):
    scene_key = "S2_Maps"

    def construct(self):
        self.header("The maps  (Section 06)")

        # m_i = C l_i
        eq1 = MathTex("m_i", "=", "C", r"\ell_i").scale(1.5).shift(UP * 1.3)
        eq1[0].set_color(VAR); eq1[2].set_color(WHITE); eq1[3].set_color(VAR)
        self.play_beat(Write(eq1))                                         # beat 1

        # decode C
        brC = Brace(eq1[2], DOWN, color=WHITE)
        clab = Text("fixed normative connectome,  V voxels x V voxels\nthe same C as everywhere in this paper",
                    font_size=23, color=WHITE, line_spacing=0.8)\
            .next_to(brC, DOWN, buff=0.25)
        self.play_beat(GrowFromCenter(brC), FadeIn(clab))                  # beat 2

        # substitute l_i = l_0 + delta_i
        self.play(FadeOut(VGroup(brC, clab)), run_time=0.4)
        eq2 = MathTex("m_i", "=", "C", r"(", r"\ell_0", "+", r"\delta_i", r")")\
            .scale(1.5).shift(UP * 1.3)
        eq2[0].set_color(VAR); eq2[2].set_color(WHITE)
        eq2[4].set_color(BACK); eq2[6].set_color(VAR)
        self.play_beat(TransformMatchingTex(eq1, eq2))                     # beat 3

        # distribute C -> two terms
        eq3 = MathTex("m_i", "=", "C", r"\ell_0", "+", "C", r"\delta_i")\
            .scale(1.5).shift(UP * 1.3)
        eq3[0].set_color(VAR); eq3[2].set_color(WHITE); eq3[3].set_color(BACK)
        eq3[5].set_color(WHITE); eq3[6].set_color(VAR)
        self.play_beat(TransformMatchingTex(eq2, eq3))                     # beat 4

        # annotate shared term C l_0
        br_shared = Brace(eq3[2:4], DOWN, color=BACK)
        shared = Text("shared: the VIM's own fingerprint\nidentical for every patient",
                      font_size=23, color=BACK, line_spacing=0.8)\
            .next_to(br_shared, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(br_shared), FadeIn(shared))          # beat 5

        # annotate patient-specific term C delta_i
        br_spec = Brace(eq3[5:7], UP, color=VAR)
        spec = Text("patient-specific: the only thing that varies\n(size + within-target position)",
                    font_size=23, color=VAR, line_spacing=0.8)\
            .next_to(br_spec, UP, buff=0.2)
        self.play_beat(GrowFromCenter(br_spec), FadeIn(spec))              # beat 6

        # read off: differences live in the small term
        readoff = Text("between-patient differences come ENTIRELY from  C δᵢ",
                       font_size=26, color=RES).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeOut(VGroup(shared, br_shared)),
                       FadeIn(readoff, shift=UP * 0.2))                    # beat 7


# ----------------------------------------------------------------------
# Scene 3 — Variance kills the common term
# ----------------------------------------------------------------------
class S3_Variance(NarratedScene):
    scene_key = "S3_Variance"

    def construct(self):
        self.header("Variance kills the common term")

        # decode Var_i
        vlab = MathTex(r"\mathrm{Var}_i").scale(1.6).shift(UP * 1.6)
        vlab.set_color(RES)
        vcap = Text("the spread of a quantity as we look ACROSS patients i",
                    font_size=24, color=DIM).next_to(vlab, DOWN, buff=0.35)
        self.play_beat(Write(vlab), FadeIn(vcap))                         # beat 1

        # Var_i(m_i) = Var_i(C l_0 + C delta_i)
        self.play(FadeOut(VGroup(vlab, vcap)), run_time=0.4)
        eq1 = MathTex(r"\mathrm{Var}_i", r"(m_i)", "=",
                      r"\mathrm{Var}_i", r"\big(", "C", r"\ell_0", "+",
                      "C", r"\delta_i", r"\big)").scale(1.15).shift(UP * 1.2)
        eq1[0].set_color(RES); eq1[3].set_color(RES)
        eq1[1].set_color(VAR); eq1[6].set_color(BACK); eq1[9].set_color(VAR)
        self.play_beat(Write(eq1))                                        # beat 2

        # C l_0 is a constant: doesn't depend on i
        cst = Text("C ℓ₀  does not depend on i\nevery patient contributes the SAME C ℓ₀",
                   font_size=25, color=BACK, line_spacing=0.8)\
            .next_to(eq1, DOWN, buff=0.6)
        box = SurroundingRectangle(eq1[5:7], color=BACK, buff=0.12)
        self.play_beat(Create(box), FadeIn(cst))                          # beat 3

        # a constant has zero variance
        self.play(FadeOut(cst), run_time=0.3)
        zero = MathTex(r"\mathrm{Var}_i", r"(", "C", r"\ell_0", r")", "=", "0")\
            .scale(1.2)
        zero[0].set_color(RES); zero[3].set_color(BACK); zero[6].set_color(BAD)
        zero.next_to(eq1, DOWN, buff=0.6)
        zcap = Text("a constant shifts the whole cloud but never spreads it",
                    font_size=23, color=DIM).next_to(zero, DOWN, buff=0.25)
        self.play_beat(Write(zero), FadeIn(zcap))                         # beat 4

        # so the shared term drops out
        self.play(FadeOut(VGroup(eq1, box, zero, zcap)), run_time=0.5)
        key = MathTex(r"\mathrm{Var}_i", r"(m_i)", "=",
                      r"\mathrm{Var}_i", r"(", "C", r"\delta_i", r")")\
            .scale(1.5).shift(UP * 0.6)
        key[0].set_color(RES); key[3].set_color(RES)
        key[1].set_color(VAR); key[6].set_color(VAR)
        kbox = SurroundingRectangle(key, color=RES, buff=0.2)
        self.play_beat(Write(key), Create(kbox))                          # beat 5

        # delta_i dominated by size + small position offset
        dom = Text("all between-patient variance lives in the small term;\nδᵢ is dominated by lesion SIZE plus a small position offset",
                   font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(kbox, DOWN, buff=0.5)
        self.play_beat(FadeIn(dom, shift=UP * 0.2))                       # beat 6

        # the mutation in one line
        mut = VGroup(
            Text("different locations sampling one C", font_size=24, color=DIM),
            Text("↓  becomes", font_size=22, color=DIM),
            Text("graded perturbation of one seed", font_size=24, color=RES),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.55)
        self.play_beat(FadeOut(dom),
                       LaggedStart(*[FadeIn(m) for m in mut], lag_ratio=0.3))  # beat 7


# ----------------------------------------------------------------------
# Scene 4 — The scattered-locations mechanism vanishes
# ----------------------------------------------------------------------
class S4_Mechanism(NarratedScene):
    scene_key = "S4_Mechanism"

    def construct(self):
        self.header("The scattered-locations mechanism vanishes")

        # P1's engine: many locations, one C
        engine = VGroup(
            Text("P1's engine needs:", font_size=27, color=BAD),
            Text("many DIFFERENT lesion locations, all sampling the same C",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.9)
        self.play_beat(FadeIn(engine, shift=UP * 0.2))                    # beat 1

        # scattered seeds -> backbone
        seeds = VGroup(*[
            Dot(2.6 * np.array([np.cos(a), np.sin(a), 0]) * (0.5 + 0.5 * (k % 2))
                + DOWN * 0.4, radius=0.07, color=VAR)
            for k, a in enumerate(np.linspace(0, 2 * np.pi, 9, endpoint=False))
        ])
        cone = Text("all project onto the leading components → the BACKBONE",
                    font_size=24, color=BACK).to_edge(DOWN, buff=1.1)
        self.play_beat(FadeIn(seeds, lag_ratio=0.1), FadeIn(cone))        # beat 2

        # premise = variance in location
        self.play(FadeOut(VGroup(seeds, cone)), run_time=0.4)
        prem = VGroup(
            Text("the demonstration needs a POPULATION of scattered seeds",
                 font_size=25, color=WHITE),
            Text("its premise: variance in lesion LOCATION", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.25).next_to(engine, DOWN, buff=0.7)
        self.play_beat(FadeIn(prem[0]), FadeIn(prem[1], shift=UP * 0.2))   # beat 3

        # here: one location, take away scatter
        self.play(FadeOut(VGroup(engine, prem)), run_time=0.5)
        here = VGroup(
            Text("Here: one location, dosed at different sizes.",
                 font_size=28, color=WHITE),
            Text("Take away the scatter → take away the demonstration.",
                 font_size=28, color=RES),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.0)
        self.play_beat(FadeIn(here[0]), FadeIn(here[1], shift=UP * 0.2))   # beat 4

        # premise is gone -> can't operate
        gone = MathTex(r"\mathrm{Var}_i(\text{location})", "=", "0",
                       r"\ \Rightarrow\ ", r"\text{premise gone}")\
            .scale(1.0)
        gone[2].set_color(BAD); gone[4].set_color(BAD)
        gone.next_to(here, DOWN, buff=0.7)
        self.play_beat(Write(gone))                                       # beat 5

        # a genuinely different object
        diff = VGroup(
            Text("what is left is a DIFFERENT object:", font_size=26, color=WHITE),
            Text("a graded dose (size, position)  →  a graded outcome",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeOut(gone), FadeIn(diff, shift=UP * 0.2))        # beat 6


# ----------------------------------------------------------------------
# Scene 5 — Three moves for a clean test
# ----------------------------------------------------------------------
class S5_Plan(NarratedScene):
    scene_key = "S5_Plan"

    def construct(self):
        self.header("Three moves for a clean test")

        # the surviving threat: C l_0
        threat = VGroup(
            Text("one threat survives the mutation:", font_size=26, color=BAD),
            MathTex("C", r"\ell_0", r"\quad\text{the shared backbone}").scale(1.1),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.9)
        threat[1][1].set_color(BACK)
        self.play_beat(FadeIn(threat[0]), Write(threat[1]))               # beat 1

        # average map is mostly backbone
        avg = MathTex(r"\bar{m}", r"\approx", "C", r"\ell_0",
                      r"\ \approx\ ", r"\text{hub structure}").scale(1.0)
        avg[0].set_color(VAR); avg[3].set_color(BACK); avg[5].set_color(BACK)
        avg.next_to(threat, DOWN, buff=0.6)
        acap = Text("the average single-target map is, once again, mostly backbone",
                    font_size=23, color=DIM).next_to(avg, DOWN, buff=0.25)
        self.play_beat(Write(avg), FadeIn(acap))                          # beat 2

        # the job: test C delta_i without C l_0 faking it
        self.play(FadeOut(VGroup(threat, avg, acap)), run_time=0.5)
        job = VGroup(
            MathTex(r"\text{test the small part }", "C", r"\delta_i",
                    r"\text{ ...}").scale(1.0),
            Text("...without letting the large shared part manufacture significance",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.9)
        job[0][2].set_color(VAR)
        self.play_beat(FadeIn(job, shift=UP * 0.2))                       # beat 3

        # move 1
        m1 = VGroup(
            Text("Move 1", font_size=26, color=RES),
            Text("outcome-label permutation, size-protected", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.4).next_to(job, DOWN, buff=0.55)
        m1cap = Text("shuffle outcomes with size held fixed → neither backbone nor size can fake it",
                     font_size=21, color=DIM).next_to(m1, DOWN, buff=0.15)
        self.play_beat(FadeIn(m1, shift=RIGHT * 0.2), FadeIn(m1cap))       # beat 4

        # move 2
        m2 = VGroup(
            Text("Move 2", font_size=26, color=RES),
            Text("strip the backbone", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.4).next_to(m1cap, DOWN, buff=0.4)
        m2cap = Text("project each map off the leading connectome subspace before testing",
                     font_size=21, color=DIM).next_to(m2, DOWN, buff=0.15)
        self.play_beat(FadeIn(m2, shift=RIGHT * 0.2), FadeIn(m2cap))       # beat 5

        # move 3
        m3 = VGroup(
            Text("Move 3", font_size=26, color=RES),
            Text("beat a degree baseline", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.4).next_to(m2cap, DOWN, buff=0.4)
        m3cap = Text("predict held-out outcomes; beat a model using only hub-connectedness",
                     font_size=21, color=DIM).next_to(m3, DOWN, buff=0.15)
        # fade the header as the third move lands: keeps the list uncluttered
        self.play_beat(FadeOut(job), FadeIn(m3, shift=RIGHT * 0.2),
                       FadeIn(m3cap))                                       # beat 6

        # the moral: calibration / power / credibility -> c0802-c0804
        self.play(FadeOut(VGroup(m1, m1cap, m2, m2cap, m3, m3cap)),
                  run_time=0.5)
        moral = VGroup(
            Text("Move 1 fixes calibration.", font_size=28, color=WHITE),
            Text("Move 2 improves power.", font_size=28, color=WHITE),
            Text("Move 3 is the credibility bar.", font_size=28, color=WHITE),
            Text("They set up the next three chapters.", font_size=28, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                      # beat 7
