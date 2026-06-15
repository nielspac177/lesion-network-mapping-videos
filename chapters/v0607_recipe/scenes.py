"""v0607_recipe — "Conformal prediction: the recipe".

Five narrated scenes assembling the conformal workflow for a calibrated
AE-risk predictor: pick a nonconformity score, hold out calibration (or use
jackknife+/CV+), compute the quantile, form the set, then check coverage and
sharpness. Then: why the score choice controls efficiency not validity; the two
diagnostics; the three pitfalls; and the closing promise.

All equations/numbers/claims come from:
  volumes/vol6_conformal/chapters/07_recipe.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0607_recipe ./render.sh \
      chapters/v0607_recipe/scenes.py -q ql \
      S1_Recipe S2_ScoreChoice S3_Diagnostics S4_Pitfalls S5_Close
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the recipe: the whole workflow as one flow diagram
# ----------------------------------------------------------------------
class S1_Recipe(NarratedScene):
    scene_key = "S1_Recipe"

    def construct(self):
        title = Text("The recipe", font_size=42, color=WHITE).to_edge(UP, buff=0.4)
        self.play_beat(Write(title))                                       # beat 1

        # Build the five-step flow, one box per step, top to bottom.
        steps = [
            ("1  Score", "nonconformity score (APS)", VAR),
            ("2  Calibrate", "hold-out  or  jackknife+ / CV+", BACK),
            ("3  Quantile", "cut-off from calibration scores", EIG),
            ("4  Set", "labels at or below the quantile", VAR),
            ("5  Check", "coverage  and  sharpness", RES),
        ]
        boxes = VGroup(*[self._step_box(h, s, c) for h, s, c in steps])
        boxes.arrange(DOWN, buff=0.30).scale(0.78).next_to(title, DOWN, buff=0.4)

        arrows = VGroup(*[
            Arrow(boxes[i].get_bottom(), boxes[i + 1].get_top(),
                  buff=0.05, color=DIM, stroke_width=3, max_tip_length_to_length_ratio=0.18)
            for i in range(len(boxes) - 1)
        ])

        # beat 2 — step 1: the score
        self.play_beat(FadeIn(boxes[0], shift=UP * 0.2))                   # beat 2
        # beat 3 — step 2: calibration
        self.play_beat(GrowArrow(arrows[0]), FadeIn(boxes[1], shift=UP * 0.2))  # beat 3
        # beat 4 — step 3: quantile
        self.play_beat(GrowArrow(arrows[1]), FadeIn(boxes[2], shift=UP * 0.2))  # beat 4
        # beat 5 — step 4: form the set
        self.play_beat(GrowArrow(arrows[2]), FadeIn(boxes[3], shift=UP * 0.2))  # beat 5
        # beat 6 — step 5: check coverage + sharpness
        self.play_beat(GrowArrow(arrows[3]), FadeIn(boxes[4], shift=UP * 0.2))  # beat 6

        # beat 7 — the loop named, whole diagram pulses
        loop = Text("score → calibrate → quantile → set → check",
                    font_size=24, color=DIM).to_edge(DOWN, buff=0.35)
        self.play_beat(FadeIn(loop, shift=UP * 0.2),
                       boxes.animate.set_stroke(opacity=1.0))             # beat 7

    def _step_box(self, head, sub, color):
        box = RoundedRectangle(width=7.2, height=0.95, corner_radius=0.12,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.10)
        h = Text(head, font_size=24, color=color, weight=BOLD)
        s = Text(sub, font_size=20, color=WHITE)
        txt = VGroup(h, s).arrange(RIGHT, buff=0.45).move_to(box)
        return VGroup(box, txt)


# ----------------------------------------------------------------------
# Scene 2 — choosing the score: efficiency, not validity
# ----------------------------------------------------------------------
class S2_ScoreChoice(NarratedScene):
    scene_key = "S2_ScoreChoice"

    def construct(self):
        self.header("Choosing the score")

        head = Text("the score controls efficiency, not validity",
                    font_size=30, color=RES).shift(UP * 2.5)
        self.play_beat(FadeIn(head))                                      # beat 1

        # the guarantee is model-agnostic — decode every symbol on screen
        guar = MathTex(r"\Pr\big(", r"Y", r"\in", r"C(X)", r"\big)",
                       r"\ge", r"1-\alpha").scale(1.1).shift(UP * 1.2)
        guar[1].set_color(VAR); guar[3].set_color(VAR); guar[6].set_color(RES)
        b_y = Brace(guar[1], DOWN, color=VAR)
        l_y = Text("true label", font_size=20, color=VAR).next_to(b_y, DOWN, buff=0.12)
        b_c = Brace(guar[3], UP, color=VAR)
        l_c = Text("the prediction set", font_size=20, color=VAR).next_to(b_c, UP, buff=0.12)
        b_a = Brace(guar[6], DOWN, color=RES)
        l_a = Text("target coverage  (1 − miss rate α)", font_size=20, color=RES)\
            .next_to(b_a, DOWN, buff=0.12)
        gcap = Text("holds for ANY symmetric model", font_size=24, color=BACK)\
            .next_to(l_a, DOWN, buff=0.3)
        self.play_beat(Write(guar), GrowFromCenter(b_y), FadeIn(l_y),
                       GrowFromCenter(b_c), FadeIn(l_c),
                       GrowFromCenter(b_a), FadeIn(l_a),
                       FadeIn(gcap), lag_ratio=0.15)                       # beat 2

        # bad model -> vague, not wrong
        self.play(FadeOut(VGroup(head, guar, gcap,
                                 b_y, l_y, b_c, l_c, b_a, l_a)), run_time=0.4)
        vague = VGroup(
            Text("a bad model is not WRONG", font_size=28, color=WHITE),
            Text("it is only VAGUE", font_size=28, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.7)
        self.play_beat(FadeIn(vague[0]), FadeIn(vague[1], shift=UP * 0.2))  # beat 3

        # the full set: valid and worthless
        fullset = MathTex(r"C(X)", "=", r"\{\,\text{AE}^{+},\ \text{AE}^{-}\,\}")\
            .scale(1.1).next_to(vague, DOWN, buff=0.55)
        fullset[0].set_color(VAR); fullset[2].set_color(BAD)
        fcap = Text("valid  —  and completely worthless",
                    font_size=24, color=DIM).next_to(fullset, DOWN, buff=0.3)
        self.play_beat(Write(fullset), FadeIn(fcap))                      # beat 4

        # better model -> tighter sets, same coverage
        self.play(FadeOut(VGroup(vague, fullset, fcap)), run_time=0.4)
        trade = VGroup(
            Text("better model  →  tighter sets", font_size=28, color=BACK),
            Text("same coverage either way", font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.3)
        self.play_beat(FadeIn(trade[0], shift=UP * 0.2), FadeIn(trade[1]))  # beat 5

        # why validity is score-agnostic: rank, not model quality
        why = VGroup(
            Text("coverage rests on EXCHANGEABILITY of the scores", font_size=25, color=WHITE),
            Text("on rank order — not on the model being good", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.22).next_to(trade, DOWN, buff=0.6)
        self.play_beat(FadeIn(why, lag_ratio=0.3))                        # beat 6

        # the default choice
        self.play(FadeOut(VGroup(trade, why)), run_time=0.4)
        default = VGroup(
            Text("default:  L2-logistic  →  APS score", font_size=27, color=VAR),
            Text("stable at small N;  feeds a natural conformity input",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.6)
        self.play_beat(FadeIn(default, lag_ratio=0.3))                    # beat 7

        moral = Text("choosing well buys a smaller set — never a more honest one",
                     font_size=25, color=RES).next_to(default, DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 8


# ----------------------------------------------------------------------
# Scene 3 — diagnostics: coverage AND sharpness
# ----------------------------------------------------------------------
class S3_Diagnostics(NarratedScene):
    scene_key = "S3_Diagnostics"

    def construct(self):
        self.header("Diagnostics")

        head = Text("report TWO numbers — coverage alone is gameable",
                    font_size=28, color=RES).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                      # beat 1

        # metric 1: empirical coverage
        cov = MathTex(r"\widehat{\text{cov}}", "=",
                      r"\frac{\#\{\,Y_i \in C(X_i)\,\}}{N}")\
            .scale(1.1).shift(UP * 1.1)
        cov[0].set_color(BACK); cov[2].set_color(WHITE)
        cov_cap = Text("fraction of held-out patients whose truth landed in the set",
                       font_size=22, color=DIM).next_to(cov, DOWN, buff=0.3)
        self.play_beat(Write(cov), FadeIn(cov_cap))                       # beat 2

        # gaming coverage: predict everything
        self.play(FadeOut(VGroup(cov, cov_cap)), run_time=0.4)
        game = VGroup(
            Text("predict EVERYTHING  →  output the full set always",
                 font_size=26, color=BAD),
            MathTex(r"\widehat{\text{cov}} = 100\%", color=BAD).scale(1.0),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.0)
        self.play_beat(FadeIn(game[0]), Write(game[1]))                   # beat 3

        gap = Text("perfect coverage, zero information", font_size=26, color=DIM)\
            .next_to(game, DOWN, buff=0.4)
        necc = Text("coverage is NECESSARY, never SUFFICIENT",
                    font_size=26, color=RES).next_to(gap, DOWN, buff=0.3)
        self.play_beat(FadeIn(gap), FadeIn(necc, shift=UP * 0.2))         # beat 4

        # metric 2: sharpness
        self.play(FadeOut(VGroup(game, gap, necc)), run_time=0.4)
        sharp = VGroup(
            Text("sharpness", font_size=30, color=BACK),
            MathTex(r"\overline{|C(X)|}\ \text{(mean set size)}", color=WHITE).scale(0.95),
            Text("+  fraction of confident SINGLETONS  |C| = 1",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.28).shift(UP * 1.0)
        self.play_beat(FadeIn(sharp, lag_ratio=0.3))                      # beat 5

        useful = Text("useful  =  high coverage  AND  high sharpness",
                      font_size=26, color=RES).next_to(sharp, DOWN, buff=0.55)
        self.play_beat(FadeIn(useful, shift=UP * 0.2))                    # beat 6

        # the two-model comparison
        self.play(FadeOut(VGroup(sharp, useful)), run_time=0.4)
        modelA = self._model_card("Model A", "cov 90%", "size 1.7", "commits on 1/3", BACK)
        modelB = self._model_card("Model B", "cov 90%", "size 2.0", "full set, never commits", BAD)
        cards = VGroup(modelA, modelB).arrange(RIGHT, buff=0.9).shift(UP * 0.5)
        self.play_beat(FadeIn(modelA, shift=RIGHT * 0.2))                 # beat 7

        verdict = Text("same coverage — only Model A tells you anything",
                       font_size=25, color=RES).next_to(cards, DOWN, buff=0.6)
        self.play_beat(FadeIn(modelB, shift=LEFT * 0.2),
                       FadeIn(verdict, shift=UP * 0.2))                   # beat 8

    def _model_card(self, name, cov, size, note, color):
        box = RoundedRectangle(width=4.6, height=2.4, corner_radius=0.14,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.08)
        title = Text(name, font_size=26, color=color, weight=BOLD)
        l1 = Text(cov, font_size=22, color=WHITE)
        l2 = Text(size, font_size=22, color=WHITE)
        l3 = Text(note, font_size=20, color=DIM)
        body = VGroup(title, l1, l2, l3).arrange(DOWN, buff=0.20).move_to(box)
        return VGroup(box, body)


# ----------------------------------------------------------------------
# Scene 4 — pitfalls
# ----------------------------------------------------------------------
class S4_Pitfalls(NarratedScene):
    scene_key = "S4_Pitfalls"

    def construct(self):
        self.header("Pitfalls")

        head = Text("a recipe is copied without its caveats — here are three",
                    font_size=28, color=RES).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                      # beat 1

        # Pitfall 1: leakage — title + exchangeability requirement
        p1 = VGroup(
            Text("1.  LEAKAGE  (train ↔ calibration)", font_size=27, color=BAD),
            Text("coverage holds only if calibration & test scores are EXCHANGEABLE",
                 font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).shift(UP * 1.0)
        self.play_beat(FadeIn(p1, shift=UP * 0.2))                        # beat 2

        # what couples them: anything on all N
        coupling = Text("anything computed on all N couples test to calibration:\nscaler, PCA basis, feature-selection",
                        font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(p1, DOWN, buff=0.4)
        self.play_beat(FadeIn(coupling))                                  # beat 3

        # the loudest leak: through the label
        self.play(FadeOut(VGroup(p1, coupling)), run_time=0.4)
        label_leak = VGroup(
            Text("the loudest leak runs through the LABEL",
                 font_size=27, color=BAD),
            Text("feature from a template fit on the same patients",
                 font_size=23, color=WHITE),
            Text("→  a patient's own label leaks into its own feature",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.2)
        self.play_beat(FadeIn(label_leak, lag_ratio=0.3))                # beat 4

        consequence = VGroup(
            Text("the held-out patient was never really held out",
                 font_size=24, color=DIM),
            Text("coverage looks beautiful — and is OPTIMISTIC; inference goes circular",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.22).next_to(label_leak, DOWN, buff=0.55)
        self.play_beat(FadeIn(consequence, lag_ratio=0.3))               # beat 5

        # the fix: fold discipline
        fix = Text("FIX: refit scaler, template, everything INSIDE each fold\n(or use a separate cohort)",
                   font_size=24, color=BACK, line_spacing=0.8)\
            .next_to(consequence, DOWN, buff=0.5)
        self.play_beat(FadeIn(fix, shift=UP * 0.2))                      # beat 6

        # Pitfall 2: broken exchangeability
        self.play(FadeOut(VGroup(label_leak, consequence, fix)), run_time=0.4)
        p2 = VGroup(
            Text("2.  BROKEN EXCHANGEABILITY", font_size=27, color=BAD),
            Text("calibrate on site A, deploy on site B with sicker patients",
                 font_size=23, color=WHITE),
            Text("→  the promise can crack under the shift",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.2)
        self.play_beat(FadeIn(p2, lag_ratio=0.3))                        # beat 7

        # Pitfall 3: over-conditioning
        p3 = VGroup(
            Text("3.  CONDITIONING BEYOND THE DATA", font_size=27, color=BAD),
            MathTex(r"\Pr\big(Y\in C(X)\big)\ge 1-\alpha\quad\text{is MARGINAL}",
                    color=WHITE).scale(0.85),
            Text("averaged over patients — never a promise about THIS one",
                 font_size=23, color=RES),
        ).arrange(DOWN, buff=0.2).next_to(p2, DOWN, buff=0.55)
        self.play_beat(FadeIn(p3, lag_ratio=0.3))                        # beat 8


# ----------------------------------------------------------------------
# Scene 5 — closing
# ----------------------------------------------------------------------
class S5_Close(NarratedScene):
    scene_key = "S5_Close"

    def construct(self):
        self.header("Closing")

        head = MathTex(r"\text{any predictor}", r"\ \longrightarrow\ ",
                       r"\text{finite-sample coverage guarantee}")\
            .scale(0.95).shift(UP * 2.3)
        head[0].set_color(VAR); head[2].set_color(RES)
        self.play_beat(Write(head))                                       # beat 1

        # finite-sample meaning
        fin = VGroup(
            Text("finite-sample: holds at the N you HAVE", font_size=27, color=WHITE),
            Text("no asymptotics, no large-sample hand-waving", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.1)
        self.play_beat(FadeIn(fin[0]), FadeIn(fin[1], shift=UP * 0.2))    # beat 2

        # robust, model-free
        robust = Text("robust  &  model-free:  logistic, tree, anything symmetric",
                      font_size=25, color=BACK).next_to(fin, DOWN, buff=0.5)
        self.play_beat(FadeIn(robust, shift=UP * 0.2))                    # beat 3

        # the one assumption
        self.play(FadeOut(VGroup(fin, robust)), run_time=0.4)
        assume = VGroup(
            Text("honest about its ONE assumption:", font_size=27, color=WHITE),
            Text("EXCHANGEABILITY", font_size=34, color=RES, weight=BOLD),
            Text("the single price; the whole guarantee rests on it",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.9)
        self.play_beat(FadeIn(assume, lag_ratio=0.3))                    # beat 4

        # the right constant
        self.play(FadeOut(assume), run_time=0.4)
        const = VGroup(
            MathTex(r"\text{split} + \text{APS:}\quad", r"\text{exact } 1-\alpha")
            .scale(0.95),
            MathTex(r"\text{jackknife}^{+} / \text{CV}^{+}:\quad",
                    r"\ge 1-2\alpha").scale(0.95),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.2)
        const[0][1].set_color(RES); const[1][1].set_color(BACK)
        ccap = Text("quote the constant for the construction you actually ran",
                    font_size=22, color=DIM).next_to(const, DOWN, buff=0.4)
        self.play_beat(FadeIn(const, lag_ratio=0.3), FadeIn(ccap))        # beat 5

        # what it never claims
        self.play(FadeOut(VGroup(const, ccap)), run_time=0.4)
        never = VGroup(
            Text("it calibrates a FORECAST", font_size=27, color=WHITE),
            Text("answers: this patient's risk", font_size=24, color=VAR),
            Text("never: which connection CAUSES the harm", font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.9)
        self.play_beat(FadeIn(never, lag_ratio=0.3))                     # beat 6

        moral = VGroup(
            Text("causation-agnostic  &  marginal.", font_size=28, color=DIM),
            Text("One assumption, stated plainly.", font_size=30, color=WHITE),
            Text("A guarantee you can audit. That is the recipe.",
                 font_size=30, color=RES),
        ).arrange(DOWN, buff=0.3).next_to(never, DOWN, buff=0.55)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                     # beat 7
