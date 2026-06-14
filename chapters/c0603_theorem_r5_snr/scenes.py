"""c0603_theorem_r5_snr — "Theorem R5: residualization improves SNR (proof)".

Five narrated scenes that state and prove R5: under the backbone-sharing
assumption, residualizing the leading connectome modes out of every map weakly
raises the per-voxel signal-to-noise ratio of a between-group contrast, with strict
inequality exactly when the backbone carries within-group variance but no
between-group signal.

All equations/numbers are quoted from:
  responses/lnm_critique/sections/04_removing_the_backbone.md
specifically the "[!math] Residualization is signal-preserving and noise-reducing"
block and the backbone-sharing "[!IMPORTANT]" assumption.

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0603_theorem_r5_snr ./render.sh \
      chapters/c0603_theorem_r5_snr/scenes.py -q ql \
      S1_Statement S2_Model S3_Strategy S4_Proof S5_Moral
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the R5 statement
# ----------------------------------------------------------------------
class S1_Statement(NarratedScene):
    scene_key = "S1_Statement"

    def construct(self):
        self.header("The R5 statement")

        intro = Text("Removing variance can RAISE signal-to-noise",
                     font_size=30, color=RES).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # Definition of SNR
        snr = MathTex(r"\mathrm{SNR}(v)", "=",
                      r"\frac{\delta(v)^2}{\mathrm{Var}\!\big(m(v)\big)}")\
            .scale(1.25).shift(UP * 1.0)
        snr[0].set_color(VAR)
        snr[2].set_color(WHITE)
        self.play_beat(Write(snr), intro.animate.set_opacity(0.4))         # beat 2

        # annotate the numerator: delta = between-group signal
        brace_num = Brace(snr[2][0:5], UP, color=BACK)  # the delta(v)^2 numerator glyphs
        num_lab = Text("between-group signal:\nmean map difference, group 1 minus group 0",
                       font_size=21, color=BACK, line_spacing=0.8)\
            .next_to(brace_num, UP, buff=0.2)
        self.play_beat(GrowFromCenter(brace_num), FadeIn(num_lab))         # beat 3

        # annotate the denominator: within-group noise
        self.play(FadeOut(VGroup(brace_num, num_lab)), run_time=0.4)
        brace_den = Brace(snr[2], DOWN, color=BAD)
        den_lab = Text("within-group noise:\nvariance of the map across patients at voxel v",
                       font_size=21, color=BAD, line_spacing=0.8)\
            .next_to(brace_den, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_den), FadeIn(den_lab))         # beat 4

        # the inequality itself
        self.play(FadeOut(VGroup(brace_den, den_lab, intro)),
                  snr.animate.scale(0.7).to_edge(UP, buff=1.1), run_time=0.5)
        ineq = MathTex(r"\mathrm{SNR}_{\tilde m}(v)", r"\;\ge\;",
                       r"\mathrm{SNR}_{m}(v)").scale(1.3).shift(UP * 0.6)
        ineq[0].set_color(BACK); ineq[2].set_color(DIM)
        ineq_cap = Text("residualized map  vs  raw map,  under backbone-sharing",
                        font_size=23, color=DIM).next_to(ineq, DOWN, buff=0.35)
        self.play_beat(Write(ineq), FadeIn(ineq_cap))                      # beat 5

        # strict when backbone carries variance but no signal
        strict = VGroup(
            Text("STRICT  >  exactly when the backbone carries", font_size=24, color=RES),
            Text("within-group variance  but  no between-group signal",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.18).next_to(ineq_cap, DOWN, buff=0.55)
        self.play_beat(FadeIn(strict, shift=UP * 0.2))                     # beat 6

        moral = Text("strip shared structure that is pure noise for the contrast",
                     font_size=25, color=WHITE).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(moral))                                      # beat 7


# ----------------------------------------------------------------------
# Scene 2 — the signal model
# ----------------------------------------------------------------------
class S2_Model(NarratedScene):
    scene_key = "S2_Model"

    def construct(self):
        self.header("The signal model")

        intro = Text("split every map into two orthogonal pieces",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # m = Pi_B m + tilde m
        decomp = MathTex("m", "=", r"\Pi_{\mathcal B}\, m", "+", r"\tilde m")\
            .scale(1.35).shift(UP * 1.2)
        decomp[0].set_color(VAR)
        decomp[2].set_color(BACK)
        decomp[4].set_color(RES)
        b1 = Brace(decomp[2], DOWN, color=BACK)
        l1 = Text("backbone part:  the shared bulk", font_size=21, color=BACK)\
            .next_to(b1, DOWN, buff=0.15)
        b2 = Brace(decomp[4], DOWN, color=RES)
        l2 = Text("residual:  the sliver on top", font_size=21, color=RES)\
            .next_to(b2, DOWN, buff=0.15)
        self.play_beat(Write(decomp), GrowFromCenter(b1), FadeIn(l1),
                       GrowFromCenter(b2), FadeIn(l2))                     # beat 2

        # Pi_B is the fixed projector onto leading modes
        self.play(FadeOut(VGroup(b1, l1, b2, l2, intro)), run_time=0.4)
        proj = MathTex(r"\Pi_{\mathcal B}", "=",
                       r"\sum_{j=1}^{r} u_j u_j^{\top}")\
            .scale(1.15).next_to(decomp, DOWN, buff=0.8)
        proj[0].set_color(BACK); proj[2].set_color(BACK)
        proj_cap = Text("projector onto the leading connectome modes u_1 ... u_r\nfixed before any patient is seen — label-independent",
                        font_size=21, color=DIM, line_spacing=0.8)\
            .next_to(proj, DOWN, buff=0.3)
        self.play_beat(Write(proj), FadeIn(proj_cap))                      # beat 3

        # now the population view: mu (shared backbone)
        self.play(FadeOut(VGroup(proj, proj_cap)),
                  decomp.animate.scale(0.7).to_edge(UP, buff=1.1), run_time=0.5)
        mu = VGroup(
            MathTex(r"\mu", color=BACK).scale(1.3),
            Text("the shared backbone — common to BOTH groups",
                 font_size=24, color=BACK),
        ).arrange(RIGHT, buff=0.4).shift(UP * 1.1)
        self.play_beat(FadeIn(mu, shift=UP * 0.2))                         # beat 4

        # delta-tilde (discriminative signal, off-backbone)
        dt = VGroup(
            MathTex(r"\tilde\delta", color=RES).scale(1.3),
            Text("the discriminative signal — differs between groups,\nlives OFF the backbone, in the residual",
                 font_size=23, color=RES, line_spacing=0.8),
        ).arrange(RIGHT, buff=0.4).next_to(mu, DOWN, buff=0.5)
        self.play_beat(FadeIn(dt, shift=UP * 0.2))                         # beat 5

        # noise (within-group variability)
        nz = VGroup(
            MathTex(r"\varepsilon", color=BAD).scale(1.3),
            Text("noise — within-group variability across patients,\nwith a backbone share and a residual share",
                 font_size=23, color=BAD, line_spacing=0.8),
        ).arrange(RIGHT, buff=0.4).next_to(dt, DOWN, buff=0.5)
        self.play_beat(FadeIn(nz, shift=UP * 0.2))                         # beat 6

        # the sharp question
        self.play(FadeOut(VGroup(mu, dt, nz)), run_time=0.5)
        q = VGroup(
            Text("Does keeping only the residual m-tilde", font_size=27, color=WHITE),
            MathTex(r"\text{throw away any of } \tilde\delta \;?",
                    color=WHITE).scale(1.0),
            Text("The model says NO.", font_size=30, color=RES),
        ).arrange(DOWN, buff=0.35)
        q[1][0].set_color(RES)
        self.play_beat(FadeIn(q, lag_ratio=0.3))                          # beat 7


# ----------------------------------------------------------------------
# Scene 3 — pre-proof strategy
# ----------------------------------------------------------------------
class S3_Strategy(NarratedScene):
    scene_key = "S3_Strategy"

    def construct(self):
        self.header("Pre-proof strategy")

        head = Text("the whole shape, in one breath", font_size=28, color=DIM)\
            .shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                       # beat 1

        plan = VGroup(
            Text("numerator  (signal)", font_size=26, color=BACK),
            Text("UNTOUCHED", font_size=26, color=BACK),
            Text("denominator  (noise)", font_size=26, color=BAD),
            Text("can only SHRINK", font_size=26, color=BAD),
        ).arrange_in_grid(rows=2, cols=2, buff=(0.8, 0.25)).shift(UP * 1.3)
        self.play_beat(FadeIn(plan, lag_ratio=0.15))                       # beat 2

        # backbone-sharing = P1's convergence, restated
        self.play(FadeOut(VGroup(head, plan)), run_time=0.4)
        bs = Text("Engine: the backbone-sharing assumption",
                  font_size=27, color=RES).shift(UP * 2.3)
        p1 = Text("= P1's own convergence claim, read at the population level",
                  font_size=24, color=DIM).next_to(bs, DOWN, buff=0.25)
        self.play_beat(FadeIn(bs), FadeIn(p1))                             # beat 3

        conv = MathTex(r"\text{avg}\big(\textstyle\sum (M\times C)\big)",
                       r"\longrightarrow", r"\deg(C)").scale(1.0)\
            .next_to(p1, DOWN, buff=0.5)
        conv[2].set_color(BACK)
        conv_cap = Text("M = stacked lesion seeds,  C = normative connectome\n"
                        "avg over a heterogeneous set lands on deg(C): the shared backbone",
                        font_size=21, color=DIM, line_spacing=0.8)\
            .next_to(conv, DOWN, buff=0.25)
        self.play_beat(Write(conv), FadeIn(conv_cap))                      # beat 4

        # same mean in both groups
        same = MathTex(r"\mathbb{E}[\Pi_{\mathcal B} m \mid y{=}1]", "=",
                       r"\mathbb{E}[\Pi_{\mathcal B} m \mid y{=}0]")\
            .scale(0.95).next_to(conv_cap, DOWN, buff=0.55)
        same[0].set_color(BACK); same[2].set_color(BACK)
        same_cap = Text("backbone has the SAME mean in both groups → no between-group difference",
                        font_size=21, color=WHITE).next_to(same, DOWN, buff=0.25)
        self.play_beat(Write(same), FadeIn(same_cap))                      # beat 5

        # signal lives off-backbone, orthogonal
        self.play(FadeOut(VGroup(bs, p1, conv, conv_cap, same, same_cap)),
                  run_time=0.5)
        orth = VGroup(
            Text("common structure cannot tell two groups apart",
                 font_size=26, color=WHITE),
            Text("the discriminative signal lives OFF the backbone,",
                 font_size=26, color=RES),
            Text("orthogonal to it — the subtraction never touches it",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.4)
        self.play_beat(FadeIn(orth, lag_ratio=0.2))                        # beat 6

        concl = Text("numerator fixed,  noise removed  ⇒  the ratio can only rise",
                     font_size=26, color=BACK).to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(concl, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 4 — the proof
# ----------------------------------------------------------------------
class S4_Proof(NarratedScene):
    scene_key = "S4_Proof"

    def construct(self):
        self.header("The proof")

        head = Text("words between every step", font_size=26, color=DIM)\
            .to_edge(UP, buff=0.75)
        self.play_beat(FadeIn(head))                                       # beat 1

        # delta split into two brackets
        split = MathTex(
            r"\delta(v)", "=",
            r"\big(\mathbb{E}[\Pi_{\mathcal B}m\mid y{=}1]-\mathbb{E}[\Pi_{\mathcal B}m\mid y{=}0]\big)",
            "+",
            r"\big(\mathbb{E}[\tilde m\mid y{=}1]-\mathbb{E}[\tilde m\mid y{=}0]\big)",
        ).scale(0.7).shift(UP * 1.4)
        split[0].set_color(BACK)
        split[2].set_color(BACK)
        split[4].set_color(RES)
        self.play_beat(Write(split))                                       # beat 2

        b_back = Brace(split[2], DOWN, color=BACK)
        l_back = Text("backbone difference", font_size=20, color=BACK)\
            .next_to(b_back, DOWN, buff=0.12)
        b_res = Brace(split[4], DOWN, color=RES)
        l_res = Text("residual difference", font_size=20, color=RES)\
            .next_to(b_res, DOWN, buff=0.12)
        self.play_beat(GrowFromCenter(b_back), FadeIn(l_back),
                       GrowFromCenter(b_res), FadeIn(l_res))               # beat 3

        # first bracket = 0
        zero = MathTex(r"\underbrace{(\;\cdots\;)}_{=\,0\ \text{by backbone-sharing}}",
                       "+", r"\tilde\delta(v)").scale(0.9)
        zero[0].set_color(BACK); zero[2].set_color(RES)
        zero.next_to(VGroup(b_back, b_res), DOWN, buff=0.5)
        self.play_beat(Write(zero))                                        # beat 4

        # delta = tilde-delta
        self.play(FadeOut(VGroup(split, b_back, l_back, b_res, l_res, zero)),
                  run_time=0.5)
        num = MathTex(r"\delta(v)", "=", r"\tilde\delta(v)").scale(1.2)\
            .shift(UP * 2.0)
        num[0].set_color(BACK); num[2].set_color(RES)
        num_cap = Text("NUMERATOR unchanged — residualizing costs no signal",
                       font_size=22, color=BACK).next_to(num, DOWN, buff=0.25)
        self.play(FadeIn(num), FadeIn(num_cap), run_time=0.5)

        # variance decomposition
        var = MathTex(
            r"\mathrm{Var}(m)", "=",
            r"\mathrm{Var}(\Pi_{\mathcal B}m)", "+",
            r"\mathrm{Var}(\tilde m)", "+",
            r"2\,\mathrm{Cov}_i(\Pi_{\mathcal B}m,\tilde m)",
        ).scale(0.75).next_to(num_cap, DOWN, buff=0.55)
        var[0].set_color(BAD)
        var[2].set_color(BACK); var[4].set_color(RES); var[6].set_color(DIM)
        self.play_beat(Write(var))                                         # beat 5

        # delete the backbone variance term
        cross = Cross(var[2], stroke_color=BAD, stroke_width=5)
        drop = MathTex(r"\propto \lambda_1^2 \ \text{— the dominant chunk}",
                       color=BAD).scale(0.8).next_to(var, DOWN, buff=0.45)
        self.play_beat(Create(cross), FadeIn(drop))                        # beat 6

        # shrinks denominator if covariance non-negative
        cond = MathTex(r"\mathrm{Cov}_i(\Pi_{\mathcal B}m,\tilde m)", r"\geq", "0")\
            .scale(0.9)
        cond[0].set_color(DIM); cond[2].set_color(RES)
        cond.next_to(drop, DOWN, buff=0.45)
        cond_cap = Text("removed and retained parts not anti-correlated across patients",
                        font_size=21, color=DIM).next_to(cond, DOWN, buff=0.2)
        self.play_beat(Write(cond), FadeIn(cond_cap))                      # beat 7

        # QED
        self.play(FadeOut(VGroup(num, num_cap, var, cross, drop, cond,
                                 cond_cap, head)), run_time=0.5)
        qed = MathTex(
            r"\mathrm{SNR}_{\tilde m}(v)", "=",
            r"\frac{\tilde\delta(v)^2}{\mathrm{Var}(\tilde m(v))}",
            r"\;\ge\;",
            r"\frac{\delta(v)^2}{\mathrm{Var}(m(v))}", "=",
            r"\mathrm{SNR}_{m}(v)",
        ).scale(0.95).shift(UP * 0.4)
        qed[0].set_color(BACK); qed[6].set_color(DIM)
        qbox = SurroundingRectangle(qed, color=RES, buff=0.25)
        qcap = Text("same numerator,  smaller denominator  —  R5 proved",
                    font_size=24, color=RES).next_to(qbox, DOWN, buff=0.4)
        self.play_beat(Write(qed), Create(qbox), FadeIn(qcap))             # beat 8


# ----------------------------------------------------------------------
# Scene 5 — moral and limits
# ----------------------------------------------------------------------
class S5_Moral(NarratedScene):
    scene_key = "S5_Moral"

    def construct(self):
        self.header("Moral and limits")

        moral = VGroup(
            Text("Strip the shared structure to see the difference.",
                 font_size=30, color=WHITE),
            Text("Cancel the chord, and the hum becomes audible.",
                 font_size=28, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.3)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 1

        choir = Text("two choirs, the same loud chord, one different hum each —\nto tell them apart, the chord is useless: remove it",
                     font_size=24, color=DIM, line_spacing=0.8)\
            .next_to(moral, DOWN, buff=0.6)
        self.play_beat(FadeIn(choir))                                      # beat 2

        # the scope
        self.play(FadeOut(VGroup(moral, choir)), run_time=0.5)
        scope = Text("But the result rests on ONE assumption:",
                     font_size=28, color=RES).shift(UP * 2.3)
        scope2 = Text("the real signal does NOT live in the backbone",
                      font_size=27, color=WHITE).next_to(scope, DOWN, buff=0.3)
        self.play_beat(FadeIn(scope), FadeIn(scope2, shift=UP * 0.2))      # beat 3

        # if it does, residualizing hurts
        hurt = MathTex(r"\text{signal} \in \mathcal{B}", r"\ \Rightarrow\ ",
                       r"\Pi_{\mathcal B} m\ \text{carries signal}", r"\ \Rightarrow\ ",
                       r"\text{residualizing HURTS}").scale(0.85)
        hurt[0].set_color(BACK); hurt[4].set_color(BAD)
        hurt.next_to(scope2, DOWN, buff=0.55)
        hurt_cap = Text("if the disease shifts the backbone itself — more or fewer hubs",
                        font_size=21, color=DIM).next_to(hurt, DOWN, buff=0.25)
        self.play_beat(Write(hurt), FadeIn(hurt_cap))                      # beat 4

        # it's a testable hypothesis
        self.play(FadeOut(VGroup(scope, scope2, hurt, hurt_cap)), run_time=0.5)
        hyp = VGroup(
            Text("So residualization is a HYPOTHESIS", font_size=28, color=RES),
            Text("about where the signal lives —", font_size=27, color=WHITE),
            Text("and it is TESTABLE.", font_size=28, color=BACK),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.1)
        self.play_beat(FadeIn(hyp, lag_ratio=0.2))                         # beat 5

        test = Text("compare backbone projections across groups BEFORE discarding;\nif they differ, do not residualize that mode",
                    font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(hyp, DOWN, buff=0.5)
        self.play_beat(FadeIn(test, shift=UP * 0.2))                       # beat 6

        # final honest limit
        self.play(FadeOut(VGroup(hyp, test)), run_time=0.5)
        limit = VGroup(
            Text("One limit we do NOT solve:", font_size=27, color=BAD),
            Text("a static connectome cannot recover higher-order or", font_size=25, color=WHITE),
            Text("dynamic effects it never encoded.", font_size=25, color=WHITE),
            Text("R5 is honest about its own scope.", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.22)
        self.play_beat(FadeIn(limit, lag_ratio=0.2))                       # beat 7
