"""c0704_p1_curve — "P1's own convergence curve".

Five narrated scenes that walk the critique's OWN published conjunction
simulation. P1 varied between-lesion Dice overlap and measured the fraction of
voxels (lesion sets) reaching significance in a convergence map. As overlap
grows, significance explodes: Dice 0.08 -> 10%, 0.16 -> 64%, >0.25 -> 97%
(van den Heuvel et al., Nat Neurosci 2026, p.1243). We define the Dice
coefficient on screen, plot the three points, then explain WHY with the
shared-backbone inflation bound p^K + (1-p)^K -> 1: convergence is a function of
overlap (shared backbone), not of disease specificity. At realistic overlaps,
near-total agreement is the default under the null of shared structure, so a lit
convergence map is uninformative about a network. We close with the honest
recipe — test against a shared-backbone null, or residualize first, tying to
Part 6 and the symptom-label null. A recipe, not nihilism.

All numbers are page-cited in:
  responses/lnm_critique/sections/05_the_convergence_trap.md
  responses/lnm_critique/papers/P1_critique.md  (p.1243)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0704_p1_curve ./render.sh \
      chapters/c0704_p1_curve/scenes.py -q ql \
      S1_Experiment S2_Curve S3_Interpret S4_Default S5_Resolution
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — The Dice experiment: define Dice between lesion masks
# ----------------------------------------------------------------------
class S1_Experiment(NarratedScene):
    scene_key = "S1_Experiment"

    def construct(self):
        title = Text("The Dice experiment", font_size=42, color=WHITE)
        self.play_beat(Write(title))                                       # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP, buff=0.3),
                  run_time=0.6)

        sim = VGroup(
            Text("P1's conjunction simulation", font_size=27, color=RES),
            MathTex(r"\approx 500{,}000 \ \text{simulated lesions across the atlas}")
                .scale(0.85).set_color(WHITE),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.4)
        self.play_beat(FadeIn(sim[0]), Write(sim[1]))                      # beat 2

        knob = Text("one knob: how much the lesions in a set overlap",
                    font_size=26, color=VAR).next_to(sim, DOWN, buff=0.55)
        self.play_beat(FadeIn(knob, shift=UP * 0.2))                       # beat 3

        # Define the Dice coefficient
        self.play(FadeOut(VGroup(sim, knob)), run_time=0.4)
        # Render the fraction as ONE \frac argument (one mobject, robust), then
        # label numerator/denominator with text positioned relative to the whole
        # fraction's top and bottom edges — no fragile sub-glyph frac slicing.
        dice = MathTex(r"\mathrm{Dice}(A,B)", "=",
                       r"\frac{2\,|A \cap B|}{|A| + |B|}")\
            .scale(1.3).shift(UP * 0.7)
        dice[0].set_color(VAR); dice[2].set_color(WHITE)
        self.play_beat(Write(dice))                                        # beat 4

        frac = dice[2]
        num_lab = Text("twice the shared voxels (on top)", font_size=22, color=BACK)\
            .next_to(frac, UP, buff=0.25)
        num_arr = Arrow(num_lab.get_bottom(), frac.get_top() + UP * 0.05,
                        buff=0.06, color=BACK, stroke_width=3,
                        max_tip_length_to_length_ratio=0.15)
        den_lab = Text("total voxels of both masks (on the bottom)",
                       font_size=22, color=DIM).next_to(frac, DOWN, buff=0.25)
        den_arr = Arrow(den_lab.get_top(), frac.get_bottom() + DOWN * 0.05,
                        buff=0.06, color=DIM, stroke_width=3,
                        max_tip_length_to_length_ratio=0.15)
        scale = MathTex(r"0 \ \text{(no overlap)} \ \longleftrightarrow\ "
                        r"1 \ \text{(identical)}").scale(0.8).set_color(EIG)\
            .to_edge(DOWN, buff=0.9)
        self.play_beat(GrowArrow(num_arr), FadeIn(num_lab),
                       GrowArrow(den_arr), FadeIn(den_lab),
                       FadeIn(scale))                                       # beat 5

        # the other axis: fraction reaching significance
        self.play(FadeOut(VGroup(dice, num_arr, num_lab, den_arr, den_lab,
                                 scale)), run_time=0.4)
        axis = VGroup(
            Text("the other axis:", font_size=26, color=DIM),
            Text("fraction of voxels reaching significance", font_size=28, color=RES),
            Text("how much of the convergence map lights up", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.6)
        self.play_beat(FadeIn(axis, lag_ratio=0.3))                        # beat 6

        thr = VGroup(
            MathTex(r"\text{sensitivity:}\ \ |t| > 7", color=DIM).scale(0.9),
            MathTex(r"\text{specificity:}\ \ |t| > 10", color=BAD).scale(0.9),
        ).arrange(DOWN, buff=0.3).next_to(axis, DOWN, buff=0.6)
        hold = Text("hold the thresholds; vary only overlap",
                    font_size=23, color=BACK).next_to(thr, DOWN, buff=0.35)
        self.play_beat(FadeIn(thr, lag_ratio=0.3), FadeIn(hold))           # beat 7


# ----------------------------------------------------------------------
# Scene 2 — The curve: 0.08->10%, 0.16->64%, 0.25->97%
# ----------------------------------------------------------------------
class S2_Curve(NarratedScene):
    scene_key = "S2_Curve"

    def construct(self):
        self.header("The curve  (P1, p.1243)")

        ax = Axes(
            x_range=[0, 0.30, 0.05], y_range=[0, 100, 25],
            x_length=8.0, y_length=4.4,
            axis_config={"color": DIM, "include_tip": True,
                         "font_size": 20},
            x_axis_config={"numbers_to_include": [0.08, 0.16, 0.25]},
            y_axis_config={"numbers_to_include": [25, 50, 75, 100]},
        ).shift(DOWN * 0.4)
        x_lab = ax.get_x_axis_label(
            Text("between-lesion Dice", font_size=22, color=VAR),
            edge=DOWN, direction=DOWN, buff=0.3)
        y_lab = ax.get_y_axis_label(
            Text("% significant", font_size=22, color=RES),
            edge=LEFT, direction=LEFT, buff=0.3).rotate(PI / 2)
        self.play_beat(Create(ax), FadeIn(x_lab), FadeIn(y_lab))           # beat 1

        # the three data points
        pts = [(0.08, 10), (0.16, 64), (0.25, 97)]
        dots, labels = [], []
        cols = [DIM, EIG, BAD]
        for (dx, dy), col in zip(pts, cols):
            d = Dot(ax.c2p(dx, dy), color=col, radius=0.10)
            dots.append(d)

        d1 = dots[0]
        l1 = MathTex(r"0.08 \to 10\%", color=DIM).scale(0.75)\
            .next_to(d1, UP + RIGHT, buff=0.12)
        self.play_beat(GrowFromCenter(d1), FadeIn(l1))                     # beat 2

        d2 = dots[1]
        l2 = MathTex(r"0.16 \to 64\%", color=EIG).scale(0.75)\
            .next_to(d2, LEFT, buff=0.2)
        self.play_beat(GrowFromCenter(d2), FadeIn(l2))                     # beat 3

        d3 = dots[2]
        l3 = MathTex(r"0.25 \to 97\%", color=BAD).scale(0.75)\
            .next_to(d3, DOWN + RIGHT, buff=0.12)
        self.play_beat(GrowFromCenter(d3), FadeIn(l3))                     # beat 4

        # connect: steep rise
        curve = VMobject(color=RES, stroke_width=4)
        curve.set_points_smoothly([d1.get_center(), d2.get_center(),
                                   d3.get_center()])
        steep = Text("agreement rises steeply — almost a cliff",
                     font_size=24, color=RES).to_edge(DOWN, buff=0.25)
        self.play_beat(Create(curve), FadeIn(steep))                      # beat 5

        cite = Text("van den Heuvel et al., Nat Neurosci 2026 — their own numbers",
                    font_size=22, color=DIM).next_to(steep, UP, buff=0.15)
        self.play_beat(FadeIn(cite))                                       # beat 6

        self.play(FadeOut(VGroup(steep, cite)), run_time=0.3)
        moral = Text("lesions barely have to overlap before\n\"significant convergence\" is the default outcome",
                     font_size=25, color=WHITE, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.2)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 3 — What drives significance: overlap -> shared backbone -> agreement
# ----------------------------------------------------------------------
class S3_Interpret(NarratedScene):
    scene_key = "S3_Interpret"

    def construct(self):
        self.header("What drives significance")

        q = Text("why does a little overlap manufacture so much significance?",
                 font_size=28, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(q))                                          # beat 1

        # the backbone model r_k = mu + eps_k
        model = MathTex("r_k(v)", "=", r"\mu(v)", "+", r"\varepsilon_k(v)")\
            .scale(1.3).shift(UP * 1.0)
        model[0].set_color(VAR); model[2].set_color(BACK); model[4].set_color(DIM)
        br_mu = Brace(model[2], DOWN, color=BACK)
        mu_lab = Text("the shared backbone, common to every map",
                      font_size=22, color=BACK).next_to(br_mu, DOWN, buff=0.15)
        br_e = Brace(model[4], UP, color=DIM)
        e_lab = Text("cohort-specific noise", font_size=22, color=DIM)\
            .next_to(br_e, UP, buff=0.15)
        self.play_beat(Write(model), GrowFromCenter(br_mu), FadeIn(mu_lab),
                       GrowFromCenter(br_e), FadeIn(e_lab))                # beat 2

        self.play(FadeOut(VGroup(q, br_mu, mu_lab, br_e, e_lab)),
                  model.animate.scale(0.7).to_edge(UP, buff=1.1),
                  run_time=0.5)
        more = VGroup(
            Text("more overlap → lesions sample the same rows of C",
                 font_size=26, color=WHITE),
            Text("→ their maps share even more of that shared μ",
                 font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.7)
        self.play_beat(FadeIn(more, lag_ratio=0.3))                        # beat 3

        inter = Text("where maps share a strong common part,\nthey agree in sign almost everywhere it is strong",
                     font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(more, DOWN, buff=0.5)
        tag = Text("agreement is an intersection", font_size=24, color=RES)\
            .next_to(inter, DOWN, buff=0.3)
        self.play_beat(FadeIn(inter), FadeIn(tag, shift=UP * 0.2))         # beat 4

        # the inflation bound
        self.play(FadeOut(VGroup(more, inter, tag)), run_time=0.4)
        bound = MathTex(r"\Pr[\text{all } K \text{ agree}]", "=",
                        "p^K", "+", "(1-p)^K")\
            .scale(1.2).shift(UP * 0.6)
        bound[2].set_color(BACK); bound[4].set_color(DIM)
        p_cap = MathTex(r"p = \Pr[\,\text{a map recovers the backbone sign}\,]")\
            .scale(0.8).set_color(VAR).next_to(bound, DOWN, buff=0.4)
        self.play_beat(Write(bound), FadeIn(p_cap))                        # beat 5

        limit = MathTex(r"p \to 1", r"\ \ \Longrightarrow\ \ ",
                        r"p^K + (1-p)^K \to 1", r"\ \ \text{for every } K")\
            .scale(0.95).next_to(p_cap, DOWN, buff=0.5)
        limit[2].set_color(RES)
        self.play_beat(Write(limit))                                       # beat 6

        self.play(FadeOut(VGroup(model, bound, p_cap, limit)), run_time=0.4)
        concl = VGroup(
            Text("the convergence is a function of OVERLAP — of shared backbone",
                 font_size=26, color=BACK),
            Text("not a function of disease SPECIFICITY at all",
                 font_size=26, color=BAD),
        ).arrange(DOWN, buff=0.4)
        self.play_beat(FadeIn(concl[0]), FadeIn(concl[1], shift=UP * 0.2)) # beat 7


# ----------------------------------------------------------------------
# Scene 4 — Agreement is the default
# ----------------------------------------------------------------------
class S4_Default(NarratedScene):
    scene_key = "S4_Default"

    def construct(self):
        self.header("Agreement is the default")

        setup = MathTex(r"K = 4 \ \text{maps},\quad p = 0.9")\
            .scale(1.1).set_color(WHITE).shift(UP * 2.3)
        self.play_beat(Write(setup))                                       # beat 1

        # independent coins
        indep = MathTex(r"\text{independent coins:}\ \ ", r"2^{\,1-K}",
                        "=", r"2^{-3}", "=", r"12.5\%")\
            .scale(1.0).shift(UP * 1.0)
        indep[1].set_color(DIM); indep[5].set_color(DIM)
        self.play_beat(Write(indep))                                       # beat 2

        # shared backbone
        shared = MathTex(r"\text{shared backbone:}\ \ ", r"0.9^4 + 0.1^4",
                         "=", r"0.6561 + 0.0001", r"\approx", r"65.6\%")\
            .scale(0.92).next_to(indep, DOWN, buff=0.6)
        shared[1].set_color(BACK); shared[5].set_color(RES)
        self.play_beat(Write(shared))                                      # beat 3

        jump = MathTex(r"12.5\% \ \longrightarrow\ 65.6\%",
                       r"\quad (\text{a fivefold jump})")\
            .scale(0.95).next_to(shared, DOWN, buff=0.6)
        jump[0].set_color(RES)
        only = Text("same operator, same K — only the shared backbone changed",
                    font_size=23, color=DIM).next_to(jump, DOWN, buff=0.3)
        self.play_beat(Write(jump), FadeIn(only))                         # beat 4

        self.play(FadeOut(VGroup(setup, indep, shared, jump, only)),
                  run_time=0.5)
        default = Text("at realistic overlaps, near-total agreement is\nEXACTLY what you expect under the null of shared structure",
                       font_size=26, color=WHITE, line_spacing=0.8).shift(UP * 1.0)
        self.play_beat(FadeIn(default, shift=UP * 0.2))                    # beat 5

        unin = VGroup(
            Text("the map being lit is uninformative about a network",
                 font_size=26, color=BAD),
            Text("a big convergence set is the default, not a finding",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3).next_to(default, DOWN, buff=0.6)
        self.play_beat(FadeIn(unin[0]), FadeIn(unin[1]))                   # beat 6

        free = Text("anything you got for free cannot pay for an inference",
                    font_size=26, color=RES).to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(free, shift=UP * 0.2))                       # beat 7


# ----------------------------------------------------------------------
# Scene 5 — How to test convergence honestly
# ----------------------------------------------------------------------
class S5_Resolution(NarratedScene):
    scene_key = "S5_Resolution"

    def construct(self):
        self.header("How to test convergence honestly")

        nih = VGroup(
            Text("This is not nihilism.", font_size=30, color=WHITE),
            Text("convergence is not meaningless — it needs the right yardstick",
                 font_size=25, color=DIM),
        ).arrange(DOWN, buff=0.3).shift(UP * 2.2)
        self.play_beat(FadeIn(nih[0]), FadeIn(nih[1]))                     # beat 1

        wrong = MathTex(r"\text{WRONG yardstick:}\ \ ", r"2^{\,1-K}",
                        r"\ \ (\text{independence})")\
            .scale(0.95).shift(UP * 0.9)
        wrong[1].set_color(BAD)
        wrong_cap = Text("makes any agreement look spectacular",
                         font_size=22, color=DIM).next_to(wrong, DOWN, buff=0.25)
        self.play_beat(Write(wrong), FadeIn(wrong_cap))                    # beat 2

        right = MathTex(r"\text{HONEST yardstick:}\ \ ",
                        r"p^K + (1-p)^K")\
            .scale(0.95).next_to(wrong_cap, DOWN, buff=0.55)
        right[1].set_color(BACK)
        right_cap = Text("does the agreement EXCEED what shared structure predicts?",
                         font_size=22, color=RES).next_to(right, DOWN, buff=0.25)
        self.play_beat(Write(right), FadeIn(right_cap))                    # beat 3

        self.play(FadeOut(VGroup(nih, wrong, wrong_cap, right, right_cap)),
                  run_time=0.5)
        resid = VGroup(
            Text("or residualize first  (Part 6):", font_size=27, color=RES),
            Text("strip the shared backbone out of each map,",
                 font_size=25, color=WHITE),
            Text("then build the convergence on what remains",
                 font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).shift(UP * 1.2)
        self.play_beat(FadeIn(resid, lag_ratio=0.3))                       # beat 4

        survive = Text("the agreement that survives is the part\nthe backbone could NOT manufacture",
                       font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(resid, DOWN, buff=0.5)
        null = Text("→ the symptom-label null doing real work",
                    font_size=24, color=RES).next_to(survive, DOWN, buff=0.3)
        self.play_beat(FadeIn(survive), FadeIn(null, shift=UP * 0.2))      # beat 5

        self.play(FadeOut(VGroup(resid, survive, null)), run_time=0.5)
        recipe = VGroup(
            Text("The recipe:", font_size=28, color=WHITE),
            Text("report convergence as a description, against the backbone baseline",
                 font_size=24, color=DIM),
            Text("never as the headline", font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).shift(UP * 1.0)
        self.play_beat(FadeIn(recipe, lag_ratio=0.3))                      # beat 6

        ride = VGroup(
            Text("let the inferential claim ride on the contrast\nunder a symptom-label null",
                 font_size=25, color=WHITE, line_spacing=0.8),
            Text("honest convergence is earned, not free",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.4).next_to(recipe, DOWN, buff=0.6)
        self.play_beat(FadeIn(ride[0]), FadeIn(ride[1], shift=UP * 0.2))   # beat 7
