"""c0602_residualization — "Removing the backbone: degree / PC1 residualization".

Five narrated scenes. Define the residualized map m-tilde_l = Pi_B^perp m_l, show
it equals the spectral tail sum_{j>r} lambda_j (u_j^T l) u_j, define the backbone
fraction rho_B(l), give the geometric projection picture, and bridge to the
signal-to-noise proof (R5) of c0603.

All equations/numbers are from:
  responses/lnm_critique/sections/04_removing_the_backbone.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0602_residualization ./render.sh \
      chapters/c0602_residualization/scenes.py -q ql \
      S1_Define S2_Zeroing S3_Fraction S4_Picture S5_Bridge
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — define the residualized map
# ----------------------------------------------------------------------
class S1_Define(NarratedScene):
    scene_key = "S1_Define"

    def construct(self):
        self.header("The residualized map")

        # m_l = C l
        raw = MathTex("m", r"_{\ell}", "=", "C", r"\ell").scale(1.4).shift(UP * 1.9)
        raw[0].set_color(VAR); raw[1].set_color(VAR)
        raw[3].set_color(WHITE); raw[4].set_color(VAR)
        rb = Brace(raw, DOWN, color=DIM)
        rl = Text("seed-based map: connectome C times lesion seed ell",
                  font_size=22, color=DIM).next_to(rb, DOWN, buff=0.18)
        self.play_beat(Write(raw), GrowFromCenter(rb), FadeIn(rl))          # beat 1

        # R1 threat: backbone domination
        self.play(FadeOut(VGroup(rb, rl)), raw.animate.scale(0.7).to_edge(UP, buff=1.0),
                  run_time=0.5)
        threat = VGroup(
            Text("R1: m_ell is mostly ONE shared pattern", font_size=27, color=BAD),
            Text("the backbone — the connectome's hub / degree structure",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.6)
        self.play_beat(FadeIn(threat[0]), FadeIn(threat[1], shift=UP * 0.2))  # beat 2

        # the projector Pi_B^perp
        self.play(FadeOut(threat), run_time=0.4)
        # NOTE: a lone r"\qquad" arg renders to zero glyphs and would be dropped,
        # shifting every later index. Fold the spacer into the preceding arg so
        # each indexed argument stays visibly non-empty.
        proj = MathTex(r"\Pi_{\mathcal B}", "=", r"\sum_{j=1}^{r}", "u_j", r"u_j^{\top}\qquad",
                       r"\Pi_{\mathcal B}^{\perp}", "=", "I", "-", r"\Pi_{\mathcal B}")\
            .scale(1.0).shift(UP * 0.9)
        proj[0].set_color(BACK); proj[3].set_color(BACK); proj[4].set_color(BACK)
        proj[5].set_color(RES); proj[9].set_color(BACK)
        pcap = Text("pick rank r leading modes = backbone;  pi-perp keeps the orthogonal rest",
                    font_size=22, color=DIM).next_to(proj, DOWN, buff=0.3)
        self.play_beat(Write(proj), FadeIn(pcap))                           # beat 3

        # the definition m-tilde = Pi_B^perp m_l
        self.play(FadeOut(VGroup(proj, pcap)), run_time=0.4)
        defn = MathTex(r"\tilde m", r"_{\ell}", "=", "m", r"_{\ell}", "-",
                       r"\Pi_{\mathcal B}", "m", r"_{\ell}", "=",
                       r"\Pi_{\mathcal B}^{\perp}", "m", r"_{\ell}")\
            .scale(1.2).shift(UP * 0.8)
        defn[0].set_color(RES); defn[1].set_color(RES)
        defn[3].set_color(VAR); defn[4].set_color(VAR)
        defn[6].set_color(BACK); defn[7].set_color(VAR); defn[8].set_color(VAR)
        defn[10].set_color(RES); defn[11].set_color(VAR); defn[12].set_color(VAR)
        db = Brace(defn, DOWN, color=RES)
        dl = Text("subtract the backbone part, keep the rest",
                  font_size=24, color=RES).next_to(db, DOWN, buff=0.18)
        self.play_beat(Write(defn), GrowFromCenter(db), FadeIn(dl))         # beat 4

        # closed form: spectral tail
        self.play(FadeOut(VGroup(db, dl)), defn.animate.scale(0.7).to_edge(UP, buff=1.0),
                  run_time=0.5)
        tail = MathTex(r"\tilde m", r"_{\ell}", "=", r"\sum_{j>r}",
                       r"\lambda_j", r"\,(", r"u_j^{\top}", r"\ell", r")\,", "u_j")\
            .scale(1.15).shift(UP * 0.5)
        tail[0].set_color(RES); tail[1].set_color(RES)
        tail[4].set_color(EIG); tail[6].set_color(BACK); tail[7].set_color(VAR)
        tail[9].set_color(BACK)
        self.play_beat(Write(tail))                                        # beat 5

        # decode each symbol
        b_lam = Brace(tail[4], DOWN, color=EIG)
        l_lam = Text("eigenvalue", font_size=20, color=EIG).next_to(b_lam, DOWN, buff=0.12)
        b_u = Brace(tail[9], UP, color=BACK)
        l_u = Text("mode j", font_size=20, color=BACK).next_to(b_u, UP, buff=0.12)
        b_c = Brace(tail[6:8], DOWN, color=BACK)
        l_c = Text("seed's loading on mode j", font_size=20, color=BACK)\
            .next_to(b_c, DOWN, buff=0.12).shift(RIGHT * 0.9)
        self.play_beat(GrowFromCenter(b_lam), FadeIn(l_lam),
                       GrowFromCenter(b_u), FadeIn(l_u),
                       GrowFromCenter(b_c), FadeIn(l_c))                    # beat 6

        # the moral: zero out the first r terms
        self.play(FadeOut(VGroup(b_lam, l_lam, b_u, l_u, b_c, l_c)), run_time=0.4)
        moral = Text("residualizing against the top r modes\n= discarding the first r spectral terms — exactly, by construction",
                     font_size=25, color=WHITE, line_spacing=0.8).to_edge(DOWN, buff=0.9)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 2 — zeroing the leading coefficients
# ----------------------------------------------------------------------
class S2_Zeroing(NarratedScene):
    scene_key = "S2_Zeroing"

    def construct(self):
        self.header("Zeroing leading coefficients")

        # full spectral expansion
        full = MathTex("m", r"_{\ell}", "=", r"\sum_{j=1}^{V}", r"\lambda_j",
                       r"\,(", r"u_j^{\top}", r"\ell", r")\,", "u_j")\
            .scale(1.2).shift(UP * 1.9)
        full[0].set_color(VAR); full[1].set_color(VAR)
        full[4].set_color(EIG); full[6].set_color(BACK); full[7].set_color(VAR)
        full[9].set_color(BACK)
        self.play_beat(Write(full))                                        # beat 1

        # each term = mode scaled by two numbers
        terms = Text("each term: a connectome mode u_j, scaled by two numbers",
                     font_size=25, color=DIM).next_to(full, DOWN, buff=0.5)
        b1 = Brace(full[4], DOWN, color=EIG)
        t1 = Text("eigenvalue lambda_j", font_size=21, color=EIG).next_to(b1, DOWN, buff=0.12)
        self.play_beat(FadeIn(terms), GrowFromCenter(b1), FadeIn(t1))      # beat 2

        # the coefficient u_j^T l
        self.play(FadeOut(VGroup(b1, t1)), run_time=0.3)
        b2 = Brace(full[5:9], DOWN, color=BACK)
        t2 = Text("coefficient u_j-transpose-ell = projection of the seed onto mode j",
                  font_size=22, color=BACK).next_to(b2, DOWN, buff=0.12)
        self.play_beat(GrowFromCenter(b2), FadeIn(t2))                     # beat 3

        # residualization sets j<=r to zero
        self.play(FadeOut(VGroup(terms, b2, t2)),
                  full.animate.scale(0.75).to_edge(UP, buff=1.0), run_time=0.5)
        split = MathTex(r"\tilde m", r"_{\ell}", "=",
                        r"\underbrace{\sum_{j\le r}\lambda_j(u_j^{\top}\ell)u_j}_{\text{set to }0}",
                        "+", r"\sum_{j>r}\lambda_j(u_j^{\top}\ell)u_j")\
            .scale(0.95).shift(UP * 0.4)
        split[0].set_color(RES); split[1].set_color(RES)
        split[3].set_color(BAD); split[5].set_color(RES)
        self.play_beat(Write(split))                                       # beat 4

        # u_1 is the degree mode, huge & shared
        self.play(FadeOut(split), run_time=0.4)
        deg = MathTex("u_1", "=", r"\tfrac{1}{\sqrt V}(1,1,\dots,1)^{\top}")\
            .scale(1.1).shift(UP * 0.9)
        deg[0].set_color(BACK)
        degcap = Text("the all-positive degree mode: every non-empty seed loads on it\nso the first term is huge and shared by everyone",
                      font_size=23, color=DIM, line_spacing=0.8).next_to(deg, DOWN, buff=0.35)
        self.play_beat(Write(deg), FadeIn(degcap))                         # beat 5

        # drop the top term -> chord gone
        self.play(FadeOut(VGroup(deg, degcap)), run_time=0.4)
        chord = VGroup(
            Text("drop the top term", font_size=27, color=BAD),
            Text("→  the loud common chord disappears", font_size=27, color=WHITE),
            Text("what remains is the tail — where seeds differ", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.4)
        self.play_beat(LaggedStart(*[FadeIn(c) for c in chord], lag_ratio=0.3))  # beat 6

        # the tail is where signal could live
        keep = MathTex(r"\tilde m", r"_{\ell}", "=", r"\sum_{j=r+1}^{V}",
                       r"\lambda_j(u_j^{\top}\ell)u_j").scale(1.0)
        keep[0].set_color(RES); keep[1].set_color(RES); keep[4].set_color(RES)
        keepcap = Text("the only place a disorder-specific signal could live",
                       font_size=24, color=RES)
        block = VGroup(keep, keepcap).arrange(DOWN, buff=0.35).to_edge(DOWN, buff=0.8)
        self.play_beat(Write(keep), FadeIn(keepcap))                       # beat 7


# ----------------------------------------------------------------------
# Scene 3 — the backbone fraction
# ----------------------------------------------------------------------
class S3_Fraction(NarratedScene):
    scene_key = "S3_Fraction"

    def construct(self):
        self.header("The backbone fraction")

        intro = Text("how much of a raw map lives in the backbone?",
                     font_size=28, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # norm-ratio definition
        ratio = MathTex(r"\rho_{\mathcal B}", r"(\ell)", "=",
                        r"\frac{\big\|\Pi_{\mathcal B} m_{\ell}\big\|^2}{\big\|m_{\ell}\big\|^2}")\
            .scale(1.3).shift(UP * 0.7)
        ratio[0].set_color(BACK); ratio[1].set_color(VAR); ratio[3].set_color(WHITE)
        nb = Brace(ratio[3], DOWN, color=DIM)
        nl = Text("squared norm of the backbone part  /  squared norm of the whole map",
                  font_size=22, color=DIM).next_to(nb, DOWN, buff=0.2)
        self.play_beat(Write(ratio), GrowFromCenter(nb), FadeIn(nl),
                       intro.animate.set_opacity(0.4))                     # beat 2

        # spectral numerator
        self.play(FadeOut(VGroup(nb, nl, intro)),
                  ratio.animate.scale(0.7).to_edge(UP, buff=1.0), run_time=0.5)
        spec = MathTex(r"\rho_{\mathcal B}(\ell)", "=",
                       r"\frac{\sum_{j\le r}\lambda_j^2 (u_j^{\top}\ell)^2}"
                       r"{\sum_{j}\lambda_j^2 (u_j^{\top}\ell)^2}")\
            .scale(1.1).shift(UP * 0.5)
        spec[0].set_color(BACK); spec[2].set_color(WHITE)
        nb2 = Brace(spec[2], UP, color=BACK)
        nl2 = Text("numerator: leading modes only, j up to r", font_size=21, color=BACK)\
            .next_to(nb2, UP, buff=0.15)
        self.play_beat(Write(spec), GrowFromCenter(nb2), FadeIn(nl2))      # beat 3

        # denominator = all modes -> share of energy
        self.play(FadeOut(VGroup(nb2, nl2)), run_time=0.3)
        db = Brace(spec[2], DOWN, color=DIM)
        dl = Text("denominator: all modes → rho-B is the share of map energy in the backbone",
                  font_size=22, color=DIM).next_to(db, DOWN, buff=0.18)
        self.play_beat(GrowFromCenter(db), FadeIn(dl))                     # beat 4

        # R1: rho_B ~ 1
        self.play(FadeOut(VGroup(db, dl)), run_time=0.3)
        r1 = MathTex(r"\rho_{\mathcal B}(\ell)", r"\approx", "1",
                     r"\quad\text{for almost every }", r"\ell").scale(1.0)
        r1[0].set_color(BACK); r1[2].set_color(BAD); r1[4].set_color(VAR)
        r1cap = Text("because lambda-one dwarfs the rest, and every seed loads on u-one",
                     font_size=23, color=DIM)
        block = VGroup(r1, r1cap).arrange(DOWN, buff=0.3).shift(DOWN * 0.7)
        self.play_beat(Write(r1), FadeIn(r1cap))                           # beat 5

        # the symmetry: residual keeps 1 - rho_B
        self.play(FadeOut(block), run_time=0.4)
        sym = MathTex(r"\frac{\|\tilde m_{\ell}\|^2}{\|m_{\ell}\|^2}", "=",
                      "1", "-", r"\rho_{\mathcal B}(\ell)").scale(1.2).shift(UP * 0.3)
        sym[0].set_color(RES); sym[4].set_color(BACK)
        symcap = Text("what R1 calls nonspecific is exactly what residualization deletes",
                      font_size=24, color=RES).next_to(sym, DOWN, buff=0.4)
        self.play_beat(Write(sym), FadeIn(symcap))                         # beat 6

        # high rho_B is the good regime
        self.play(FadeOut(VGroup(sym, symcap)), run_time=0.4)
        good = VGroup(
            Text("high rho-B  →  raw map is almost all hub", font_size=26, color=WHITE),
            Text("not a worry — the regime where projecting it out", font_size=25, color=BACK),
            Text("costs little and clarifies much", font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.25).shift(DOWN * 0.1)
        self.play_beat(FadeIn(good, shift=UP * 0.2))                       # beat 7


# ----------------------------------------------------------------------
# Scene 4 — geometric picture
# ----------------------------------------------------------------------
class S4_Picture(NarratedScene):
    scene_key = "S4_Picture"

    def construct(self):
        self.header("Geometric picture")

        # axes: a plane with a backbone axis u_1
        plane = NumberPlane(
            x_range=[-4, 4, 1], y_range=[-2.6, 2.6, 1],
            background_line_style={"stroke_color": DIM, "stroke_opacity": 0.18,
                                   "stroke_width": 1},
            axis_config={"stroke_color": DIM, "stroke_opacity": 0.3},
        ).shift(DOWN * 0.2)
        u1_axis = Arrow(plane.c2p(0, 0), plane.c2p(3.4, 0), color=BACK,
                        buff=0, stroke_width=5)
        u1_lab = MathTex("u_1", color=BACK).scale(0.9).next_to(u1_axis, RIGHT, buff=0.15)
        u1_cap = Text("the backbone axis (degree mode)", font_size=22, color=BACK)\
            .next_to(plane, UP, buff=0.15)
        self.play_beat(Create(plane), GrowArrow(u1_axis), FadeIn(u1_lab),
                       FadeIn(u1_cap))                                     # beat 1

        # two seeds, both nearly along u_1
        mA = Arrow(plane.c2p(0, 0), plane.c2p(3.0, 0.55), color=VAR,
                   buff=0, stroke_width=5)
        mB = Arrow(plane.c2p(0, 0), plane.c2p(2.9, -0.5), color="#C77DFF",
                   buff=0, stroke_width=5)
        mA_lab = MathTex("m_A", color=VAR).scale(0.8).next_to(mA.get_end(), UR, buff=0.05)
        mB_lab = MathTex("m_B", color="#C77DFF").scale(0.8).next_to(mB.get_end(), DR, buff=0.05)
        self.play_beat(GrowArrow(mA), GrowArrow(mB), FadeIn(mA_lab), FadeIn(mB_lab))  # beat 2

        # near parallel -> correlation near 1
        corr = MathTex(r"r(m_A, m_B)", r"\approx", "1").scale(1.0)\
            .to_corner(UR, buff=0.5)
        corr[2].set_color(BAD)
        corr_cap = Text("R1's convergence — but only the GROUP AVERAGE\nunder uniform, NON-overlapping sampling",
                        font_size=20, color=BAD, line_spacing=0.8)\
            .next_to(corr, DOWN, buff=0.2).align_to(corr, RIGHT)
        self.play_beat(FadeIn(corr), FadeIn(corr_cap))                    # beat 3

        # project onto plane orthogonal to u_1 (here the vertical line)
        perp_line = DashedLine(plane.c2p(0, -2.3), plane.c2p(0, 2.3),
                               color=RES, stroke_width=3)
        perp_lab = MathTex(r"\Pi_{\mathcal B}^{\perp}", color=RES).scale(0.85)\
            .next_to(perp_line, UP, buff=0.1)
        projA = DashedLine(mA.get_end(), plane.c2p(0, 0.55), color=DIM, stroke_width=2)
        projB = DashedLine(mB.get_end(), plane.c2p(0, -0.5), color=DIM, stroke_width=2)
        self.play_beat(Create(perp_line), FadeIn(perp_lab),
                       Create(projA), Create(projB))                      # beat 4

        # residual arrows: off-backbone, no longer parallel
        rA = Arrow(plane.c2p(0, 0), plane.c2p(0, 0.55), color=VAR,
                   buff=0, stroke_width=6)
        rB = Arrow(plane.c2p(0, 0), plane.c2p(0, -0.5), color="#C77DFF",
                   buff=0, stroke_width=6)
        rA_lab = MathTex(r"\tilde m_A", color=VAR).scale(0.75).next_to(rA, LEFT, buff=0.1)
        rB_lab = MathTex(r"\tilde m_B", color="#C77DFF").scale(0.75).next_to(rB, LEFT, buff=0.1)
        self.play_beat(GrowArrow(rA), GrowArrow(rB), FadeIn(rA_lab), FadeIn(rB_lab),
                       FadeOut(VGroup(projA, projB)))                      # beat 5

        # correlation drops
        corr2 = MathTex(r"r(\tilde m_A, \tilde m_B)", r"\ll", "1").scale(1.0)\
            .to_corner(DR, buff=0.5)
        corr2[0].set_color(RES); corr2[2].set_color(RES)
        corr2_cap = Text("real lesions overlap & sample specific rows of C:\nsame-symptom r = 0.44  vs  0.16 to the degree map",
                         font_size=19, color=RES, line_spacing=0.8)\
            .next_to(corr2, UP, buff=0.18).align_to(corr2, RIGHT)
        self.play_beat(Transform(corr, corr2), Transform(corr_cap, corr2_cap))  # beat 6

        # scale-up note
        self.play(FadeOut(VGroup(plane, u1_axis, u1_lab, u1_cap, mA, mB, mA_lab,
                                 mB_lab, perp_line, perp_lab, rA, rB, rA_lab,
                                 rB_lab, corr, corr_cap)), run_time=0.5)
        scale = Text("Same arithmetic, scaled to ~100,000 voxels and the empirical\nconnectome elbow at a handful of modes — the real procedure.",
                     font_size=26, color=WHITE, line_spacing=0.8)
        self.play_beat(FadeIn(scale, shift=UP * 0.2))                     # beat 7


# ----------------------------------------------------------------------
# Scene 5 — does it actually help? (bridge to c0603)
# ----------------------------------------------------------------------
class S5_Bridge(NarratedScene):
    scene_key = "S5_Bridge"

    def construct(self):
        self.header("Does it actually help?")

        q = Text("the geometry is clean — but does removing variance HELP?",
                 font_size=28, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(q))                                         # beat 1

        # R5 claim
        claim = VGroup(
            Text("R5 (to prove next):", font_size=27, color=RES),
            Text("residualization raises the signal-to-noise ratio", font_size=26, color=WHITE),
            Text("signal-preserving  AND  noise-reducing", font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.7)
        self.play_beat(FadeIn(claim, shift=UP * 0.2), q.animate.set_opacity(0.4))  # beat 2

        # signal-preserving line
        self.play(FadeOut(VGroup(q, claim)), run_time=0.4)
        sig = VGroup(
            Text("✓ signal-preserving", font_size=26, color=BACK),
            Text("the backbone carries no between-group mean difference,",
                 font_size=24, color=WHITE),
            Text("so all of the signal sits in the residual", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).shift(UP * 1.3)
        self.play_beat(FadeIn(sig, shift=UP * 0.2))                       # beat 3

        # the backbone-sharing assumption (typed)
        bs = MathTex(r"\mathbb{E}\big[\Pi_{\mathcal B} m_{\ell}\,\big|\,y{=}1\big]",
                     "=", r"\mathbb{E}\big[\Pi_{\mathcal B} m_{\ell}\,\big|\,y{=}0\big]")\
            .scale(0.95).next_to(sig, DOWN, buff=0.5)
        bs[0].set_color(BACK); bs[2].set_color(BACK)
        bscap = Text("backbone-sharing: same backbone in labelled & unlabelled groups\nneeds only the few LEADING shared modes to be label-free —\nthe off-backbone tail may still carry the symptom signal",
                     font_size=21, color=DIM, line_spacing=0.8).next_to(bs, DOWN, buff=0.25)
        self.play_beat(Write(bs), FadeIn(bscap))                          # beat 4

        # noise-reducing line
        self.play(FadeOut(VGroup(sig, bs, bscap)), run_time=0.4)
        noise = VGroup(
            Text("✓ noise-reducing", font_size=26, color=BACK),
            Text("within-group variance of the raw map is dominated", font_size=24, color=WHITE),
            Text("by the big lambda-one backbone term", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).shift(UP * 1.2)
        tstat = MathTex(r"t = \frac{\tilde\delta(v)}{\sqrt{\mathrm{Var}(\tilde m(v))}}",
                        r"\ \Rightarrow\ ", r"\text{denominator shrinks}")\
            .scale(0.95).next_to(noise, DOWN, buff=0.5)
        tstat[0].set_color(RES); tstat[2].set_color(BAD)
        self.play_beat(FadeIn(noise, shift=UP * 0.2), Write(tstat))       # beat 5

        # the caveat
        self.play(FadeOut(VGroup(noise, tstat)), run_time=0.4)
        warn = VGroup(
            Text("⚠ caveat", font_size=27, color=BAD),
            Text("residualization helps ONLY if the signal is off-backbone",
                 font_size=25, color=WHITE),
            Text("if the disease shifts the backbone itself,", font_size=24, color=DIM),
            Text("projecting it out would delete the signal", font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.5)
        self.play_beat(FadeIn(warn, shift=UP * 0.2))                      # beat 6

        # bridge to c0603
        self.play(FadeOut(warn), run_time=0.4)
        nxt = VGroup(
            Text("Next (c0603):", font_size=28, color=RES),
            Text("prove the SNR inequality precisely,", font_size=26, color=WHITE),
            Text("and state the exact condition for a free removal.", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.28)
        self.play_beat(FadeIn(nxt, lag_ratio=0.3))                        # beat 7
