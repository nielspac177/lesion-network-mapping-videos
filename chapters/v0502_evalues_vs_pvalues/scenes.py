"""v0502_evalues_vs_pvalues — "E-values versus p-values".

Five narrated scenes building the bridge between p-values and e-values.
Every equation/number is page-cited in:
  volumes/vol5_evalues/chapters/02_evalues_and_pvalues.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0502_evalues_vs_pvalues ./render.sh \
      chapters/v0502_evalues_vs_pvalues/scenes.py -q ql \
      S1_Pvalue S2_Calibrate S3_Conservative S4_WhenEach S5_Takeaway
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — what a p-value is: uniform under the null, reject at alpha
# ----------------------------------------------------------------------
class S1_Pvalue(NarratedScene):
    scene_key = "S1_Pvalue"

    def construct(self):
        self.header("What a p-value is")

        intro = Text("the currency you already know",
                     font_size=28, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                       # beat 1

        # p as a tail probability
        defn = MathTex(r"p", r"=", r"\Pr_{H_0}", r"\big(", r"\text{data this extreme, or worse}", r"\big)")\
            .scale(0.85).shift(UP * 1.0)
        defn[0].set_color(VAR); defn[2].set_color(WHITE); defn[4].set_color(DIM)
        tail = Text("a tail probability under the null",
                    font_size=24, color=DIM).next_to(defn, DOWN, buff=0.3)
        self.play_beat(Write(defn), FadeIn(tail), intro.animate.set_opacity(0.4))  # beat 2

        rng = MathTex(r"0", r"\ \leq\ ", r"p", r"\ \leq\ ", r"1",
                      r"\qquad", r"\text{small} = \text{surprising}")\
            .scale(0.9).next_to(tail, DOWN, buff=0.5)
        rng[2].set_color(VAR); rng[6].set_color(RES)
        self.play_beat(Write(rng))                                         # beat 3

        # the uniform anchor — draw the flat density on axes
        self.play(FadeOut(VGroup(intro, defn, tail, rng)), run_time=0.5)
        ax = Axes(x_range=[0, 1, 0.25], y_range=[0, 1.6, 1],
                  x_length=6.2, y_length=2.6,
                  axis_config={"include_tip": False, "color": DIM,
                               "stroke_width": 2}).shift(DOWN * 0.4)
        xlab = MathTex("p", color=VAR).scale(0.8).next_to(ax.x_axis, RIGHT, buff=0.2)
        flat = ax.plot(lambda x: 1.0, x_range=[0, 1], color=BACK, stroke_width=4)
        flat_lab = Text("uniform on [0, 1] under the null",
                        font_size=24, color=BACK).next_to(ax, UP, buff=0.35)
        self.play_beat(Create(ax), FadeIn(xlab), Create(flat), FadeIn(flat_lab))  # beat 4

        # area to the left of alpha = alpha
        a = 0.3
        region = ax.get_area(flat, x_range=[0, a], color=RES, opacity=0.5)
        atick = DashedLine(ax.c2p(a, 0), ax.c2p(a, 1.0), color=RES, stroke_width=3)
        alab = MathTex(r"\alpha", color=RES).scale(0.85).next_to(atick, UP, buff=0.1)
        area_eq = MathTex(r"\Pr_{H_0}", r"(", r"p", r"\leq", r"\alpha", r")",
                          r"=", r"\alpha").scale(0.85).to_edge(DOWN, buff=0.5)
        area_eq[2].set_color(VAR); area_eq[4].set_color(RES); area_eq[7].set_color(RES)
        self.play_beat(FadeIn(region), Create(atick), FadeIn(alab),
                       Write(area_eq))                                      # beat 5

        # the decision rule
        rule = MathTex(r"\text{reject } H_0", r"\iff", r"p", r"\leq", r"\alpha")\
            .scale(1.0).next_to(area_eq, UP, buff=0.45)
        rule[0].set_color(RES); rule[2].set_color(VAR); rule[4].set_color(RES)
        box = SurroundingRectangle(rule, color=RES, buff=0.15)
        self.play_beat(Write(rule), Create(box))                           # beat 6

        safe = Text("uniformity holds the false-positive rate at alpha",
                    font_size=24, color=BACK).next_to(flat_lab, UP, buff=0.25)
        self.play_beat(FadeIn(safe, shift=UP * 0.2))                       # beat 7


# ----------------------------------------------------------------------
# Scene 2 — calibrators: from p to e and back
# ----------------------------------------------------------------------
class S2_Calibrate(NarratedScene):
    scene_key = "S2_Calibrate"

    def construct(self):
        self.header("From p to e and back")

        # two-lane bridge
        p_chip = self._chip("p-value", VAR).shift(LEFT * 3.8 + UP * 2.0)
        e_chip = self._chip("e-value", EIG).shift(RIGHT * 3.8 + UP * 2.0)
        lane = Line(p_chip.get_right(), e_chip.get_left(), color=DIM)
        title = Text("two languages, one bridge",
                     font_size=26, color=DIM).next_to(lane, DOWN, buff=0.6)
        self.play_beat(FadeIn(p_chip), FadeIn(e_chip), Create(lane),
                       FadeIn(title))                                       # beat 1

        # recall the e-value
        ev = MathTex(r"\mathbb{E}_{H_0}", r"[", r"E", r"]", r"\ \leq\ ", r"1")\
            .scale(1.0).next_to(title, DOWN, buff=0.5)
        ev[2].set_color(EIG); ev[5].set_color(RES)
        ev_cap = Text("stake $1; under the null you cannot expect to profit",
                      font_size=23, color=DIM).next_to(ev, DOWN, buff=0.25)
        self.play_beat(Write(ev), FadeIn(ev_cap))                          # beat 2

        # E -> p direction (Markov), the forward lane
        fwd = Arrow(e_chip.get_bottom() + DOWN * 0.1, p_chip.get_bottom() + DOWN * 0.1,
                    color=VAR, buff=0.2, stroke_width=3)
        fwd_eq = MathTex(r"p", r"=", r"\min", r"\big(", r"1", r",", r"\tfrac{1}{E}", r"\big)")\
            .scale(0.85).next_to(fwd, DOWN, buff=0.15)
        fwd_eq[0].set_color(VAR); fwd_eq[6].set_color(EIG)
        self.play_beat(GrowArrow(fwd), Write(fwd_eq),
                       FadeOut(VGroup(ev, ev_cap)))                        # beat 3

        # p -> E direction needs a calibrator
        self.play(FadeOut(VGroup(fwd, fwd_eq, lane)), run_time=0.4)
        cal = MathTex(r"E", r"=", r"f", r"(", r"p", r")")\
            .scale(1.2).next_to(title, DOWN, buff=0.6)
        cal[0].set_color(EIG); cal[2].set_color(BACK); cal[4].set_color(VAR)
        cal_cap = Text("a calibrator f turns a p-value into an e-value",
                       font_size=24, color=BACK).next_to(cal, DOWN, buff=0.3)
        self.play_beat(Write(cal), FadeIn(cal_cap))                        # beat 4

        # the two requirements on f
        req = VGroup(
            Text("f is non-increasing  →  small p pays a big E",
                 font_size=24, color=WHITE),
            Text("its area against uniform input is at most 1",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.25).next_to(cal_cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(req[0]), FadeIn(req[1], shift=UP * 0.2))      # beat 5

        # the integral condition
        intg = MathTex(r"\int_0^1", r"f(u)", r"\,du", r"\ \leq\ ", r"1")\
            .scale(1.1).next_to(req, DOWN, buff=0.4)
        intg[1].set_color(BACK); intg[4].set_color(RES)
        self.play_beat(Write(intg))                                        # beat 6

        # the smooth power-family calibrator
        self.play(FadeOut(VGroup(p_chip, e_chip, title, cal, cal_cap, req, intg)),
                  run_time=0.5)
        fam = MathTex(r"E", r"=", r"\kappa\,", r"p^{\,\kappa-1}",
                      r",\qquad", r"\kappa \in (0,1)").scale(1.2).shift(UP * 1.2)
        fam[0].set_color(EIG); fam[2].set_color(BACK); fam[3].set_color(VAR)
        fam[5].set_color(DIM)
        fam_cap = Text("the smooth power family", font_size=24, color=DIM)\
            .next_to(fam, UP, buff=0.3)
        self.play_beat(Write(fam), FadeIn(fam_cap))                        # beat 7

        # decay curve: payout grows as p -> 0
        ax = Axes(x_range=[0, 1, 0.25], y_range=[0, 5, 1],
                  x_length=5.6, y_length=2.4,
                  axis_config={"include_tip": False, "color": DIM,
                               "stroke_width": 2}).shift(DOWN * 1.4)
        xlab = MathTex("p", color=VAR).scale(0.7).next_to(ax.x_axis, RIGHT, buff=0.15)
        ylab = MathTex("E", color=EIG).scale(0.7).next_to(ax.y_axis, UP, buff=0.1)
        # kappa = 0.5: E = 0.5 * p^{-0.5}; clip near 0 for plotting
        curve = ax.plot(lambda x: 0.5 * x ** (-0.5), x_range=[0.01, 1], color=BACK,
                        stroke_width=4)
        grow = Text("small p, big E, no cliff", font_size=22, color=BACK)\
            .next_to(ax, RIGHT, buff=0.2)
        self.play_beat(Create(ax), FadeIn(xlab), FadeIn(ylab), Create(curve),
                       FadeIn(grow))                                       # beat 8

        # the integral equals exactly one
        check = MathTex(r"\int_0^1", r"\kappa\, u^{\,\kappa-1}", r"\,du", r"=", r"1")\
            .scale(0.9).to_edge(DOWN, buff=0.35)
        check[1].set_color(BACK); check[4].set_color(RES)
        self.play_beat(Write(check))                                       # beat 9

    def _chip(self, label, color):
        box = RoundedRectangle(width=2.4, height=0.7, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=22, color=color).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 3 — 1/E is a conservative p-value
# ----------------------------------------------------------------------
class S3_Conservative(NarratedScene):
    scene_key = "S3_Conservative"

    def construct(self):
        self.header("1/E as a p-value")

        defn = MathTex(r"p", r":=", r"\min", r"\big(", r"1", r",", r"\tfrac{1}{E}", r"\big)")\
            .scale(1.3).shift(UP * 2.0)
        defn[0].set_color(VAR); defn[6].set_color(EIG)
        always = Text("always a valid p-value", font_size=25, color=BACK)\
            .next_to(defn, DOWN, buff=0.3)
        self.play_beat(Write(defn), FadeIn(always))                        # beat 1

        # why valid: Markov
        markov = MathTex(r"\Pr_{H_0}", r"\big(", r"E", r"\geq", r"\tfrac{1}{\alpha}",
                         r"\big)", r"\ \leq\ ", r"\alpha")\
            .scale(1.0).next_to(always, DOWN, buff=0.5)
        markov[2].set_color(EIG); markov[4].set_color(RES); markov[7].set_color(RES)
        markov_cap = Text("Markov: rejecting when E reaches 1/alpha is a level-alpha test",
                          font_size=22, color=DIM).next_to(markov, DOWN, buff=0.25)
        self.play_beat(Write(markov), FadeIn(markov_cap))                  # beat 2

        # reading 1/E as the cut-off
        cut = MathTex(r"\alpha \geq \tfrac{1}{E}", r"\ \Rightarrow\ \text{reject}",
                      r";\quad", r"\text{cap at } 1")\
            .scale(0.85).next_to(markov_cap, DOWN, buff=0.4)
        cut[0].set_color(EIG); cut[1].set_color(RES)
        self.play_beat(Write(cut))                                         # beat 3

        # conservative
        self.play(FadeOut(VGroup(defn, always, markov, markov_cap, cut)),
                  run_time=0.5)
        cons = VGroup(
            Text("conservative", font_size=30, color=BAD),
            Text("a perfect p-value meets its bound with equality;",
                 font_size=24, color=WHITE),
            Text("this one under-reports its own significance.",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 2.0)
        self.play_beat(FadeIn(cons, lag_ratio=0.2))                        # beat 4

        # worked number: X=3 -> E ~ 12.18
        # decode the origin: the likelihood-ratio e-value for N(0,1) vs N(1,1)
        origin = MathTex(r"E", r"=", r"\tfrac{q(X)}{p(X)}", r"=",
                         r"\exp\!\big(X - \tfrac{1}{2}\big)")\
            .scale(0.85).next_to(cons, DOWN, buff=0.45)
        origin[0].set_color(EIG); origin[2].set_color(WHITE); origin[4].set_color(WHITE)
        origin_cap = Text("likelihood ratio, null N(0,1) vs alternative N(1,1)",
                          font_size=21, color=DIM).next_to(origin, DOWN, buff=0.18)
        worked = MathTex(r"E", r"=", r"\exp", r"\big(", r"3 - 0.5", r"\big)",
                         r"\approx", r"12.18").scale(1.0).next_to(origin_cap, DOWN, buff=0.35)
        worked[0].set_color(EIG); worked[7].set_color(EIG)
        worked_cap = Text("X = 3, three null-SDs out", font_size=22, color=DIM)\
            .next_to(worked, DOWN, buff=0.2)
        self.play_beat(Write(origin), FadeIn(origin_cap),
                       Write(worked), FadeIn(worked_cap))                  # beat 5

        # translate to p
        trans = MathTex(r"p", r"=", r"\min", r"\big(", r"1", r",", r"\tfrac{1}{12.18}",
                        r"\big)", r"\approx", r"0.082").scale(0.95)\
            .next_to(worked_cap, DOWN, buff=0.4)
        trans[0].set_color(VAR); trans[9].set_color(RES)
        self.play_beat(Write(trans))                                       # beat 6

        # the exact tail, 60x sharper
        self.play(FadeOut(VGroup(cons, worked, worked_cap)), run_time=0.4)
        compare = VGroup(
            VGroup(Text("e-value p", font_size=24, color=DIM),
                   MathTex(r"\approx 0.082", color=RES).scale(1.0)
                   ).arrange(DOWN, buff=0.12),
            MathTex(r"\text{vs}", color=DIM).scale(0.9),
            VGroup(Text("exact normal p", font_size=24, color=DIM),
                   MathTex(r"\approx 0.00135", color=BAD).scale(1.0)
                   ).arrange(DOWN, buff=0.12),
        ).arrange(RIGHT, buff=1.0).shift(UP * 0.6)
        gap = Text("sixty times more cautious", font_size=25, color=WHITE)\
            .next_to(compare, DOWN, buff=0.45)
        self.play_beat(FadeIn(compare, lag_ratio=0.2), FadeIn(gap),
                       trans.animate.shift(UP * 0.3).set_opacity(0.3))     # beat 7

        moral = Text("not a mistake: the conservative p stays valid even if\nthe model is wrong, which the exact tail does not",
                     font_size=24, color=BACK, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.5)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 8


# ----------------------------------------------------------------------
# Scene 4 — when each shines
# ----------------------------------------------------------------------
class S4_WhenEach(NarratedScene):
    scene_key = "S4_WhenEach"

    def construct(self):
        self.header("When each shines")

        intro = Text("it depends on the freedom you need",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # p-value column
        p_head = Text("p-value", font_size=30, color=VAR).shift(LEFT * 3.6 + UP * 1.6)
        p1 = Text("single, fixed, pre-registered test", font_size=22, color=WHITE)\
            .next_to(p_head, DOWN, buff=0.3)
        p2 = Text("clean parametric null  →  tight, sharp", font_size=22, color=WHITE)\
            .next_to(p1, DOWN, buff=0.2)
        self.play_beat(FadeIn(p_head), FadeIn(p1), FadeIn(p2))             # beat 2

        e_warn = Text("here, the e-value just leaves power on the table",
                      font_size=23, color=DIM).next_to(p2, DOWN, buff=0.35)\
            .align_to(p1, LEFT)
        self.play_beat(FadeIn(e_warn, shift=UP * 0.2))                     # beat 3

        # e-value column — three superpowers
        e_head = Text("e-value", font_size=30, color=EIG).shift(RIGHT * 3.6 + UP * 1.6)
        self.play(intro.animate.set_opacity(0.3))
        e1 = self._bullet("optional stopping: peek and halt anytime", BACK)\
            .next_to(e_head, DOWN, buff=0.3).align_to(e_head, LEFT)
        self.play_beat(FadeIn(e_head), FadeIn(e1, shift=RIGHT * 0.2))      # beat 4

        e2 = self._bullet("optional continuation: gather more, keep betting", BACK)\
            .next_to(e1, DOWN, buff=0.25).align_to(e1, LEFT)
        self.play_beat(FadeIn(e2, shift=RIGHT * 0.2))                      # beat 5

        e3 = self._bullet("combine dependent evidence: bets multiply", BACK)\
            .next_to(e2, DOWN, buff=0.25).align_to(e2, LEFT)
        self.play_beat(FadeIn(e3, shift=RIGHT * 0.2))                      # beat 6

        # the trade, stated plainly
        self.play(FadeOut(VGroup(intro, p_head, p1, p2, e_warn,
                                 e_head, e1, e2, e3)), run_time=0.5)
        trade = VGroup(
            Text("p-values: sharp but rigid", font_size=30, color=VAR),
            Text("e-values: a touch looser, but they travel", font_size=30, color=EIG),
        ).arrange(DOWN, buff=0.4)
        self.play_beat(FadeIn(trade[0]), FadeIn(trade[1], shift=UP * 0.2))  # beat 7

    def _bullet(self, label, color):
        dot = Dot(radius=0.06, color=color)
        t = Text(label, font_size=21, color=WHITE).next_to(dot, RIGHT, buff=0.2)
        return VGroup(dot, t)


# ----------------------------------------------------------------------
# Scene 5 — takeaway
# ----------------------------------------------------------------------
class S5_Takeaway(NarratedScene):
    scene_key = "S5_Takeaway"

    def construct(self):
        self.header("Takeaway")

        head = Text("two currencies for evidence",
                    font_size=34, color=WHITE).shift(UP * 2.5)
        self.play_beat(Write(head))                                        # beat 1

        # the two readings
        readings = VGroup(
            VGroup(Text("p-value", font_size=27, color=VAR),
                   Text("a tail probability — surprise", font_size=23, color=DIM)
                   ).arrange(DOWN, buff=0.12),
            VGroup(Text("e-value", font_size=27, color=EIG),
                   Text("a wealth multiplier — evidence that composes",
                        font_size=23, color=DIM)
                   ).arrange(DOWN, buff=0.12),
        ).arrange(DOWN, buff=0.5).shift(UP * 0.6)
        self.play_beat(FadeIn(readings[0]), FadeIn(readings[1], shift=UP * 0.2))  # beat 2

        # the bridge, both directions
        bridge = VGroup(
            MathTex(r"p = \min\big(1, \tfrac{1}{E}\big)").scale(0.95),
            MathTex(r"E = f(p)").scale(0.95),
        ).arrange(RIGHT, buff=1.2).next_to(readings, DOWN, buff=0.5)
        bridge[0].set_color(VAR); bridge[1].set_color(EIG)
        self.play_beat(Write(bridge))                                      # beat 3

        lossy = Text("the crossing is lossy — do not round-trip casually",
                     font_size=24, color=BAD).next_to(bridge, DOWN, buff=0.4)
        self.play_beat(FadeIn(lossy, shift=UP * 0.2))                      # beat 4

        # the deal in one sentence
        self.play(FadeOut(VGroup(head, readings, bridge, lossy)), run_time=0.5)
        deal = VGroup(
            Text("E-values trade a little power", font_size=30, color=WHITE),
            Text("for the freedom to peek, stop, and combine", font_size=30, color=RES),
            Text("without inflating error.", font_size=30, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        box = SurroundingRectangle(deal, color=RES, buff=0.3)
        self.play_beat(FadeIn(deal, lag_ratio=0.2), Create(box))           # beat 5

        nxt = Text("that freedom is the whole point of the chapters to come:\nwealth becomes a martingale you can watch, stop, and multiply",
                   font_size=24, color=BACK, line_spacing=0.8)\
            .next_to(box, DOWN, buff=0.5)
        self.play_beat(FadeIn(nxt, shift=UP * 0.2))                        # beat 6
