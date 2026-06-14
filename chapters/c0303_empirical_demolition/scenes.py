"""c0303_empirical_demolition — "The empirical case".

Five narrated scenes presenting the EMPIRICAL evidence van den Heuvel et al.
marshal against lesion network mapping (LNM), then scoping it honestly:

  S1_Dataset       102 maps across 72 studies — what a published network is.
  S2_DegreeTrace   78/102 carry a significant degree trace; spin / BrainSMASH.
  S3_Shuffled      shuffled lesions reproduce networks at r = 0.73 to 0.95.
  S4_Variance      basic connectome properties explain 93% (sLNM 79%) of variance.
  S5_WhatItProves  premises true, narrow conclusion true; the contrast is a
                   DIFFERENT object the evidence does not touch.

All equations/numbers page-cited in:
  responses/lnm_critique/papers/P1_critique.md
  responses/lnm_critique/papers/P2_nullmodels.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0303_empirical_demolition ./render.sh \
      chapters/c0303_empirical_demolition/scenes.py -q ql \
      S1_Dataset S2_DegreeTrace S3_Shuffled S4_Variance S5_WhatItProves
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the dataset: 102 maps, 72 studies
# ----------------------------------------------------------------------
class S1_Dataset(NarratedScene):
    scene_key = "S1_Dataset"

    def construct(self):
        self.header("102 maps, 72 studies   (P1, p.1239; Methods)")

        intro = Text("the critique comes with a re-analysis of the literature",
                     font_size=28, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # the two headline counts
        counts = VGroup(
            self._stat("102", "published (s)LNM maps", BAD),
            self._stat("72", "separate studies", VAR),
        ).arrange(RIGHT, buff=1.4).next_to(intro, DOWN, buff=0.7)
        self.play_beat(FadeIn(counts, lag_ratio=0.3))                      # beat 2

        # condition breakdown
        self.play(intro.animate.set_opacity(0.35), run_time=0.4)
        cond = MathTex("50", r"\ \text{neurological}", r"\ +\ ", "18",
                       r"\ \text{psychiatric}", r"\ +\ ", "4",
                       r"\ \text{behavioral}").scale(0.85)
        cond[0].set_color(VAR); cond[3].set_color(VAR); cond[6].set_color(VAR)
        cond.next_to(counts, DOWN, buff=0.7)
        self.play_beat(Write(cond))                                        # beat 3

        # how the corpus was built
        built = VGroup(
            Text("350 lesion masks manually segmented from papers",
                 font_size=24, color=WHITE),
            Text("+ 1,442 brain coordinates from 8 coordinate-based studies",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.22).next_to(cond, DOWN, buff=0.55)
        self.play_beat(FadeIn(built, lag_ratio=0.3))                       # beat 4

        # what a "published network" IS — the pipeline to one map
        self.play(FadeOut(VGroup(intro, counts, cond, built)), run_time=0.5)
        pipe = VGroup(
            self._chip("each patient's\nlesion", VAR),
            MathTex(r"\times\, C", color=WHITE).scale(1.1),
            self._chip("per-patient\nmap", DIM),
            MathTex(r"\xrightarrow{\ \text{average}\ }", color=BACK).scale(0.9),
            self._chip("ONE group\nmap", BAD),
        ).arrange(RIGHT, buff=0.45).shift(UP * 0.4)
        self.play_beat(FadeIn(pipe, lag_ratio=0.25))                       # beat 5

        verdict = Text("that single averaged map is the object on trial",
                       font_size=27, color=RES).next_to(pipe, DOWN, buff=0.8)
        box = SurroundingRectangle(pipe.submobjects[-1], color=RES, buff=0.12)
        self.play_beat(FadeIn(verdict, shift=UP * 0.2), Create(box))       # beat 6

    def _stat(self, big, label, color):
        n = Text(big, font_size=64, color=color)
        t = Text(label, font_size=22, color=DIM).next_to(n, DOWN, buff=0.15)
        return VGroup(n, t)

    def _chip(self, label, color):
        box = RoundedRectangle(width=2.0, height=1.0, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=19, color=color, line_spacing=0.8).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 2 — 78 of 102 carry a degree trace; spin / BrainSMASH nulls
# ----------------------------------------------------------------------
class S2_DegreeTrace(NarratedScene):
    scene_key = "S2_DegreeTrace"

    def construct(self):
        self.header("78 of 102 carry a degree trace   (P1, p.1243)")

        # headline count
        head = MathTex("78", r"\,/\,", "102", r"\ \text{maps carry a degree trace}")\
            .scale(1.2).shift(UP * 2.2)
        head[0].set_color(BAD); head[2].set_color(WHITE)
        self.play_beat(Write(head))                                        # beat 1

        # what degree is
        deg = MathTex(r"\deg(a)", "=", r"\textstyle\sum_b C_{ab}",
                      "=", r"\text{the hub map}").scale(0.95)
        deg[0].set_color(BAD); deg[4].set_color(BAD)
        deg.next_to(head, DOWN, buff=0.5)
        # decode every symbol: a (the fixed region/row), b (summed over), C_ab
        deg_brace = Brace(deg[2], DOWN, color=DIM)
        deg_cap = VGroup(
            MathTex(r"C_{ab}", r"=\ \text{connectivity of region } a \text{ to region } b",
                    color=DIM).scale(0.6),
            Text("fix row a, sum over every column b  →  region a's total connectivity",
                 font_size=21, color=DIM),
        ).arrange(DOWN, buff=0.16).next_to(deg_brace, DOWN, buff=0.18)
        deg_cap[0][0].set_color(WHITE)
        self.play_beat(Write(deg), GrowFromCenter(deg_brace),
                       FadeIn(deg_cap))                                     # beat 2

        # significance against what?
        self.play(FadeOut(VGroup(deg, deg_brace, deg_cap)),
                  head.animate.scale(0.7).to_edge(UP, buff=1.0), run_time=0.5)
        q = Text("significant against WHAT null?", font_size=30, color=RES)\
            .shift(UP * 1.4)
        warn = Text("you cannot just correlate two brain maps — smooth maps overlap by chance",
                    font_size=23, color=WHITE).next_to(q, DOWN, buff=0.3)
        self.play_beat(FadeIn(q), FadeIn(warn))                            # beat 3

        # spatial autocorrelation
        self.play(FadeOut(VGroup(q, warn)), run_time=0.4)
        sac = VGroup(
            Text("brain maps have SPATIAL AUTOCORRELATION", font_size=26, color=BACK),
            Text("nearby regions carry similar values", font_size=23, color=DIM),
            Text("→ a fair null must PRESERVE that smoothness", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.9)
        self.play_beat(FadeIn(sac, lag_ratio=0.3))                         # beat 4

        # the spin test
        self.play(FadeOut(sac), run_time=0.4)
        spin = VGroup(
            Text("SPIN TEST", font_size=28, color=BACK),
            Text("randomly rotate one map across the cortical surface", font_size=23, color=WHITE),
            Text("keeps spatial structure, breaks the alignment", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.0)
        self.play_beat(FadeIn(spin, lag_ratio=0.3))                        # beat 5

        # the p-spin threshold and the count
        pspin = MathTex(r"10{,}000\ \text{rotations}", r"\ \Rightarrow\ ",
                        r"P_{\text{spin}} < 0.05", r"\ \Rightarrow\ ", "78/102")\
            .scale(0.85).next_to(spin, DOWN, buff=0.6)
        pspin[2].set_color(BACK); pspin[4].set_color(BAD)
        self.play_beat(Write(pspin))                                       # beat 6

        # brainsmash, 91/102
        self.play(FadeOut(VGroup(spin, pspin)), run_time=0.4)
        bs = MathTex(r"\text{BrainSMASH null}", r"\ \Rightarrow\ ",
                     r"P_{\text{brainsmash}} < 0.05", r"\ \Rightarrow\ ", "91/102")\
            .scale(0.85).shift(UP * 0.7)
        bs[2].set_color(BACK); bs[4].set_color(BAD)
        bs_cap = Text("a second null with matched spatial autocorrelation",
                      font_size=22, color=DIM).next_to(bs, DOWN, buff=0.25)
        self.play_beat(Write(bs), FadeIn(bs_cap))                          # beat 7

        moral = MathTex(r"78", r"\text{ to }", r"91", r"\ \text{of}\ ", r"102",
                        r"\ \text{maps echo}\ ", r"\deg(C)").scale(0.95)
        moral[0].set_color(BAD); moral[2].set_color(BAD); moral[6].set_color(BAD)
        moral.next_to(bs_cap, DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 8


# ----------------------------------------------------------------------
# Scene 3 — shuffled lesions reproduce networks at r = 0.73 to 0.95
# ----------------------------------------------------------------------
class S3_Shuffled(NarratedScene):
    scene_key = "S3_Shuffled"

    def construct(self):
        self.header("Shuffled lesions reproduce the networks   (P1, p.1239)")

        intro = Text("take a published map — then throw away the real lesions",
                     font_size=27, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # the swap
        swap = VGroup(
            self._chip("real lesions", VAR),
            MathTex(r"\longrightarrow", color=BAD).scale(1.0),
            self._chip("shuffled\nat random", BAD),
        ).arrange(RIGHT, buff=0.5).next_to(intro, DOWN, buff=0.55)
        same = Text("...then run the SAME pipeline",
                    font_size=23, color=DIM).next_to(swap, DOWN, buff=0.3)
        self.play_beat(FadeIn(swap, lag_ratio=0.3), FadeIn(same))          # beat 2

        # which disorders
        disorders = Text("disrupted agency · autism · addiction · epilepsy",
                         font_size=24, color=WHITE).next_to(same, DOWN, buff=0.5)
        indist = Text("shuffled map  ≈  real map", font_size=26, color=BAD)\
            .next_to(disorders, DOWN, buff=0.25)
        self.play_beat(FadeIn(disorders), FadeIn(indist))                  # beat 3

        # the r range
        self.play(FadeOut(VGroup(intro, swap, same, disorders, indist)),
                  run_time=0.5)
        rrange = MathTex("r", "=", "0.73", r"\ \text{to}\ ", "0.95")\
            .scale(1.5).shift(UP * 1.4)
        rrange[2].set_color(BAD); rrange[4].set_color(BAD)
        rcap = Text("correlation between the real map and the shuffled-lesion map",
                    font_size=23, color=DIM).next_to(rrange, DOWN, buff=0.3)
        self.play_beat(Write(rrange), FadeIn(rcap))                        # beat 4

        # why high r under a null is damaging
        why = VGroup(
            Text("a good disease map should DIE", font_size=26, color=WHITE),
            Text("when you destroy the disease signal", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.18).next_to(rcap, DOWN, buff=0.6)
        self.play_beat(FadeIn(why, lag_ratio=0.3))                         # beat 5

        # what it means
        self.play(FadeOut(VGroup(rrange, rcap, why)), run_time=0.5)
        means = VGroup(
            MathTex(r"r = 0.95\ \text{under random lesions}").scale(0.95),
            Text("⇒  the map never carried the lesions' information",
                 font_size=25, color=WHITE),
            Text("it carried the CONNECTOME's", font_size=26, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.6)
        means[0].set_color(DIM)
        self.play_beat(FadeIn(means, lag_ratio=0.3))                       # beat 6

        # ties to the algebra
        tie = MathTex(r"\text{any heterogeneous lesion set}", r"\ \longrightarrow\ ",
                      r"\deg(C)").scale(0.95).next_to(means, DOWN, buff=0.55)
        tie[2].set_color(BAD)
        self.play_beat(Write(tie))                                         # beat 7

        moral = Text("the shuffle test is the empirical face of the convergence proof —\naimed squarely at the AVERAGE map",
                     font_size=24, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 8

    def _chip(self, label, color):
        box = RoundedRectangle(width=2.2, height=0.95, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=20, color=color, line_spacing=0.8).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 4 — 93% of variance explained by basic connectome properties
# ----------------------------------------------------------------------
class S4_Variance(NarratedScene):
    scene_key = "S4_Variance"

    def construct(self):
        self.header("93 percent of variance   (P1, p.1243)")

        q = Text("how much of a published map is predictable from C alone?",
                 font_size=27, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(q))                                          # beat 1

        # the predictors
        preds = VGroup(
            Text("predictors  =  basic connectome properties:", font_size=24, color=WHITE),
            Text("subcortical + cortical degree", font_size=23, color=DIM),
            Text("degree of 4 network modules", font_size=23, color=DIM),
            Text("3 functional gradients (first 3 PCs of C)", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).next_to(q, DOWN, buff=0.5)
        self.play_beat(FadeIn(preds, lag_ratio=0.25))                      # beat 2

        # no disease info
        nodis = Text("no disease info · no symptom scores · just the geometry of C",
                     font_size=23, color=BACK).next_to(preds, DOWN, buff=0.45)
        self.play_beat(FadeIn(nodis))                                      # beat 3

        # bar 1: LNM 93%
        self.play(FadeOut(VGroup(q, preds, nodis)), run_time=0.5)
        bar_lnm = self._bar(0.93, "93%", "LNM  (averaging)", "s.d. 5.0%")\
            .shift(UP * 1.1)
        self.play_beat(*[FadeIn(m) for m in bar_lnm.submobjects], lag_ratio=0.1)  # beat 4

        # bar 2: sLNM 79%
        bar_slnm = self._bar(0.79, "79%", "sLNM  (symptom-weighted)", "s.d. 10.2%")\
            .shift(DOWN * 0.9)
        self.play_beat(*[FadeIn(m) for m in bar_slnm.submobjects], lag_ratio=0.1)  # beat 5

        # read both bars
        read = Text("both bars filled almost to the top by connectome structure alone",
                    font_size=24, color=WHITE).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(read, shift=UP * 0.2))                       # beat 6

        # the caveat — about the AGGREGATE maps
        self.play(FadeOut(VGroup(bar_lnm, bar_slnm, read)), run_time=0.5)
        caveat = VGroup(
            Text("crucial caveat", font_size=28, color=RES),
            Text("these regressions are run on the AGGREGATE, averaged maps",
                 font_size=25, color=WHITE),
            Text("they describe what the GROUP picture is made of — nothing finer",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.28)
        self.play_beat(FadeIn(caveat, lag_ratio=0.3))                      # beat 7

    def _bar(self, frac, pct, name, sd):
        w = 8.0
        full = Rectangle(width=w, height=0.55, stroke_color=WHITE, stroke_width=2,
                         fill_opacity=0)
        filled = Rectangle(width=w * frac, height=0.55, stroke_width=0,
                           fill_color=BAD, fill_opacity=0.85)
        filled.align_to(full, LEFT)
        bar = VGroup(full, filled)
        pct_lab = Text(pct, font_size=30, color=BAD).next_to(full, RIGHT, buff=0.3)
        name_lab = Text(name, font_size=22, color=WHITE).next_to(full, UP, buff=0.18)
        sd_lab = Text(sd, font_size=20, color=DIM).next_to(full, DOWN, buff=0.15)
        return VGroup(bar, pct_lab, name_lab, sd_lab).move_to(ORIGIN)


# ----------------------------------------------------------------------
# Scene 5 — what the evidence does and does not prove
# ----------------------------------------------------------------------
class S5_WhatItProves(NarratedScene):
    scene_key = "S5_WhatItProves"

    def construct(self):
        self.header("What the evidence does — and does NOT — prove")

        # the three numbers
        three = VGroup(
            MathTex("78/102", color=BAD).scale(0.95),
            MathTex(r"r \leq 0.95", color=BAD).scale(0.95),
            MathTex(r"93\%\ \text{variance}", color=BAD).scale(0.95),
        ).arrange(RIGHT, buff=0.9).shift(UP * 2.3)
        three_cap = Text("three numbers — all real, all replicated",
                         font_size=23, color=DIM).next_to(three, DOWN, buff=0.25)
        self.play_beat(FadeIn(three, lag_ratio=0.3), FadeIn(three_cap))    # beat 1

        # the clean conclusion
        clean = VGroup(
            Text("✓  the GROUP-AVERAGE map is backbone-dominated → nonspecific",
                 font_size=24, color=BACK),
            Text("premise true — and the rebuttal CONCEDES it", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.18).next_to(three_cap, DOWN, buff=0.55)
        self.play_beat(FadeIn(clean, shift=UP * 0.2))                      # beat 2

        # so a real error is caught
        caught = Text("read a transdiagnostic hub network off the average and call it\nbiology — and the critique has caught a genuine error",
                      font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(clean, DOWN, buff=0.5)
        self.play_beat(FadeIn(caught, shift=UP * 0.2))                     # beat 3

        # BUT watch the object
        self.play(FadeOut(VGroup(three, three_cap, clean, caught)), run_time=0.5)
        watch = VGroup(
            Text("watch the OBJECT", font_size=30, color=RES),
            Text("every test is run on the AVERAGE, or its correlation to degree",
                 font_size=24, color=WHITE),
            Text("that is ONE specific quantity", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.4)
        self.play_beat(FadeIn(watch, lag_ratio=0.3))                       # beat 4

        # the un-proven claim: AVERAGE != CONTRAST
        split = VGroup(
            VGroup(
                Text("AVERAGE", font_size=26, color=DIM),
                Text("proven nonspecific", font_size=21, color=DIM),
            ).arrange(DOWN, buff=0.12),
            MathTex(r"\neq", color=RES).scale(1.4),
            VGroup(
                Text("CONTRAST", font_size=26, color=RES),
                Text("under a LABEL null", font_size=21, color=RES),
            ).arrange(DOWN, buff=0.12),
        ).arrange(RIGHT, buff=1.0).next_to(watch, DOWN, buff=0.6)
        notproven = Text("it does NOT prove the contrast finds nothing",
                         font_size=24, color=WHITE).next_to(split, DOWN, buff=0.35)
        self.play_beat(FadeIn(split, lag_ratio=0.2), FadeIn(notproven))    # beat 5

        # variability lost by averaging (P2)
        self.play(FadeOut(VGroup(watch, split, notproven)), run_time=0.5)
        varlost = VGroup(
            Text("averaging ERASES the across-lesion variability", font_size=25, color=WHITE),
            Text("Zalesky & Cash: the disease signal may live in", font_size=23, color=DIM),
            Text("precisely the variability that averaging throws away", font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.3)
        self.play_beat(FadeIn(varlost, lag_ratio=0.3))                     # beat 6

        # correlation is not evidence of no difference (P2, r=0.8)
        corr = MathTex(r"r = 0.80", r"\ \text{globally}", r"\ \not\Rightarrow\ ",
                       r"\text{no local difference}").scale(0.95)
        corr[0].set_color(BAD); corr[3].set_color(BACK)
        corr.next_to(varlost, DOWN, buff=0.6)
        corr_cap = Text("two maps can correlate at 0.80 yet differ sharply in a focal region",
                        font_size=22, color=DIM).next_to(corr, DOWN, buff=0.25)
        self.play_beat(Write(corr), FadeIn(corr_cap))                      # beat 7

        # the honest verdict
        self.play(FadeOut(VGroup(varlost, corr, corr_cap)), run_time=0.5)
        verdict = VGroup(
            Text("The average is nonspecific.   PROVEN.", font_size=28, color=WHITE),
            Text("The contrast is hopeless.   NOT proven.", font_size=28, color=RES),
            Text("Tested elsewhere under the right null, it survives.",
                 font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.32)
        self.play_beat(FadeIn(verdict, lag_ratio=0.3))                     # beat 8
