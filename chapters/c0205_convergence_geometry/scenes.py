"""c0205_convergence_geometry — "Why convergence is not validation".

Part 2 / R1 of the LNM series. Source: sections/02_what_is_entailed.md.

The geometry of convergence. Every seed's map points near the backbone u_1 (the
cos^2 alignment bound). Pictured as a funnel: a cone around u_1 that almost all
maps fall into. A shared endpoint therefore certifies the funnel (the connectome
spectrum), not the lesion and not the disease. That is exactly the gap the
critique exploits for AVERAGE maps -- and exactly why a CONTRAST recovers signal,
because the backbone term cancels from Delta = m+ - m-. We present both sides:
the cancellation is exact only in expectation, and residual leakage is real.
Bridge: the question becomes which null you test, setting up Parts 4 and 5.

Balanced framing (non-negotiable): convergence is a property of C's spectrum, not
a verdict on the method. We do not debunk LNM; we localize where signal can live.

All math and numbers come from sections/02_what_is_entailed.md:
  C = sum_j lambda_j u_j u_j^T,  lambda_1 >= lambda_2 >= ... >= 0
  m_i = C ell_i = sum_j lambda_j (u_j^T ell_i) u_j
  cos^2 angle(m, u_1) = lambda_1^2 c_1^2 / sum_j lambda_j^2 c_j^2  -> 1 as gap->0
  Delta = m+ - m- = sum_j lambda_j (c_j+ - c_j-) u_j
  worked check: lambda_1=10, lambda_2=1; (c1+,c2+)=(2.0,0.5), (c1-,c2-)=(2.0,-0.5)
    m+ = 20 u_1 + 0.5 u_2,  m- = 20 u_1 - 0.5 u_2,  Delta = 1.0 u_2
    each average ~99.9% backbone; contrast 100% u_2.

Render:
  MEDIA=$HOME/lnm_media/c0205_convergence_geometry ./render.sh \
      chapters/c0205_convergence_geometry/scenes.py -q ql \
      S1_Restate S2_Funnel S3_Certifies S4_ContrastVsAverage S5_Bridge
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# S1 — Restate: every seed's map points near the backbone u_1.
# ----------------------------------------------------------------------
class S1_Restate(NarratedScene):
    scene_key = "S1_Restate"

    def construct(self):
        self.header("Restated: every seed's map points near  u₁")

        # spectral decomposition of C
        spec = MathTex("C", "=", r"\sum_j", r"\lambda_j", "u_j", "u_j^{\\top}").scale(1.3)\
            .shift(UP * 2.2)
        spec[0].set_color(WHITE)
        spec[3].set_color(EIG)
        spec[4].set_color(BACK)
        spec[5].set_color(BACK)
        self.play_beat(Write(spec))

        # decode lambda_j and u_j
        br_u = Brace(spec[4], DOWN, color=DIM)
        u_lab = br_u.get_text("eigenvectors: the brain-wide patterns").scale(0.62)
        u_lab.set_color(BACK)
        br_l = Brace(spec[3], UP, color=DIM)
        l_lab = br_l.get_tex(r"\text{eigenvalues:}\ \ \lambda_1 \ge \lambda_2 \ge \cdots \ge 0").scale(0.62)
        l_lab.set_color(EIG)
        self.play_beat(GrowFromCenter(br_u), FadeIn(u_lab),
                       GrowFromCenter(br_l), FadeIn(l_lab))

        # the seed map as a weighted sum of patterns
        self.play(FadeOut(VGroup(br_u, u_lab, br_l, l_lab)), run_time=0.35)
        mp = MathTex("m", "=", "C", r"\ell", "=", r"\sum_j", r"\lambda_j",
                     r"(u_j^{\top}\ell)", "u_j").scale(1.1).next_to(spec, DOWN, buff=1.0)
        mp[0].set_color(VAR)
        mp[3].set_color(VAR)
        mp[6].set_color(EIG)
        mp[7].set_color(VAR)
        mp[8].set_color(BACK)
        self.play_beat(Write(mp))

        # the loading u_j^T ell is the only place the lesion enters
        br_c = Brace(mp[7], DOWN, color=DIM)
        c_lab = br_c.get_text("loading: how much of pattern j the lesion marks").scale(0.6)
        c_lab.set_color(VAR)
        only = Text("the only place the lesion gets a vote", font_size=22, color=VAR)\
            .next_to(c_lab, DOWN, buff=0.25)
        self.play_beat(GrowFromCenter(br_c), FadeIn(c_lab), FadeIn(only))

        # the cos^2 alignment bound
        self.play(FadeOut(VGroup(spec, mp, br_c, c_lab, only)), run_time=0.4)
        cos = MathTex(r"\cos^2\angle(m, u_1)", "=",
                      r"\frac{\lambda_1^2\, c_1^2}{\sum_j \lambda_j^2\, c_j^2}")\
            .scale(1.3).shift(UP * 1.4)
        cos[0].set_color(VAR)
        cos[2].set_color(WHITE)
        angcap = Text("the squared cosine of the angle between the map and the backbone u₁",
                      font_size=22, color=DIM).next_to(cos, DOWN, buff=0.45)
        self.play_beat(Write(cos), FadeIn(angcap))

        # the spectral gap is the lever
        self.play(FadeOut(angcap), run_time=0.3)
        gap = MathTex(r"\frac{\lambda_2}{\lambda_1}", r"\;\to\; 0",
                      r"\quad\Longrightarrow\quad", r"\cos^2\angle(m,u_1)", r"\;\to\; 1")\
            .scale(1.0).next_to(cos, DOWN, buff=0.7)
        gap[0].set_color(EIG)
        gap[3].set_color(VAR)
        gap[4].set_color(RES)
        gapcap = Text("the spectral gap is the lever: λ₁ swamps the rest",
                      font_size=23, color=EIG).next_to(gap, DOWN, buff=0.35)
        self.play_beat(Write(gap), FadeIn(gapcap))

        # the moral
        self.play(FadeOut(VGroup(cos, gap, gapcap)), run_time=0.4)
        moral = VGroup(
            Text("Every seed's map points very nearly along u₁.", font_size=30, color=BACK),
            Text("Not because the lesions agree —", font_size=26, color=DIM),
            Text("because λ₁ was always going to win the tug-of-war.", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(LaggedStart(*[FadeIn(m, shift=UP * 0.15) for m in moral],
                                   lag_ratio=0.4))


# ----------------------------------------------------------------------
# S2 — The funnel: a cone around u_1 that almost all maps fall into.
# ----------------------------------------------------------------------
class S2_Funnel(NarratedScene):
    scene_key = "S2_Funnel"

    def _cone(self, apex, direction, half_angle, length, color):
        """Return a VGroup: two edges of a 2-D cone (the funnel walls)."""
        d = direction / np.linalg.norm(direction)
        # rotate d by +/- half_angle in the plane
        ca, sa = np.cos(half_angle), np.sin(half_angle)
        e1 = np.array([ca * d[0] - sa * d[1], sa * d[0] + ca * d[1], 0.0])
        e2 = np.array([ca * d[0] + sa * d[1], -sa * d[0] + ca * d[1], 0.0])
        l1 = Line(apex, apex + e1 * length, color=color)
        l2 = Line(apex, apex + e2 * length, color=color)
        return VGroup(l1, l2)

    def construct(self):
        self.header("The funnel")

        apex = LEFT * 4.5 + DOWN * 0.3
        axis = np.array([1.0, 0.25, 0.0])
        axis = axis / np.linalg.norm(axis)

        # the backbone direction u_1
        u1 = Arrow(apex, apex + axis * 6.5, color=BACK, buff=0, stroke_width=6)
        u1_lab = MathTex("u_1", color=BACK).scale(1.1).next_to(u1.get_end(), RIGHT, buff=0.2)
        backcap = Text("the backbone: one fixed direction in map space",
                       font_size=22, color=BACK).to_edge(DOWN, buff=0.5)
        self.play_beat(GrowArrow(u1), Write(u1_lab), FadeIn(backcap))

        # the cone, walls = spectral gap
        cone = self._cone(apex, axis, 0.32, 6.7, DIM)
        gapcap = MathTex(r"\text{cone half-angle} \sim \lambda_2/\lambda_1",
                         color=EIG).scale(0.75).to_edge(DOWN, buff=0.5)
        self.play(FadeOut(backcap), run_time=0.3)
        self.play_beat(Create(cone[0]), Create(cone[1]), FadeIn(gapcap))

        # fire seeds from different mouths, different directions
        self.play(FadeOut(gapcap), run_time=0.3)
        np.random.seed(7)
        starts = [apex + UP * 2.6 + LEFT * 0.2,
                  apex + DOWN * 2.4 + RIGHT * 0.3,
                  apex + UP * 1.4 + RIGHT * 1.2,
                  apex + DOWN * 1.6 + RIGHT * 1.0]
        raw_dirs = [np.array([1.0, 1.4, 0]), np.array([1.0, -1.5, 0]),
                    np.array([1.0, 0.9, 0]), np.array([1.0, -0.8, 0])]
        seeds = VGroup(*[Dot(s, color=VAR, radius=0.07) for s in starts])
        rays = VGroup(*[Arrow(s, s + d / np.linalg.norm(d) * 1.6,
                              color=VAR, buff=0, stroke_width=3)
                        for s, d in zip(starts, raw_dirs)])
        seedcap = Text("seeds from anywhere — different voxels, different directions",
                       font_size=22, color=VAR).to_edge(DOWN, buff=0.5)
        self.play_beat(LaggedStart(*[FadeIn(s) for s in seeds], lag_ratio=0.2),
                       LaggedStart(*[GrowArrow(r) for r in rays], lag_ratio=0.2),
                       FadeIn(seedcap))

        # but each map is pulled into the cone -> lands near u_1
        self.play(FadeOut(seedcap), run_time=0.3)
        targets = [apex + axis * (3.0 + 0.7 * k) + np.array([0, 0.0, 0])
                   for k in range(4)]
        pulled = VGroup(*[Arrow(s, t, color=RES, buff=0, stroke_width=4)
                          for s, t in zip(starts, targets)])
        landings = VGroup(*[Dot(t, color=RES, radius=0.06) for t in targets])
        pullcap = Text("λ₁ is so heavy: almost every map falls inside the cone",
                       font_size=22, color=RES).to_edge(DOWN, buff=0.5)
        self.play_beat(LaggedStart(*[GrowArrow(p) for p in pulled], lag_ratio=0.25),
                       LaggedStart(*[FadeIn(l) for l in landings], lag_ratio=0.25),
                       FadeIn(pullcap), FadeOut(rays))

        # name it: the funnel, one outlet
        self.play(FadeOut(pullcap), run_time=0.3)
        funnelcap = VGroup(
            Text("different mouths → one outlet:  u₁", font_size=26, color=BACK),
        ).to_edge(DOWN, buff=0.5)
        self.play_beat(FadeIn(funnelcap, shift=UP * 0.15),
                       cone[0].animate.set_color(BACK),
                       cone[1].animate.set_color(BACK))

        # the funnel was shaped before any patient arrived
        self.play(FadeOut(funnelcap), run_time=0.3)
        priorcap = VGroup(
            Text("The funnel's walls are the eigenvalues of C.", font_size=25, color=EIG),
            Text("Shaped before any patient arrived —", font_size=24, color=DIM),
            Text("they know nothing about lesions, symptoms, or disease.", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.45)
        self.play_beat(LaggedStart(*[FadeIn(p) for p in priorcap], lag_ratio=0.3))

        # so convergence is real; the question is what it certifies
        self.play(FadeOut(VGroup(u1, u1_lab, cone, seeds, pulled, landings,
                                 priorcap)), run_time=0.5)
        q = VGroup(
            Text("Convergence here is real — exactly what the critique observed.",
                 font_size=28, color=WHITE),
            Text("What can a shared endpoint certify, and what can it not?",
                 font_size=28, color=RES),
        ).arrange(DOWN, buff=0.45)
        self.play_beat(FadeIn(q[0]), FadeIn(q[1], shift=UP * 0.15))


# ----------------------------------------------------------------------
# S3 — A shared endpoint certifies the funnel, not the lesion or the disease.
# ----------------------------------------------------------------------
class S3_Certifies(NarratedScene):
    scene_key = "S3_Certifies"

    def construct(self):
        self.header("A shared endpoint certifies the funnel — not the disease")

        # three inputs converge to ~ u_1
        inputs = VGroup(
            Text("addiction cohort", font_size=24, color=VAR),
            Text("depression cohort", font_size=24, color=VAR),
            Text("random lesions", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.7).shift(LEFT * 4.2 + UP * 0.3)
        endpoint = Dot(RIGHT * 2.6 + UP * 0.3, color=BACK, radius=0.12)
        end_lab = MathTex(r"\approx u_1", color=BACK).scale(1.0).next_to(endpoint, RIGHT, buff=0.25)
        arrows = VGroup(*[Arrow(t.get_right(), endpoint.get_center(),
                                color=DIM, buff=0.25, stroke_width=3) for t in inputs])
        self.play_beat(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.2) for t in inputs],
                                   lag_ratio=0.25),
                       LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.25),
                       FadeIn(endpoint), Write(end_lab))

        # it proves the funnel exists
        proves = Text("Proven: the funnel exists — the geometry of C, its backbone u₁.",
                      font_size=24, color=BACK).to_edge(DOWN, buff=1.4)
        self.play_beat(FadeIn(proves, shift=UP * 0.15))

        # NOT the lesion
        self.play(FadeOut(proves), run_time=0.3)
        not_les = Text("NOT the lesion: the marked voxels were thrown away\n"
                       "the moment λ₁ dragged every map into the cone.",
                       font_size=24, color=BAD, line_spacing=0.9).to_edge(DOWN, buff=1.2)
        self.play_beat(FadeIn(not_les))

        # NOT the disease
        self.play(FadeOut(not_les), run_time=0.3)
        not_dis = Text("NOT the disease: all three converge for the same reason —\n"
                       "they share u₁, and u₁ is doing all the talking.",
                       font_size=24, color=BAD, line_spacing=0.9).to_edge(DOWN, buff=1.2)
        self.play_beat(FadeIn(not_dis))

        # the concession, made in full
        self.play(FadeOut(VGroup(inputs, arrows, endpoint, end_lab, not_dis)),
                  run_time=0.5)
        concede = VGroup(
            Text("Concede it cleanly, in full:", font_size=26, color=WHITE),
            Text("the one-sample average map is nonspecific.", font_size=30, color=RES),
            Text("Backbone-dominated, convergent across disorders,", font_size=23, color=DIM),
            Text("reproduced by random seeds. Denying this is denying arithmetic.",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(LaggedStart(*[FadeIn(c, shift=UP * 0.12) for c in concede],
                                   lag_ratio=0.3))

        # but: this is a claim about the AVERAGE, and only the average
        self.play(concede.animate.scale(0.7).to_edge(UP, buff=1.2), run_time=0.4)
        scope = MathTex(r"\bar m", r"\;=\;", r"\sum_j \lambda_j\, \bar c_j\, u_j",
                        r"\;\approx\; \lambda_1 \bar c_1\, u_1").scale(1.0).shift(DOWN * 0.3)
        scope[0].set_color(VAR)
        scope[3].set_color(BACK)
        scopecap = Text("a true statement about the average map — and only the average map",
                        font_size=23, color=WHITE).next_to(scope, DOWN, buff=0.45)
        self.play_beat(Write(scope), FadeIn(scopecap))

        # property of the spectrum, not a verdict
        self.play(FadeOut(VGroup(scope, scopecap)), run_time=0.35)
        verdict = VGroup(
            Text("A property of C's spectrum — not a verdict on the method.",
                 font_size=27, color=BACK),
            Text("A verdict would need a claim about a different object entirely.",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.4).shift(DOWN * 0.2)
        self.play_beat(FadeIn(verdict[0]), FadeIn(verdict[1], shift=UP * 0.15))


# ----------------------------------------------------------------------
# S4 — The gap: critique's leverage on AVERAGES; the CONTRAST recovers signal.
# ----------------------------------------------------------------------
class S4_ContrastVsAverage(NarratedScene):
    scene_key = "S4_ContrastVsAverage"

    def construct(self):
        self.header("The average loses it; the contrast keeps it")

        # split the cohort
        split = VGroup(
            Text("symptomatic seeds", font_size=26, color=BACK),
            Text("asymptomatic seeds", font_size=26, color=VAR),
        ).arrange(RIGHT, buff=1.6).shift(UP * 2.4)
        self.play_beat(FadeIn(split[0], shift=LEFT * 0.2),
                       FadeIn(split[1], shift=RIGHT * 0.2))

        # the two group averages, both dragged to u_1
        avgs = MathTex(r"\bar m^{+}", "=", r"\sum_j \lambda_j \bar c_j^{+} u_j",
                       r"\qquad", r"\bar m^{-}", "=", r"\sum_j \lambda_j \bar c_j^{-} u_j")\
            .scale(0.85).next_to(split, DOWN, buff=0.6)
        avgs[0].set_color(BACK)
        avgs[4].set_color(VAR)
        bothcap = Text("both dragged toward u₁ — both nonspecific. The critique is right about each.",
                       font_size=22, color=DIM).next_to(avgs, DOWN, buff=0.4)
        self.play_beat(Write(avgs), FadeIn(bothcap))

        # the contrast Delta
        self.play(FadeOut(VGroup(split, avgs, bothcap)), run_time=0.4)
        delta = MathTex(r"\Delta", "=", r"\bar m^{+}", "-", r"\bar m^{-}").scale(1.4)\
            .shift(UP * 2.2)
        delta[0].set_color(RES)
        delta[2].set_color(BACK)
        delta[4].set_color(VAR)
        dcap = Text("the symptom lives in the contrast, not in either average",
                    font_size=23, color=RES).next_to(delta, DOWN, buff=0.4)
        self.play_beat(Write(delta), FadeIn(dcap))

        # subtract component by component; leading term
        self.play(FadeOut(dcap), delta.animate.scale(0.7).to_edge(UP, buff=1.0),
                  run_time=0.4)
        expand = MathTex(r"\Delta", "=", r"\sum_j \lambda_j",
                         r"(\bar c_j^{+} - \bar c_j^{-})", "u_j").scale(1.05)\
            .shift(UP * 0.8)
        expand[0].set_color(RES)
        expand[2].set_color(EIG)
        expand[3].set_color(WHITE)
        expand[4].set_color(BACK)
        lead = MathTex(r"\text{leading term:}\ \ ", r"\lambda_1",
                       r"(\bar c_1^{+} - \bar c_1^{-})", "u_1").scale(0.95)\
            .next_to(expand, DOWN, buff=0.6)
        lead[1].set_color(EIG)
        lead[2].set_color(WHITE)
        lead[3].set_color(BACK)
        self.play_beat(Write(expand), Write(lead))

        # the backbone difference is near zero -> u_1 cancels
        br = Brace(lead[2], DOWN, color=DIM)
        brlab = br.get_tex(r"\text{groups load on hubs the same way}\ \rightarrow\ \approx 0").scale(0.6)
        brlab.set_color(BAD)
        cancel = MathTex(r"\Rightarrow\ \lambda_1(\bar c_1^{+}-\bar c_1^{-})\,u_1",
                         r"\ \to\ 0").scale(0.9).next_to(br, DOWN, buff=0.35)
        cancel[0].set_color(BAD)
        cancel[1].set_color(BAD)
        self.play_beat(GrowFromCenter(br), FadeIn(brlab), Write(cancel))

        # what survives: the higher components
        self.play(FadeOut(VGroup(delta, expand, lead, br, brlab, cancel)), run_time=0.45)
        survive = MathTex(r"\Delta", r"\;\approx\;", r"\sum_{j\ge 2}",
                          r"\lambda_j", r"(\bar c_j^{+}-\bar c_j^{-})", "u_j").scale(1.15)\
            .shift(UP * 1.6)
        survive[0].set_color(RES)
        survive[3].set_color(EIG)
        survive[5].set_color(BACK)
        survcap = Text("u₂, u₃, … weighted by genuine group differences —\n"
                       "the backbone that poisoned the average is cleansed from the contrast.",
                       font_size=22, color=BACK, line_spacing=0.9).next_to(survive, DOWN, buff=0.5)
        self.play_beat(Write(survive), FadeIn(survcap))

        # the worked check: numbers
        self.play(FadeOut(VGroup(survive, survcap)), run_time=0.4)
        nums = VGroup(
            MathTex(r"\lambda_1 = 10,\quad \lambda_2 = 1", color=EIG).scale(0.9),
            MathTex(r"(\bar c_1^{+},\bar c_2^{+}) = (2.0,\ +0.5)", color=BACK).scale(0.9),
            MathTex(r"(\bar c_1^{-},\bar c_2^{-}) = (2.0,\ -0.5)", color=VAR).scale(0.9),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.3)
        self.play_beat(LaggedStart(*[Write(n) for n in nums], lag_ratio=0.3))

        # averages ~99.9% backbone; contrast pure u_2
        self.play(nums.animate.scale(0.75).to_edge(UP, buff=1.1), run_time=0.4)
        result = VGroup(
            MathTex(r"\bar m^{+} = 20\,u_1 + 0.5\,u_2,\quad \bar m^{-} = 20\,u_1 - 0.5\,u_2").scale(0.85),
            Text("each average ≈ 99.9% backbone — nonspecific, as charged",
                 font_size=22, color=DIM),
            MathTex(r"\Delta = 0\cdot u_1 + 1.0\,u_2").scale(1.0),
            Text("the contrast is 100% u₂: the backbone has vanished",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.3)
        result[0].set_color(WHITE)
        result[2].set_color(RES)
        self.play_beat(LaggedStart(*[FadeIn(r, shift=UP * 0.12) for r in result],
                                   lag_ratio=0.3))

        # be fair: cancellation is exact only in expectation (the WARNING)
        self.play(FadeOut(VGroup(nums, result)), run_time=0.45)
        warn = VGroup(
            Text("Be fair in both directions:", font_size=26, color=WHITE),
            Text("the cancellation is exact only in expectation.", font_size=25, color=BAD),
            Text("If groups truly load on hubs differently — selection, lesion-size —",
                 font_size=23, color=DIM),
            Text("a residual u₁ term leaks through and can masquerade as signal.",
                 font_size=23, color=BAD),
        ).arrange(DOWN, buff=0.28)
        self.play_beat(LaggedStart(*[FadeIn(w, shift=UP * 0.1) for w in warn],
                                   lag_ratio=0.3))

        # the narrow, fair point
        self.play(FadeOut(warn), run_time=0.4)
        narrow = VGroup(
            Text("That residual is what the right null and backbone removal will kill.",
                 font_size=25, color=BACK),
            Text("The point here is narrow: the contrast is where signal CAN survive —",
                 font_size=25, color=WHITE),
            Text("and the critique never tested it.", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(LaggedStart(*[FadeIn(n, shift=UP * 0.12) for n in narrow],
                                   lag_ratio=0.35))


# ----------------------------------------------------------------------
# S5 — Bridge to specificity: which null you test. Sets up Parts 4 and 5.
# ----------------------------------------------------------------------
class S5_Bridge(NarratedScene):
    scene_key = "S5_Bridge"

    def construct(self):
        self.header("The question becomes: which null?")

        # not validation, not refutation -- geometry
        gist = VGroup(
            Text("Convergence toward u₁ is not validation —", font_size=28, color=WHITE),
            Text("and not refutation either.", font_size=28, color=WHITE),
            Text("It is geometry, and geometry handed us a sharper question.", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(LaggedStart(*[FadeIn(g, shift=UP * 0.12) for g in gist],
                                   lag_ratio=0.35))

        # the new question
        self.play(FadeOut(gist), run_time=0.4)
        old = Text("not  “is the average map specific?”  (conceded: it is not)",
                   font_size=26, color=DIM).shift(UP * 1.2)
        new = Text("but  “which null do you test the contrast against?”",
                   font_size=30, color=RES).next_to(old, DOWN, buff=0.6)
        self.play_beat(FadeIn(old), FadeIn(new, shift=UP * 0.15))

        # wrong null vs right null
        self.play(FadeOut(VGroup(old, new)), run_time=0.4)
        wrong = Text("Wrong null → the leaked backbone can fake a result.",
                     font_size=26, color=BAD).shift(UP * 1.6)
        right = VGroup(
            Text("Right null: shuffle the symptom labels,", font_size=26, color=BACK),
            Text("holding lesion geometry fixed — so u₁ cancels by construction.",
                 font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.25).next_to(wrong, DOWN, buff=0.7)
        self.play_beat(FadeIn(wrong, shift=UP * 0.1),
                       LaggedStart(*[FadeIn(r) for r in right], lag_ratio=0.3))

        # the exact guarantee
        self.play(FadeOut(VGroup(wrong, right)), run_time=0.4)
        guar = VGroup(
            Text("u₁ is label-independent.", font_size=28, color=BACK),
            Text("It appears identically in the observed and every permuted statistic —",
                 font_size=24, color=DIM),
            Text("so it cannot inflate a p-value. An exact guarantee.", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(LaggedStart(*[FadeIn(g, shift=UP * 0.12) for g in guar],
                                   lag_ratio=0.35))

        # Part 4
        self.play(FadeOut(guar), run_time=0.4)
        p4 = VGroup(
            Text("Part 4", font_size=32, color=RES),
            Text("builds that null — and asks which candidate null", font_size=25, color=WHITE),
            Text("actually targets the symptom hypothesis.", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(p4[0], scale=1.1),
                       FadeIn(p4[1]), FadeIn(p4[2]))

        # Part 5 + closing line
        self.play(p4.animate.scale(0.75).to_edge(UP, buff=1.2), run_time=0.4)
        p5 = VGroup(
            Text("Part 5", font_size=32, color=RES),
            Text("removes the residual backbone leakage explicitly,", font_size=25, color=WHITE),
            Text("so what is left in the contrast is symptom signal, not the cone.",
                 font_size=25, color=WHITE),
            Text("Convergence set the question; specificity will answer it.",
                 font_size=27, color=BACK),
        ).arrange(DOWN, buff=0.3).shift(DOWN * 0.3)
        self.play_beat(FadeIn(p5[0], scale=1.1),
                       LaggedStart(*[FadeIn(p, shift=UP * 0.1) for p in p5[1:]],
                                   lag_ratio=0.3))
