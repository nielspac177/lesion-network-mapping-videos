"""v0604_class_conditional — "Class-conditional and adaptive sets".

Five narrated scenes for Volume 6 (Conformal). We take the marginal-coverage
guarantee apart along the rare class, build Mondrian (class-conditional)
conformal, the APS adaptive score, read set size as a difficulty meter, then
state the honest cost of conditioning.

All equations/numbers are quoted from:
  volumes/vol6_conformal/chapters/04_class_conditional.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0604_class_conditional ./render.sh \
      chapters/v0604_class_conditional/scenes.py -q ql \
      S1_Problem S2_Mondrian S3_APS S4_SetSize S5_Cost
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Marginal coverage hides gaps
# ----------------------------------------------------------------------
class S1_Problem(NarratedScene):
    scene_key = "S1_Problem"

    def construct(self):
        self.header("Marginal coverage hides gaps")

        # beat 1 — the marginal guarantee
        guar = MathTex(r"\Pr\big(", "Y_{n+1}", r"\in", "C(X_{n+1})", r"\big)",
                       r"\ge", "1-\\alpha").scale(1.1).shift(UP * 1.9)
        guar[1].set_color(VAR); guar[3].set_color(VAR); guar[6].set_color(RES)
        avg = Text("one number — averaged over all patients",
                   font_size=24, color=DIM).next_to(guar, DOWN, buff=0.3)
        self.play_beat(Write(guar), FadeIn(avg))                            # beat 1

        # beat 2 — rare event motivation
        self.play(FadeOut(avg), guar.animate.scale(0.8).to_edge(UP, buff=1.0),
                  run_time=0.5)
        rare = VGroup(
            Text("rare adverse event (severe ataxia)", font_size=26, color=BAD),
            Text("the one patient you cannot afford to under-cover",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.7)
        self.play_beat(FadeIn(rare, shift=UP * 0.2))                        # beat 2

        # beat 3 — define prevalence pi
        self.play(FadeOut(rare), run_time=0.4)
        pi = MathTex(r"\pi", "=", r"\Pr(", "Y_{n+1}", "=", "1", ")").scale(1.1)\
            .shift(UP * 0.9)
        pi[0].set_color(EIG); pi[3].set_color(VAR)
        pi_lab = Text("prevalence: the fraction who get the event",
                      font_size=24, color=EIG).next_to(pi, DOWN, buff=0.3)
        self.play_beat(Write(pi), FadeIn(pi_lab))                           # beat 3

        # beat 4 — total probability decomposition
        self.play(FadeOut(VGroup(pi, pi_lab)), run_time=0.4)
        decomp = MathTex(
            r"\Pr(Y\in C)", "=",
            r"\pi", r"\,\Pr(Y\in C\mid Y{=}1)", "+",
            r"(1-\pi)", r"\,\Pr(Y\in C\mid Y{=}0)"
        ).scale(0.85).shift(UP * 0.9)
        decomp[0].set_color(WHITE); decomp[2].set_color(EIG)
        decomp[3].set_color(BAD); decomp[5].set_color(EIG); decomp[6].set_color(BACK)
        b_marg = Brace(decomp[0], UP, color=WHITE)
        l_marg = Text("marginal", font_size=20, color=WHITE).next_to(b_marg, UP, buff=0.1)
        b_pos = Brace(decomp[3], DOWN, color=BAD)
        l_pos = Text("AE+ coverage", font_size=20, color=BAD).next_to(b_pos, DOWN, buff=0.1)
        self.play_beat(Write(decomp), GrowFromCenter(b_marg), FadeIn(l_marg),
                       GrowFromCenter(b_pos), FadeIn(l_pos))                # beat 4

        # beat 5 — pi tiny, positive term barely counts
        self.play(FadeOut(VGroup(b_marg, l_marg, b_pos, l_pos)), run_time=0.4)
        small = MathTex(r"\pi = 0.08", r"\ \Rightarrow\ ",
                        r"\text{AE+ term}\times 0.08").scale(1.0)
        small[0].set_color(EIG); small[2].set_color(BAD)
        small.next_to(decomp, DOWN, buff=0.6)
        self.play_beat(Write(small))                                       # beat 5

        # beat 6 — the arithmetic
        arith = MathTex(r"0.08\times 0.10", "+", r"0.92\times 0.97", "=",
                        r"0.90").scale(1.0)
        arith[0].set_color(BAD); arith[2].set_color(BACK); arith[4].set_color(RES)
        arith.next_to(small, DOWN, buff=0.5)
        head90 = Text("headline reads ninety percent", font_size=22, color=RES)\
            .next_to(arith, DOWN, buff=0.25)
        self.play_beat(Write(arith), FadeIn(head90))                       # beat 6

        # beat 7 — but AE+ covered only 10%
        self.play(FadeOut(VGroup(decomp, small, arith, head90)), run_time=0.5)
        gap = VGroup(
            MathTex(r"\text{AE- coverage} = 0.97", color=BACK).scale(1.0),
            MathTex(r"\text{AE+ coverage} = 0.10", color=BAD).scale(1.0),
        ).arrange(DOWN, buff=0.35).shift(UP * 0.6)
        banked = Text("coverage banked on the cheap majority",
                      font_size=24, color=DIM).next_to(gap, DOWN, buff=0.4)
        self.play_beat(FadeIn(gap[0]), FadeIn(gap[1], shift=UP * 0.2),
                       FadeIn(banked))                                      # beat 7

        # beat 8 — not a bug; ask by class
        self.play(FadeOut(VGroup(gap, banked, guar)), run_time=0.5)
        moral = VGroup(
            Text("Not a bug — exactly what the theorem promised.",
                 font_size=28, color=WHITE),
            Text("If you need the rare class covered,", font_size=28, color=WHITE),
            Text("ask for it BY CLASS.", font_size=30, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 8


# ----------------------------------------------------------------------
# Scene 2 — Mondrian / class-conditional conformal
# ----------------------------------------------------------------------
class S2_Mondrian(NarratedScene):
    scene_key = "S2_Mondrian"

    def construct(self):
        self.header("Mondrian / class-conditional conformal")

        # beat 1 — two separate piles
        idea = Text("stop blending the classes:\ntwo calibration piles, two thresholds",
                    font_size=28, color=WHITE, line_spacing=0.8).shift(UP * 2.0)
        piles = VGroup(
            self._pile("AE+", BAD),
            self._pile("AE-", BACK),
        ).arrange(RIGHT, buff=1.6).shift(DOWN * 0.4)
        self.play_beat(FadeIn(idea), FadeIn(piles, lag_ratio=0.2))         # beat 1

        # beat 2 — define score s(x,y)
        self.play(FadeOut(VGroup(idea, piles)), run_time=0.5)
        score = MathTex("s", "(", "x", ",", "y", ")").scale(1.3).shift(UP * 1.6)
        score[0].set_color(VAR); score[2].set_color(VAR); score[4].set_color(EIG)
        s_lab = Text("nonconformity score — how STRANGE is label y for features x\nbig = surprising,  small = unsurprising",
                     font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(score, DOWN, buff=0.35)
        self.play_beat(Write(score), FadeIn(s_lab))                        # beat 2

        # beat 3 — the simple score 1 - p_y
        self.play(FadeOut(s_lab), score.animate.to_edge(UP, buff=1.1).scale(0.7),
                  run_time=0.5)
        simple = MathTex("s", "(", "x", ",", "y", ")", "=", "1", "-",
                         r"\hat p_y(x)").scale(1.1).shift(UP * 0.9)
        simple[0].set_color(VAR); simple[9].set_color(EIG)
        brace = Brace(simple[9], DOWN, color=EIG)
        p_lab = Text("model's predicted probability of label y",
                     font_size=22, color=EIG).next_to(brace, DOWN, buff=0.2)
        self.play_beat(Write(simple), GrowFromCenter(brace), FadeIn(p_lab))  # beat 3

        # beat 4 — define n_c and within-class scores
        self.play(FadeOut(VGroup(simple, brace, p_lab, score)), run_time=0.5)
        nc = MathTex("n_c", "=", r"\#\{\,\text{calibration patients in class } c\,\}")\
            .scale(0.95).shift(UP * 1.0)
        nc[0].set_color(EIG)
        wc = MathTex(r"\{\, s_i = s(X_i, Y_i)\ :\ Y_i = c \,\}")\
            .scale(0.95).next_to(nc, DOWN, buff=0.5)
        wc.set_color(WHITE)
        self.play_beat(Write(nc), Write(wc))                               # beat 4

        # beat 5 — per-class threshold quantile
        self.play(FadeOut(VGroup(nc, wc)), run_time=0.5)
        thr = MathTex(r"\hat q_c", "=",
                      r"\big\lceil (1-\alpha)(n_c+1) \big\rceil",
                      r"\text{-th smallest score}").scale(0.9).shift(UP * 1.0)
        thr[0].set_color(RES); thr[2].set_color(EIG)
        note = Text("same quantile index as before —\nnow n_c, the per-class count, replaces n",
                    font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(thr, DOWN, buff=0.4)
        self.play_beat(Write(thr), FadeIn(note))                           # beat 5

        # beat 6 — the prediction set rule
        self.play(FadeOut(VGroup(thr, note)), run_time=0.5)
        cset = MathTex("C(x)", "=", r"\big\{\, y \in \{0,1\}\ :\ ",
                       "s(x,y)", r"\le", r"\hat q_y", r"\,\big\}")\
            .scale(0.95).shift(UP * 0.9)
        cset[0].set_color(VAR); cset[3].set_color(VAR); cset[5].set_color(RES)
        keep = Text("keep each label whose score clears ITS OWN class threshold",
                    font_size=23, color=WHITE).next_to(cset, DOWN, buff=0.4)
        self.play_beat(Write(cset), FadeIn(keep))                          # beat 6

        # beat 7 — read it: AE+ judged only by AE+ threshold
        self.play(FadeOut(keep), run_time=0.4)
        read = MathTex("s(x,1)", r"\ \le\ ", r"\hat q_1").scale(1.1)\
            .next_to(cset, DOWN, buff=0.5)
        read[0].set_color(BAD); read[2].set_color(BAD)
        rlab = Text("AE+ score vs AE+ threshold (built only from AE+ patients)\nthe majority never touches this comparison",
                    font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(read, DOWN, buff=0.3)
        self.play_beat(Write(read), FadeIn(rlab))                          # beat 7

        # beat 8 — why it works: rank argument within class
        self.play(FadeOut(VGroup(cset, read, rlab)), run_time=0.5)
        why = MathTex(
            r"\Pr\big(Y_{n+1}\in C \mid Y_{n+1}=c\big)", r"\ \ge\ ", "1-\\alpha"
        ).scale(0.95).shift(UP * 0.6)
        why[0].set_color(WHITE); why[2].set_color(RES)
        rank = Text("the rank argument, run inside one class:\nthe new score is equally likely at any rank",
                    font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(why, DOWN, buff=0.4)
        self.play_beat(Write(why), FadeIn(rank))                           # beat 8

        # beat 9 — the name "Mondrian"
        self.play(FadeOut(VGroup(why, rank)), run_time=0.5)
        blocks = self._mondrian_blocks().shift(LEFT * 3.2)
        name = VGroup(
            Text("\"Mondrian\" (Vovk):", font_size=27, color=RES),
            Text("carve the data into fixed blocks —", font_size=24, color=WHITE),
            Text("here, by true class —", font_size=24, color=WHITE),
            Text("calibrate each block on its own.", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(RIGHT * 2.4)
        self.play_beat(FadeIn(blocks, lag_ratio=0.1), FadeIn(name, lag_ratio=0.2))  # beat 9

    def _pile(self, label, color):
        box = RoundedRectangle(width=2.6, height=2.0, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.10)
        t = Text(label, font_size=30, color=color).move_to(box.get_top() + DOWN * 0.4)
        dots = VGroup(*[Dot(color=color, radius=0.06) for _ in range(9)])\
            .arrange_in_grid(rows=3, cols=3, buff=0.28)\
            .move_to(box.get_center() + DOWN * 0.25)
        return VGroup(box, t, dots)

    def _mondrian_blocks(self):
        cols = [BAD, BACK, EIG, VAR]
        rects = VGroup()
        x = -1.0
        for w, c in zip([0.9, 0.6, 1.1, 0.7], cols):
            r = Rectangle(width=w, height=1.8, stroke_color=WHITE, stroke_width=2,
                          fill_color=c, fill_opacity=0.25)
            r.move_to([x + w / 2, 0, 0])
            x += w
            rects.add(r)
        return rects


# ----------------------------------------------------------------------
# Scene 3 — Adaptive prediction sets (APS)
# ----------------------------------------------------------------------
class S3_APS(NarratedScene):
    scene_key = "S3_APS"

    def construct(self):
        self.header("Adaptive prediction sets (APS)")

        # beat 1 — 1 - p can be uninformative
        problem = VGroup(
            Text("Mondrian fixed WHO is covered.", font_size=27, color=DIM),
            Text("APS fixes HOW informative the set is.", font_size=27, color=WHITE),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.7)
        bad = MathTex("s = 1 - \\hat p", r"\ \Rightarrow\ ",
                      r"\text{sets that say nothing}").scale(0.95)
        bad[2].set_color(BAD)
        bad.next_to(problem, DOWN, buff=0.5)
        self.play_beat(FadeIn(problem, lag_ratio=0.2), Write(bad))         # beat 1

        # beat 2 — what we want
        self.play(FadeOut(VGroup(problem, bad)), run_time=0.5)
        want = VGroup(
            Text("singleton when the model is confident", font_size=26, color=BACK),
            Text("grows only when the patient is ambiguous", font_size=26, color=RES),
            Text("set size REPORTS difficulty", font_size=27, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(want, lag_ratio=0.25))                       # beat 2

        # beat 3 — the walk-down idea
        self.play(FadeOut(want), run_time=0.4)
        walk = Text("line labels up: most likely  →  least likely\nwalk down, adding probabilities",
                    font_size=27, color=WHITE, line_spacing=0.8).shift(UP * 1.6)
        bars = self._sorted_bars([0.6, 0.3, 0.1]).shift(DOWN * 0.6)
        self.play_beat(FadeIn(walk), FadeIn(bars, lag_ratio=0.2))          # beat 3

        # beat 4 — sorted probs and rank r(y)
        self.play(FadeOut(VGroup(walk, bars)), run_time=0.5)
        srt = MathTex(r"\hat p_{(1)}", r"\ge", r"\hat p_{(2)}", r"\ge", r"\cdots")\
            .scale(1.1).shift(UP * 1.2)
        srt[0].set_color(EIG); srt[2].set_color(EIG)
        ry = MathTex("r(y)", "=", r"\text{rank of label } y\ \ (1=\text{top})")\
            .scale(0.95).next_to(srt, DOWN, buff=0.5)
        ry[0].set_color(VAR)
        self.play_beat(Write(srt), Write(ry))                              # beat 4

        # beat 5 — the APS score formula
        self.play(FadeOut(VGroup(srt, ry)), run_time=0.5)
        aps = MathTex(r"s_{\mathrm{APS}}(x,y)", "=",
                      r"\sum_{k=1}^{r(y)}", r"\hat p_{(k)}(x)").scale(1.1).shift(UP * 1.0)
        aps[0].set_color(VAR); aps[3].set_color(EIG)
        brace = Brace(aps[2:], DOWN, color=WHITE)
        b_lab = Text("cumulative mass through label y —\nthe running total when you include it",
                     font_size=22, color=WHITE, line_spacing=0.8)\
            .next_to(brace, DOWN, buff=0.25)
        self.play_beat(Write(aps), GrowFromCenter(brace), FadeIn(b_lab))   # beat 5

        # beat 6 — binary worked example
        self.play(FadeOut(VGroup(aps, brace, b_lab)), run_time=0.5)
        ex = VGroup(
            MathTex(r"\hat p_0 = 0.8,\quad \hat p_1 = 0.2").scale(1.0),
            MathTex(r"s_{\mathrm{APS}}(x,0) = 0.8").scale(1.0),
            MathTex(r"s_{\mathrm{APS}}(x,1) = 0.8 + 0.2 = 1.0").scale(1.0),
        ).arrange(DOWN, buff=0.35)
        ex[0].set_color(EIG); ex[1].set_color(BACK); ex[2].set_color(BAD)
        self.play_beat(LaggedStart(*[Write(e) for e in ex], lag_ratio=0.3))  # beat 6

        # beat 7 — set membership thresholds
        self.play(ex.animate.scale(0.7).to_edge(UP, buff=1.1), run_time=0.5)
        rule = VGroup(
            MathTex(r"\hat q \ge 0.8", r"\ \Rightarrow\ ", r"\{\text{AE-}\}").scale(1.0),
            MathTex(r"\hat q \ge 1.0", r"\ \Rightarrow\ ", r"\{\text{AE-},\text{AE+}\}").scale(1.0),
        ).arrange(DOWN, buff=0.4).shift(DOWN * 0.2)
        rule[0][0].set_color(RES); rule[0][2].set_color(BACK)
        rule[1][0].set_color(RES); rule[1][2].set_color(WHITE)
        single = Text("a confident patient gets a singleton",
                      font_size=24, color=DIM).next_to(rule, DOWN, buff=0.4)
        self.play_beat(Write(rule), FadeIn(single))                        # beat 7

        # beat 8 — exactness
        self.play(FadeOut(VGroup(ex, rule, single)), run_time=0.5)
        exact = MathTex(r"\Pr\big(Y_{n+1}\in C(X_{n+1})\big)", "=", "1-\\alpha")\
            .scale(1.1).shift(UP * 0.5)
        exact[0].set_color(WHITE); exact[2].set_color(RES)
        box = SurroundingRectangle(exact, color=RES, buff=0.2)
        cap = Text("with the randomized tie-break: exact, on the nose —\nnot just \"at least\"",
                   font_size=23, color=DIM, line_spacing=0.8)\
            .next_to(box, DOWN, buff=0.4)
        self.play_beat(Write(exact), Create(box), FadeIn(cap))             # beat 8

    def _sorted_bars(self, ps):
        grp = VGroup()
        for i, p in enumerate(ps):
            bar = Rectangle(width=4 * p, height=0.5, stroke_width=0,
                            fill_color=EIG, fill_opacity=0.8)
            lab = MathTex(rf"\hat p_{{({i+1})}}={p}").scale(0.6).next_to(bar, RIGHT, buff=0.2)
            row = VGroup(bar, lab)
            bar.align_to(grp, LEFT) if i else None
            grp.add(row)
        grp.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        return grp


# ----------------------------------------------------------------------
# Scene 4 — Set size as difficulty
# ----------------------------------------------------------------------
class S4_SetSize(NarratedScene):
    scene_key = "S4_SetSize"

    def construct(self):
        self.header("Set size as difficulty")

        # beat 1 — watch three patients
        intro = Text("set width reports difficulty —\nwatch three patients",
                     font_size=28, color=WHITE, line_spacing=0.8).shift(UP * 2.3)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # beat 2 — P1 confident
        p1 = self._patient("P1", 0.95, 0.05, "singleton", BACK).shift(UP * 0.9)
        self.play_beat(FadeIn(p1, shift=UP * 0.2), intro.animate.set_opacity(0.4))  # beat 2

        # beat 3 — P3 confident other way
        p3 = self._patient("P3", 0.20, 0.80, "singleton", BACK).shift(DOWN * 0.5)
        self.play_beat(FadeIn(p3, shift=UP * 0.2))                         # beat 3

        # beat 4 — P2 fence-sitter
        self.play(FadeOut(VGroup(intro, p1, p3)), run_time=0.5)
        p2 = self._patient("P2", 0.55, 0.45, "two labels", BAD).shift(UP * 0.7)
        torn = Text("the fence-sitter earns the two-label set,\nadmitting the genuine doubt",
                    font_size=24, color=DIM, line_spacing=0.8)\
            .next_to(p2, DOWN, buff=0.5)
        self.play_beat(FadeIn(p2, shift=UP * 0.2), FadeIn(torn))           # beat 4

        # beat 5 — sharpness
        self.play(FadeOut(VGroup(p2, torn)), run_time=0.5)
        sharp = VGroup(
            Text("SHARPNESS", font_size=30, color=RES),
            Text("spend extra width only where it is honestly needed",
                 font_size=25, color=WHITE),
            Text("not one-size-fits-all sets that ignore who is hard",
                 font_size=25, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(sharp, lag_ratio=0.25))                      # beat 5

        # beat 6 — singleton fraction
        self.play(FadeOut(sharp), run_time=0.4)
        sf = MathTex(r"\text{singleton fraction}", "=",
                     r"\frac{\#\{\,|C(x)| = 1\,\}}{\#\text{patients}}")\
            .scale(0.95).shift(UP * 0.7)
        sf[2].set_color(RES)
        sf_lab = Text("high singleton fraction WITH valid coverage\n= correct AND sharp",
                      font_size=23, color=DIM, line_spacing=0.8)\
            .next_to(sf, DOWN, buff=0.4)
        self.play_beat(Write(sf), FadeIn(sf_lab))                          # beat 6

        # beat 7 — binary needs randomized tie-break
        self.play(FadeOut(VGroup(sf, sf_lab)), run_time=0.5)
        rnd = MathTex(r"s_{\mathrm{APS}}(x, \text{2nd})", "=",
                      r"\hat p_{(1)}", "+", "U", r"\cdot", r"\hat p_{(2)}")\
            .scale(1.0).shift(UP * 0.6)
        rnd[0].set_color(VAR); rnd[2].set_color(EIG); rnd[4].set_color(BAD)
        rnd[6].set_color(EIG)
        u_lab = MathTex(r"U \sim \mathrm{Uniform}(0,1)").scale(0.85)\
            .set_color(BAD).next_to(rnd, DOWN, buff=0.3)
        why = Text("in the binary case, true two-label width needs this tie-break",
                   font_size=22, color=DIM).next_to(u_lab, DOWN, buff=0.3)
        self.play_beat(Write(rnd), FadeIn(u_lab), FadeIn(why))             # beat 7

        # beat 8 — fence-sitter crosses first
        self.play(FadeOut(VGroup(rnd, u_lab, why)), run_time=0.5)
        cross = VGroup(
            MathTex(r"\text{P2: } 0.55 + 0.5\times 0.45 = 0.775").scale(0.95),
            MathTex(r"\text{P3: } 0.80 + 0.5\times 0.20 = 0.90").scale(0.95),
            Text("P2 gains its second label at a lower threshold",
                 font_size=24, color=WHITE),
            Text("set width tracks the model's actual confusion",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.3)
        cross[0].set_color(BAD); cross[1].set_color(BACK)
        self.play_beat(FadeIn(cross, lag_ratio=0.2))                       # beat 8

    def _patient(self, name, p0, p1, verdict, vcol):
        title = Text(f"{name}", font_size=26, color=WHITE)
        probs = MathTex(rf"\hat p_0={p0},\ \ \hat p_1={p1}").scale(0.9)
        probs.set_color(EIG)
        # a width bar: longer for two labels
        w = 1.0 if verdict == "singleton" else 2.6
        bar = RoundedRectangle(width=w, height=0.45, corner_radius=0.1,
                               stroke_color=vcol, stroke_width=2,
                               fill_color=vcol, fill_opacity=0.2)
        vlab = Text(verdict, font_size=22, color=vcol).next_to(bar, RIGHT, buff=0.3)
        row = VGroup(bar, vlab)
        grp = VGroup(title, probs, row).arrange(DOWN, buff=0.2)
        return grp


# ----------------------------------------------------------------------
# Scene 5 — The cost of conditioning
# ----------------------------------------------------------------------
class S5_Cost(NarratedScene):
    scene_key = "S5_Cost"

    def construct(self):
        self.header("The cost of conditioning")

        # beat 1 — small n_1 is noisy
        cost = VGroup(
            Text("the AE+ threshold is a quantile of only", font_size=26, color=WHITE),
            MathTex("n_1", r"\text{ scores}").scale(1.1),
            Text("small n_1  →  noisy quantile, coarse index", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.3)
        cost[1][0].set_color(EIG)
        self.play_beat(FadeIn(cost, lag_ratio=0.2))                        # beat 1

        # beat 2 — worked pass: AE- index
        self.play(FadeOut(cost), run_time=0.4)
        setup = Text("worked pass:  80 AE-,  12 AE+,  target 90%",
                     font_size=25, color=DIM).shift(UP * 2.0)
        aem = MathTex(r"\lceil 0.9 \times 81 \rceil", "=", "73")\
            .scale(1.1).next_to(setup, DOWN, buff=0.5)
        aem[2].set_color(BACK)
        aem_lab = Text("73rd of 80 AE- scores — plenty of data, stable",
                       font_size=23, color=BACK).next_to(aem, DOWN, buff=0.3)
        self.play_beat(FadeIn(setup), Write(aem), FadeIn(aem_lab))         # beat 2

        # beat 3 — AE+ index = max
        self.play(FadeOut(VGroup(aem, aem_lab)), run_time=0.4)
        aep = MathTex(r"\lceil 0.9 \times 13 \rceil", "=", "12",
                      r"\ =\ \text{the maximum}").scale(1.0).next_to(setup, DOWN, buff=0.5)
        aep[2].set_color(BAD); aep[3].set_color(BAD)
        aep_lab = Text("one atypical AE+ patient sets it —\nreport n_1, call it underpowered",
                       font_size=23, color=DIM, line_spacing=0.8)\
            .next_to(aep, DOWN, buff=0.3)
        self.play_beat(Write(aep), FadeIn(aep_lab))                        # beat 3

        # beat 4 — the wall
        self.play(FadeOut(VGroup(setup, aep, aep_lab)), run_time=0.5)
        wall = MathTex(r"\big\lceil (1-\alpha)(n_1+1) \big\rceil", ">", "n_1")\
            .scale(1.05).shift(UP * 0.9)
        wall[0].set_color(EIG); wall[2].set_color(EIG)
        wall_lab = Text("index points PAST the largest score\nfor 90% coverage: any  n_1 ≤ 8",
                        font_size=24, color=BAD, line_spacing=0.8)\
            .next_to(wall, DOWN, buff=0.4)
        self.play_beat(Write(wall), FadeIn(wall_lab))                      # beat 4

        # beat 5 — honest output below the wall
        self.play(FadeOut(VGroup(wall, wall_lab)), run_time=0.5)
        honest = VGroup(
            Text("below the wall: no finite threshold works", font_size=26, color=WHITE),
            Text("honest output for AE+ = the FULL set", font_size=26, color=RES),
            Text("report \"coverage uninformative\" — don't quote a number you can't back",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(honest, lag_ratio=0.25))                     # beat 5

        # beat 6 — LOO lets every AE+ patient feed the threshold
        self.play(FadeOut(honest), run_time=0.4)
        loo = VGroup(
            Text("leave-one-out: every AE+ patient feeds the threshold",
                 font_size=25, color=WHITE),
            Text("instead of burning half on a held-out split",
                 font_size=24, color=DIM),
            Text("Mondrian and jackknife+ compose cleanly", font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(loo, lag_ratio=0.2))                         # beat 6

        # beat 7 — the honest limit
        self.play(FadeOut(loo), run_time=0.4)
        limit = VGroup(
            Text("THE HONEST LIMIT", font_size=28, color=RES),
            Text("exact conditional coverage for every individual x", font_size=24, color=WHITE),
            Text("is impossible distribution-free", font_size=25, color=BAD),
            Text("per-class coverage: yes.   per-person: no, without assumptions.",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.25)
        self.play_beat(FadeIn(limit, lag_ratio=0.2))                       # beat 7

        # beat 8 — don't over-claim guarantees
        self.play(FadeOut(limit), run_time=0.4)
        guar = VGroup(
            MathTex(r"\text{APS (split)}:\ \ \Pr = 1-\alpha\ \ \text{exact}").scale(0.9),
            MathTex(r"\text{jackknife+}:\ \ \Pr \ge 1-2\alpha\ \ \text{floor}").scale(0.9),
            Text("there is no per-individual theorem to write",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.35)
        guar[0].set_color(RES); guar[1].set_color(BACK)
        self.play_beat(FadeIn(guar, lag_ratio=0.25))                       # beat 8
