"""v0601_the_guarantee — "The conformal coverage guarantee".

Five narrated scenes opening Volume 6. State the conformal promise (K1): the
predicted SET C(X) contains the true label with probability at least 1 - alpha,
distribution-free, finite-sample, model-free. Name the one price
(exchangeability). Flag that coverage is MARGINAL, not conditional. Preview the
uniform-rank mechanism that makes it work, setting up split conformal in v0602.

All equations/numbers are quoted from:
  volumes/vol6_conformal/chapters/01_the_guarantee.md
  volumes/vol6_conformal/VOLUME.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0601_the_guarantee ./render.sh \
      chapters/v0601_the_guarantee/scenes.py -q ql \
      S1_Promise S2_Exchangeable S3_Distribution S4_Marginal S5_Why
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the promise: Pr(Y in C(X)) >= 1 - alpha
# ----------------------------------------------------------------------
class S1_Promise(NarratedScene):
    scene_key = "S1_Promise"

    def construct(self):
        title = Text("The promise", font_size=42, color=WHITE)
        sub = Text("a set, not a number", font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))            # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # the three possible sets for a binary AE
        sets = VGroup(
            self._set_chip(r"\{\,\text{AE}-\,\}", BACK),
            self._set_chip(r"\{\,\text{AE}+\,\}", BAD),
            self._set_chip(r"\{\,\text{AE}-,\ \text{AE}+\,\}", DIM),
        ).arrange(RIGHT, buff=0.7).shift(UP * 1.4)
        self.play_beat(FadeIn(sets, lag_ratio=0.3))                         # beat 2

        # the guarantee, K1
        eq = MathTex(r"\Pr", r"\big(", "Y", r"\in", "C(X)", r"\big)",
                     r"\ge", r"1-\alpha").scale(1.4).shift(DOWN * 0.4)
        eq[2].set_color(VAR); eq[4].set_color(VAR); eq[7].set_color(RES)
        self.play_beat(Write(eq))                                           # beat 3

        # decode C(X)
        brace_c = Brace(eq[4], DOWN, color=VAR)
        c_lab = Text("the prediction SET for a new patient with features X\n"
                     "a set of candidate labels, not a point",
                     font_size=22, color=VAR, line_spacing=0.8)\
            .next_to(brace_c, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_c), FadeIn(c_lab))              # beat 4

        # decode alpha
        self.play(FadeOut(VGroup(brace_c, c_lab)), run_time=0.4)
        alpha_eq = MathTex(r"\alpha = 0.1", r"\ \Rightarrow\ ",
                           r"1-\alpha = 0.9", r"\ =\ ",
                           r"90\%\ \text{target}").scale(1.0)
        alpha_eq[0].set_color(EIG); alpha_eq[2].set_color(RES)
        alpha_eq[4].set_color(RES)
        alpha_eq.next_to(eq, DOWN, buff=0.6)
        a_cap = Text("alpha is the miscoverage level you choose",
                     font_size=22, color=DIM).next_to(alpha_eq, DOWN, buff=0.25)
        self.play_beat(Write(alpha_eq), FadeIn(a_cap))                      # beat 5

        # the probability is over the whole draw
        self.play(FadeOut(VGroup(alpha_eq, a_cap)), run_time=0.4)
        prob = Text("the probability averages over the whole draw of patients\n"
                    "at least 90% of the time the truth is inside the set",
                    font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(eq, DOWN, buff=0.6)
        self.play_beat(FadeIn(prob, shift=UP * 0.2))                       # beat 6

        # the floor: K1
        self.play(FadeOut(VGroup(sets, prob)), run_time=0.4)
        k1 = VGroup(
            Text("aim for 90%  →  get at least 90%", font_size=28, color=WHITE),
            Text("the floor of the whole volume.  Call it  K1.",
                 font_size=28, color=RES),
        ).arrange(DOWN, buff=0.3).next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(k1, lag_ratio=0.3))                          # beat 7

    def _set_chip(self, tex, color):
        box = RoundedRectangle(width=2.6, height=0.9, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.12)
        t = MathTex(tex, color=color).scale(0.7).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 2 — the one assumption: exchangeability
# ----------------------------------------------------------------------
class S2_Exchangeable(NarratedScene):
    scene_key = "S2_Exchangeable"

    def construct(self):
        self.header("The one assumption")

        intro = Text("coverage normally costs distributional faith.\n"
                     "conformal charges exactly ONE assumption — about your data",
                     font_size=26, color=DIM, line_spacing=0.8).shift(UP * 2.3)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # name it
        name = VGroup(
            Text("exchangeability", font_size=40, color=RES),
            Text("shuffle the order of patients → the world looks the same",
                 font_size=24, color=WHITE),
            Text("order carries no information", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.3)
        self.play_beat(FadeIn(name[0], scale=1.1),
                       FadeIn(name[1], shift=UP * 0.2),
                       FadeIn(name[2]))                                     # beat 2

        # the patients as pairs Z_i
        self.play(FadeOut(VGroup(intro, name)), run_time=0.4)
        zi = MathTex("Z_i", "=", r"\big(", "X_i", ",", "Y_i", r"\big)")\
            .scale(1.3).shift(UP * 1.6)
        zi[0].set_color(VAR); zi[3].set_color(VAR); zi[5].set_color(EIG)
        zi_cap = Text("X_i = features (lesion size, position, fingerprint)\n"
                      "Y_i = outcome  (AE− or AE+)",
                      font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(zi, DOWN, buff=0.3)
        roster = MathTex(r"Z_1,\dots,Z_n", r"\ \ \text{calibration},\quad",
                         r"Z_{n+1}", r"\ \text{new patient}").scale(0.9)
        roster[0].set_color(VAR); roster[2].set_color(RES)
        roster.next_to(zi_cap, DOWN, buff=0.4)
        self.play_beat(Write(zi), FadeIn(zi_cap), FadeIn(roster))          # beat 3

        # the formal definition: invariance under permutation
        self.play(FadeOut(VGroup(zi, zi_cap, roster)), run_time=0.4)
        defn = MathTex(r"(Z_1,\dots,Z_{n+1})", r"\;\overset{d}{=}\;",
                       r"(Z_{\pi(1)},\dots,Z_{\pi(n+1)})")\
            .scale(1.1).shift(UP * 0.9)
        defn[0].set_color(VAR); defn[2].set_color(VAR)
        d_cap = Text("the joint distribution is invariant under permutation pi",
                     font_size=24, color=WHITE).next_to(defn, DOWN, buff=0.35)
        self.play_beat(Write(defn), FadeIn(d_cap))                         # beat 4

        # decode the equals-with-d symbol
        brace = Brace(defn[1], DOWN, color=RES)
        sym = Text("\"has the same distribution as\"\n"
                   "every ordering of the n+1 patients is equally likely",
                   font_size=22, color=RES, line_spacing=0.8)\
            .next_to(brace, DOWN, buff=0.2).shift(DOWN * 0.4)
        self.play_beat(GrowFromCenter(brace), FadeIn(sym))                 # beat 5

        # weaker than i.i.d.
        self.play(FadeOut(VGroup(defn, d_cap, brace, sym)), run_time=0.4)
        weaker = MathTex(r"\text{i.i.d.}", r"\ \Rightarrow\ ",
                         r"\text{exchangeable}", r"\ \not\Leftarrow\ ",
                         r"\text{i.i.d.}").scale(1.1).shift(UP * 0.8)
        weaker[0].set_color(DIM); weaker[2].set_color(RES); weaker[4].set_color(DIM)
        w_cap = Text("exchangeable is WEAKER than i.i.d.\n"
                     "you can be exchangeable without being independent",
                     font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(weaker, DOWN, buff=0.4)
        self.play_beat(Write(weaker), FadeIn(w_cap))                       # beat 6

        # a shared cohort effect is fine — symmetry is what matters
        self.play(FadeOut(VGroup(weaker, w_cap)), run_time=0.4)
        shared = VGroup(
            Text("a shared, unknown cohort effect that hits everyone alike → fine",
                 font_size=24, color=WHITE),
            Text("what matters is SYMMETRY — no patient singled out by position",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.6)
        self.play_beat(FadeIn(shared[0]), FadeIn(shared[1], shift=UP * 0.2))  # beat 7

        # the new patient must be in the bunch
        newp = VGroup(
            Text("and the NEW patient must be in the bunch too — same pot, same draw",
                 font_size=24, color=WHITE),
            Text("you need not believe your model.  you believe THIS.",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3).next_to(shared, DOWN, buff=0.6)
        self.play_beat(FadeIn(newp, shift=UP * 0.2))                       # beat 8


# ----------------------------------------------------------------------
# Scene 3 — distribution-free, model-free, finite-sample
# ----------------------------------------------------------------------
class S3_Distribution(NarratedScene):
    scene_key = "S3_Distribution"

    def construct(self):
        self.header("Distribution-free and model-free")

        intro = Text("look at what the guarantee does NOT require",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # any model
        any_model = VGroup(
            Text("ANY model", font_size=30, color=VAR),
            Text("logistic · gradient-boosted tree · neural net · a coin flip",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.4)
        self.play_beat(FadeIn(any_model, shift=UP * 0.2))                  # beat 2

        # bad model -> bigger sets, not lost coverage
        trade = VGroup(
            Text("a broken model does not lose coverage", font_size=24, color=WHITE),
            Text("it just makes the sets BIGGER — hedging to keep its word",
                 font_size=24, color=DIM),
            Text("model quality buys SHARPNESS, not validity",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.18).next_to(any_model, DOWN, buff=0.5)
        self.play_beat(FadeIn(trade, lag_ratio=0.3))                       # beat 3

        # any distribution
        self.play(FadeOut(VGroup(any_model, trade)), run_time=0.4)
        any_dist = VGroup(
            Text("ANY distribution", font_size=30, color=VAR),
            Text("no \"assume Gaussian residuals\" · no \"assume the link is right\"",
                 font_size=23, color=WHITE),
            Text("distribution-free", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.0)
        self.play_beat(FadeIn(any_dist, lag_ratio=0.3))                    # beat 4

        # finite-sample
        finite = MathTex(r"n = 40", r"\quad\text{as true as}\quad", r"n = 40{,}000")\
            .scale(1.0)
        finite[0].set_color(RES); finite[2].set_color(RES)
        finite.next_to(any_dist, DOWN, buff=0.6)
        f_cap = Text("finite-sample — not \"eventually, as n grows\"",
                     font_size=23, color=DIM).next_to(finite, DOWN, buff=0.25)
        self.play_beat(Write(finite), FadeIn(f_cap))                       # beat 5

        # contrast: the Wald interval
        self.play(FadeOut(VGroup(intro, any_dist, finite, f_cap)), run_time=0.4)
        wald = VGroup(
            Text("contrast a Wald confidence interval — it needs:",
                 font_size=25, color=WHITE),
            Text("asymptotic normality · a correct model · a large sample",
                 font_size=24, color=BAD),
            Text("three distributional IOUs", font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.9)
        self.play_beat(FadeIn(wald, lag_ratio=0.3))                        # beat 6

        # conformal moves the bet
        moved = VGroup(
            Text("conformal pays NONE of them.  it moves the bet:",
                 font_size=25, color=WHITE),
            Text("not that the world is Gaussian — only that patients are interchangeable",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.25).next_to(wald, DOWN, buff=0.6)
        self.play_beat(FadeIn(moved, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 4 — marginal, not conditional
# ----------------------------------------------------------------------
class S4_Marginal(NarratedScene):
    scene_key = "S4_Marginal"

    def construct(self):
        self.header("Marginal, not conditional")

        intro = Text("the coverage is MARGINAL — a precise word that bites in the clinic",
                     font_size=26, color=RES).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # marginal statement
        marg = MathTex(r"\Pr", r"\big(", "Y", r"\in", "C(X)", r"\big)",
                       r"\ge", r"1-\alpha").scale(1.1).shift(UP * 1.4)
        marg[2].set_color(VAR); marg[4].set_color(VAR); marg[7].set_color(RES)
        m_cap = Text("averaged over patients — over the features X too",
                     font_size=23, color=DIM).next_to(marg, DOWN, buff=0.3)
        self.play_beat(Write(marg), FadeIn(m_cap))                         # beat 2

        # conditional statement (the stronger, per-patient one)
        cond = MathTex(r"\Pr", r"\big(", "Y", r"\in", "C(X)",
                       r"\mid", "X = x", r"\big)", r"\ge", r"1-\alpha")\
            .scale(1.0).next_to(m_cap, DOWN, buff=0.6)
        cond[2].set_color(VAR); cond[4].set_color(VAR)
        cond[6].set_color(BAD); cond[9].set_color(RES)
        c_cap = Text("the stronger per-patient promise — for EVERY x",
                     font_size=23, color=WHITE).next_to(cond, DOWN, buff=0.25)
        self.play_beat(Write(cond), FadeIn(c_cap))                         # beat 3

        # impossible distribution-free
        imposs = Text("distribution-free CONDITIONAL coverage is provably impossible\n"
                      "at finite n.  conformal gives the honest marginal one.",
                      font_size=24, color=BAD, line_spacing=0.8)\
            .next_to(c_cap, DOWN, buff=0.4)
        self.play_beat(FadeIn(imposs, shift=UP * 0.2))                     # beat 4

        # the worked gap: easy vs hard split
        self.play(FadeOut(VGroup(intro, marg, m_cap, cond, c_cap, imposs)),
                  run_time=0.5)
        split = VGroup(
            VGroup(
                Text("easy 90%", font_size=24, color=BACK),
                Text("covered 99%", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.12),
            VGroup(
                Text("hard 10%", font_size=24, color=BAD),
                Text("covered 9%", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.12),
        ).arrange(RIGHT, buff=1.8).shift(UP * 1.4)
        self.play_beat(FadeIn(split, lag_ratio=0.3))                       # beat 5

        # the pooled arithmetic
        pooled = MathTex("0.90", r"\times", "0.99", "+", "0.10", r"\times",
                         "0.09", "=", "0.90").scale(1.0)
        pooled[0].set_color(BACK); pooled[2].set_color(BACK)
        pooled[4].set_color(BAD); pooled[6].set_color(BAD)
        pooled[8].set_color(RES)
        pooled.next_to(split, DOWN, buff=0.7)
        p_cap = Text("pooled — a clean 90%.  marginal coverage hits the target.",
                     font_size=23, color=WHITE).next_to(pooled, DOWN, buff=0.3)
        self.play_beat(Write(pooled), FadeIn(p_cap))                       # beat 6

        # but the hard 10% is starved
        starved = Text("but the hard 10% — the large-lesion patients you most need\n"
                       "to be right about — are covered only 9% of the time",
                       font_size=24, color=BAD, line_spacing=0.8)\
            .next_to(p_cap, DOWN, buff=0.45)
        self.play_beat(FadeIn(starved, shift=UP * 0.2))                    # beat 7

        # moral
        self.play(FadeOut(VGroup(split, pooled, p_cap, starved)), run_time=0.5)
        moral = VGroup(
            Text("kept on average — broken exactly where it matters",
                 font_size=28, color=WHITE),
            Text("marginal  ≠  per-patient", font_size=32, color=RES),
        ).arrange(DOWN, buff=0.4)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 8


# ----------------------------------------------------------------------
# Scene 5 — why it works at all: the uniform-rank preview
# ----------------------------------------------------------------------
class S5_Why(NarratedScene):
    scene_key = "S5_Why"

    def construct(self):
        self.header("Why it works at all")

        intro = Text("why should counting give a guarantee with no distributional faith?\n"
                     "here is the mechanism — proved in full next chapter",
                     font_size=25, color=DIM, line_spacing=0.8).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # hold out calibration patients, score each
        hold = VGroup(
            Text("hold out calibration patients whose true outcome you know",
                 font_size=24, color=WHITE),
            Text("score each: how STRANGE does the fitted model find them?",
                 font_size=24, color=VAR),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.2)
        self.play_beat(FadeIn(hold, lag_ratio=0.3))                        # beat 2

        # the score
        score = MathTex("s", "=", "1", "-", r"\hat p_{\,y}(x)").scale(1.2)
        score[0].set_color(BAD); score[4].set_color(VAR)
        score.next_to(hold, DOWN, buff=0.6)
        s_cap = Text("one minus the probability the model put on the true label\n"
                     "correct & confident → small;  wrong & confident → large",
                     font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(score, DOWN, buff=0.3)
        self.play_beat(Write(score), FadeIn(s_cap))                        # beat 3

        # new patient is one more draw
        self.play(FadeOut(VGroup(intro, hold, score, s_cap)), run_time=0.5)
        draw = Text("the new patient is just one more draw from the same pool\n"
                    "its strangeness has NO privileged position",
                    font_size=25, color=WHITE, line_spacing=0.8).shift(UP * 1.7)
        self.play_beat(FadeIn(draw, shift=UP * 0.2))                       # beat 4

        # the uniform rank
        rank = MathTex(r"\Pr", r"\big(", "R", "=", "r", r"\big)", "=",
                       r"\frac{1}{n+1}").scale(1.3).shift(UP * 0.1)
        rank[2].set_color(RES); rank[7].set_color(RES)
        r_cap = Text("R = rank of the new score among all n+1 scores\n"
                     "under exchangeability, every rank is equally likely",
                     font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(rank, DOWN, buff=0.35)
        self.play_beat(Write(rank), FadeIn(r_cap))                         # beat 5

        # bottom 90%
        bottom = Text("\"land in the bottom 90%?\"  =  \"a uniform rank falls low enough?\"\n"
                      "it does — about 90% of the time",
                      font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(r_cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(bottom, shift=UP * 0.2))                     # beat 6

        # the moral and the bridge
        self.play(FadeOut(VGroup(draw, rank, r_cap, bottom)), run_time=0.5)
        moral = VGroup(
            Text("a uniform rank — distribution-free,", font_size=28, color=WHITE),
            Text("because counting positions never used the values, only the order",
                 font_size=26, color=RES),
            Text("next:  split conformal makes this a machine  (v0602)",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.2)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 7
