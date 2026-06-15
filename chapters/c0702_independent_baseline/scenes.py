"""c0702_independent_baseline — "The independent baseline".

Five narrated scenes building the FAIR yardstick for convergence maps. If the K
cohort maps' signs at a voxel were independent fair coins, then the probability
they all agree is exactly 2^(1-K). We set up the model (S1), derive the formula
counting-style (S2), read off K=2/4/8 and watch the curve plunge (S3), state that
in THIS world a big agreement set would be strong evidence (S4), then spring the
catch: real LNM maps are NOT independent — they share the connectome backbone, so
the coin null is wrong and the next chapter replaces it (S5).

All equations/numbers are from:
  responses/lnm_critique/sections/05_the_convergence_trap.md
  ("Baseline 1: if the maps were independent coins, agreement would be rare")

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0702_independent_baseline ./render.sh \
      chapters/c0702_independent_baseline/scenes.py -q ql \
      S1_Setup S2_Derive S3_Numbers S4_SoFar S5_Catch
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — set up the independent fair-coin model
# ----------------------------------------------------------------------
class S1_Setup(NarratedScene):
    scene_key = "S1_Setup"

    def construct(self):
        title = Text("If maps were independent", font_size=42, color=WHITE)
        sub = Text("building a fair yardstick for agreement",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # one voxel, K studies each with a sign
        voxel = VGroup(
            Square(side_length=0.7, stroke_color=VAR, stroke_width=3,
                   fill_color=VAR, fill_opacity=0.12),
            Text("one\nvoxel", font_size=18, color=VAR, line_spacing=0.8),
        )
        voxel[1].move_to(voxel[0])
        voxel.shift(LEFT * 4.3 + UP * 0.2)
        signs = VGroup(*[
            self._sign_chip(f"study {k}", s)
            for k, s in [(1, "+"), (2, "-"), (3, "+"), (4, "+")]
        ]).arrange(DOWN, buff=0.3).shift(RIGHT * 2.0 + UP * 0.2)
        arrows = VGroup(*[
            Arrow(voxel.get_right(), chip.get_left(), color=DIM,
                  stroke_width=2, buff=0.15)
            for chip in signs.submobjects
        ])
        self.play_beat(FadeIn(voxel), GrowArrow(arrows[0]),
                       FadeIn(signs[0]))                                    # beat 2

        # the clean assumption: independent fair coins
        coin = MathTex(r"\text{sign } r_k(v) \in \{\,+,\ -\,\}")\
            .scale(0.95).shift(DOWN * 1.7)
        coin.set_color(WHITE)
        self.play_beat(LaggedStart(*[GrowArrow(a) for a in arrows[1:]],
                                   *[FadeIn(c) for c in signs[1:]],
                                   lag_ratio=0.2),
                       FadeIn(coin))                                        # beat 3

        # P(+) = P(-) = 1/2
        self.play(FadeOut(VGroup(voxel, signs, arrows, coin)), run_time=0.5)
        prob = MathTex(r"\Pr[\,+\,]", "=", r"\Pr[\,-\,]", "=", r"\tfrac{1}{2}")\
            .scale(1.3).shift(UP * 0.5)
        prob[0].set_color(VAR); prob[2].set_color(VAR); prob[4].set_color(EIG)
        b = Brace(prob[4], DOWN, color=EIG)
        b_lab = Text("a fair coin: equally likely either way",
                     font_size=22, color=EIG).next_to(b, DOWN, buff=0.2)
        self.play_beat(Write(prob), GrowFromCenter(b), FadeIn(b_lab))       # beat 4

        # independence across k
        self.play(FadeOut(VGroup(prob, b, b_lab)), run_time=0.4)
        indep = MathTex(r"\text{sign } r_1, \text{sign } r_2, \dots, "
                        r"\text{sign } r_K", r"\ :\ ",
                        r"\text{independent}").scale(0.95).shift(UP * 0.6)
        indep[0].set_color(VAR); indep[2].set_color(BACK)
        cap = Text("study one's sign tells you nothing about study two's",
                   font_size=23, color=DIM).next_to(indep, DOWN, buff=0.35)
        self.play_beat(Write(indep), FadeIn(cap))                          # beat 5

        moral = Text("no common cheat sheet  —  the honest baseline",
                     font_size=26, color=BACK).next_to(cap, DOWN, buff=0.55)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 6

    def _sign_chip(self, label, sign):
        col = BACK if sign == "+" else BAD
        box = RoundedRectangle(width=2.2, height=0.62, corner_radius=0.12,
                               stroke_color=col, stroke_width=2,
                               fill_color=col, fill_opacity=0.12)
        t = Text(f"{label}:  {sign}", font_size=20, color=col).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 2 — derive Pr[all K agree] = 2^(1-K)
# ----------------------------------------------------------------------
class S2_Derive(NarratedScene):
    scene_key = "S2_Derive"

    def construct(self):
        self.header("Probability all K agree")

        # the question
        q = MathTex(r"\Pr\big[\,\text{all } K \text{ signs agree}\,\big]")\
            .scale(1.2).shift(UP * 2.2)
        q.set_color(WHITE)
        self.play_beat(Write(q))                                           # beat 1

        # two clean events
        events = VGroup(
            self._evt("all +", BACK),
            MathTex(r"\text{or}", color=DIM).scale(0.9),
            self._evt("all -", BAD),
        ).arrange(RIGHT, buff=0.7).shift(UP * 0.7)
        self.play_beat(FadeIn(events, lag_ratio=0.3))                      # beat 2

        # fix study 1, others must match
        self.play(events.animate.scale(0.8).shift(UP * 0.5), run_time=0.4)
        ref = MathTex(r"\underbrace{+}_{\text{study }1}",
                      r"\ \ \to\ \ ",
                      r"\text{the other } K-1 \text{ must match}")\
            .scale(0.9).shift(DOWN * 0.2)
        ref[0].set_color(EIG); ref[2].set_color(WHITE)
        each = MathTex(r"\text{each matches with prob } \tfrac{1}{2}")\
            .scale(0.85).set_color(VAR).next_to(ref, DOWN, buff=0.35)
        self.play_beat(Write(ref), FadeIn(each))                           # beat 3

        # multiply the (K-1) halves -> one block = (1/2)^(K-1)... shown as (1/2)^K with the ref coin
        self.play(FadeOut(VGroup(q, events, ref, each)), run_time=0.5)
        block_p = MathTex(r"\Pr[\text{all }+]", "=",
                          r"\Big(\tfrac{1}{2}\Big)^{K}").scale(1.0)
        block_p[0].set_color(BACK); block_p[2].set_color(EIG)
        block_m = MathTex(r"\Pr[\text{all }-]", "=",
                          r"\Big(\tfrac{1}{2}\Big)^{K}").scale(1.0)
        block_m[0].set_color(BAD); block_m[2].set_color(EIG)
        block = VGroup(block_p, block_m).arrange(RIGHT, buff=1.0).shift(UP * 0.7)
        cap = Text("each of the K coins lands on the shared sign",
                   font_size=22, color=DIM).next_to(block, DOWN, buff=0.35)
        self.play_beat(Write(block), FadeIn(cap))                          # beat 4

        # disjoint -> add -> 2*(1/2)^K = 2^(1-K)
        self.play(FadeOut(cap), block.animate.scale(0.8).to_edge(UP, buff=1.3),
                  run_time=0.5)
        add = MathTex(r"\Pr[\text{all agree}]", "=",
                      r"\Big(\tfrac{1}{2}\Big)^{K}", "+",
                      r"\Big(\tfrac{1}{2}\Big)^{K}", "=",
                      r"2\cdot\Big(\tfrac{1}{2}\Big)^{K}", "=",
                      r"2^{\,1-K}").scale(1.0).shift(UP * 0.2)
        add[0].set_color(WHITE); add[2].set_color(EIG); add[4].set_color(EIG)
        add[6].set_color(EIG); add[8].set_color(RES)
        boxr = SurroundingRectangle(add[8], color=RES, buff=0.15)
        self.play_beat(Write(add), Create(boxr))                           # beat 5

        # decode the exponent
        brace = Brace(add[8], DOWN, color=RES)
        decode = VGroup(
            Text("the 1: from doubling (+ or -)", font_size=22, color=DIM),
            Text("the -K: the cost of all K coins lining up", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).next_to(brace, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace), FadeIn(decode))              # beat 6

        # conclusion: expected fraction shrinks geometrically
        self.play(FadeOut(VGroup(block, add, boxr, brace, decode)),
                  run_time=0.5)
        concl = VGroup(
            Text("expected fraction of the brain that converges", font_size=25, color=WHITE),
            MathTex(r"=\ 2^{\,1-K}\ \ \longrightarrow\ \ \text{shrinks geometrically in } K",
                    color=RES).scale(0.95),
        ).arrange(DOWN, buff=0.4)
        self.play_beat(FadeIn(concl, lag_ratio=0.3))                       # beat 7

    def _evt(self, label, col):
        box = RoundedRectangle(width=1.9, height=0.7, corner_radius=0.12,
                               stroke_color=col, stroke_width=2,
                               fill_color=col, fill_opacity=0.12)
        t = Text(label, font_size=24, color=col).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 3 — the numbers, the curve drops fast
# ----------------------------------------------------------------------
class S3_Numbers(NarratedScene):
    scene_key = "S3_Numbers"

    def construct(self):
        self.header("The numbers")

        formula = MathTex(r"\Pr[\text{all } K \text{ agree}]", "=", r"2^{\,1-K}")\
            .scale(1.0).to_edge(UP, buff=1.0)
        formula[2].set_color(RES)
        self.add(formula)

        # K=2 -> 1/2
        row2 = self._row(r"K = 2", r"2^{\,1-2} = \tfrac{1}{2}", r"50\%")
        row2.shift(UP * 1.4)
        self.play_beat(Write(row2))                                        # beat 1

        # K=4 -> 12.5%
        row4 = self._row(r"K = 4", r"2^{-3} = \tfrac{1}{8}", r"12.5\%")
        row4.shift(UP * 0.3)
        self.play_beat(Write(row4))                                        # beat 2

        # K=8 -> 0.8%
        row8 = self._row(r"K = 8", r"2^{-7}", r"\approx 0.8\%")
        row8.shift(DOWN * 0.8)
        self.play_beat(Write(row8))                                        # beat 3

        # the curve
        self.play(FadeOut(VGroup(row2, row4, row8)),
                  formula.animate.scale(0.85).to_corner(UL).shift(DOWN * 0.4),
                  run_time=0.5)
        ax = Axes(x_range=[2, 8, 1], y_range=[0, 0.5, 0.1],
                  x_length=7.5, y_length=4.0,
                  axis_config={"color": DIM, "include_tip": False,
                               "font_size": 22}).shift(DOWN * 0.4)
        xlab = Text("number of studies  K", font_size=22, color=DIM)\
            .next_to(ax, DOWN, buff=0.2)
        ylab = Text("Pr[all agree]", font_size=22, color=DIM)\
            .rotate(PI / 2).next_to(ax, LEFT, buff=0.15)
        curve = ax.plot(lambda k: 2 ** (1 - k), x_range=[2, 8], color=RES)
        dots = VGroup(*[
            Dot(ax.c2p(k, 2 ** (1 - k)), color=BAD, radius=0.06)
            for k in (2, 4, 8)
        ])
        self.play_beat(Create(ax), FadeIn(xlab), FadeIn(ylab),
                       Create(curve), FadeIn(dots))                        # beat 4

        # impressive in this world
        msg = Text("in the independent world, unanimous agreement is RARE",
                   font_size=25, color=BACK).to_edge(DOWN, buff=0.55)
        self.play_beat(FadeIn(msg, shift=UP * 0.2))                        # beat 5

        self.play(FadeOut(msg), run_time=0.3)
        msg2 = Text("a big convergence set would beat chance  →  a real signal",
                    font_size=25, color=RES).to_edge(DOWN, buff=0.55)
        self.play_beat(FadeIn(msg2, shift=UP * 0.2))                       # beat 6

    def _row(self, k, mid, pct):
        km = MathTex(k).scale(1.0).set_color(VAR)
        m = MathTex(mid).scale(1.0).set_color(EIG)
        p = MathTex(pct).scale(1.1).set_color(RES)
        return VGroup(km, m, p).arrange(RIGHT, buff=1.1)


# ----------------------------------------------------------------------
# Scene 4 — so agreement looks like strong evidence
# ----------------------------------------------------------------------
class S4_SoFar(NarratedScene):
    scene_key = "S4_SoFar"

    def construct(self):
        self.header("So agreement looks impressive")

        # IF the model held -> strong evidence
        head = VGroup(
            Text("IF the independence model held...", font_size=28, color=DIM),
            Text("a lit-up convergence map = strong evidence", font_size=29, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.9)
        self.play_beat(FadeIn(head[0]), FadeIn(head[1], shift=UP * 0.2))    # beat 1

        beat = MathTex(r"\text{big agreement set}", r"\ \gg\ ", r"2^{\,1-K}")\
            .scale(1.0).shift(UP * 0.5)
        beat[0].set_color(WHITE); beat[2].set_color(RES)
        cap = Text("many maps, separately derived, all pointing the same way",
                   font_size=23, color=DIM).next_to(beat, DOWN, buff=0.3)
        self.play_beat(Write(beat), FadeIn(cap))                           # beat 2

        intuition = Text("feels like the disease network shining through",
                         font_size=25, color=WHITE).next_to(cap, DOWN, buff=0.55)
        self.play_beat(FadeIn(intuition, shift=UP * 0.2))                  # beat 3

        # the implicit assumption
        self.play(FadeOut(VGroup(head, beat, cap, intuition)), run_time=0.5)
        implicit = VGroup(
            Text("This is the implicit assumption behind", font_size=27, color=WHITE),
            Text("reading convergence as validation.", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.0)
        self.play_beat(FadeIn(implicit, shift=UP * 0.2))                   # beat 4

        rests = MathTex(r"\text{the inference rests on:}", r"\ \ ",
                        r"\text{maps are independent coins}")\
            .scale(0.9).next_to(implicit, DOWN, buff=0.6)
        rests[0].set_color(DIM); rests[2].set_color(BACK)
        box = SurroundingRectangle(rests[2], color=BACK, buff=0.15)
        self.play_beat(Write(rests), Create(box))                          # beat 5

        ask = Text("name it explicitly  →  now we can ask: is it true for LNM?",
                   font_size=25, color=WHITE).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(ask, shift=UP * 0.2))                        # beat 6


# ----------------------------------------------------------------------
# Scene 5 — the catch: not independent, they share the backbone
# ----------------------------------------------------------------------
class S5_Catch(NarratedScene):
    scene_key = "S5_Catch"

    def construct(self):
        self.header("But are they independent?")

        catch = VGroup(
            Text("The catch:", font_size=30, color=BAD),
            Text("LNM maps are NOT independent coins", font_size=29, color=WHITE),
        ).arrange(DOWN, buff=0.25).shift(UP * 2.2)
        self.play_beat(FadeIn(catch[0]), FadeIn(catch[1], shift=UP * 0.2))  # beat 1

        # same fixed connectome -> shared backbone u_1
        share = MathTex(r"\text{every map computed against the same fixed } C")\
            .scale(0.9).set_color(WHITE).shift(UP * 1.1)
        bb = MathTex(r"\Rightarrow\ \text{they share its backbone }", r"u_1")\
            .scale(0.9).next_to(share, DOWN, buff=0.3)
        bb[1].set_color(BACK)
        self.play_beat(Write(share), Write(bb))                            # beat 2

        # cheat sheet analogy
        self.play(FadeOut(VGroup(share, bb)), run_time=0.4)
        cheat = VGroup(
            Text("every student copied the same cheat sheet", font_size=26, color=WHITE),
            Text("now they all match almost everywhere", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.7)
        self.play_beat(FadeIn(cheat[0]), FadeIn(cheat[1], shift=UP * 0.2))  # beat 3

        tells = Text("the matches tell you they SHARED a sheet,\nnot that anyone understood the material",
                     font_size=25, color=DIM, line_spacing=0.8)\
            .next_to(cheat, DOWN, buff=0.5)
        self.play_beat(FadeIn(tells, shift=UP * 0.2))                      # beat 4

        # the yardstick is wrong
        self.play(FadeOut(VGroup(catch, cheat, tells)), run_time=0.5)
        wrong = MathTex(r"2^{\,1-K}", r"\ \ \text{is the WRONG null}")\
            .scale(1.1).shift(UP * 1.5)
        wrong[0].set_color(RES); wrong[1].set_color(BAD)
        why = Text("it assumes a separateness the maps do not have",
                   font_size=24, color=DIM).next_to(wrong, DOWN, buff=0.3)
        self.play_beat(Write(wrong), FadeIn(why))                          # beat 5

        # next: shared-backbone model (clear the prior block so <=6 mobjects show)
        self.play(FadeOut(VGroup(wrong, why)), run_time=0.4)
        nxt = MathTex(r"r_k(v)", "=", r"\mu(v)", "+", r"\varepsilon_k(v)")\
            .scale(1.25).shift(UP * 0.6)
        nxt[0].set_color(VAR); nxt[2].set_color(BACK); nxt[4].set_color(DIM)
        b0 = Brace(nxt[0], UP, color=VAR)
        l0 = Text("cohort k's map at voxel v", font_size=20, color=VAR)\
            .next_to(b0, UP, buff=0.15)
        b1 = Brace(nxt[2], DOWN, color=BACK)
        l1 = Text("shared backbone", font_size=20, color=BACK)\
            .next_to(b1, DOWN, buff=0.15)
        b2 = Brace(nxt[4], DOWN, color=DIM)
        l2 = Text("cohort wobble", font_size=20, color=DIM)\
            .next_to(b2, DOWN, buff=0.15)
        self.play_beat(Write(nxt),
                       GrowFromCenter(b0), FadeIn(l0),
                       GrowFromCenter(b1), FadeIn(l1),
                       GrowFromCenter(b2), FadeIn(l2))                     # beat 6

        moral = Text("under that model, agreement is large by construction\n— a striking convergence map becomes the DEFAULT",
                     font_size=24, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.5)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7
