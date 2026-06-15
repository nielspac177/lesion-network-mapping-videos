"""c0804_degree_baseline — "Move 3: beat a degree baseline".

Five narrated scenes building the credibility bar of the single-target recipe.
The critique's worry is that LNM maps recover the connectome's degree structure
(P1: basic connectome properties explain 93% of LNM-map variance, p.1244). So the
recipe makes degree the thing to beat: the degree-baseline model predicts outcome
from backbone overlap u_1^T l_i and lesion size s_i alone. If the residualized
full-fingerprint model out-predicts that baseline OUT OF SAMPLE, there is genuine
off-backbone, location-specific signal — exactly what the critique doubted.

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/06_single_target.md   (Move 3)
  responses/lnm_critique/sections/08_recipe.md           (C8 row)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0804_degree_baseline ./render.sh \
      chapters/c0804_degree_baseline/scenes.py -q ql \
      S1_Baseline S2_Why S3_OutOfSample S4_Verdict S5_Recipe
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the degree baseline model, every symbol decoded
# ----------------------------------------------------------------------
class S1_Baseline(NarratedScene):
    scene_key = "S1_Baseline"

    def construct(self):
        title = Text("The degree baseline model", font_size=40, color=WHITE)\
            .to_edge(UP, buff=0.4)
        sub = Text("the model your method has to beat",
                   font_size=24, color=DIM).next_to(title, DOWN, buff=0.2)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(FadeOut(sub), run_time=0.4)

        # the predictor.  Index each arg so we can color & brace it.
        eq = MathTex(
            r"\hat{y}_i^{\,\mathrm{deg}}",   # 0
            "=",                              # 1
            "a",                              # 2
            "+",                              # 3
            "b",                              # 4
            r"\,(u_1^{\top}\ell_i)",          # 5
            "+",                              # 6
            "c",                              # 7
            r"\,s_i",                         # 8
        ).scale(1.25).shift(UP * 1.4)
        eq[0].set_color(VAR)
        eq[2].set_color(EIG); eq[4].set_color(EIG); eq[7].set_color(EIG)
        eq[5].set_color(BACK)
        eq[8].set_color(RES)
        self.play_beat(Write(eq))                                          # beat 2

        # decode y-hat
        br_y = Brace(eq[0], DOWN, color=VAR)
        lab_y = Text("predicted outcome for patient i\n(tremor relief / adverse-effect score)",
                     font_size=22, color=VAR, line_spacing=0.8)\
            .next_to(br_y, DOWN, buff=0.2).shift(LEFT * 0.2)
        self.play_beat(GrowFromCenter(br_y), FadeIn(lab_y))                # beat 3

        # decode u_1^T l_i
        self.play(FadeOut(VGroup(br_y, lab_y)), run_time=0.4)
        br_u = Brace(eq[5], DOWN, color=BACK)
        lab_u = Text("seed's loading on the leading connectome\ncomponent — how much it sits on the hub backbone",
                     font_size=22, color=BACK, line_spacing=0.8)\
            .next_to(br_u, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(br_u), FadeIn(lab_u))                # beat 4

        # decode s_i
        self.play(FadeOut(VGroup(br_u, lab_u)), run_time=0.4)
        br_s = Brace(eq[8], DOWN, color=RES)
        lab_s = MathTex(r"s_i = \mathbf{1}^{\top}\ell_i",
                        r"\ \text{: lesion size (voxels destroyed)}")\
            .scale(0.8).next_to(br_s, DOWN, buff=0.2)
        lab_s[0].set_color(RES)
        self.play_beat(GrowFromCenter(br_s), FadeIn(lab_s))                # beat 5

        # decode a, b, c
        self.play(FadeOut(VGroup(br_s, lab_s)), run_time=0.4)
        br_abc = VGroup(Brace(eq[2], UP, color=EIG),
                        Brace(eq[4], UP, color=EIG),
                        Brace(eq[7], UP, color=EIG))
        lab_abc = Text("a, b, c  —  fitted weights:\nintercept, slope on hub-loading, slope on size",
                       font_size=22, color=EIG, line_spacing=0.8)\
            .next_to(eq, UP, buff=0.9)
        self.play_beat(FadeIn(br_abc, lag_ratio=0.2), FadeIn(lab_abc))     # beat 6

        # the moral: two cheap facts only
        self.play(FadeOut(VGroup(br_abc, lab_abc)), run_time=0.4)
        moral = VGroup(
            Text("Predicts outcome from two cheap facts only:",
                 font_size=26, color=WHITE),
            Text("how hub-connected the lesion is,  and  how big it is.",
                 font_size=26, color=BACK),
            Text("No within-target location detail at all.",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(eq, DOWN, buff=0.8)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 7


# ----------------------------------------------------------------------
# Scene 2 — why this baseline: it operationalizes the critique
# ----------------------------------------------------------------------
class S2_Why(NarratedScene):
    scene_key = "S2_Why"

    def construct(self):
        self.header("Why this baseline  (C8 · P1 p.1244)")

        intro = Text("the baseline is the critique, turned into a competitor",
                     font_size=28, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # the 93% fact as a bar
        bar = self._variance_bar(0.93).shift(UP * 0.5)
        self.play_beat(*[FadeIn(m) for m in bar.submobjects],
                       lag_ratio=0.1)                                      # beat 2

        # if 93% is degree+size, degree+size should predict
        impl = VGroup(
            Text("If ninety-three percent of the map is degree-and-size structure",
                 font_size=24, color=WHITE),
            Text("then degree-and-size alone should already predict outcome well.",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.2).next_to(bar, DOWN, buff=0.6)
        self.play_beat(FadeIn(impl, lag_ratio=0.3))                       # beat 3

        # the bar to clear
        self.play(FadeOut(VGroup(intro, bar, impl)), run_time=0.5)
        bar2 = VGroup(
            Text("So any honest method must beat a model using", font_size=26, color=WHITE),
            Text("ONLY  backbone overlap  +  lesion size.", font_size=28, color=RES),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.3)
        self.play_beat(FadeIn(bar2[0]), FadeIn(bar2[1], shift=UP * 0.2))   # beat 4

        # backbone is IN the baseline
        inside = VGroup(
            Text("The backbone is INSIDE the baseline.", font_size=26, color=BACK),
            Text("No result can be waved away as \"just degree\" —", font_size=24, color=DIM),
            Text("degree is the thing being out-competed.", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.18).next_to(bar2, DOWN, buff=0.55)
        self.play_beat(FadeIn(inside, lag_ratio=0.25))                    # beat 5

        # the rebuttal uses the same standard
        self.play(FadeOut(VGroup(bar2, inside)), run_time=0.5)
        reb = Text("The rebuttal uses the same standard (REBUTTAL p.3):",
                   font_size=25, color=RES).shift(UP * 1.6)
        nums = MathTex(r"r_{\text{same-symptom}} = 0.44",
                       r"\quad\text{vs}\quad",
                       r"r_{\text{to degree}} = 0.16").scale(1.0)
        nums[0].set_color(BACK); nums[2].set_color(BAD)
        nums.next_to(reb, DOWN, buff=0.45)
        self.play_beat(FadeIn(reb), Write(nums))                          # beat 6

        agree = VGroup(
            Text("Both sides agree on the bar:", font_size=26, color=WHITE),
            Text("make degree the thing to clear,", font_size=26, color=RES),
            Text("then ask whether the fingerprint clears it.", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.18).next_to(nums, DOWN, buff=0.6)
        self.play_beat(FadeIn(agree, lag_ratio=0.25))                     # beat 7

    def _variance_bar(self, frac):
        w = 8.0
        full = Rectangle(width=w, height=0.55, stroke_color=WHITE, stroke_width=2,
                         fill_opacity=0)
        filled = Rectangle(width=w * frac, height=0.55, stroke_width=0,
                           fill_color=BAD, fill_opacity=0.85)
        filled.align_to(full, LEFT)
        bar = VGroup(full, filled)
        lab = MathTex(r"93\%", color=BAD).scale(1.0).next_to(full, UP, buff=0.2)
        cap = Text("of LNM-map variance explained by basic connectome properties",
                   font_size=21, color=DIM).next_to(full, DOWN, buff=0.2)
        return VGroup(bar, lab, cap).move_to(ORIGIN)


# ----------------------------------------------------------------------
# Scene 3 — out-of-sample test: train / predict held-out
# ----------------------------------------------------------------------
class S3_OutOfSample(NarratedScene):
    scene_key = "S3_OutOfSample"

    def construct(self):
        self.header("Out-of-sample test  (C8 · 06 Move 3)")

        intro = Text("the comparison must be made OUT of sample",
                     font_size=28, color=RES).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # within vs out-of-sample
        contrast = VGroup(
            Text("A within-sample p-value can be argued away", font_size=25, color=DIM),
            Text("as overfitting, or as backbone.", font_size=25, color=DIM),
            Text("Out-of-sample prediction cannot.", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.18).next_to(intro, DOWN, buff=0.5)
        self.play_beat(FadeIn(contrast, lag_ratio=0.25))                 # beat 2

        # split into train / test
        self.play(FadeOut(VGroup(intro, contrast)), run_time=0.5)
        train = self._cohort_box("TRAIN", BACK).shift(LEFT * 3.2 + UP * 1.2)
        test = self._cohort_box("TEST  (held out)", VAR).shift(RIGHT * 3.2 + UP * 1.2)
        split_cap = Text("split the patients; the test set is never seen while learning",
                         font_size=22, color=DIM).next_to(VGroup(train, test), DOWN, buff=0.5)
        self.play_beat(FadeIn(train, shift=RIGHT * 0.2),
                       FadeIn(test, shift=LEFT * 0.2),
                       FadeIn(split_cap))                                 # beat 3

        # learn on train
        learn = Text("On TRAIN: learn how graded outcome relates to the\nlesion — fingerprint, size, position.",
                     font_size=24, color=BACK, line_spacing=0.8)\
            .next_to(split_cap, DOWN, buff=0.5)
        arr1 = Arrow(train.get_bottom(), learn.get_top() + LEFT * 1.5,
                     color=BACK, buff=0.15, stroke_width=3)
        self.play_beat(GrowArrow(arr1), FadeIn(learn))                   # beat 4

        # predict on test, score by OOS R^2
        self.play(FadeOut(VGroup(arr1, learn)), run_time=0.4)
        score = MathTex(r"\text{predict held-out }", r"y_i",
                        r"\ \Rightarrow\ \text{gain in out-of-sample } R^2")\
            .scale(0.95)
        score[1].set_color(VAR)
        score.next_to(split_cap, DOWN, buff=0.55)
        arr2 = Arrow(test.get_bottom(), score.get_top() + RIGHT * 1.2,
                     color=VAR, buff=0.15, stroke_width=3)
        self.play_beat(GrowArrow(arr2), Write(score))                    # beat 5

        # the requirement
        req = VGroup(
            Text("The full residualized-fingerprint model must beat", font_size=24, color=WHITE),
            Text("the degree baseline on the UNSEEN patients —", font_size=24, color=RES),
            Text("not merely fit the training data better.", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.16).next_to(score, DOWN, buff=0.5)
        self.play_beat(FadeIn(req, lag_ratio=0.25))                      # beat 6

        # keep features low-dimensional
        self.play(FadeOut(VGroup(train, test, split_cap, arr2, score, req)),
                  run_time=0.5)
        lowd = VGroup(
            Text("Keep the features low-dimensional:", font_size=26, color=WHITE),
            Text("size, within-target position, a few fingerprint scalars.", font_size=24, color=VAR),
            Text("Tens of thousands of voxels with N in the tens = guaranteed overfit.",
                 font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.22)
        self.play_beat(FadeIn(lowd, lag_ratio=0.25))                     # beat 7

    def _cohort_box(self, label, color):
        box = RoundedRectangle(width=3.4, height=1.0, corner_radius=0.14,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=24, color=color).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 4 — what beating it would mean (the verdict)
# ----------------------------------------------------------------------
class S4_Verdict(NarratedScene):
    scene_key = "S4_Verdict"

    def construct(self):
        self.header("What beating it would mean  (06 Move 3 · C8)")

        suppose = Text("Suppose the full model WINS, out of sample.",
                       font_size=30, color=RES).shift(UP * 2.4)
        self.play_beat(FadeIn(suppose, shift=UP * 0.2))                  # beat 1

        # not backbone
        not_bb = VGroup(
            Text("It cannot be the backbone —", font_size=26, color=WHITE),
            MathTex(r"u_1^{\top}\ell_i", r"\ \text{is already in the baseline it beat.}")
            .scale(0.85),
        ).arrange(DOWN, buff=0.2).next_to(suppose, DOWN, buff=0.6)
        not_bb[1][0].set_color(BACK)
        self.play_beat(FadeIn(not_bb, lag_ratio=0.3))                    # beat 2

        # not dose
        not_dose = VGroup(
            Text("It cannot be a pure size dose-response —", font_size=26, color=WHITE),
            MathTex(r"s_i", r"\ \text{is already in the baseline too.}").scale(0.85),
        ).arrange(DOWN, buff=0.2).next_to(not_bb, DOWN, buff=0.5)
        not_dose[1][0].set_color(RES)
        self.play_beat(FadeIn(not_dose, lag_ratio=0.3))                  # beat 3

        # therefore: signal beyond degree and dose
        self.play(FadeOut(VGroup(suppose, not_bb, not_dose)), run_time=0.5)
        gain = MathTex(r"\text{prediction gain}", r"\ \Rightarrow\ ",
                       r"\text{info beyond degree \& dose}").scale(1.0)\
            .shift(UP * 1.5)
        gain[0].set_color(VAR); gain[2].set_color(RES)
        box = SurroundingRectangle(gain, color=RES, buff=0.2)
        self.play_beat(Write(gain), Create(box))                         # beat 4

        # off-backbone, location-specific signal
        signal = VGroup(
            Text("Genuine off-backbone, location-specific signal —", font_size=26, color=BACK),
            Text("exactly the thing the critique doubted could exist.", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.22).next_to(box, DOWN, buff=0.55)
        self.play_beat(FadeIn(signal, lag_ratio=0.3))                    # beat 5

        # on the critique's own terms
        terms = Text("demonstrated on the critique's own terms,\nagainst a degree baseline it would have endorsed",
                     font_size=25, color=DIM, line_spacing=0.8)\
            .next_to(signal, DOWN, buff=0.5)
        self.play_beat(FadeIn(terms, shift=UP * 0.2))                    # beat 6

        # the existence proof
        self.play(FadeOut(VGroup(gain, box, signal, terms)), run_time=0.5)
        proof = VGroup(
            Text("The rebuttal shows it is achievable (REBUTTAL p.3):",
                 font_size=25, color=WHITE),
            MathTex(r"t > 10:\quad", r"0\ \text{false positives}",
                    r"\ /\ 1000\ \text{iterations}").scale(1.0),
        ).arrange(DOWN, buff=0.4)
        proof[1][1].set_color(RES)
        self.play_beat(FadeIn(proof[0]), Write(proof[1]))                # beat 7


# ----------------------------------------------------------------------
# Scene 5 — the three moves together (recap)
# ----------------------------------------------------------------------
class S5_Recipe(NarratedScene):
    scene_key = "S5_Recipe"

    def construct(self):
        self.header("The three moves together  (06 · 08 recipe)")

        intro = Text("the single-target recipe, in three moves",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                    # beat 1

        # move 1
        m1 = self._move_row("1", "Permute outcomes, size-protected",
                            "neither backbone nor size can fake a result", BACK)
        m1.shift(UP * 1.3)
        self.play_beat(FadeIn(m1, shift=UP * 0.2))                       # beat 2

        # move 2
        m2 = self._move_row("2", "Strip the backbone first",
                            "project off the leading components; lift the small signal", VAR)
        m2.next_to(m1, DOWN, buff=0.4)
        self.play_beat(FadeIn(m2, shift=UP * 0.2))                       # beat 3

        # move 3 (today's)
        m3 = self._move_row("3", "Beat a degree baseline out-of-sample",
                            "the win is signal that is neither backbone nor dose", RES)
        m3.next_to(m2, DOWN, buff=0.4)
        self.play_beat(FadeIn(m3, shift=UP * 0.2))                       # beat 4

        # roles: calibration / power / certification
        self.play(FadeOut(VGroup(intro, m1, m2, m3)), run_time=0.5)
        roles = VGroup(
            Text("Move 1 fixes calibration — the null cannot lie.", font_size=25, color=BACK),
            Text("Move 2 improves power.", font_size=25, color=VAR),
            Text("Move 3 certifies the whole thing on held-out patients.", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).shift(UP * 0.6)
        self.play_beat(FadeIn(roles, lag_ratio=0.25))                    # beat 5

        # answers rather than dodges
        answer = Text("A recipe that ANSWERS the critique rather than dodging it —\non the critique's own chosen battleground.",
                      font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(roles, DOWN, buff=0.55)
        self.play_beat(FadeIn(answer, shift=UP * 0.2))                   # beat 6

        # the one-line moral
        self.play(FadeOut(VGroup(roles, answer)), run_time=0.5)
        moral = VGroup(
            Text("Make the backbone cancel,  subtract it,  out-predict it.",
                 font_size=28, color=RES),
            Text("Pass all three, and \"LNM is hopeless\" does not follow.",
                 font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                     # beat 7

    def _move_row(self, num, head, why, color):
        chip = VGroup(
            Circle(radius=0.32, stroke_color=color, stroke_width=2.5,
                   fill_color=color, fill_opacity=0.15),
            Text(num, font_size=26, color=color),
        )
        txt = VGroup(
            Text(head, font_size=26, color=color),
            Text(why, font_size=21, color=DIM),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        txt.next_to(chip, RIGHT, buff=0.4)
        return VGroup(chip, txt)
