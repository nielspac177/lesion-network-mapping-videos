"""c0304_convergence_trap_stated — "The convergence trap, stated".

Five narrated scenes. State the convergence trap in its stated, fair form, then
draw the line the critique misses:

  S1_Funnel        every seed (real, synthetic, random) points along the backbone
                   u-one, so any averaged map lands in one cone. Backbone green.
  S2_AverageIsHub  the group-average map = the hub map = degree of C, nonspecific
                   by construction. A shared endpoint certifies the funnel, not the
                   lesion.
  S3_ConcedeCamera explicitly concede the camera: as a one-sample description,
                   convergence is trivial. Rebuttal (Siddiqi) agrees the average
                   converges to the degree map.
  S4_ButContrast   the contrast under a symptom null subtracts the shared backbone
                   away algebraically; the hub cancels. Witness: zero false
                   positives in one thousand iterations at t > 10.
  S5_Bridge        bridge to Parts 4-5: a failed null is a failed question. Two
                   cameras, opposite fates. Define what comes next.

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/05_the_convergence_trap.md
  responses/lnm_critique/papers/P1_critique.md   (Eq. 3; r>0.44; 0/1000 at t>10;
    0.44 / 0.09 / 0.16; degree = row-sum of C)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0304_convergence_trap_stated ./render.sh \
      chapters/c0304_convergence_trap_stated/scenes.py -q ql \
      S1_Funnel S2_AverageIsHub S3_ConcedeCamera S4_ButContrast S5_Bridge
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the funnel: three seeds, one cone along u_1
# ----------------------------------------------------------------------
class S1_Funnel(NarratedScene):
    scene_key = "S1_Funnel"

    def construct(self):
        self.header("The funnel")

        intro = Text("every seed points in nearly the same direction",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # the geometry: m = C ell inherits the backbone u_1
        eq = MathTex("m", "=", "C", r"\ell").scale(1.5).shift(UP * 1.1)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        bb = MathTex(r"\text{backbone } u_1,\ \ \text{scaled by } \lambda_1")\
            .scale(0.9).set_color(BACK).next_to(eq, DOWN, buff=0.35)
        self.play_beat(Write(eq), FadeIn(bb), intro.animate.set_opacity(0.4))  # beat 2

        # three seeds on the left
        self.play(FadeOut(VGroup(intro, eq, bb)), run_time=0.4)
        seeds = VGroup(
            self._seed_chip("real symptom lesion", VAR),
            self._seed_chip("synthetic blob", DIM),
            self._seed_chip("random voxels", BAD),
        ).arrange(DOWN, buff=0.55).shift(LEFT * 4.4)
        self.play_beat(FadeIn(seeds, lag_ratio=0.25))                      # beat 3

        # apex of the cone = u_1 direction, on the right
        apex = RIGHT * 3.4
        u1_arrow = Arrow(apex + LEFT * 0.1, apex + RIGHT * 1.8 + UP * 0.0,
                         color=BACK, buff=0.0, stroke_width=6)
        u1_lab = MathTex(r"u_1", color=BACK).scale(1.2)\
            .next_to(u1_arrow, RIGHT, buff=0.15)
        # three seed-arrows funneling from each chip toward the apex
        funnels = VGroup(*[
            Arrow(chip.get_right() + RIGHT * 0.1, apex, color=c, buff=0.15,
                  stroke_width=3)
            for chip, c in zip(seeds.submobjects, (VAR, DIM, BAD))
        ])
        times_C = MathTex(r"\times\, C", color=WHITE).scale(0.9)\
            .move_to(midpoint(seeds.get_right(), apex) + UP * 1.6)
        self.play_beat(LaggedStart(*[GrowArrow(a) for a in funnels],
                                   lag_ratio=0.25),
                       GrowArrow(u1_arrow), FadeIn(u1_lab), FadeIn(times_C))  # beat 4

        # the cone: shade the wedge that all three land inside
        cone = Polygon(apex, apex + LEFT * 5.2 + UP * 1.7,
                       apex + LEFT * 5.2 + DOWN * 1.7,
                       stroke_color=BACK, stroke_width=2,
                       fill_color=BACK, fill_opacity=0.12)
        cone_lab = Text("one cone, along the backbone",
                        font_size=24, color=BACK).to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(cone), FadeIn(cone_lab))                     # beat 5

        # average lands in the cone too
        avg = Arrow(apex + LEFT * 4.6, apex, color=RES, buff=0.1,
                    stroke_width=6)
        avg_lab = MathTex(r"\bar m", color=RES).scale(1.1)\
            .next_to(avg, UP, buff=0.15).shift(LEFT * 1.2)
        avg_cap = Text("the average lands in the cone too",
                       font_size=22, color=RES).next_to(cone_lab, UP, buff=0.25)
        self.play_beat(GrowArrow(avg), FadeIn(avg_lab),
                       FadeIn(avg_cap), cone_lab.animate.set_opacity(0.5))  # beat 6

        # owned by lambda_1, a property of C alone
        self.play(FadeOut(VGroup(seeds, funnels, u1_arrow, u1_lab, times_C,
                                 cone, cone_lab, avg, avg_lab, avg_cap)),
                  run_time=0.5)
        owned = MathTex(r"\text{averaged direction}", r"\ \propto\ ",
                        r"\lambda_1 u_1", r"\quad(\text{a property of } C \text{ alone})")\
            .scale(0.95)
        owned[2].set_color(BACK)
        self.play_beat(Write(owned))                                       # beat 7

    def _seed_chip(self, label, color):
        box = RoundedRectangle(width=3.0, height=0.7, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=20, color=color).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 2 — the average IS the hub map, by construction
# ----------------------------------------------------------------------
class S2_AverageIsHub(NarratedScene):
    scene_key = "S2_AverageIsHub"

    def construct(self):
        self.header("The average is the hub map")

        intro = Text("group-average map  =  hub map  =  nonspecific",
                     font_size=28, color=RES).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # the bookkeeping: LNM = sum M x C  (Eq. 3)
        eq = MathTex(r"\mathrm{LNM}", "=", r"\textstyle\sum_{s}", "M",
                     r"\times", "C").scale(1.4).shift(UP * 1.0)
        eq[0].set_color(VAR); eq[3].set_color(VAR); eq[5].set_color(WHITE)
        eq3 = Text("(P1, Eq. 3)", font_size=22, color=DIM)\
            .next_to(eq, RIGHT, buff=0.5)
        self.play_beat(Write(eq), FadeIn(eq3), intro.animate.set_opacity(0.4))  # beat 2

        # annotate M and C
        brace_M = Brace(eq[3], UP, color=VAR)
        m_lab = Text("lesion matrix: 1 where a lesion covers a region",
                     font_size=21, color=VAR).next_to(brace_M, UP, buff=0.15)
        brace_C = Brace(eq[5], DOWN, color=WHITE)
        c_lab = Text("fixed normative connectome",
                     font_size=21, color=WHITE).next_to(brace_C, DOWN, buff=0.15)
        self.play_beat(GrowFromCenter(brace_M), FadeIn(m_lab),
                       GrowFromCenter(brace_C), FadeIn(c_lab))             # beat 3

        # M -> I copies C; row-sum = degree = hub map
        self.play(FadeOut(VGroup(intro, eq3, brace_M, m_lab, brace_C, c_lab)),
                  eq.animate.scale(0.7).to_edge(UP, buff=1.0), run_time=0.5)
        conv = MathTex("M", r"\to", "I", r"\ \Rightarrow\ ",
                       r"\text{copies } C").scale(1.1).shift(UP * 0.9)
        conv[0].set_color(VAR); conv[2].set_color(EIG)
        deg = MathTex(r"\text{row-sum of } C", "=", r"\deg(C)", "=",
                      r"\text{hub map}").scale(1.05).next_to(conv, DOWN, buff=0.45)
        deg[2].set_color(BAD); deg[4].set_color(BAD)
        self.play_beat(Write(conv), Write(deg))                           # beat 4

        # name the endpoint: degree, hubs dominate
        endpoint = Text("the funnel's endpoint has a name: degree",
                        font_size=26, color=BAD).next_to(deg, DOWN, buff=0.55)
        self.play_beat(FadeIn(endpoint, shift=UP * 0.2))                  # beat 5

        # arrives fast: r>0.44 at >=10 lesions; >0.62 at 20-25
        self.play(FadeOut(VGroup(conv, deg, endpoint)),
                  eq.animate.set_opacity(0.0), run_time=0.4)
        fast = VGroup(
            MathTex(r"\geq 10\ \text{heterogeneous lesions}", r"\ \Rightarrow\ ",
                    r"r > 0.44").scale(1.0),
            MathTex(r"20\text{–}25\ \text{lesions}", r"\ \Rightarrow\ ",
                    r"r > 0.62").scale(1.0),
        ).arrange(DOWN, buff=0.4)
        fast[0][2].set_color(BAD); fast[1][2].set_color(BAD)
        self.play_beat(FadeIn(fast, lag_ratio=0.3))                       # beat 6

        # shared endpoint certifies the funnel, not the lesion
        self.play(FadeOut(fast), run_time=0.4)
        moral = VGroup(
            Text("a shared endpoint certifies the FUNNEL,", font_size=27, color=WHITE),
            Text("not the lesion", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.6)
        sub = MathTex(r"\text{agreement} = \text{agreement on } u_1")\
            .scale(0.9).set_color(BACK).next_to(moral, DOWN, buff=0.5)
        self.play_beat(FadeIn(moral, shift=UP * 0.2), FadeIn(sub))        # beat 7

        # the convergence map = descriptive shadow of the backbone
        shadow = Text("the convergence map redraws the hub —\nit is the descriptive shadow of the backbone",
                      font_size=24, color=DIM, line_spacing=0.8)\
            .next_to(sub, DOWN, buff=0.5)
        self.play_beat(FadeIn(shadow))                                    # beat 8


# ----------------------------------------------------------------------
# Scene 3 — concede the camera fully
# ----------------------------------------------------------------------
class S3_ConcedeCamera(NarratedScene):
    scene_key = "S3_ConcedeCamera"

    def construct(self):
        self.header("Concede the camera")

        head = Text("as a DESCRIPTION, the camera is broken",
                    font_size=30, color=WHITE).shift(UP * 2.5)
        self.play_beat(FadeIn(head))                                      # beat 1

        # one-sample photograph -> convergence is trivial
        trivial = VGroup(
            Text("one-sample average  =  a photograph of the stack",
                 font_size=26, color=DIM),
            Text("of course every average lands on the backbone — C forced it",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.9)
        self.play_beat(FadeIn(trivial[0]), FadeIn(trivial[1], shift=UP * 0.2))  # beat 2

        # agreement is almost free -> no inference
        free = VGroup(
            Text("significant convergence, by itself, is NOT evidence",
                 font_size=26, color=BAD),
            Text("the agreement was almost free; free cannot buy an inference",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(trivial, DOWN, buff=0.55)
        self.play_beat(FadeIn(free, lag_ratio=0.3))                       # beat 3

        # the rebuttal concedes the math verbatim
        self.play(FadeOut(VGroup(head, trivial, free)), run_time=0.5)
        reb = Text("Rebuttal (Siddiqi et al.):", font_size=27, color=RES)\
            .shift(UP * 2.3)
        concede = Text("\"...will converge on the row-summation vector of C\n"
                       "(the degree map)...\"",
                       font_size=24, color=DIM, line_spacing=0.8)\
            .next_to(reb, DOWN, buff=0.3)
        self.play_beat(FadeIn(reb), FadeIn(concede))                      # beat 4

        # "we fully agree, ASSUMING random sampling" -> the conceded scope
        agree = Text("\"...we fully agree with this,\n"
                     "assuming the connectome is sampled randomly.\"",
                     font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(concede, DOWN, buff=0.4)
        both = Text("both sides agree: under RANDOM sampling, the camera converges to degree",
                    font_size=22, color=DIM).next_to(agree, DOWN, buff=0.35)
        self.play_beat(FadeIn(agree, shift=UP * 0.2), FadeIn(both))       # beat 5

        # grant the narrow conclusion in full
        self.play(FadeOut(VGroup(reb, concede, agree, both)), run_time=0.5)
        granted = VGroup(
            Text("CONCEDED:", font_size=28, color=BACK),
            Text("under UNIFORM, NON-OVERLAPPING sampling,",
                 font_size=24, color=BACK),
            Text("the one-sample average map of a symptomatic group",
                 font_size=25, color=WHITE),
            Text("is backbone-dominated, hence nonspecific.",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).shift(UP * 0.7)
        self.play_beat(FadeIn(granted, shift=UP * 0.2))                   # beat 6

        # but it is a fact about ONE object, by ONE machine
        scope = VGroup(
            Text("but this is a fact about ONE object — the average,",
                 font_size=25, color=DIM),
            Text("built by ONE machine — the camera.",
                 font_size=25, color=DIM),
            Text("nothing yet said about any other machine.",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).next_to(granted, DOWN, buff=0.5)
        self.play_beat(FadeIn(scope, lag_ratio=0.25))                     # beat 7


# ----------------------------------------------------------------------
# Scene 4 — but the contrast is a different camera
# ----------------------------------------------------------------------
class S4_ButContrast(NarratedScene):
    scene_key = "S4_ButContrast"

    def construct(self):
        self.header("But the contrast is a different camera")

        head = Text("a second camera — the court does not average, it contrasts",
                    font_size=27, color=WHITE).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                      # beat 1

        # the contrast under a symptom-label null
        delta = MathTex(r"\Delta", "=", r"\bar m_{+}", "-", r"\bar m_{-}")\
            .scale(1.4).shift(UP * 1.0)
        delta[0].set_color(RES); delta[2].set_color(VAR); delta[4].set_color(VAR)
        null_cap = Text("shuffle only the symptom labels; hold C and every lesion fixed",
                        font_size=22, color=DIM).next_to(delta, DOWN, buff=0.35)
        self.play_beat(Write(delta), FadeIn(null_cap),
                       head.animate.set_opacity(0.4))                     # beat 2

        # split each map: x = b + r
        self.play(FadeOut(VGroup(head, null_cap)),
                  delta.animate.scale(0.7).to_edge(UP, buff=1.0), run_time=0.5)
        split = MathTex("x", "=", "b", "+", "r").scale(1.4).shift(UP * 1.1)
        split[0].set_color(VAR); split[2].set_color(BACK); split[4].set_color(VAR)
        b_lab = MathTex("b", "=", r"\lambda_1", r"\,(u_1^{\top}\ell)\,", "u_1")\
            .scale(1.0).next_to(split, DOWN, buff=0.4)
        b_lab[0].set_color(BACK); b_lab[2].set_color(EIG); b_lab[4].set_color(BACK)
        r_note = Text("r = everything left over", font_size=22, color=DIM)\
            .next_to(b_lab, DOWN, buff=0.3)
        self.play_beat(Write(split), Write(b_lab), FadeIn(r_note))        # beat 3

        # the load-bearing fact: b doesn't depend on the label
        self.play(FadeOut(VGroup(split, b_lab, r_note)), run_time=0.4)
        fact = VGroup(
            Text("the backbone piece b depends on WHERE the lesion sits in C,",
                 font_size=25, color=WHITE),
            Text("not on the symptom LABEL the patient carries.",
                 font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.9)
        self.play_beat(FadeIn(fact[0]), FadeIn(fact[1], shift=UP * 0.2))  # beat 4

        # so it cancels: hub subtracts away
        cancel = MathTex(r"\Delta", "=", r"(b - b)", "+", r"(r_{+} - r_{-})",
                         "=", r"r_{+} - r_{-}").scale(1.05)\
            .next_to(fact, DOWN, buff=0.55)
        cancel[0].set_color(RES); cancel[2].set_color(BACK); cancel[6].set_color(VAR)
        strike = Line(cancel[2].get_left(), cancel[2].get_right(),
                      color=BAD, stroke_width=5)
        self.play_beat(Write(cancel), Create(strike))                    # beat 5

        # one mechanism, opposite fates
        self.play(FadeOut(VGroup(fact, cancel, strike, delta)), run_time=0.5)
        flip = VGroup(
            Text("the backbone in every map made the camera nonspecific",
                 font_size=25, color=DIM),
            Text("the same backbone is inert in the court — it cancels",
                 font_size=25, color=BACK),
            Text("one mechanism, opposite fates", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.6)
        self.play_beat(FadeIn(flip, lag_ratio=0.25))                     # beat 6

        # the witness: 0 / 1000 at t > 10
        self.play(FadeOut(flip), run_time=0.4)
        witness = MathTex(r"t > 10:\quad", r"0\ \text{false positives}",
                          r"\ /\ 1000\ \text{iterations}").scale(1.05).shift(UP * 0.3)
        witness[1].set_color(RES)
        box = SurroundingRectangle(witness, color=RES, buff=0.25)
        self.play_beat(Write(witness), Create(box))                      # beat 7

        # closing moral: confound for one camera, inert for the other
        moral = Text("the backbone: the confound for one camera,\ninert for the other",
                     font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(box, DOWN, buff=0.55)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                    # beat 8


# ----------------------------------------------------------------------
# Scene 5 — bridge to sensitivity and specificity
# ----------------------------------------------------------------------
class S5_Bridge(NarratedScene):
    scene_key = "S5_Bridge"

    def construct(self):
        self.header("Bridge to sensitivity and specificity")

        intro = Text("two cameras, the same maps, opposite fates",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # the two-column verdict
        cam = VGroup(
            Text("CAMERA", font_size=26, color=DIM),
            MathTex(r"\bar m", color=VAR).scale(1.2),
            Text("backbone-dominated", font_size=22, color=BACK),
            Text("nonspecific", font_size=22, color=BAD),
        ).arrange(DOWN, buff=0.2)
        court = VGroup(
            Text("COURT", font_size=26, color=RES),
            MathTex(r"\Delta", color=RES).scale(1.2),
            Text("backbone subtracted away", font_size=22, color=BACK),
            Text("can carry signal", font_size=22, color=RES),
        ).arrange(DOWN, buff=0.2)
        cols = VGroup(cam, court).arrange(RIGHT, buff=2.6).shift(UP * 0.1)
        vs = MathTex(r"\neq", color=WHITE).scale(1.4).move_to(cols)
        self.play_beat(FadeIn(cam, lag_ratio=0.2), FadeIn(court, lag_ratio=0.2),
                       FadeIn(vs))                                        # beat 2

        # a failed null is a failed question
        self.play(FadeOut(VGroup(intro, cam, court, vs)), run_time=0.5)
        lesson = VGroup(
            Text("a failed null is often a FAILED QUESTION,",
                 font_size=28, color=RES),
            Text("not a failed method.", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.4)
        why = Text("convergence failed because the average asked the wrong thing",
                   font_size=23, color=DIM).next_to(lesson, DOWN, buff=0.4)
        self.play_beat(FadeIn(lesson, shift=UP * 0.2), FadeIn(why))       # beat 3

        # sensitivity question
        self.play(FadeOut(VGroup(lesson, why)), run_time=0.4)
        sens = VGroup(
            Text("SENSITIVITY", font_size=27, color=BACK),
            Text("does a real effect light the map up at all?",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.4)
        self.play_beat(FadeIn(sens, shift=UP * 0.2))                     # beat 4

        # specificity question
        spec = VGroup(
            Text("SPECIFICITY", font_size=27, color=RES),
            Text("does it light up MORE for this symptom",
                 font_size=25, color=WHITE),
            Text("than for a shuffled label?", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.18).next_to(sens, DOWN, buff=0.5)
        self.play_beat(FadeIn(spec, shift=UP * 0.2))                     # beat 5

        # what comes next: the backbone term must vanish
        self.play(FadeOut(VGroup(sens, spec)), run_time=0.4)
        nxt = MathTex(r"\text{next: watch}\quad",
                      r"\lambda_1 (\,\bar c_{1+} - \bar c_{1-}\,)",
                      r"\quad\text{vanish from } \Delta").scale(0.9).shift(UP * 0.6)
        nxt[1].set_color(BACK)
        cap = Text("build the symptom-label permutation explicitly",
                   font_size=23, color=DIM).next_to(nxt, DOWN, buff=0.4)
        self.play_beat(Write(nxt), FadeIn(cap))                          # beat 6

        # closing line
        self.play(FadeOut(VGroup(nxt, cap)), run_time=0.4)
        close = VGroup(
            Text("Two cameras, opposite fates.", font_size=30, color=WHITE),
            Text("The camera is conceded.", font_size=30, color=DIM),
            Text("The court is what comes next.", font_size=30, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(close, lag_ratio=0.3))                     # beat 7
