"""c0902_prediction_ceiling — "The prediction ceiling".

Five narrated scenes on P3's load-bearing empirical fact: connectome-based maps
hit a LOW, refinement-proof prediction ceiling. We define R^2, cite the exact
stroke numbers (R^2 = 0.01 to 0.18, n = 132), show that anatomical refinement did
NOT help (a model-class limit, not a resolution problem), state precisely what a
low ceiling does and does not bound, and keep the EFFECT-SIZE axis distinct from
the VALIDITY axis.

All equations/numbers are page-cited in:
  responses/lnm_critique/papers/P3_biolimits.md          (R^2 = 0.01-0.18, n=132)
  responses/lnm_critique/sections/07_biological_limits.md (effect size vs validity)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0902_prediction_ceiling ./render.sh \
      chapters/c0902_prediction_ceiling/scenes.py -q ql \
      S1_Question S2_Numbers S3_Refinement S4_Bounds S5_Honest
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — How well can it predict?  Define R^2.
# ----------------------------------------------------------------------
class S1_Question(NarratedScene):
    scene_key = "S1_Question"

    def construct(self):
        title = Text("How well can it predict", font_size=42, color=WHITE)
        sub = Text("the bluntest clinical question",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        cite = Text("Pini, Salvalaggio & Corbetta, Nat. Neurosci. Comment (2026)",
                    font_size=23, color=DIM).shift(UP * 1.9)
        paper = Text("\"Considering biological limitations of\nlesion network mapping\"",
                     font_size=26, color=WHITE, line_spacing=0.8)\
            .next_to(cite, DOWN, buff=0.35)
        self.play_beat(FadeIn(cite), FadeIn(paper))                         # beat 2

        # the empirical question
        self.play(FadeOut(VGroup(cite, paper)), run_time=0.5)
        q = VGroup(
            Text("The empirical question:", font_size=28, color=RES),
            Text("of the variance in patient outcomes,", font_size=26, color=WHITE),
            Text("how much can a connectome map explain?", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT).shift(UP * 0.6)
        self.play_beat(FadeIn(q, lag_ratio=0.2))                            # beat 3

        # define R^2
        self.play(FadeOut(q), run_time=0.5)
        eq = MathTex("R^2", "=", r"\text{fraction of outcome variance explained}")\
            .scale(1.0).shift(UP * 1.2)
        eq[0].set_color(EIG)
        rng = MathTex("0", r"\ \leq\ ", "R^2", r"\ \leq\ ", "1").scale(1.1)
        rng[2].set_color(EIG)
        rng.next_to(eq, DOWN, buff=0.6)
        self.play_beat(Write(eq), Write(rng))                               # beat 4

        # the two poles of R^2
        poles = VGroup(
            VGroup(
                MathTex("R^2", "=", "1", color=EIG).scale(0.95),
                Text("predicts the outcome perfectly", font_size=23, color=BACK),
            ).arrange(DOWN, buff=0.18),
            VGroup(
                MathTex("R^2", "=", "0", color=EIG).scale(0.95),
                Text("predicts nothing at all", font_size=23, color=BAD),
            ).arrange(DOWN, buff=0.18),
        ).arrange(RIGHT, buff=1.6).next_to(rng, DOWN, buff=0.6)
        self.play_beat(FadeIn(poles, lag_ratio=0.2))                        # beat 5

        moral = VGroup(
            Text("This chapter lives on one number.", font_size=26, color=WHITE),
            Text("Not \"is the test valid\" — but \"how big is the effect.\"",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.22).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                       # beat 6


# ----------------------------------------------------------------------
# Scene 2 — the stroke numbers:  R^2 = 0.01 to 0.18,  n = 132
# ----------------------------------------------------------------------
class S2_Numbers(NarratedScene):
    scene_key = "S2_Numbers"

    def construct(self):
        self.header("The stroke numbers  (P3, p.1)")

        n = MathTex("n", "=", "132", r"\ \text{first-stroke patients}")\
            .scale(1.1).shift(UP * 2.2)
        n[0].set_color(VAR); n[2].set_color(RES)
        self.play_beat(Write(n))                                            # beat 1

        what = Text("LNM predicted behavioral outcomes\nacross several cognitive domains",
                    font_size=26, color=WHITE, line_spacing=0.8).shift(UP * 1.0)
        self.play_beat(FadeIn(what))                                        # beat 2

        # the range itself
        self.play(FadeOut(what), run_time=0.4)
        rng = MathTex("R^2", "=", "0.01", r"\ \text{to}\ ", "0.18")\
            .scale(1.4).shift(UP * 0.9)
        rng[0].set_color(EIG); rng[2].set_color(BAD); rng[4].set_color(BAD)
        brace = Brace(rng[2:], DOWN, color=DIM)
        blab = Text("worst domain  →  best domain", font_size=22, color=DIM)\
            .next_to(brace, DOWN, buff=0.2)
        self.play_beat(Write(rng), GrowFromCenter(brace), FadeIn(blab))     # beat 3

        # read as percent
        self.play(FadeOut(VGroup(brace, blab)), run_time=0.4)
        pct = MathTex(r"1\%", r"\ \text{to}\ ", r"18\%",
                      r"\ \text{of variance explained}").scale(1.0)
        pct[0].set_color(BAD); pct[2].set_color(BAD)
        pct.next_to(rng, DOWN, buff=0.55)
        self.play_beat(Write(pct))                                          # beat 4

        # the ceiling bar: even the best leaves >82% on the table
        bar = self._ceiling_bar(0.18).next_to(pct, DOWN, buff=0.55)
        self.play_beat(*[FadeIn(m) for m in bar.submobjects], lag_ratio=0.1)  # beat 5

        low = Text("A low ceiling: the signal is small, far below clinical demand",
                   font_size=24, color=RES).to_edge(DOWN, buff=0.9)
        self.play_beat(FadeIn(low, shift=UP * 0.2))                         # beat 6

        keep = MathTex(r"\text{keep this bar:}\quad", r"R^2 = 0.01\text{--}0.18",
                       r",\ \ n = 132").scale(0.85)
        keep[1].set_color(EIG)
        keep.to_edge(DOWN, buff=0.4)
        self.play_beat(FadeIn(keep))                                        # beat 7

    def _ceiling_bar(self, frac):
        w = 8.0
        full = Rectangle(width=w, height=0.5, stroke_color=WHITE, stroke_width=2,
                         fill_opacity=0)
        filled = Rectangle(width=w * frac, height=0.5, stroke_width=0,
                           fill_color=BAD, fill_opacity=0.85)
        filled.align_to(full, LEFT)
        bar = VGroup(full, filled)
        explained = Text("18% explained", font_size=20, color=BAD)\
            .next_to(filled, UP, buff=0.12).align_to(filled, LEFT)
        rest = Text("> 82% unaccounted for", font_size=20, color=DIM)\
            .move_to(full).shift(RIGHT * 1.4)
        return VGroup(bar, explained, rest).move_to(ORIGIN)


# ----------------------------------------------------------------------
# Scene 3 — refinement did NOT help
# ----------------------------------------------------------------------
class S3_Refinement(NarratedScene):
    scene_key = "S3_Refinement"

    def construct(self):
        self.header("Refinement did not help  (P3, p.1, quote 5)")

        obj = Text("Objection: maybe the ceiling is just noise —\na cleaner anatomy would lift it.",
                   font_size=27, color=DIM, line_spacing=0.8).shift(UP * 2.1)
        self.play_beat(FadeIn(obj))                                         # beat 1

        # the refinement
        refine = VGroup(
            Text("The refined method:", font_size=26, color=WHITE),
            Text("restrict analysis to voxels with", font_size=25, color=VAR),
            Text("coherent connectivity profiles", font_size=25, color=VAR),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).shift(UP * 0.7)
        self.play_beat(FadeIn(refine, lag_ratio=0.2))                       # beat 2

        goal = Text("Goal: strip non-specific signal —\nthe white/gray-matter overlap that blurs true connections",
                    font_size=24, color=DIM, line_spacing=0.8)\
            .next_to(refine, DOWN, buff=0.45)
        self.play_beat(FadeIn(goal))                                        # beat 3

        # the result
        self.play(FadeOut(VGroup(obj, refine, goal)), run_time=0.5)
        result = VGroup(
            Text("more detail   ·   more specificity   ·   sharper input",
                 font_size=25, color=VAR),
            Text("\"did not improve clinical prediction\"",
                 font_size=28, color=BAD),
        ).arrange(DOWN, buff=0.4).shift(UP * 1.4)
        self.play_beat(FadeIn(result[0]), FadeIn(result[1], shift=UP * 0.2))  # beat 4

        # same ceiling: two bars side by side
        bars = self._two_bars().next_to(result, DOWN, buff=0.6)
        self.play_beat(FadeIn(bars, lag_ratio=0.15))                        # beat 5

        tell = Text("The critical tell: cleaning anatomy did not raise R²\n→ not a noise problem you can residualize away",
                    font_size=24, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(tell, shift=UP * 0.2))                        # beat 6

        self.play(FadeOut(VGroup(result, bars, tell)), run_time=0.5)
        cls = VGroup(
            Text("It points at the MODEL CLASS, not the resolution.",
                 font_size=28, color=WHITE),
            Text("The ceiling is intrinsic to a static, first-order connectome.",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(cls, lag_ratio=0.3))                          # beat 7

    def _two_bars(self):
        def bar(frac, color, label):
            w = 5.5
            full = Rectangle(width=w, height=0.4, stroke_color=WHITE,
                             stroke_width=1.5, fill_opacity=0)
            filled = Rectangle(width=w * frac, height=0.4, stroke_width=0,
                               fill_color=color, fill_opacity=0.85)
            filled.align_to(full, LEFT)
            lab = Text(label, font_size=21, color=color)\
                .next_to(full, LEFT, buff=0.3)
            return VGroup(lab, full, filled)
        b1 = bar(0.18, DIM, "standard")
        b2 = bar(0.18, BAD, "refined")
        grp = VGroup(b1, b2).arrange(DOWN, buff=0.5, aligned_edge=RIGHT)
        same = Text("same low ceiling", font_size=22, color=BAD)\
            .next_to(grp, RIGHT, buff=0.4)
        return VGroup(grp, same).move_to(ORIGIN)


# ----------------------------------------------------------------------
# Scene 4 — what that bounds  (be precise: what IS and ISN'T bounded)
# ----------------------------------------------------------------------
class S4_Bounds(NarratedScene):
    scene_key = "S4_Bounds"

    def construct(self):
        self.header("What that bounds")

        head = Text("What does a low, refinement-proof ceiling bound?\nBe careful — it is easy to over-read.",
                    font_size=27, color=DIM, line_spacing=0.8).shift(UP * 2.3)
        self.play_beat(FadeIn(head))                                        # beat 1

        # it bounds clinical utility
        b1 = VGroup(
            Text("It BOUNDS clinical utility:", font_size=27, color=RES),
            Text("how much any static-linear LNM method can deliver",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).shift(UP * 1.0)
        self.play_beat(FadeIn(b1, shift=UP * 0.2))                          # beat 2

        # "any" = the whole model class
        anyword = MathTex(r"\text{``any''}", r"\ =\ ",
                          r"\text{the whole model class, not one careless analysis}")\
            .scale(0.8)
        anyword[0].set_color(RES)
        anyword.next_to(b1, DOWN, buff=0.5)
        self.play_beat(Write(anyword))                                      # beat 3

        # even a clean pipeline
        clean = Text("Even a statistically spotless pipeline\n— exact nulls, honest residualization —\nhits the same ceiling.",
                     font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(anyword, DOWN, buff=0.45)
        self.play_beat(FadeIn(clean, shift=UP * 0.2))                       # beat 4

        # why: residual lives in dimensions a static map cannot reach
        self.play(FadeOut(VGroup(head, b1, anyword, clean)), run_time=0.5)
        why = VGroup(
            Text("The residual variance lives in dimensions", font_size=26, color=DIM),
            Text("a static, first-order map cannot reach:", font_size=26, color=DIM),
            Text("higher-order reorganization", font_size=25, color=BAD),
            Text("hyper- vs hypoconnectivity over time", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.5)
        self.play_beat(FadeIn(why, lag_ratio=0.2))                          # beat 5

        # what it does NOT bound
        self.play(FadeOut(why), run_time=0.5)
        notbound = VGroup(
            Text("What it does NOT bound:", font_size=27, color=BACK),
            Text("it does not say no real circuit exists", font_size=25, color=WHITE),
            Text("it does not say the maps are noise", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(UP * 0.9)
        self.play_beat(FadeIn(notbound, lag_ratio=0.2))                     # beat 6

        moral = Text("It bounds the SIZE of what a static-linear method delivers.\nIt forbids no small, genuine effect from being real.",
                     font_size=25, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                       # beat 7


# ----------------------------------------------------------------------
# Scene 5 — honest framing: effect size vs validity (two distinct axes)
# ----------------------------------------------------------------------
class S5_Honest(NarratedScene):
    scene_key = "S5_Honest"

    def construct(self):
        self.header("Honest framing")

        head = Text("The honest framing turns on keeping two axes apart.",
                    font_size=28, color=WHITE).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                        # beat 1

        # draw the two axes
        axes = Axes(
            x_range=[0, 1, 1], y_range=[0, 1, 1],
            x_length=4.5, y_length=3.2,
            axis_config={"include_tip": True, "color": DIM},
        ).shift(DOWN * 0.4)
        xlab = Text("validity\n(error control)", font_size=20, color=BACK,
                    line_spacing=0.8).next_to(axes.x_axis, DOWN, buff=0.2)
        ylab = Text("effect size\n(R²)", font_size=20, color=EIG,
                    line_spacing=0.8).next_to(axes.y_axis, LEFT, buff=0.2)
        self.play_beat(Create(axes), FadeIn(xlab), FadeIn(ylab))           # beat 2

        # effect-size axis is the separate question
        es = Text("Effect size asks a SEPARATE question:\ngranted the effect is real, how big is it?",
                  font_size=23, color=EIG, line_spacing=0.8)\
            .next_to(axes, RIGHT, buff=0.6)
        self.play_beat(FadeIn(es, shift=UP * 0.2))                          # beat 3

        # P3 is about the second axis
        self.play(FadeOut(es), run_time=0.4)
        p3 = Text("P3 speaks to effect size, not validity:\na limit on clinical utility.",
                  font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(axes, RIGHT, buff=0.6)
        self.play_beat(FadeIn(p3, shift=UP * 0.2))                          # beat 4

        # the valid-but-small point: a dot low on R^2, high on validity
        dot = Dot(axes.c2p(0.85, 0.15), color=RES, radius=0.1)
        dlab = Text("valid AND small:\na real but small effect",
                    font_size=22, color=RES, line_spacing=0.8)\
            .next_to(dot, RIGHT, buff=0.3)
        self.play_beat(FadeIn(dot, scale=0.5), FadeIn(dlab))               # beat 5

        # independence
        self.play(FadeOut(VGroup(p3, dlab)), run_time=0.4)
        indep = VGroup(
            Text("low R² does not refute validity", font_size=24, color=WHITE),
            Text("a valid test does not promise a large effect", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.22).next_to(axes, RIGHT, buff=0.5)
        self.play_beat(FadeIn(indep[0]), FadeIn(indep[1], shift=UP * 0.2))  # beat 6

        self.play(FadeOut(VGroup(head, axes, xlab, ylab, dot, indep)),
                  run_time=0.5)
        moral = VGroup(
            Text("Concede the small effect size.", font_size=30, color=WHITE),
            Text("Keep it distinct from whether the test is sound.",
                 font_size=30, color=RES),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 7
