"""c0601_backbone_subspace — "The backbone subspace and projector".

Five narrated scenes. The pure linear-algebra setup for residualization (c0602):
recall the spectral decomposition of C, define the backbone subspace B as the
span of the top r eigenvectors, build the orthogonal projector Pi_B, form its
complement Pi_B^perp = I - Pi_B, and motivate the whole construction (camera vs
court: strip the shared backbone, keep the discriminative remainder).

All equations come from:
  responses/lnm_critique/sections/04_removing_the_backbone.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0601_backbone_subspace ./render.sh \
      chapters/c0601_backbone_subspace/scenes.py -q ql \
      S1_Recall S2_Subspace S3_Projector S4_Complement S5_Why
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG

from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — recall the spectrum of C
# ----------------------------------------------------------------------
class S1_Recall(NarratedScene):
    scene_key = "S1_Recall"

    def construct(self):
        self.header("Recall the spectrum")

        intro = Text("name the backbone before we remove it",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                       # beat 1

        sym = Text("C is symmetric over V voxels  →  a clean spectral sum",
                   font_size=26, color=WHITE).shift(UP * 1.5)
        self.play_beat(FadeIn(sym), intro.animate.set_opacity(0.4))         # beat 2

        # the spectral decomposition
        eq = MathTex("C", "=", r"\sum_{j=1}^{V}",
                     r"\lambda_j", r"\,u_j", r"u_j^{\top}").scale(1.4)
        eq[0].set_color(WHITE); eq[3].set_color(EIG)
        eq[4].set_color(BACK); eq[5].set_color(BACK)
        self.play_beat(Write(eq),
                       sym.animate.scale(0.85).to_edge(UP, buff=1.0))       # beat 3

        # annotate lambda_j
        brace_l = Brace(eq[3], DOWN, color=EIG)
        l_lab = VGroup(
            Text("eigenvalue: a single number,", font_size=22, color=EIG),
            MathTex(r"\lambda_1 \ge \lambda_2 \ge \cdots",
                    color=EIG).scale(0.9),
        ).arrange(DOWN, buff=0.15).next_to(brace_l, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_l), FadeIn(l_lab))              # beat 4

        # annotate u_j
        self.play(FadeOut(VGroup(brace_l, l_lab)), run_time=0.4)
        brace_u = Brace(eq[4], DOWN, color=BACK)
        u_lab = VGroup(
            Text("eigenvector: a unit direction;", font_size=22, color=BACK),
            Text("orthonormal — unit length, mutually perpendicular",
                 font_size=22, color=BACK),
        ).arrange(DOWN, buff=0.15).next_to(brace_u, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_u), FadeIn(u_lab))              # beat 5

        # annotate the outer product
        self.play(FadeOut(VGroup(brace_u, u_lab)), run_time=0.4)
        brace_o = Brace(eq[5], DOWN, color=BACK)
        o_lab = VGroup(
            Text("outer product: column × row → a V×V matrix",
                 font_size=22, color=WHITE),
            Text("it projects onto the single direction u_j",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15).next_to(brace_o, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_o), FadeIn(o_lab))              # beat 6

        # the reading: weighted stack of 1-D projectors
        self.play(FadeOut(VGroup(brace_o, o_lab, sym)), run_time=0.4)
        reading = Text("C is a weighted stack of one-dimensional projectors,\n"
                       "each scaled by its eigenvalue λ_j",
                       font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(reading, shift=UP * 0.2))                     # beat 7

        # the leading modes carry the backbone
        bb = VGroup(
            Text("the leading few modes carry the BACKBONE", font_size=26, color=BACK),
            MathTex(r"u_1 = \text{ dominant degree mode}",
                    color=BACK).scale(0.95),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.7)
        self.play(FadeOut(reading), run_time=0.3)
        self.play_beat(FadeIn(bb, lag_ratio=0.3))                          # beat 8


# ----------------------------------------------------------------------
# Scene 2 — the backbone subspace B
# ----------------------------------------------------------------------
class S2_Subspace(NarratedScene):
    scene_key = "S2_Subspace"

    def construct(self):
        self.header("The backbone subspace B")

        intro = Text("pick a rank r — the number of top modes = backbone",
                     font_size=26, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                       # beat 1

        # definition of B
        eq = MathTex(r"\mathcal{B}", "=", r"\mathrm{span}",
                     r"\{u_1, \dots, u_r\}").scale(1.4).shift(UP * 1.1)
        eq[0].set_color(BACK); eq[3].set_color(BACK)
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4))          # beat 2

        # span = all linear combinations
        span = MathTex(r"\mathcal{B} = \big\{",
                       r"c_1 u_1 + \cdots + c_r u_r",
                       r"\ :\ c_i \in \mathbb{R}\big\}").scale(1.0)
        span[1].set_color(BACK)
        span.next_to(eq, DOWN, buff=0.6)
        span_cap = Text("span = all linear combinations of the r modes",
                        font_size=23, color=DIM).next_to(span, DOWN, buff=0.25)
        self.play_beat(Write(span), FadeIn(span_cap))                      # beat 3

        # r-dimensional honest subspace
        self.play(FadeOut(VGroup(span, span_cap, intro)), run_time=0.4)
        dim = VGroup(
            Text("the u_j are orthonormal → the r directions are independent",
                 font_size=24, color=WHITE),
            Text("so B is an honest r-dimensional subspace of the V-dim voxel space",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(dim, lag_ratio=0.3))                         # beat 4

        # geometric reading
        self.play(FadeOut(dim), run_time=0.3)
        geo = Text("B is the flat that contains the backbone —\n"
                   "every pure-backbone map lives entirely inside it",
                   font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(geo, shift=UP * 0.2))                        # beat 5

        # how to choose r: the spectral elbow
        self.play(FadeOut(VGroup(eq, geo)), run_time=0.4)
        elbow = self._elbow_plot().shift(DOWN * 0.2)
        elbow_cap = Text("choose r at the spectral elbow: where λ_j drops from huge to ordinary",
                         font_size=23, color=DIM).next_to(elbow, DOWN, buff=0.35)
        self.play_beat(*[Create(m) for m in elbow.submobjects],
                       FadeIn(elbow_cap), lag_ratio=0.1)                    # beat 6

        why = Text("R1's threat lives in those few huge, flat eigenvalues —\n"
                   "the modes shared by every seed, no more",
                   font_size=24, color=BACK, line_spacing=0.8)\
            .next_to(elbow_cap, DOWN, buff=0.3)
        self.play_beat(FadeIn(why))                                        # beat 7

        # label-blind choice
        self.play(FadeOut(VGroup(elbow, elbow_cap, why)), run_time=0.4)
        blind = VGroup(
            Text("r is chosen from C alone — before any patient label is seen",
                 font_size=26, color=WHITE),
            Text("that label-blindness keeps the later inference honest",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(blind, lag_ratio=0.3))                       # beat 8

    def _elbow_plot(self):
        ax = Axes(x_range=[0, 9, 1], y_range=[0, 11, 2],
                  x_length=6.0, y_length=3.0,
                  axis_config={"color": DIM, "stroke_width": 2,
                               "include_ticks": False})
        xl = MathTex("j", color=DIM).scale(0.7).next_to(ax.x_axis, RIGHT, buff=0.15)
        yl = MathTex(r"\lambda_j", color=EIG).scale(0.7)\
            .next_to(ax.y_axis, UP, buff=0.15)
        # Schematic spectrum: a few huge eigenvalues, then a cliff to "ordinary".
        # Illustrative only — the source gives no fixed elbow count (its worked
        # toy uses r=1; empirically the elbow is "a handful" of modes), so the
        # cut is drawn generically rather than asserting a specific r.
        vals = [10.0, 9.4, 1.2, 1.0, 0.8, 0.6, 0.5, 0.4]
        elbow_at = 2  # schematic only; not a claim from the source
        dots = VGroup(*[
            Dot(ax.c2p(i + 1, v), radius=0.06,
                color=(BACK if i < elbow_at else DIM))
            for i, v in enumerate(vals)
        ])
        gap = DashedLine(ax.c2p(elbow_at + 0.5, 0), ax.c2p(elbow_at + 0.5, 11),
                         color=RES, stroke_width=2)
        gap_lab = Text("elbow → take r here", font_size=20, color=RES)\
            .next_to(ax.c2p(elbow_at + 0.5, 11), UP, buff=0.1)
        return VGroup(ax, xl, yl, dots, gap, gap_lab)


# ----------------------------------------------------------------------
# Scene 3 — the projector Pi_B
# ----------------------------------------------------------------------
class S3_Projector(NarratedScene):
    scene_key = "S3_Projector"

    def construct(self):
        self.header("The projector onto B")

        intro = Text("the operator that lands a vector on B",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # Pi_B definition
        eq = MathTex(r"\Pi_{\mathcal{B}}", "=", r"\sum_{j=1}^{r}",
                     r"u_j", r"u_j^{\top}").scale(1.4).shift(UP * 1.2)
        eq[0].set_color(RES); eq[3].set_color(BACK); eq[4].set_color(BACK)
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4))          # beat 2

        # leading r outer products, lambdas dropped
        brace = Brace(eq[2:], DOWN, color=DIM)
        b_lab = Text("the leading r outer products from the spectrum — λ's dropped",
                     font_size=22, color=DIM).next_to(brace, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace), FadeIn(b_lab))               # beat 3

        # action on v
        self.play(FadeOut(VGroup(brace, b_lab, intro)), run_time=0.4)
        act = MathTex(r"\Pi_{\mathcal{B}}", "v", r"\ =\ ",
                      r"\text{the part of }", "v", r"\text{ inside }",
                      r"\mathcal{B}").scale(1.0)
        act[0].set_color(RES); act[1].set_color(VAR); act[4].set_color(VAR)
        act[6].set_color(BACK)
        act.next_to(eq, DOWN, buff=0.7)
        act_cap = Text("keeps the in-B component of v, discards the rest",
                       font_size=23, color=DIM).next_to(act, DOWN, buff=0.25)
        self.play_beat(Write(act), FadeIn(act_cap))                        # beat 4

        # property 1: idempotent
        self.play(FadeOut(VGroup(act, act_cap)), run_time=0.4)
        idem = MathTex(r"\text{idempotent:}\quad",
                       r"\Pi_{\mathcal{B}}", r"\Pi_{\mathcal{B}}",
                       "=", r"\Pi_{\mathcal{B}}").scale(1.1)
        idem[1].set_color(RES); idem[2].set_color(RES); idem[4].set_color(RES)
        idem.next_to(eq, DOWN, buff=0.7)
        self.play_beat(Write(idem))                                        # beat 5

        idem_cap = Text("apply it twice and nothing new happens —\n"
                        "once inside B, projecting again leaves you put",
                        font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(idem, DOWN, buff=0.4)
        self.play_beat(FadeIn(idem_cap, shift=UP * 0.2))                   # beat 6

        # property 2: symmetric
        self.play(FadeOut(VGroup(idem, idem_cap)), run_time=0.4)
        sym = MathTex(r"\text{symmetric:}\quad",
                      r"\Pi_{\mathcal{B}}^{\top}", "=",
                      r"\Pi_{\mathcal{B}}").scale(1.1)
        sym[1].set_color(RES); sym[3].set_color(RES)
        sym.next_to(eq, DOWN, buff=0.7)
        sym_cap = Text("an orthogonal projector — drops v straight down onto B "
                       "at a right angle", font_size=23, color=DIM)\
            .next_to(sym, DOWN, buff=0.3)
        self.play_beat(Write(sym), FadeIn(sym_cap))                        # beat 7

        # fixedness moral
        self.play(FadeOut(VGroup(sym, sym_cap, eq)), run_time=0.4)
        fixed = VGroup(
            Text("Π_B is a fixed, label-independent linear operator,",
                 font_size=27, color=WHITE),
            Text("known the moment C is known.", font_size=27, color=WHITE),
            Text("that fixedness is the source of every good property to come.",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(fixed, lag_ratio=0.3))                       # beat 8


# ----------------------------------------------------------------------
# Scene 4 — the orthogonal complement
# ----------------------------------------------------------------------
class S4_Complement(NarratedScene):
    scene_key = "S4_Complement"

    def construct(self):
        self.header("The orthogonal complement")

        intro = Text("now the mirror image: throw the backbone away, keep the rest",
                     font_size=26, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # complementary projector
        eq = MathTex(r"\Pi_{\mathcal{B}}^{\perp}", "=", "I", "-",
                     r"\Pi_{\mathcal{B}}").scale(1.5).shift(UP * 1.2)
        eq[0].set_color(BACK); eq[2].set_color(EIG); eq[4].set_color(RES)
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4))          # beat 2

        # I = identity
        brace_I = Brace(eq[2], DOWN, color=EIG)
        I_lab = VGroup(
            Text("identity — the do-nothing operator", font_size=22, color=EIG),
            MathTex("I", r"\,v", "=", "v", color=EIG).scale(0.95),
        ).arrange(DOWN, buff=0.15).next_to(brace_I, DOWN, buff=0.2)
        I_lab[1][0].set_color(EIG); I_lab[1][1].set_color(VAR)
        I_lab[1][3].set_color(VAR)
        self.play_beat(GrowFromCenter(brace_I), FadeIn(I_lab))             # beat 3

        # I - Pi_B reading
        self.play(FadeOut(VGroup(brace_I, I_lab, intro)), run_time=0.4)
        reading = Text("take the whole vector, subtract off its backbone part —\n"
                       "what remains is everything orthogonal to the backbone",
                       font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(reading, shift=UP * 0.2))                    # beat 4

        # residual subspace
        self.play(FadeOut(reading), run_time=0.3)
        resid = MathTex(r"\Pi_{\mathcal{B}}^{\perp}",
                        r"\text{ projects onto }",
                        r"\mathrm{span}\{u_{r+1}, \dots, u_V\}").scale(0.95)
        resid[0].set_color(BACK); resid[2].set_color(VAR)
        resid.next_to(eq, DOWN, buff=0.7)
        resid_cap = Text("the residual subspace — the orthogonal complement of B",
                         font_size=23, color=DIM).next_to(resid, DOWN, buff=0.25)
        self.play_beat(Write(resid), FadeIn(resid_cap))                    # beat 5

        # the split of any vector
        self.play(FadeOut(VGroup(resid, resid_cap, eq)), run_time=0.4)
        split = MathTex(r"\Pi_{\mathcal{B}}", "v", "+",
                        r"\Pi_{\mathcal{B}}^{\perp}", "v", "=", "v")\
            .scale(1.3).shift(UP * 0.9)
        split[0].set_color(RES); split[1].set_color(VAR)
        split[3].set_color(BACK); split[4].set_color(VAR); split[6].set_color(VAR)
        split_cap = MathTex(r"\Pi_{\mathcal{B}} + (I - \Pi_{\mathcal{B}}) = I",
                            color=DIM).scale(0.9).next_to(split, DOWN, buff=0.35)
        self.play_beat(Write(split), FadeIn(split_cap))                    # beat 6

        # perpendicular pieces
        perp = Text("the two pieces meet at a right angle and share nothing",
                    font_size=25, color=WHITE).next_to(split_cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(perp))                                       # beat 7

        # clean decomposition moral
        self.play(FadeOut(VGroup(split, split_cap, perp)), run_time=0.4)
        moral = VGroup(
            Text("every map decomposes — no overlap, no leftover —", font_size=26, color=WHITE),
            Text("into a backbone half inside B", font_size=26, color=RES),
            Text("and a residual half outside it", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 8


# ----------------------------------------------------------------------
# Scene 5 — why build this machinery
# ----------------------------------------------------------------------
class S5_Why(NarratedScene):
    scene_key = "S5_Why"

    def construct(self):
        self.header("Why build this machinery")

        goal = VGroup(
            Text("Goal:", font_size=30, color=RES),
            Text("one clean operator that removes EXACTLY the backbone",
                 font_size=26, color=WHITE),
            Text("and keeps EXACTLY the rest", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.4)
        self.play_beat(FadeIn(goal, lag_ratio=0.2))                        # beat 1

        op = MathTex(r"\Pi_{\mathcal{B}}^{\perp}",
                     r"\text{ — no estimation, no tuning beyond } r")\
            .scale(0.95)
        op[0].set_color(BACK)
        op.next_to(goal, DOWN, buff=0.6)
        self.play_beat(Write(op))                                          # beat 2

        # deletes the right thing
        self.play(FadeOut(VGroup(goal, op)), run_time=0.4)
        right = Text("the group-average backbone is shared across disorders (R1) —\n"
                     "so it cannot be where a disease-specific signal lives",
                     font_size=25, color=WHITE, line_spacing=0.8).shift(UP * 1.3)
        self.play_beat(FadeIn(right, shift=UP * 0.2))                      # beat 3

        # camera vs court
        self.play(FadeOut(right), run_time=0.3)
        cam = VGroup(
            Text("Camera vs court", font_size=28, color=RES),
            Text("a photo of any room is mostly the room — shared by every photo",
                 font_size=24, color=DIM),
            Text("the face you want is the thin part that DIFFERS",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.0)
        self.play_beat(FadeIn(cam, lag_ratio=0.25))                        # beat 4

        tie = VGroup(
            Text("the backbone is the room.", font_size=26, color=DIM),
            Text("Π_B^perp strips the shared part so the discriminative part stands out",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.25).next_to(cam, DOWN, buff=0.55)
        self.play_beat(FadeIn(tie, shift=UP * 0.2))                        # beat 5

        # next chapter: residualized map
        self.play(FadeOut(VGroup(cam, tie)), run_time=0.4)
        nxt = MathTex(r"\tilde{m}_\ell", "=", r"\Pi_{\mathcal{B}}^{\perp}",
                      "C", r"\ell").scale(1.4).shift(UP * 0.6)
        nxt[0].set_color(VAR); nxt[2].set_color(BACK)
        nxt[3].set_color(WHITE); nxt[4].set_color(VAR)
        nxt_cap = Text("next chapter: the residualized map", font_size=24, color=DIM)\
            .next_to(nxt, DOWN, buff=0.4)
        self.play_beat(Write(nxt), FadeIn(nxt_cap))                        # beat 6

        last = Text("that residual is where every honest contrast will be run.\n"
                    "here we built the operator — next, we put it to work.",
                    font_size=25, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(last, shift=UP * 0.2))                       # beat 7
