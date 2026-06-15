"""v0503_anytime_validity — "Anytime validity and optional stopping".

Five narrated scenes building the test-martingale / Ville's-inequality story:
  S1_Problem   the peeking problem: classical tests break under optional stopping
  S2_EProcess  the e-process E_t = prod B_s of conditionally-fair bets
  S3_Ville     Ville: Pr(exists t: E_t >= 1/alpha) <= alpha
  S4_Stop      optional stopping is safe; the p-value disaster as contrast
  S5_Meaning   why it matters: validity from martingale structure, not fixed n

All equations/numbers are drawn from:
  volumes/vol5_evalues/chapters/03_anytime_validity.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0503_anytime_validity ./render.sh \
      chapters/v0503_anytime_validity/scenes.py -q ql \
      S1_Problem S2_EProcess S3_Ville S4_Stop S5_Meaning
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the peeking problem
# ----------------------------------------------------------------------
class S1_Problem(NarratedScene):
    scene_key = "S1_Problem"

    def construct(self):
        self.header("The peeking problem")

        title = Text("Classical tests break if you peek",
                     font_size=34, color=WHITE).shift(UP * 2.5)
        sub = Text("computed once, at a sample size fixed in advance",
                   font_size=24, color=DIM).next_to(title, DOWN, buff=0.25)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1

        # evidence accrues over time
        self.play(FadeOut(VGroup(title, sub)), run_time=0.4)
        accrue = VGroup(
            Text("evidence rarely arrives all at once", font_size=28, color=WHITE),
            Text("patients accrue over years, a few at a time",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 2.3)
        self.play_beat(FadeIn(accrue, lag_ratio=0.3))                      # beat 2

        # the running p-value, peeking at three looks
        axes = Axes(
            x_range=[0, 80, 20], y_range=[0, 0.20, 0.05],
            x_length=8.0, y_length=3.2,
            axis_config={"color": DIM, "include_tip": False, "font_size": 20},
        ).shift(DOWN * 0.6)
        x_lab = axes.get_x_axis_label(Text("patients n", font_size=22, color=DIM))
        y_lab = axes.get_y_axis_label(
            MathTex("p", color=DIM).scale(0.9), edge=LEFT, direction=LEFT)
        # a jagged running p-value path that dips below alpha by chance
        pts = [(0, 0.18), (10, 0.14), (20, 0.11), (30, 0.13),
               (40, 0.07), (50, 0.085), (60, 0.03), (70, 0.06), (80, 0.05)]
        path = axes.plot_line_graph(
            [p[0] for p in pts], [p[1] for p in pts],
            line_color=VAR, add_vertex_dots=False, stroke_width=4)
        self.play_beat(Create(axes), FadeIn(x_lab), FadeIn(y_lab),
                       Create(path))                                        # beat 3

        # alpha line
        alpha_y = axes.c2p(0, 0.05)[1]
        alpha_line = DashedLine(
            axes.c2p(0, 0.05), axes.c2p(80, 0.05), color=BAD, stroke_width=3)
        alpha_lab = MathTex(r"\alpha = 0.05", color=BAD).scale(0.8)\
            .next_to(alpha_line, RIGHT, buff=0.15)
        alpha_txt = Text("alpha: allowed false-positive rate",
                         font_size=22, color=BAD).to_edge(DOWN, buff=0.4)
        self.play_beat(Create(alpha_line), FadeIn(alpha_lab),
                       FadeIn(alpha_txt))                                   # beat 4

        # mark the three peeks
        peek_xs = [20, 40, 60]
        peek_dots = VGroup(*[
            Dot(axes.c2p(px, next(p[1] for p in pts if p[0] == px)),
                radius=0.07, color=EIG)
            for px in peek_xs])
        peek_lab = Text("three peeks  =  three chances to cross by luck",
                        font_size=24, color=EIG).to_edge(DOWN, buff=0.4)
        self.play_beat(FadeOut(alpha_txt),
                       LaggedStart(*[GrowFromCenter(d) for d in peek_dots],
                                   lag_ratio=0.3),
                       FadeIn(peek_lab))                                    # beat 5

        # highlight the spurious crossing
        cross_dot = Dot(axes.c2p(60, 0.03), radius=0.10, color=BAD)
        cross_ring = Circle(radius=0.28, color=BAD, stroke_width=3)\
            .move_to(cross_dot)
        chance = Text("dips below alpha by chance, not because the null is false",
                      font_size=23, color=BAD).to_edge(DOWN, buff=0.4)
        self.play_beat(FadeOut(peek_lab), GrowFromCenter(cross_dot),
                       Create(cross_ring), FadeIn(chance))                 # beat 6

        # the verdict: error balloons
        self.play(FadeOut(VGroup(axes, x_lab, y_lab, path, alpha_line,
                                 alpha_lab, peek_dots, cross_dot, cross_ring,
                                 chance, accrue)), run_time=0.5)
        verdict = VGroup(
            Text("peek and stop early", font_size=28, color=WHITE),
            MathTex(r"\Rightarrow\quad \text{real error rate} \;\gg\; \alpha",
                    color=BAD).scale(1.0),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.4)
        self.play_beat(FadeIn(verdict[0]), Write(verdict[1]))              # beat 7

        promise = Text("This chapter: an object you may watch and stop anytime.",
                       font_size=26, color=RES).next_to(verdict, DOWN, buff=0.7)
        self.play_beat(FadeIn(promise, shift=UP * 0.2))                    # beat 8


# ----------------------------------------------------------------------
# Scene 2 — the e-process (test martingale)
# ----------------------------------------------------------------------
class S2_EProcess(NarratedScene):
    scene_key = "S2_EProcess"

    def construct(self):
        self.header("E-processes")

        casino = VGroup(
            Text("stop computing p-values — start betting", font_size=28, color=WHITE),
            Text("walk in with $1;  the null says the coin is fair",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 2.4)
        self.play_beat(FadeIn(casino, lag_ratio=0.3))                      # beat 1

        # the bet B_t
        bet = MathTex("B_t", r"\geq", "0").scale(1.4).shift(UP * 0.7)
        bet[0].set_color(VAR)
        brace_b = Brace(bet[0], DOWN, color=VAR)
        b_lab = Text("the bet at round t: a non-negative multiplier\nt indexes the rounds  1, 2, 3, ...",
                     font_size=22, color=VAR, line_spacing=0.8)\
            .next_to(brace_b, DOWN, buff=0.2)
        self.play_beat(Write(bet), GrowFromCenter(brace_b), FadeIn(b_lab)) # beat 2

        # wealth = running product
        self.play(FadeOut(VGroup(bet, brace_b, b_lab, casino)), run_time=0.4)
        wealth = MathTex("E_t", "=", r"\prod_{s=1}^{t}", "B_s")\
            .scale(1.4).shift(UP * 1.0)
        wealth[0].set_color(EIG); wealth[3].set_color(VAR)
        wcap = Text("bet your whole pile each round; start from $1",
                    font_size=24, color=DIM).next_to(wealth, DOWN, buff=0.35)
        self.play_beat(Write(wealth), FadeIn(wcap))                        # beat 3

        # decode E_t and t
        brace_e = Brace(wealth[0], UP, color=EIG)
        e_lab = Text("wealth after round t  =  the e-process\na valid e-value at every time t",
                     font_size=22, color=EIG, line_spacing=0.8)\
            .next_to(brace_e, UP, buff=0.2)
        self.play_beat(GrowFromCenter(brace_e), FadeIn(e_lab))             # beat 4

        # the fairness condition
        self.play(FadeOut(VGroup(brace_e, e_lab, wcap)),
                  wealth.animate.scale(0.7).to_edge(UP, buff=1.1),
                  run_time=0.5)
        fair = MathTex(r"\mathbb{E}_{H_0}\!\left[", "B_t", r"\mid",
                       r"\mathcal{F}_{t-1}", r"\right]", r"\leq", "1")\
            .scale(1.2).shift(UP * 0.4)
        fair[1].set_color(VAR); fair[3].set_color(BACK); fair[6].set_color(EIG)
        fcap = Text("each bet is fair under the null — given what you know",
                    font_size=24, color=WHITE).next_to(fair, DOWN, buff=0.35)
        self.play_beat(Write(fair), FadeIn(fcap))                          # beat 5

        # decode the filtration F_{t-1}
        brace_f = Brace(fair[3], DOWN, color=BACK)
        f_lab = Text("the past: the full record of data seen\nthrough the previous round",
                     font_size=22, color=BACK, line_spacing=0.8)\
            .next_to(brace_f, DOWN, buff=0.2)
        self.play_beat(FadeOut(fcap), GrowFromCenter(brace_f),
                       FadeIn(f_lab))                                       # beat 6

        # the meaning of conditional fairness
        self.play(FadeOut(VGroup(brace_f, f_lab)), run_time=0.4)
        meaning = VGroup(
            Text("whatever you've seen, the next bet can't grow",
                 font_size=25, color=WHITE),
            Text("your money on average if the null is true",
                 font_size=25, color=WHITE),
            Text("adapt cleverly — but never escape fairness",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.18).next_to(fair, DOWN, buff=0.6)
        self.play_beat(FadeIn(meaning, lag_ratio=0.25))                    # beat 7

        # the consequence
        self.play(FadeOut(VGroup(fair, meaning)),
                  wealth.animate.scale(1.0 / 0.7).move_to(UP * 1.6),
                  run_time=0.5)
        cons = MathTex(r"\mathbb{E}_{H_0}", r"\!\left[", "E_t", r"\right]",
                       r"\leq", "1", r"\quad\text{for every } t")\
            .scale(1.1).shift(DOWN * 0.4)
        cons[2].set_color(EIG); cons[5].set_color(RES)
        box = SurroundingRectangle(cons, color=RES, buff=0.2)
        cons_cap = Text("multiply fair bets → the whole trajectory stays fair",
                        font_size=24, color=DIM).next_to(box, DOWN, buff=0.4)
        self.play_beat(Write(cons), Create(box), FadeIn(cons_cap))         # beat 8


# ----------------------------------------------------------------------
# Scene 3 — Ville's inequality
# ----------------------------------------------------------------------
class S3_Ville(NarratedScene):
    scene_key = "S3_Ville"

    def construct(self):
        self.header("Ville's inequality")

        # Markov: one fixed peek
        markov = MathTex(r"\Pr_{H_0}\!\left(", "E_t", r"\geq",
                         r"\tfrac{1}{\alpha}", r"\right)", r"\leq", r"\alpha")\
            .scale(1.1).shift(UP * 2.2)
        markov[1].set_color(EIG); markov[6].set_color(BAD)
        mcap = Text("Markov: one fixed time t — a single peek",
                    font_size=24, color=DIM).next_to(markov, DOWN, buff=0.25)
        self.play_beat(Write(markov), FadeIn(mcap))                        # beat 1

        upgrade = Text("Ville controls the ENTIRE history at once",
                       font_size=27, color=WHITE).shift(UP * 0.5)
        self.play_beat(markov.animate.set_opacity(0.4),
                       mcap.animate.set_opacity(0.4),
                       FadeIn(upgrade, shift=UP * 0.2))                     # beat 2

        # the ingredients: non-negative supermartingale starting at 1
        self.play(FadeOut(VGroup(markov, mcap, upgrade)), run_time=0.4)
        ingr = VGroup(
            Text("needs:  a non-negative supermartingale, starting at 1",
                 font_size=26, color=WHITE),
            MathTex(r"\mathbb{E}[E_t \mid \mathcal{F}_{t-1}] \;\leq\; E_{t-1}",
                    color=BACK).scale(1.0),
            Text("supermartingale: expected next value ≤ current value",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.1)
        ingr[1][0].set_color(BACK)
        self.play_beat(FadeIn(ingr[0]), Write(ingr[1]), FadeIn(ingr[2]))   # beat 3

        # why our wealth qualifies
        qual = VGroup(
            Text("each bet is break-even-or-worse under the null,",
                 font_size=25, color=WHITE),
            Text("so on average the pile never grows — and every bet ≥ 0",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.2).next_to(ingr, DOWN, buff=0.55)
        self.play_beat(FadeIn(qual, lag_ratio=0.3))                        # beat 4

        # the theorem
        self.play(FadeOut(VGroup(ingr, qual)), run_time=0.5)
        ville = MathTex(r"\Pr_{H_0}\!\Big(", r"\exists\, t:", "E_t",
                        r"\geq", r"\tfrac{1}{\alpha}", r"\Big)", r"\leq",
                        r"\alpha").scale(1.25).shift(UP * 0.9)
        ville[1].set_color(VAR); ville[2].set_color(EIG)
        ville[4].set_color(WHITE); ville[7].set_color(BAD)
        box = SurroundingRectangle(ville, color=RES, buff=0.25)
        self.play_beat(Write(ville), Create(box))                          # beat 5

        # decode the quantifier
        brace_q = Brace(ville[1], DOWN, color=VAR)
        q_lab = Text("'there exists a t'  =  EVER, at any round\nnot a moment fixed beforehand",
                     font_size=23, color=VAR, line_spacing=0.8)\
            .next_to(brace_q, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_q), FadeIn(q_lab))             # beat 6

        # the twenty-fold intuition
        self.play(FadeOut(VGroup(brace_q, q_lab)), run_time=0.4)
        intuit = VGroup(
            Text("ever getting twenty-fold rich vs a true null:",
                 font_size=25, color=WHITE),
            MathTex(r"\Pr \;\leq\; \tfrac{1}{20} \;=\; 5\%",
                    color=RES).scale(1.1),
        ).arrange(DOWN, buff=0.3).next_to(box, DOWN, buff=0.6)
        self.play_beat(FadeIn(intuit[0]), Write(intuit[1]))                # beat 7

        guar = Text("the running maximum is bounded by the SAME constant\nas a single peek — the anytime guarantee",
                    font_size=24, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.5)
        self.play_beat(FadeIn(guar, shift=UP * 0.2))                       # beat 8


# ----------------------------------------------------------------------
# Scene 4 — optional stopping is safe
# ----------------------------------------------------------------------
class S4_Stop(NarratedScene):
    scene_key = "S4_Stop"

    def construct(self):
        self.header("Optional stopping is safe")

        head = Text("the bound holds simultaneously for ALL t",
                    font_size=28, color=RES).shift(UP * 2.5)
        sub = Text("so you may stop whenever you like", font_size=24, color=DIM)\
            .next_to(head, DOWN, buff=0.25)
        self.play_beat(FadeIn(head), FadeIn(sub, shift=UP * 0.2))          # beat 1

        # the procedure: fix alpha, start at 1, update
        self.play(FadeOut(VGroup(head, sub)), run_time=0.4)
        proc = VGroup(
            MathTex(r"\text{fix } \alpha \Rightarrow \text{threshold } "
                    r"\tfrac{1}{\alpha} = 20", color=WHITE).scale(0.95),
            MathTex("E_0", "=", "1", color=EIG).scale(0.95),
            MathTex("E_t", "=", "E_{t-1}", r"\cdot", "B_t").scale(0.95),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.4)
        proc[1][0].set_color(EIG)
        proc[2][0].set_color(EIG); proc[2][2].set_color(EIG)
        proc[2][4].set_color(VAR)
        self.play_beat(LaggedStart(*[Write(m) for m in proc], lag_ratio=0.3)) # beat 2

        # reject at first crossing — the stopping time
        reject = MathTex(r"\text{reject } H_0 \text{ at first }",
                         "E_t", r"\geq", r"\tfrac{1}{\alpha}")\
            .scale(1.0).next_to(proc, DOWN, buff=0.55)
        reject[1].set_color(EIG); reject[3].set_color(BAD)
        tau = Text("a data-dependent stopping time: a moment you choose by watching",
                   font_size=22, color=DIM).next_to(reject, DOWN, buff=0.25)
        self.play_beat(Write(reject), FadeIn(tau))                         # beat 3

        # may quit for any reason
        self.play(FadeOut(VGroup(proc, reject, tau)), run_time=0.5)
        quit_txt = VGroup(
            Text("otherwise keep watching", font_size=27, color=WHITE),
            Text("quit for any reason: funding ends, cohort closes, you got bored",
                 font_size=23, color=DIM),
            Text("— and still control your error", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.3)
        self.play_beat(FadeIn(quit_txt, lag_ratio=0.3))                    # beat 4

        guar = MathTex(r"\Pr(\text{ever hit threshold}) \leq \alpha",
                       r"\;\Rightarrow\;",
                       r"\text{type-I error} \leq \alpha")\
            .scale(0.9).next_to(quit_txt, DOWN, buff=0.6)
        guar[0].set_color(BACK); guar[2].set_color(RES)
        self.play_beat(Write(guar))                                        # beat 5

        # contrast: the p-value disaster
        self.play(FadeOut(VGroup(quit_txt, guar)), run_time=0.5)
        disaster = VGroup(
            Text("the p-value disaster", font_size=28, color=BAD),
            Text("reuse the 0.05 cutoff at three interim looks →",
                 font_size=24, color=WHITE),
            MathTex(r"\Pr(\text{cross somewhere}) \;\approx\; 3 \times \alpha",
                    color=BAD).scale(0.95),
        ).arrange(DOWN, buff=0.28).shift(UP * 0.9)
        self.play_beat(FadeIn(disaster[0]), FadeIn(disaster[1]),
                       Write(disaster[2]))                                 # beat 6

        inflate = Text("classic alpha inflation — trials need spending rules to peek legally\nthe martingale builds the freedom in",
                       font_size=23, color=DIM, line_spacing=0.8)\
            .next_to(disaster, DOWN, buff=0.5)
        self.play_beat(FadeIn(inflate, shift=UP * 0.2))                    # beat 7

        self.play(FadeOut(VGroup(disaster, inflate)), run_time=0.5)
        slogan = VGroup(
            Text("no committed sample size.", font_size=30, color=WHITE),
            Text("no peeking tax.", font_size=30, color=WHITE),
            Text("that is anytime-validity.", font_size=30, color=RES),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(FadeIn(slogan, lag_ratio=0.3))                      # beat 8


# ----------------------------------------------------------------------
# Scene 5 — why it matters
# ----------------------------------------------------------------------
class S5_Meaning(NarratedScene):
    scene_key = "S5_Meaning"

    def construct(self):
        self.header("Why it matters")

        head = Text("anytime-valid inference: monitor evidence continuously",
                    font_size=27, color=WHITE).shift(UP * 2.5)
        sub = Text("look after every patient — and stop on a dime",
                   font_size=24, color=DIM).next_to(head, DOWN, buff=0.25)
        self.play_beat(FadeIn(head), FadeIn(sub, shift=UP * 0.2))          # beat 1

        # stop on success vs futility
        self.play(FadeOut(VGroup(head, sub)), run_time=0.4)
        two = VGroup(
            VGroup(
                Text("stop on SUCCESS", font_size=26, color=RES),
                MathTex(r"E_t \geq \tfrac{1}{\alpha}", color=EIG).scale(0.9),
                Text("declare the effect real", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.18),
            VGroup(
                Text("stop on FUTILITY", font_size=26, color=DIM),
                Text("accrual ends", font_size=22, color=DIM),
                Text("report the wealth reached", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.18),
        ).arrange(RIGHT, buff=1.6).shift(UP * 0.9)
        self.play_beat(FadeIn(two, lag_ratio=0.2))                         # beat 2

        calib = Text("either way the number is a calibrated measure of evidence\nno committed sample size, no penalty for looking",
                     font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(two, DOWN, buff=0.6)
        self.play_beat(FadeIn(calib, shift=UP * 0.2))                      # beat 3

        # source of validity
        self.play(FadeOut(VGroup(two, calib)), run_time=0.5)
        src = VGroup(
            Text("validity comes from the MARTINGALE STRUCTURE",
                 font_size=27, color=RES),
            MathTex("E_t", "=", r"\prod_{s=1}^{t}", "B_s",
                    r"\quad", r"\mathbb{E}[B_s \mid \mathcal{F}_{s-1}] \leq 1")
            .scale(0.9),
            Text("conditionally-fair bets, multiplied through time",
                 font_size=23, color=DIM),
            Text("not from a fixed sample size", font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.7)
        src[1][0].set_color(EIG); src[1][3].set_color(VAR)
        self.play_beat(FadeIn(src[0]), Write(src[1]), FadeIn(src[2]),
                       FadeIn(src[3]))                                      # beat 4

        # the hinge: non-negativity
        self.play(FadeOut(src), run_time=0.5)
        hinge = VGroup(
            Text("the hinge is non-negativity", font_size=28, color=WHITE),
            MathTex(r"B_t \geq 0", color=VAR).scale(1.1),
            Text("drop it and Ville fails outright —", font_size=24, color=BAD),
            Text("that is why e-values are non-negative by definition",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.28).shift(UP * 0.6)
        self.play_beat(FadeIn(hinge, lag_ratio=0.25))                      # beat 5

        # cost is power, not validity
        self.play(FadeOut(hinge), run_time=0.5)
        cost = VGroup(
            Text("the cost is POWER, not validity", font_size=28, color=RES),
            Text("a bet hedging many alternatives grows slower",
                 font_size=24, color=WHITE),
            Text("than a fixed-n test tuned to the truth",
                 font_size=24, color=WHITE),
            Text("validity is free; you trade efficiency",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.6)
        self.play_beat(FadeIn(cost, lag_ratio=0.25))                       # beat 6

        # caution: confounding
        self.play(FadeOut(cost), run_time=0.5)
        caution = VGroup(
            Text("one caution", font_size=27, color=BAD),
            Text("valid only for the null its bets are fair against",
                 font_size=24, color=WHITE),
            Text("a confounder ignored = evidence against the WRONG null",
                 font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.9)
        self.play_beat(FadeIn(caution, lag_ratio=0.25))                    # beat 7

        moral = Text("Fix confounding in the design, then ride the martingale on top.\nFor a slowly-accruing cohort, this is the honest way to monitor.",
                     font_size=24, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 8
