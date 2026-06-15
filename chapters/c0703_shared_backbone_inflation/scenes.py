"""c0703_shared_backbone_inflation — "Shared-backbone inflation".

Five narrated scenes. The convergence (sign-agreement) map looks like discovery,
but under R1's backbone-sharing model r_k = mu + eps_k near-total agreement is the
DEFAULT. We derive Pr[all K agree] = p^K + (1-p)^K, contrast the independent
2^(1-K) yardstick, take p -> 1 (-> 1 for every K), watch the 0.8% baseline for
K=8 collapse to ~100%, and draw the moral: convergence certifies the backbone
(the funnel), not a disease network.

All equations/numbers are from:
  responses/lnm_critique/sections/05_the_convergence_trap.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0703_shared_backbone_inflation ./render.sh \
      chapters/c0703_shared_backbone_inflation/scenes.py -q ql \
      S1_Model S2_Derive S3_Limit S4_Collapse S5_Moral
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — a shared-backbone model:  r_k = mu + eps_k
# ----------------------------------------------------------------------
class S1_Model(NarratedScene):
    scene_key = "S1_Model"

    def construct(self):
        self.header("A shared-backbone model")

        intro = Text("convergence map: keep voxels where every map agrees in sign",
                     font_size=26, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                       # beat 1

        # the decomposition r_k = mu + eps_k
        eq = MathTex("r", "_k", "(v)", "=", r"\mu", "(v)", "+", r"\varepsilon", "_k", "(v)")\
            .scale(1.4).shift(UP * 0.9)
        eq[0].set_color(VAR); eq[1].set_color(VAR); eq[2].set_color(VAR)
        eq[4].set_color(BACK); eq[5].set_color(BACK)
        eq[7].set_color(BAD); eq[8].set_color(BAD); eq[9].set_color(BAD)
        rk_lab = Text("cohort k's map at voxel v", font_size=22, color=VAR)\
            .next_to(eq, DOWN, buff=0.5)
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4),
                       FadeIn(rk_lab))                                      # beat 2

        # annotate mu — the shared backbone
        self.play(FadeOut(rk_lab), run_time=0.3)
        brace_mu = Brace(eq[4:6], DOWN, color=BACK)
        mu_lab = MathTex(r"\mu(v) \approx \lambda_1\,(u_1^\top \ell)\, u_1(v)",
                         color=BACK).scale(0.85).next_to(brace_mu, DOWN, buff=0.2)
        mu_txt = Text("the shared backbone: dominant component of C",
                      font_size=21, color=DIM).next_to(mu_lab, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_mu), FadeIn(mu_lab), FadeIn(mu_txt))  # beat 3

        # mu is common to all K — no subscript
        self.play(FadeOut(VGroup(mu_lab, mu_txt)), run_time=0.3)
        common = VGroup(
            Text("mu carries NO subscript k", font_size=26, color=BACK),
            Text("the same cheat sheet copied into every map",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.22).next_to(brace_mu, DOWN, buff=0.25)
        self.play_beat(FadeIn(common, shift=UP * 0.2))                     # beat 4

        # annotate eps_k — cohort-specific noise
        self.play(FadeOut(VGroup(brace_mu, common)), run_time=0.3)
        brace_eps = Brace(eq[7:10], UP, color=BAD)
        eps_lab = Text("cohort-specific deviation, independent, noise scale sigma",
                       font_size=21, color=BAD).next_to(brace_eps, UP, buff=0.2)
        eps_txt = Text("this part DOES carry a k", font_size=22, color=DIM)\
            .next_to(eps_lab, UP, buff=0.18)
        self.play_beat(GrowFromCenter(brace_eps), FadeIn(eps_lab),
                       FadeIn(eps_txt))                                     # beat 5

        # define p
        self.play(FadeOut(VGroup(brace_eps, eps_lab, eps_txt, intro)),
                  eq.animate.scale(0.7).to_edge(UP, buff=1.1), run_time=0.5)
        pdef = MathTex("p", "=", r"\Pr\big[\,", r"\operatorname{sign} r_k(v)",
                       "=", r"\operatorname{sign}\mu(v)", r"\,\big]")\
            .scale(1.1).shift(UP * 0.5)
        pdef[0].set_color(EIG); pdef[3].set_color(VAR); pdef[5].set_color(BACK)
        pcap = Text("p = chance one map matches mu's sign at this voxel",
                    font_size=24, color=DIM).next_to(pdef, DOWN, buff=0.4)
        self.play_beat(Write(pdef), FadeIn(pcap))                          # beat 6

        # where backbone dominates p -> 1
        regime = VGroup(
            Text("backbone dominates  →  p near 1", font_size=25, color=BACK),
            Text("noise rules  →  p toward one half", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.25).next_to(pcap, DOWN, buff=0.5)
        self.play_beat(FadeIn(regime[0]), FadeIn(regime[1], shift=UP * 0.2))  # beat 7


# ----------------------------------------------------------------------
# Scene 2 — Pr[all K agree] = p^K + (1-p)^K vs independent 2^(1-K)
# ----------------------------------------------------------------------
class S2_Derive(NarratedScene):
    scene_key = "S2_Derive"

    def construct(self):
        self.header("Probability all K agree, correlated")

        intro = Text("agreement is an intersection — count the ways it happens",
                     font_size=26, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # two disjoint ways
        ways = VGroup(
            Text("all K on the backbone sign", font_size=26, color=BACK),
            Text("OR", font_size=24, color=DIM),
            Text("all K on the opposite sign", font_size=26, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.2)
        self.play_beat(FadeIn(ways, lag_ratio=0.3))                        # beat 2

        # p^K term
        term1 = MathTex("p", "^K").scale(1.5).shift(LEFT * 2.5 + DOWN * 0.4)
        term1[0].set_color(EIG); term1[1].set_color(EIG)
        t1_lab = Text("all match: p, K times", font_size=22, color=BACK)\
            .next_to(term1, DOWN, buff=0.3)
        self.play_beat(Write(term1), FadeIn(t1_lab))                       # beat 3

        # (1-p)^K term
        term2 = MathTex("(1-p)", "^K").scale(1.5).shift(RIGHT * 2.5 + DOWN * 0.4)
        term2[0].set_color(BAD); term2[1].set_color(BAD)
        t2_lab = Text("all oppose: (1-p), K times", font_size=22, color=BAD)\
            .next_to(term2, DOWN, buff=0.3)
        plus = MathTex("+", color=WHITE).scale(1.5).move_to(
            (term1.get_right() + term2.get_left()) / 2)
        self.play_beat(Write(term2), FadeIn(t2_lab), FadeIn(plus))         # beat 4

        # the full formula, boxed
        self.play(FadeOut(VGroup(ways, t1_lab, t2_lab, term1, term2, plus, intro)),
                  run_time=0.5)
        full = MathTex(r"\Pr[\text{all } K \text{ agree}]", "=",
                       "p^{K}", "+", "(1-p)^{K}").scale(1.25).shift(UP * 0.9)
        full[0].set_color(WHITE); full[2].set_color(EIG); full[4].set_color(BAD)
        box = SurroundingRectangle(full, color=RES, buff=0.22)
        self.play_beat(Write(full), Create(box))                           # beat 5

        # contrast: independent 2^(1-K)
        indep = MathTex(r"\text{independent fair coins:}\quad",
                        r"\Pr[\text{all agree}]", "=", r"2^{\,1-K}")\
            .scale(1.0).next_to(box, DOWN, buff=0.7)
        indep[1].set_color(DIM); indep[3].set_color(VAR)
        self.play_beat(FadeIn(indep, shift=UP * 0.2))                      # beat 6

        # geometric shrink note
        note = Text("the independent baseline halves with every extra map —\nthe backbone formula does not",
                    font_size=23, color=DIM, line_spacing=0.8)\
            .next_to(indep, DOWN, buff=0.45)
        self.play_beat(FadeIn(note))                                       # beat 7


# ----------------------------------------------------------------------
# Scene 3 — as p -> 1, p^K + (1-p)^K -> 1 for every K
# ----------------------------------------------------------------------
class S3_Limit(NarratedScene):
    scene_key = "S3_Limit"

    def construct(self):
        self.header("As the backbone dominates")

        # the limit statement
        lim = MathTex("p", r"\to", "1", r"\ \ \Longrightarrow\ \ ",
                      "p^{K}", "+", "(1-p)^{K}", r"\to", "1")\
            .scale(1.15).shift(UP * 2.3)
        lim[0].set_color(EIG); lim[2].set_color(EIG)
        lim[4].set_color(EIG); lim[6].set_color(BAD); lim[8].set_color(RES)
        self.play_beat(Write(lim))                                         # beat 1

        # term-by-term
        terms = VGroup(
            MathTex("p^{K}", r"\to", "1", color=EIG),
            MathTex("(1-p)^{K}", r"\to", "0", color=BAD),
        ).arrange(RIGHT, buff=1.2).next_to(lim, DOWN, buff=0.45)
        forevery = Text("the sum → 1, for EVERY K", font_size=25, color=RES)\
            .next_to(terms, DOWN, buff=0.3)
        self.play_beat(FadeIn(terms, lag_ratio=0.3), FadeIn(forevery))     # beat 2

        # K no longer protects you
        kkill = Text("stacking more studies (larger K) no longer protects you",
                     font_size=25, color=WHITE).next_to(forevery, DOWN, buff=0.45)
        self.play_beat(FadeIn(kkill, shift=UP * 0.2))                      # beat 3

        # the curve
        self.play(FadeOut(VGroup(lim, terms, forevery, kkill)), run_time=0.5)
        ax = Axes(x_range=[0.5, 1.0, 0.1], y_range=[0, 1.0, 0.25],
                  x_length=6.5, y_length=3.4,
                  axis_config={"color": DIM, "include_tip": True,
                               "font_size": 20}).shift(DOWN * 0.3)
        xlab = MathTex("p", color=EIG).scale(0.9).next_to(ax.x_axis, RIGHT, buff=0.2)
        ylab = MathTex(r"\Pr[\text{agree}]", color=WHITE).scale(0.7)\
            .next_to(ax.y_axis, UP, buff=0.15)
        K = 4
        curve = ax.plot(lambda p: p**K + (1 - p)**K, x_range=[0.5, 1.0],
                        color=RES, stroke_width=4)
        one_line = DashedLine(ax.c2p(0.5, 1.0), ax.c2p(1.0, 1.0),
                              color=BACK, stroke_width=2)
        clab = MathTex("p^{K}+(1-p)^{K}", color=RES).scale(0.7)\
            .next_to(ax.c2p(0.78, 0.55), UP, buff=0.15)
        self.play_beat(Create(ax), FadeIn(xlab), FadeIn(ylab),
                       Create(curve), Create(one_line), FadeIn(clab))      # beat 4

        # derivative is positive
        deriv = MathTex(r"\frac{d}{dp}\big[p^{K}+(1-p)^{K}\big]",
                        "=", "K p^{K-1}", "-", "K(1-p)^{K-1}", ">", "0")\
            .scale(0.8).to_edge(DOWN, buff=0.55)
        deriv[2].set_color(EIG); deriv[4].set_color(BAD); deriv[6].set_color(RES)
        derw = Text("on (1/2, 1)", font_size=20, color=DIM)\
            .next_to(deriv, UP, buff=0.15)
        self.play_beat(Write(deriv), FadeIn(derw))                         # beat 5

        # so it only increases -> driven by mu
        self.play(FadeOut(VGroup(ax, xlab, ylab, curve, one_line, clab,
                                 derw)),
                  deriv.animate.to_edge(UP, buff=1.2), run_time=0.5)
        driven = VGroup(
            Text("so it only increases, hitting 1 at p = 1", font_size=25, color=WHITE),
            MathTex(r"\text{agreement driven entirely by }\mu",
                    color=BACK).scale(0.95),
        ).arrange(DOWN, buff=0.3).shift(DOWN * 0.2)
        self.play_beat(FadeIn(driven, lag_ratio=0.3))                      # beat 6

        manuf = Text("not by any disease-specific effect —\nthe same connectome, written into every map",
                     font_size=24, color=BAD, line_spacing=0.8)\
            .next_to(driven, DOWN, buff=0.5)
        self.play_beat(FadeIn(manuf, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 4 — the baseline collapses: 0.8% (K=8) becomes ~100%
# ----------------------------------------------------------------------
class S4_Collapse(NarratedScene):
    scene_key = "S4_Collapse"

    def construct(self):
        self.header("The baseline collapses")

        setk = MathTex("K", "=", "8").scale(1.6).shift(UP * 2.2)
        setk[0].set_color(VAR); setk[2].set_color(EIG)
        setk_lab = Text("eight cohorts", font_size=24, color=DIM)\
            .next_to(setk, DOWN, buff=0.25)
        self.play_beat(Write(setk), FadeIn(setk_lab))                      # beat 1

        # independent: 2^-7 ~ 0.8%
        indep = MathTex(r"2^{\,1-8}", "=", "2^{-7}", r"\approx", r"0.8\%")\
            .scale(1.15).shift(UP * 0.7)
        indep[0].set_color(VAR); indep[2].set_color(VAR); indep[4].set_color(VAR)
        ind_lab = Text("independent coins: impressively rare",
                       font_size=22, color=DIM).next_to(indep, DOWN, buff=0.25)
        self.play_beat(Write(indep), FadeIn(ind_lab))                      # beat 2

        # that's the informative world
        info = Text("this tiny baseline is the world where convergence is informative",
                    font_size=24, color=WHITE).next_to(ind_lab, DOWN, buff=0.45)
        self.play_beat(FadeIn(info, shift=UP * 0.2))                       # beat 3

        # but maps share a backbone
        self.play(FadeOut(VGroup(setk, setk_lab, indep, ind_lab, info)),
                  run_time=0.5)
        share = VGroup(
            Text("but the maps are NOT independent coins", font_size=27, color=BAD),
            Text("they share a backbone — R1 says they always do",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 2.0)
        self.play_beat(FadeIn(share, shift=UP * 0.2))                      # beat 4

        # p=0.9, K=4: 12.5% -> 65.6%
        comp = VGroup(
            MathTex(r"\text{independent}", "=", r"12.5\%").scale(1.0),
            MathTex(r"0.9^{4}+0.1^{4}", r"\approx", r"65.6\%").scale(1.0),
        ).arrange(DOWN, buff=0.4)
        comp[0][2].set_color(VAR)
        comp[1][0].set_color(EIG); comp[1][2].set_color(BAD)
        comp.next_to(share, DOWN, buff=0.5)
        casecap = Text("p = 0.9,  K = 4", font_size=22, color=DIM)\
            .next_to(comp, UP, buff=0.2)
        self.play_beat(FadeIn(casecap), Write(comp[0]), Write(comp[1]))    # beat 5

        # fivefold jump; K=8 runs 0.8% -> ~100%
        jump = MathTex(r"K=8:\quad", r"0.8\%", r"\ \longrightarrow\ ",
                       r"\sim 100\%").scale(1.05).next_to(comp, DOWN, buff=0.5)
        jump[1].set_color(VAR); jump[3].set_color(BAD)
        jump_lab = Text("same operator, more than a fivefold jump",
                        font_size=22, color=DIM).next_to(jump, DOWN, buff=0.2)
        self.play_beat(Write(jump), FadeIn(jump_lab))                      # beat 6

        # evidence evaporates
        self.play(FadeOut(VGroup(share, casecap, comp, jump, jump_lab)),
                  run_time=0.5)
        evap = VGroup(
            Text("the evidence evaporates", font_size=32, color=RES),
            Text("agreement is the default, not a discovery", font_size=27, color=WHITE),
            Text("a big convergence set is what the backbone alone predicts",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(evap, lag_ratio=0.3))                        # beat 7


# ----------------------------------------------------------------------
# Scene 5 — moral: convergence certifies the funnel, not a disease network
# ----------------------------------------------------------------------
class S5_Moral(NarratedScene):
    scene_key = "S5_Moral"

    def construct(self):
        self.header("Convergence certifies the funnel")

        intro = Text("a large convergence map is consistent with two worlds",
                     font_size=27, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # the two worlds
        worlds = VGroup(
            VGroup(
                Text("WORLD 1", font_size=24, color=BACK),
                Text("a real disease-specific circuit", font_size=23, color=WHITE),
            ).arrange(DOWN, buff=0.15),
            MathTex(r"\textbf{?}", color=RES).scale(1.6),
            VGroup(
                Text("WORLD 2", font_size=24, color=BAD),
                Text("only the shared backbone", font_size=23, color=WHITE),
            ).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=1.1).shift(UP * 1.0)
        self.play_beat(FadeIn(worlds, lag_ratio=0.2))                      # beat 2

        # both produce big agreement; null produces it readily
        both = VGroup(
            Text("both produce big agreement sets", font_size=25, color=WHITE),
            Text("the backbone-only null produces agreement readily",
                 font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.25).next_to(worlds, DOWN, buff=0.55)
        self.play_beat(FadeIn(both[0]), FadeIn(both[1], shift=UP * 0.2))    # beat 3

        # evidence has to be what the null wouldn't produce
        self.play(FadeOut(VGroup(intro, worlds, both)), run_time=0.5)
        ev = VGroup(
            Text("evidence = something the null would NOT readily produce",
                 font_size=25, color=WHITE),
            Text("this null produces it readily → convergence is not that evidence",
                 font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.7)
        self.play_beat(FadeIn(ev, lag_ratio=0.3))                          # beat 4

        # what convergence certifies
        cert = VGroup(
            Text("cross-study convergence certifies the SHARED BACKBONE",
                 font_size=25, color=BACK),
            Text("the funnel every seed falls into — not a disease network",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.25).next_to(ev, DOWN, buff=0.55)
        self.play_beat(FadeIn(cert, shift=UP * 0.2))                       # beat 5

        # same lesson as the average map
        same = Text("same lesson as the average map, now wearing agreement's costume:\nthe average described the funnel; convergence redraws it",
                    font_size=24, color=DIM, line_spacing=0.8)\
            .next_to(cert, DOWN, buff=0.45)
        self.play_beat(FadeIn(same))                                       # beat 6

        # the rule
        self.play(FadeOut(VGroup(ev, cert, same)), run_time=0.5)
        rule = VGroup(
            Text("Never headline a convergence map.", font_size=30, color=RES),
            Text("The inference lives in the backbone-calibrated contrast —",
                 font_size=25, color=WHITE),
            Text("not in agreement the connectome gave you for free.",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(rule, lag_ratio=0.3))                        # beat 7
