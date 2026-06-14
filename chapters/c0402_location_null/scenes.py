"""c0402_location_null — "The location null".

Five narrated scenes that state ONE of the two nulls precisely: the
random-lesion / location null. It asks "is THIS lesion location special
compared to an ensemble R of other locations?" We define the ensemble R,
the test statistic (backbone shape T), the permutation procedure, and
exactly what the null can and cannot answer. The symptom-label null is the
subject of Part 5; here we only set up the location question fairly.

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/03_the_right_null.md   (the location null)
  responses/lnm_critique/papers/P2_nullmodels.md          (the procedure)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0402_location_null ./render.sh \
      chapters/c0402_location_null/scenes.py -q ql \
      S1_Question S2_Ensemble S3_Statistic S4_Procedure S5_WhatItAsks
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — what the location null asks  (7 beats)
# ----------------------------------------------------------------------
class S1_Question(NarratedScene):
    scene_key = "S1_Question"

    def construct(self):
        title = Text("What the location null asks", font_size=40, color=WHITE)
        sub = Text("a null model is a question in disguise",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))            # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # the candidate
        cand = VGroup(
            Text("The first candidate:", font_size=26, color=DIM),
            Text("the random-lesion null", font_size=30, color=VAR),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.7)
        self.play_beat(FadeIn(cand, shift=UP * 0.2))                        # beat 2

        # the question it asks
        q = VGroup(
            Text("It asks one thing:", font_size=26, color=WHITE),
            Text("is THIS lesion location special", font_size=28, color=RES),
            Text("compared to other locations we could have drawn?",
                 font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.2).next_to(cand, DOWN, buff=0.5)
        self.play_beat(FadeIn(q, lag_ratio=0.3))                           # beat 3

        # define R
        self.play(FadeOut(VGroup(cand, q)), run_time=0.45)
        rdef = MathTex(r"\mathcal{R}", "=",
                       r"\text{ensemble of alternative lesion placements}")\
            .scale(0.95).shift(UP * 1.6)
        rdef[0].set_color(VAR)
        examples = VGroup(
            Text("random blobs", font_size=23, color=DIM),
            Text("synthetic seeds", font_size=23, color=DIM),
            Text("real lesions reshuffled to new spots", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).next_to(rdef, DOWN, buff=0.45)
        self.play_beat(Write(rdef), FadeIn(examples, lag_ratio=0.25))       # beat 4

        # type the hypothesis
        self.play(FadeOut(examples), rdef.animate.scale(0.85).to_edge(UP, buff=1.1),
                  run_time=0.5)
        h0 = MathTex(r"H_0^{\mathrm{loc}}", r":\;",
                     r"\ell_{\mathrm{obs}}", r"\ \overset{d}{=}\ ",
                     r"\ell \sim \mathcal{R}").scale(1.15).shift(UP * 0.6)
        h0[0].set_color(RES); h0[2].set_color(VAR); h0[4].set_color(VAR)
        h0cap = Text("the observed location is exchangeable with locations drawn from R",
                     font_size=23, color=DIM).next_to(h0, DOWN, buff=0.35)
        self.play_beat(Write(h0), FadeIn(h0cap))                           # beat 5

        # decode "exchangeable"
        exch = VGroup(
            Text("exchangeable = swappable", font_size=26, color=BACK),
            Text("under the null, your real placement is just one more draw",
                 font_size=24, color=WHITE),
            Text("no more special than the fakes", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.18).next_to(h0cap, DOWN, buff=0.5)
        self.play_beat(FadeIn(exch, lag_ratio=0.3))                        # beat 6

        # what rejection means
        self.play(FadeOut(VGroup(rdef, h0, h0cap, exch)), run_time=0.5)
        rej = VGroup(
            Text("Reject  H0-loc   means:", font_size=28, color=RES),
            Text("this location produces a more extreme map", font_size=26, color=WHITE),
            Text("than a typical location would.", font_size=26, color=WHITE),
            Text("That, and only that.", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.22)
        self.play_beat(FadeIn(rej, lag_ratio=0.25))                        # beat 7


# ----------------------------------------------------------------------
# Scene 2 — the reference ensemble R  (7 beats)
# ----------------------------------------------------------------------
class S2_Ensemble(NarratedScene):
    scene_key = "S2_Ensemble"

    def construct(self):
        self.header("The reference ensemble")

        intro = Text("draw the ensemble R itself: everything downstream compares against it",
                     font_size=25, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # cloud of fake placements
        brain = Circle(radius=1.5, color=DIM, stroke_width=2).shift(LEFT * 3.3 + DOWN * 0.3)
        brain_lab = Text("R", font_size=30, color=VAR).next_to(brain, UP, buff=0.15)
        import random as _r
        _r.seed(7)
        blobs = VGroup()
        for _ in range(9):
            a = _r.uniform(0, TAU); rr = _r.uniform(0.2, 1.15)
            d = Dot(point=brain.get_center() + np.array([rr * np.cos(a),
                    rr * np.sin(a), 0]), radius=0.09, color=BAD)
            blobs.add(d)
        cloud_cap = Text("fake placements:\nrandom, scattered,\nnon-overlapping",
                         font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(brain, DOWN, buff=0.35)
        self.play_beat(Create(brain), FadeIn(brain_lab),
                       FadeIn(blobs, lag_ratio=0.15), FadeIn(cloud_cap))   # beat 2

        # m_ell = C ell  (keep the subscript attached to its base m)
        eq = MathTex(r"m_{\ell}", "=", "C", r"\,\ell")\
            .scale(1.3).shift(RIGHT * 2.5 + UP * 1.2)
        eq[0].set_color(VAR); eq[2].set_color(WHITE); eq[3].set_color(VAR)
        eq_cap = Text("push each placement through LNM",
                      font_size=23, color=DIM).next_to(eq, UP, buff=0.3)
        self.play_beat(Write(eq), FadeIn(eq_cap))                          # beat 3

        # annotate C and ell
        bc = Brace(eq[2], DOWN, color=WHITE)
        cl = Text("fixed normative connectome", font_size=21, color=WHITE)\
            .next_to(bc, DOWN, buff=0.15)
        be = Brace(eq[3], DOWN, color=VAR)
        el = Text("marks the lesion's voxels", font_size=21, color=VAR)\
            .next_to(be, DOWN, buff=0.15).shift(RIGHT * 0.1)
        # stack the ell label below the C label to avoid overlap
        el.next_to(cl, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(bc), FadeIn(cl),
                       GrowFromCenter(be), FadeIn(el))                     # beat 4

        # real map + crowd of null maps
        self.play(FadeOut(VGroup(eq_cap, bc, cl, be, el, intro)), run_time=0.45)
        crowd = VGroup(
            Text("1 real map", font_size=24, color=RES),
            Text("+", font_size=24, color=DIM),
            Text("a whole crowd of null maps", font_size=24, color=BAD),
        ).arrange(RIGHT, buff=0.35).next_to(eq, DOWN, buff=0.9)
        self.play_beat(FadeIn(crowd, lag_ratio=0.3))                       # beat 5

        # what "special" means
        special = VGroup(
            Text("\"special\"  =  the observed map stands out from the crowd",
                 font_size=24, color=WHITE),
            Text("more backbone-shaped, or less, than a typical fake",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(crowd, DOWN, buff=0.5)
        self.play_beat(FadeIn(special, lag_ratio=0.3))                     # beat 6

        # the reduction
        self.play(FadeOut(VGroup(eq, crowd, special)), run_time=0.45)
        reduce = VGroup(
            Text("The whole test reduces to one comparison:",
                 font_size=27, color=RES),
            Text("where does the real map fall inside the cloud of maps from R?",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.3).move_to(RIGHT * 0.0 + DOWN * 0.1)
        self.play_beat(FadeIn(reduce, lag_ratio=0.3))                      # beat 7


# ----------------------------------------------------------------------
# Scene 3 — the test statistic is backbone shape  (7 beats)
# ----------------------------------------------------------------------
class S3_Statistic(NarratedScene):
    scene_key = "S3_Statistic"

    def construct(self):
        self.header("The test statistic is backbone shape")

        intro = Text("we need ONE number per map: a summary statistic",
                     font_size=27, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # T = cosine similarity to pooled connectome map
        eq = MathTex("T", "=",
                     r"\cos\!\big(", "m", r",\;", r"\bar m_C", r"\big)")\
            .scale(1.15).shift(UP * 1.2)
        eq[0].set_color(RES); eq[3].set_color(VAR); eq[5].set_color(BACK)
        bm = Brace(eq[3], DOWN, color=VAR)
        ml = Text("your map", font_size=21, color=VAR).next_to(bm, DOWN, buff=0.12)
        bc = Brace(eq[5], DOWN, color=BACK)
        cl = Text("pooled connectome map", font_size=21, color=BACK)\
            .next_to(bc, DOWN, buff=0.12)
        cap = Text("how backbone-shaped is this map", font_size=23, color=DIM)\
            .next_to(eq, UP, buff=0.35)
        self.play_beat(Write(eq), FadeIn(cap),
                       GrowFromCenter(bm), FadeIn(ml),
                       GrowFromCenter(bc), FadeIn(cl))                     # beat 2

        # T_obs
        self.play(FadeOut(VGroup(bm, ml, bc, cl, cap, intro)),
                  eq.animate.scale(0.8).to_edge(UP, buff=1.1), run_time=0.5)
        tobs = MathTex(r"T_{\mathrm{obs}}", "=",
                       r"T(", "m", r")\quad\text{on the OBSERVED lesions}")\
            .scale(1.0).shift(UP * 1.5)
        tobs[0].set_color(RES); tobs[3].set_color(VAR)
        self.play_beat(Write(tobs))                                        # beat 3

        # T^(b) on each ensemble draw
        tb = MathTex(r"T^{(b)}", "=",
                     r"T\big(", r"m_{\ell^{(b)}}", r"\big)",
                     r"\quad b = 1,\dots,B \in \mathcal{R}").scale(1.0)\
            .next_to(tobs, DOWN, buff=0.6)
        tb[0].set_color(BAD); tb[3].set_color(BAD)
        self.play_beat(Write(tb))                                         # beat 4

        # the null distribution (histogram)
        self.play(FadeOut(VGroup(tobs, tb)),
                  eq.animate.scale(0.85).to_corner(UL).shift(DOWN * 0.4 + RIGHT * 0.3),
                  run_time=0.5)
        axes = Axes(x_range=[0, 1, 0.25], y_range=[0, 1.1, 0.5],
                    x_length=7.5, y_length=2.8,
                    axis_config={"color": DIM, "include_tip": False,
                                 "include_numbers": False}).shift(DOWN * 0.3)
        xlab = Text("backbone-shape score  T", font_size=22, color=DIM)\
            .next_to(axes, DOWN, buff=0.2)
        # a bell-ish null histogram of T^(b)
        bars = VGroup()
        import math as _m
        for i, xc in enumerate(np.linspace(0.06, 0.94, 12)):
            h = _m.exp(-((xc - 0.5) ** 2) / (2 * 0.16 ** 2))
            bar = Rectangle(width=0.55, height=max(0.05, h) * 2.4,
                            stroke_width=0, fill_color=BAD, fill_opacity=0.55)
            bar.move_to(axes.c2p(xc, 0), aligned_edge=DOWN)
            bars.add(bar)
        nlab = MathTex(r"\{\,T^{(b)}\,\}", color=BAD).scale(0.85)\
            .next_to(axes, UP, buff=0.1).shift(LEFT * 1.8)
        self.play_beat(Create(axes), FadeIn(xlab),
                       FadeIn(bars, lag_ratio=0.1), FadeIn(nlab))          # beat 5

        # drop T_obs onto it
        x_obs = 0.62
        line = DashedLine(axes.c2p(x_obs, 0), axes.c2p(x_obs, 1.05),
                          color=RES, stroke_width=4)
        dot = Dot(axes.c2p(x_obs, 0), radius=0.1, color=RES)
        olab = MathTex(r"T_{\mathrm{obs}}", color=RES).scale(0.9)\
            .next_to(line, UP, buff=0.1)
        self.play_beat(Create(line), FadeIn(dot), FadeIn(olab))           # beat 6

        # hold the picture
        moral = Text("one observed statistic  vs  a histogram of ensemble statistics",
                     font_size=24, color=WHITE).next_to(xlab, DOWN, buff=0.4)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 7


# ----------------------------------------------------------------------
# Scene 4 — the procedure  (8 beats)
# ----------------------------------------------------------------------
class S4_Procedure(NarratedScene):
    scene_key = "S4_Procedure"

    def construct(self):
        self.header("The procedure  (P2, p.1025)")

        intro = Text("step by step, as the responders spell it out",
                     font_size=27, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # step 1
        s1 = VGroup(
            Text("1.", font_size=28, color=RES),
            Text("take one draw  b  from  R  →  reposition lesions randomly",
                 font_size=25, color=WHITE),
        ).arrange(RIGHT, buff=0.25).shift(UP * 1.55)
        s1[1][:].set_color(WHITE)
        self.play_beat(FadeIn(s1, shift=UP * 0.2))                        # beat 2

        # step 2
        s2 = VGroup(
            Text("2.", font_size=28, color=RES),
            Text("recompute LNM for those randomized lesions → a null map",
                 font_size=25, color=WHITE),
        ).arrange(RIGHT, buff=0.25).next_to(s1, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play_beat(FadeIn(s2, shift=UP * 0.2))                        # beat 3

        # step 3
        s3 = VGroup(
            Text("3.", font_size=28, color=RES),
            Text("retain the MAX voxel-wise value as one null sample",
                 font_size=25, color=WHITE),
        ).arrange(RIGHT, buff=0.25).next_to(s2, DOWN, buff=0.4, aligned_edge=LEFT)
        s3stat = MathTex(r"T^{(b)} = \max_v \, m^{(b)}_v", color=BAD)\
            .scale(0.85).next_to(s3, DOWN, buff=0.25, aligned_edge=LEFT).shift(RIGHT * 0.6)
        self.play_beat(FadeIn(s3, shift=UP * 0.2), Write(s3stat))         # beat 4

        # repeat >= 5000
        rep = MathTex(r"\text{repeat}", r"\ \geq 5000\ ", r"\text{permutations}")\
            .scale(0.95).next_to(s3stat, DOWN, buff=0.5)
        rep[1].set_color(EIG)
        rep_cap = Text("the histogram of T-(b) fills in", font_size=22, color=DIM)\
            .next_to(rep, DOWN, buff=0.2)
        self.play_beat(Write(rep), FadeIn(rep_cap))                       # beat 5

        # the p-value as a fraction
        self.play(FadeOut(VGroup(intro, s1, s2, s3, s3stat, rep, rep_cap)),
                  run_time=0.5)
        pval = MathTex(r"p", "=",
                       r"\frac{1}{B}\sum_{b=1}^{B}",
                       r"\mathbf{1}\!\left[\,", r"T^{(b)}", r"\ \geq\ ",
                       r"T_{\mathrm{obs}}", r"\,\right]")\
            .scale(1.05).shift(UP * 1.1)
        pval[0].set_color(VAR); pval[4].set_color(BAD); pval[6].set_color(RES)
        # decode the two unfamiliar symbols: the count B and the indicator 1[...]
        bB = Brace(pval[2], UP, color=DIM)
        bB_lab = Text("average over all B draws", font_size=20, color=DIM)\
            .next_to(bB, UP, buff=0.12)
        bI = Brace(pval[3], DOWN, color=DIM)
        bI_lab = Text("counts 1 when the draw beats T-obs, else 0",
                      font_size=20, color=DIM).next_to(bI, DOWN, buff=0.12)
        pcap = Text("the fraction of ensemble draws at least as large as observed",
                    font_size=23, color=DIM).next_to(bI_lab, DOWN, buff=0.3)
        self.play_beat(Write(pval), GrowFromCenter(bB), FadeIn(bB_lab),
                       GrowFromCenter(bI), FadeIn(bI_lab), FadeIn(pcap))   # beat 6

        # voxel version: 95th percentile, FWER 0.05  (clear the braces first)
        vox = VGroup(
            Text("voxel version:", font_size=24, color=WHITE),
            Text("significant if real value  >  95th percentile of the null",
                 font_size=24, color=BACK),
            Text("→  family-wise error controlled at 0.05", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.2).next_to(pcap, DOWN, buff=0.5)
        self.play_beat(FadeOut(VGroup(bB, bB_lab, bI, bI_lab)),
                       FadeIn(vox, lag_ratio=0.25))                        # beat 7

        # every symbol defined
        self.play(FadeOut(VGroup(pval, pcap, vox)), run_time=0.5)
        legend = VGroup(
            MathTex(r"\mathcal{R}", r"\ \text{= ensemble}", color=VAR).scale(0.95),
            MathTex(r"T^{(b)}", r"\ \text{= each null draw}", color=BAD).scale(0.95),
            MathTex(r"T_{\mathrm{obs}}", r"\ \text{= the real statistic}", color=RES).scale(0.95),
            MathTex(r"p", r"\ \text{= its right-tail rank}", color=WHITE).scale(0.95),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        legend[0][0].set_color(VAR); legend[1][0].set_color(BAD)
        legend[2][0].set_color(RES); legend[3][0].set_color(VAR)
        self.play_beat(FadeIn(legend, lag_ratio=0.25))                    # beat 8


# ----------------------------------------------------------------------
# Scene 5 — what it can and cannot answer  (7 beats)
# ----------------------------------------------------------------------
class S5_WhatItAsks(NarratedScene):
    scene_key = "S5_WhatItAsks"

    def construct(self):
        self.header("What it can and cannot answer")

        intro = Text("read the fine print — this is where nulls get misused",
                     font_size=27, color=RES).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                     # beat 1

        # one question only
        one = VGroup(
            Text("This null asks ONE question:", font_size=27, color=WHITE),
            Text("is the lesion location special?", font_size=28, color=VAR),
            MathTex(r"\text{nothing more is encoded in }H_0^{\mathrm{loc}}")
                .scale(0.85).set_color(DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.8)
        self.play_beat(FadeIn(one, lag_ratio=0.3))                        # beat 2

        # right tool IF claim is about location
        right = VGroup(
            Text("✓ the RIGHT tool  IF  the claim is about location",
                 font_size=26, color=BACK),
            Text("\"lesions HERE rather than THERE produce this map\"",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.2).next_to(one, DOWN, buff=0.55)
        self.play_beat(FadeIn(right, shift=UP * 0.2))                     # beat 3

        # small p meaning under the right claim
        small = Text("then a small p  =  real evidence the location drives the map",
                     font_size=24, color=DIM).next_to(right, DOWN, buff=0.4)
        self.play_beat(FadeIn(small))                                     # beat 4

        # cannot speak to symptom-label
        self.play(FadeOut(VGroup(intro, one, right, small)), run_time=0.5)
        cannot = VGroup(
            Text("✗ it CANNOT speak to a symptom–label relationship",
                 font_size=27, color=BAD),
            Text("it never looks at who was impaired and who was spared",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.3)
        self.play_beat(FadeIn(cannot, shift=UP * 0.2))                    # beat 5

        # needs a different null (Part 5)
        diff = VGroup(
            Text("does the SYMPTOM track the lesions?", font_size=26, color=RES),
            Text("a different question  →  a different null", font_size=25, color=WHITE),
            Text("the symptom-label null  (Part 5)", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.22).next_to(cannot, DOWN, buff=0.55)
        self.play_beat(FadeIn(diff, lag_ratio=0.3))                       # beat 6

        # the moral
        self.play(FadeOut(VGroup(cannot, diff)), run_time=0.5)
        moral = VGroup(
            Text("Same data, two questions.", font_size=30, color=WHITE),
            Text("Today: the LOCATION question, built cleanly and fully.",
                 font_size=26, color=VAR),
            Text("Next: the SYMPTOM question.", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                      # beat 7
