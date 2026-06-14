"""c0505_freedman_lane — "Freedman-Lane and the size nuisance".

Five narrated scenes. Lesion volume is a label-correlated nuisance: it tracks
both the map magnitude (the backbone loading beta_i correlates with volume) and
often the symptom. A naive raw-label shuffle can leak that size effect as false
signal. Freedman-Lane fixes it: regress the outcome y on the nuisance s, take
the covariate-adjusted residuals e, and permute THOSE, not the raw labels.
Permuting residuals holds the size effect fixed while testing only the
symptom-map link; the backbone cancellation from Part 5 still holds in residual
space. We keep the source's honesty flag verbatim: whether the published
responses used Freedman-Lane or a raw shuffle is [verify against primary
source]; the size-protection recommendation is ours.

All equations/numbers/claims are page-cited in:
  responses/lnm_critique/sections/03_the_right_null.md  (esp. p.69, 86, 96, 112, 157)
  responses/lnm_critique/papers/REBUTTAL_sound.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0505_freedman_lane ./render.sh \
      chapters/c0505_freedman_lane/scenes.py -q ql \
      S1_Nuisance S2_Residualize S3_WhyResidual S4_OpenQuestion S5_Takeaway
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Lesion volume is a confound  (7 beats)
# ----------------------------------------------------------------------
class S1_Nuisance(NarratedScene):
    scene_key = "S1_Nuisance"

    def construct(self):
        title = Text("Lesion volume is a confound", font_size=42, color=WHITE)
        sub = Text("a label-correlated nuisance we must protect",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # volume correlates with map magnitude (via the backbone loading)
        link1 = MathTex(r"\text{volume}", r"\ \uparrow\ ", r"\Longrightarrow",
                        r"\ \beta_i\, ", r"\uparrow",
                        r"\quad(\beta_i = \lambda_1\, u_1^\top \ell_i)").scale(0.95)
        link1[0].set_color(EIG); link1[3].set_color(BACK)
        link1.shift(UP * 1.4)
        cap1 = VGroup(
            Text("βᵢ = backbone loading    λ₁ = top connectome eigenvalue",
                 font_size=21, color=DIM),
            Text("u₁ = backbone direction    ℓᵢ = patient i's 0/1 lesion mask",
                 font_size=21, color=DIM),
            Text("a larger lesion projects more strongly onto the backbone u₁",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.16).next_to(link1, DOWN, buff=0.3)
        self.play_beat(Write(link1), FadeIn(cap1))                         # beat 2

        # volume correlates with the symptom too
        link2 = VGroup(
            Text("volume  ↑   ⟹   symptom severity  ↑",
                 font_size=27, color=WHITE),
            Text("bigger lesions tend to cause more, or more severe, deficits",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(cap1, DOWN, buff=0.55)
        self.play_beat(FadeIn(link2[0]), FadeIn(link2[1], shift=UP * 0.2))  # beat 3

        # so it is tied to BOTH sides: the diagram
        self.play(FadeOut(VGroup(link1, cap1, link2)), run_time=0.5)
        node_s = self._chip("lesion volume", EIG).shift(UP * 1.3)
        node_x = self._chip("the map  x", VAR).shift(DOWN * 0.6 + LEFT * 3.2)
        node_y = self._chip("the symptom  y", RES).shift(DOWN * 0.6 + RIGHT * 3.2)
        a1 = Arrow(node_s.get_bottom(), node_x.get_top(), color=DIM, buff=0.12)
        a2 = Arrow(node_s.get_bottom(), node_y.get_top(), color=DIM, buff=0.12)
        confound = Text("volume is tied to BOTH sides at once — a confound",
                        font_size=24, color=BAD).to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(node_s), FadeIn(node_x), FadeIn(node_y),
                       GrowArrow(a1), GrowArrow(a2), FadeIn(confound))      # beat 4

        # name it: s_i
        self.play(FadeOut(VGroup(node_s, node_x, node_y, a1, a2, confound)),
                  run_time=0.5)
        define = MathTex("s_i", r"\;=\;", r"\text{lesion volume of patient } i")\
            .scale(1.2).shift(UP * 0.9)
        define[0].set_color(EIG)
        br = Brace(define[0], DOWN, color=EIG)
        brlab = Text("one number per patient — the nuisance covariate",
                     font_size=23, color=EIG).next_to(br, DOWN, buff=0.2)
        self.play_beat(Write(define), GrowFromCenter(br), FadeIn(brlab))   # beat 5

        # the danger: naive shuffle leaks it
        self.play(FadeOut(VGroup(define, br, brlab)), run_time=0.5)
        danger = VGroup(
            Text("the danger:", font_size=27, color=BAD),
            Text("a naive shuffle of the RAW symptom labels", font_size=25, color=WHITE),
            Text("can leak the size effect, dressed up as false signal", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.9)
        self.play_beat(FadeIn(danger, lag_ratio=0.3))                      # beat 6

        leak = Text("reject not because the symptom tracks the WIRING,\nbut merely because it tracks lesion SIZE",
                    font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(danger, DOWN, buff=0.55)
        self.play_beat(FadeIn(leak, shift=UP * 0.2))                       # beat 7

    def _chip(self, label, color):
        box = RoundedRectangle(width=2.9, height=0.75, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=22, color=color).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 2 — Freedman-Lane: permute residuals  (6 beats)
# ----------------------------------------------------------------------
class S2_Residualize(NarratedScene):
    scene_key = "S2_Residualize"

    def construct(self):
        self.header("Freedman–Lane: permute residuals")

        intro = Text("permute the part of the data the nuisance does NOT explain",
                     font_size=27, color=WHITE).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # step 1: regress y on s
        step1 = MathTex("y_i", r"\;=\;", "b\\,", "s_i", r"\;+\;", "e_i")\
            .scale(1.3).shift(UP * 1.1)
        step1[0].set_color(RES); step1[2].set_color(WHITE)
        step1[3].set_color(EIG); step1[5].set_color(VAR)
        s1tag = Text("1.  regress the outcome y on the nuisance s",
                     font_size=24, color=DIM).next_to(step1, UP, buff=0.35)
        self.play_beat(Write(step1), FadeIn(s1tag),
                       intro.animate.set_opacity(0.35))                    # beat 2

        # step 2: the residual e_i, with every symbol braced
        br_y = Brace(step1[0], DOWN, color=RES)
        ly = Text("outcome", font_size=20, color=RES).next_to(br_y, DOWN, buff=0.12)
        br_bs = Brace(step1[2:4], DOWN, color=EIG)
        lbs = Text("size-predicted part  (slope b × volume sᵢ)",
                   font_size=20, color=EIG).next_to(br_bs, DOWN, buff=0.12)
        br_e = Brace(step1[5], UP, color=VAR)
        le = Text("residual eᵢ = what y has left after size is removed",
                  font_size=20, color=VAR).next_to(br_e, UP, buff=0.12)
        self.play_beat(GrowFromCenter(br_y), FadeIn(ly),
                       GrowFromCenter(br_bs), FadeIn(lbs),
                       GrowFromCenter(br_e), FadeIn(le))                   # beat 3

        # step 3: permute the residuals, not raw y
        self.play(FadeOut(VGroup(br_y, ly, br_bs, lbs, br_e, le, s1tag, intro)),
                  run_time=0.45)
        self.play(step1.animate.scale(0.8).to_edge(UP, buff=1.05), run_time=0.5)
        step3 = MathTex(r"\{e_i\}", r"\ \xrightarrow{\ \pi\ }\ ", r"\{e_{\pi(i)}\}")\
            .scale(1.25).shift(UP * 0.6)
        step3[0].set_color(VAR); step3[2].set_color(VAR)
        s3tag = Text("3.  permute the RESIDUALS across patients — not the raw outcome",
                     font_size=24, color=DIM).next_to(step3, DOWN, buff=0.35)
        self.play_beat(Write(step3), FadeIn(s3tag))                        # beat 4

        # contrast naive vs Freedman-Lane
        self.play(FadeOut(VGroup(step1, step3, s3tag)), run_time=0.5)
        col_naive = VGroup(
            Text("NAIVE shuffle", font_size=25, color=BAD),
            MathTex(r"\{y_i\}\ \to\ \{y_{\pi(i)}\}").scale(0.95),
            Text("carries the size effect along", font_size=21, color=DIM),
        ).arrange(DOWN, buff=0.25)
        col_naive[1].set_color(RES)
        col_fl = VGroup(
            Text("FREEDMAN–LANE", font_size=25, color=BACK),
            MathTex(r"\{e_i\}\ \to\ \{e_{\pi(i)}\}").scale(0.95),
            Text("size already removed first", font_size=21, color=DIM),
        ).arrange(DOWN, buff=0.25)
        col_fl[1].set_color(VAR)
        cols = VGroup(col_naive, col_fl).arrange(RIGHT, buff=1.4).shift(UP * 0.3)
        divider = Line(UP * 1.6, DOWN * 1.4, color=DIM, stroke_width=1)\
            .move_to(cols)
        self.play_beat(FadeIn(col_naive, lag_ratio=0.2),
                       Create(divider),
                       FadeIn(col_fl, lag_ratio=0.2))                      # beat 5

        # the three-move recipe
        self.play(FadeOut(VGroup(cols, divider)), run_time=0.5)
        recipe = VGroup(
            Text("1.  fit  y  on  s", font_size=27, color=WHITE),
            Text("2.  take the residuals  e", font_size=27, color=VAR),
            Text("3.  shuffle the residuals → build the null", font_size=27, color=BACK),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        self.play_beat(FadeIn(recipe, lag_ratio=0.3))                      # beat 6


# ----------------------------------------------------------------------
# Scene 3 — Why residual space  (7 beats)
# ----------------------------------------------------------------------
class S3_WhyResidual(NarratedScene):
    scene_key = "S3_WhyResidual"

    def construct(self):
        self.header("Why residual space")

        intro = Text("residualizing holds the SIZE effect fixed,\nso we test only the symptom-to-map link",
                     font_size=27, color=WHITE, line_spacing=0.8).shift(UP * 2.2)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # the residual, fully typed
        eq = MathTex("e_i", "=", "y_i", "-", "b\\,", "s_i")\
            .scale(1.3).shift(UP * 0.6)
        eq[0].set_color(VAR); eq[2].set_color(RES)
        eq[4].set_color(WHITE); eq[5].set_color(EIG)
        leg = VGroup(
            Text("eᵢ = residual    yᵢ = outcome", font_size=21, color=DIM),
            Text("b·sᵢ = the fitted line: slope b times volume sᵢ",
                 font_size=21, color=DIM),
        ).arrange(DOWN, buff=0.15).next_to(eq, DOWN, buff=0.45)
        self.play_beat(Write(eq), FadeIn(leg),
                       intro.animate.set_opacity(0.3))                     # beat 2

        # the nuisance piece is the same in every permutation
        self.play(FadeOut(VGroup(leg, intro)), run_time=0.4)
        br_ns = Brace(eq[4:6], DOWN, color=EIG)
        nlab = Text("b·sᵢ is NEVER reshuffled → the size effect is held fixed",
                    font_size=24, color=EIG).next_to(br_ns, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(br_ns), FadeIn(nlab))                # beat 3

        # what's left, e_i, is uncorrelated with s_i
        self.play(FadeOut(VGroup(br_ns, nlab)), run_time=0.4)
        orth = MathTex(r"\mathrm{corr}", r"\big(", "e_i", ",", "s_i", r"\big)",
                       "=", "0").scale(1.2).next_to(eq, DOWN, buff=0.7)
        orth[2].set_color(VAR); orth[4].set_color(EIG); orth[7].set_color(BACK)
        ocap = Text("by construction: size has been projected OUT of the residual",
                    font_size=23, color=DIM).next_to(orth, DOWN, buff=0.3)
        self.play_beat(Write(orth), FadeIn(ocap))                          # beat 4

        # recall the backbone split
        self.play(FadeOut(VGroup(eq, orth, ocap)), run_time=0.5)
        decomp = MathTex("x_i", "=", r"\underbrace{\beta_i\, u_1}_{\text{backbone, label-free}}",
                         "+", "r_i").scale(1.15).shift(UP * 1.1)
        decomp[0].set_color(VAR); decomp[2].set_color(BACK); decomp[4].set_color(RES)
        dleg = VGroup(
            Text("xᵢ = patient i's fixed map    βᵢ = backbone loading",
                 font_size=21, color=DIM),
            Text("u₁ = backbone direction    rᵢ = residual (label-sensitive part)",
                 font_size=21, color=DIM),
        ).arrange(DOWN, buff=0.15).next_to(decomp, DOWN, buff=0.4)
        self.play_beat(Write(decomp), FadeIn(dleg))                        # beat 5

        # beta_i correlates with volume -> size-correlated backbone removed
        self.play(FadeOut(dleg), run_time=0.4)
        rmv = MathTex(r"\beta_i", r"\ \text{correlates with}\ ", "s_i",
                      r"\ \Rightarrow\ ", r"\text{regress on } s",
                      r"\ \text{removes it}").scale(0.9)
        rmv[0].set_color(BACK); rmv[2].set_color(EIG); rmv[4].set_color(WHITE)
        rmv.next_to(decomp, DOWN, buff=0.55)
        self.play_beat(Write(rmv))                                         # beat 6

        # what's left is size-orthogonal AND label-independent -> cancellation holds
        moral = VGroup(
            Text("the leftover backbone is orthogonal to size", font_size=24, color=WHITE),
            Text("and still LABEL-INDEPENDENT", font_size=25, color=BACK),
            Text("→ the Part-5 cancellation holds in residual space too", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.22).next_to(rmv, DOWN, buff=0.5)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 7


# ----------------------------------------------------------------------
# Scene 4 — An honest caveat  (7 beats)
# ----------------------------------------------------------------------
class S4_OpenQuestion(NarratedScene):
    scene_key = "S4_OpenQuestion"

    def construct(self):
        self.header("An honest caveat")

        intro = Text("we must not overclaim what the published responses actually did",
                     font_size=27, color=WHITE).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # what the rebuttal describes
        desc = Text("\"...randomly shuffling each patient's clinical symptom\nwith a different patient's network map\"",
                    font_size=25, color=WHITE, line_spacing=0.8).shift(UP * 1.1)
        dcap = Text("— Siddiqi et al., p.4  (a symptom-label permutation)",
                    font_size=22, color=DIM).next_to(desc, DOWN, buff=0.25)
        self.play_beat(FadeIn(desc), FadeIn(dcap))                         # beat 2

        # is it FL or a raw shuffle? not settled
        self.play(FadeOut(VGroup(intro, desc, dcap)), run_time=0.5)
        q = VGroup(
            Text("Freedman–Lane?", font_size=27, color=BACK),
            Text("(permute size-adjusted residuals e)", font_size=22, color=DIM),
            MathTex(r"\ \text{vs.}\ ").scale(1.1),
            Text("raw-label shuffle?", font_size=27, color=BAD),
            Text("(permute the labels y directly)", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.18).shift(UP * 0.8)
        q[2].set_color(WHITE)
        notsettled = Text("not settled from the abstracts alone",
                          font_size=25, color=RES).next_to(q, DOWN, buff=0.45)
        self.play_beat(FadeIn(q, lag_ratio=0.2), FadeIn(notsettled))       # beat 3

        # reads closer to raw; verify against primary source
        self.play(FadeOut(VGroup(q, notsettled)), run_time=0.5)
        reads = VGroup(
            Text("the rebuttal's wording reads closer to a RAW-data shuffle",
                 font_size=25, color=WHITE),
            Text("[verify against primary source]", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.35).shift(UP * 0.9)
        box = SurroundingRectangle(reads[1], color=RES, buff=0.18)
        self.play_beat(FadeIn(reads[0]), FadeIn(reads[1]), Create(box))    # beat 4

        # the math holds either way
        self.play(FadeOut(VGroup(reads, box)), run_time=0.5)
        holds = VGroup(
            Text("the math holds EITHER way, given exchangeability:",
                 font_size=25, color=WHITE),
            Text("•  exact validity", font_size=24, color=BACK),
            Text("•  backbone cancellation", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT).shift(UP * 0.7)
        self.play_beat(FadeIn(holds, lag_ratio=0.3))                       # beat 5

        # we recommend FL; that's ours
        ours = VGroup(
            Text("we RECOMMEND Freedman–Lane:", font_size=25, color=WHITE),
            Text("size is a label-correlated nuisance a raw shuffle does not protect",
                 font_size=23, color=DIM),
            Text("that recommendation is OURS", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.22).next_to(holds, DOWN, buff=0.5)
        self.play_beat(FadeIn(ours, lag_ratio=0.3))                        # beat 6

        # keep the caveat in view
        self.play(FadeOut(VGroup(holds, ours)), run_time=0.5)
        keep = VGroup(
            Text("Take the size-protected recipe as our ADVICE —", font_size=27, color=WHITE),
            Text("not as a claim about what the preprints already did.", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.2)
        self.play_beat(FadeIn(keep[0]), FadeIn(keep[1], shift=UP * 0.2))    # beat 7


# ----------------------------------------------------------------------
# Scene 5 — Takeaway  (6 beats)
# ----------------------------------------------------------------------
class S5_Takeaway(NarratedScene):
    scene_key = "S5_Takeaway"

    def construct(self):
        self.header("Takeaway")

        head = Text("size-protected permutation gives a VALID test\neven when volume confounds",
                    font_size=28, color=WHITE, line_spacing=0.8).shift(UP * 1.9)
        self.play_beat(FadeIn(head))                                       # beat 1

        # build the four-line recipe one beat at a time
        r1 = VGroup(
            Text("1.  RESIDUALIZE the nuisance", font_size=26, color=WHITE),
            Text("regress the outcome on lesion volume; keep what is left",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 0.3)
        self.play_beat(FadeIn(r1, shift=UP * 0.2),
                       head.animate.scale(0.85).to_edge(UP, buff=1.0))     # beat 2

        r2 = VGroup(
            Text("2.  PERMUTE the residuals", font_size=26, color=VAR),
            Text("not the raw labels — the size effect stays fixed across shuffles",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(r1, DOWN, buff=0.4)
        self.play_beat(FadeIn(r2, shift=UP * 0.2))                         # beat 3

        r3 = VGroup(
            Text("3.  the BACKBONE cancels", font_size=26, color=BACK),
            Text("label-free and size-correlated → drops out in residual space",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(r2, DOWN, buff=0.4)
        self.play_beat(FadeIn(r3, shift=UP * 0.2))                         # beat 4

        r4 = VGroup(
            Text("4.  the SIGNAL survives", font_size=26, color=RES),
            Text("only genuine, size-independent, label-dependent structure can reject",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(r3, DOWN, buff=0.4)
        self.play_beat(FadeIn(r4, shift=UP * 0.2))                         # beat 5

        # the one-line summary
        self.play(FadeOut(VGroup(head, r1, r2, r3, r4)), run_time=0.5)
        moral = VGroup(
            Text("Residualize the nuisance.", font_size=30, color=WHITE),
            Text("Permute the residuals.", font_size=30, color=VAR),
            Text("The backbone cancels.", font_size=30, color=BACK),
            Text("The signal survives.", font_size=30, color=RES),
        ).arrange(DOWN, buff=0.3)
        tag = Text("a test that is honest about size",
                   font_size=24, color=DIM).next_to(moral, DOWN, buff=0.5)
        self.play_beat(FadeIn(moral, lag_ratio=0.35), FadeIn(tag))         # beat 6
