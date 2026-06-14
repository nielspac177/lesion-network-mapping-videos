"""c0401_diagnostic_vocabulary — "Sensitivity, specificity, and what a null is".

Five narrated scenes that build the diagnostic-test vocabulary the rest of the
LNM argument needs: the 2x2 confusion matrix; sensitivity = TP/(TP+FN);
specificity = TN/(TN+FP); the ROC sensitivity-vs-specificity trade-off; and the
thesis that a null hypothesis is a QUESTION, so "found nothing" can mean the
answer is no OR the question was wrong.

All claims/numbers are from:
  responses/lnm_critique/sections/03_the_right_null.md
("A null model is a question."; the location null vs the symptom-label null;
 zero false positives in 1000 iterations at t > 10, leakage 4.6% only at t = 3.0.)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0401_diagnostic_vocabulary ./render.sh \
      chapters/c0401_diagnostic_vocabulary/scenes.py -q ql \
      S1_Confusion S2_Sensitivity S3_Specificity S4_ROC S5_NullIsQuestion
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Shared helper: build the 2x2 confusion matrix with row / column headers.
# Returns a VGroup (.submobjects = grid, labels, the two col headers, the two
# row headers) so the caller can .shift(...) it; cell rects / headers are also
# exposed as attributes (grp.cell, grp.grid, ...) for later highlighting.
# ----------------------------------------------------------------------
def build_confusion(cell_texts, cell_colors):
    """cell_texts/cell_colors: dict keyed 'TP','FP','FN','TN'.
    Layout (rows = truth, cols = test):
                  reject        keep
      signal       TP           FN
      no signal    FP           TN
    Returns a VGroup; cell rectangles accessible via grp.cell['TP'] etc.
    """
    cw, ch = 2.7, 1.35
    positions = {
        "TP": (LEFT * cw / 2,  UP * ch / 2),
        "FN": (RIGHT * cw / 2, UP * ch / 2),
        "FP": (LEFT * cw / 2,  DOWN * ch / 2),
        "TN": (RIGHT * cw / 2, DOWN * ch / 2),
    }
    cell = {}
    labels = {}
    for k, (dx, dy) in positions.items():
        rect = Rectangle(width=cw, height=ch, stroke_color=DIM, stroke_width=2,
                         fill_color=cell_colors[k], fill_opacity=0.10)
        rect.move_to(dx + dy)
        lab = Text(cell_texts[k], font_size=20, color=cell_colors[k],
                   line_spacing=0.8).move_to(rect)
        cell[k] = rect
        labels[k] = lab
    grid = VGroup(*cell.values())
    lab_grp = VGroup(*labels.values())

    # column headers (the TEST verdict)
    col_reject = Text("test: REJECT", font_size=22, color=VAR)\
        .next_to(cell["TP"], UP, buff=0.25)
    col_keep = Text("test: KEEP", font_size=22, color=VAR)\
        .next_to(cell["FN"], UP, buff=0.25)
    # row headers (the TRUTH)
    row_sig = Text("truth:\nsignal", font_size=22, color=BACK, line_spacing=0.8)\
        .next_to(cell["TP"], LEFT, buff=0.3)
    row_no = Text("truth:\nno signal", font_size=22, color=BACK, line_spacing=0.8)\
        .next_to(cell["FP"], LEFT, buff=0.3)

    grp = VGroup(grid, lab_grp, col_reject, col_keep, row_sig, row_no)
    grp.cell = cell
    grp.lab = labels
    grp.col_reject = col_reject
    grp.col_keep = col_keep
    grp.row_sig = row_sig
    grp.row_no = row_no
    grp.grid = grid
    return grp


# ----------------------------------------------------------------------
# Scene 1 — the confusion matrix
# ----------------------------------------------------------------------
class S1_Confusion(NarratedScene):
    scene_key = "S1_Confusion"

    def construct(self):
        self.header("The confusion matrix")

        texts = {"TP": "?", "FP": "?", "FN": "?", "TN": "?"}
        cols = {"TP": DIM, "FP": DIM, "FN": DIM, "TN": DIM}
        cm = build_confusion(texts, cols).shift(RIGHT * 0.7 + DOWN * 0.1)

        intro = Text("the vocabulary of testing lives in one little table",
                     font_size=26, color=DIM).to_edge(UP, buff=1.0)
        self.play_beat(FadeIn(intro), Create(cm.grid))                     # beat 1

        # rows = truth (we never see this column directly)
        self.play_beat(FadeIn(cm.row_sig, shift=RIGHT * 0.2),
                       FadeIn(cm.row_no, shift=RIGHT * 0.2))               # beat 2

        # cols = test verdict
        self.play_beat(FadeIn(cm.col_reject, shift=DOWN * 0.2),
                       FadeIn(cm.col_keep, shift=DOWN * 0.2),
                       FadeOut(intro))                                     # beat 3

        # TP — top-left
        cm.cell["TP"].set_fill(BACK, 0.18)
        tp = Text("TP\ntrue positive\ncaught a real effect",
                  font_size=18, color=BACK, line_spacing=0.8)\
            .move_to(cm.cell["TP"])
        self.play_beat(cm.cell["TP"].animate.set_stroke(BACK, 3),
                       FadeIn(tp), FadeOut(cm.lab["TP"]))                  # beat 4

        # FP — bottom-left (no-signal row, reject column) — the villain
        cm.cell["FP"].set_fill(BAD, 0.18)
        fp = Text("FP\nfalse positive\ncried wolf",
                  font_size=18, color=BAD, line_spacing=0.8)\
            .move_to(cm.cell["FP"])
        self.play_beat(cm.cell["FP"].animate.set_stroke(BAD, 3),
                       FadeIn(fp), FadeOut(cm.lab["FP"]))                  # beat 5

        # FN — top-right (signal row, keep column)
        cm.cell["FN"].set_fill(DIM, 0.18)
        fn = Text("FN\nfalse negative\nmissed it",
                  font_size=18, color=DIM, line_spacing=0.8)\
            .move_to(cm.cell["FN"])
        self.play_beat(cm.cell["FN"].animate.set_stroke(WHITE, 3),
                       FadeIn(fn), FadeOut(cm.lab["FN"]))                  # beat 6

        # TN — bottom-right
        cm.cell["TN"].set_fill(BACK, 0.10)
        tn = Text("TN\ntrue negative\ncorrectly silent",
                  font_size=18, color=BACK, line_spacing=0.8)\
            .move_to(cm.cell["TN"])
        self.play_beat(cm.cell["TN"].animate.set_stroke(BACK, 3),
                       FadeIn(tn), FadeOut(cm.lab["TN"]))                  # beat 7


# ----------------------------------------------------------------------
# Scene 2 — sensitivity = TP / (TP + FN)
# ----------------------------------------------------------------------
class S2_Sensitivity(NarratedScene):
    scene_key = "S2_Sensitivity"

    def construct(self):
        self.header("Sensitivity")

        intro = Text("sensitivity  =  true-positive rate",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        eq = MathTex(r"\text{sensitivity}", "=",
                     r"\frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}}")\
            .scale(1.4).shift(UP * 0.7)
        eq[0].set_color(WHITE)
        eq[2].set_color(WHITE)
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4))          # beat 2

        # denominator = whole top row (truth = signal)
        denom = MathTex(r"\mathrm{TP} + \mathrm{FN}").scale(1.0).set_color(BACK)
        denom.next_to(eq, DOWN, buff=0.7)
        denom_lab = Text("the whole top row: every case with a real signal",
                         font_size=23, color=BACK).next_to(denom, DOWN, buff=0.25)
        self.play_beat(Write(denom), FadeIn(denom_lab))                    # beat 3

        # numerator = TP only
        self.play(FadeOut(VGroup(denom, denom_lab)), run_time=0.4)
        numer = MathTex(r"\mathrm{TP}").scale(1.1).set_color(RES)
        numer.next_to(eq, DOWN, buff=0.7)
        numer_lab = Text("the ones in that row we actually caught",
                         font_size=23, color=RES).next_to(numer, DOWN, buff=0.25)
        self.play_beat(Write(numer), FadeIn(numer_lab))                    # beat 4

        # the reading: of the real effects, what fraction we catch
        self.play(FadeOut(VGroup(numer, numer_lab, intro)), run_time=0.4)
        reading = VGroup(
            Text("of the real effects,", font_size=27, color=WHITE),
            Text("what fraction do we catch?", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.2).next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(reading, lag_ratio=0.3))                     # beat 5

        # perfect sensitivity: FN -> 0
        perfect = MathTex(r"\text{perfect}", r"\;\Rightarrow\;",
                          r"\mathrm{FN} \to 0").scale(1.05)
        perfect[2].set_color(BACK)
        perfect.next_to(reading, DOWN, buff=0.5)
        self.play_beat(Write(perfect), reading.animate.set_opacity(0.6))   # beat 6

        # sensitivity = power; the easy virtue
        moral = Text("sensitivity is the test's POWER — the easy virtue to chase",
                     font_size=25, color=DIM).to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 3 — specificity = TN / (TN + FP), FP is the villain
# ----------------------------------------------------------------------
class S3_Specificity(NarratedScene):
    scene_key = "S3_Specificity"

    def construct(self):
        self.header("Specificity")

        intro = Text("specificity  =  the conscience of the test",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        eq = MathTex(r"\text{specificity}", "=",
                     r"\frac{\mathrm{TN}}{\mathrm{TN} + \mathrm{FP}}")\
            .scale(1.4).shift(UP * 0.7)
        eq[0].set_color(WHITE)
        eq[2].set_color(WHITE)
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4))          # beat 2

        # denominator = whole bottom row (truth = no signal)
        denom = MathTex(r"\mathrm{TN} + \mathrm{FP}").scale(1.0).set_color(BACK)
        denom.next_to(eq, DOWN, buff=0.7)
        denom_lab = Text("the whole bottom row: every genuinely empty case",
                         font_size=23, color=BACK).next_to(denom, DOWN, buff=0.25)
        self.play_beat(Write(denom), FadeIn(denom_lab))                    # beat 3

        # numerator = TN only
        self.play(FadeOut(VGroup(denom, denom_lab)), run_time=0.4)
        numer = MathTex(r"\mathrm{TN}").scale(1.1).set_color(RES)
        numer.next_to(eq, DOWN, buff=0.7)
        numer_lab = Text("the empty cases we correctly cleared",
                         font_size=23, color=RES).next_to(numer, DOWN, buff=0.25)
        self.play_beat(Write(numer), FadeIn(numer_lab))                    # beat 4

        # the reading
        self.play(FadeOut(VGroup(numer, numer_lab, intro)), run_time=0.4)
        reading = VGroup(
            Text("of the nulls,", font_size=27, color=WHITE),
            Text("what fraction do we correctly clear?", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.2).next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(reading, lag_ratio=0.3))                     # beat 5

        # FP the villain
        self.play(FadeOut(reading), run_time=0.4)
        villain = VGroup(
            Text("the villain:  FP", font_size=30, color=BAD),
            Text("a null we wrongly flagged as real", font_size=24, color=BAD),
            Text("every false positive eats your specificity", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.2).next_to(eq, DOWN, buff=0.6)
        self.play_beat(FadeIn(villain, lag_ratio=0.3))                     # beat 6

        # why it matters for LNM
        moral = Text("for lesion mapping the backbone MANUFACTURES false positives",
                     font_size=25, color=BAD).to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 4 — the trade-off (ROC)
# ----------------------------------------------------------------------
class S4_ROC(NarratedScene):
    scene_key = "S4_ROC"

    def construct(self):
        self.header("The trade-off")

        intro = Text("you cannot freely maximize both",
                     font_size=28, color=RES).shift(UP * 2.6)
        link = MathTex(r"\text{sensitivity}", r"\;\longleftrightarrow\;",
                       r"\text{specificity}").scale(1.0).next_to(intro, DOWN, buff=0.3)
        link[0].set_color(BACK); link[2].set_color(BAD)
        self.play_beat(FadeIn(intro), Write(link))                         # beat 1

        # the threshold dial
        axes = Axes(x_range=[0, 1, 0.5], y_range=[0, 1, 0.5],
                    x_length=4.6, y_length=4.6,
                    axis_config={"include_tip": True, "color": DIM,
                                 "include_numbers": False})\
            .shift(DOWN * 0.6 + LEFT * 2.6)
        xlab = Text("1 - specificity\n(false-positive rate)", font_size=18,
                    color=BAD, line_spacing=0.8).next_to(axes, DOWN, buff=0.2)
        ylab = Text("sensitivity", font_size=18, color=BACK)\
            .rotate(PI / 2).next_to(axes, LEFT, buff=0.2)
        self.play_beat(Create(axes), FadeIn(xlab), FadeIn(ylab),
                       FadeOut(VGroup(intro, link)))                       # beat 2

        # the ROC curve itself (concave, bowing toward top-left)
        roc = axes.plot(lambda x: x ** 0.32, x_range=[0, 1], color=RES)
        diag = DashedLine(axes.c2p(0, 0), axes.c2p(1, 1), color=DIM)
        trade = Text("reject more  →  sensitivity up,\nspecificity down",
                     font_size=22, color=WHITE, line_spacing=0.8)\
            .shift(RIGHT * 3.4 + UP * 1.0)
        self.play_beat(Create(diag), FadeIn(trade))                        # beat 3

        # sweep the dial -> trace the curve
        self.play_beat(Create(roc), run_time=2.0)                          # beat 4

        # the always-reject corner: sens=1, spec=0
        corner = Dot(axes.c2p(1, 1), color=BAD, radius=0.09)
        corner_lab = VGroup(
            Text("always REJECT", font_size=22, color=BAD),
            MathTex(r"\text{sensitivity} = 1,\ \ \text{specificity} = 0").scale(0.7),
        ).arrange(DOWN, buff=0.15).next_to(corner, RIGHT, buff=0.2).shift(DOWN * 0.3)
        self.play_beat(FadeIn(corner, scale=2.0), FadeIn(corner_lab))      # beat 5

        # worthless
        worthless = Text("a test that always says yes is sensitive and worthless",
                         font_size=23, color=DIM).to_edge(DOWN, buff=0.6)
        self.play_beat(FadeIn(worthless, shift=UP * 0.2))                  # beat 6

        # why specificity is the hard one for LNM
        self.play(FadeOut(VGroup(axes, xlab, ylab, roc, diag, trade,
                                 corner, corner_lab, worthless)), run_time=0.5)
        lnm = VGroup(
            Text("for LNM, SPECIFICITY is the hard one", font_size=28, color=BAD),
            Text("the backbone makes almost every map look real", font_size=24, color=WHITE),
            Text("catching is easy; clearing is not", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25)
        self.play_beat(FadeIn(lnm, lag_ratio=0.3))                         # beat 7


# ----------------------------------------------------------------------
# Scene 5 — a null is a question
# ----------------------------------------------------------------------
class S5_NullIsQuestion(NarratedScene):
    scene_key = "S5_NullIsQuestion"

    def construct(self):
        self.header("A null is a question")

        thesis = VGroup(
            Text("A null hypothesis is not just a baseline.", font_size=28, color=WHITE),
            Text("It is a QUESTION.", font_size=34, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.4)
        self.play_beat(FadeIn(thesis[0]), Write(thesis[1]))                # beat 1

        quote = Text("\"A null model is a question. Get the question wrong, and a\n"
                     "perfectly good test gives you a useless answer.\"",
                     font_size=24, color=DIM, line_spacing=0.8)\
            .next_to(thesis, DOWN, buff=0.5)
        self.play_beat(FadeIn(quote))                                      # beat 2

        # found nothing -> two reasons
        self.play(FadeOut(VGroup(thesis, quote)), run_time=0.5)
        found = Text("\"Found nothing\"  can mean two different things",
                     font_size=28, color=WHITE).shift(UP * 2.4)
        self.play_beat(FadeIn(found))                                      # beat 3

        # reason 1: the answer is no
        r1 = VGroup(
            Text("1.  the answer really is NO", font_size=27, color=BACK),
            Text("no signal — the test correctly stayed silent", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 0.9)
        self.play_beat(FadeIn(r1, shift=UP * 0.2))                         # beat 4

        # reason 2: the question was wrong
        r2 = VGroup(
            Text("2.  the QUESTION was wrong", font_size=27, color=BAD),
            Text("wrong null — a real signal had nowhere to show up", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(r1, DOWN, buff=0.5)
        self.play_beat(FadeIn(r2, shift=UP * 0.2))                         # beat 5

        # preview: same data, two nulls
        self.play(FadeOut(VGroup(found, r1, r2)), run_time=0.5)
        preview = Text("the trap ahead: the SAME lesion data, two different nulls",
                       font_size=27, color=RES).shift(UP * 2.3)
        self.play_beat(FadeIn(preview))                                    # beat 6

        # the two questions, side by side
        loc = VGroup(
            Text("LOCATION null", font_size=25, color=BAD),
            Text("is this lesion location\nspecial?", font_size=21, color=WHITE,
                 line_spacing=0.8),
        ).arrange(DOWN, buff=0.2)
        sym = VGroup(
            Text("SYMPTOM null", font_size=25, color=BACK),
            Text("does the symptom track\nthese lesions more than\nchance?",
                 font_size=21, color=WHITE, line_spacing=0.8),
        ).arrange(DOWN, buff=0.2)
        pair = VGroup(loc, MathTex(r"\neq", color=RES).scale(1.4), sym)\
            .arrange(RIGHT, buff=1.1).shift(DOWN * 0.2)
        self.play_beat(FadeIn(pair, lag_ratio=0.2))                        # beat 7

        # same patients, opposite fates
        moral = VGroup(
            Text("same patients, same connectome, opposite fates",
                 font_size=25, color=WHITE),
            Text("next: why one question fails and the other cannot",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 8
