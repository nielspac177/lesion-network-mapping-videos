"""c1002_camera_vs_court_settled — "Camera vs court, settled".

The closing chapter. One connectome C, two operations: the average (camera) and
the contrast (court). Same data, opposite fates. Concede the camera cleanly,
keep the court standing, state the unifying slogan ("a failed null is a failed
question"), and lay out the synthesis: average = nonspecific (critique right),
contrast can carry signal (rebuttal right), model class is limited (P3 right).

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/08_recipe.md
  responses/lnm_critique/sections/00_abstract_intro.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c1002_camera_vs_court_settled ./render.sh \
      chapters/c1002_camera_vs_court_settled/scenes.py -q ql \
      S1_OneMatrix S2_Camera S3_Court S4_Slogan S5_Settled
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — one matrix, two operations
# ----------------------------------------------------------------------
class S1_OneMatrix(NarratedScene):
    scene_key = "S1_OneMatrix"

    def construct(self):
        self.header("One matrix, two operations")

        # the one matrix C
        cmat = MathTex("C").scale(2.2).set_color(WHITE).shift(UP * 1.7)
        c_lab = Text("the one normative connectome", font_size=24, color=DIM)\
            .next_to(cmat, DOWN, buff=0.25)
        self.play_beat(Write(cmat), FadeIn(c_lab))                          # beat 1

        # operation one: the camera = the average
        self.play(FadeOut(c_lab),
                  cmat.animate.scale(0.55).to_edge(UP, buff=1.0),
                  run_time=0.5)
        avg = MathTex(r"\text{average}", r"\;=\;",
                      r"\tfrac{1}{n}\textstyle\sum_{s}\, m_s").scale(1.0)
        avg[0].set_color(DIM); avg[2].set_color(DIM)
        camera = Text("the CAMERA", font_size=28, color=DIM)
        cam_grp = VGroup(avg, camera).arrange(DOWN, buff=0.3).shift(UP * 0.4)
        self.play_beat(Write(avg), FadeIn(camera, shift=UP * 0.2))          # beat 2

        # operation two: the court = the contrast
        court_eq = MathTex(r"\text{contrast}", r"\;=\;",
                           r"\bar m_{\text{sym}} - \bar m_{\text{asym}}").scale(1.0)
        court_eq[0].set_color(RES); court_eq[2].set_color(RES)
        court = Text("the COURT", font_size=28, color=RES)
        court_grp = VGroup(court_eq, court).arrange(DOWN, buff=0.3)\
            .next_to(cam_grp, DOWN, buff=0.7)
        self.play_beat(Write(court_eq), FadeIn(court, shift=UP * 0.2))      # beat 3

        # same data feeds both
        same = Text("same C  ·  same lesions  ·  same data",
                    font_size=26, color=VAR).to_edge(DOWN, buff=0.9)
        only = Text("only the OPERATION differs", font_size=22, color=WHITE)\
            .next_to(same, DOWN, buff=0.2)
        self.play_beat(FadeIn(same), FadeIn(only, shift=UP * 0.2))          # beat 4

        # opposite fates
        self.play(FadeOut(VGroup(same, only)), run_time=0.4)
        broken = Text("✗ broken", font_size=26, color=BAD)\
            .next_to(camera, RIGHT, buff=0.8)
        stands = Text("✓ stands", font_size=26, color=BACK)\
            .next_to(court, RIGHT, buff=0.8)
        self.play_beat(FadeIn(broken, shift=LEFT * 0.2),
                       FadeIn(stands, shift=LEFT * 0.2))                    # beat 5

        # the verdict is a separation, not a winner
        self.play(FadeOut(VGroup(cmat, avg, camera, court_eq, court,
                                 broken, stands)), run_time=0.5)
        verdict = VGroup(
            Text("Not a winner.", font_size=32, color=WHITE),
            Text("A description that fails,", font_size=28, color=DIM),
            Text("and an inference that survives.", font_size=28, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(verdict, lag_ratio=0.3))                     # beat 6


# ----------------------------------------------------------------------
# Scene 2 — the camera is broken
# ----------------------------------------------------------------------
class S2_Camera(NarratedScene):
    scene_key = "S2_Camera"

    def construct(self):
        self.header("The camera is broken")

        intro = Text("conceded cleanly — the math is the critique's, and it is right",
                     font_size=26, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # LNM = sum(M x C)
        eq = MathTex(r"\mathrm{LNM}", "=", r"\textstyle\sum_{s}", "M",
                     r"\times", "C").scale(1.3).shift(UP * 1.0)
        eq[0].set_color(DIM); eq[3].set_color(VAR); eq[5].set_color(WHITE)
        brace_M = Brace(eq[3], DOWN, color=VAR)
        m_lab = Text("M selects and averages rows of C",
                     font_size=22, color=VAR).next_to(brace_M, DOWN, buff=0.2)
        self.play_beat(Write(eq), GrowFromCenter(brace_M), FadeIn(m_lab))  # beat 2

        # M -> I  =>  converges to degree  (ONLY under uniform non-overlapping sampling)
        self.play(FadeOut(VGroup(brace_M, m_lab, intro)), run_time=0.4)
        conv = MathTex("M", r"\to", "I", r"\ \Longrightarrow\ ",
                       r"\deg(C)").scale(1.15).next_to(eq, DOWN, buff=0.7)
        conv[0].set_color(VAR); conv[2].set_color(EIG); conv[4].set_color(BAD)
        i_brace = Brace(conv[2], UP, color=EIG)
        i_lab = Text("I = identity: uniform, non-overlapping coverage",
                     font_size=20, color=EIG).next_to(i_brace, UP, buff=0.15)
        conv_cap = Text("only under that sampling, the average becomes the row-sum of C: the hub map",
                        font_size=22, color=DIM).next_to(conv, DOWN, buff=0.3)
        self.play_beat(Write(conv), GrowFromCenter(i_brace),
                       FadeIn(i_lab), FadeIn(conv_cap))                    # beat 3

        # 93% of variance
        self.play(FadeOut(VGroup(eq, conv, conv_cap, i_brace, i_lab)),
                  run_time=0.5)
        bar = self._variance_bar(0.93).shift(UP * 0.6)
        self.play_beat(*[FadeIn(m) for m in bar.submobjects], lag_ratio=0.1)  # beat 4

        # nonspecific by construction
        cone = VGroup(
            Text("real lesions", font_size=22, color=VAR),
            Text("synthetic blobs", font_size=22, color=DIM),
            Text("random seeds", font_size=22, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(LEFT * 3.4 + DOWN * 1.4)
        arrow = Arrow(LEFT * 1.0 + DOWN * 1.4, RIGHT * 0.8 + DOWN * 1.4,
                      color=DIM, buff=0.1)
        hub = Text("the same hub-shaped cone", font_size=24, color=BAD)\
            .shift(RIGHT * 3.0 + DOWN * 1.4)
        self.play_beat(FadeIn(cone, lag_ratio=0.2), GrowArrow(arrow),
                       FadeIn(hub))                                        # beat 5

        # grant it in full
        self.play(FadeOut(VGroup(bar, cone, arrow, hub)), run_time=0.5)
        grant = VGroup(
            Text("The critique's central claim — granted in full.",
                 font_size=28, color=WHITE),
            Text("The camera is broken.", font_size=32, color=BAD),
            Text("Nothing to defend here.", font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(grant, lag_ratio=0.3))                      # beat 6

    def _variance_bar(self, frac):
        w = 8.0
        full = Rectangle(width=w, height=0.55, stroke_color=WHITE,
                         stroke_width=2, fill_opacity=0)
        filled = Rectangle(width=w * frac, height=0.55, stroke_width=0,
                           fill_color=BAD, fill_opacity=0.85)
        filled.align_to(full, LEFT)
        bar = VGroup(full, filled)
        lab = MathTex(r"93\%", color=BAD).scale(1.0).next_to(full, UP, buff=0.2)
        cap = Text("of LNM-map variance from basic connectome properties",
                   font_size=21, color=DIM).next_to(full, DOWN, buff=0.2)
        return VGroup(bar, lab, cap).move_to(ORIGIN)


# ----------------------------------------------------------------------
# Scene 3 — the court still stands
# ----------------------------------------------------------------------
class S3_Court(NarratedScene):
    scene_key = "S3_Court"

    def construct(self):
        self.header("The court still stands")

        # signal lives in the contrast, after backbone removal
        idea = VGroup(
            Text("the signal was never in the average", font_size=26, color=DIM),
            Text("it lives in the DIFFERENCE, after the backbone is removed",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.7)
        self.play_beat(FadeIn(idea[0]), FadeIn(idea[1], shift=UP * 0.2))   # beat 1

        # shuffle labels, not lesions
        self.play(idea.animate.scale(0.85).to_edge(UP, buff=1.1), run_time=0.5)
        null = VGroup(
            Text("shuffle the CLINICAL LABELS — not the lesions",
                 font_size=26, color=WHITE),
            Text("C and the lesion geometry stay fixed; only the label link breaks",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.2)
        self.play_beat(FadeIn(null, lag_ratio=0.3))                       # beat 2

        # the backbone is label-independent
        self.play(FadeOut(VGroup(idea, null)), run_time=0.5)
        indep = MathTex(r"\text{backbone}", r"\;=\;", r"f(C)",
                        r"\;\perp\;", r"\text{symptom label}").scale(1.0)
        indep[0].set_color(BACK); indep[2].set_color(WHITE); indep[4].set_color(EIG)
        indep.shift(UP * 1.6)
        indep_cap = Text("C never saw the symptom: the backbone is label-independent",
                         font_size=23, color=DIM).next_to(indep, DOWN, buff=0.3)
        self.play_beat(Write(indep), FadeIn(indep_cap))                   # beat 3

        # it cancels in the contrast
        cancel = MathTex(r"(\,b + \text{signal}\,)", "-", r"(\,b + 0\,)",
                         "=", r"\text{signal}").scale(1.05)\
            .next_to(indep_cap, DOWN, buff=0.6)
        cancel[0].set_color(WHITE); cancel[2].set_color(WHITE)
        cancel[4].set_color(RES)
        b_brace = Brace(VGroup(cancel[0], cancel[2]), DOWN, color=BACK)
        b_lab = Text("the backbone b is identical in real and shuffled — it cancels",
                     font_size=22, color=BACK).next_to(b_brace, DOWN, buff=0.2)
        self.play_beat(Write(cancel), GrowFromCenter(b_brace),
                       FadeIn(b_lab))                                      # beat 4

        # exact, distribution-free
        self.play(FadeOut(VGroup(indep, indep_cap, cancel, b_brace, b_lab)),
                  run_time=0.5)
        props = VGroup(
            Text("exact under exchangeability  (permutation-exactness theorem)",
                 font_size=25, color=WHITE),
            Text("distribution-free  —  no model of the data assumed",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.4)
        self.play_beat(FadeIn(props, lag_ratio=0.3))                      # beat 5

        # the data: r=0.44 / 0.09 / 0.16
        data = VGroup(
            Text("same-symptom", font_size=22, color=DIM),
            MathTex("r = 0.44", color=BACK).scale(1.0),
            Text("different-symptom", font_size=22, color=DIM),
            MathTex("r = 0.09", color=DIM).scale(1.0),
            Text("degree map", font_size=22, color=DIM),
            MathTex("r = 0.16", color=BAD).scale(1.0),
        ).arrange_in_grid(rows=3, cols=2, buff=(0.5, 0.22)).shift(DOWN * 0.8)
        self.play_beat(FadeIn(data, lag_ratio=0.1))                       # beat 6

        # the witness: 0 FP / 1000 at t>10
        self.play(FadeOut(VGroup(props, data)), run_time=0.5)
        witness = MathTex(r"t > 10:\quad", r"0\ \text{false positives}",
                          r"\ /\ 1000\ \text{iterations}").scale(1.05)
        witness[1].set_color(RES)
        stands = Text("The court still stands.", font_size=32, color=BACK)\
            .next_to(witness, DOWN, buff=0.6)
        self.play_beat(Write(witness), FadeIn(stands, shift=UP * 0.2))     # beat 7


# ----------------------------------------------------------------------
# Scene 4 — a failed null is a failed question
# ----------------------------------------------------------------------
class S4_Slogan(NarratedScene):
    scene_key = "S4_Slogan"

    def construct(self):
        self.header("A failed null is a failed question")

        slogan = Text("a null that finds nothing\nmay just be the wrong question",
                      font_size=34, color=RES, line_spacing=0.8)
        self.play_beat(Write(slogan))                                     # beat 1

        # the location null asks the wrong thing
        self.play(slogan.animate.scale(0.55).to_edge(UP, buff=1.0), run_time=0.5)
        loc = VGroup(
            Text("LOCATION null:", font_size=26, color=BAD),
            Text("is THIS location special?", font_size=26, color=WHITE),
            Text("but every location gives the same backbone", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.9)
        self.play_beat(FadeIn(loc, lag_ratio=0.25))                       # beat 2

        # not LNM failing — a mis-aimed question
        misfire = Text("not LNM failing — a mis-aimed question,\na confident but empty answer",
                       font_size=26, color=BAD, line_spacing=0.8)\
            .next_to(loc, DOWN, buff=0.5)
        self.play_beat(FadeIn(misfire, shift=UP * 0.2))                   # beat 3

        # swap the question: the label null
        self.play(FadeOut(VGroup(loc, misfire)), run_time=0.5)
        lab = VGroup(
            Text("LABEL null:", font_size=26, color=BACK),
            Text("does the symptom track the map at all?", font_size=26, color=WHITE),
            Text("this question has an exact, backbone-immune answer",
                 font_size=22, color=BACK),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.5)
        self.play_beat(FadeIn(lab, lag_ratio=0.25))                       # beat 4

        # the critique broke a question, not the possibility
        self.play(FadeOut(VGroup(slogan, lab)), run_time=0.5)
        moral = VGroup(
            Text("A failed null is a failed question —", font_size=30, color=WHITE),
            Text("not a closed door.", font_size=30, color=WHITE),
            Text("The critique broke a QUESTION, not the\npossibility of inference.",
                 font_size=28, color=RES, line_spacing=0.8),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                      # beat 5

        # read every dead result this way
        check = Text("Read every dead result this way: did the null\neven point at the signal you were hunting?",
                     font_size=26, color=DIM, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(check, shift=UP * 0.2))                     # beat 6


# ----------------------------------------------------------------------
# Scene 5 — what is settled
# ----------------------------------------------------------------------
class S5_Settled(NarratedScene):
    scene_key = "S5_Settled"

    def construct(self):
        self.header("What is settled")

        head = VGroup(
            Text("Not a winner.", font_size=32, color=WHITE),
            Text("Three claims, each true in its own scope.", font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 2.2)
        self.play_beat(FadeIn(head, lag_ratio=0.3))                       # beat 1

        # settled 1: average = nonspecific (critique right)
        s1 = VGroup(
            Text("1.  the AVERAGE is nonspecific", font_size=27, color=BAD),
            Text("critique (van den Heuvel et al.) — right about what it measured",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 0.9)
        self.play_beat(FadeIn(s1, shift=UP * 0.2))                        # beat 2

        # settled 2: contrast can carry signal (rebuttal right)
        s2 = VGroup(
            Text("2.  the CONTRAST can carry signal", font_size=27, color=BACK),
            Text("rebuttal — right: specificity survives a label-permuting test",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(s1, DOWN, buff=0.4)
        self.play_beat(FadeIn(s2, shift=UP * 0.2))                        # beat 3

        # settled 3: model class is limited (P3 right)
        s3 = VGroup(
            Text("3.  the MODEL CLASS is limited", font_size=27, color=EIG),
            Text("P3 — right: a static C is blind to dynamic, higher-order reorganization",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(s2, DOWN, buff=0.4)
        self.play_beat(FadeIn(s3, shift=UP * 0.2))                        # beat 4

        # they do not cancel — different axes
        self.play(FadeOut(VGroup(head, s1, s2, s3)), run_time=0.5)
        axes = VGroup(
            Text("a DESCRIPTION  ·  an INFERENCE  ·  a MODEL",
                 font_size=26, color=WHITE),
            Text("different axes — all three standing", font_size=24, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.8)
        self.play_beat(FadeIn(axes[0]), FadeIn(axes[1], shift=UP * 0.2))   # beat 5

        # the closing line
        close = VGroup(
            Text("Settled as a SYNTHESIS, not a verdict.", font_size=30, color=WHITE),
            Text("One matrix, two operations, three truths.", font_size=28, color=RES),
        ).arrange(DOWN, buff=0.3).next_to(axes, DOWN, buff=0.7)
        self.play_beat(FadeIn(close, lag_ratio=0.3))                      # beat 6
