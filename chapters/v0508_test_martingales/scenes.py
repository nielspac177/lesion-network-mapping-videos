"""v0508_test_martingales — "Test martingales, Ville, and optional stopping".

Six narrated scenes. Build the wealth process as a non-negative martingale under
H0; name the test martingale as the running product of conditionally-fair bets;
prove Ville's inequality step by step; relax to supermartingales for composite
nulls; state optional stopping and tie martingale -> Ville -> anytime validity;
then name the whole structure as the engine of the e-value volume.

All equations/numbers are taken from:
  volumes/vol5_evalues/chapters/03_anytime_validity.md
  volumes/vol5_evalues/chapters/01_what_is_an_evalue.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0508_test_martingales ./render.sh \
      chapters/v0508_test_martingales/scenes.py -q ql \
      S1_Wealth S2_TestMartingale S3_VilleProof S4_Supermartingale \
      S5_Stopping S6_Why
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — wealth as a martingale  (7 beats)
# ----------------------------------------------------------------------
class S1_Wealth(NarratedScene):
    scene_key = "S1_Wealth"

    def construct(self):
        self.header("Wealth as a martingale")

        # beat 1 — the casino picture
        casino = VGroup(
            Text("You walk into a casino with $1.", font_size=30, color=WHITE),
            Text("The house says the coin is fair.", font_size=26, color=DIM),
            Text("\"fair coin\"  =  the null  H_0", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.28).shift(UP * 0.6)
        self.play_beat(FadeIn(casino, lag_ratio=0.3))                      # beat 1

        # beat 2 — define W_t and W_0 = 1
        self.play(FadeOut(casino), run_time=0.4)
        w0 = MathTex("W_0", "=", "1").scale(1.5).shift(UP * 1.6)
        w0[0].set_color(VAR); w0[2].set_color(EIG)
        wt_def = MathTex("W_t", r"=\ \text{your wealth after round } t").scale(1.0)
        wt_def[0].set_color(VAR)
        wt_def.next_to(w0, DOWN, buff=0.6)
        self.play_beat(Write(w0), FadeIn(wt_def))                          # beat 2

        # beat 3 — wealth is the running product
        self.play(FadeOut(VGroup(w0, wt_def)), run_time=0.4)
        prod = MathTex("W_t", "=", "W_{t-1}", r"\cdot", "B_t",
                       "=", r"\prod_{s=1}^{t}", "B_s").scale(1.3).shift(UP * 0.9)
        prod[0].set_color(VAR); prod[2].set_color(VAR); prod[4].set_color(EIG)
        prod[7].set_color(EIG)
        br = Brace(prod[4], DOWN, color=EIG)
        br_lab = Text("each round, multiply by that round's factor",
                      font_size=23, color=DIM).next_to(br, DOWN, buff=0.2)
        self.play_beat(Write(prod), GrowFromCenter(br), FadeIn(br_lab))    # beat 3

        # beat 4 — the martingale property appears
        self.play(FadeOut(VGroup(prod, br, br_lab)), run_time=0.4)
        mart = MathTex(r"\mathbb{E}", r"\big[", "W_t", r"\mid", r"\text{past}",
                       r"\big]", "=", "W_{t-1}").scale(1.3).shift(UP * 0.8)
        mart[2].set_color(VAR); mart[7].set_color(VAR)
        title = Text("a martingale: a fair game", font_size=28, color=RES)\
            .next_to(mart, UP, buff=0.5)
        self.play_beat(Write(mart), FadeIn(title))                         # beat 4

        # beat 5 — decode the conditional expectation
        br_e = Brace(mart[0], DOWN, color=DIM)
        e_lab = Text("expected next value, given everything seen so far",
                     font_size=23, color=DIM).next_to(br_e, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(br_e), FadeIn(e_lab))                # beat 5

        # beat 6 — non-negative, start at 1: three words
        self.play(FadeOut(VGroup(mart, title, br_e, e_lab)), run_time=0.4)
        three = VGroup(
            Text("non-negative", font_size=30, color=RES),
            Text("martingale", font_size=30, color=RES),
            Text("starting at  W_0 = 1", font_size=30, color=EIG),
        ).arrange(DOWN, buff=0.3)
        nn = MathTex("W_t", r"\geq", "0").scale(1.2).next_to(three, DOWN, buff=0.5)
        nn[0].set_color(VAR)
        self.play_beat(FadeIn(three, lag_ratio=0.3), Write(nn))            # beat 6

        # beat 7 — getting rich is evidence
        self.play(FadeOut(VGroup(three, nn)), run_time=0.4)
        rich = VGroup(
            MathTex(r"\$1 \;\longrightarrow\; \$20", color=VAR).scale(1.3),
            Text("hard to do against a true null", font_size=26, color=DIM),
            Text("getting rich  =  evidence the null is wrong", font_size=27, color=BAD),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(FadeIn(rich, lag_ratio=0.3))                        # beat 7


# ----------------------------------------------------------------------
# Scene 2 — the test martingale  (8 beats)
# ----------------------------------------------------------------------
class S2_TestMartingale(NarratedScene):
    scene_key = "S2_TestMartingale"

    def construct(self):
        self.header("The test martingale")

        # beat 1 — intro
        intro = Text("the wealth process, built one fair bet at a time",
                     font_size=28, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # beat 2 — the filtration F_{s-1}
        filt = MathTex(r"\mathcal{F}_{s-1}").scale(1.6).shift(UP * 0.9)
        filt.set_color(BACK)
        br_f = Brace(filt, DOWN, color=BACK)
        f_lab = Text("the filtration: everything known after round s minus one",
                     font_size=23, color=BACK).next_to(br_f, DOWN, buff=0.2)
        self.play_beat(Write(filt), GrowFromCenter(br_f), FadeIn(f_lab))   # beat 2

        # beat 3 — the bet B_s
        self.play(FadeOut(VGroup(filt, br_f, f_lab)), run_time=0.4)
        bet = MathTex("B_s", r"\geq", "0").scale(1.5).shift(UP * 0.9)
        bet[0].set_color(EIG)
        br_b = Brace(bet[0], DOWN, color=EIG)
        b_lab = Text("the bet: a non-negative multiplier  (1.3 means +30%)",
                     font_size=23, color=EIG).next_to(br_b, DOWN, buff=0.2)
        self.play_beat(Write(bet), GrowFromCenter(br_b), FadeIn(b_lab))    # beat 3

        # beat 4 — the product
        self.play(FadeOut(VGroup(bet, br_b, b_lab, intro)), run_time=0.4)
        prod = MathTex("W_t", "=", r"\prod_{s=1}^{t}", "B_s").scale(1.5).shift(UP * 0.9)
        prod[0].set_color(VAR); prod[3].set_color(EIG)
        cap = Text("the running product, starting from $1", font_size=24, color=DIM)\
            .next_to(prod, DOWN, buff=0.4)
        self.play_beat(Write(prod), FadeIn(cap))                           # beat 4

        # beat 5 — the fairness condition
        self.play(FadeOut(VGroup(prod, cap)), run_time=0.4)
        fair = MathTex(r"\mathbb{E}_{H_0}", r"\big[", "B_s", r"\mid",
                       r"\mathcal{F}_{s-1}", r"\big]", r"\leq", "1")\
            .scale(1.3).shift(UP * 0.9)
        fair[2].set_color(EIG); fair[4].set_color(BACK); fair[7].set_color(RES)
        br_fair = Brace(fair, DOWN, color=DIM)
        fair_lab = Text("conditionally break-even: given the past, the bet can't grow",
                        font_size=23, color=DIM).next_to(br_fair, DOWN, buff=0.2)
        self.play_beat(Write(fair), GrowFromCenter(br_fair), FadeIn(fair_lab))  # beat 5

        # beat 6 — the canonical likelihood-ratio bet
        self.play(FadeOut(VGroup(fair, br_fair, fair_lab)), run_time=0.4)
        cb = MathTex("B_s", "=", r"\frac{q(X_s)}{p(X_s)}").scale(1.4).shift(UP * 0.8)
        cb[0].set_color(EIG); cb[2].set_color(VAR)
        br_q = Brace(cb[2], UP, color=VAR)
        q_lab = Text("q: the rival density you suspect", font_size=22, color=VAR)\
            .next_to(br_q, UP, buff=0.15)
        br_p = Brace(cb[2], DOWN, color=BACK)
        p_lab = Text("p: the null density", font_size=22, color=BACK)\
            .next_to(br_p, DOWN, buff=0.15)
        self.play_beat(Write(cb), GrowFromCenter(br_q), FadeIn(q_lab),
                       GrowFromCenter(br_p), FadeIn(p_lab))                # beat 6

        # beat 7 — why it is fair: the cancellation integral
        self.play(FadeOut(VGroup(cb, br_q, q_lab, br_p, p_lab)), run_time=0.4)
        integ = MathTex(r"\mathbb{E}_{p}", r"\!\left[\frac{q(X_s)}{p(X_s)}\right]",
                        "=", r"\int \frac{q(x)}{p(x)}\,p(x)\,dx",
                        "=", r"\int q(x)\,dx", "=", "1")\
            .scale(0.95).shift(UP * 0.8)
        integ[1].set_color(VAR); integ[7].set_color(RES)
        integ_cap = Text("the p's cancel; q integrates to one  =  a fair bet",
                         font_size=23, color=DIM).next_to(integ, DOWN, buff=0.5)
        self.play_beat(Write(integ), FadeIn(integ_cap))                    # beat 7

        # beat 8 — the result
        self.play(FadeOut(VGroup(integ, integ_cap)), run_time=0.4)
        res = MathTex(r"\mathbb{E}_{H_0}", r"\big[", "W_t", r"\big]",
                      r"\leq", "1").scale(1.4).shift(UP * 0.5)
        res[2].set_color(VAR); res[5].set_color(RES)
        res_cap = Text("at every fixed round  =  a test martingale",
                       font_size=26, color=RES).next_to(res, DOWN, buff=0.5)
        self.play_beat(Write(res), FadeIn(res_cap))                        # beat 8


# ----------------------------------------------------------------------
# Scene 3 — Ville's inequality, carefully  (8 beats)
# ----------------------------------------------------------------------
class S3_VilleProof(NarratedScene):
    scene_key = "S3_VilleProof"

    def construct(self):
        self.header("Ville's inequality, carefully")

        # beat 1 — Markov vs Ville motivation
        motiv = VGroup(
            Text("Markov: bounds the wealth at one fixed moment", font_size=26, color=DIM),
            Text("Ville: bounds the wealth over its whole history at once",
                 font_size=27, color=RES),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.0)
        self.play_beat(FadeIn(motiv, lag_ratio=0.3))                       # beat 1

        # beat 2 — the theorem
        self.play(FadeOut(motiv), run_time=0.4)
        ville = MathTex(r"\Pr_{H_0}", r"\Big(", r"\sup_{t \ge 0}", "W_t",
                        r"\geq", r"\tfrac{1}{\alpha}", r"\Big)", r"\leq",
                        r"\alpha").scale(1.25).shift(UP * 0.9)
        ville[3].set_color(VAR); ville[5].set_color(EIG); ville[8].set_color(RES)
        cond = MathTex(r"W_0 = 1,\quad W_t \ge 0").scale(0.9).set_color(DIM)\
            .next_to(ville, DOWN, buff=0.45)
        self.play_beat(Write(ville), FadeIn(cond))                         # beat 2

        # beat 3 — decode the supremum
        br_sup = Brace(ville[2], UP, color=VAR)
        sup_lab = Text("the largest value the wealth ever takes",
                       font_size=23, color=VAR).next_to(br_sup, UP, buff=0.15)
        num = MathTex(r"\tfrac{1}{\alpha} = 20 \;\Rightarrow\; \Pr \le \tfrac{1}{20}")\
            .scale(0.9).set_color(EIG).next_to(cond, DOWN, buff=0.4)
        self.play_beat(GrowFromCenter(br_sup), FadeIn(sup_lab), FadeIn(num))  # beat 3

        # beat 4 — define the stopping time tau
        self.play(FadeOut(VGroup(ville, cond, br_sup, sup_lab, num)), run_time=0.5)
        head = Text("Why it's true — the gist", font_size=26, color=DIM)\
            .to_edge(UP, buff=1.0)
        tau = MathTex(r"\tau", r"=\ \text{first round with } W_t \ge \tfrac{1}{\alpha}")\
            .scale(1.05).shift(UP * 0.8)
        tau[0].set_color(BAD)
        tau_cap = MathTex(r"(\tau = \infty \text{ if it never crosses})")\
            .scale(0.85).set_color(DIM).next_to(tau, DOWN, buff=0.35)
        self.play_beat(FadeIn(head), Write(tau), FadeIn(tau_cap))          # beat 4

        # beat 5 — the event equivalence
        self.play(FadeOut(VGroup(tau, tau_cap)), run_time=0.4)
        equiv = MathTex(r"\big\{", r"\sup_t W_t \ge \tfrac{1}{\alpha}",
                        r"\big\}", "=", r"\big\{", r"\tau < \infty", r"\big\}")\
            .scale(1.1).shift(UP * 0.8)
        equiv[1].set_color(VAR); equiv[5].set_color(BAD)
        eq_cap = Text("a supremum is crossed iff there is a first crossing",
                      font_size=23, color=DIM).next_to(equiv, DOWN, buff=0.4)
        self.play_beat(Write(equiv), FadeIn(eq_cap))                       # beat 5

        # beat 6 — optional stopping bound
        self.play(FadeOut(VGroup(equiv, eq_cap)), run_time=0.4)
        os = MathTex(r"\mathbb{E}", r"\big[", r"W_{\min(t,\tau)}", r"\big]",
                     r"\leq", "1").scale(1.15).shift(UP * 1.0)
        os[2].set_color(VAR); os[5].set_color(RES)
        on = MathTex(r"\text{on } \{\tau \le t\}:\quad W_{\min(t,\tau)} \ge \tfrac{1}{\alpha}")\
            .scale(0.9).set_color(EIG).next_to(os, DOWN, buff=0.45)
        self.play_beat(Write(os), FadeIn(on))                             # beat 6

        # beat 7 — the inequality chain
        self.play(FadeOut(VGroup(os, on)), run_time=0.4)
        chain = MathTex("1", r"\geq", r"\mathbb{E}\big[W_{\min(t,\tau)}\big]",
                        r"\geq", r"\tfrac{1}{\alpha}", r"\Pr(\tau \le t)")\
            .scale(1.05).shift(UP * 0.9)
        chain[4].set_color(EIG); chain[5].set_color(BAD)
        rearr = MathTex(r"\Pr(\tau \le t)", r"\leq", r"\alpha",
                        r"\quad \text{for every } t").scale(1.0)\
            .next_to(chain, DOWN, buff=0.5)
        rearr[2].set_color(RES)
        self.play_beat(Write(chain), FadeIn(rearr))                        # beat 7

        # beat 8 — limit and the hinge
        self.play(FadeOut(VGroup(chain, rearr, head)), run_time=0.4)
        lim = MathTex(r"t \to \infty:\quad", r"\Pr(\tau < \infty)", r"\leq",
                      r"\alpha").scale(1.2).shift(UP * 0.7)
        lim[1].set_color(BAD); lim[3].set_color(RES)
        hinge = Text("non-negativity is the hinge it turns on",
                     font_size=27, color=BAD).next_to(lim, DOWN, buff=0.6)
        self.play_beat(Write(lim), FadeIn(hinge))                          # beat 8


# ----------------------------------------------------------------------
# Scene 4 — supermartingales and composite nulls  (7 beats)
# ----------------------------------------------------------------------
class S4_Supermartingale(NarratedScene):
    scene_key = "S4_Supermartingale"

    def construct(self):
        self.header("Supermartingales and composite nulls")

        # beat 1 — composite null is a set
        comp = VGroup(
            Text("a composite null is a SET of distributions",
                 font_size=28, color=WHITE),
            MathTex(r"H_0 = \{\, P : \text{nothing is going on} \,\}")
            .scale(1.0).set_color(BACK),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.6)
        self.play_beat(FadeIn(comp, lag_ratio=0.3))                        # beat 1

        # beat 2 — fairness becomes inequality, for every P
        self.play(FadeOut(comp), run_time=0.4)
        forall = MathTex(r"\mathbb{E}_P", r"\big[", "B_s", r"\mid",
                         r"\mathcal{F}_{s-1}", r"\big]", r"\leq", "1",
                         r"\quad \forall\, P \in H_0").scale(1.05).shift(UP * 0.8)
        forall[2].set_color(EIG); forall[6].set_color(RES); forall[7].set_color(RES)
        cap = Text("at most one  —  the inequality, not the equality",
                   font_size=24, color=DIM).next_to(forall, DOWN, buff=0.45)
        self.play_beat(Write(forall), FadeIn(cap))                         # beat 2

        # beat 3 — supermartingale property
        self.play(FadeOut(VGroup(forall, cap)), run_time=0.4)
        sm = MathTex(r"\mathbb{E}", r"\big[", "W_t", r"\mid", r"\text{past}",
                     r"\big]", r"\leq", "W_{t-1}").scale(1.25).shift(UP * 0.9)
        sm[2].set_color(VAR); sm[6].set_color(RES); sm[7].set_color(VAR)
        title = Text("a supermartingale: on average, cannot grow",
                     font_size=27, color=RES).next_to(sm, DOWN, buff=0.5)
        self.play_beat(Write(sm), FadeIn(title))                           # beat 3

        # beat 4 — decode "super"
        br = Brace(sm[7], DOWN, color=VAR)
        decode = Text("the current wealth sits ABOVE its expected future",
                      font_size=24, color=VAR).next_to(br, DOWN, buff=0.2)
        self.play(FadeOut(title), run_time=0.3)
        self.play_beat(GrowFromCenter(br), FadeIn(decode))                 # beat 4

        # beat 5 — why composite forces the direction
        self.play(FadeOut(VGroup(sm, br, decode)), run_time=0.4)
        why = VGroup(
            Text("one bet, fair against MANY distributions at once,",
                 font_size=26, color=WHITE),
            Text("can only leave money on the table — never demand more",
                 font_size=26, color=DIM),
            Text("so fairness can only be  ≤, forcing the supermartingale",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.28).shift(UP * 0.2)
        self.play_beat(FadeIn(why, lag_ratio=0.3))                         # beat 5

        # beat 6 — the one-line derivation
        self.play(FadeOut(why), run_time=0.4)
        deriv = MathTex(r"\mathbb{E}", r"[", "W_{t-1} B_t", r"\mid",
                        r"\mathcal{F}_{t-1}", "]", "=", "W_{t-1}",
                        r"\,\mathbb{E}[B_t \mid \mathcal{F}_{t-1}]",
                        r"\leq", "W_{t-1}").scale(0.9).shift(UP * 0.8)
        deriv[2].set_color(VAR); deriv[7].set_color(VAR); deriv[10].set_color(VAR)
        steps = Text("pull out the known W_{t-1}, then apply fairness to the bet",
                     font_size=23, color=DIM).next_to(deriv, DOWN, buff=0.45)
        self.play_beat(Write(deriv), FadeIn(steps))                        # beat 6

        # beat 7 — Ville still holds
        self.play(FadeOut(VGroup(deriv, steps)), run_time=0.4)
        still = VGroup(
            Text("Ville was stated for non-negative SUPERmartingales",
                 font_size=27, color=WHITE),
            MathTex(r"\Pr_{H_0}\Big(\sup_t W_t \ge \tfrac{1}{\alpha}\Big) \le \alpha")
            .scale(1.05),
            Text("composite nulls cost nothing — same constant alpha",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.35)
        still[1].set_color(EIG)
        self.play_beat(FadeIn(still, lag_ratio=0.3))                       # beat 7


# ----------------------------------------------------------------------
# Scene 5 — optional stopping theorem  (7 beats)
# ----------------------------------------------------------------------
class S5_Stopping(NarratedScene):
    scene_key = "S5_Stopping"

    def construct(self):
        self.header("Optional stopping theorem")

        # beat 1 — intro
        intro = Text("the engine we leaned on inside Ville, stated on its own",
                     font_size=27, color=DIM).shift(UP * 2.3)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # beat 2 — the theorem
        ost = MathTex(r"\mathbb{E}", r"\big[", r"W_\tau", r"\big]",
                      r"\leq", "1").scale(1.5).shift(UP * 0.9)
        ost[2].set_color(VAR); ost[5].set_color(RES)
        cap = Text("at any stopping time tau, for a non-negative supermartingale",
                   font_size=24, color=DIM).next_to(ost, DOWN, buff=0.45)
        self.play_beat(Write(ost), FadeIn(cap), intro.animate.set_opacity(0.4))  # beat 2

        # beat 3 — decode the stopping time
        br = Brace(ost[2], UP, color=BAD)
        tau_lab = VGroup(
            Text("a stopping time: a quit-rule using only the past,",
                 font_size=23, color=BAD),
            Text("never the future", font_size=23, color=BAD),
        ).arrange(DOWN, buff=0.1).next_to(br, UP, buff=0.15)
        self.play_beat(GrowFromCenter(br), FadeIn(tau_lab))                # beat 3

        # beat 4 — the punchline: valid when you stop on the data
        self.play(FadeOut(VGroup(ost, cap, br, tau_lab, intro)), run_time=0.5)
        punch = VGroup(
            Text("the bound that held at every FIXED round", font_size=27, color=DIM),
            Text("still holds at a round you CHOOSE by watching",
                 font_size=27, color=RES),
            Text("the test stays valid when you stop on the data",
                 font_size=27, color=WHITE),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.3)
        self.play_beat(FadeIn(punch, lag_ratio=0.3))                       # beat 4

        # beat 5 — the rule
        self.play(FadeOut(punch), run_time=0.4)
        rule = VGroup(
            MathTex(r"\text{Reject } H_0 \text{ at first } t:\ W_t \ge \tfrac{1}{\alpha}")
            .scale(1.05),
            Text("otherwise keep watching; stop whenever you like",
                 font_size=25, color=DIM),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.4)
        rule[0].set_color(RES)
        self.play_beat(FadeIn(rule, lag_ratio=0.3))                        # beat 5

        # beat 6 — tie three together
        self.play(FadeOut(rule), run_time=0.4)
        tie = VGroup(
            Text("martingale  →  the fair game", font_size=27, color=VAR),
            Text("Ville  →  bounds the running maximum", font_size=27, color=EIG),
            Text("optional stopping  →  the chosen stop stays honest",
                 font_size=27, color=BACK),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(tie, lag_ratio=0.3))                         # beat 6

        # beat 7 — one picture: anytime validity
        self.play(FadeOut(tie), run_time=0.4)
        av = VGroup(
            Text("ANYTIME-VALIDITY", font_size=34, color=RES),
            MathTex(r"\text{type-I error} \;\le\; \alpha").scale(1.2),
            Text("no matter when or how often you look", font_size=26, color=WHITE),
            Text("safe peeking, in one theorem", font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.3)
        av[1].set_color(EIG)
        self.play_beat(FadeIn(av, lag_ratio=0.3))                          # beat 7


# ----------------------------------------------------------------------
# Scene 6 — why this is the engine  (7 beats)
# ----------------------------------------------------------------------
class S6_Why(NarratedScene):
    scene_key = "S6_Why"

    def construct(self):
        self.header("Why this is the engine")

        # beat 1 — step back
        back = Text("one structure underwrites this whole volume",
                    font_size=30, color=WHITE).shift(UP * 1.4)
        self.play_beat(FadeIn(back))                                       # beat 1

        # beat 2 — the atom: each bet is an e-value
        atom = MathTex(r"B_s \ge 0,\qquad \mathbb{E}[B_s \mid \mathcal{F}_{s-1}] \le 1")\
            .scale(1.05).shift(UP * 0.2)
        atom.set_color(EIG)
        atom_cap = Text("each bet is an e-value, conditionally  —  the atom of evidence",
                        font_size=24, color=DIM).next_to(atom, DOWN, buff=0.4)
        self.play_beat(Write(atom), FadeIn(atom_cap),
                       back.animate.set_opacity(0.4))                      # beat 2

        # beat 3 — multiply -> test martingale
        self.play(FadeOut(VGroup(atom, atom_cap, back)), run_time=0.4)
        mult = MathTex(r"W_t = \prod_{s=1}^{t} B_s", r"\quad\Rightarrow\quad",
                       r"\mathbb{E}_{H_0}[W_t] \le 1").scale(1.05).shift(UP * 0.5)
        mult[0].set_color(VAR); mult[2].set_color(RES)
        mult_cap = Text("multiply the atoms through time: the test martingale",
                        font_size=25, color=WHITE).next_to(mult, DOWN, buff=0.45)
        self.play_beat(Write(mult), FadeIn(mult_cap))                      # beat 3

        # beat 4 — Ville: time-uniform
        self.play(FadeOut(VGroup(mult, mult_cap)), run_time=0.4)
        v = MathTex(r"\Pr_{H_0}\Big(\sup_t W_t \ge \tfrac{1}{\alpha}\Big) \le \alpha")\
            .scale(1.15).shift(UP * 0.5)
        v.set_color(EIG)
        v_cap = Text("Ville: a time-uniform guarantee on the running maximum",
                     font_size=25, color=WHITE).next_to(v, DOWN, buff=0.45)
        self.play_beat(Write(v), FadeIn(v_cap))                            # beat 4

        # beat 5 — optional stopping cashes it
        self.play(FadeOut(VGroup(v, v_cap)), run_time=0.4)
        cash = VGroup(
            Text("optional stopping lets you cash that guarantee",
                 font_size=27, color=WHITE),
            Text("at a moment you choose by watching", font_size=27, color=RES),
            Text("anytime-valid inference, from one clean structure",
                 font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.2)
        self.play_beat(FadeIn(cash, lag_ratio=0.3))                        # beat 5

        # beat 6 — every downstream guarantee is a corollary
        self.play(FadeOut(cash), run_time=0.4)
        cor = VGroup(
            Text("every e-value guarantee downstream:", font_size=27, color=DIM),
            Text("combining cohorts · controlling false discovery · accruing patients",
                 font_size=24, color=WHITE),
            Text("→  a corollary of  martingale + Ville", font_size=28, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.1)
        self.play_beat(FadeIn(cor, lag_ratio=0.3))                         # beat 6

        # beat 7 — name it
        self.play(FadeOut(cor), run_time=0.4)
        name = VGroup(
            Text("The martingale + Ville structure", font_size=32, color=WHITE),
            Text("is the mathematical engine", font_size=32, color=RES),
            Text("of anytime-valid inference.", font_size=32, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(name, lag_ratio=0.3))                        # beat 7
