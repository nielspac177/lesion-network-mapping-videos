"""v0507_recipe_and_limits — "E-values: recipe and limits".

Five narrated scenes closing Volume 5. Assemble the six pieces into one
end-to-end recipe (E8), say when the e-value layer earns its keep, then draw
the three honest fences (E7): the power cost, a valid e-value of the WRONG null,
and the fact that the whole stack rests on E[e] <= 1 under the null.

All equations/numbers are quoted from:
  volumes/vol5_evalues/chapters/07_recipe_and_limits.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0507_recipe_and_limits ./render.sh \
      chapters/v0507_recipe_and_limits/scenes.py -q ql \
      S1_Recipe S2_WhenWorth S3_Limit_power S4_Limit_wrongnull S5_Close
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the recipe (E8): one flow diagram
# ----------------------------------------------------------------------
class S1_Recipe(NarratedScene):
    scene_key = "S1_Recipe"

    def construct(self):
        self.header("The recipe  (Result E8)")

        intro = Text("six pieces, bolted into one pipeline",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # Step 1 — MINT
        mint = self._step("1.  MINT", "one e-value per analysis cell", VAR)
        mint.shift(UP * 1.2)
        ei = MathTex(r"e_i", r"\ge", "0", r",\qquad",
                     r"\mathbb{E}_{H_0}", r"[\,e_i\,]", r"\leq", "1")\
            .scale(0.95).next_to(mint, DOWN, buff=0.35)
        ei[0].set_color(VAR); ei[7].set_color(RES)
        self.play_beat(FadeIn(mint, shift=UP * 0.2), intro.animate.set_opacity(0.4))  # beat 2
        # decode the e-value object as we Write it
        self.play_beat(Write(ei))                                         # beat 3

        # the two roads to mint
        self.play(FadeOut(VGroup(mint, ei)), run_time=0.4)
        calib = MathTex(r"e_i", "=", r"\kappa", r"\,p_i^{\,\kappa-1}")\
            .scale(1.0).shift(UP * 1.4 + LEFT * 2.6)
        calib[0].set_color(VAR); calib[2].set_color(EIG); calib[3].set_color(WHITE)
        calib_lab = Text("calibrate a permutation p-value\n(integrates to 1 over a uniform p)",
                         font_size=20, color=DIM, line_spacing=0.8)\
            .next_to(calib, DOWN, buff=0.25)
        uirow = MathTex(r"U_i", r"\ \ \text{(split-LRT)}")\
            .scale(1.0).shift(UP * 1.4 + RIGHT * 2.8)
        uirow[0].set_color(VAR)
        ui_lab = Text("universal inference\nwhere a likelihood exists",
                      font_size=20, color=DIM, line_spacing=0.8)\
            .next_to(uirow, DOWN, buff=0.25)
        roads = VGroup(calib, calib_lab, uirow, ui_lab)
        self.play_beat(FadeIn(roads, lag_ratio=0.2))                      # beat 4

        # Step 2 — e-BH
        self.play(roads.animate.scale(0.55).to_edge(UP, buff=1.0).set_opacity(0.5),
                  run_time=0.5)
        ebh = MathTex(r"k^{\star}", "=", r"\max\Big\{k:\ ",
                      r"e_{(k)}", r"\geq", r"\frac{m}{\alpha\,k}", r"\Big\}")\
            .scale(1.0).shift(UP * 0.1)
        ebh[0].set_color(RES); ebh[3].set_color(VAR); ebh[5].set_color(EIG)
        ebh_key = MathTex(r"m=\#\text{cells}", r",\ \ ",
                          r"\alpha=\text{FDR level}", r",\ \ ",
                          r"e_{(k)}=k\text{-th largest e-value}")\
            .scale(0.5).next_to(ebh, UP, buff=0.3)
        ebh_key[0].set_color(EIG); ebh_key[2].set_color(EIG); ebh_key[4].set_color(VAR)
        ebh_lab = Text("2.  e-BH:  sort descending, reject the top k*\n"
                       "FDR ≤ α under ARBITRARY dependence",
                       font_size=22, color=WHITE, line_spacing=0.8)\
            .next_to(ebh, DOWN, buff=0.35)
        ebh_lab[0].set_color(WHITE)
        self.play_beat(Write(ebh), FadeIn(ebh_key), FadeIn(ebh_lab))      # beat 5

        # Step 3 — accumulate across cohorts
        self.play(FadeOut(VGroup(ebh, ebh_lab)), run_time=0.4)
        acc = VGroup(
            Text("3.  POOL across sites and time", font_size=24, color=BACK),
            MathTex(r"\text{independent:}\ ", r"E_{1}\cdot E_{2}",
                    r"\qquad\text{dependent:}\ ", r"\tfrac12(E_1+E_2)").scale(0.85),
            Text("live accrual → running product is a martingale (Ville: stop anytime)",
                 font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.3)
        acc[1][1].set_color(VAR); acc[1][3].set_color(VAR)
        self.play_beat(FadeIn(acc, lag_ratio=0.2))                        # beat 6

        # Step 4 — report alongside
        self.play(FadeOut(acc), run_time=0.4)
        rep = VGroup(
            Text("4.  REPORT alongside the FWE maps", font_size=26, color=RES),
            Text("e-value layer = across-analyses accountant", font_size=22, color=DIM),
            Text("within-map permutation = the referee  —  keep both",
                 font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.28)
        self.play_beat(FadeIn(rep, shift=UP * 0.2))                       # beat 7

        # moral: no new math
        self.play(FadeOut(rep), run_time=0.4)
        moral = Text("No new mathematics —\n"
                     "calibrator + e-BH + product/average + martingale, composed.",
                     font_size=26, color=WHITE, line_spacing=0.9)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                      # beat 8

    def _step(self, head, sub, color):
        return VGroup(
            Text(head, font_size=28, color=color),
            Text(sub, font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.18)


# ----------------------------------------------------------------------
# Scene 2 — when e-values are worth it
# ----------------------------------------------------------------------
class S2_WhenWorth(NarratedScene):
    scene_key = "S2_WhenWorth"

    def construct(self):
        self.header("When e-values are worth it")

        intro = Text("three situations — and one where they are not",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # worth-it #1: optional stopping
        w1 = VGroup(
            Text("✓  optional stopping", font_size=25, color=BACK),
            MathTex(r"\text{running product is a martingale}\ \Rightarrow\ "
                    r"\text{stop at}\ E \geq \tfrac{1}{\alpha}").scale(0.8),
        ).arrange(DOWN, buff=0.18).shift(UP * 1.5)
        self.play_beat(FadeIn(w1, shift=UP * 0.2))                        # beat 2

        # worth-it #2: dependence-robust multiple testing
        w2 = VGroup(
            Text("✓  dependence-robust multiple testing", font_size=25, color=BACK),
            Text("e-BH holds FDR ≤ α under ANY dependence",
                 font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.18).next_to(w1, DOWN, buff=0.4)
        self.play_beat(FadeIn(w2, shift=UP * 0.2))                        # beat 3

        # worth-it #3: composite / no regularity
        w3 = VGroup(
            Text("✓  composite nulls, no regularity conditions", font_size=25, color=BACK),
            Text("universal inference mints E from a likelihood, no asymptotics",
                 font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.18).next_to(w2, DOWN, buff=0.4)
        self.play_beat(FadeIn(w3, shift=UP * 0.2))                        # beat 4

        # the worked sweep: e-BH rejects 0, BH rejects 2
        self.play(FadeOut(VGroup(intro, w1, w2, w3)), run_time=0.5)
        compare = VGroup(
            VGroup(
                Text("e-BH", font_size=26, color=RES),
                Text("rejects 0 / 5", font_size=24, color=DIM),
            ).arrange(DOWN, buff=0.15),
            MathTex(r"\text{vs}", color=DIM).scale(0.9),
            VGroup(
                Text("plain BH", font_size=26, color=BAD),
                Text("rejects cells 1, 2", font_size=24, color=DIM),
            ).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=1.1).shift(UP * 1.1)
        sweep_cap = Text("worked m = 5 sweep,  α = 0.05",
                         font_size=22, color=DIM).next_to(compare, UP, buff=0.4)
        self.play_beat(FadeIn(compare, lag_ratio=0.2), FadeIn(sweep_cap))  # beat 5

        # the gap = premium for robustness
        gap = Text("the gap is the premium:\nno dependence assumption → a more conservative threshold",
                   font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(compare, DOWN, buff=0.6)
        self.play_beat(FadeIn(gap, shift=UP * 0.2))                       # beat 6

        # NOT worth it
        self.play(FadeOut(VGroup(compare, sweep_cap, gap)), run_time=0.5)
        notworth = VGroup(
            Text("✗  NOT worth the power loss", font_size=27, color=BAD),
            Text("a single, fixed, clean test with a defensible\nindependence assumption — use the ordinary p-value",
                 font_size=25, color=WHITE, line_spacing=0.85),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(notworth, shift=UP * 0.2))                  # beat 7


# ----------------------------------------------------------------------
# Scene 3 — the power cost (calibrator intuition)
# ----------------------------------------------------------------------
class S3_Limit_power(NarratedScene):
    scene_key = "S3_Limit_power"

    def construct(self):
        self.header("The power cost  (Limit, E7)")

        head = Text("e-values are typically LESS powerful\nthan the optimal fixed-n p-value",
                    font_size=28, color=RES, line_spacing=0.85).shift(UP * 2.2)
        self.play_beat(FadeIn(head))                                      # beat 1

        # the calibrator definition
        calib = MathTex("f", r":", "[0,1]", r"\to", r"[0,\infty)",
                        r",\quad f\ \text{non-increasing}")\
            .scale(0.95).shift(UP * 0.6)
        calib[0].set_color(VAR)
        self.play_beat(Write(calib), head.animate.scale(0.7).to_edge(UP, buff=1.1))  # beat 2

        # the integral budget
        budget = MathTex(r"\int_0^1", "f(p)", r"\,dp", r"\ \leq\ ", "1")\
            .scale(1.1).next_to(calib, DOWN, buff=0.6)
        budget[1].set_color(VAR); budget[4].set_color(RES)
        bbrace = Brace(budget, DOWN, color=DIM)
        blab = Text("a budget: large on small p must be paid for elsewhere",
                    font_size=22, color=DIM).next_to(bbrace, DOWN, buff=0.2)
        self.play_beat(Write(budget), GrowFromCenter(bbrace), FadeIn(blab))  # beat 3

        # the workhorse, with the worked number
        self.play(FadeOut(VGroup(budget, bbrace, blab, calib)), run_time=0.5)
        work = MathTex("f(p)", "=", r"\kappa", r"\,p^{\,\kappa-1}",
                       r"\quad\Rightarrow\quad",
                       r"p=0.04", r"\ \mapsto\ ", "e=2.5")\
            .scale(0.95).shift(UP * 0.4)
        work[0].set_color(VAR); work[2].set_color(EIG)
        work[7].set_color(BAD)
        kcap = Text("with κ = ½  (the workhorse calibrator)",
                    font_size=22, color=DIM).next_to(work, DOWN, buff=0.35)
        self.play_beat(Write(work), FadeIn(kcap))                         # beat 4

        # softer statement
        softer = Text("2.5 is real evidence — but a SOFTER statement\nthan the p-value 0.04 was.  The conversion gives ground.",
                      font_size=24, color=WHITE, line_spacing=0.85)\
            .next_to(kcap, DOWN, buff=0.5)
        self.play_beat(FadeIn(softer, shift=UP * 0.2))                    # beat 5

        # pick kappa before looking
        self.play(FadeOut(VGroup(head, work, kcap, softer)), run_time=0.5)
        pre = VGroup(
            Text("pick κ BEFORE looking", font_size=27, color=RES),
            Text("tuning κ to maximize e afterward\nbreaks the integral bound — the very thing that made it valid",
                 font_size=24, color=WHITE, line_spacing=0.85),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.6)
        self.play_beat(FadeIn(pre, shift=UP * 0.2))                       # beat 6

        # moral: the cost buys two gifts
        moral = VGroup(
            Text("the power cost buys two gifts:", font_size=25, color=DIM),
            Text("stop whenever you like  •  combine across anything",
                 font_size=25, color=BACK),
            Text("a single clean test needs neither", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.25).next_to(pre, DOWN, buff=0.55)
        self.play_beat(FadeIn(moral, lag_ratio=0.25))                     # beat 7


# ----------------------------------------------------------------------
# Scene 4 — a wrong null still misleads
# ----------------------------------------------------------------------
class S4_Limit_wrongnull(NarratedScene):
    scene_key = "S4_Limit_wrongnull"

    def construct(self):
        self.header("A wrong null still misleads  (Limit, E7)")

        head = Text("a valid e-value of the WRONG null\nis still the wrong question",
                    font_size=28, color=RES, line_spacing=0.85).shift(UP * 2.3)
        self.play_beat(FadeIn(head))                                      # beat 1

        # the conditional property
        prop = MathTex(r"\mathbb{E}_{P}", "[", "E", "]", r"\ \leq\ ", "1",
                       r"\quad\text{for every}\ ", "P", r"\in", "H_0")\
            .scale(1.05).shift(UP * 0.7)
        prop[2].set_color(VAR); prop[5].set_color(RES); prop[9].set_color(BACK)
        pcap = Text("validity is relative to H₀ — it says nothing\nabout whether H₀ is the RIGHT null",
                    font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(prop, DOWN, buff=0.4)
        self.play_beat(Write(prop), FadeIn(pcap),
                       head.animate.scale(0.7).to_edge(UP, buff=1.1))     # beat 2

        # the confounded story
        self.play(FadeOut(VGroup(prop, pcap)), run_time=0.4)
        story = VGroup(
            Text("lesion SIZE confounds the ataxia effect", font_size=25, color=WHITE),
            Text("you mint an e-value whose null IGNORES size",
                 font_size=25, color=BAD),
            Text("the machinery works flawlessly:  𝔼[E] ≤ 1 under that null",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.28).shift(UP * 0.4)
        self.play_beat(FadeIn(story, lag_ratio=0.25))                     # beat 3

        # big E, false declaration
        self.play(FadeOut(story), run_time=0.4)
        bigE = MathTex(r"E = 40", r"\ \Rightarrow\ ",
                       r"\text{``discovery''}").scale(1.1).shift(UP * 0.9)
        bigE[0].set_color(VAR); bigE[2].set_color(BAD)
        reads = Text("but a big E says only:\n“the data are surprising IF the network is noise AND size doesn't matter”",
                     font_size=23, color=WHITE, line_spacing=0.85)\
            .next_to(bigE, DOWN, buff=0.5)
        self.play_beat(Write(bigE), FadeIn(reads))                        # beat 4

        # size matters -> strawman
        straw = Text("and the data ARE surprising — because size matters.\n"
                     "you measured strong evidence against a strawman.",
                     font_size=24, color=BAD, line_spacing=0.85)\
            .next_to(reads, DOWN, buff=0.45)
        self.play_beat(FadeIn(straw, shift=UP * 0.2))                     # beat 5

        # validity != correctness
        self.play(FadeOut(VGroup(head, bigE, reads, straw)), run_time=0.5)
        vc = VGroup(
            VGroup(
                Text("VALIDITY", font_size=26, color=BACK),
                Text("𝔼[E] ≤ 1 under H₀", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.12),
            MathTex(r"\perp", color=RES).scale(1.4),
            VGroup(
                Text("CORRECTNESS", font_size=26, color=RES),
                Text("H₀ is the right null", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.12),
        ).arrange(RIGHT, buff=1.0).shift(UP * 1.0)
        cooked = Text("the arithmetic is right; the books are cooked",
                      font_size=24, color=WHITE).next_to(vc, DOWN, buff=0.5)
        self.play_beat(FadeIn(vc, lag_ratio=0.2), FadeIn(cooked))         # beat 6

        # the fix lives upstream
        fix = VGroup(
            Text("the fix lives upstream:", font_size=24, color=DIM),
            Text("design matrix + Freedman-Lane → permute under the partial null",
                 font_size=24, color=WHITE),
            Text("the e-value inherits the null's confound-handling; it adds none",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.22).next_to(cooked, DOWN, buff=0.5)
        self.play_beat(FadeIn(fix, lag_ratio=0.2))                        # beat 7

        # worse: bound itself can fail -> whole stack snaps
        self.play(FadeOut(VGroup(vc, cooked, fix)), run_time=0.5)
        snap = MathTex(r"\mathrm{FDR}", r"\ \leq\ ",
                       r"\frac{\alpha}{m}\sum_{i\in\mathcal{H}_0}",
                       r"\mathbb{E}[e_i]", r"\ \leq\ ", r"\alpha")\
            .scale(1.0).shift(UP * 0.4)
        snap[0].set_color(RES); snap[3].set_color(VAR); snap[5].set_color(EIG)
        snap_key = MathTex(r"m=\#\text{cells}", r",\ \ ",
                           r"\alpha=\text{FDR level}", r",\ \ ",
                           r"\mathcal{H}_0=\text{true-null cells}")\
            .scale(0.5).next_to(snap, UP, buff=0.3)
        snap_key[0].set_color(EIG); snap_key[2].set_color(EIG); snap_key[4].set_color(BACK)
        snaplab = Text("mis-specify the null and 𝔼[eᵢ] > 1:\n"
                       "the chain snaps here — e-BH, Ville, and Markov all fall with it",
                       font_size=23, color=BAD, line_spacing=0.85)\
            .next_to(snap, DOWN, buff=0.5)
        self.play_beat(Write(snap), FadeIn(snap_key), FadeIn(snaplab))    # beat 8


# ----------------------------------------------------------------------
# Scene 5 — closing
# ----------------------------------------------------------------------
class S5_Close(NarratedScene):
    scene_key = "S5_Close"

    def construct(self):
        self.header("Closing")

        head = Text("e-values: a robust, composable\nevidence currency",
                    font_size=34, color=WHITE, line_spacing=0.85).shift(UP * 2.0)
        self.play_beat(FadeIn(head))                                      # beat 1

        # the guarantees
        gua = VGroup(
            Text("•  anytime-validity — peek freely", font_size=25, color=BACK),
            Text("•  e-BH — FDR ≤ α under ANY dependence", font_size=25, color=BACK),
            Text("•  universal inference — no regularity needed", font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).shift(UP * 0.1)
        self.play_beat(FadeIn(gua, lag_ratio=0.2),
                       head.animate.scale(0.62).to_edge(UP, buff=1.0))    # beat 2

        # all rest on one inequality
        self.play(FadeOut(gua), run_time=0.4)
        spine = MathTex(r"\mathbb{E}_{H_0}", "[", "E", "]", r"\ \leq\ ", "1")\
            .scale(1.4).shift(UP * 0.5)
        spine[2].set_color(VAR); spine[5].set_color(RES)
        box = SurroundingRectangle(spine, color=RES, buff=0.25)
        spcap = Text("every guarantee is a corollary of this one inequality",
                     font_size=24, color=DIM).next_to(box, DOWN, buff=0.4)
        self.play_beat(Write(spine), Create(box), FadeIn(spcap))          # beat 3

        # spend skepticism on the null
        skept = Text("spend your skepticism on each cell's null —\n"
                     "the combiners are bookkeeping, not guarantees",
                     font_size=25, color=WHITE, line_spacing=0.85)\
            .next_to(spcap, DOWN, buff=0.55)
        self.play_beat(FadeIn(skept, shift=UP * 0.2))                     # beat 4

        # they don't rescue a bad question
        self.play(FadeOut(VGroup(head, spine, box, spcap, skept)), run_time=0.5)
        bad = Text("they do NOT rescue a bad question:\n"
                   "a valid bet against the wrong null is worthless",
                   font_size=27, color=BAD, line_spacing=0.85).shift(UP * 1.2)
        self.play_beat(FadeIn(bad, shift=UP * 0.2))                       # beat 5

        # but they make honest inference possible
        good = VGroup(
            Text("what they DO give:", font_size=25, color=DIM),
            Text("honest sequential and multiple inference —",
                 font_size=27, color=RES),
            Text("stop when convinced, weigh many analyses,\nwithout lying about the evidence",
                 font_size=25, color=WHITE, line_spacing=0.85),
        ).arrange(DOWN, buff=0.3).next_to(bad, DOWN, buff=0.7)
        self.play_beat(FadeIn(good, lag_ratio=0.25))                      # beat 6
