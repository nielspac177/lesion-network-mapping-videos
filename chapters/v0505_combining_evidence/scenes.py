"""v0505_combining_evidence — "Combining evidence".

Five narrated scenes on pooling e-values across studies. Define the inputs
E_1..E_K; prove the product is an e-value under independence (split-the-
expectation); prove the average is an e-value under ARBITRARY dependence (pure
linearity); contrast power vs robustness; close with the merging calculus.

All equations and numbers are quoted from:
  volumes/vol5_evalues/chapters/05_combining_evidence.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0505_combining_evidence ./render.sh \
      chapters/v0505_combining_evidence/scenes.py -q ql \
      S1_Goal S2_Product S3_Average S4_Tradeoff S5_Merge
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the goal: define the inputs E_1..E_K
# ----------------------------------------------------------------------
class S1_Goal(NarratedScene):
    scene_key = "S1_Goal"

    def construct(self):
        title = Text("Pooling many studies", font_size=42, color=WHITE)
        sub = Text("two cohorts, one number", font_size=24, color=DIM)\
            .next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # two cities, two e-values
        tor = self._chip("Toronto", r"E_1 = 4.0", VAR).shift(LEFT * 3.2 + UP * 0.9)
        seo = self._chip("Seoul", r"E_2 = 6.0", BACK).shift(RIGHT * 3.2 + UP * 0.9)
        self.play_beat(FadeIn(tor, shift=RIGHT * 0.2),
                       FadeIn(seo, shift=LEFT * 0.2))                       # beat 2

        # what an e-value is
        prop = MathTex(r"\mathbb{E}_P", r"[", "E", "]", r"\leq", "1")\
            .scale(1.2).shift(DOWN * 0.6)
        prop[2].set_color(VAR); prop[4].set_color(RES); prop[5].set_color(RES)
        br = Brace(prop, DOWN, color=DIM)
        br_lab = Text("under the null, a bet against \"nothing's going on\"",
                      font_size=22, color=DIM).next_to(br, DOWN, buff=0.2)
        self.play_beat(Write(prop), GrowFromCenter(br), FadeIn(br_lab))    # beat 3

        # payout reading
        payout = Text("payout of 20  =  you twentupled your stake  =  strong evidence",
                      font_size=24, color=RES).to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(payout, shift=UP * 0.2))                     # beat 4

        # name the inputs
        self.play(FadeOut(VGroup(tor, seo, prop, br, br_lab, payout)),
                  run_time=0.5)
        inputs = MathTex("E_1", ",", "E_2", ",", r"\dots", ",", "E_K")\
            .scale(1.5).shift(UP * 0.6)
        for i in (0, 2, 6):
            inputs[i].set_color(VAR)
        inbr = Brace(inputs, UP, color=DIM)
        inbr_lab = Text("K studies, one e-value each", font_size=24, color=DIM)\
            .next_to(inbr, UP, buff=0.2)
        self.play_beat(Write(inputs), GrowFromCenter(inbr),
                       FadeIn(inbr_lab))                                    # beat 5

        # the shared property
        defn = MathTex("E_i", r"\geq", "0", r"\quad\text{and}\quad",
                       r"\mathbb{E}_P", "[", "E_i", "]", r"\leq", "1")\
            .scale(1.0).next_to(inputs, DOWN, buff=0.9)
        defn[0].set_color(VAR); defn[6].set_color(VAR)
        defn[8].set_color(RES); defn[9].set_color(RES)
        only = Text("the only property we will use",
                    font_size=22, color=DIM).next_to(defn, DOWN, buff=0.3)
        self.play_beat(Write(defn), FadeIn(only))                          # beat 6

        # the fork ahead
        self.play(FadeOut(VGroup(inbr, inbr_lab, defn, only)), run_time=0.4)
        fork = VGroup(
            Text("MULTIPLY", font_size=30, color=VAR),
            Text("or", font_size=24, color=DIM),
            Text("AVERAGE", font_size=30, color=BACK),
        ).arrange(RIGHT, buff=0.8).next_to(inputs, DOWN, buff=0.9)
        forkcap = Text("which one depends entirely on independence",
                       font_size=24, color=RES).next_to(fork, DOWN, buff=0.35)
        self.play_beat(FadeIn(fork, lag_ratio=0.3), FadeIn(forkcap))       # beat 7

    def _chip(self, city, eq, color):
        box = RoundedRectangle(width=2.9, height=1.2, corner_radius=0.14,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.1)
        name = Text(city, font_size=22, color=color).move_to(box).shift(UP * 0.28)
        val = MathTex(eq, color=color).scale(0.9).move_to(box).shift(DOWN * 0.25)
        return VGroup(box, name, val)


# ----------------------------------------------------------------------
# Scene 2 — the product: independent e-values multiply
# ----------------------------------------------------------------------
class S2_Product(NarratedScene):
    scene_key = "S2_Product"

    def construct(self):
        self.header("Multiplying independent e-values")

        # casino parlay intro
        parlay = Text("re-bet the whole pot: $1 → $4 in Toronto → all $4 ride to Seoul",
                      font_size=25, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(parlay))                                     # beat 1

        # the product claim
        eq = MathTex(r"\prod_{i=1}^{K}", "E_i", "=", "E_1", "E_2",
                     r"\cdots", "E_K").scale(1.3).shift(UP * 1.2)
        for i in (1, 3, 4, 6):
            eq[i].set_color(VAR)
        claim = Text("for INDEPENDENT e-values, this product is again an e-value",
                     font_size=24, color=RES).next_to(eq, DOWN, buff=0.4)
        self.play_beat(Write(eq), FadeIn(claim),
                       parlay.animate.set_opacity(0.4))                    # beat 2

        # independence = factorization
        self.play(FadeOut(VGroup(parlay, claim)), run_time=0.4)
        indep = MathTex(r"\text{joint of }(E_1,\dots,E_K)", "=",
                        r"\prod_i \text{(marginals)}").scale(0.95)\
            .next_to(eq, DOWN, buff=0.5)
        indep[0].set_color(VAR)
        indep_cap = Text("knowing E sub one tells you nothing about E sub two",
                         font_size=23, color=DIM).next_to(indep, DOWN, buff=0.3)
        self.play_beat(Write(indep), FadeIn(indep_cap))                    # beat 3

        # what separate cohorts give
        sep = Text("separate cohorts: different patients, different scanners,\nno shared data, no shared peeking",
                   font_size=23, color=BACK, line_spacing=0.8)\
            .next_to(indep_cap, DOWN, buff=0.4)
        self.play_beat(FadeIn(sep, shift=UP * 0.2))                        # beat 4

        # step 1 — split the expectation
        self.play(FadeOut(VGroup(eq, indep, indep_cap, sep)), run_time=0.5)
        s1 = MathTex(r"\mathbb{E}_P\!\left[\prod_{i=1}^{K} E_i\right]", "=",
                     r"\prod_{i=1}^{K}", r"\mathbb{E}_P[E_i]")\
            .scale(1.05).shift(UP * 1.3)
        s1[0].set_color(VAR); s1[3].set_color(VAR)
        s1tag = Text("Step 1 — independence splits the expectation",
                     font_size=23, color=DIM).next_to(s1, UP, buff=0.3)
        self.play_beat(Write(s1), FadeIn(s1tag))                           # beat 5

        # step 2 — bound each factor
        s2 = MathTex(r"\mathbb{E}_P[E_i]", r"\leq", "1")\
            .scale(1.05).next_to(s1, DOWN, buff=0.7)
        s2[0].set_color(VAR); s2[1].set_color(RES); s2[2].set_color(RES)
        s2tag = Text("Step 2 — each factor is an e-value",
                     font_size=22, color=DIM).next_to(s2, RIGHT, buff=0.5)
        self.play_beat(Write(s2), FadeIn(s2tag))                           # beat 6

        # step 3 — multiply the bounds
        s3 = MathTex(r"\prod_{i=1}^{K} \mathbb{E}_P[E_i]", r"\leq",
                     r"\prod_{i=1}^{K} 1", "=", "1")\
            .scale(1.05).next_to(s2, DOWN, buff=0.7)
        s3[1].set_color(RES); s3[3].set_color(RES); s3[4].set_color(RES)
        s3tag = Text("Step 3 — a product of numbers in [0,1] stays in [0,1]",
                     font_size=22, color=BACK).next_to(s3, DOWN, buff=0.3)
        self.play_beat(Write(s3), FadeIn(s3tag))                           # beat 7

        # worked number
        self.play(FadeOut(VGroup(s1, s1tag, s2, s2tag, s3, s3tag)),
                  run_time=0.5)
        worked = MathTex("E_1", r"\times", "E_2", "=", "4.0", r"\times",
                         "6.0", "=", "24.0").scale(1.3).shift(UP * 0.8)
        worked[0].set_color(VAR); worked[2].set_color(VAR); worked[8].set_color(RES)
        pval = MathTex("p", r"\leq", r"\tfrac{1}{E}", "=", r"\tfrac{1}{24}",
                       r"\approx", "0.042").scale(1.1).next_to(worked, DOWN, buff=0.6)
        pval[6].set_color(RES)
        self.play_beat(Write(worked), Write(pval))                         # beat 8

        # = the Ch.3 martingale
        mart = Text("this running product IS the Ch.3 test martingale —\nmultiply across sites, peek across time: same object",
                    font_size=24, color=BACK, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(mart, shift=UP * 0.2))                       # beat 9


# ----------------------------------------------------------------------
# Scene 3 — the average: arbitrary dependence
# ----------------------------------------------------------------------
class S3_Average(NarratedScene):
    scene_key = "S3_Average"

    def construct(self):
        self.header("Averaging arbitrary e-values")

        # the danger
        danger = Text("the product is only as honest as the independence claim",
                      font_size=27, color=BAD).shift(UP * 2.6)
        sub = Text("share patients → you parlay the same fluke twice",
                   font_size=23, color=DIM).next_to(danger, DOWN, buff=0.25)
        self.play_beat(FadeIn(danger), FadeIn(sub))                        # beat 1

        # counterexample: E itself is valid
        ce = MathTex("E", "=", "4", r"\ \text{w.p.}\ ", r"\tfrac14", ",",
                     r"\quad 0\ \text{w.p.}\ ", r"\tfrac34").scale(1.0)\
            .shift(UP * 1.0)
        ce[0].set_color(VAR)
        cev = MathTex(r"\mathbb{E}[E]", "=", r"\tfrac14\cdot 4 + \tfrac34\cdot 0",
                      "=", "1").scale(0.95).next_to(ce, DOWN, buff=0.35)
        cev[4].set_color(BACK)
        self.play_beat(Write(ce), Write(cev),
                       danger.animate.set_opacity(0.4),
                       sub.animate.set_opacity(0.4))                       # beat 2

        # but E^2 has mean 4 > 1
        ce2 = MathTex(r"\mathbb{E}[E^2]", "=", r"\tfrac14\cdot 16", "=",
                      "4", ">", "1").scale(1.1).next_to(cev, DOWN, buff=0.5)
        ce2[4].set_color(BAD); ce2[5].set_color(BAD); ce2[6].set_color(BAD)
        ce2cap = Text("the product is NOT an e-value any more",
                      font_size=23, color=BAD).next_to(ce2, DOWN, buff=0.25)
        self.play_beat(Write(ce2), FadeIn(ce2cap))                         # beat 3

        # the average, always safe
        self.play(FadeOut(VGroup(danger, sub, ce, cev, ce2, ce2cap)),
                  run_time=0.5)
        avg = MathTex(r"\bar{E}", "=", r"\frac{1}{K}", r"\sum_{i=1}^{K}", "E_i")\
            .scale(1.4).shift(UP * 1.3)
        avg[0].set_color(BACK); avg[4].set_color(VAR)
        avgcap = Text("split your stake across the tables — always safe",
                      font_size=24, color=BACK).next_to(avg, DOWN, buff=0.4)
        self.play_beat(Write(avg), FadeIn(avgcap))                         # beat 4

        # one word: linearity
        lin = MathTex(r"\mathbb{E}_P\!\left[\tfrac1K\sum_i E_i\right]", "=",
                      r"\tfrac1K\sum_i", r"\mathbb{E}_P[E_i]")\
            .scale(1.0).next_to(avgcap, DOWN, buff=0.6)
        lin[0].set_color(BACK); lin[3].set_color(VAR)
        lintag = Text("linearity — true for ANY variables, dependent or not",
                      font_size=23, color=DIM).next_to(lin, DOWN, buff=0.3)
        self.play_beat(Write(lin), FadeIn(lintag))                         # beat 5

        # bound and finish
        fin = MathTex(r"\tfrac1K\sum_i \mathbb{E}_P[E_i]", r"\leq",
                      r"\tfrac1K\sum_i 1", "=", r"\tfrac1K\cdot K", "=", "1")\
            .scale(0.95).next_to(lin, DOWN, buff=0.5)
        fin[1].set_color(RES); fin[6].set_color(RES)
        self.play_beat(Write(fin))                                         # beat 6

        # the price of safety
        self.play(FadeOut(VGroup(avg, avgcap, lin, lintag, fin)),
                  run_time=0.5)
        price = MathTex(r"\bar{E}", "=", r"\tfrac12(4+6)", "=", "5.0",
                        r"\quad\text{vs}\quad", r"\text{product } 24")\
            .scale(1.1).shift(UP * 0.7)
        price[0].set_color(BACK); price[4].set_color(BACK); price[6].set_color(VAR)
        between = Text("always between the inputs, never above the maximum",
                       font_size=24, color=DIM).next_to(price, DOWN, buff=0.45)
        self.play_beat(Write(price), FadeIn(between))                      # beat 7

        # the trade
        trade = Text("the average refuses to be fooled —\nbut it cannot reward genuine replication like a legitimate parlay",
                     font_size=24, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(trade, shift=UP * 0.2))                      # beat 8


# ----------------------------------------------------------------------
# Scene 4 — product vs average tradeoff
# ----------------------------------------------------------------------
class S4_Tradeoff(NarratedScene):
    scene_key = "S4_Tradeoff"

    def construct(self):
        self.header("Product vs average")

        intro = Text("same question, opposite temperaments",
                     font_size=28, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # build two columns
        prod_head = Text("PRODUCT", font_size=30, color=VAR)
        avg_head = Text("AVERAGE", font_size=30, color=BACK)
        prod_head.shift(LEFT * 3.4 + UP * 1.7)
        avg_head.shift(RIGHT * 3.4 + UP * 1.7)
        prod_eq = MathTex(r"\prod_i E_i", color=VAR).scale(0.9)\
            .next_to(prod_head, DOWN, buff=0.25)
        avg_eq = MathTex(r"\tfrac1K\sum_i E_i", color=BACK).scale(0.9)\
            .next_to(avg_head, DOWN, buff=0.25)
        vline = Line(UP * 2.0, DOWN * 2.4, color=DIM, stroke_width=1)
        self.play_beat(FadeIn(prod_head), FadeIn(avg_head),
                       Write(prod_eq), Write(avg_eq), Create(vline),
                       intro.animate.set_opacity(0.35))                    # beat 2

        # product powerful
        p_pow = VGroup(
            Text("+ powerful", font_size=24, color=RES),
            Text("two positives compound:", font_size=22, color=WHITE),
            Text("24 is replication at work", font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        p_pow.next_to(prod_eq, DOWN, buff=0.5).align_to(prod_eq, LEFT).shift(LEFT * 0.6)
        self.play_beat(FadeIn(p_pow, shift=UP * 0.2))                      # beat 3

        # average robust
        a_rob = VGroup(
            Text("+ robust", font_size=24, color=RES),
            Text("valid under ANY", font_size=22, color=WHITE),
            Text("dependence at all", font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        a_rob.next_to(avg_eq, DOWN, buff=0.5).align_to(avg_eq, LEFT).shift(LEFT * 0.4)
        self.play_beat(FadeIn(a_rob, shift=UP * 0.2))                      # beat 4

        # the costs
        p_cost = Text("– fragile: needs independence",
                      font_size=22, color=BAD).next_to(p_pow, DOWN, buff=0.4)\
            .align_to(p_pow, LEFT)
        a_cost = Text("– conservative: never\n  beats a parlay",
                      font_size=22, color=BAD, line_spacing=0.8)\
            .next_to(a_rob, DOWN, buff=0.4).align_to(a_rob, LEFT)
        self.play_beat(FadeIn(p_cost), FadeIn(a_cost))                     # beat 5

        # the rule, part 1
        self.play(FadeOut(VGroup(intro, prod_head, avg_head, prod_eq, avg_eq,
                                 vline, p_pow, a_rob, p_cost, a_cost)),
                  run_time=0.5)
        rule1 = VGroup(
            Text("Separate cohorts —", font_size=27, color=VAR),
            Text("no shared patients, no shared peeking", font_size=24, color=WHITE),
            Text("→  MULTIPLY  (clean replication)", font_size=26, color=VAR),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.9)
        self.play_beat(FadeIn(rule1, lag_ratio=0.25))                      # beat 6

        # the rule, part 2
        rule2 = VGroup(
            Text("Any doubt about shared data or selection —", font_size=27, color=BACK),
            Text("→  AVERAGE", font_size=26, color=BACK),
            Text("when unsure, average: never wrong, only cautious",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.22).next_to(rule1, DOWN, buff=0.7)
        self.play_beat(FadeIn(rule2, lag_ratio=0.25))                      # beat 7


# ----------------------------------------------------------------------
# Scene 5 — merging is closed (the takeaway of the volume)
# ----------------------------------------------------------------------
class S5_Merge(NarratedScene):
    scene_key = "S5_Merge"

    def construct(self):
        self.header("Merging is closed")

        head = Text("a closed, composable calculus of evidence",
                    font_size=30, color=RES).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                       # beat 1

        # closure: e-values in, e-value out
        close = MathTex(r"\underbrace{E_1,\dots,E_K}_{\text{e-values}}",
                        r"\;\longmapsto\;",
                        r"\underbrace{\textstyle\prod_i E_i \;\text{or}\; \tfrac1K\sum_i E_i}_{\text{again an e-value}}")\
            .scale(0.95).shift(UP * 1.1)
        close[0].set_color(VAR); close[2].set_color(BACK)
        self.play_beat(Write(close))                                       # beat 2

        # keep going
        chain = VGroup(
            Text("Toronto × Seoul", font_size=24, color=WHITE),
            Text("→", font_size=24, color=DIM),
            Text("fold in Boston", font_size=24, color=WHITE),
            Text("→", font_size=24, color=DIM),
            Text("next year's cohort", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.35).next_to(close, DOWN, buff=0.6)
        chaincap = Text("the chain never leaves the family",
                        font_size=23, color=DIM).next_to(chain, DOWN, buff=0.3)
        self.play_beat(FadeIn(chain, lag_ratio=0.2), FadeIn(chaincap))     # beat 3

        # across time = martingale
        self.play(FadeOut(VGroup(close, chain, chaincap)), run_time=0.5)
        across = MathTex(r"M_k = \prod_{i\leq k} E_i",
                         r"\;\Rightarrow\;",
                         r"\text{Ville + safe peeking, free}")\
            .scale(1.0).shift(UP * 1.2)
        across[0].set_color(VAR); across[2].set_color(BACK)
        self.play_beat(Write(across), head.animate.set_opacity(0.35))      # beat 4

        # p-values cannot
        pv = Text("p-values cannot be merged this freely:\nno running-product structure, no clean pooling under dependence",
                  font_size=24, color=BAD, line_spacing=0.8)\
            .next_to(across, DOWN, buff=0.6)
        self.play_beat(FadeIn(pv, shift=UP * 0.2))                         # beat 5

        # guardrail: shared null
        guard = Text("guardrail: a combiner is only as good as the shared null —\nmultiplying e-values for different claims answers neither",
                     font_size=23, color=RES, line_spacing=0.8)\
            .next_to(pv, DOWN, buff=0.5)
        self.play_beat(FadeIn(guard, shift=UP * 0.2))                      # beat 6

        # report alongside Vol 4
        self.play(FadeOut(VGroup(across, pv, guard)), run_time=0.5)
        along = VGroup(
            Text("report ALONGSIDE the within-map", font_size=25, color=WHITE),
            Text("permutation maps (Vol 4) — never instead", font_size=25, color=WHITE),
            Text("the two layers are orthogonal", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.0)
        self.play_beat(FadeIn(along, lag_ratio=0.2))                       # beat 7

        # the moral
        moral = VGroup(
            Text("E-values compose.", font_size=30, color=WHITE),
            Text("Evidence accumulates.", font_size=30, color=WHITE),
            Text("And the average is the number you can never get wrong.",
                 font_size=28, color=RES),
        ).arrange(DOWN, buff=0.32).next_to(along, DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 8
