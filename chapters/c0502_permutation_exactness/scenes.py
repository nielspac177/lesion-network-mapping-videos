"""c0502_permutation_exactness — "Permutation exactness (full proof)".

Five narrated scenes. State the symptom-label permutation p-value and the exactness
claim, decode every symbol, lay out the pre-proof strategy (exchangeability ->
rank-uniformity -> the bound), carry the proof step by step with words between each
line, re-name every symbol against the formula, then close on the moral: the test is
distribution-free and exact because its validity rests on the SYMMETRY of the null,
not on a model.

All equations/numbers are quoted from:
  responses/lnm_critique/sections/03_the_right_null.md   (boxed theorem T4 + proof)
  responses/lnm_critique/papers/REBUTTAL_sound.md        (symptom-label null; 0/1000)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0502_permutation_exactness ./render.sh \
      chapters/c0502_permutation_exactness/scenes.py -q ql \
      S1_Statement S2_Strategy S3_Proof S4_Symbols S5_Moral
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the exactness claim, every symbol named
# ----------------------------------------------------------------------
class S1_Statement(NarratedScene):
    scene_key = "S1_Statement"

    def construct(self):
        self.header("The exactness claim")

        intro = Text("the symptom-label null, made exact",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # the permutation p-value
        p = MathTex(
            "p", "=",
            r"\frac{1}{|G|}",
            r"\sum_{\pi \in G}",
            r"\mathbf{1}\!\left[\,",
            "T(y_\\pi)", r"\;\ge\;", "T(y_{\\mathrm{id}})",
            r"\,\right]",
        ).scale(1.15).shift(UP * 1.1)
        p[0].set_color(RES)                 # p
        p[2].set_color(WHITE)               # 1/|G|
        p[3].set_color(WHITE)               # sum over pi
        p[5].set_color(VAR)                 # T(y_pi)
        p[7].set_color(BACK)                # T(y_id)
        self.play_beat(Write(p), intro.animate.set_opacity(0.4))          # beat 2

        # decode the indicator
        br_ind = Brace(VGroup(p[4], p[5], p[6], p[7], p[8]), DOWN, color=DIM)
        ind_lab = Text("one when the relabeled stat meets or beats the observed,\nelse zero",
                       font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(br_ind, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(br_ind), FadeIn(ind_lab))           # beat 3

        # decode G and the sum
        self.play(FadeOut(VGroup(br_ind, ind_lab)), run_time=0.4)
        g_def = VGroup(
            MathTex(r"G \subseteq S_n", color=WHITE).scale(0.95),
            Text("a subgroup of S_n (all n! label permutations) —",
                 font_size=22, color=DIM),
            Text("the relabelings the null treats as equivalent",
                 font_size=22, color=WHITE),
        ).arrange(DOWN, buff=0.18).next_to(p, DOWN, buff=0.5)
        self.play_beat(FadeIn(g_def, lag_ratio=0.3))                      # beat 4

        # |G| size — the count
        self.play(FadeOut(g_def), run_time=0.4)
        size = VGroup(
            MathTex(r"|G|", r"\;=\;", r"\#\,\text{relabelings}",
                    r"\;=\;", r"\tfrac{n!}{n_1!\,n_0!}").scale(0.95),
            Text("two impaired, two spared out of four  →  six",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(p, DOWN, buff=0.6)
        size[0][0].set_color(WHITE)
        size[0][4].set_color(WHITE)
        self.play_beat(FadeIn(size, lag_ratio=0.3))                       # beat 5

        # y_id vs y_pi
        self.play(FadeOut(size), run_time=0.4)
        labels = VGroup(
            MathTex("y_{\\mathrm{id}}", r"\;=\;",
                    r"\text{the observed labeling}").scale(0.95),
            MathTex("y_\\pi", r"\;=\;",
                    r"\text{labels after applying }\pi").scale(0.95),
        ).arrange(DOWN, buff=0.3).next_to(p, DOWN, buff=0.6)
        labels[0][0].set_color(BACK)
        labels[1][0].set_color(VAR)
        self.play_beat(FadeIn(labels, lag_ratio=0.3))                     # beat 6

        # the claim itself
        self.play(FadeOut(labels), p.animate.scale(0.8).to_edge(UP, buff=1.1),
                  run_time=0.5)
        claim = MathTex(r"\Pr\!\big(", "p", r"\le", r"\alpha", r"\big)",
                        r"\;\le\;", r"\alpha").scale(1.25).shift(UP * 0.5)
        claim[1].set_color(RES); claim[3].set_color(EIG); claim[6].set_color(EIG)
        claim_box = SurroundingRectangle(claim, color=RES, buff=0.22)
        claim_cap = Text("under the null  H_0^sym,  for every alpha in [0,1]",
                         font_size=23, color=DIM).next_to(claim_box, DOWN, buff=0.3)
        self.play_beat(Write(claim), Create(claim_box), FadeIn(claim_cap))  # beat 7

        tag = VGroup(
            Text("finite-sample", font_size=24, color=BACK),
            Text("·", font_size=24, color=DIM),
            Text("distribution-free", font_size=24, color=BACK),
            Text("·", font_size=24, color=DIM),
            Text("exact", font_size=24, color=RES),
        ).arrange(RIGHT, buff=0.3).next_to(claim_cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(tag, lag_ratio=0.2))                        # beat 8


# ----------------------------------------------------------------------
# Scene 2 — pre-proof strategy
# ----------------------------------------------------------------------
class S2_Strategy(NarratedScene):
    scene_key = "S2_Strategy"

    def construct(self):
        self.header("Pre-proof strategy")

        intro = Text("one word does all the work:  exchangeable",
                     font_size=28, color=RES).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # exchangeability defined
        exch = MathTex("y", r"\stackrel{d}{=}", "y_\\pi",
                       r"\quad\text{for every }\pi \in G").scale(1.1).shift(UP * 1.4)
        exch[0].set_color(WHITE); exch[2].set_color(VAR)
        exch_cap = Text("every assignment of the observed labels is equally likely",
                        font_size=23, color=DIM).next_to(exch, DOWN, buff=0.3)
        self.play_beat(Write(exch), FadeIn(exch_cap),
                       intro.animate.set_opacity(0.4))                    # beat 2

        # observed is just one draw
        draw = Text("so  T(y_id)  is not privileged — just one draw from the bag",
                    font_size=25, color=WHITE).next_to(exch_cap, DOWN, buff=0.6)
        self.play_beat(FadeIn(draw, shift=UP * 0.2))                      # beat 3

        # the orbit
        self.play(FadeOut(VGroup(exch, exch_cap, draw, intro)), run_time=0.5)
        orbit = MathTex(r"\big\{\,", "T(y_\\pi)", r"\;:\;", r"\pi \in G",
                        r"\,\big\}").scale(1.2).shift(UP * 1.6)
        orbit[1].set_color(VAR)
        orbit_cap = Text("the ORBIT — every element equally likely under the null",
                         font_size=23, color=DIM).next_to(orbit, DOWN, buff=0.3)
        # little dots illustrating equally-likely values
        dots = VGroup(*[
            Dot(radius=0.09, color=VAR) for _ in range(6)
        ]).arrange(RIGHT, buff=0.6).next_to(orbit_cap, DOWN, buff=0.5)
        obs_mark = Dot(radius=0.11, color=BACK).move_to(dots[4])
        self.play_beat(Write(orbit), FadeIn(orbit_cap),
                       FadeIn(dots, lag_ratio=0.15))                      # beat 4

        # uniform rank
        rank = Text("equally likely  ⇒  the rank of the observed value is UNIFORM",
                    font_size=25, color=WHITE).next_to(dots, DOWN, buff=0.6)
        self.play_beat(FadeIn(obs_mark, scale=1.4), FadeIn(rank))         # beat 5

        # uniform rank gives the bound
        self.play(FadeOut(VGroup(orbit, orbit_cap, dots, obs_mark, rank)),
                  run_time=0.5)
        bound = MathTex(r"\text{rank uniform}", r"\;\Rightarrow\;",
                        r"\Pr(\text{top-}\alpha) \le \alpha")\
            .scale(1.05).shift(UP * 0.8)
        bound[2].set_color(RES)
        self.play_beat(Write(bound))                                      # beat 6

        # the three-move plan
        plan = VGroup(
            MathTex(r"\text{exchangeable}", r"\;\Rightarrow\;",
                    r"\text{identically distributed}", color=WHITE).scale(0.85),
            MathTex(r"\text{identically distributed}", r"\;\Rightarrow\;",
                    r"\text{uniform rank}", color=WHITE).scale(0.85),
            MathTex(r"\text{uniform rank}", r"\;\Rightarrow\;",
                    r"\Pr(p \le \alpha) \le \alpha", color=RES).scale(0.85),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(bound, DOWN, buff=0.6)
        self.play_beat(FadeIn(plan, lag_ratio=0.3))                       # beat 7

        miss = Text("nothing in this plan is a MODEL of the maps —\nthe validity will come from symmetry",
                    font_size=23, color=BACK, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.5)
        self.play_beat(FadeIn(miss, shift=UP * 0.2))                      # beat 8


# ----------------------------------------------------------------------
# Scene 3 — the proof
# ----------------------------------------------------------------------
class S3_Proof(NarratedScene):
    scene_key = "S3_Proof"

    def construct(self):
        self.header("The proof")

        assume = Text("Assume  H_0^sym:  the labels are exchangeable over  G",
                      font_size=26, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(assume))                                    # beat 1

        # step 1
        s1 = VGroup(
            Text("Step 1.", font_size=24, color=RES),
            MathTex("y", r"\stackrel{d}{=}", "y_\\pi",
                    r"\ \ \forall\,\pi \in G").scale(0.95),
        ).arrange(RIGHT, buff=0.35).shift(UP * 1.7)
        s1[1][0].set_color(WHITE); s1[1][2].set_color(VAR)
        self.play_beat(FadeIn(s1[0]), Write(s1[1]))                       # beat 2

        # step 2 — push through T
        s2 = VGroup(
            Text("Step 2.", font_size=24, color=RES),
            MathTex("T(y)", r"\stackrel{d}{=}", "T(y_\\pi)").scale(0.95),
        ).arrange(RIGHT, buff=0.35).next_to(s1, DOWN, buff=0.45, aligned_edge=LEFT)
        s2[1][0].set_color(BACK); s2[1][2].set_color(VAR)
        s2_cap = Text("apply the same fixed T to both sides",
                      font_size=21, color=DIM).next_to(s2, RIGHT, buff=0.4)
        self.play_beat(FadeIn(s2[0]), Write(s2[1]), FadeIn(s2_cap))       # beat 3

        # orbit identically distributed
        orb = MathTex(r"\Rightarrow\ ", "T(y_{\\mathrm{id}})",
                      r"\ \text{exchangeable with}\ ", r"\{T(y_\pi)\}")\
            .scale(0.9).next_to(s2, DOWN, buff=0.45, aligned_edge=LEFT)
        orb[1].set_color(BACK); orb[3].set_color(VAR)
        self.play_beat(Write(orb))                                        # beat 4

        # step 3 — uniform rank
        self.play(FadeOut(VGroup(assume, s1, s2, s2_cap, orb)), run_time=0.5)
        s3 = VGroup(
            Text("Step 3.", font_size=24, color=RES),
            MathTex(r"\mathrm{rank}\big(T(y_{\mathrm{id}})\big)",
                    r"\sim", r"\mathrm{Unif}\{1,\dots,|G|\}").scale(0.95),
        ).arrange(RIGHT, buff=0.35).shift(UP * 1.6)
        s3[1][0].set_color(BACK); s3[1][2].set_color(WHITE)
        self.play_beat(FadeIn(s3[0]), Write(s3[1]))                       # beat 5

        # step 4 — p is the upper-tail fraction
        s4 = VGroup(
            Text("Step 4.", font_size=24, color=RES),
            MathTex("p", r"=", r"\frac{\#\{\pi : T(y_\pi) \ge T(y_{\mathrm{id}})\}}{|G|}")
            .scale(0.9),
        ).arrange(RIGHT, buff=0.35).next_to(s3, DOWN, buff=0.55, aligned_edge=LEFT)
        s4[1][0].set_color(RES)
        s4_cap = Text("the p-value is exactly the upper-tail rank",
                      font_size=21, color=DIM).next_to(s4, DOWN, buff=0.25,
                                                       aligned_edge=LEFT)
        self.play_beat(FadeIn(s4[0]), Write(s4[1]), FadeIn(s4_cap))       # beat 6

        # ties -> conservative
        ties = Text("uniform rank  ⇒  Pr(fraction ≤ α) ≤ α;   ties only enlarge p (more conservative)",
                    font_size=22, color=WHITE).to_edge(DOWN, buff=1.1)
        self.play_beat(FadeIn(ties, shift=UP * 0.2))                      # beat 7

        # QED
        qed = MathTex(r"\therefore\ ", r"\Pr\!\big(p \le \alpha\big) \le \alpha",
                      r"\quad\forall\,\alpha", r"\qquad\blacksquare")\
            .scale(1.05).to_edge(DOWN, buff=0.45)
        qed[1].set_color(RES)
        self.play_beat(Write(qed))                                        # beat 8


# ----------------------------------------------------------------------
# Scene 4 — every symbol decoded, tied back to the formula
# ----------------------------------------------------------------------
class S4_Symbols(NarratedScene):
    scene_key = "S4_Symbols"

    def construct(self):
        self.header("Every symbol, decoded")

        # the formula stays up top as the anchor
        p = MathTex(
            "p", "=",
            r"\frac{1}{|G|}",
            r"\sum_{\pi \in G}",
            r"\mathbf{1}\big[\,",
            "T(y_\\pi)", r"\ge", "T(y_{\\mathrm{id}})",
            r"\,\big]",
        ).scale(1.0).to_edge(UP, buff=1.0)
        p[0].set_color(RES); p[5].set_color(VAR); p[7].set_color(BACK)
        self.play_beat(Write(p))                                          # beat 1

        # G
        g = VGroup(
            MathTex("G", color=WHITE).scale(1.1),
            Text("the relabeling group — permutations the null treats as equivalent",
                 font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.4).shift(UP * 0.7)
        self.play_beat(FadeIn(g, shift=RIGHT * 0.2))                      # beat 2

        # |G|
        self.play(g.animate.set_opacity(0.35), run_time=0.3)
        gsz = VGroup(
            MathTex(r"|G|", r"=", r"\tfrac{n!}{n_1!\,n_0!}", color=WHITE).scale(1.0),
            Text("its size: how many relabelings there are",
                 font_size=22, color=DIM),
        ).arrange(RIGHT, buff=0.4).next_to(g, DOWN, buff=0.4)
        self.play_beat(FadeIn(gsz, shift=RIGHT * 0.2))                    # beat 3

        # pi and y_pi
        self.play(gsz.animate.set_opacity(0.35), run_time=0.3)
        pis = VGroup(
            MathTex(r"\pi,\ y_\pi", color=VAR).scale(1.0),
            Text("a permutation of the labels, and the relabeled label vector",
                 font_size=22, color=DIM),
        ).arrange(RIGHT, buff=0.4).next_to(gsz, DOWN, buff=0.4)
        self.play_beat(FadeIn(pis, shift=RIGHT * 0.2))                    # beat 4

        # the indicator
        self.play(pis.animate.set_opacity(0.35), run_time=0.3)
        ind = VGroup(
            MathTex(r"\mathbf{1}[\,\cdot\,]", color=WHITE).scale(1.0),
            Text("the indicator: one if permuted ≥ observed, else zero",
                 font_size=22, color=DIM),
        ).arrange(RIGHT, buff=0.4).next_to(pis, DOWN, buff=0.4)
        self.play_beat(FadeIn(ind, shift=RIGHT * 0.2))                    # beat 5

        # the rank
        self.play(ind.animate.set_opacity(0.35), run_time=0.3)
        rk = VGroup(
            MathTex(r"\mathrm{rank}", color=BACK).scale(1.0),
            Text("where the observed stat sits in the sorted orbit — uniform under H_0",
                 font_size=22, color=DIM),
        ).arrange(RIGHT, buff=0.4).next_to(ind, DOWN, buff=0.4)
        self.play_beat(FadeIn(rk, shift=RIGHT * 0.2))                     # beat 6

        # alpha
        self.play(rk.animate.set_opacity(0.35), run_time=0.3)
        al = VGroup(
            MathTex(r"\alpha", color=EIG).scale(1.1),
            Text("the level chosen in advance — our tolerance for a false alarm",
                 font_size=22, color=DIM),
        ).arrange(RIGHT, buff=0.4).next_to(rk, DOWN, buff=0.4)
        self.play_beat(FadeIn(al, shift=RIGHT * 0.2))                     # beat 7

        # read it back
        self.play(FadeOut(VGroup(g, gsz, pis, ind, rk, al)), run_time=0.5)
        readback = Text(
            "count the relabelings at least as extreme as observed,\n"
            "then divide by how many there are",
            font_size=27, color=WHITE, line_spacing=0.85).shift(DOWN * 0.6)
        self.play_beat(FadeIn(readback, shift=UP * 0.2))                  # beat 8


# ----------------------------------------------------------------------
# Scene 5 — the moral
# ----------------------------------------------------------------------
class S5_Moral(NarratedScene):
    scene_key = "S5_Moral"

    def construct(self):
        self.header("The moral")

        intro = Text("the exactness was purely combinatorial",
                     font_size=30, color=RES).shift(UP * 2.4)
        no = VGroup(
            Text("no normality", font_size=25, color=DIM),
            Text("no large-n", font_size=25, color=DIM),
        ).arrange(RIGHT, buff=0.8).next_to(intro, DOWN, buff=0.4)
        self.play_beat(FadeIn(intro), FadeIn(no, lag_ratio=0.2))          # beat 1

        # didn't care about the maps
        dc = Text("it never asked the maps to be nice —\nbackbone-dominated, ugly, low-rank, shared across disorders: all fine",
                  font_size=24, color=WHITE, line_spacing=0.8).next_to(no, DOWN, buff=0.5)
        self.play_beat(FadeIn(dc, shift=UP * 0.2))                        # beat 2

        # the source of validity
        self.play(FadeOut(VGroup(intro, no, dc)), run_time=0.5)
        src = VGroup(
            Text("validity comes from", font_size=27, color=DIM),
            Text("the SYMMETRY of the null", font_size=32, color=RES),
            Text("not from a model of the data", font_size=27, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.1)
        self.play_beat(FadeIn(src[1], scale=1.1),
                       FadeIn(src[0]), FadeIn(src[2]))                    # beat 3

        # contrast the two nulls
        self.play(FadeOut(src), run_time=0.4)
        loc = VGroup(
            Text("LOCATION null", font_size=26, color=BAD),
            Text("\"is this place special?\"", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.15).shift(UP * 1.4 + LEFT * 3.2)
        self.play_beat(FadeIn(loc, shift=UP * 0.2))                       # beat 4

        loc_fail = Text("backbone made every place alike →\nnull glued to the observed value, nothing rejects",
                        font_size=22, color=BAD, line_spacing=0.8)\
            .next_to(loc, DOWN, buff=0.4).shift(RIGHT * 3.2)
        self.play_beat(FadeIn(loc_fail, shift=UP * 0.2))                  # beat 5

        sym = VGroup(
            Text("SYMPTOM null", font_size=26, color=BACK),
            Text("leans on label exchangeability —", font_size=23, color=DIM),
            Text("a symmetry the backbone cannot break (it cancels)",
                 font_size=23, color=BACK),
        ).arrange(DOWN, buff=0.15).next_to(loc_fail, DOWN, buff=0.5)
        self.play_beat(FadeIn(sym, shift=UP * 0.2))                       # beat 6

        # the witness
        self.play(FadeOut(VGroup(loc, loc_fail, sym)), run_time=0.5)
        witness = MathTex(r"t > 10:\quad", r"0\ \text{false positives}",
                          r"\ /\ 1000\ \text{iterations}").scale(1.05).shift(UP * 0.6)
        witness[1].set_color(RES)
        wcap = Text("(Siddiqi et al., the rebuttal, at standard thresholds)",
                    font_size=22, color=DIM).next_to(witness, DOWN, buff=0.3)
        self.play_beat(Write(witness), FadeIn(wcap))                      # beat 7

        moral = VGroup(
            Text("One assumption, defended honestly,", font_size=29, color=WHITE),
            Text("buys an exact test.", font_size=29, color=RES),
        ).arrange(DOWN, buff=0.25).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                      # beat 8
