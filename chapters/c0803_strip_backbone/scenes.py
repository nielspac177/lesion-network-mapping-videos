"""c0803_strip_backbone — "Move 2: strip the backbone".

Five narrated scenes on backbone residualization in the single-target case.
Even with one VIM target each map m_i is backbone-dominated; the discriminative
fingerprint lives off the backbone in C*delta_i. Residualize
m-tilde_i = (I - Pi_B) m_i, combine with the Move 1 permutation null, and keep
the honest caveat: this is a HYPOTHESIS that the signal is off-backbone.

All equations/numbers are from:
  responses/lnm_critique/sections/06_single_target.md   (Move 2, R5)
  responses/lnm_critique/sections/04_removing_the_backbone.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0803_strip_backbone ./render.sh \
      chapters/c0803_strip_backbone/scenes.py -q ql \
      S1_Why S2_Operator S3_Fingerprint S4_Combine S5_Caveat
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Why strip even here
# ----------------------------------------------------------------------
class S1_Why(NarratedScene):
    scene_key = "S1_Why"

    def construct(self):
        self.header("Why strip even here")

        intro = VGroup(
            Text("Move 1 fixed the null.", font_size=28, color=DIM),
            Text("Move 2 fixes the estimate.", font_size=28, color=WHITE),
            Text("one tiny VIM target — every lesion in the same few mm",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.6)
        self.play_beat(FadeIn(intro, lag_ratio=0.3))                       # beat 1

        # the single-target decomposition
        self.play(FadeOut(intro), run_time=0.4)
        eq = MathTex("m_i", "=", r"C\ell_0", "+", r"C\delta_i")\
            .scale(1.5).shift(UP * 0.9)
        eq[0].set_color(VAR); eq[2].set_color(BACK); eq[4].set_color(RES)
        self.play_beat(Write(eq))                                          # beat 2

        # annotate C l_0 (shared)
        brace_sh = Brace(eq[2], DOWN, color=BACK)
        sh_lab = Text("shared VIM fingerprint\nidentical for every patient → constant",
                      font_size=22, color=BACK, line_spacing=0.8)\
            .next_to(brace_sh, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_sh), FadeIn(sh_lab))           # beat 3

        # it's backbone-dominated
        self.play(FadeOut(VGroup(brace_sh, sh_lab)), run_time=0.4)
        bb = MathTex(r"C\ell_0", r"\approx", r"\lambda_1", r"(u_1^\top \ell_0)", r"\, u_1")\
            .scale(1.1).next_to(eq, DOWN, buff=0.7)
        bb[0].set_color(BACK); bb[2].set_color(EIG); bb[4].set_color(BACK)
        bb_cap = VGroup(
            MathTex(r"\lambda_1", r":\ \text{top eigenvalue}\quad",
                    r"u_1", r":\ \text{leading mode}\quad",
                    r"(u_1^\top \ell_0)", r":\ \text{how much the target loads on it}")
            .scale(0.55),
            Text("→ almost pure backbone (recall c0601)", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(bb, DOWN, buff=0.25)
        bb_cap[0][0].set_color(EIG); bb_cap[0][2].set_color(BACK)
        bb_cap[0][4].set_color(BACK)
        self.play_beat(Write(bb), FadeIn(bb_cap))                          # beat 4

        # more backbone-dominated than scattered case
        self.play(FadeOut(VGroup(bb, bb_cap)), run_time=0.4)
        more = Text("single-target average is MORE backbone-dominated, not less\n"
                    "— everyone adds the same Cℓ₀",
                    font_size=25, color=BAD, line_spacing=0.8)\
            .next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(more, shift=UP * 0.2))                       # beat 5

        # the signal lives in C delta_i
        self.play(FadeOut(more), run_time=0.4)
        brace_pt = Brace(eq[4], DOWN, color=RES)
        pt_lab = Text("patient-specific: size + position within target\n"
                      "the ONLY varying part → the discriminative fingerprint",
                      font_size=22, color=RES, line_spacing=0.8)\
            .next_to(brace_pt, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_pt), FadeIn(pt_lab))           # beat 6

        # so: residualize
        self.play(FadeOut(VGroup(eq, brace_pt, pt_lab)), run_time=0.5)
        res = MathTex(r"\tilde m_i", "=", "m_i", "-", r"\Pi_{\mathcal B}\, m_i")\
            .scale(1.4)
        res[0].set_color(RES); res[2].set_color(VAR); res[4].set_color(BACK)
        res_cap = Text("strip the backbone — let us decode the operator",
                       font_size=24, color=DIM).next_to(res, DOWN, buff=0.4)
        self.play_beat(Write(res), FadeIn(res_cap))                        # beat 7


# ----------------------------------------------------------------------
# Scene 2 — The residualization
# ----------------------------------------------------------------------
class S2_Operator(NarratedScene):
    scene_key = "S2_Operator"

    def construct(self):
        self.header("The residualization  (recall c0601–c0602)")

        # the operator form
        eq = MathTex(r"\tilde m_i", "=", r"\big(I - \Pi_{\mathcal B}\big)", "m_i")\
            .scale(1.4).shift(UP * 1.6)
        eq[0].set_color(RES); eq[2].set_color(BACK); eq[3].set_color(VAR)
        self.play_beat(Write(eq))                                          # beat 1

        # Pi_B onto the backbone subspace
        brace_pi = Brace(eq[2][1:], DOWN, color=BACK)  # under the Pi_B part
        pi_lab = Text("Pi_B : orthogonal projector onto the BACKBONE\n"
                      "span{ u_1, ..., u_r } — the top r connectome eigenvectors",
                      font_size=22, color=BACK, line_spacing=0.8)\
            .next_to(brace_pi, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_pi), FadeIn(pi_lab))           # beat 2

        # closed form for Pi_B
        self.play(FadeOut(VGroup(brace_pi, pi_lab)), run_time=0.4)
        pidef = MathTex(r"\Pi_{\mathcal B}", "=",
                        r"\sum_{j=1}^{r}", r"u_j\, u_j^\top").scale(1.2)
        pidef[0].set_color(BACK); pidef[3].set_color(BACK)
        pidef.next_to(eq, DOWN, buff=0.7)
        pidef_cap = Text("keeps only the part of a map lying along the leading modes",
                         font_size=22, color=DIM).next_to(pidef, DOWN, buff=0.25)
        self.play_beat(Write(pidef), FadeIn(pidef_cap))                    # beat 3

        # applied to m_i gives the backbone slice
        self.play(FadeOut(VGroup(pidef, pidef_cap)), run_time=0.4)
        slice_eq = MathTex(r"\Pi_{\mathcal B}\, m_i", "=",
                           r"\sum_{j=1}^{r} \lambda_j (u_j^\top \ell_i)\, u_j")\
            .scale(1.0).next_to(eq, DOWN, buff=0.7)
        slice_eq[0].set_color(BACK); slice_eq[2].set_color(BACK)
        slice_cap = Text("the dominant, shared, nonspecific bulk the critique named",
                         font_size=22, color=DIM).next_to(slice_eq, DOWN, buff=0.25)
        self.play_beat(Write(slice_eq), FadeIn(slice_cap))                 # beat 4

        # complement projector
        self.play(FadeOut(VGroup(slice_eq, slice_cap)), run_time=0.4)
        comp = MathTex(r"I - \Pi_{\mathcal B}", r"\;=\;",
                       r"\Pi_{\mathcal B}^{\perp}").scale(1.2).next_to(eq, DOWN, buff=0.7)
        comp[0].set_color(BACK); comp[2].set_color(RES)
        comp_cap = Text("projects onto everything orthogonal to the backbone\n"
                        "— the off-backbone tail of the spectrum",
                        font_size=22, color=RES, line_spacing=0.8)\
            .next_to(comp, DOWN, buff=0.25)
        self.play_beat(Write(comp), FadeIn(comp_cap))                      # beat 5

        # what survives: m-tilde ~ complement of C delta_i
        self.play(FadeOut(VGroup(comp, comp_cap)), run_time=0.4)
        surv = MathTex(r"\tilde m_i", r"\approx",
                       r"\big(I - \Pi_{\mathcal B}\big)\, C\delta_i").scale(1.1)
        surv[0].set_color(RES); surv[2].set_color(RES)
        surv.next_to(eq, DOWN, buff=0.7)
        surv_cap = Text("shared Cℓ₀ is gone; only the patient-specific part remains",
                        font_size=22, color=DIM).next_to(surv, DOWN, buff=0.25)
        self.play_beat(Write(surv), FadeIn(surv_cap))                      # beat 6

        # Pi_B is label-blind — fixed before any patient
        self.play(FadeOut(VGroup(surv, surv_cap)), run_time=0.4)
        blind = VGroup(
            Text("Pi_B is fixed BEFORE any patient is seen", font_size=26, color=BACK),
            Text("a property of C alone — label-blind", font_size=24, color=DIM),
            Text("that fixedness is what keeps the move honest", font_size=24, color=RES),
        ).arrange(DOWN, buff=0.22).next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(blind, lag_ratio=0.3))                       # beat 7


# ----------------------------------------------------------------------
# Scene 3 — The VIM fingerprint concentrates
# ----------------------------------------------------------------------
class S3_Fingerprint(NarratedScene):
    scene_key = "S3_Fingerprint"

    def construct(self):
        self.header("The VIM fingerprint concentrates")

        # raw maps: all pointing nearly the same way (the chord)
        origin = LEFT * 3.4 + DOWN * 0.3
        chord = Arrow(origin, origin + RIGHT * 4.2 + UP * 0.4,
                      color=BACK, buff=0, stroke_width=7)
        chord_lab = Text("backbone direction (shared)", font_size=20, color=BACK)\
            .next_to(chord, UP, buff=0.15)
        rays = VGroup(*[
            Arrow(origin, origin + RIGHT * 4.0 + UP * (0.4 + a),
                  color=VAR, buff=0, stroke_width=3)
            for a in (-0.18, 0.0, 0.18, 0.36)
        ])
        rays_lab = Text("raw maps m_i — all nearly parallel", font_size=20, color=VAR)\
            .next_to(chord, DOWN, buff=1.4)
        self.play_beat(Create(chord), FadeIn(chord_lab),
                       Create(rays), FadeIn(rays_lab))                     # beat 1

        # the only difference is C delta_i
        diff = MathTex(r"\text{only difference: }", r"C\delta_i")\
            .scale(0.9).to_edge(DOWN, buff=0.9)
        diff[1].set_color(RES)
        self.play_beat(FadeIn(diff, shift=UP * 0.2))                       # beat 2

        # raw correlation squashed toward 1
        self.play(FadeOut(VGroup(diff, rays_lab)), run_time=0.4)
        squash = MathTex(r"\mathrm{corr}(m_i, m_k)", r"\to", "1")\
            .scale(1.0).to_edge(DOWN, buff=1.0)
        squash[2].set_color(BAD)
        squash_cap = Text("the chord squashes correlations toward one — "
                          "the difference hides in the 3rd decimal",
                          font_size=21, color=DIM).next_to(squash, DOWN, buff=0.2)
        self.play_beat(Write(squash), FadeIn(squash_cap))                  # beat 3

        # apply I - Pi_B : the chord cancels
        self.play(FadeOut(VGroup(squash, squash_cap, chord, chord_lab)),
                  run_time=0.5)
        op = MathTex(r"\big(I - \Pi_{\mathcal B}\big)").scale(1.0)\
            .next_to(rays, UP, buff=0.5)
        op.set_color(RES)
        cross = Cross(chord, stroke_color=BAD, stroke_width=6)
        self.add(chord)
        self.play_beat(FadeIn(op), Create(cross),
                       chord.animate.set_opacity(0.25))                    # beat 4

        # what's left: residual fingerprints, now spread out
        self.play(FadeOut(VGroup(op, cross, chord)),
                  rays.animate.set_color(DIM).set_opacity(0.3), run_time=0.5)
        fan_o = LEFT * 3.0 + DOWN * 0.5
        fan = VGroup(*[
            Arrow(fan_o, fan_o + RIGHT * 2.6 * np.cos(t) + UP * 2.6 * np.sin(t),
                  color=RES, buff=0, stroke_width=4)
            for t in (0.15, 0.55, 0.95, 1.35)
        ])
        fan_lab = MathTex(r"\tilde m_i \approx \big(I-\Pi_{\mathcal B}\big) C\delta_i")\
            .scale(0.9).set_color(RES).next_to(fan, RIGHT, buff=0.8)
        fan_cap = Text("the VIM fingerprint, now SEPARATED in the residual subspace",
                       font_size=21, color=RES).to_edge(DOWN, buff=0.9)
        self.play_beat(Create(fan, lag_ratio=0.2), FadeIn(fan_lab),
                       FadeIn(fan_cap))                                    # beat 5

        # signal-preserving, noise-reducing
        self.play(FadeOut(VGroup(rays, fan, fan_lab, fan_cap)), run_time=0.5)
        snr = MathTex(r"\delta(v)", "=", r"\tilde\delta(v)",
                      r"\quad\text{(signal preserved)}").scale(0.95).shift(UP * 0.7)
        snr[0].set_color(RES); snr[2].set_color(RES)
        snr2 = MathTex(r"\mathrm{Var}(\tilde m)", r"\leq", r"\mathrm{Var}(m)",
                       r"\quad\text{(noise reduced)}").scale(0.95)\
            .next_to(snr, DOWN, buff=0.5)
        snr2[0].set_color(RES); snr2[2].set_color(BAD)
        snr_key = Text("δ(v): between-group signal at voxel v   "
                       "Var(·): within-group variability across patients",
                       font_size=18, color=DIM).next_to(snr2, DOWN, buff=0.35)
        self.play_beat(Write(snr), Write(snr2), FadeIn(snr_key))          # beat 6

        # SNR can only go up
        ineq = MathTex(r"\mathrm{SNR}_{\tilde m}(v)", r"\;\geq\;",
                       r"\mathrm{SNR}_{m}(v)").scale(1.2)\
            .next_to(snr2, DOWN, buff=0.7)
        ineq[0].set_color(RES)
        box = SurroundingRectangle(ineq, color=RES, buff=0.2)
        self.play_beat(Write(ineq), Create(box))                          # beat 7


# ----------------------------------------------------------------------
# Scene 4 — Combine with Move 1
# ----------------------------------------------------------------------
class S4_Combine(NarratedScene):
    scene_key = "S4_Combine"

    def construct(self):
        self.header("Combine with Move 1")

        head = Text("run the outcome-permutation test on the residualized maps",
                    font_size=27, color=WHITE).shift(UP * 2.4)
        self.play_beat(FadeIn(head))                                       # beat 1

        # division of labour
        labour = VGroup(
            VGroup(
                Text("permutation null (Move 1)", font_size=24, color=VAR),
                Text("CALIBRATES — controls false positives", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.12),
            VGroup(
                Text("residualization (Move 2)", font_size=24, color=RES),
                Text("SHARPENS — raises power and specificity", font_size=22, color=DIM),
            ).arrange(DOWN, buff=0.12),
        ).arrange(DOWN, buff=0.5).shift(UP * 0.5)
        self.play_beat(FadeIn(labour, lag_ratio=0.3))                      # beat 2

        # backbone neutralized twice — (1) fixed in null
        self.play(FadeOut(VGroup(head, labour)), run_time=0.5)
        twice = Text("the backbone is neutralized TWICE", font_size=28, color=RES)\
            .shift(UP * 2.3)
        n1 = VGroup(
            Text("1.  in the NULL", font_size=25, color=VAR),
            Text("held fixed by exchangeability → cannot fake a small p",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.14).shift(UP * 1.0)
        self.play_beat(FadeIn(twice), FadeIn(n1, shift=UP * 0.2))          # beat 3

        # (2) projected out of estimate
        n2 = VGroup(
            Text("2.  in the ESTIMATE", font_size=25, color=RES),
            MathTex(r"\text{projected out by } \Pi_{\mathcal B}",
                    r"\ \to\ \text{not even in the statistic}").scale(0.85),
        ).arrange(DOWN, buff=0.16).next_to(n1, DOWN, buff=0.5)
        n2[1].set_color(DIM)
        self.play_beat(FadeIn(n2, shift=UP * 0.2))                        # beat 4

        # size protected by Freedman-Lane
        self.play(FadeOut(VGroup(twice, n1, n2)), run_time=0.5)
        size = VGroup(
            Text("size — the dominant single-target nuisance", font_size=25, color=BAD),
            Text("protected by Freedman-Lane permutation", font_size=24, color=VAR),
            Text("backbone stripped by the projector Pi_B", font_size=24, color=RES),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.8)
        self.play_beat(FadeIn(size, lag_ratio=0.3))                       # beat 5

        # the three conditions together
        self.play(FadeOut(size), run_time=0.4)
        three = VGroup(
            Text("backbone removed", font_size=27, color=RES),
            Text("size controlled", font_size=27, color=VAR),
            Text("outcome permuted", font_size=27, color=EIG),
        ).arrange(RIGHT, buff=0.7).shift(UP * 1.0)
        crit = Text("\"your network is just degree structure\"\n"
                    "must now get past BOTH defences at once",
                    font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(three, DOWN, buff=0.6)
        self.play_beat(FadeIn(three, lag_ratio=0.3), FadeIn(crit))        # beat 6

        # so any signal is clean
        self.play(FadeOut(VGroup(three, crit)), run_time=0.4)
        clean = VGroup(
            Text("signal, if any, is now CLEAN", font_size=30, color=RES),
            Text("not the shared fingerprint, not the dose —", font_size=24, color=DIM),
            MathTex(r"\text{if it clears the threshold, it lives in } C\delta_i")
                .scale(0.9).set_color(RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(clean, lag_ratio=0.3))                      # beat 7


# ----------------------------------------------------------------------
# Scene 5 — The honest caveat
# ----------------------------------------------------------------------
class S5_Caveat(NarratedScene):
    scene_key = "S5_Caveat"

    def construct(self):
        self.header("The honest caveat")

        head = Text("Move 2 rests on one assumption that can fail",
                    font_size=28, color=RES).shift(UP * 2.4)
        self.play_beat(FadeIn(head))                                       # beat 1

        # backbone-sharing assumption
        assume = VGroup(
            Text("Backbone-sharing:", font_size=26, color=BACK),
            MathTex(r"\mathbb{E}\big[\Pi_{\mathcal B} m \mid y{=}1\big]",
                    "=",
                    r"\mathbb{E}\big[\Pi_{\mathcal B} m \mid y{=}0\big]").scale(0.95),
            Text("the shared modes carry no between-group difference\n"
                 "— P1's own convergence claim, read at the population level\n"
                 "(holds only under uniform, NON-overlapping sampling;\n"
                 "real lesions overlap → symptom signal in the off-backbone tail)",
                 font_size=20, color=DIM, line_spacing=0.8),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.6)
        assume[1][0].set_color(BACK); assume[1][2].set_color(BACK)
        self.play_beat(FadeIn(assume, lag_ratio=0.3))                     # beat 2

        # but suppose the effect lived in the backbone
        self.play(FadeOut(VGroup(head, assume)), run_time=0.5)
        suppose = Text("But suppose the real effect lived IN the backbone\n"
                       "— the disease added or removed hubs, not just a sliver",
                       font_size=26, color=WHITE, line_spacing=0.8).shift(UP * 1.6)
        self.play_beat(FadeIn(suppose, shift=UP * 0.2))                   # beat 3

        # then stripping deletes the signal
        danger = MathTex(r"\Pi_{\mathcal B} m", r"\ \text{carries signal}",
                         r"\ \Rightarrow\ ", r"\text{stripping deletes it}")\
            .scale(1.0).next_to(suppose, DOWN, buff=0.7)
        danger[0].set_color(BACK); danger[3].set_color(BAD)
        danger_cap = Text("the cure would erase the disease", font_size=24, color=BAD)\
            .next_to(danger, DOWN, buff=0.3)
        self.play_beat(Write(danger), FadeIn(danger_cap))                 # beat 4

        # so Move 2 is a hypothesis, testable not assumed
        self.play(FadeOut(VGroup(suppose, danger, danger_cap)), run_time=0.5)
        hyp = VGroup(
            Text("Move 2 is not assumed silently.", font_size=27, color=WHITE),
            Text("It is a HYPOTHESIS:", font_size=27, color=RES),
            Text("the VIM fingerprint signal lives OFF the backbone",
                 font_size=25, color=RES),
            Text("— and a hypothesis is testable, not assumed", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.6)
        self.play_beat(FadeIn(hyp, lag_ratio=0.3))                        # beat 5

        # the guard
        self.play(FadeOut(hyp), run_time=0.4)
        guard = VGroup(
            Text("The guard:", font_size=26, color=BACK),
            Text("compare backbone projections across groups\n"
                 "BEFORE you discard them", font_size=24, color=WHITE, line_spacing=0.8),
            Text("if they differ on a mode, do not residualize that mode",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.7)
        self.play_beat(FadeIn(guard, lag_ratio=0.3))                      # beat 6

        # keep the scope
        self.play(FadeOut(guard), run_time=0.4)
        scope = VGroup(
            Text("Keep the scope.", font_size=30, color=RES),
            Text("This move lives inside a STATIC connectome C.",
                 font_size=25, color=WHITE),
            Text("it sharpens the estimate — it cannot recover the\n"
                 "dynamic, higher-order structure C never encoded",
                 font_size=24, color=DIM, line_spacing=0.8),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(scope, lag_ratio=0.3))                      # beat 7
