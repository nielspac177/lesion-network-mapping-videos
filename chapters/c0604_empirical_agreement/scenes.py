"""c0604_empirical_agreement — "Empirical agreement: strip the backbone".

Five narrated scenes on the rare point of agreement in the LNM debate: BOTH the
critique and the rebuttal-adjacent work prescribe removing a low-rank "backbone"
before testing anything. The critique (P1) measures that backbone at 93% of LNM-map
variance; the biological-limits Comment (P3) measures it at 5-7 PCs capturing >90%.
Residualization deletes exactly that agreed-upon nuisance. The only live
disagreement is whether anything SURVIVES the stripping — an empirical question
settled by the contrast under the symptom-label null (same-symptom r = 0.44 vs
degree 0.16; 0 false positives / 1000 iterations at t > 10).

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/04_removing_the_backbone.md
  responses/lnm_critique/papers/P1_critique.md
  responses/lnm_critique/papers/P3_biolimits.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0604_empirical_agreement ./render.sh \
      chapters/c0604_empirical_agreement/scenes.py -q ql \
      S1_Converge S2_P1 S3_P3 S4_Synthesis S5_Takeaway
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Two camps, one prescription
# ----------------------------------------------------------------------
class S1_Converge(NarratedScene):
    scene_key = "S1_Converge"

    def construct(self):
        title = Text("Two camps, one prescription", font_size=40, color=WHITE)
        sub = Text("the rare point of agreement", font_size=24, color=DIM)\
            .next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))            # beat 1
        self.play(title.animate.scale(0.62).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # left camp: the critique
        left = self._camp("THE CRITIQUE", "van den Heuvel et al.",
                          "the map IS the backbone", BAD)
        left.shift(LEFT * 3.5 + DOWN * 0.3)
        self.play_beat(FadeIn(left, shift=RIGHT * 0.2))                      # beat 2

        # right camp: the rebuttal-adjacent work
        right = self._camp("THE REBUTTAL", "Siddiqi et al. (adjacent)",
                           "signal lives OFF the backbone", BACK)
        right.shift(RIGHT * 3.5 + DOWN * 0.3)
        self.play_beat(FadeIn(right, shift=LEFT * 0.2))                      # beat 3

        # the handshake: one shared prescription
        rx = MathTex(r"\Pi_{\mathcal B}^{\perp}", color=EIG).scale(1.3)
        presc = Text("Rx:  remove the backbone first",
                     font_size=27, color=EIG).next_to(rx, RIGHT, buff=0.3)
        hand = VGroup(rx, presc).move_to(DOWN * 0.3)
        bridge = DoubleArrow(left.get_right() + RIGHT * 0.1,
                             right.get_left() + LEFT * 0.1,
                             color=DIM, buff=0.1, stroke_width=3).shift(UP * 1.0)
        self.play_beat(GrowFromCenter(bridge), FadeIn(hand))                # beat 4

        # same scalpel, opposite hope
        self.play(FadeOut(VGroup(bridge, hand)), run_time=0.4)
        hope = VGroup(
            Text("critic strips it: the backbone is ALL there is",
                 font_size=24, color=BAD),
            Text("defender strips it: to reveal what sits on TOP",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 0.2)
        same = Text("same scalpel, opposite hope", font_size=26, color=WHITE)\
            .next_to(hope, DOWN, buff=0.45)
        self.play_beat(FadeIn(hope[0]), FadeIn(hope[1]), FadeIn(same))       # beat 5

        # the plan: both put a number on the backbone
        self.play(FadeOut(VGroup(left, right, hope, same)), run_time=0.5)
        plan = VGroup(
            Text("The agreement is not rhetorical.", font_size=28, color=WHITE),
            Text("Both camps put a NUMBER on the backbone —", font_size=26, color=DIM),
            Text("and the numbers nearly match.", font_size=26, color=EIG),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(plan, lag_ratio=0.3))                         # beat 6

    def _camp(self, title, who, claim, color):
        box = RoundedRectangle(width=4.4, height=2.2, corner_radius=0.15,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.08)
        t = Text(title, font_size=24, color=color)
        w = Text(who, font_size=19, color=DIM)
        c = Text(claim, font_size=20, color=WHITE)
        stack = VGroup(t, w, c).arrange(DOWN, buff=0.22).move_to(box)
        return VGroup(box, stack)


# ----------------------------------------------------------------------
# Scene 2 — P1: 93 percent is connectome
# ----------------------------------------------------------------------
class S2_P1(NarratedScene):
    scene_key = "S2_P1"

    def construct(self):
        self.header("P1: 93 percent is connectome  (P1, p.1243)")

        intro = Text("How big is the backbone? The critique measures it.",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                       # beat 1

        # the regression: map ~ generic connectome properties
        eq = MathTex(r"\widehat{m}", "=", r"\beta_1\,", r"\mathrm{deg}", "+",
                     r"\beta_2\,", r"\mathrm{mod}", "+", r"\beta_3\,",
                     r"\mathrm{grad}").scale(1.0).shift(UP * 1.25)
        eq[0].set_color(VAR); eq[3].set_color(BACK)
        eq[6].set_color(BACK); eq[9].set_color(BACK)
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4))          # beat 2

        # annotate the predictors — all label-free geometry
        brace = Brace(eq[3:], DOWN, color=BACK)
        b_lab = VGroup(
            Text("degree, four modular-degree terms, three gradients",
                 font_size=22, color=BACK),
            Text("generic connectome geometry — NO disease label enters",
                 font_size=21, color=DIM),
        ).arrange(DOWN, buff=0.15).next_to(brace, DOWN, buff=0.2)
        m_brace = Brace(eq[0], UP, color=VAR)
        m_lab = Text("each LNM map", font_size=21, color=VAR)\
            .next_to(m_brace, UP, buff=0.15)
        self.play_beat(GrowFromCenter(brace), FadeIn(b_lab),
                       GrowFromCenter(m_brace), FadeIn(m_lab))              # beat 3

        # the headline number: 93%
        self.play(FadeOut(VGroup(brace, b_lab, m_brace, m_lab, intro)),
                  eq.animate.scale(0.8).to_edge(UP, buff=1.1), run_time=0.5)
        bar = self._variance_bar(0.93, r"93\%",
                                 "of LNM-map variance,  s.d. = 5.0%").shift(UP * 0.4)
        self.play_beat(*[FadeIn(m) for m in bar.submobjects], lag_ratio=0.1)  # beat 4

        slnm = Text("(seventy-nine percent for the symptom-weighted variant, s.d. 10.2%)",
                    font_size=20, color=DIM).next_to(bar, DOWN, buff=0.4)
        read = Text("ninety-three percent of an LNM map IS shared backbone",
                    font_size=25, color=WHITE).next_to(slnm, DOWN, buff=0.35)
        self.play_beat(FadeIn(slnm), FadeIn(read, shift=UP * 0.2))          # beat 5

        # the hinge: that 93% is exactly what residualization removes
        self.play(FadeOut(VGroup(eq, bar, slnm, read)), run_time=0.5)
        hinge = MathTex(r"\tilde m", "=", r"\Pi_{\mathcal B}^{\perp}", "m",
                        r"\quad\text{deletes the}\ ", r"93\%").scale(1.05).shift(UP * 0.7)
        hinge[0].set_color(RES); hinge[2].set_color(EIG); hinge[3].set_color(VAR)
        hinge[5].set_color(BAD)
        hinge_cap = Text("project out the leading connectome modes → the shared bulk is gone, by construction",
                         font_size=21, color=DIM).next_to(hinge, DOWN, buff=0.35)
        self.play_beat(Write(hinge), FadeIn(hinge_cap))                    # beat 6

        moral = Text("the headline number is not an objection to stripping —\nit is the SIZE of the thing both sides agree to strip",
                     font_size=25, color=RES, line_spacing=0.8)\
            .next_to(hinge_cap, DOWN, buff=0.55)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7

    def _variance_bar(self, frac, label_tex, caption):
        w = 8.0
        full = Rectangle(width=w, height=0.55, stroke_color=WHITE, stroke_width=2,
                         fill_opacity=0)
        filled = Rectangle(width=w * frac, height=0.55, stroke_width=0,
                           fill_color=BAD, fill_opacity=0.85)
        filled.align_to(full, LEFT)
        bar = VGroup(full, filled)
        lab = MathTex(label_tex, color=BAD).scale(1.0).next_to(full, UP, buff=0.2)
        cap = Text(caption, font_size=21, color=DIM).next_to(full, DOWN, buff=0.2)
        return VGroup(bar, lab, cap).move_to(ORIGIN)


# ----------------------------------------------------------------------
# Scene 3 — P3: 5 to 7 PCs over 90 percent
# ----------------------------------------------------------------------
class S3_P3(NarratedScene):
    scene_key = "S3_P3"

    def construct(self):
        self.header("P3: 5-7 PCs over 90 percent  (P3, p.1)")

        intro = VGroup(
            Text("A second, independent measurement —", font_size=27, color=DIM),
            Text("Pini, Salvalaggio & Corbetta (the biological-limits Comment)",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.18).shift(UP * 2.3)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # PCA question — every symbol braced before we move on
        q = MathTex(r"m_\ell", r"\;\approx\;",
                    r"\sum_{k=1}^{K}", r"c_k\,", r"u_k").scale(1.15).shift(UP * 1.05)
        q[0].set_color(VAR); q[3].set_color(EIG); q[4].set_color(BACK)
        b_m = Brace(q[0], UP, color=VAR)
        l_m = Text("one LNM map", font_size=20, color=VAR).next_to(b_m, UP, buff=0.12)
        b_u = Brace(q[4], DOWN, color=BACK)
        l_u = Text("u sub k: principal components (eigenvectors of C)",
                   font_size=19, color=BACK).next_to(b_u, DOWN, buff=0.12)
        b_c = Brace(q[3], DOWN, color=EIG)
        l_c = Text("c sub k: how much of each", font_size=19, color=EIG)\
            .next_to(b_c, DOWN, buff=0.12).shift(LEFT * 2.4)
        qcap = Text("K = how many components rebuild the maps?",
                    font_size=22, color=DIM).next_to(l_u, DOWN, buff=0.28)
        self.play_beat(Write(q), GrowFromCenter(b_m), FadeIn(l_m),
                       GrowFromCenter(b_u), FadeIn(l_u),
                       GrowFromCenter(b_c), FadeIn(l_c), FadeIn(qcap))      # beat 2

        # the answer: K = 5 to 7 captures >90%
        self.play(FadeOut(VGroup(intro, qcap, b_m, l_m, b_u, l_u, b_c, l_c)),
                  q.animate.scale(0.8).to_edge(UP, buff=1.1), run_time=0.5)
        ans = MathTex(r"K = 5\text{--}7", r"\ \Longrightarrow\ ",
                      r">90\%", r"\ \text{of variance}").scale(1.15).shift(UP * 0.9)
        ans[0].set_color(BACK); ans[2].set_color(RES)
        box = SurroundingRectangle(ans, color=RES, buff=0.2)
        self.play_beat(Write(ans), Create(box))                            # beat 3

        # 5-7 out of 100,000 voxels -> almost flat
        flat = MathTex(r"5\text{--}7", r"\ \text{directions out of}\ ",
                       r"\sim 10^{5}", r"\ \text{voxels}").scale(0.95)\
            .next_to(box, DOWN, buff=0.5)
        flat[0].set_color(BACK); flat[2].set_color(DIM)
        flat_cap = Text("the maps are almost low-dimensional — that shell IS the backbone",
                        font_size=22, color=DIM).next_to(flat, DOWN, buff=0.3)
        self.play_beat(FadeIn(flat), FadeIn(flat_cap))                     # beat 4

        # the convergence of the two numbers
        self.play(FadeOut(VGroup(ans, box, flat, flat_cap)), run_time=0.5)
        twin = VGroup(
            VGroup(Text("P1", font_size=24, color=BAD),
                   Text("93% = generic connectome properties", font_size=22, color=WHITE))
            .arrange(RIGHT, buff=0.4),
            VGroup(Text("P3", font_size=24, color=BACK),
                   Text(">90% lives in 5-7 components", font_size=22, color=WHITE))
            .arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).shift(UP * 0.7)
        self.play_beat(FadeIn(twin[0]), FadeIn(twin[1], shift=UP * 0.2))    # beat 5

        verdict = Text("two papers, two methods, one verdict: a low-rank backbone dominates",
                       font_size=25, color=RES).next_to(twin, DOWN, buff=0.6)
        survive = Text("strip those components → what survives is where specificity COULD live",
                       font_size=24, color=WHITE).next_to(verdict, DOWN, buff=0.3)
        self.play_beat(FadeIn(verdict), FadeIn(survive, shift=UP * 0.2))    # beat 6

        # P3's own conclusion: nothing it cares about survives -> the empirical claim
        self.play(FadeOut(VGroup(twin, verdict, survive)), run_time=0.5)
        claim = VGroup(
            Text("P3's own conclusion: nothing it cares about survives.",
                 font_size=26, color=BAD),
            Text("That is exactly the empirical claim we will TEST —",
                 font_size=25, color=WHITE),
            Text("not assume.", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(claim, lag_ratio=0.3))                       # beat 7


# ----------------------------------------------------------------------
# Scene 4 — The synthesis
# ----------------------------------------------------------------------
class S4_Synthesis(NarratedScene):
    scene_key = "S4_Synthesis"

    def construct(self):
        self.header("The synthesis")

        agree = VGroup(
            Text("AGREED:", font_size=27, color=BACK),
            Text("the backbone exists, dominates, and should be removed",
                 font_size=25, color=WHITE),
        ).arrange(RIGHT, buff=0.3).shift(UP * 2.3)
        q = Text("So where is the actual disagreement?",
                 font_size=27, color=DIM).next_to(agree, DOWN, buff=0.4)
        self.play_beat(FadeIn(agree), FadeIn(q))                           # beat 1

        # it is about what survives, not whether to strip
        split = VGroup(
            Text("NOT  whether to strip", font_size=26, color=DIM),
            Text("BUT  what survives the stripping", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3).move_to(UP * 0.4)
        resid = MathTex(r"\tilde m", "=", r"\Pi_{\mathcal B}^{\perp} m",
                        r"\ \neq\ 0\,?").scale(1.1).next_to(split, DOWN, buff=0.5)
        resid[0].set_color(RES); resid[2].set_color(VAR)
        self.play_beat(FadeIn(split[0]), FadeIn(split[1]), Write(resid))    # beat 2

        # the two NO answers
        self.play(FadeOut(VGroup(agree, q, split, resid)), run_time=0.5)
        no_side = VGroup(
            Text("\"NO, residual is empty\"", font_size=25, color=BAD),
            Text("P1: every lesion permutation lands back on degree", font_size=21, color=DIM),
            Text("P3: blind to higher-order & dynamic biology", font_size=21, color=DIM),
        ).arrange(DOWN, buff=0.18).shift(UP * 1.5)
        self.play_beat(FadeIn(no_side, shift=UP * 0.2))                    # beat 3

        # the YES answer
        yes_side = VGroup(
            Text("\"YES, signal survives\"", font_size=25, color=BACK),
            Text("rebuttal: real symptom lesions OVERLAP and are NON-random",
                 font_size=21, color=DIM),
            Text("→ they sample a STRUCTURED subset of rows of C, not a uniform sweep",
                 font_size=21, color=DIM),
        ).arrange(DOWN, buff=0.18).next_to(no_side, DOWN, buff=0.5)
        self.play_beat(FadeIn(yes_side, shift=UP * 0.2))                   # beat 4

        # a question of fact needs a test
        self.play(FadeOut(VGroup(no_side, yes_side)), run_time=0.5)
        test = VGroup(
            Text("A question of FACT, not philosophy.", font_size=27, color=WHITE),
            Text("The test: the contrast under the symptom-label null.",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.6)
        self.play_beat(FadeIn(test[0]), FadeIn(test[1], shift=UP * 0.2))    # beat 5

        recipe = VGroup(
            Text("permute symptom labels", font_size=23, color=VAR),
            Text("→ recompute the contrast on the residual", font_size=23, color=WHITE),
            Text("→ does the true labeling stand out from its shuffles?", font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.2).next_to(test, DOWN, buff=0.5)
        self.play_beat(FadeIn(recipe, lag_ratio=0.25))                     # beat 6

        # the measured answer (part 1)
        self.play(FadeOut(VGroup(test, recipe)), run_time=0.5)
        data = VGroup(
            Text("same-symptom", font_size=23, color=DIM),
            MathTex("r = 0.44", color=BACK).scale(1.05),
            Text("to degree backbone", font_size=23, color=DIM),
            MathTex("r = 0.16", color=BAD).scale(1.05),
        ).arrange_in_grid(rows=2, cols=2, buff=(0.6, 0.3)).shift(UP * 0.8)
        self.play_beat(FadeIn(data, lag_ratio=0.15))                       # beat 7

        # the measured answer (part 2): 0 FP / 1000
        witness = MathTex(r"t > 10:\quad", r"0\ \text{false positives}",
                          r"\ /\ 1000\ \text{iterations}").scale(1.0)
        witness[1].set_color(RES)
        witness.next_to(data, DOWN, buff=0.6)
        settled = Text("something DOES survive. The disagreement is settled by data.",
                       font_size=24, color=WHITE).next_to(witness, DOWN, buff=0.4)
        self.play_beat(Write(witness), FadeIn(settled, shift=UP * 0.2))     # beat 8


# ----------------------------------------------------------------------
# Scene 5 — Takeaway
# ----------------------------------------------------------------------
class S5_Takeaway(NarratedScene):
    scene_key = "S5_Takeaway"

    def construct(self):
        self.header("Takeaway")

        head = Text("Residualization is NOT a trick to manufacture signal.",
                    font_size=30, color=WHITE).shift(UP * 2.4)
        self.play_beat(FadeIn(head))                                       # beat 1

        # it removes a known, agreed-upon nuisance
        nuis = VGroup(
            Text("it removes a KNOWN nuisance both sides agree dominates:",
                 font_size=25, color=DIM),
            VGroup(
                Text("P1: 93%", font_size=24, color=BAD),
                Text("•", font_size=24, color=DIM),
                Text("P3: >90% in 5-7 PCs", font_size=24, color=BACK),
            ).arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.9)
        self.play_beat(FadeIn(nuis[0]), FadeIn(nuis[1]))                   # beat 2

        # cannot invent a difference: shared by construction
        shared = MathTex(r"\mathbb{E}[\Pi_{\mathcal B} m \mid y{=}1]", "=",
                         r"\mathbb{E}[\Pi_{\mathcal B} m \mid y{=}0]")\
            .scale(0.95).next_to(nuis, DOWN, buff=0.55)
        shared[0].set_color(BACK); shared[2].set_color(BACK)
        shared_cap = Text("the two groups share the backbone by construction →\nremoving it cannot invent a between-group difference",
                          font_size=21, color=DIM, line_spacing=0.8)\
            .next_to(shared, DOWN, buff=0.3)
        self.play_beat(Write(shared), FadeIn(shared_cap))                  # beat 3

        # the chord/hum: SNR rises by deleting noise
        self.play(FadeOut(VGroup(head, nuis, shared, shared_cap)), run_time=0.5)
        snr = MathTex(r"\mathrm{SNR}_{\tilde m}", r"\;\geq\;",
                      r"\mathrm{SNR}_{m}").scale(1.2).shift(UP * 1.4)
        snr[0].set_color(RES); snr[2].set_color(DIM)
        snr_cap = Text("stop the shared chord from drowning out a faint, genuine hum:\nSNR rises because we delete NOISE, not signal",
                       font_size=22, color=WHITE, line_spacing=0.8)\
            .next_to(snr, DOWN, buff=0.4)
        self.play_beat(Write(snr), FadeIn(snr_cap))                        # beat 4

        # off-backbone signal becomes a clean empirical question
        empq = VGroup(
            Text("Does off-backbone signal exist?", font_size=26, color=WHITE),
            Text("a clean, separate, EMPIRICAL question — for the symptom null",
                 font_size=23, color=RES),
        ).arrange(DOWN, buff=0.3).next_to(snr_cap, DOWN, buff=0.55)
        self.play_beat(FadeIn(empq[0]), FadeIn(empq[1], shift=UP * 0.2))    # beat 5

        # run honestly -> not always empty
        self.play(FadeOut(VGroup(snr, snr_cap, empq)), run_time=0.5)
        result = VGroup(
            Text("Run honestly, the residual is not always empty.",
                 font_size=26, color=WHITE),
            MathTex(r"\text{same-symptom}\ r = 0.44,\quad",
                    r"0\ \text{FP}/1000\ \text{at}\ t>10").scale(0.9),
        ).arrange(DOWN, buff=0.4).shift(UP * 1.0)
        result[1][1].set_color(RES)
        self.play_beat(FadeIn(result[0]), Write(result[1]))                # beat 6

        moral = VGroup(
            Text("Strip the agreed-upon backbone.", font_size=29, color=BACK),
            Text("Then let the symptom null decide what is left.", font_size=29, color=RES),
            Text("Both camps already hold the scalpel.", font_size=27, color=WHITE),
        ).arrange(DOWN, buff=0.32).next_to(result, DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 7
