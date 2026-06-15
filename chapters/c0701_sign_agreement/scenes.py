"""c0701_sign_agreement — "Sign-agreement convergence maps".

Five narrated scenes. DEFINE the convergence map (the sign-agreement operator),
decode every symbol, show a small voxel grid lighting up where signs agree, state
the convergence claim FAIRLY, and pose the question that c0702 answers with the
2^(1-K) baseline. This chapter sets the object up honestly; it does not yet rebut.

All equations/numbers are from:
  responses/lnm_critique/sections/05_the_convergence_trap.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0701_sign_agreement ./render.sh \
      chapters/c0701_sign_agreement/scenes.py -q ql \
      S1_Idea S2_Formula S3_Meaning S4_Claim S5_Question
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — What a convergence map is
# ----------------------------------------------------------------------
class S1_Idea(NarratedScene):
    scene_key = "S1_Idea"

    def construct(self):
        title = Text("What a convergence map is", font_size=40, color=WHITE)
        self.play_beat(Write(title))                                       # beat 1
        self.play(title.animate.scale(0.62).to_edge(UP, buff=0.3),
                  run_time=0.6)

        feel = Text("many maps, independently derived,\nagreeing on the same circuit",
                    font_size=27, color=DIM, line_spacing=0.8).shift(UP * 1.7)
        self.play_beat(FadeIn(feel, shift=UP * 0.2))                       # beat 2

        # voxel grid + the symbol v
        self.play(FadeOut(feel), run_time=0.4)
        grid = self._grid().shift(LEFT * 3.2 + DOWN * 0.2)
        v_cell = grid.submobjects[8]
        v_cell.set_fill(VAR, opacity=0.5)
        v_lab = MathTex("v", color=VAR).scale(1.1).next_to(v_cell, DOWN, buff=0.15)
        v_txt = Text("the brain is a grid of voxels;\nv is one voxel",
                     font_size=24, color=WHITE, line_spacing=0.8)\
            .shift(RIGHT * 2.7 + UP * 0.2)
        self.play_beat(FadeIn(grid, lag_ratio=0.04), Write(v_lab),
                       FadeIn(v_txt))                                      # beat 3

        # r_k(v)
        self.play(FadeOut(VGroup(v_txt, v_lab)),
                  grid.animate.scale(0.85).to_edge(LEFT, buff=0.8), run_time=0.5)
        rk = MathTex(r"r_k(v)", color=VAR).scale(1.5).shift(RIGHT * 1.6 + UP * 1.1)
        rk_lab = Text("value of study k's map at voxel v\n(connectivity / Fisher-z correlation)",
                      font_size=23, color=WHITE, line_spacing=0.8)\
            .next_to(rk, DOWN, buff=0.4)
        self.play_beat(Write(rk), FadeIn(rk_lab))                          # beat 4

        # K maps r_1 .. r_K
        self.play(FadeOut(VGroup(rk, rk_lab)), run_time=0.4)
        maps = MathTex(r"r_1,\ r_2,\ \dots,\ r_K").scale(1.3)\
            .shift(RIGHT * 1.6 + UP * 1.0)
        maps.set_color(VAR)
        kcap = MathTex("K", r"\ \text{studies, all over the same voxels}")\
            .scale(0.9).next_to(maps, DOWN, buff=0.4)
        kcap[0].set_color(EIG)
        self.play_beat(Write(maps), FadeIn(kcap))                          # beat 5

        # sign definition
        self.play(FadeOut(VGroup(maps, kcap)), run_time=0.4)
        sgn = MathTex(r"\operatorname{sign} r =",
                      r"+1", r",\ ", r"-1", r",\ ", r"0").scale(1.2)\
            .shift(RIGHT * 1.6 + UP * 1.1)
        sgn[1].set_color(BACK); sgn[3].set_color(BAD); sgn[5].set_color(DIM)
        sgn_lab = VGroup(
            Text("+1  if the value is positive", font_size=22, color=BACK),
            Text("-1  if the value is negative", font_size=22, color=BAD),
            Text(" 0  if it is exactly zero", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).next_to(sgn, DOWN, buff=0.4)
        self.play_beat(Write(sgn), FadeIn(sgn_lab, lag_ratio=0.2))         # beat 6

        # votes
        self.play(FadeOut(VGroup(sgn, sgn_lab)), run_time=0.4)
        votes = VGroup(
            Text("each map, at each voxel, votes:", font_size=26, color=WHITE),
            Text("up  ↑     down  ↓     silent  •", font_size=26, color=DIM),
            Text("the convergence map asks where the votes AGREE",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3).shift(RIGHT * 1.6 + UP * 0.4)
        self.play_beat(FadeIn(votes, lag_ratio=0.3))                       # beat 7

    def _grid(self, n=3):
        cells = VGroup()
        for i in range(n):
            for j in range(n):
                c = Square(side_length=0.7, stroke_color=DIM, stroke_width=2,
                           fill_color=BG, fill_opacity=1.0)
                c.move_to(RIGHT * j * 0.74 + DOWN * i * 0.74)
                cells.add(c)
        cells.move_to(ORIGIN)
        return cells


# ----------------------------------------------------------------------
# Scene 2 — The agreement statistic
# ----------------------------------------------------------------------
class S2_Formula(NarratedScene):
    scene_key = "S2_Formula"

    def construct(self):
        self.header("The agreement statistic")

        # the full operator, eq (R6) from the source
        eq = MathTex(
            r"A(v)",                                                # 0
            r"=",                                                   # 1
            r"\Big(\bigwedge_{k=1}^{K}",                            # 2
            r"\mathbb{1}\big[",                                     # 3
            r"\operatorname{sign} r_k(v) = \operatorname{sign} r_1(v)",  # 4
            r"\big]\Big)",                                          # 5
            r"\cdot",                                               # 6
            r"\operatorname{sign} r_1(v)",                          # 7
        ).scale(0.92).shift(UP * 1.7)
        eq[0].set_color(RES); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        eq[7].set_color(BACK)
        self.play_beat(Write(eq))                                          # beat 1

        # reference sign
        br_ref = Brace(eq[7], DOWN, color=BACK)
        ref_lab = Text("reference sign: map one's sign here,\nthe shared sign we record",
                       font_size=23, color=BACK, line_spacing=0.8)\
            .next_to(br_ref, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(br_ref), FadeIn(ref_lab))            # beat 2

        # the test inside
        self.play(FadeOut(VGroup(br_ref, ref_lab)), run_time=0.4)
        br_test = Brace(eq[4], DOWN, color=VAR)
        test_lab = Text("the test: does study k's sign\nequal the reference sign?",
                        font_size=23, color=VAR, line_spacing=0.8)\
            .next_to(br_test, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(br_test), FadeIn(test_lab))          # beat 3

        # the indicator
        self.play(FadeOut(VGroup(br_test, test_lab)), run_time=0.4)
        ind = MathTex(r"\mathbb{1}[\cdot] = 1", r"\ \text{if match},\ ",
                      r"0", r"\ \text{if not}").scale(1.0)
        ind[0].set_color(VAR); ind[2].set_color(DIM)
        ind.next_to(eq, DOWN, buff=0.9)
        ind_top = Text("the indicator", font_size=24, color=VAR)\
            .next_to(ind, UP, buff=0.3)
        self.play_beat(FadeIn(ind_top), Write(ind))                        # beat 4

        # the big AND
        self.play(FadeOut(VGroup(ind, ind_top)), run_time=0.4)
        br_and = Brace(eq[2], UP, color=WHITE)
        and_lab = MathTex(r"\bigwedge_{k=1}^{K}",
                          r":\ \text{logical AND over all } K \text{ studies}")\
            .scale(0.75).next_to(br_and, UP, buff=0.2)
        and_lab[0].set_color(WHITE)
        and_note = Text("= 1 only if EVERY map matches the reference",
                        font_size=23, color=RES).next_to(eq, DOWN, buff=0.8)
        self.play_beat(GrowFromCenter(br_and), FadeIn(and_lab),
                       FadeIn(and_note))                                   # beat 5

        # the product
        self.play(FadeOut(VGroup(br_and, and_lab, and_note)), run_time=0.4)
        prod = VGroup(
            Text("multiply the AND by the reference sign", font_size=25, color=WHITE),
            Text("A(v) inherits the shared + or - ,", font_size=25, color=BACK),
            Text("but ONLY when everyone agrees", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.22).next_to(eq, DOWN, buff=0.8)
        self.play_beat(FadeIn(prod, lag_ratio=0.3))                        # beat 6

        # the codomain
        self.play(FadeOut(prod), run_time=0.4)
        cod = MathTex(r"A(v) \in \{", r"-1", r",\ ", r"0", r",\ ", r"+1", r"\}")\
            .scale(1.3).next_to(eq, DOWN, buff=0.9)
        cod[1].set_color(BAD); cod[3].set_color(DIM); cod[5].set_color(BACK)
        cod_cap = Text("agreement, and its direction, in one number per voxel",
                       font_size=23, color=DIM).next_to(cod, DOWN, buff=0.3)
        self.play_beat(Write(cod), FadeIn(cod_cap))                        # beat 7


# ----------------------------------------------------------------------
# Scene 3 — Reading the map
# ----------------------------------------------------------------------
class S3_Meaning(NarratedScene):
    scene_key = "S3_Meaning"

    def construct(self):
        self.header("Reading the map")

        rule = MathTex(r"A(v) =", r"\pm 1", r"\ \text{iff all } K \text{ agree};\quad",
                       r"0", r"\ \text{otherwise}").scale(1.0).shift(UP * 2.5)
        rule[1].set_color(BACK); rule[3].set_color(DIM)
        self.play_beat(Write(rule))                                        # beat 1

        # build the grid: 6 cells, each a stack of 3 arrows (K=3)
        # signs per voxel for the worked-example flavour: agree, agree, mixed,
        # agree, agree, mixed  (like mu = (+,+,~0,-,-,~0))
        patterns = [
            ("up", "up", "up"),       # all +
            ("up", "up", "up"),       # all +
            ("up", "down", "up"),     # mixed
            ("down", "down", "down"), # all -
            ("down", "down", "down"), # all -
            ("down", "up", "down"),   # mixed
        ]
        cells = VGroup()
        for p in patterns:
            cells.add(self._cell(p))
        cells.arrange(RIGHT, buff=0.45).shift(DOWN * 0.3)

        self.play_beat(FadeIn(cells, lag_ratio=0.1))                       # beat 2

        # light the all-up cells to +1 (green)
        ups = VGroup(cells.submobjects[0], cells.submobjects[1])
        self.play_beat(*[c.submobjects[0].animate.set_fill(BACK, opacity=0.55)
                         for c in ups],
                       *[FadeIn(self._plus(c)) for c in ups])              # beat 3

        # collapse the mixed cells to 0 (dark X)
        mixed = VGroup(cells.submobjects[2], cells.submobjects[5])
        self.play_beat(*[c.submobjects[0].animate.set_fill(BG, opacity=1.0)
                         for c in mixed],
                       *[FadeIn(self._zero(c)) for c in mixed])            # beat 4

        # also light all-down to -1 so support is visible; then label support
        downs = VGroup(cells.submobjects[3], cells.submobjects[4])
        for c in downs:
            c.submobjects[0].set_fill(BAD, opacity=0.5)
            self.add(self._minus(c))
        supp = MathTex(r"\text{support} = \{v : A(v) \neq 0\}")\
            .scale(0.95).set_color(RES).next_to(cells, DOWN, buff=0.7)
        self.play_beat(Write(supp))                                        # beat 5

        consensus = Text("meant to look like cross-study consensus,\ndrawn for the eye",
                         font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(supp, DOWN, buff=0.4)
        self.play_beat(FadeIn(consensus, shift=UP * 0.2))                  # beat 6

        # the half-space identity
        self.play(FadeOut(VGroup(cells, supp, consensus)), run_time=0.5)
        half = MathTex(
            r"\{v : A(v) \neq 0\}", r"=",
            r"\Big(\bigcap_{k} \{r_k(v) > 0\}\Big)",
            r"\cup",
            r"\Big(\bigcap_{k} \{r_k(v) < 0\}\Big)",
        ).scale(0.82).shift(UP * 0.2)
        half[0].set_color(RES); half[2].set_color(BACK); half[4].set_color(BAD)
        half_cap = VGroup(
            Text("⋂ = all maps positive   ⋃ = joined with   all maps negative",
                 font_size=22, color=DIM),
            Text("agreement is an intersection of half-spaces",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.18).next_to(half, DOWN, buff=0.4)
        self.play_beat(Write(half), FadeIn(half_cap))                      # beat 7

    def _cell(self, pattern):
        box = Square(side_length=1.0, stroke_color=DIM, stroke_width=2,
                     fill_color=BG, fill_opacity=1.0)
        arrows = VGroup()
        for s in pattern:
            if s == "up":
                a = Arrow(DOWN * 0.12, UP * 0.12, color=BACK, buff=0,
                          stroke_width=4, max_tip_length_to_length_ratio=0.5)
            else:
                a = Arrow(UP * 0.12, DOWN * 0.12, color=BAD, buff=0,
                          stroke_width=4, max_tip_length_to_length_ratio=0.5)
            arrows.add(a)
        arrows.arrange(RIGHT, buff=0.1).scale(0.9).move_to(box)
        return VGroup(box, arrows)

    def _plus(self, cell):
        return MathTex("+1", color=BACK).scale(0.7).next_to(cell, DOWN, buff=0.12)

    def _minus(self, cell):
        return MathTex("-1", color=BAD).scale(0.7).next_to(cell, DOWN, buff=0.12)

    def _zero(self, cell):
        return MathTex("0", color=DIM).scale(0.7).next_to(cell, DOWN, buff=0.12)


# ----------------------------------------------------------------------
# Scene 4 — The convergence claim
# ----------------------------------------------------------------------
class S4_Claim(NarratedScene):
    scene_key = "S4_Claim"

    def construct(self):
        self.header("The convergence claim")

        intro = Text("the claim papers attach to this picture —\nstated as strongly as it deserves",
                     font_size=27, color=DIM, line_spacing=0.8).shift(UP * 2.3)
        self.play_beat(FadeIn(intro))                                      # beat 1

        story = VGroup(
            Text("many maps, from different cohorts,", font_size=27, color=WHITE),
            Text("all agree on the same voxels —", font_size=27, color=WHITE),
            Text("surely the disease network shining through",
                 font_size=27, color=RES),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.6)
        self.play_beat(FadeIn(story, lag_ratio=0.3))                       # beat 2

        self.play(FadeOut(VGroup(intro, story)), run_time=0.5)
        reading = VGroup(
            Text("THE READING:", font_size=26, color=RES),
            Text("widespread agreement = independent convergence",
                 font_size=26, color=WHITE),
            Text("onto a real, disease-specific network",
                 font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.3)
        self.play_beat(FadeIn(reading, shift=UP * 0.2))                    # beat 3

        honest = Text("and there is an honest case for it:\nif several disorders implicate one hub,\nthat recurrence is real and may matter clinically",
                      font_size=25, color=BACK, line_spacing=0.8)\
            .next_to(reading, DOWN, buff=0.5)
        self.play_beat(FadeIn(honest))                                     # beat 4

        desc = Text("a convergence map is a perfectly good DESCRIPTION\nof which connectome features keep recurring",
                    font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(honest, DOWN, buff=0.4)
        self.play_beat(FadeIn(desc, shift=UP * 0.2))                       # beat 5

        self.play(FadeOut(VGroup(reading, honest, desc)), run_time=0.5)
        grant = VGroup(
            Text("We grant the interpretation full standing.", font_size=29, color=WHITE),
            Text("A big agreement set IS consistent", font_size=27, color=BACK),
            Text("with a shared disease-specific circuit.", font_size=27, color=BACK),
            Text("Hold that thought.", font_size=27, color=DIM),
        ).arrange(DOWN, buff=0.28)
        self.play_beat(FadeIn(grant, lag_ratio=0.25))                      # beat 6


# ----------------------------------------------------------------------
# Scene 5 — The question to ask
# ----------------------------------------------------------------------
class S5_Question(NarratedScene):
    scene_key = "S5_Question"

    def construct(self):
        self.header("The question to ask")

        q = Text("Is the agreement actually surprising?",
                 font_size=34, color=RES).shift(UP * 2.4)
        self.play_beat(Write(q))                                           # beat 1

        base = VGroup(
            Text("surprise is not absolute —", font_size=27, color=WHITE),
            Text("it is measured against a BASELINE:", font_size=27, color=RES),
            Text("how often would K maps agree by chance,", font_size=26, color=DIM),
            Text("with no shared circuit at all?", font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.4)
        self.play_beat(FadeIn(base, lag_ratio=0.25))                       # beat 2

        self.play(FadeOut(base), run_time=0.4)
        striking = Text("\"striking\" against WHAT?\na third of the brain agreeing across six cohorts\nis impressive only relative to a yardstick",
                        font_size=26, color=WHITE, line_spacing=0.8).shift(UP * 0.7)
        self.play_beat(FadeIn(striking, shift=UP * 0.2))                   # beat 3

        # set up the coin model
        self.play(FadeOut(striking), run_time=0.4)
        coin = MathTex(r"\operatorname{sign} r_k(v)",
                       r"\ \text{independent},\ ",
                       r"\Pr[+] = \Pr[-] = \tfrac{1}{2}").scale(0.95)\
            .shift(UP * 0.9)
        coin[0].set_color(VAR); coin[2].set_color(EIG)
        coin_cap = Text("suppose the K signs were independent fair coins",
                        font_size=24, color=DIM).next_to(coin, DOWN, buff=0.3)
        self.play_beat(Write(coin), FadeIn(coin_cap))                      # beat 4

        # the 2^(1-K) baseline
        self.play(FadeOut(VGroup(coin, coin_cap)), run_time=0.4)
        formula = MathTex(r"\Pr[\text{all } K \text{ agree}]", "=",
                          r"2^{\,1-K}").scale(1.4).shift(UP * 0.7)
        formula[0].set_color(WHITE); formula[2].set_color(RES)
        box = SurroundingRectangle(formula[2], color=RES, buff=0.15)
        f_cap = Text("the independent-signs baseline — built next, in the sequel",
                     font_size=23, color=DIM).next_to(formula, DOWN, buff=0.4)
        self.play_beat(Write(formula), Create(box), FadeIn(f_cap))         # beat 5

        self.play(FadeOut(VGroup(formula, box, f_cap)), run_time=0.4)
        test = VGroup(
            Text("if the agreement merely MATCHES that baseline,",
                 font_size=26, color=WHITE),
            Text("it is not evidence.", font_size=26, color=BAD),
            Text("only agreement that BEATS the right baseline can be.",
                 font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.5)
        self.play_beat(FadeIn(test, lag_ratio=0.25))                       # beat 6

        moral = Text("agreement is cheap until you show it is more\nthan the baseline gives you for free",
                     font_size=27, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.9)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7
