"""v0504_ebh_fdr — "E-values for FDR: the e-BH procedure".

Five narrated scenes on e-BH, the e-value Benjamini-Hochberg. Define FDR, give
the sort/threshold rule (reject top k where E_(k) >= m/(alpha k)), state the
arbitrary-dependence guarantee (Wang & Ramdas 2022), decode why linearity of
expectation makes dependence free, and tie it to voxelwise/brain-map sweeps.

All equations/numbers are from:
  volumes/vol5_evalues/chapters/04_ebh_fdr.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0504_ebh_fdr ./render.sh \
      chapters/v0504_ebh_fdr/scenes.py -q ql \
      S1_Multiple S2_eBH S3_Guarantee S4_Why S5_Use
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Many tests at once: define FDR
# ----------------------------------------------------------------------
class S1_Multiple(NarratedScene):
    scene_key = "S1_Multiple"

    def construct(self):
        self.header("Many tests at once")

        # beat 1 — the sweep
        sweep = VGroup(
            Text("A sweep, not one analysis:", font_size=28, color=WHITE),
            Text("adverse event  ×  timepoint  ×  model spec",
                 font_size=26, color=VAR),
            Text("each cell = its own whole-brain map = its own test",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.6)
        self.play_beat(FadeIn(sweep, lag_ratio=0.3))                       # beat 1

        # beat 2 — m hypotheses, m e-values
        evals = MathTex("E_1", ",", "E_2", ",", r"\dots", ",", "E_m")\
            .scale(1.3).shift(DOWN * 0.2)
        for idx in (0, 2, 6):
            evals[idx].set_color(EIG)
        ehead = Text("m hypotheses  →  m e-values",
                     font_size=26, color=WHITE).next_to(evals, UP, buff=0.5)
        self.play_beat(FadeIn(ehead), Write(evals))                        # beat 2

        # beat 3 — what an e-value is
        self.play(FadeOut(sweep), evals.animate.shift(UP * 1.4),
                  ehead.animate.shift(UP * 1.4), run_time=0.5)
        edef = MathTex("E_i", r"\geq", "0", r"\quad\text{and}\quad",
                       r"\mathbb{E}[E_i]", r"\leq", "1")\
            .scale(1.05).shift(DOWN * 0.1)
        edef[0].set_color(EIG); edef[4].set_color(EIG); edef[6].set_color(RES)
        bd = Brace(edef[4:7], DOWN, color=DIM)
        bd_lab = Text("expectation under its OWN null is at most one",
                      font_size=22, color=DIM).next_to(bd, DOWN, buff=0.2)
        big = Text("big e-value  =  strong evidence against that null",
                   font_size=23, color=BACK).next_to(bd_lab, DOWN, buff=0.4)
        self.play_beat(Write(edef), GrowFromCenter(bd),
                       FadeIn(bd_lab), FadeIn(big))                         # beat 3

        # beat 4 — discoveries, some are noise
        self.play(FadeOut(VGroup(ehead, evals, edef, bd, bd_lab, big)),
                  run_time=0.5)
        disc = VGroup(
            Text("Declare the impressive maps \"real\" = your DISCOVERIES",
                 font_size=26, color=WHITE),
            Text("some are genuine, some are flukes the null coughed up",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.7)
        self.play_beat(FadeIn(disc, lag_ratio=0.3))                        # beat 4

        # beat 5 — FDP definition
        fdp = MathTex(r"\mathrm{FDP}", "=",
                      r"\frac{\#\{\text{discoveries that are null}\}}"
                      r"{\#\{\text{discoveries}\}}")\
            .scale(1.0).shift(DOWN * 0.1)
        fdp[0].set_color(BAD)
        self.play_beat(Write(fdp))                                         # beat 5

        # beat 6 — you can't see the FDP
        unseen = Text("you are never told which discoveries were flukes\n"
                      "→  you cannot see the FDP; control its AVERAGE instead",
                      font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(fdp, DOWN, buff=0.6)
        self.play_beat(FadeIn(unseen, shift=UP * 0.2))                     # beat 6

        # beat 7 — FDR = E[FDP]
        self.play(FadeOut(VGroup(disc, fdp, unseen)), run_time=0.5)
        fdr = MathTex(r"\mathrm{FDR}", "=", r"\mathbb{E}", r"[", r"\mathrm{FDP}", r"]")\
            .scale(1.4).shift(UP * 0.7)
        fdr[0].set_color(RES); fdr[4].set_color(BAD)
        target = MathTex(r"\mathrm{FDR}", r"\leq", "0.05")\
            .scale(1.1).next_to(fdr, DOWN, buff=0.6)
        target[0].set_color(RES); target[2].set_color(EIG)
        tcap = Text("on average, ≤ 5% of your calls are false",
                    font_size=23, color=DIM).next_to(target, DOWN, buff=0.25)
        self.play_beat(Write(fdr), Write(target), FadeIn(tcap))            # beat 7

        # beat 8 — looser than FWER
        contrast = VGroup(
            Text("FWER:  forbid even ONE false positive  (strict)",
                 font_size=24, color=BAD),
            Text("FDR:  tolerate a few liars, keep the slice small  (right for a sweep)",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.3).to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(contrast[0]),
                       FadeIn(contrast[1], shift=UP * 0.2))                # beat 8


# ----------------------------------------------------------------------
# Scene 2 — the e-BH procedure
# ----------------------------------------------------------------------
class S2_eBH(NarratedScene):
    scene_key = "S2_eBH"

    def construct(self):
        self.header("The e-BH procedure")

        # beat 1 — one threshold on the whole pile
        intro = VGroup(
            Text("e-BH:  the e-value Benjamini–Hochberg", font_size=30, color=WHITE),
            Text("one threshold, applied to the whole pile of e-values",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 2.3)
        self.play_beat(FadeIn(intro, lag_ratio=0.3))                       # beat 1

        # beat 2 — step 1: sort descending
        srt = MathTex("E_{(1)}", r"\geq", "E_{(2)}", r"\geq", r"\cdots",
                      r"\geq", "E_{(m)}").scale(1.2).shift(UP * 0.9)
        for idx in (0, 2, 6):
            srt[idx].set_color(EIG)
        s1 = Text("Step 1 — sort descending: biggest evidence first",
                  font_size=24, color=BACK).next_to(srt, UP, buff=0.45)
        bk = Brace(srt[0], DOWN, color=DIM)
        bk_lab = Text("E in parentheses k = the k-th largest e-value",
                      font_size=21, color=DIM).next_to(bk, DOWN, buff=0.2)
        self.play_beat(FadeIn(s1), Write(srt),
                       GrowFromCenter(bk), FadeIn(bk_lab))                 # beat 2

        # beat 3 — step 2 (walk down for largest clearing rank)
        self.play(FadeOut(VGroup(intro, srt, s1, bk, bk_lab)), run_time=0.5)
        s2 = VGroup(
            Text("Step 2 — find the cutoff rank", font_size=27, color=BACK),
            Text("walk down the sorted list; find the LARGEST rank k",
                 font_size=24, color=WHITE),
            Text("whose e-value still clears a RISING bar",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.2)
        self.play_beat(FadeIn(s2, lag_ratio=0.3))                          # beat 3

        # beat 4 — the rule itself
        rule = MathTex(r"k^\star", "=", r"\max\Big\{ k :",
                       "E_{(k)}", r"\geq", r"\frac{m}{\alpha\, k}", r"\Big\}")\
            .scale(1.15).next_to(s2, DOWN, buff=0.7)
        rule[0].set_color(RES); rule[3].set_color(EIG); rule[5].set_color(BAD)
        br = Brace(rule[5], DOWN, color=BAD)
        br_lab = Text("the bar:  m over alpha times k", font_size=21, color=BAD)\
            .next_to(br, DOWN, buff=0.18)
        zero = Text("(k-star = 0 if no rank clears)",
                    font_size=20, color=DIM).next_to(br_lab, DOWN, buff=0.25)
        self.play_beat(Write(rule), GrowFromCenter(br),
                       FadeIn(br_lab), FadeIn(zero))                       # beat 4

        # beat 5 — step 3: reject top k-star
        self.play(FadeOut(VGroup(s2, rule, br, br_lab, zero)), run_time=0.5)
        s3 = VGroup(
            Text("Step 3 — reject the top k-star", font_size=28, color=BACK),
            Text("the k-star analyses with the largest e-values = discoveries",
                 font_size=24, color=WHITE),
            Text("one sort, one threshold", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.4)
        self.play_beat(FadeIn(s3, lag_ratio=0.3))                          # beat 5

        # beat 6 — price of admission, lone discovery
        lone = MathTex(r"k=1:\quad", r"\text{bar} = \frac{m}{\alpha}",
                       r"\ =\ 800", r"\quad (m=40,\ \alpha=0.05)")\
            .scale(0.95).next_to(s3, DOWN, buff=0.7)
        lone[1].set_color(BAD); lone[2].set_color(RES)
        lone_cap = Text("a LONE discovery must be overwhelming",
                        font_size=23, color=DIM).next_to(lone, DOWN, buff=0.3)
        self.play_beat(Write(lone), FadeIn(lone_cap))                      # beat 6

        # beat 7 — a crowd shares the burden
        crowd = MathTex(r"k=20:\quad", r"\text{bar} = \frac{m}{\alpha\cdot 20}",
                        r"\ =\ 40").scale(0.95).next_to(lone_cap, DOWN, buff=0.45)
        crowd[1].set_color(BACK); crowd[2].set_color(RES)
        crowd_cap = Text("a big club shares the burden of proof",
                         font_size=23, color=BACK).next_to(crowd, DOWN, buff=0.25)
        self.play_beat(Write(crowd), FadeIn(crowd_cap))                    # beat 7

        # beat 8 — mirror of plain BH on 1/E
        self.play(FadeOut(VGroup(s3, lone, lone_cap, crowd, crowd_cap)),
                  run_time=0.5)
        mirror = VGroup(
            VGroup(
                Text("plain BH (p-values)", font_size=24, color=DIM),
                Text("small good · sort ascending", font_size=21, color=DIM),
                MathTex(r"\text{bar }\ \tfrac{\alpha k}{m}\ \text{ grows}",
                        color=DIM).scale(0.85),
            ).arrange(DOWN, buff=0.18),
            MathTex(r"\Longleftrightarrow", color=RES).scale(1.3),
            VGroup(
                Text("e-BH (e-values)", font_size=24, color=EIG),
                Text("big good · sort descending", font_size=21, color=EIG),
                MathTex(r"\text{bar }\ \tfrac{m}{\alpha k}\ \text{ shrinks}",
                        color=EIG).scale(0.85),
            ).arrange(DOWN, buff=0.18),
        ).arrange(RIGHT, buff=0.8).shift(UP * 0.7)
        link = MathTex(r"1/E", r"\ \text{is a cautious p-value}",
                       r"\ \Rightarrow\ ", r"\text{e-BH = BH run on } 1/E")\
            .scale(0.9).next_to(mirror, DOWN, buff=0.6)
        link[0].set_color(EIG); link[3].set_color(WHITE)
        self.play_beat(FadeIn(mirror, lag_ratio=0.2), Write(link))         # beat 8


# ----------------------------------------------------------------------
# Scene 3 — FDR control under any dependence
# ----------------------------------------------------------------------
class S3_Guarantee(NarratedScene):
    scene_key = "S3_Guarantee"

    def construct(self):
        self.header("FDR control under any dependence")

        # beat 1 — the payoff
        payoff = VGroup(
            Text("The e-value superpower:", font_size=30, color=RES),
            Text("e-BH controls FDR at α for ARBITRARY dependence",
                 font_size=27, color=WHITE),
            Text("between the e-values", font_size=27, color=WHITE),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.6)
        self.play_beat(FadeIn(payoff, lag_ratio=0.3))                      # beat 1

        # beat 2 — the hypotheses
        hyp = MathTex("E_i", r"\geq", "0", r",\quad", r"\mathbb{E}[E_i]",
                      r"\leq", "1", r"\ \text{under}\ ", "H_i")\
            .scale(1.0).next_to(payoff, DOWN, buff=0.6)
        hyp[0].set_color(EIG); hyp[4].set_color(EIG)
        hyp[6].set_color(RES); hyp[8].set_color(VAR)
        self.play_beat(Write(hyp))                                         # beat 2

        # beat 3 — run e-BH
        self.play(FadeOut(payoff), hyp.animate.to_edge(UP, buff=1.1),
                  run_time=0.5)
        run = MathTex(r"\text{reject top }", r"k^\star", "=",
                      r"\max\{ k :", "E_{(k)}", r"\geq", r"\tfrac{m}{\alpha k}", r"\}")\
            .scale(1.0).shift(UP * 1.4)
        run[1].set_color(RES); run[4].set_color(EIG); run[6].set_color(BAD)
        self.play_beat(Write(run))                                         # beat 3

        # beat 4 — the bound
        bound = MathTex(r"\mathrm{FDR}", r"\;\leq\;",
                        r"\frac{\alpha}{m} \sum_{i \in \mathcal{H}_0} \mathbb{E}[E_i]",
                        r"\;\leq\;", r"\alpha")\
            .scale(1.15).next_to(run, DOWN, buff=0.7)
        bound[0].set_color(RES); bound[4].set_color(RES)
        b0 = Brace(bound[2], DOWN, color=DIM)
        b0_lab = Text("H-naught = the truly null hypotheses",
                      font_size=21, color=DIM).next_to(b0, DOWN, buff=0.2)
        self.play_beat(Write(bound), GrowFromCenter(b0), FadeIn(b0_lab))   # beat 4

        # beat 5 — load-bearing phrase
        self.play(FadeOut(VGroup(b0, b0_lab)), run_time=0.4)
        phrase = Text("with NO assumption on the joint dependence of the e-values",
                      font_size=26, color=BACK).next_to(bound, DOWN, buff=0.6)
        box = SurroundingRectangle(phrase, color=BACK, buff=0.22)
        self.play_beat(FadeIn(phrase), Create(box))                        # beat 5

        # beat 6 — the dependence examples
        self.play(FadeOut(VGroup(hyp, run, bound, phrase, box)), run_time=0.5)
        deps = VGroup(
            Text("voxels bleed into their neighbors", font_size=25, color=WHITE),
            Text("the 3-month map and the 12-month map share patients",
                 font_size=25, color=WHITE),
            Text("two models share data", font_size=25, color=WHITE),
            Text("e-BH does not care", font_size=28, color=RES),
        ).arrange(DOWN, buff=0.28).shift(UP * 0.3)
        self.play_beat(LaggedStart(*[FadeIn(d, shift=UP * 0.15) for d in deps],
                                   lag_ratio=0.25))                        # beat 6

        # beat 7 — attribution + why BH can't
        self.play(FadeOut(deps), run_time=0.4)
        attr = VGroup(
            Text("Wang & Ramdas, JRSS-B 84(3):822–852 (2022)",
                 font_size=22, color=DIM),
            Text("doi:10.1111/rssb.12489 · arXiv:2009.02824",
                 font_size=20, color=DIM),
            Text("plain BH needs a positive-dependence (PRDS) assumption",
                 font_size=24, color=BAD),
            Text("you often cannot defend for overlapping brain maps",
                 font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.4)
        self.play_beat(FadeIn(attr, lag_ratio=0.25))                       # beat 7


# ----------------------------------------------------------------------
# Scene 4 — why dependence is free
# ----------------------------------------------------------------------
class S4_Why(NarratedScene):
    scene_key = "S4_Why"

    def construct(self):
        self.header("Why dependence is free")

        # beat 1 — the thesis
        thesis = VGroup(
            Text("The guarantee rides on LINEARITY OF EXPECTATION",
                 font_size=28, color=RES),
            Text("not on independence", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.25).shift(UP * 2.4)
        self.play_beat(FadeIn(thesis, lag_ratio=0.3))                      # beat 1

        # beat 2 — Move 1: rejection forces a floor
        m1 = Text("Move 1 — the rule never rejects a cheap e-value",
                  font_size=25, color=BACK).shift(UP * 1.3)
        m1eq = MathTex(r"i\ \text{rejected}", r"\ \Rightarrow\ ",
                       "E_i", r"\geq", r"\frac{m}{\alpha\, |\mathcal{R}|}")\
            .scale(1.05).next_to(m1, DOWN, buff=0.4)
        m1eq[2].set_color(EIG); m1eq[4].set_color(BAD)
        br = Brace(m1eq[4], DOWN, color=DIM)
        br_lab = Text("|R| = total number of rejections",
                      font_size=21, color=DIM).next_to(br, DOWN, buff=0.18)
        self.play_beat(FadeIn(m1), Write(m1eq),
                       GrowFromCenter(br), FadeIn(br_lab))                 # beat 2

        # beat 3 — flip it
        self.play(FadeOut(VGroup(m1, br, br_lab)),
                  m1eq.animate.shift(UP * 1.0), run_time=0.5)
        flip = MathTex(r"\frac{1}{|\mathcal{R}|}", r"\;\leq\;",
                       r"\frac{\alpha}{m}", "E_i")\
            .scale(1.25).shift(UP * 0.1)
        flip[0].set_color(BAD); flip[2].set_color(RES); flip[3].set_color(EIG)
        flip_cap = Text("each discovery's contribution to the FDP\n"
                        "is paid for by a chunk of its own e-value",
                        font_size=23, color=DIM, line_spacing=0.8)\
            .next_to(flip, DOWN, buff=0.5)
        self.play_beat(Write(flip), FadeIn(flip_cap))                      # beat 3

        # beat 4 — Move 2: sum over true nulls
        self.play(FadeOut(VGroup(m1eq, flip, flip_cap)), run_time=0.5)
        m2 = Text("Move 2 — sum the trade over the true nulls",
                  font_size=25, color=BACK).shift(UP * 1.5)
        m2eq = MathTex(r"\mathrm{FDP}", r"\;\leq\;",
                       r"\frac{\alpha}{m}", r"\sum_{i \in \mathcal{H}_0}", "E_i")\
            .scale(1.2).next_to(m2, DOWN, buff=0.5)
        m2eq[0].set_color(BAD); m2eq[2].set_color(RES); m2eq[4].set_color(EIG)
        self.play_beat(FadeIn(m2), Write(m2eq))                            # beat 4

        # beat 5 — fixed constant
        fixed = Text("the coefficient  α / m  is a FIXED constant — not random",
                     font_size=24, color=BACK).next_to(m2eq, DOWN, buff=0.6)
        fbox = SurroundingRectangle(fixed, color=BACK, buff=0.2)
        self.play_beat(FadeIn(fixed), Create(fbox))                        # beat 5

        # beat 6 — Move 3: take expectation
        self.play(FadeOut(VGroup(m2, m2eq, fixed, fbox)), run_time=0.5)
        m3 = Text("Move 3 — take the expectation of both sides",
                  font_size=25, color=BACK).shift(UP * 1.5)
        m3eq = MathTex(r"\mathrm{FDR}", "=", r"\mathbb{E}[\mathrm{FDP}]", r"\;\leq\;",
                       r"\frac{\alpha}{m}", r"\sum_{i \in \mathcal{H}_0}",
                       r"\mathbb{E}[E_i]").scale(1.0).next_to(m3, DOWN, buff=0.5)
        m3eq[0].set_color(RES); m3eq[4].set_color(RES); m3eq[6].set_color(EIG)
        lin = Text("expectation is linear, ALWAYS:\n"
                   "a sum of expectations no matter how the terms correlate",
                   font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(m3eq, DOWN, buff=0.5)
        self.play_beat(FadeIn(m3), Write(m3eq), FadeIn(lin))               # beat 6

        # beat 7 — the exact place dependence dies
        self.play(FadeOut(VGroup(m3, lin)),
                  m3eq.animate.shift(UP * 1.1), run_time=0.5)
        kill = Text("this is exactly where dependence would kill a p-value argument\n"
                    "— and where it simply does not enter",
                    font_size=24, color=WHITE, line_spacing=0.8).shift(DOWN * 0.4)
        kill2 = Text("linearity never needs independence",
                     font_size=26, color=RES).next_to(kill, DOWN, buff=0.4)
        self.play_beat(FadeIn(kill, shift=UP * 0.2), FadeIn(kill2))        # beat 7

        # beat 8 — close: E[E_i] <= 1 collapses it
        self.play(FadeOut(VGroup(m3eq, kill, kill2)), run_time=0.5)
        close = MathTex(r"\mathrm{FDR}", r"\;\leq\;", r"\frac{\alpha}{m}",
                        r"\sum_{i \in \mathcal{H}_0} \mathbb{E}[E_i]", r"\;\leq\;",
                        r"\frac{\alpha}{m}", r"\cdot m", "=", r"\alpha")\
            .scale(1.05).shift(UP * 0.5)
        close[0].set_color(RES); close[8].set_color(RES)
        cap = Text("each true-null term ≤ 1; there are ≤ m of them.  Done.",
                   font_size=24, color=WHITE).next_to(close, DOWN, buff=0.6)
        self.play_beat(Write(close), FadeIn(cap))                          # beat 8


# ----------------------------------------------------------------------
# Scene 5 — where this helps
# ----------------------------------------------------------------------
class S5_Use(NarratedScene):
    scene_key = "S5_Use"

    def construct(self):
        self.header("Where this helps")

        # beat 1 — the setting
        setting = VGroup(
            Text("Voxelwise brain-map testing is MASSIVELY dependent",
                 font_size=27, color=WHITE),
            Text("exactly the setting e-BH was built for",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.25).shift(UP * 2.3)
        self.play_beat(FadeIn(setting, lag_ratio=0.3))                     # beat 1

        # beat 2 — finding D3
        d3 = VGroup(
            Text("Audit finding D3:", font_size=26, color=BAD),
            Text("the batch pipeline tests timepoint × AE × model",
                 font_size=24, color=WHITE),
            Text("as separate maps — and nothing controls error ACROSS them",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.22).next_to(setting, DOWN, buff=0.6)
        self.play_beat(FadeIn(d3, lag_ratio=0.3))                          # beat 2

        # beat 3 — within-map FWE
        self.play(FadeOut(VGroup(setting, d3)), run_time=0.5)
        within = VGroup(
            Text("Within-map control already exists (Vol 4):",
                 font_size=25, color=DIM),
            Text("max-stat permutation FWE", font_size=27, color=BACK),
            Text("\"is there a false positive ANYWHERE in this one map?\"",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.3)
        self.play_beat(FadeIn(within, lag_ratio=0.3))                      # beat 3

        # beat 4 — e-BH sits on top
        ontop = VGroup(
            Text("e-BH sits ON TOP — a different question:",
                 font_size=25, color=DIM),
            Text("\"of all the maps I called real, what fraction are false?\"",
                 font_size=24, color=WHITE),
            Text("across-sweep FDR.   You want BOTH layers.",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.25).next_to(within, DOWN, buff=0.7)
        self.play_beat(FadeIn(ontop, lag_ratio=0.3))                       # beat 4

        # beat 5 — wildly dependent; BH can't
        self.play(FadeOut(VGroup(within, ontop)), run_time=0.5)
        wild = VGroup(
            Text("The maps are wildly dependent:", font_size=26, color=WHITE),
            Text("overlapping cohorts · autocorrelated voxels · shared data",
                 font_size=24, color=VAR),
            Text("plain BH needs a positive-dependence claim",
                 font_size=24, color=BAD),
            Text("you cannot honestly defend here",
                 font_size=24, color=BAD),
        ).arrange(DOWN, buff=0.24).shift(UP * 0.6)
        self.play_beat(FadeIn(wild, lag_ratio=0.25))                       # beat 5

        # beat 6 — proof never used dependence -> recipe
        self.play(FadeOut(wild), run_time=0.4)
        recipe = VGroup(
            Text("the e-BH proof never used a dependence assumption",
                 font_size=25, color=BACK),
            Text("→  that whole worry is off the table", font_size=24, color=DIM),
            MathTex(r"\text{mint one } E_i \text{ per cell}", r"\ \Rightarrow\ ",
                    r"\text{e-BH}", r"\ \Rightarrow\ ",
                    r"\text{FDR-controlled subset}").scale(0.9),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.4)
        recipe[2][0].set_color(EIG); recipe[2][2].set_color(RES)
        recipe[2][4].set_color(BACK)
        self.play_beat(FadeIn(recipe, lag_ratio=0.25))                     # beat 6

        # beat 7 — two caveats
        self.play(FadeOut(recipe), run_time=0.4)
        cav = VGroup(
            Text("Two honest caveats:", font_size=26, color=BAD),
            Text("1.  e-BH is conservative — buys robustness with POWER;",
                 font_size=23, color=WHITE),
            Text("     can reject nothing where BH would flag a cell",
                 font_size=23, color=WHITE),
            Text("2.  only as good as the null behind each e-value —",
                 font_size=23, color=WHITE),
            Text("     adjust for confounders like lesion size",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(UP * 0.3)
        self.play_beat(FadeIn(cav, lag_ratio=0.2))                         # beat 7

        # beat 8 — tie back to the series
        self.play(FadeOut(cav), run_time=0.4)
        close = VGroup(
            Text("One e-value at a time built the bet.", font_size=28, color=WHITE),
            Text("e-BH takes the whole pile and hands back", font_size=28, color=WHITE),
            Text("an honest, dependence-proof slice of discoveries.",
                 font_size=28, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(close, lag_ratio=0.3))                       # beat 8
