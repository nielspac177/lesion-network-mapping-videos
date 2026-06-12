"""c0103_charge_formalized — "The critique, formalized, and its exact scope".

Six narrated scenes. State the 2026 van den Heuvel critique precisely and FAIRLY,
formalize its object (LNM = sum(M x C) -> degree of C), give its evidence, then
bound it: the proof holds only for the GROUP-AVERAGE map under UNIFORM,
NON-OVERLAPPING sampling. Real symptom-causing lesions overlap and are non-random,
and a symptom CONTRAST is a different object.

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/01_the_charge_formalized.md
  responses/lnm_critique/papers/P1_critique.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0103_charge_formalized ./render.sh \
      chapters/c0103_charge_formalized/scenes.py -q ql \
      S1_Thesis S2_FormalObject S3_sLNM S4_Evidence S5_Scope S6_EntailedVsOverclaimed
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the thesis, stated fairly
# ----------------------------------------------------------------------
class S1_Thesis(NarratedScene):
    scene_key = "S1_Thesis"

    def construct(self):
        title = Text("The charge, stated precisely", font_size=42, color=WHITE)
        sub = Text("a fair hearing before any rebuttal",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        cite = Text("van den Heuvel et al., Nature Neuroscience 29:1237–1247 (2026)",
                    font_size=24, color=DIM).shift(UP * 1.7)
        paper = Text("\"Investigating the methodological foundation of\nlesion network mapping\"",
                     font_size=26, color=WHITE, line_spacing=0.8).next_to(cite, DOWN, buff=0.4)
        self.play_beat(FadeIn(cite), FadeIn(paper))                         # beat 2

        thesis = VGroup(
            Text("Thesis:", font_size=28, color=RES),
            Text("published disease maps may be largely reconstructions",
                 font_size=26, color=WHITE),
            Text("of one fixed object — the connectome's geometry.",
                 font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        thesis.next_to(paper, DOWN, buff=0.6)
        self.play_beat(FadeIn(thesis, shift=UP * 0.2))                      # beat 3

        # three seeds -> roughly one map
        self.play(FadeOut(VGroup(cite, paper, thesis)), run_time=0.5)
        seeds = VGroup(
            self._seed_chip("real lesion", VAR),
            self._seed_chip("synthetic", DIM),
            self._seed_chip("random blob", BAD),
        ).arrange(DOWN, buff=0.45).shift(LEFT * 3.6 + DOWN * 0.3)
        arrow = Arrow(LEFT * 1.2 + DOWN * 0.3, RIGHT * 1.0 + DOWN * 0.3,
                      color=DIM, buff=0.1)
        same = VGroup(
            Text("roughly the SAME", font_size=26, color=RES),
            Text("picture", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.1).shift(RIGHT * 3.3 + DOWN * 0.3)
        self.play_beat(FadeIn(seeds, lag_ratio=0.2), GrowArrow(arrow),
                       FadeIn(same))                                        # beat 4

        backbone = Text("the atlas has a dominant skeleton every seed lights up",
                        font_size=26, color=BACK).to_edge(DOWN, buff=1.1)
        bb_word = Text("→  the BACKBONE", font_size=28, color=BACK)\
            .next_to(backbone, DOWN, buff=0.25)
        self.play_beat(FadeIn(backbone), FadeIn(bb_word, shift=UP * 0.2))   # beat 5

        self.play(FadeOut(VGroup(seeds, arrow, same, backbone, bb_word)),
                  run_time=0.5)
        plan = VGroup(
            Text("Goal of this video:", font_size=28, color=WHITE),
            Text("1.  make \"roughly the same picture\" precise", font_size=26, color=VAR),
            Text("2.  fence in the ONE assumption that makes it true", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        self.play_beat(FadeIn(plan, lag_ratio=0.2))                        # beat 6

    def _seed_chip(self, label, color):
        box = RoundedRectangle(width=2.7, height=0.7, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=22, color=color).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 2 — the formal object: LNM = sum(M x C) -> degree(C)
# ----------------------------------------------------------------------
class S2_FormalObject(NarratedScene):
    scene_key = "S2_FormalObject"

    def construct(self):
        self.header("The formal object  (P1, Eq. 3)")

        intro = Text("LNM compresses to a single matrix expression",
                     font_size=28, color=DIM).shift(UP * 2.4)
        self.play_beat(FadeIn(intro))                                      # beat 1

        eq = MathTex(r"\mathrm{LNM}", "=", r"\textstyle\sum_{s}", "M", r"\times", "C")\
            .scale(1.4).shift(UP * 0.9)
        eq[0].set_color(VAR); eq[3].set_color(VAR); eq[5].set_color(WHITE)
        self.play_beat(Write(eq), intro.animate.set_opacity(0.4))          # beat 2

        # annotate C
        brace_C = Brace(eq[5], DOWN, color=WHITE)
        c_lab = Text("fixed normative connectome\nC_ab = connectivity of region a to b",
                     font_size=22, color=WHITE, line_spacing=0.8)\
            .next_to(brace_C, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(brace_C), FadeIn(c_lab))             # beat 3

        # annotate M
        self.play(FadeOut(VGroup(brace_C, c_lab)), run_time=0.4)
        brace_M = Brace(eq[3], UP, color=VAR)
        m_lab = Text("lesion matrix:  rows = patients,  cols = regions\n1 if the lesion covers that region, else 0",
                     font_size=22, color=VAR, line_spacing=0.8)\
            .next_to(brace_M, UP, buff=0.2)
        self.play_beat(GrowFromCenter(brace_M), FadeIn(m_lab))             # beat 4

        # what M x C does
        self.play(FadeOut(VGroup(brace_M, m_lab, intro)), run_time=0.4)
        action = VGroup(
            Text("M × C  selects the rows of C that a lesion hit",
                 font_size=26, color=WHITE),
            Text("the outer sum averages those rows across patients",
                 font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(action, lag_ratio=0.3))                      # beat 5

        # convergence claim: M -> I
        self.play(FadeOut(action), eq.animate.scale(0.7).to_edge(UP, buff=1.1),
                  run_time=0.5)
        conv = MathTex("M", r"\to", "I", r"\quad\Longrightarrow\quad",
                       r"\mathrm{LNM}\ \text{copies}\ C").scale(1.1).shift(UP * 0.9)
        conv[0].set_color(VAR); conv[2].set_color(EIG); conv[4].set_color(WHITE)
        conv_cap = Text("uniform coverage: one lesion per region",
                        font_size=24, color=DIM).next_to(conv, DOWN, buff=0.3)
        self.play_beat(Write(conv), FadeIn(conv_cap))                      # beat 6

        # row-sum = degree = hub map
        deg = MathTex(r"\text{row-sum of } C", "=", r"\deg(C)", "=",
                      r"\text{the hub map}").scale(1.1).next_to(conv_cap, DOWN, buff=0.6)
        deg[2].set_color(BAD); deg[4].set_color(BAD)
        self.play_beat(Write(deg))                                         # beat 7

        fast = MathTex(r"\geq 10\ \text{heterogeneous lesions}", r"\ \Rightarrow\ ",
                       r"r > 0.44\ \text{to degree}").scale(0.95)
        fast[2].set_color(BAD)
        fast.next_to(deg, DOWN, buff=0.5)
        self.play_beat(FadeIn(fast))                                       # beat 8


# ----------------------------------------------------------------------
# Scene 3 — sLNM -> PC1(C),  r(PC1, degree) = 0.82
# ----------------------------------------------------------------------
class S3_sLNM(NarratedScene):
    scene_key = "S3_sLNM"

    def construct(self):
        self.header("The symptom-weighted variant  (P1, Eq. 4)")

        intro = Text("sLNM weights each map by a symptom score",
                     font_size=28, color=DIM).shift(UP * 2.3)
        self.play_beat(FadeIn(intro))                                      # beat 1

        eq = MathTex(r"\mathrm{sLNM}", "=", "s_v", r"\times", r"(M \times C)")\
            .scale(1.3).shift(UP * 0.9)
        eq[0].set_color(BAD); eq[2].set_color(EIG); eq[4].set_color(VAR)
        brace = Brace(eq[2], DOWN, color=EIG)
        sv_lab = Text("standardized symptom vector", font_size=22, color=EIG)\
            .next_to(brace, DOWN, buff=0.2)
        self.play_beat(Write(eq), GrowFromCenter(brace), FadeIn(sv_lab))   # beat 2

        # structured matrix -> dominant latent factor
        self.play(FadeOut(VGroup(brace, sv_lab, intro)), run_time=0.4)
        why = VGroup(
            Text("M × C is structured and nearly low-rank",
                 font_size=26, color=WHITE),
            Text("so sLNM aligns with its dominant latent factor",
                 font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(eq, DOWN, buff=0.7)
        self.play_beat(FadeIn(why, lag_ratio=0.3))                         # beat 3

        # PC1
        self.play(FadeOut(why), eq.animate.scale(0.75).to_edge(UP, buff=1.1),
                  run_time=0.5)
        pc1 = MathTex(r"\mathrm{sLNM}", r"\;\longrightarrow\;",
                      r"\mathrm{PC1}(C)").scale(1.3).shift(UP * 0.7)
        pc1[0].set_color(BAD); pc1[2].set_color(BACK)
        pc1_cap = Text("the first principal component of C",
                       font_size=24, color=DIM).next_to(pc1, DOWN, buff=0.3)
        self.play_beat(Write(pc1), FadeIn(pc1_cap))                        # beat 4

        # the catch: PC1 ~ degree at r=0.82
        catch = MathTex(r"r\big(", r"\mathrm{PC1}", ",", r"\deg(C)", r"\big)",
                        "=", "0.82").scale(1.25).next_to(pc1_cap, DOWN, buff=0.7)
        catch[1].set_color(BACK); catch[3].set_color(BAD); catch[6].set_color(RES)
        box = SurroundingRectangle(catch, color=RES, buff=0.2)
        self.play_beat(Write(catch), Create(box))                          # beat 5

        moral = Text("both roads — averaging and symptom-weighting —\nlead to almost the same hub-shaped place",
                     font_size=26, color=WHITE, line_spacing=0.8)\
            .next_to(box, DOWN, buff=0.5)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 6


# ----------------------------------------------------------------------
# Scene 4 — the evidence
# ----------------------------------------------------------------------
class S4_Evidence(NarratedScene):
    scene_key = "S4_Evidence"

    def construct(self):
        self.header("The evidence  (P1, p.1239–1243)")

        intro = Text("three blunt numbers back the claim",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # fact 1: shuffled lesions reproduce networks
        f1 = VGroup(
            Text("random / shuffled lesions reproduce published networks",
                 font_size=25, color=WHITE),
            MathTex(r"r = 0.73 \;-\; 0.95", color=BAD).scale(1.1),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.0)
        self.play_beat(FadeIn(f1[0]), Write(f1[1]))                        # beat 2

        # fact 2: 93% variance
        bar = self._variance_bar(0.93).shift(DOWN * 0.5)
        self.play_beat(*[FadeIn(m) for m in bar.submobjects], lag_ratio=0.1)  # beat 3

        # fact 3: 78/102 carry degree
        f3 = MathTex(r"78 \,/\, 102", r"\ \text{maps carry a significant degree trace}")\
            .scale(1.0)
        f3[0].set_color(BAD)
        f3.to_edge(DOWN, buff=1.0)
        f3sub = Text("(P_spin < 0.05;  91 / 102 for P_brainsmash)",
                     font_size=22, color=DIM).next_to(f3, DOWN, buff=0.2)
        self.play_beat(Write(f3), FadeIn(f3sub))                           # beat 4

        # premises -> conclusion
        self.play(FadeOut(VGroup(intro, f1, bar, f3, f3sub)), run_time=0.5)
        chain = VGroup(
            Text("samples one fixed C", font_size=26, color=WHITE),
            Text("↓", font_size=28, color=DIM),
            Text("sampling converges to degree", font_size=26, color=WHITE),
            Text("↓", font_size=28, color=DIM),
            Text("the maps look like degree", font_size=26, color=BAD),
        ).arrange(DOWN, buff=0.18).shift(UP * 0.2)
        self.play_beat(LaggedStart(*[FadeIn(c) for c in chain], lag_ratio=0.2))  # beat 5

        concl = Text("⇒  a large share of published LNM networks are\nnonspecific — may not reflect disease-specific biology",
                     font_size=26, color=RES, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(concl, shift=UP * 0.2))                      # beat 6

    def _variance_bar(self, frac):
        w = 8.0
        full = Rectangle(width=w, height=0.55, stroke_color=WHITE, stroke_width=2,
                         fill_opacity=0)
        filled = Rectangle(width=w * frac, height=0.55, stroke_width=0,
                           fill_color=BAD, fill_opacity=0.85)
        filled.align_to(full, LEFT)
        bar = VGroup(full, filled)
        lab = MathTex(r"93\%", color=BAD).scale(1.0).next_to(full, UP, buff=0.2)
        cap = Text("of LNM-map variance explained by basic connectome properties",
                   font_size=21, color=DIM).next_to(full, DOWN, buff=0.2)
        return VGroup(bar, lab, cap).move_to(ORIGIN)


# ----------------------------------------------------------------------
# Scene 5 — THE SCOPE: the hidden conditional
# ----------------------------------------------------------------------
class S5_Scope(NarratedScene):
    scene_key = "S5_Scope"

    def construct(self):
        self.header("The scope — the hidden conditional")

        head = Text("everything just proved rests on ONE conditional",
                    font_size=28, color=RES).shift(UP * 2.5)
        self.play_beat(FadeIn(head))                                       # beat 1

        cond = VGroup(
            Text("holds for the GROUP-AVERAGE map", font_size=27, color=WHITE),
            Text("under UNIFORM, NON-OVERLAPPING sampling", font_size=27, color=BACK),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.1)
        self.play_beat(FadeIn(cond[0]), FadeIn(cond[1], shift=UP * 0.2))    # beat 2

        why = MathTex("M", r"\to", "I", r"\ \ \Leftarrow\ \ ",
                      r"\text{uniform coverage}").scale(1.0)
        why[0].set_color(VAR); why[2].set_color(EIG)
        why.next_to(cond, DOWN, buff=0.5)
        loose = Text("remove it → the proof goes loose",
                     font_size=24, color=BAD).next_to(why, DOWN, buff=0.3)
        self.play_beat(Write(why), FadeIn(loose))                          # beat 3

        # the rebuttal concedes the math
        self.play(FadeOut(VGroup(head, cond, why, loose)), run_time=0.5)
        reb = Text("Rebuttal (Siddiqi et al., p.5):", font_size=27, color=RES)\
            .shift(UP * 2.4)
        concede = Text("\"...will converge on the row-summation vector of C\n(the degree map). We fully agree with this...\"",
                       font_size=24, color=DIM, line_spacing=0.8)\
            .next_to(reb, DOWN, buff=0.3)
        self.play_beat(FadeIn(reb), FadeIn(concede))                       # beat 4

        # but real lesions overlap & are non-random
        step = Text("\"...but actual lesions causing specific symptoms\noverlap, and their distributions are NOT random.\"",
                    font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(concede, DOWN, buff=0.45)
        self.play_beat(FadeIn(step, shift=UP * 0.2))                       # beat 5

        # structured subset of rows
        subset = MathTex(r"\Rightarrow\ \text{sample only a STRUCTURED subset of rows of } C")\
            .scale(0.85).set_color(BACK).next_to(step, DOWN, buff=0.45)
        goal = Text("which the rebuttal calls the GOAL of LNM — not a flaw",
                    font_size=23, color=BACK).next_to(subset, DOWN, buff=0.25)
        self.play_beat(Write(subset), FadeIn(goal))                        # beat 6

        # average vs contrast — different objects
        self.play(FadeOut(VGroup(reb, concede, step, subset, goal)), run_time=0.5)
        split = VGroup(
            VGroup(
                Text("AVERAGE", font_size=27, color=DIM),
                Text("a description", font_size=23, color=DIM),
            ).arrange(DOWN, buff=0.15),
            MathTex(r"\neq", color=RES).scale(1.4),
            VGroup(
                Text("CONTRAST", font_size=27, color=RES),
                Text("an inference", font_size=23, color=RES),
            ).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=1.0).shift(UP * 1.2)
        diff = Text("a symptom contrast is a DIFFERENT object from the average",
                    font_size=25, color=WHITE).next_to(split, DOWN, buff=0.5)
        self.play_beat(FadeIn(split, lag_ratio=0.2), FadeIn(diff))         # beat 7

        # the data
        data = VGroup(
            Text("same-symptom", font_size=22, color=DIM),
            MathTex("r = 0.44", color=BACK).scale(1.0),
            Text("different-symptom", font_size=22, color=DIM),
            MathTex("r = 0.09", color=DIM).scale(1.0),
            Text("degree map", font_size=22, color=DIM),
            MathTex("r = 0.16", color=BAD).scale(1.0),
        ).arrange_in_grid(rows=3, cols=2, buff=(0.5, 0.22))
        data.next_to(diff, DOWN, buff=0.5)
        self.play_beat(FadeIn(data, lag_ratio=0.1))                        # beat 8


# ----------------------------------------------------------------------
# Scene 6 — entailed vs over-claimed
# ----------------------------------------------------------------------
class S6_EntailedVsOverclaimed(NarratedScene):
    scene_key = "S6_EntailedVsOverclaimed"

    def construct(self):
        self.header("Entailed  vs  over-claimed")

        intro = Text("separate the proof from the over-reach",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # entailed #1
        e1 = VGroup(
            Text("✓ ENTAILED", font_size=24, color=BACK),
            Text("the one-sample average map is backbone-dominated → nonspecific",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 1.5)
        self.play_beat(FadeIn(e1, shift=UP * 0.2))                         # beat 2

        # entailed #2
        e2 = VGroup(
            Text("✓ ENTAILED", font_size=24, color=BACK),
            Text("random, synthetic, real seeds funnel into one cone →",
                 font_size=24, color=WHITE),
            Text("cross-disorder convergence of average maps by construction",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(e1, DOWN, buff=0.45)
        self.play_beat(FadeIn(e2, shift=UP * 0.2))                         # beat 3

        # over-claimed
        self.play(FadeOut(VGroup(intro, e1, e2)), run_time=0.5)
        over = VGroup(
            Text("✗ OVER-CLAIMED", font_size=26, color=BAD),
            Text("\"the average is nonspecific, therefore LNM cannot\nrecover any lesion–symptom relationship\"",
                 font_size=25, color=WHITE, line_spacing=0.8),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.6)
        self.play_beat(FadeIn(over, shift=UP * 0.2))                       # beat 4

        gap = VGroup(
            Text("the average ERASES the difference", font_size=25, color=DIM),
            Text("the contrast under a symptom-label null does NOT", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.25).next_to(over, DOWN, buff=0.5)
        self.play_beat(FadeIn(gap[0]), FadeIn(gap[1], shift=UP * 0.2))      # beat 5

        witness = MathTex(r"t > 10:\quad", r"0\ \text{false positives}",
                          r"\ /\ 1000\ \text{iterations}").scale(1.0)
        witness[1].set_color(RES)
        witness.next_to(gap, DOWN, buff=0.5)
        self.play_beat(Write(witness))                                     # beat 6

        self.play(FadeOut(VGroup(over, gap, witness)), run_time=0.5)
        moral = VGroup(
            Text("The premises are true.", font_size=30, color=WHITE),
            Text("The narrow conclusion is true.", font_size=30, color=WHITE),
            Text("Only the leap to \"LNM is hopeless\" over-shoots the proof.",
                 font_size=30, color=RES),
        ).arrange(DOWN, buff=0.35)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                       # beat 7
