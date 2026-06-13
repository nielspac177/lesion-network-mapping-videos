"""c0202_backbone_term — The map in the spectral basis.

We rewrite the seed map m = C ell in the eigenbasis of the symmetric connectome
C = sum_j lambda_j u_j u_j^T, so that

    m = C ell = sum_j lambda_j (u_j^T ell) u_j,

then isolate the BACKBONE TERM lambda_1 (u_1^T ell) u_1, read the spectral gap
lambda_2 / lambda_1, separate the off-backbone remainder (j >= 2), run a numeric
check with the source's three-voxel spectrum lambda = (4.0, 0.3, 0.1), and close
with the careful balanced caveat: this is about the MAP'S DIRECTION, owned by the
spectrum of C, not yet a statement about whether a symptom CONTRAST carries signal.

Every equation/number is from responses/lnm_critique/sections/02_what_is_entailed.md
(the spectral expansion, the leading term, the cos^2 angle bound) and the source's
three-voxel spectrum lambda = (4.0, 0.3, 0.1) used in c0101_map_operator.

Render:
  MEDIA=$HOME/lnm_media/c0202_backbone_term ./render.sh \
      chapters/c0202_backbone_term/scenes.py -q ql \
      S1_Spectral S2_Backbone S3_Gap S4_Remainder S5_Numeric S6_Takeaway
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# S1 — Push a lesion through C in the spectral basis.
# ----------------------------------------------------------------------
class S1_Spectral(NarratedScene):
    scene_key = "S1_Spectral"

    def construct(self):
        self.header("The map in the spectral basis")

        # m = C ell, the operator we already built.
        eq = MathTex("m", "=", "C", r"\ell").scale(1.8).shift(UP * 1.9)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        lens = Text("look at it through the eigenbasis of C",
                    font_size=25, color=DIM).next_to(eq, DOWN, buff=0.5)
        self.play_beat(Write(eq), FadeIn(lens))

        # spectral decomposition of the symmetric C.
        self.play(FadeOut(lens), eq.animate.scale(0.6).to_corner(UL).shift(DOWN * 0.6),
                  run_time=0.5)
        spec = MathTex("C", "=", r"\sum_j", r"\lambda_j", "u_j", "u_j^{\\top}")\
            .scale(1.3).shift(UP * 1.2)
        spec[0].set_color(WHITE); spec[3].set_color(EIG); spec[4].set_color(BACK)
        spec[5].set_color(BACK)
        speccap = Text("C is symmetric, so it has a spectral decomposition",
                       font_size=24, color=DIM).next_to(spec, DOWN, buff=0.4)
        self.play_beat(Write(spec), FadeIn(speccap))

        # name lambda_j and u_j with braces.
        self.play(FadeOut(speccap), run_time=0.3)
        br_lam = Brace(spec[3], DOWN, color=EIG)
        lam_lab = br_lam.get_text("eigenvalues: the strengths, largest first")
        lam_lab.set_color(EIG).scale(0.65)
        br_u = Brace(VGroup(spec[4], spec[5]), UP, color=BACK)
        u_lab = br_u.get_text("eigenvectors: the connectome's patterns")
        u_lab.set_color(BACK).scale(0.65)
        self.play_beat(GrowFromCenter(br_lam), FadeIn(lam_lab),
                       GrowFromCenter(br_u), FadeIn(u_lab))

        # push ell through -> the spectral expansion of m.
        self.play(FadeOut(VGroup(br_lam, lam_lab, br_u, u_lab, spec)), run_time=0.4)
        exp = MathTex("m", "=", "C", r"\ell", "=",
                      r"\sum_j", r"\lambda_j", r"(u_j^{\top}\ell)", "u_j")\
            .scale(1.15).shift(UP * 0.9)
        exp[0].set_color(VAR); exp[3].set_color(VAR)
        exp[6].set_color(EIG); exp[7].set_color(VAR); exp[8].set_color(BACK)
        self.play_beat(Write(exp))

        # the inner product (u_j^T ell): how much the lesion overlaps pattern j.
        br_ip = Brace(exp[7], DOWN, color=VAR)
        ip_lab = br_ip.get_text("inner product: how much the lesion overlaps pattern j")
        ip_lab.set_color(VAR).scale(0.62)
        ipnum = Text("one number per pattern — the lesion's alignment with u_j",
                     font_size=22, color=DIM).next_to(ip_lab, DOWN, buff=0.4)
        self.play_beat(GrowFromCenter(br_ip), FadeIn(ip_lab), FadeIn(ipnum))

        # the recipe reading.
        self.play(FadeOut(VGroup(br_ip, ip_lab, ipnum)), run_time=0.3)
        recipe = VGroup(
            Text("u_j : the pattern poured in", font_size=25, color=BACK),
            Text("lambda_j : its strength (eigenvalue)", font_size=25, color=EIG),
            Text("(u_j^T ell) : how much the lesion overlaps it", font_size=25, color=VAR),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).next_to(exp, DOWN, buff=0.8)
        self.play_beat(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in recipe],
                                   lag_ratio=0.35))


# ----------------------------------------------------------------------
# S2 — Isolate the backbone term.
# ----------------------------------------------------------------------
class S2_Backbone(NarratedScene):
    scene_key = "S2_Backbone"

    def construct(self):
        self.header("The backbone term")

        # the full sum, with j=1 about to be pulled out.
        full = MathTex("m", "=", r"\lambda_1", r"(u_1^{\top}\ell)", "u_1", "+",
                       r"\sum_{j\ge 2}", r"\lambda_j", r"(u_j^{\top}\ell)", "u_j")\
            .scale(1.0).shift(UP * 1.6)
        full[0].set_color(VAR)
        full[2].set_color(EIG); full[3].set_color(VAR); full[4].set_color(BACK)
        full[7].set_color(EIG); full[8].set_color(VAR); full[9].set_color(DIM)
        self.play_beat(Write(full))

        # isolate the backbone term big and centered.
        bb = MathTex(r"m_{\ell}^{\,\mathrm{bb}}", "=",
                     r"\lambda_1", r"(u_1^{\top}\ell)", "u_1").scale(1.4)
        bb[0].set_color(RES); bb[2].set_color(EIG); bb[3].set_color(VAR); bb[4].set_color(BACK)
        bb.next_to(full, DOWN, buff=0.9)
        box = SurroundingRectangle(full[2:5], color=RES, buff=0.12)
        self.play_beat(Create(box), TransformFromCopy(full[2:5], bb[2:]), Write(bb[:2]))

        # annotate lambda_1: the largest eigenvalue.
        br_l1 = Brace(bb[2], DOWN, color=EIG)
        l1_lab = br_l1.get_text("largest eigenvalue").set_color(EIG).scale(0.7)
        self.play_beat(GrowFromCenter(br_l1), FadeIn(l1_lab))

        # annotate (u_1^T ell): overlap with top pattern, generically nonzero.
        self.play(FadeOut(VGroup(br_l1, l1_lab)), run_time=0.3)
        br_c1 = Brace(bb[3], DOWN, color=VAR)
        c1_lab = br_c1.get_text("overlap with the top pattern, generically nonzero")
        c1_lab.set_color(VAR).scale(0.62)
        self.play_beat(GrowFromCenter(br_c1), FadeIn(c1_lab))

        # annotate u_1: the backbone direction.
        self.play(FadeOut(VGroup(br_c1, c1_lab)), run_time=0.3)
        br_u1 = Brace(bb[4], UP, color=BACK)
        u1_lab = br_u1.get_text("the backbone: hub-shaped dominant pattern")
        u1_lab.set_color(BACK).scale(0.62)
        self.play_beat(GrowFromCenter(br_u1), FadeIn(u1_lab))

        # the chapter question.
        self.play(FadeOut(VGroup(br_u1, u1_lab, box, full)),
                  bb.animate.to_edge(UP, buff=1.3), run_time=0.5)
        q = Text("When does this one term drown out all the rest?",
                 font_size=30, color=RES).shift(DOWN * 0.3)
        self.play_beat(FadeIn(q, shift=UP * 0.15))


# ----------------------------------------------------------------------
# S3 — The spectral gap and the cos^2 bound.
# ----------------------------------------------------------------------
class S3_Gap(NarratedScene):
    scene_key = "S3_Gap"

    def construct(self):
        self.header("The spectral gap")

        # the gap ratio.
        gap = MathTex(r"\frac{\lambda_2}{\lambda_1}").scale(2.0).shift(UP * 1.7)
        gap.set_color(EIG)
        gaplab = Text("the spectral gap", font_size=26, color=DIM)\
            .next_to(gap, RIGHT, buff=0.6)
        self.play_beat(Write(gap), FadeIn(gaplab))

        # small ratio = large gap.
        small = Text("small ratio  =  large gap:   lambda_2 tiny next to lambda_1",
                     font_size=26, color=BACK).next_to(gap, DOWN, buff=0.7)
        self.play_beat(FadeIn(small))

        # why one term dominates: lagging eigenvalues cap the rest.
        why = Text("every term past the first is capped by its eigenvalue —\n"
                   "and those have already collapsed",
                   font_size=25, color=DIM, line_spacing=0.9).next_to(small, DOWN, buff=0.5)
        self.play_beat(FadeIn(why))

        # introduce cos^2 of the angle.
        self.play(FadeOut(VGroup(gap, gaplab, small, why)), run_time=0.4)
        cos_intro = MathTex(r"\cos^2 \angle(m,\, u_1)").scale(1.3).shift(UP * 1.9)
        cos_intro[0].set_color(RES)
        ci_cap = Text("squared cosine of the angle between the map and the backbone",
                      font_size=23, color=DIM).next_to(cos_intro, DOWN, buff=0.35)
        self.play_beat(Write(cos_intro), FadeIn(ci_cap))

        # the bound itself (source Eq.), with c_j = u_j^T ell.
        self.play(FadeOut(ci_cap), cos_intro.animate.scale(0.85).shift(UP * 0.2 + LEFT * 3.4),
                  run_time=0.5)
        bound = MathTex("=",
                        r"\frac{\lambda_1^2 c_1^2}{\sum_j \lambda_j^2 c_j^2}")\
            .scale(1.2).next_to(cos_intro, RIGHT, buff=0.3)
        bound[1].set_color(WHITE)
        cdef = MathTex("c_j", "=", r"u_j^{\top}\ell").scale(0.95)\
            .next_to(VGroup(cos_intro, bound), DOWN, buff=0.7)
        cdef[0].set_color(VAR); cdef[2].set_color(VAR)
        cdefcap = Text("c_j is the overlap of the lesion with pattern j",
                       font_size=22, color=DIM).next_to(cdef, DOWN, buff=0.3)
        self.play_beat(Write(bound), Write(cdef), FadeIn(cdefcap))

        # send the gap to zero -> cos^2 -> 1.
        self.play(FadeOut(VGroup(cdef, cdefcap)), run_time=0.3)
        limit = MathTex(r"\frac{\lambda_2}{\lambda_1} \to 0",
                        r"\ \Longrightarrow\ ",
                        r"\cos^2 \angle(m,\, u_1) \to 1").scale(1.0)\
            .next_to(VGroup(cos_intro, bound), DOWN, buff=0.8)
        limit[0].set_color(EIG); limit[2].set_color(RES)
        self.play_beat(Write(limit))

        # cos=1 means angle 0: aligns with u_1 regardless of voxels.
        self.play(FadeOut(VGroup(cos_intro, bound, limit)), run_time=0.4)
        align = VGroup(
            Text("cosine one  =  angle zero", font_size=30, color=RES),
            Text('the map "aligns with the backbone u_1\n'
                 'regardless of which voxels the lesions marked"',
                 font_size=26, color=BACK, line_spacing=0.95),
        ).arrange(DOWN, buff=0.5)
        self.play_beat(FadeIn(align[0], shift=UP * 0.15), FadeIn(align[1]))


# ----------------------------------------------------------------------
# S4 — The off-backbone remainder.
# ----------------------------------------------------------------------
class S4_Remainder(NarratedScene):
    scene_key = "S4_Remainder"

    def construct(self):
        self.header("The off-backbone remainder")

        # the honest split.
        intro = Text("the map is not only its backbone term — split it honestly",
                     font_size=26, color=DIM).to_edge(UP, buff=1.1)
        self.play_beat(FadeIn(intro))

        split = MathTex("m", "=",
                        r"\underbrace{\lambda_1 (u_1^{\top}\ell)\, u_1}_{\text{backbone}}",
                        "+",
                        r"\underbrace{\sum_{j\ge 2} \lambda_j (u_j^{\top}\ell)\, u_j}_{\text{remainder}}")\
            .scale(1.0).shift(UP * 0.4)
        split[0].set_color(VAR)
        split[2].set_color(BACK)
        split[4].set_color(BAD)
        self.play_beat(Write(split))

        # the remainder lives in u_2, u_3, ...
        rem_dir = Text("the remainder lives in u_2, u_3, ... — the subtler patterns",
                       font_size=25, color=DIM).next_to(split, DOWN, buff=0.7)
        self.play_beat(FadeIn(rem_dir))

        # bounded by lagging eigenvalues.
        self.play(FadeOut(rem_dir), run_time=0.3)
        capeq = MathTex(r"\|m_{\mathrm{rem}}\|^2", "=",
                        r"\sum_{j\ge 2} \lambda_j^2 c_j^2",
                        r"\ \le\ ", r"\lambda_2^2 \sum_{j\ge 2} c_j^2")\
            .scale(0.95).next_to(split, DOWN, buff=0.7)
        capeq[0].set_color(BAD); capeq[2].set_color(WHITE); capeq[4].set_color(EIG)
        capcap = Text("each off-backbone term carries a small eigenvalue (j >= 2)",
                      font_size=23, color=DIM).next_to(capeq, DOWN, buff=0.35)
        self.play_beat(Write(capeq), FadeIn(capcap))

        # big gap inflates backbone, starves remainder.
        self.play(FadeOut(VGroup(capeq, capcap, rem_dir)), run_time=0.3)
        two = VGroup(
            Text("large spectral gap  →  inflates the backbone term",
                 font_size=25, color=BACK),
            Text("large spectral gap  →  starves the remainder",
                 font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.4).next_to(split, DOWN, buff=0.7)
        self.play_beat(FadeIn(two[0], shift=RIGHT * 0.2), FadeIn(two[1], shift=RIGHT * 0.2))

        # keep the remainder in view: where the contrast will live.
        self.play(FadeOut(VGroup(intro, split, two)), run_time=0.4)
        keep = VGroup(
            Text("Keep the remainder in view.", font_size=30, color=WHITE),
            Text("Small in the average — but later, exactly where\n"
                 "the symptom contrast will turn out to live.",
                 font_size=26, color=RES, line_spacing=0.95),
        ).arrange(DOWN, buff=0.45)
        self.play_beat(FadeIn(keep[0], shift=UP * 0.15), FadeIn(keep[1]))


# ----------------------------------------------------------------------
# S5 — Numeric: lambda = (4.0, 0.3, 0.1).
# ----------------------------------------------------------------------
class S5_Numeric(NarratedScene):
    scene_key = "S5_Numeric"

    def construct(self):
        self.header("Numeric check:  lambda = (4.0, 0.3, 0.1)")

        # the spectrum.
        lam = MathTex(r"\lambda_1 = 4.0", r",\quad", r"\lambda_2 = 0.3",
                      r",\quad", r"\lambda_3 = 0.1").scale(1.0).shift(UP * 2.0)
        lam[0].set_color(EIG); lam[2].set_color(EIG); lam[4].set_color(EIG)
        self.play_beat(Write(lam))

        # equal overlaps c_j = 1 so the lesion is not stacking the deck.
        cvec = MathTex("c_1 = c_2 = c_3 = 1").scale(1.0).next_to(lam, DOWN, buff=0.5)
        cvec.set_color(VAR)
        ccap = Text("equal overlaps — the lesion does not stack the deck",
                    font_size=23, color=DIM).next_to(cvec, DOWN, buff=0.3)
        self.play_beat(Write(cvec), FadeIn(ccap))

        # the three coefficients lambda_j c_j.
        self.play(FadeOut(ccap), run_time=0.3)
        coeffs = MathTex(r"\lambda_1 c_1 = 4.0", r",\quad",
                         r"\lambda_2 c_2 = 0.3", r",\quad",
                         r"\lambda_3 c_3 = 0.1").scale(0.95)\
            .next_to(cvec, DOWN, buff=0.7)
        coeffs[0].set_color(BACK); coeffs[2].set_color(DIM); coeffs[4].set_color(DIM)
        self.play_beat(Write(coeffs))

        # the backbone coefficient dwarfs the rest.
        cmp = Text("4.0   ≫   0.3,  0.1\nthe backbone coefficient dwarfs the rest",
                   font_size=27, color=RES, line_spacing=0.95)\
            .next_to(coeffs, DOWN, buff=0.6)
        self.play_beat(FadeIn(cmp))

        # plug into cos^2.
        self.play(FadeOut(VGroup(cmp, coeffs)), run_time=0.3)
        comp = MathTex(r"\cos^2\angle(m,u_1)", "=",
                       r"\frac{4.0^2}{4.0^2 + 0.3^2 + 0.1^2}", "=",
                       r"\frac{16}{16.10}", r"\approx", "0.994")\
            .scale(0.85).next_to(cvec, DOWN, buff=0.8)
        comp[0].set_color(RES); comp[6].set_color(RES)
        self.play_beat(Write(comp))

        # the resulting angle.
        self.play(FadeOut(VGroup(lam, cvec, comp)), run_time=0.4)
        ang = VGroup(
            Text("≈ 99.4% of the map's energy is along the backbone",
                 font_size=28, color=RES),
            MathTex(r"\angle(m,\, u_1)\ \approx\ 4.5^\circ").scale(1.1).set_color(BACK),
            Text("the gap 0.3 / 4.0 did the work — exactly as the bound predicts",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.45)
        self.play_beat(FadeIn(ang[0]), Write(ang[1]), FadeIn(ang[2]))


# ----------------------------------------------------------------------
# S6 — Takeaway and the careful caveat.
# ----------------------------------------------------------------------
class S6_Takeaway(NarratedScene):
    scene_key = "S6_Takeaway"

    def construct(self):
        self.header("Takeaway")

        # what we showed.
        shown = MathTex(r"\frac{\lambda_2}{\lambda_1}\ \text{small}",
                        r"\ \Longrightarrow\ ",
                        r"m \parallel u_1").scale(1.2).shift(UP * 2.0)
        shown[0].set_color(EIG); shown[2].set_color(BACK)
        self.play_beat(Write(shown))

        # it's geometry: direction owned by the eigenvalues of C.
        geom = Text('"The geometry — which direction the map ends up pointing —\n'
                    'is owned by the eigenvalues lambda_j, a property of C alone."',
                    font_size=24, color=DIM, line_spacing=0.95).next_to(shown, DOWN, buff=0.6)
        self.play_beat(FadeIn(geom))

        # why average maps look alike.
        self.play(FadeOut(geom), run_time=0.3)
        alike = Text("addiction average · depression average · random seeds\n"
                     "all share u_1 — and u_1 is doing the talking",
                     font_size=25, color=BACK, line_spacing=0.95).next_to(shown, DOWN, buff=0.6)
        self.play_beat(FadeIn(alike))

        # the careful caveat: direction, not signal.
        self.play(FadeOut(VGroup(shown, alike)), run_time=0.4)
        caveat = VGroup(
            Text("We pinned down the map's DIRECTION —", font_size=29, color=WHITE),
            Text("not whether a symptom CONTRAST carries signal.",
                 font_size=29, color=RES),
        ).arrange(DOWN, buff=0.4).shift(UP * 0.8)
        self.play_beat(FadeIn(caveat[0], shift=UP * 0.15), FadeIn(caveat[1], shift=UP * 0.15))

        # balanced framing: not a debunk.
        balanced = Text("Convergence toward u_1 is a fact about the spectrum of C.\n"
                        "It explains the look of the average — it does NOT,\n"
                        "on its own, debunk lesion network mapping.",
                        font_size=24, color=DIM, line_spacing=0.95)\
            .next_to(caveat, DOWN, buff=0.6)
        self.play_beat(FadeIn(balanced))

        # the hand-off to the contrast.
        self.play(FadeOut(VGroup(caveat, balanced)), run_time=0.4)
        nxt = VGroup(
            Text("The backbone is geometry, not a verdict.",
                 font_size=30, color=RES),
            Text("Next: the contrast — what survives once this term cancels.",
                 font_size=26, color=VAR),
        ).arrange(DOWN, buff=0.5)
        self.play_beat(FadeIn(nxt[0], shift=UP * 0.15), FadeIn(nxt[1]))
