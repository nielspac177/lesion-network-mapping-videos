"""c0901_first_order_disconnection — "First-order disconnection only".

Five narrated scenes stating P3's biological-limitations charge (Pini, Salvalaggio
& Corbetta, Nat Neurosci Comment, 2026) at its strongest. The linear model
m = C l models the brain as a static, linear connectome; it captures only
first-order (direct, one-hop) disconnection; it cannot represent dynamics,
plasticity, higher-order interaction, or nonlinearity; this is a ceiling on the
MODEL CLASS, independent of the group-average critique (P1); and even a perfect
contrast inherits the limits of a static linear C. The chapter sets up the
empirical ceiling quantified in c0902.

All claims/numbers are page-cited in:
  responses/lnm_critique/sections/07_biological_limits.md
  responses/lnm_critique/papers/P3_biolimits.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0901_first_order_disconnection ./render.sh \
      chapters/c0901_first_order_disconnection/scenes.py -q ql \
      S1_Model S2_FirstOrder S3_Missing S4_Scope S5_Bridge
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — what the linear model assumes:  m = C l
# ----------------------------------------------------------------------
class S1_Model(NarratedScene):
    scene_key = "S1_Model"

    def construct(self):
        self.header("What the linear model assumes")

        intro = Text("the brain modeled as a static, linear connectome",
                     font_size=28, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                       # beat 1

        # the model:  m = C l
        eq = MathTex("m", "=", "C", r"\ell").scale(1.8).shift(UP * 0.7)
        eq[0].set_color(VAR)        # m  — the map
        eq[2].set_color(WHITE)      # C  — the connectome
        eq[3].set_color(VAR)        # l  — the lesion
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4))          # beat 2

        # annotate C (fixed)
        brace_C = Brace(eq[2], DOWN, color=WHITE)
        c_lab = Text("fixed normative connectome\nregion-by-region, same for every patient",
                     font_size=22, color=WHITE, line_spacing=0.8)\
            .next_to(brace_C, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_C), FadeIn(c_lab))             # beat 3

        # annotate l (lesion)
        self.play(FadeOut(VGroup(brace_C, c_lab)), run_time=0.4)
        brace_l = Brace(eq[3], DOWN, color=VAR)
        l_lab = Text("the lesion vector:  1 where the injury sits,\n0 everywhere else",
                     font_size=22, color=VAR, line_spacing=0.8)\
            .next_to(brace_l, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_l), FadeIn(l_lab))             # beat 4

        # annotate m (the product / the map)
        self.play(FadeOut(VGroup(brace_l, l_lab)), run_time=0.4)
        brace_m = Brace(eq[0], UP, color=VAR)
        m_lab = Text("the map: for each region, how strongly the\nlesion connects to it through C",
                     font_size=22, color=VAR, line_spacing=0.8)\
            .next_to(brace_m, UP, buff=0.2)
        self.play_beat(GrowFromCenter(brace_m), FadeIn(m_lab))             # beat 5

        # what linearity buys
        self.play(FadeOut(VGroup(brace_m, m_lab, intro)), run_time=0.4)
        buys = VGroup(
            Text("✓ fast", font_size=26, color=BACK),
            Text("✓ transparent", font_size=26, color=BACK),
            Text("✓ one matrix multiply → whole-brain fingerprint",
                 font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(buys, lag_ratio=0.3))                        # beat 6

        # what we already committed to
        self.play(FadeOut(buys), run_time=0.4)
        commit = VGroup(
            Text("but already committed to:", font_size=26, color=DIM),
            Text("C is frozen     C is shared     one product, no more",
                 font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3).next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(commit[0]), FadeIn(commit[1], shift=UP * 0.2))  # beat 7


# ----------------------------------------------------------------------
# Scene 2 — only direct disconnection (one-hop picture)
# ----------------------------------------------------------------------
class S2_FirstOrder(NarratedScene):
    scene_key = "S2_FirstOrder"

    def construct(self):
        self.header("Only direct disconnection")

        eq = MathTex("m", "=", "C", r"\ell").scale(1.1).to_edge(UP, buff=1.0)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        self.add(eq)

        head = Text("C l captures first-order disconnection — and only that",
                    font_size=27, color=WHITE).shift(UP * 2.0)
        self.play_beat(FadeIn(head))                                       # beat 1

        defn = Text("first-order = direct: regions that lose input\nbecause they were wired straight to the lesion",
                    font_size=24, color=DIM, line_spacing=0.8).next_to(head, DOWN, buff=0.35)
        self.play_beat(FadeIn(defn))                                       # beat 2

        # one-hop picture: lesion source -> direct neighbors
        self.play(FadeOut(VGroup(head, defn)), run_time=0.4)
        lesion = Dot(point=LEFT * 4.0 + DOWN * 0.3, radius=0.22, color=BAD)
        lesion_lab = Text("lesion  l", font_size=22, color=BAD)\
            .next_to(lesion, DOWN, buff=0.2)
        self.play_beat(FadeIn(lesion, scale=0.5), FadeIn(lesion_lab))      # beat 3

        # direct neighbors one hop out
        neigh_pts = [RIGHT * 0.2 + UP * 1.4, RIGHT * 0.8 + UP * 0.1,
                     RIGHT * 0.2 + DOWN * 1.4]
        neighbors = VGroup(*[Dot(p, radius=0.16, color=VAR) for p in neigh_pts])
        edges = VGroup(*[
            Line(lesion.get_center(), d.get_center(), color=DIM, stroke_width=3)
            for d in neighbors
        ])
        hop_lab = Text("direct neighbors — one hop away", font_size=22, color=VAR)\
            .to_edge(DOWN, buff=0.9)
        self.play_beat(Create(edges, lag_ratio=0.2),
                       FadeIn(neighbors, lag_ratio=0.2), FadeIn(hop_lab))   # beat 4

        # weighted by C; this is P3 axis 1
        weight = Text("each edge weighted by its strength in C",
                      font_size=23, color=WHITE).next_to(hop_lab, UP, buff=0.4)
        axis1 = Text("P3, axis 1:  strength of DIRECT disconnection",
                     font_size=24, color=BACK).shift(UP * 1.9)
        self.play_beat(FadeIn(weight), FadeIn(axis1))                      # beat 5

        # the only axis LNM captures
        only = Text("the only axis LNM captures  (P3 p.2)",
                    font_size=26, color=RES).next_to(axis1, DOWN, buff=0.3)
        self.play_beat(FadeIn(only, shift=UP * 0.2))                       # beat 6

        # everything beyond one hop is unseen
        unseen_pts = [RIGHT * 3.3 + UP * 1.2, RIGHT * 4.0 + DOWN * 0.3,
                      RIGHT * 3.3 + DOWN * 1.5]
        unseen = VGroup(*[
            DashedVMobject(Circle(radius=0.16, color=DIM, stroke_width=2).move_to(p))
            for p in unseen_pts
        ])
        unseen_lab = Text("beyond one hop:  not seen", font_size=22, color=DIM)\
            .next_to(unseen, DOWN, buff=0.2)
        self.play_beat(FadeIn(unseen, lag_ratio=0.2), FadeIn(unseen_lab))   # beat 7


# ----------------------------------------------------------------------
# Scene 3 — what it cannot represent (four omissions)
# ----------------------------------------------------------------------
class S3_Missing(NarratedScene):
    scene_key = "S3_Missing"

    def construct(self):
        self.header("What it cannot represent")

        head = Text("four omissions of a static, linear C — each one biological",
                    font_size=27, color=DIM).shift(UP * 2.7)
        self.play_beat(FadeIn(head))                                       # beat 1

        # build four rows; reveal one per beat
        rows = VGroup(
            self._row("✗ no dynamics",
                      "C is one snapshot — cannot represent network states evolving in time"),
            self._row("✗ no plasticity",
                      "the brain rewires, sprouts, remaps — a frozen C cannot model recovery"),
            self._row("✗ no higher-order interaction",
                      "effects ripple through regions never directly touched — C stops at one hop"),
            self._row("✗ no nonlinearity",
                      "not a proportional loss — networks swing hyper- vs hypoconnected"),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).shift(DOWN * 0.2)

        self.play_beat(FadeIn(rows[0], shift=RIGHT * 0.2))                 # beat 2
        self.play_beat(FadeIn(rows[1], shift=RIGHT * 0.2))                 # beat 3
        self.play_beat(FadeIn(rows[2], shift=RIGHT * 0.2))                 # beat 4
        self.play_beat(FadeIn(rows[3], shift=RIGHT * 0.2))                 # beat 5

        # P3 verbatim on hyper/hypo/transitioning
        self.play(FadeOut(VGroup(head, rows)), run_time=0.5)
        quote = Text("\"...lacks the capacity to distinguish between networks\nthat are hyperconnected, hypoconnected or\ndynamically transitioning\"   (P3 p.2)",
                     font_size=25, color=WHITE, line_spacing=0.85).shift(UP * 0.7)
        self.play_beat(FadeIn(quote))                                      # beat 6

        moral = VGroup(
            Text("time   ·   compensation   ·   cascades", font_size=28, color=RES),
            Text("a static linear map cannot express any of them",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3).next_to(quote, DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7

    def _row(self, title, body):
        t = Text(title, font_size=26, color=BAD)
        b = Text(body, font_size=21, color=WHITE)
        return VGroup(t, b).arrange(DOWN, buff=0.12, aligned_edge=LEFT)


# ----------------------------------------------------------------------
# Scene 4 — a model-class limit (independent of the group-average critique)
# ----------------------------------------------------------------------
class S4_Scope(NarratedScene):
    scene_key = "S4_Scope"

    def construct(self):
        self.header("A model-class limit")

        head = Text("this is NOT the group-average critique",
                    font_size=28, color=RES).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                       # beat 1

        # the earlier charge (P1)
        earlier = VGroup(
            Text("earlier charge (P1):", font_size=25, color=DIM),
            MathTex(r"\textstyle\sum_s M_s", r"\;\longrightarrow\;",
                    r"\deg(C)").scale(1.0),
            Text("averaging the per-lesion maps M over seeds s →\nthe degree (row-sum) of C, under uniform, non-overlapping sampling",
                 font_size=21, color=DIM, line_spacing=0.8),
        ).arrange(DOWN, buff=0.22)
        earlier[1][0].set_color(VAR); earlier[1][2].set_color(BAD)
        earlier.shift(UP * 1.0)
        self.play_beat(FadeIn(earlier, lag_ratio=0.2))                    # beat 2

        # this charge: a ceiling on the whole family
        self.play(FadeOut(VGroup(head, earlier)), run_time=0.5)
        fam = VGroup(
            Text("this charge:  a ceiling on the whole family",
                 font_size=27, color=WHITE),
            MathTex("m", "=", "C", r"\ell").scale(1.4),
            Text("every static, linear map", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.0)
        fam[1][0].set_color(VAR); fam[1][2].set_color(WHITE); fam[1][3].set_color(VAR)
        self.play_beat(FadeIn(fam, lag_ratio=0.2))                        # beat 3

        # holds for any C, any readout
        anyc = Text("holds for any C, and any readout — average OR contrast",
                    font_size=25, color=BACK).next_to(fam, DOWN, buff=0.6)
        self.play_beat(FadeIn(anyc))                                      # beat 4

        # even a perfect contrast
        self.play(FadeOut(VGroup(fam, anyc)), run_time=0.5)
        perfect = VGroup(
            Text("even a PERFECT symptom contrast", font_size=27, color=RES),
            Text("(one that cancels the backbone exactly)", font_size=23, color=DIM),
            Text("still lives inside this family", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.1)
        self.play_beat(FadeIn(perfect, lag_ratio=0.2))                    # beat 5

        # it inherits the limits
        inherit = Text("it inherits the limits of a static linear C",
                       font_size=26, color=BAD).next_to(perfect, DOWN, buff=0.5)
        reason = Text("no operation on C recovers a dimension C never contained",
                      font_size=23, color=WHITE).next_to(inherit, DOWN, buff=0.3)
        self.play_beat(FadeIn(inherit), FadeIn(reason, shift=UP * 0.2))    # beat 6

        # cannot residualize/reweight/contrast your way in
        self.play(FadeOut(VGroup(perfect, inherit, reason)), run_time=0.5)
        cannot = VGroup(
            Text("you cannot residualize,", font_size=27, color=DIM),
            Text("reweight, or contrast", font_size=27, color=DIM),
            Text("your way into time, plasticity, or higher-order cascades",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.25)
        self.play_beat(FadeIn(cannot, lag_ratio=0.25))                    # beat 7


# ----------------------------------------------------------------------
# Scene 5 — bridge to the ceiling (sets up c0902, P3's numbers)
# ----------------------------------------------------------------------
class S5_Bridge(NarratedScene):
    scene_key = "S5_Bridge"

    def construct(self):
        self.header("Bridge to the ceiling")

        q = Text("How much does the model class actually bound prediction?",
                 font_size=28, color=WHITE).shift(UP * 2.3)
        self.play_beat(FadeIn(q))                                         # beat 1

        link = Text("a ceiling on what a model can REPRESENT matters\nonly if it caps what it can PREDICT",
                    font_size=25, color=DIM, line_spacing=0.85)\
            .next_to(q, DOWN, buff=0.5)
        self.play_beat(FadeIn(link))                                      # beat 2

        # P3's benchmark
        self.play(FadeOut(VGroup(q, link)), run_time=0.5)
        cohort = MathTex(r"n = 132", r"\ \text{first-stroke patients}").scale(1.0)
        cohort[0].set_color(VAR)
        cohort.shift(UP * 1.6)
        cohort_cap = Text("P3's sobering benchmark  (P3 p.1)",
                          font_size=23, color=DIM).next_to(cohort, DOWN, buff=0.25)
        self.play_beat(Write(cohort), FadeIn(cohort_cap))                 # beat 3

        # R^2 = 0.01 - 0.18
        r2 = MathTex(r"R^2", "=", "0.01", r"\;-\;", "0.18").scale(1.3)\
            .next_to(cohort_cap, DOWN, buff=0.7)
        r2[0].set_color(VAR); r2[2].set_color(BAD); r2[4].set_color(BAD)
        r2_cap = Text("explained variance of behavior, across cognitive domains",
                      font_size=22, color=DIM).next_to(r2, DOWN, buff=0.25)
        self.play_beat(Write(r2), FadeIn(r2_cap))                         # beat 4

        # the tell: anatomical refinement did not help
        self.play(FadeOut(VGroup(cohort, cohort_cap, r2, r2_cap)), run_time=0.5)
        tell = VGroup(
            Text("the tell:", font_size=26, color=RES),
            Text("refining the anatomy — restricting to cleaner voxels —",
                 font_size=24, color=WHITE),
            Text("did NOT improve prediction  (P3 p.1)", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.9)
        self.play_beat(FadeIn(tell, lag_ratio=0.2))                       # beat 5

        intrinsic = Text("if cleaning the anatomy does not help,\nthe ceiling is intrinsic to the model class — not noise",
                         font_size=25, color=RES, line_spacing=0.85)\
            .next_to(tell, DOWN, buff=0.55)
        self.play_beat(FadeIn(intrinsic, shift=UP * 0.2))                 # beat 6

        # hand-off to c0902
        self.play(FadeOut(VGroup(tell, intrinsic)), run_time=0.5)
        nxt = VGroup(
            Text("Those numbers — and what they bound —", font_size=27, color=WHITE),
            Text("are the next chapter.", font_size=27, color=WHITE),
            Text("Here we fixed only the ceiling's foundation.", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(nxt, lag_ratio=0.3))                        # beat 7
