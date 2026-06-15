"""c0903_different_critique — "A different critique than P1".

Five narrated scenes distinguishing two attacks on lesion network mapping:

  P1 (van den Heuvel et al.) — an INFERENCE charge: the group-average prior is
      nonspecific and converges to the connectome's degree.
  P3 (Pini, Salvalaggio & Corbetta, Nat Neurosci Comment, s41593-026-02319-8,
      posted 20 May 2026) — a MODEL-CLASS charge: a single static, first-order
      connectome C is biologically impoverished. P3 carries two sub-charges:
        (a) C is a misspecified static estimate  — a statistics problem,
            bounded by sensitivity analysis across >= 2 connectomes;
        (b) a static, first-order C is missing whole dimensions (higher-order
            reorganization; hyper-/hypoconnectivity dynamics) — NOT fixable by
            any null model. Conceded.

All equations/numbers/claims are sourced from:
  responses/lnm_critique/papers/P3_biolimits.md
  responses/lnm_critique/sections/07_biological_limits.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0903_different_critique ./render.sh \
      chapters/c0903_different_critique/scenes.py -q ql \
      S1_TwoCritiques S2_Orthogonal S3_Compose S4_Together S5_Takeaway
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — two different attacks  (7 beats)
# ----------------------------------------------------------------------
class S1_TwoCritiques(NarratedScene):
    scene_key = "S1_TwoCritiques"

    def construct(self):
        title = Text("Two different attacks", font_size=42, color=WHITE)
        sub = Text("same target, different organ",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # P1 card on the left
        p1 = self._card(
            "P1", "van den Heuvel et al.",
            ["the group-average prior", "is nonspecific:",
             "it collapses to deg(C)"],
            BAD,
        ).shift(LEFT * 3.4 + UP * 0.2)
        self.play_beat(FadeIn(p1, shift=RIGHT * 0.2))                       # beat 2

        p1_tag = Text("a charge against the INFERENCE",
                      font_size=24, color=BAD).next_to(p1, DOWN, buff=0.4)
        self.play_beat(FadeIn(p1_tag, shift=UP * 0.2))                      # beat 3

        # P3 card on the right
        p3 = self._card(
            "P3", "Pini, Salvalaggio & Corbetta",
            ["the MODEL CLASS is", "biologically impoverished:",
             "a single static C"],
            BACK,
        ).shift(RIGHT * 3.4 + UP * 0.2)
        self.play_beat(FadeIn(p3, shift=LEFT * 0.2))                        # beat 4

        # clear the cards, then decode every symbol of the seed equation
        eq = MathTex("m", "=", "C", r"\ell").scale(1.3).shift(UP * 0.4)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        brace = Brace(eq[2], DOWN, color=BACK)
        clab = Text("static, first-order connectome",
                    font_size=22, color=BACK).next_to(brace, DOWN, buff=0.12)
        brace_m = Brace(eq[0], UP, color=VAR)
        mlab = Text("LNM map", font_size=22, color=VAR)\
            .next_to(brace_m, UP, buff=0.1)
        brace_l = Brace(eq[3], DOWN, color=VAR)
        llab = Text("lesion seed", font_size=22, color=VAR)\
            .next_to(brace_l, DOWN, buff=0.12)
        self.play_beat(FadeOut(VGroup(p1, p1_tag, p3)),
                       Write(eq), GrowFromCenter(brace), FadeIn(clab),
                       GrowFromCenter(brace_m), FadeIn(mlab),
                       GrowFromCenter(brace_l), FadeIn(llab))               # beat 5

        decode = VGroup(
            Text("static = frozen at one moment", font_size=24, color=DIM),
            Text("first-order = only the direct wiring cut",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)\
            .next_to(clab, DOWN, buff=0.55)
        self.play_beat(FadeIn(decode, lag_ratio=0.3))                      # beat 6

        # different targets
        self.play(FadeOut(VGroup(eq, brace, clab, brace_m, mlab,
                                 brace_l, llab, decode)), run_time=0.5)
        verdict = VGroup(
            Text("P1:  the answer is generic", font_size=27, color=BAD),
            Text("P3:  the question itself is too small", font_size=27, color=BACK),
        ).arrange(DOWN, buff=0.3).shift(DOWN * 1.9)
        self.play_beat(FadeIn(verdict[0]), FadeIn(verdict[1], shift=UP * 0.2))  # beat 7

    def _card(self, tag, who, lines, color):
        box = RoundedRectangle(width=4.0, height=2.6, corner_radius=0.15,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.08)
        head = Text(tag, font_size=30, color=color, weight=BOLD)
        author = Text(who, font_size=18, color=DIM)
        body = VGroup(*[Text(t, font_size=20, color=WHITE) for t in lines])\
            .arrange(DOWN, buff=0.12)
        stack = VGroup(head, author, body).arrange(DOWN, buff=0.2)\
            .move_to(box)
        return VGroup(box, stack)


# ----------------------------------------------------------------------
# Scene 2 — orthogonal axes  (7 beats)
# ----------------------------------------------------------------------
class S2_Orthogonal(NarratedScene):
    scene_key = "S2_Orthogonal"

    def construct(self):
        self.header("Orthogonal axes")

        intro = Text("the two critiques are literally orthogonal",
                     font_size=28, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # build the axes
        xax = Arrow(LEFT * 4.5 + DOWN * 1.8, RIGHT * 4.5 + DOWN * 1.8,
                    color=BAD, buff=0.0, stroke_width=4)
        yax = Arrow(LEFT * 4.5 + DOWN * 1.8, LEFT * 4.5 + UP * 2.0,
                    color=BACK, buff=0.0, stroke_width=4)
        xlab = VGroup(
            Text("P1 axis — INFERENCE", font_size=22, color=BAD),
            Text("description  ->  contrast", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.1).next_to(xax, DOWN, buff=0.2)
        self.play_beat(GrowArrow(xax), FadeIn(xlab))                       # beat 2

        # moving right answers P1
        dotR = Dot(RIGHT * 3.0 + DOWN * 1.8, color=BAD, radius=0.09)
        fixed1 = Text("backbone cancels;\nsymptom signal survives",
                      font_size=20, color=BAD, line_spacing=0.8)\
            .next_to(dotR, UP, buff=0.25)
        self.play_beat(FadeIn(dotR, scale=0.5), FadeIn(fixed1))            # beat 3

        # the vertical axis: model class
        ylab = VGroup(
            Text("P3 axis", font_size=22, color=BACK),
            Text("MODEL CLASS", font_size=20, color=BACK),
            Text("static  ->  dynamic", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.08).next_to(yax, RIGHT, buff=0.25)\
            .align_to(yax, UP)
        self.play_beat(GrowArrow(yax), FadeIn(ylab))                       # beat 4

        # moving right does NOT move up
        self.play(FadeOut(VGroup(intro, fixed1)), run_time=0.4)
        proj = DashedLine(dotR.get_center(),
                          RIGHT * 3.0 + DOWN * 1.8 + UP * 0.0,
                          color=DIM)
        flat = Text("moving right does NOT move up",
                    font_size=26, color=RES).shift(UP * 1.3 + RIGHT * 0.5)
        self.play_beat(FadeIn(flat, shift=UP * 0.2), Create(proj))         # beat 5

        same = VGroup(
            Text("a clean contrast is still computed", font_size=22, color=WHITE),
            Text("through the same static C", font_size=22, color=BACK),
        ).arrange(DOWN, buff=0.12).next_to(flat, DOWN, buff=0.35)
        self.play_beat(FadeIn(same, lag_ratio=0.3))                        # beat 6

        # the resolution
        self.play(FadeOut(VGroup(flat, same, proj)), run_time=0.4)
        res = VGroup(
            Text("one axis: fixed by the symptom null", font_size=24, color=BAD),
            Text("the other: no statistic moves you up it", font_size=24, color=BACK),
            Text("=>  they are orthogonal", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.9 + RIGHT * 0.3)
        self.play_beat(FadeIn(res, lag_ratio=0.25))                        # beat 7


# ----------------------------------------------------------------------
# Scene 3 — how they compose with R1 through R5  (7 beats)
# ----------------------------------------------------------------------
class S3_Compose(NarratedScene):
    scene_key = "S3_Compose"

    def construct(self):
        self.header("How they compose with R1-R5")

        intro = Text("R1-R5 were built to answer P1 — and they do",
                     font_size=28, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # R1 + R4
        r14 = VGroup(
            Text("R1:  the average map IS the backbone", font_size=24, color=WHITE),
            Text("R4:  symptom-label permutation is exact,", font_size=24, color=WHITE),
            Text("       and it cancels that backbone", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 1.3)
        self.play_beat(FadeIn(r14, lag_ratio=0.25))                        # beat 2

        # R5
        r5 = VGroup(
            Text("R5:  residualize the leading components,", font_size=24, color=WHITE),
            Text("       sharpening the real contrast", font_size=24, color=BACK),
            Text("=>  together they defeat P1", font_size=24, color=RES),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(r14, DOWN, buff=0.4)
        self.play_beat(FadeIn(r5, lag_ratio=0.25))                         # beat 3

        # the quiet phrase: given C
        self.play(FadeOut(VGroup(intro, r14, r5)), run_time=0.5)
        given = MathTex(r"\text{everything tested is a function of }", "C")\
            .scale(1.0).shift(UP * 1.6)
        given[1].set_color(BACK)
        quiet = Text("\"given C\"  sits under every result — C was always an input",
                     font_size=24, color=DIM).next_to(given, DOWN, buff=0.4)
        self.play_beat(Write(given), FadeIn(quiet))                        # beat 4

        # P3 attacks the input
        attack = VGroup(
            Text("P3 questions the input itself:", font_size=25, color=BACK),
            Text("even a clean, backbone-cancelled contrast", font_size=24, color=WHITE),
            Text("still lives inside a static, first-order C", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.15).next_to(quiet, DOWN, buff=0.5)
        self.play_beat(FadeIn(attack, lag_ratio=0.25))                     # beat 5

        # so R1-R5 do NOT answer P3
        self.play(FadeOut(VGroup(given, quiet, attack)), run_time=0.5)
        nores = VGroup(
            Text("R1-R5 make the inference honest GIVEN C", font_size=25, color=WHITE),
            Text("they cannot enlarge what C can represent", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.1)
        self.play_beat(FadeIn(nores[0]), FadeIn(nores[1], shift=UP * 0.2))  # beat 6

        moral = VGroup(
            Text("You cannot residualize, reweight, or permute", font_size=26, color=RES),
            Text("your way to a dimension your model lacks.", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.18).next_to(nores, DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 4 — the combined picture  (8 beats)
# ----------------------------------------------------------------------
class S4_Together(NarratedScene):
    scene_key = "S4_Together"

    def construct(self):
        self.header("The combined picture")

        intro = Text("the honest response is BOTH moves at once",
                     font_size=28, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # move 1 vs P1
        m1 = VGroup(
            Text("Move 1  —  beats P1", font_size=25, color=BAD),
            Text("use the symptom-label null + residualize the backbone",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 1.4)
        self.play_beat(FadeIn(m1, shift=UP * 0.2))                         # beat 2

        # move 2 vs P3
        m2 = VGroup(
            Text("Move 2  —  concedes P3", font_size=25, color=BACK),
            Text("report the model-class ceiling honestly:",
                 font_size=23, color=WHITE),
            Text("a static, first-order C is blind to two whole axes",
                 font_size=23, color=BACK),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(m1, DOWN, buff=0.45)
        self.play_beat(FadeIn(m2, shift=UP * 0.2))                         # beat 3

        # P3 splits into charge (a) and (b)
        self.play(FadeOut(VGroup(intro, m1, m2)), run_time=0.5)
        head = Text("P3 carries TWO sub-charges", font_size=27, color=BACK)\
            .shift(UP * 2.3)
        ca = VGroup(
            Text("charge (a)", font_size=24, color=RES),
            Text("C is a misspecified STATIC estimate", font_size=23, color=WHITE),
            Text("a statistics problem", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.12)
        self.play_beat(FadeIn(head), FadeIn(ca, shift=UP * 0.2))           # beat 4

        ca_fix = VGroup(
            Text("answer (a) with SENSITIVITY analysis:", font_size=23, color=RES),
            Text("run the contrast through >= 2 defensible connectomes",
                 font_size=22, color=WHITE),
            Text("and report its stability", font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.12).next_to(ca, DOWN, buff=0.5)
        self.play_beat(FadeIn(ca_fix, lag_ratio=0.25))                     # beat 5

        # charge (b)
        self.play(FadeOut(VGroup(head, ca, ca_fix)), run_time=0.5)
        cb = VGroup(
            Text("charge (b)", font_size=24, color=BAD),
            Text("a static, first-order C is MISSING dimensions:",
                 font_size=23, color=WHITE),
            Text("higher-order reorganization", font_size=22, color=BAD),
            Text("hyper- vs hypoconnectivity dynamics", font_size=22, color=BAD),
        ).arrange(DOWN, buff=0.12).shift(UP * 1.1)
        self.play_beat(FadeIn(cb, lag_ratio=0.2))                          # beat 6

        cb_concede = VGroup(
            Text("charge (b) we CONCEDE", font_size=25, color=BAD),
            Text("no operation on a static C recovers an axis it lacks",
                 font_size=22, color=WHITE),
            Text("remedy = a different model class, not a better null",
                 font_size=22, color=RES),
        ).arrange(DOWN, buff=0.13).next_to(cb, DOWN, buff=0.5)
        self.play_beat(FadeIn(cb_concede, lag_ratio=0.2))                  # beat 7

        # both, not either
        self.play(FadeOut(VGroup(cb, cb_concede)), run_time=0.5)
        both = VGroup(
            Text("Beat P1.  Partly answer P3.", font_size=30, color=WHITE),
            Text("Concede the rest out loud.", font_size=30, color=WHITE),
            Text("Both — never either.", font_size=32, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(both, lag_ratio=0.3))                        # beat 8


# ----------------------------------------------------------------------
# Scene 5 — takeaway  (8 beats)
# ----------------------------------------------------------------------
class S5_Takeaway(NarratedScene):
    scene_key = "S5_Takeaway"

    def construct(self):
        self.header("Takeaway")

        head = Text("the most uncomfortable line in the exchange",
                    font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                       # beat 1

        durable = VGroup(
            Text("P3 is the most DURABLE critique", font_size=29, color=BACK),
            Text("because no statistic fixes a model class", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.2)
        self.play_beat(FadeIn(durable[0]), FadeIn(durable[1], shift=UP * 0.2))  # beat 2

        # exactness is conditional — decode every symbol: p_perm, alpha, C
        cond = MathTex(r"\Pr\big(", r"p_{\text{perm}}", r"\le", r"\alpha",
                       r"\ \big|\ ", "C", r"\big)\ \le\ ", r"\alpha").scale(1.0)
        cond[1].set_color(VAR); cond[3].set_color(EIG)
        cond[5].set_color(BACK); cond[7].set_color(EIG)
        cond.next_to(durable, DOWN, buff=0.55)
        brace_p = Brace(cond[1], UP, color=VAR)
        plab = Text("permutation p-value", font_size=18, color=VAR)\
            .next_to(brace_p, UP, buff=0.08)
        brace_a = Brace(cond[7], DOWN, color=EIG)
        alab = Text("significance level", font_size=18, color=EIG)\
            .next_to(brace_a, DOWN, buff=0.1)
        cond_cap = Text("exact for ANY C — even the wrong kind of object",
                        font_size=22, color=DIM).next_to(brace_a, DOWN, buff=0.3)
        self.play_beat(Write(cond), GrowFromCenter(brace_p), FadeIn(plab),
                       GrowFromCenter(brace_a), FadeIn(alab),
                       FadeIn(cond_cap))                                    # beat 3

        # right answer, wrong question
        self.play(FadeOut(VGroup(head, durable, cond, brace_p, plab,
                                 brace_a, alab, cond_cap)), run_time=0.5)
        ref = VGroup(
            Text("Right answer to the wrong question", font_size=28, color=WHITE),
            Text("is still the wrong answer.", font_size=28, color=WHITE),
            Text("the error is not in the inference — it is in the referent",
                 font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.2)
        self.play_beat(FadeIn(ref, lag_ratio=0.25))                        # beat 4

        # but the over-claim does not follow
        warn = VGroup(
            Text("but watch the over-claim:", font_size=24, color=DIM),
            Text("\"C is approximate\"  =/=>  \"LNM recovers nothing\"",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.18).next_to(ref, DOWN, buff=0.55)
        self.play_beat(FadeIn(warn[0]), FadeIn(warn[1], shift=UP * 0.2))   # beat 5

        # quantifier error
        self.play(FadeOut(VGroup(ref, warn)), run_time=0.5)
        quant = VGroup(
            Text("THERE EXISTS a way C can be wrong", font_size=25, color=WHITE),
            Text("does NOT become", font_size=22, color=DIM),
            Text("FOR ALL analyses, C destroys the result", font_size=25, color=BAD),
            Text("Concede the existential.  Deny the universal.",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.6)
        self.play_beat(FadeIn(quant, lag_ratio=0.2))                       # beat 6

        # the stance
        self.play(FadeOut(quant), run_time=0.5)
        stance = VGroup(
            Text("The right response to P3:", font_size=28, color=WHITE),
            Text("humility about effect size,", font_size=30, color=RES),
            Text("not abandonment of valid inference.", font_size=30, color=RES),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.9)
        self.play_beat(FadeIn(stance, lag_ratio=0.3))                      # beat 7

        recipe = VGroup(
            Text("Beat P1 with the symptom null.", font_size=24, color=BAD),
            Text("Bound charge (a) with sensitivity analysis.", font_size=24, color=RES),
            Text("Name charge (b) as the open frontier.", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.18).next_to(stance, DOWN, buff=0.6)
        self.play_beat(FadeIn(recipe, lag_ratio=0.25))                     # beat 8
