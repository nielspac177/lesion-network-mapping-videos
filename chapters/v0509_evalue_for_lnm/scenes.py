"""v0509_evalue_for_lnm — "An e-value version of the LNM symptom null".

Six narrated scenes. We recall the symptom-label permutation null (Part 5),
build its e-value twin as a permutation calibrator E = |G| * 1[T_obs is top],
show the backbone cancels exactly as before, motivate the e-value by
anytime-valid multiplication across cohorts, lift it across voxels with e-BH
under arbitrary spatial dependence, and close with the scope caveat: this is an
illustrative construction [verify against primary source], and a wrong null is
still wrong.

All equations/numbers are sourced from:
  volumes/vol5_evalues/chapters/01_what_is_an_evalue.md
  responses/lnm_critique/sections/03_the_right_null.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0509_evalue_for_lnm ./render.sh \
      chapters/v0509_evalue_for_lnm/scenes.py -q ql \
      S1_Recall S2_BetOnContrast S3_BackboneStill S4_Sequential \
      S5_MultipleVoxels S6_Caveat
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — recall the symptom-label permutation null
# ----------------------------------------------------------------------
class S1_Recall(NarratedScene):
    scene_key = "S1_Recall"

    def construct(self):
        title = Text("Recall the symptom null", font_size=42, color=WHITE)
        sub = Text("from Part 5 — now we make its e-value twin",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))            # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # the setup: x_i, y_i
        setup = MathTex(r"x_i \in \mathbb{R}^V", r"\qquad y_i \in \{0, 1\}")\
            .scale(1.1).shift(UP * 1.3)
        setup[0].set_color(VAR); setup[1].set_color(EIG)
        bx = Brace(setup[0], DOWN, color=VAR)
        bx_l = Text("fixed lesion-connectivity map", font_size=22, color=VAR)\
            .next_to(bx, DOWN, buff=0.15)
        by = Brace(setup[1], DOWN, color=EIG)
        by_l = Text("symptom label: impaired / spared", font_size=22, color=EIG)\
            .next_to(by, DOWN, buff=0.15)
        self.play_beat(Write(setup),
                       GrowFromCenter(bx), FadeIn(bx_l),
                       GrowFromCenter(by), FadeIn(by_l))                     # beat 2

        # the null
        self.play(FadeOut(VGroup(setup, bx, bx_l, by, by_l)), run_time=0.4)
        null = MathTex(r"H_0^{\text{sym}}", r":\;", r"(y_1,\dots,y_n)",
                       r"\ \text{exchangeable}").scale(1.0).shift(UP * 1.2)
        null[0].set_color(RES); null[2].set_color(EIG)
        null_cap = Text("the symptom carries no information about the wiring",
                        font_size=23, color=DIM).next_to(null, DOWN, buff=0.3)
        self.play_beat(Write(null), FadeIn(null_cap))                       # beat 3

        # shuffle labels, fix everything else
        shuf = VGroup(
            Text("fix the lesions   fix the connectome", font_size=25, color=WHITE),
            Text("shuffle ONLY the labels:  y  →  y_π", font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.25).next_to(null_cap, DOWN, buff=0.55)
        self.play_beat(FadeIn(shuf[0]), FadeIn(shuf[1], shift=UP * 0.2))     # beat 4

        # the permutation p-value
        self.play(FadeOut(VGroup(null, null_cap, shuf)), run_time=0.4)
        pval = MathTex(r"p", "=", r"\frac{1}{|G|}",
                       r"\sum_{\pi \in G}",
                       r"\mathbf{1}\!\left[\, T(y_\pi) \ge T(y_{\text{id}}) \,\right]")\
            .scale(1.0).shift(UP * 0.7)
        pval[0].set_color(RES); pval[4].set_color(VAR)
        # decode the symbols on screen: T is the contrast, y_pi a relabeling, y_id observed
        bind = Brace(pval[4], DOWN, color=VAR)
        bind_l = Text("contrast T of a relabeling y_pi vs the observed y_id",
                      font_size=20, color=VAR).next_to(bind, DOWN, buff=0.12)
        bsum = Brace(pval[3], UP, color=DIM)
        bsum_l = Text("sum over all relabelings pi in the group G", font_size=18,
                      color=DIM).next_to(bsum, UP, buff=0.1)
        pcap = Text("fraction of relabelings whose contrast beats the observed one",
                    font_size=22, color=DIM).next_to(bind_l, DOWN, buff=0.3)
        self.play_beat(Write(pval),
                       GrowFromCenter(bsum), FadeIn(bsum_l),
                       GrowFromCenter(bind), FadeIn(bind_l),
                       FadeIn(pcap))                                        # beat 5

        exact = Text("exact in finite samples — no distributional assumption, just counting",
                     font_size=23, color=BACK).next_to(pcap, DOWN, buff=0.45)
        self.play_beat(FadeOut(VGroup(bsum, bsum_l, bind, bind_l)),
                       FadeIn(exact))                                       # beat 6

        ask = Text("New question:  report this as a fair BET, not a p-value?",
                   font_size=26, color=RES).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(ask, shift=UP * 0.2))                        # beat 7


# ----------------------------------------------------------------------
# Scene 2 — betting on the contrast: the permutation e-value
# ----------------------------------------------------------------------
class S2_BetOnContrast(NarratedScene):
    scene_key = "S2_BetOnContrast"

    def construct(self):
        self.header("Betting on the contrast")

        # recall the e-value definition
        defn = MathTex("E", r"\ge", "0", r"\qquad \mathbb{E}_{H_0}[E]", r"\le", "1")\
            .scale(1.05).shift(UP * 2.1)
        defn[0].set_color(RES); defn[3].set_color(RES)
        dcap = Text("a $1 bet, rigged fair under the null  (Vol 5)",
                    font_size=22, color=DIM).next_to(defn, DOWN, buff=0.25)
        self.play_beat(Write(defn), FadeIn(dcap))                          # beat 1

        # the wager
        wager = VGroup(
            Text("Wager:", font_size=26, color=RES),
            Text("the observed contrast beats a randomly relabeled one",
                 font_size=25, color=WHITE),
        ).arrange(RIGHT, buff=0.3).next_to(dcap, DOWN, buff=0.5)
        self.play_beat(FadeIn(wager, shift=UP * 0.2))                      # beat 2

        # |G| = N
        self.play(FadeOut(VGroup(defn, dcap, wager)), run_time=0.4)
        size = MathTex(r"N", r"\ :=\ ", r"|G|", r"\ =\ \text{number of relabelings}")\
            .scale(1.0).shift(UP * 1.9)
        size[0].set_color(EIG); size[2].set_color(EIG)
        self.play_beat(Write(size))                                        # beat 3

        # the e-value definition
        evdef = MathTex("E", "=", r"N", r"\cdot",
                        r"\mathbf{1}\!\left[\, T(y_{\text{id}})\ \text{is top of } \{T(y_\pi)\} \,\right]")\
            .scale(0.95).next_to(size, DOWN, buff=0.7)
        evdef[0].set_color(RES); evdef[2].set_color(EIG); evdef[4].set_color(VAR)
        ebox = SurroundingRectangle(evdef, color=RES, buff=0.2)
        self.play_beat(Write(evdef), Create(ebox))                        # beat 4

        # why fair: top with prob 1/N
        why = MathTex(r"\Pr\nolimits_{H_0}\!\big(", r"T(y_{\text{id}})\ \text{is top}",
                      r"\big)", "=", r"\frac{1}{N}")\
            .scale(0.95).next_to(ebox, DOWN, buff=0.55)
        why[1].set_color(VAR); why[4].set_color(EIG)
        why_cap = Text("under exchangeability, the observed labeling is one of N equally likely",
                       font_size=21, color=DIM).next_to(why, DOWN, buff=0.25)
        self.play_beat(Write(why), FadeIn(why_cap))                       # beat 5

        # expectation = N * 1/N = 1
        self.play(FadeOut(VGroup(size, evdef, ebox, why, why_cap)), run_time=0.4)
        exp = MathTex(r"\mathbb{E}_{H_0}[E]", "=", r"N \cdot \tfrac{1}{N}", "=", "1")\
            .scale(1.2).shift(UP * 1.0)
        exp[0].set_color(RES); exp[4].set_color(BACK)
        exp_cap = Text("a valid e-value:  the calibrator  E = (1/α)·1[event]",
                       font_size=23, color=DIM).next_to(exp, DOWN, buff=0.35)
        self.play_beat(Write(exp), FadeIn(exp_cap))                       # beat 6

        # read as evidence
        read = VGroup(
            Text("top of 1000 relabelings  →  pays $1000  →  null in trouble",
                 font_size=24, color=BACK),
            Text("mid-pack  →  pays $0  →  learned nothing", font_size=24, color=DIM),
            Text("the payout IS the evidence", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.25).next_to(exp_cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(read, lag_ratio=0.3))                       # beat 7


# ----------------------------------------------------------------------
# Scene 3 — the backbone still cancels
# ----------------------------------------------------------------------
class S3_BackboneStill(NarratedScene):
    scene_key = "S3_BackboneStill"

    def construct(self):
        self.header("The backbone still cancels")

        intro = Text("the e-value is a function of the SAME contrast T —\nso it inherits everything T does",
                     font_size=27, color=WHITE, line_spacing=0.8).shift(UP * 2.1)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # decomposition
        dec = MathTex("x_i", "=", r"\underbrace{\beta_i\, u_1}_{\text{backbone}}",
                      "+", "r_i").scale(1.2).shift(UP * 0.6)
        dec[0].set_color(VAR); dec[2].set_color(BACK); dec[4].set_color(VAR)
        self.play_beat(Write(dec), intro.animate.set_opacity(0.4))        # beat 2

        # beta_i is label-free
        free = MathTex(r"\beta_i", r"\ \text{depends on lesion location, } ",
                       r"\textbf{not on } y_i")\
            .scale(0.9).next_to(dec, DOWN, buff=0.6)
        free[0].set_color(BACK); free[2].set_color(EIG)
        self.play_beat(Write(free))                                       # beat 3

        # contrast: difference of group means
        self.play(FadeOut(VGroup(intro, free)),
                  dec.animate.scale(0.8).to_edge(UP, buff=1.1), run_time=0.5)
        contrast = MathTex(
            r"t_v", r"\ \propto\ ",
            r"\big(\bar\beta^{(1)} - \bar\beta^{(0)}\big)\,u_{1,v}",
            "+",
            r"\big(\bar r^{\,(1)}_v - \bar r^{\,(0)}_v\big)")\
            .scale(0.85).shift(UP * 0.7)
        contrast[0].set_color(VAR)
        contrast[2].set_color(BACK)
        contrast[4].set_color(VAR)
        cancel = Text("same label-free constant on both sides  →  it subtracts off",
                      font_size=23, color=BAD).next_to(contrast, DOWN, buff=0.35)
        self.play_beat(Write(contrast), FadeIn(cancel))                  # beat 4

        # loadings never relabeled
        keep = Text("the backbone loadings are NEVER relabeled — only the symptom labels are",
                    font_size=23, color=WHITE).next_to(cancel, DOWN, buff=0.5)
        keep2 = Text("so the backbone enters observed T and every permuted T identically",
                     font_size=23, color=DIM).next_to(keep, DOWN, buff=0.2)
        self.play_beat(FadeIn(keep), FadeIn(keep2))                      # beat 5

        # e-value inherits cancellation
        self.play(FadeOut(VGroup(contrast, cancel, keep, keep2)), run_time=0.4)
        inh = MathTex("E", "=", r"f\big(", r"T", r"\big)",
                      r"\quad\Rightarrow\quad",
                      r"E\ \text{ignores the backbone too}")\
            .scale(0.95).shift(UP * 0.3)
        inh[0].set_color(RES); inh[3].set_color(VAR); inh[6].set_color(BACK)
        self.play_beat(Write(inh))                                       # beat 6

        moral = Text("the mechanism that detonated the LOCATION null\nis inert here — in the p-value and its e-value twin alike",
                     font_size=26, color=RES, line_spacing=0.8)\
            .next_to(inh, DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                    # beat 7


# ----------------------------------------------------------------------
# Scene 4 — why an e-value here: anytime-valid multiplication
# ----------------------------------------------------------------------
class S4_Sequential(NarratedScene):
    scene_key = "S4_Sequential"

    def construct(self):
        self.header("Why an e-value here")

        intro = Text("a p-value can't do one thing cleanly:\narithmetic ACROSS analyses",
                     font_size=28, color=WHITE, line_spacing=0.8).shift(UP * 2.2)
        self.play_beat(FadeIn(intro))                                    # beat 1

        # e-values multiply
        mult = MathTex(r"E_1 \times E_2", r"\ \text{is still a valid e-value}",
                       r"\quad(\text{independent data})")\
            .scale(0.95).shift(UP * 0.9)
        mult[0].set_color(RES)
        self.play_beat(Write(mult), intro.animate.set_opacity(0.4))      # beat 2

        # cohorts arrive
        self.play(FadeOut(VGroup(intro, mult)), run_time=0.4)
        chips = VGroup(
            self._cohort("Cohort 1", "E_1", VAR),
            self._cohort("Cohort 2", "E_2", BACK),
            self._cohort("Cohort 3", "E_3", EIG),
        ).arrange(RIGHT, buff=0.7).shift(UP * 1.3)
        self.play_beat(FadeIn(chips[0]), FadeIn(chips[1]))               # beat 3

        # running product
        prod = MathTex(r"E_{\text{cum}}", "=",
                       r"E_1", r"\times", r"E_2", r"\times", r"E_3", r"\times \cdots")\
            .scale(1.0).next_to(chips, DOWN, buff=0.8)
        prod[0].set_color(RES)
        prod[2].set_color(VAR); prod[4].set_color(BACK); prod[6].set_color(EIG)
        self.play_beat(FadeIn(chips[2], shift=UP * 0.2), Write(prod))    # beat 4

        # test martingale: E[E] <= 1 at any stopping time
        mart = MathTex(r"\mathbb{E}_{H_0}[E_{\text{cum}}]", r"\le", "1",
                       r"\quad\text{at any stopping time}")\
            .scale(0.95).next_to(prod, DOWN, buff=0.55)
        mart[0].set_color(RES); mart[2].set_color(BACK)
        mart_cap = Text("a test martingale  →  anytime-valid inference",
                        font_size=23, color=DIM).next_to(mart, DOWN, buff=0.25)
        self.play_beat(Write(mart), FadeIn(mart_cap))                    # beat 5

        # stop when large, no penalty
        self.play(FadeOut(VGroup(chips, prod, mart, mart_cap)), run_time=0.4)
        stop = Text("watch a slowly accruing surgical cohort,\nstop the moment the product is large —\nno peeking penalty, no pre-fixed sample size",
                    font_size=27, color=BACK, line_spacing=0.85).shift(UP * 0.7)
        self.play_beat(FadeIn(stop, shift=UP * 0.2))                     # beat 6

        # the coin example: power from stacking
        coin = MathTex(r"1.5^{10}", r"\approx", "57.7")\
            .scale(1.2).next_to(stop, DOWN, buff=0.7)
        coin[0].set_color(VAR); coin[2].set_color(RES)
        coin_cap = Text("ten mild bets, multiplied — stacking is where the power comes from",
                        font_size=23, color=DIM).next_to(coin, DOWN, buff=0.25)
        self.play_beat(Write(coin), FadeIn(coin_cap))                    # beat 7

    def _cohort(self, name, sym, color):
        box = RoundedRectangle(width=2.4, height=1.1, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.10)
        t = Text(name, font_size=20, color=color).move_to(box).shift(UP * 0.25)
        e = MathTex(sym, color=color).scale(0.9).move_to(box).shift(DOWN * 0.25)
        return VGroup(box, t, e)


# ----------------------------------------------------------------------
# Scene 5 — across voxels with e-BH
# ----------------------------------------------------------------------
class S5_MultipleVoxels(NarratedScene):
    scene_key = "S5_MultipleVoxels"

    def construct(self):
        self.header("Across voxels with e-BH")

        intro = MathTex(r"\text{one map}", "=", r"V", r"\ \text{voxels, each with its own symptom contrast}")\
            .scale(0.85).shift(UP * 2.2)
        intro[2].set_color(VAR)
        self.play_beat(Write(intro))                                     # beat 1

        # classic BH leans on p-values
        bh = VGroup(
            Text("classic Benjamini–Hochberg controls the FDR", font_size=25, color=WHITE),
            Text("but it leans on the p-values behaving", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(intro, DOWN, buff=0.55)
        self.play_beat(FadeIn(bh, shift=UP * 0.2))                       # beat 2

        # heavy spatial dependence
        dep = VGroup(
            Text("brain maps have HEAVY spatial dependence", font_size=25, color=BAD),
            Text("neighboring voxels are highly correlated", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(bh, DOWN, buff=0.45)
        self.play_beat(FadeIn(dep[0]), FadeIn(dep[1]))                   # beat 3

        # mint e-values, run e-BH
        self.play(FadeOut(VGroup(intro, bh, dep)), run_time=0.5)
        recipe = MathTex(r"\text{each voxel } v", r"\ \longrightarrow\ ",
                         r"E_v", r"\ \longrightarrow\ ", r"\text{e-BH}")\
            .scale(1.0).shift(UP * 1.3)
        recipe[0].set_color(VAR); recipe[2].set_color(RES); recipe[4].set_color(BACK)
        self.play_beat(Write(recipe))                                    # beat 4

        # key property: arbitrary dependence
        key = VGroup(
            Text("e-BH controls the FDR under ARBITRARY dependence",
                 font_size=26, color=RES),
            Text("no spatial-dependence model needed", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(recipe, DOWN, buff=0.6)
        kbox = SurroundingRectangle(key, color=RES, buff=0.25)
        self.play_beat(FadeIn(key, shift=UP * 0.2), Create(kbox))        # beat 5

        moral = Text("one common currency, end to end:\neach contrast a fair bet, e-BH stacks them into map-wide control",
                     font_size=25, color=WHITE, line_spacing=0.85)\
            .next_to(kbox, DOWN, buff=0.55)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                    # beat 6


# ----------------------------------------------------------------------
# Scene 6 — caveat and scope
# ----------------------------------------------------------------------
class S6_Caveat(NarratedScene):
    scene_key = "S6_Caveat"

    def construct(self):
        self.header("Caveat and scope")

        cav = VGroup(
            Text("✗ NOT a validated estimator", font_size=26, color=BAD),
            Text("this is an ILLUSTRATIVE construction — to show the machinery",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.8)
        self.play_beat(FadeIn(cav, shift=UP * 0.2))                      # beat 1

        flag = Text("[verify against primary source for the exact estimator]",
                    font_size=24, color=DIM).next_to(cav, DOWN, buff=0.5)
        fbox = SurroundingRectangle(flag, color=DIM, buff=0.2)
        self.play_beat(FadeIn(flag), Create(fbox))                       # beat 2

        # same question, now sequential
        same = Text("it answers the SAME symptom question as Part 5 —\nnow sequentially, and across analyses",
                    font_size=26, color=WHITE, line_spacing=0.85)\
            .next_to(fbox, DOWN, buff=0.55)
        self.play_beat(FadeIn(same, shift=UP * 0.2))                     # beat 3

        # the boundary
        self.play(FadeOut(VGroup(cav, flag, fbox, same)), run_time=0.5)
        bound = MathTex(r"\text{valid } E\ \text{of the WRONG null}", "=",
                        r"\text{worthless}")\
            .scale(1.0).shift(UP * 1.4)
        bound[0].set_color(RES); bound[2].set_color(BAD)
        bcap = Text("e-values own accumulation & multiplicity — NOT correctness of the question",
                    font_size=22, color=DIM).next_to(bound, DOWN, buff=0.3)
        self.play_beat(Write(bound), FadeIn(bcap))                       # beat 4

        # confounding is owned elsewhere
        conf = VGroup(
            Text("lesion size left out of the null?  betting won't fix it.",
                 font_size=25, color=WHITE),
            Text("design + Freedman–Lane own confounding.  A wrong null is still wrong.",
                 font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.25).next_to(bcap, DOWN, buff=0.55)
        self.play_beat(FadeIn(conf[0]), FadeIn(conf[1], shift=UP * 0.2)) # beat 5

        self.play(FadeOut(VGroup(bound, bcap, conf)), run_time=0.5)
        moral = VGroup(
            Text("The e-value does not change that.", font_size=29, color=WHITE),
            Text("It lets a RIGHT null speak in a richer currency:", font_size=27, color=RES),
            Text("evidence you can accumulate, and control across a whole map.",
                 font_size=27, color=BACK),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                     # beat 6
