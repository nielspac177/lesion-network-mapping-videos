"""c1003_rebuttal_data — "The rebuttal data".

Five narrated scenes presenting the rebuttal's direct empirical evidence that the
symptom CONTRAST, done right, carries disease-specific signal. Every number is
quoted from:
  responses/lnm_critique/papers/REBUTTAL_sound.md      (the 1090-lesion reanalysis)
  responses/lnm_critique/sections/08_recipe.md          (the decision table, C2/C8)

The load-bearing numbers (REBUTTAL p.3 unless noted):
  same-symptom spatial r = 0.44  vs  different-symptom r = 0.09   (p < 0.0001)
  same-symptom r = 0.44          vs  degree-map r = 0.16          (p < 0.0001)
  0 false positives / 1000 iterations at sensitivity 75%, specificity t > 10
  4.6% of permutations only at the lenient t = 3.0
  Petersen et al. (refs 4,14; recipe C2): 2,950-patient label-permutation
      recovers DISTINCT networks for distinct symptoms

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c1003_rebuttal_data ./render.sh \
      chapters/c1003_rebuttal_data/scenes.py -q ql \
      S1_Setup S2_Correlations S3_FalsePositives S4_Petersen S5_Weight
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — what would prove signal exists: the falsifiable test
# ----------------------------------------------------------------------
class S1_Setup(NarratedScene):
    scene_key = "S1_Setup"

    def construct(self):
        self.header("What would prove signal exists")

        # beat 1 — concede the average result up front
        avg = MathTex(r"\text{average map}", r"\;\longrightarrow\;", r"\deg(C)")\
            .scale(1.0).shift(UP * 2.3)
        avg[0].set_color(DIM); avg[2].set_color(BAD)
        avg_cap = Text("conceded: uniform random lesions rebuild the backbone",
                       font_size=22, color=DIM).next_to(avg, DOWN, buff=0.25)
        self.play_beat(Write(avg), FadeIn(avg_cap))                        # beat 1

        # beat 2 — but the signal lives in the contrast, not the average
        self.play(FadeOut(VGroup(avg, avg_cap)), run_time=0.4)
        live = VGroup(
            Text("the disease signal lives in the CONTRAST,",
                 font_size=28, color=WHITE),
            Text("not in the average", font_size=28, color=RES),
        ).arrange(DOWN, buff=0.2).shift(UP * 2.1)
        self.play_beat(FadeIn(live, shift=UP * 0.2))                       # beat 2

        # beat 3 — define the contrast
        contrast = MathTex(
            r"\text{contrast}", "=",
            r"\underbrace{\text{maps}_{\text{symptom A}}}_{\text{same symptom}}",
            "-",
            r"\underbrace{\text{maps}_{\text{symptom B}}}_{\text{control}}",
        ).scale(0.85).next_to(live, DOWN, buff=0.6)
        contrast[0].set_color(VAR); contrast[2].set_color(VAR)
        contrast[4].set_color(DIM)
        self.play_beat(Write(contrast))                                    # beat 3

        # beat 4 — set up the falsifiable test
        self.play(FadeOut(VGroup(live, contrast)), run_time=0.4)
        test = VGroup(
            Text("The falsifiable test", font_size=30, color=RES),
            Text("if the contrast carries disease-specific signal,",
                 font_size=25, color=WHITE),
            Text("two inequalities must hold:", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.22).shift(UP * 1.9)
        self.play_beat(FadeIn(test, lag_ratio=0.2))                        # beat 4

        # beat 5 — inequality one: same > different
        ineq1 = MathTex(r"r_{\text{same}}", ">", r"r_{\text{different}}")\
            .scale(1.15).next_to(test, DOWN, buff=0.55)
        ineq1[0].set_color(BACK); ineq1[2].set_color(DIM)
        ineq1_cap = Text("same-symptom maps agree more than different-symptom maps",
                         font_size=22, color=DIM).next_to(ineq1, DOWN, buff=0.2)
        self.play_beat(Write(ineq1), FadeIn(ineq1_cap))                    # beat 5

        # beat 6 — inequality two: same > degree
        ineq2 = MathTex(r"r_{\text{same}}", ">", r"r_{\text{degree}}")\
            .scale(1.15).next_to(ineq1_cap, DOWN, buff=0.45)
        ineq2[0].set_color(BACK); ineq2[2].set_color(BAD)
        ineq2_cap = Text("and agree more than they do with the backbone everyone shares",
                         font_size=22, color=DIM).next_to(ineq2, DOWN, buff=0.2)
        self.play_beat(Write(ineq2), FadeIn(ineq2_cap))                    # beat 6

        # beat 7 — what passing both means
        moral = Text("both hold  ⇒  similarity-to-backbone is not the whole story",
                     font_size=24, color=RES).next_to(ineq2_cap, DOWN, buff=0.4)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7

        # beat 8 — name the metric (the critique's own)
        self.play(FadeOut(VGroup(test, ineq1, ineq1_cap, ineq2, ineq2_cap, moral)),
                  run_time=0.5)
        metric = VGroup(
            Text("Metric throughout:", font_size=28, color=WHITE),
            MathTex(r"r = \text{spatial Pearson correlation}").scale(1.0),
            Text("between unthresholded whole-brain maps", font_size=24, color=DIM),
            Text("(the critique's own preferred measure)", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.25)
        metric[1].set_color(VAR)
        self.play_beat(FadeIn(metric, lag_ratio=0.2))                      # beat 8


# ----------------------------------------------------------------------
# Scene 2 — the correlation numbers: 0.44 vs 0.09 vs 0.16
# ----------------------------------------------------------------------
class S2_Correlations(NarratedScene):
    scene_key = "S2_Correlations"

    def construct(self):
        self.header("The correlation numbers  (REBUTTAL p.3)")

        # beat 1 — the database
        db = VGroup(
            Text("1090 lesion locations", font_size=30, color=VAR),
            Text("causing 34 different symptoms", font_size=26, color=DIM),
            Text("from 34 prior LNM studies", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.2).shift(UP * 2.4)
        self.play_beat(FadeIn(db, lag_ratio=0.2))                          # beat 1

        # beat 2 — set up the three-bar chart frame
        self.play(db.animate.scale(0.55).to_edge(UP, buff=1.0), run_time=0.5)
        axis = Line(LEFT * 5.2 + DOWN * 2.4, RIGHT * 5.2 + DOWN * 2.4,
                    color=DIM, stroke_width=2)
        intro = Text("three spatial correlations — watch which bar wins",
                     font_size=24, color=DIM).next_to(axis, DOWN, buff=0.2)
        self.play_beat(Create(axis), FadeIn(intro))                        # beat 2

        # geometry for the bars: r is in [0,1]; map to height (max 4.0 units)
        base_y = -2.4
        scale_h = 4.0

        def bar(value, color, xshift, toplabel, botlabel):
            h = value * scale_h
            rect = Rectangle(width=1.6, height=h, stroke_width=2,
                             stroke_color=color, fill_color=color, fill_opacity=0.6)
            rect.move_to([xshift, base_y + h / 2, 0])
            val = MathTex(f"r = {value:.2f}", color=color).scale(0.85)\
                .next_to(rect, UP, buff=0.15)
            top = Text(toplabel, font_size=22, color=color)\
                .next_to(val, UP, buff=0.12)
            bot = Text(botlabel, font_size=20, color=DIM)\
                .next_to(rect, DOWN, buff=0.2)
            return VGroup(rect, val, top, bot)

        # beat 3 — same-symptom bar (the tall winner)
        b_same = bar(0.44, BACK, -3.4, "same-symptom", "maps of SAME symptom")
        self.play_beat(GrowFromEdge(b_same[0], DOWN), FadeIn(b_same[1]),
                       FadeIn(b_same[2]), FadeIn(b_same[3]))               # beat 3

        # beat 4 — different-symptom bar
        b_diff = bar(0.09, DIM, 0.0, "different-symptom", "maps of DIFFERENT symptoms")
        self.play_beat(GrowFromEdge(b_diff[0], DOWN), FadeIn(b_diff[1]),
                       FadeIn(b_diff[2]), FadeIn(b_diff[3]))               # beat 4

        # beat 5 — degree-map bar
        b_deg = bar(0.16, BAD, 3.4, "degree map", "same-symptom vs degree")
        self.play_beat(GrowFromEdge(b_deg[0], DOWN), FadeIn(b_deg[1]),
                       FadeIn(b_deg[2]), FadeIn(b_deg[3]))                 # beat 5

        # beat 6 — assertion 1 verdict
        v1 = MathTex("0.44", ">", "0.09", r",\ \ p < 0.0001").scale(0.95)
        v1[0].set_color(BACK); v1[2].set_color(DIM); v1[3].set_color(RES)
        v1.shift(UP * 1.4 + RIGHT * 2.0)
        v1cap = Text("same  >  different", font_size=20, color=WHITE)\
            .next_to(v1, UP, buff=0.12)
        self.play_beat(Write(v1), FadeIn(v1cap))                          # beat 6

        # beat 7 — assertion 2 verdict
        v2 = MathTex("0.44", ">", "0.16", r",\ \ p < 0.0001").scale(0.95)
        v2[0].set_color(BACK); v2[2].set_color(BAD); v2[3].set_color(RES)
        v2.next_to(v1, DOWN, buff=0.55)
        v2cap = Text("same  >  degree", font_size=20, color=WHITE)\
            .next_to(v2, UP, buff=0.12)
        self.play_beat(Write(v2), FadeIn(v2cap))                          # beat 7

        # beat 8 — moral
        self.play(FadeOut(VGroup(v1, v1cap, v2, v2cap, intro)), run_time=0.4)
        moral = Text("the surviving signal is symptom-specific,\nnot just the backbone showing through",
                     font_size=26, color=RES, line_spacing=0.8)\
            .shift(UP * 1.3 + RIGHT * 2.2)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 8


# ----------------------------------------------------------------------
# Scene 3 — error control holds: 0 / 1000 at t > 10
# ----------------------------------------------------------------------
class S3_FalsePositives(NarratedScene):
    scene_key = "S3_FalsePositives"

    def construct(self):
        self.header("Error control holds  (REBUTTAL p.3)")

        # beat 1 — the skeptic's worry
        worry = VGroup(
            Text("The skeptic's worry:", font_size=28, color=BAD),
            Text("maybe the method just fires too easily,",
                 font_size=25, color=WHITE),
            Text("so even a real difference proves nothing.",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 2.2)
        self.play_beat(FadeIn(worry, lag_ratio=0.2))                      # beat 1

        # beat 2 — the FPR procedure
        self.play(FadeOut(worry), run_time=0.4)
        proc = VGroup(
            Text("False-positive-rate test", font_size=28, color=WHITE),
            MathTex(r"50\ \text{random lesions}", r"\ \ \text{vs}\ \ ",
                    r"\text{the remaining}\ 1040").scale(0.85),
        ).arrange(DOWN, buff=0.3).shift(UP * 2.1)
        proc[1][0].set_color(VAR); proc[1][2].set_color(DIM)
        self.play_beat(FadeIn(proc[0]), Write(proc[1]))                   # beat 2

        # beat 3 — the thresholds and iteration count
        thr = MathTex(r"\text{sensitivity } 75\%", r",\quad",
                      r"\text{specificity } t > 10", r",\quad",
                      r"1000\ \text{iterations}").scale(0.8)
        thr[0].set_color(EIG); thr[2].set_color(EIG); thr[4].set_color(DIM)
        thr.next_to(proc, DOWN, buff=0.5)
        thr_cap = Text("the critique's own thresholds", font_size=22, color=DIM)\
            .next_to(thr, DOWN, buff=0.2)
        self.play_beat(Write(thr), FadeIn(thr_cap))                       # beat 3

        # beat 4 — the headline result: 0 / 1000
        self.play(FadeOut(VGroup(proc, thr, thr_cap)), run_time=0.4)
        headline = MathTex(r"t > 10:\quad", r"0", r"\ \text{false positives}",
                           r"\ /\ ", r"1000\ \text{iterations}").scale(1.15)
        headline[1].set_color(RES); headline[2].set_color(RES)
        headline.shift(UP * 1.4)
        box = SurroundingRectangle(headline, color=RES, buff=0.25)
        not_one = Text("not a single one", font_size=24, color=RES)\
            .next_to(box, DOWN, buff=0.3)
        self.play_beat(Write(headline), Create(box), FadeIn(not_one))     # beat 4

        # beat 5 — only at a loosened threshold
        loose = MathTex(r"\text{false positives only at}\quad", r"t = 3.0")\
            .scale(0.95).next_to(not_one, DOWN, buff=0.6)
        loose[1].set_color(BAD)
        loose_cap = Text("far below normal LNM practice", font_size=22, color=DIM)\
            .next_to(loose, DOWN, buff=0.2)
        self.play_beat(Write(loose), FadeIn(loose_cap))                   # beat 5

        # beat 6 — and even there only 4.6%
        rate = MathTex(r"\text{and even then only}\quad", r"4.6\%",
                       r"\ \text{of permutations}").scale(0.95)
        rate[1].set_color(BAD)
        rate.next_to(loose_cap, DOWN, buff=0.4)
        self.play_beat(Write(rate))                                       # beat 6

        # beat 7 — moral: the symptom null controls error
        self.play(FadeOut(VGroup(headline, box, not_one, loose, loose_cap, rate)),
                  run_time=0.5)
        moral = VGroup(
            Text("the symptom null controls error", font_size=30, color=RES),
            Text("the specificity step keeps the nonspecific backbone —",
                 font_size=24, color=WHITE),
            Text("including degree — from leaking through", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.25)
        self.play_beat(FadeIn(moral, lag_ratio=0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 4 — the Petersen replication: 2,950 patients, distinct networks
# ----------------------------------------------------------------------
class S4_Petersen(NarratedScene):
    scene_key = "S4_Petersen"

    def construct(self):
        self.header("The Petersen replication  (recipe C2; refs 4,14)")

        # beat 1 — one database could be a fluke
        fluke = VGroup(
            Text("one database could be a fluke", font_size=28, color=DIM),
            Text("the strongest support is an independent,",
                 font_size=25, color=WHITE),
            Text("much larger replication", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 2.2)
        self.play_beat(FadeIn(fluke, lag_ratio=0.2))                      # beat 1

        # beat 2 — name the source
        self.play(FadeOut(fluke), run_time=0.4)
        who = VGroup(
            Text("Petersen et al.", font_size=32, color=BACK),
            Text("source of the raw-data permutation method,",
                 font_size=24, color=DIM),
            Text("cited by the rebuttal (refs 4, 14)", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.2).shift(UP * 2.1)
        self.play_beat(FadeIn(who, lag_ratio=0.2))                        # beat 2

        # beat 3 — the label-permutation method
        self.play(who.animate.scale(0.6).to_edge(UP, buff=1.0), run_time=0.5)
        perm = VGroup(
            Text("Label permutation", font_size=28, color=WHITE),
            MathTex(r"\text{shuffle: patient's symptom}",
                    r"\;\leftrightarrow\;",
                    r"\text{another patient's map}").scale(0.8),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.9)
        perm[1][0].set_color(EIG); perm[1][2].set_color(VAR)
        self.play_beat(FadeIn(perm[0]), Write(perm[1]))                   # beat 3

        # beat 4 — why shuffling labels holds the backbone fixed
        why = MathTex(r"\text{backbone}", r"\ \text{identical in}\ ",
                      r"\text{real}", r"\ \text{and}\ ", r"\text{shuffled}")\
            .scale(0.85).next_to(perm, DOWN, buff=0.5)
        why[0].set_color(BAD); why[2].set_color(WHITE); why[4].set_color(DIM)
        why_cap = Text("so the backbone cancels and cannot fake a result",
                       font_size=22, color=DIM).next_to(why, DOWN, buff=0.2)
        self.play_beat(Write(why), FadeIn(why_cap))                       # beat 4

        # beat 5 — the scale
        self.play(FadeOut(VGroup(perm, why, why_cap)), run_time=0.4)
        scale = VGroup(
            MathTex(r"2{,}950", r"\ \text{patients}").scale(1.3),
            Text("an order of magnitude beyond the original test",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.35).shift(UP * 1.0)
        scale[0][0].set_color(RES)
        self.play_beat(FadeIn(scale[0], scale=1.2), FadeIn(scale[1]))     # beat 5

        # beat 6 — the result: distinct networks
        result = VGroup(
            Text("distinct symptoms", font_size=27, color=VAR),
            MathTex(r"\longrightarrow", color=DIM).scale(1.0),
            Text("distinct networks", font_size=27, color=BACK),
        ).arrange(RIGHT, buff=0.45).next_to(scale, DOWN, buff=0.7)
        not_one = Text("not a single shared hub map", font_size=24, color=RES)\
            .next_to(result, DOWN, buff=0.3)
        self.play_beat(FadeIn(result, lag_ratio=0.2), FadeIn(not_one))    # beat 6

        # beat 7 — moral
        self.play(FadeOut(VGroup(scale, result, not_one)), run_time=0.4)
        moral = Text("large-scale, independent evidence:\nthe contrast separates one symptom's circuit from another's",
                     font_size=26, color=RES, line_spacing=0.85).shift(UP * 0.6)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 7


# ----------------------------------------------------------------------
# Scene 5 — weighing it: what the data does and does not do
# ----------------------------------------------------------------------
class S5_Weight(NarratedScene):
    scene_key = "S5_Weight"

    def construct(self):
        self.header("Weighing it")

        # beat 1 — set up the balance
        head = Text("weigh what this data does — and does not — do",
                    font_size=28, color=WHITE).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                      # beat 1

        # beat 2 — what it does (the support)
        does = VGroup(
            Text("✓  DOES", font_size=26, color=BACK),
            Text("direct empirical support for the rebuttal's claim:",
                 font_size=24, color=WHITE),
            Text("the contrast, done right, is specific",
                 font_size=24, color=BACK),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 1.3)
        self.play_beat(FadeIn(does, shift=UP * 0.2))                      # beat 2

        # beat 3 — the existence proof, numbers recalled
        proof = MathTex(r"r_{\text{same}} = 0.44", r"\ >\ ",
                        r"0.09,\ 0.16", r";\quad", r"0/1000\ \text{FP}")\
            .scale(0.85).next_to(does, DOWN, buff=0.45)
        proof[0].set_color(BACK); proof[2].set_color(DIM); proof[4].set_color(RES)
        proof_cap = Text("a real existence proof", font_size=22, color=DIM)\
            .next_to(proof, DOWN, buff=0.2)
        self.play_beat(Write(proof), FadeIn(proof_cap))                   # beat 3

        # beat 4 — what it does NOT do: P1 average result stands
        self.play(FadeOut(VGroup(head, does, proof, proof_cap)), run_time=0.5)
        not1 = VGroup(
            Text("✗  does NOT erase P1", font_size=26, color=BAD),
            Text("the group-average map, under uniform sampling,",
                 font_size=24, color=WHITE),
            Text("really does converge to degree", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 1.7)
        self.play_beat(FadeIn(not1, shift=UP * 0.2))                      # beat 4

        # beat 5 — does NOT touch P3 biological ceiling
        not3 = VGroup(
            Text("✗  does NOT touch P3", font_size=26, color=BAD),
            Text("a static connectome is still blind",
                 font_size=24, color=WHITE),
            Text("to dynamic reorganization", font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(not1, DOWN, buff=0.5)
        self.play_beat(FadeIn(not3, shift=UP * 0.2))                      # beat 5

        # beat 6 — the question it actually answers
        self.play(FadeOut(VGroup(not1, not3)), run_time=0.5)
        q = VGroup(
            Text("the question it answers is prior:", font_size=27, color=DIM),
            Text("“can the contrast EVER recover", font_size=27, color=WHITE),
            Text("disease-specific signal?”", font_size=27, color=WHITE),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.4)
        self.play_beat(FadeIn(q, lag_ratio=0.2))                          # beat 6

        # beat 7 — the answer: yes
        ans = Text("YES — it can", font_size=40, color=RES)\
            .next_to(q, DOWN, buff=0.5)
        line = Text("the average erases the difference;\nthe contrast, under a symptom null, does not",
                    font_size=24, color=WHITE, line_spacing=0.85)\
            .next_to(ans, DOWN, buff=0.4)
        self.play_beat(FadeIn(ans, scale=1.2), FadeIn(line))              # beat 7
