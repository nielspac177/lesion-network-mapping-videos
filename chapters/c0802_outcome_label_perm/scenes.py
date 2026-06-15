"""c0802_outcome_label_perm — "Move 1: outcome-label permutation".

Five narrated scenes. The single-target (FUS thalamotomy) defeat, Move 1. Each
patient's map splits as m_i = C l_0 + C delta_i. We test whether the patient-
specific part C delta_i relates to the clinical outcome y_i, by permuting the
outcomes (the shared map C l_0 is held fixed and cancels) with Freedman-Lane
protecting the lesion-size nuisance s_i. The test is exact under exchangeability.

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/06_single_target.md
  responses/lnm_critique/sections/03_the_right_null.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0802_outcome_label_perm ./render.sh \
      chapters/c0802_outcome_label_perm/scenes.py -q ql \
      S1_Goal S2_Permute S3_SizeProtect S4_Valid S5_Takeaway
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the goal: does the per-patient map relate to outcome?
# ----------------------------------------------------------------------
class S1_Goal(NarratedScene):
    scene_key = "S1_Goal"

    def construct(self):
        self.header("Test the outcome-map link")

        title = Text("Move 1: one clean question", font_size=40, color=WHITE)
        sub = Text("a valid answer, even with a single tiny target",
                   font_size=24, color=DIM).next_to(title, DOWN, buff=0.3)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(FadeOut(VGroup(title, sub)), run_time=0.5)

        # the question
        q = VGroup(
            Text("Does each patient's lesion map", font_size=30, color=WHITE),
            Text("relate to the clinical outcome?", font_size=30, color=RES),
            Text("(tremor relief after thalamotomy)", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.22)
        self.play_beat(FadeIn(q, lag_ratio=0.3))                           # beat 2
        self.play(FadeOut(q), run_time=0.4)

        # define y_i
        ydef = MathTex("y_i", r"\ :\ ", r"\text{patient } i\text{'s outcome}")\
            .scale(1.2).shift(UP * 1.6)
        ydef[0].set_color(EIG)
        ybr = Brace(ydef[0], DOWN, color=EIG)
        ylab = Text("binary (relief / none)  or  a graded score",
                    font_size=23, color=EIG).next_to(ybr, DOWN, buff=0.2)
        self.play_beat(Write(ydef), GrowFromCenter(ybr), FadeIn(ylab))     # beat 3
        self.play(FadeOut(VGroup(ybr, ylab)), run_time=0.4)

        # define m_i = C l_i
        mdef = MathTex("m_i", "=", "C", r"\ell_i").scale(1.4).shift(DOWN * 0.2)
        mdef[0].set_color(VAR); mdef[2].set_color(WHITE); mdef[3].set_color(VAR)
        mbr = Brace(mdef, DOWN, color=DIM)
        mlab = Text("the lesion  ℓᵢ  pushed through the connectome C",
                    font_size=23, color=DIM).next_to(mbr, DOWN, buff=0.2)
        self.play_beat(Write(mdef), GrowFromCenter(mbr), FadeIn(mlab))     # beat 4
        self.play(FadeOut(VGroup(ydef, mbr, mlab)),
                  mdef.animate.scale(0.8).to_edge(UP, buff=1.1), run_time=0.5)

        # the split: m_i = C l_0 + C delta_i, annotate shared term
        split = MathTex("m_i", "=", "C", r"\ell_0", "+", "C", r"\delta_i")\
            .scale(1.3).shift(UP * 0.3)
        split[0].set_color(VAR)
        for k in (2, 5):
            split[k].set_color(WHITE)
        split[3].set_color(BACK); split[6].set_color(VAR)
        shared_br = Brace(split[2:4], DOWN, color=BACK)
        shared_lab = Text("shared VIM fingerprint\nidentical for every patient",
                          font_size=22, color=BACK, line_spacing=0.8)\
            .next_to(shared_br, DOWN, buff=0.2)
        self.play_beat(Write(split), GrowFromCenter(shared_br),
                       FadeIn(shared_lab))                                 # beat 5

        # annotate patient-specific term
        self.play(FadeOut(VGroup(shared_br, shared_lab)), run_time=0.4)
        ps_br = Brace(split[5:7], DOWN, color=VAR)
        ps_lab = Text("small patient-specific part\nsize + within-target position",
                      font_size=22, color=VAR, line_spacing=0.8)\
            .next_to(ps_br, DOWN, buff=0.2)
        self.play_beat(GrowFromCenter(ps_br), FadeIn(ps_lab))             # beat 6

        # the moral: signal lives in C delta_i
        self.play(FadeOut(VGroup(ps_br, ps_lab)), run_time=0.4)
        moral = Text("Genuine outcome signal can only live in  C δᵢ .",
                     font_size=27, color=RES).next_to(split, DOWN, buff=0.9)
        moral_box = SurroundingRectangle(moral, color=RES, buff=0.22)
        self.play_beat(FadeIn(moral, shift=UP * 0.2), Create(moral_box))  # beat 7


# ----------------------------------------------------------------------
# Scene 2 — permute the outcomes; the shared map is held fixed
# ----------------------------------------------------------------------
class S2_Permute(NarratedScene):
    scene_key = "S2_Permute"

    def construct(self):
        self.header("Permute the outcomes")

        # rows of (map, outcome)
        rows = VGroup()
        outs = ["1", "0", "1", "0"]
        for i in range(4):
            m = MathTex(f"m_{i+1}", color=VAR).scale(0.9)
            link = MathTex(r"\sim", color=DIM).scale(0.9)
            y = MathTex(f"y_{i+1}", "=", outs[i]).scale(0.9)
            y[0].set_color(EIG); y[2].set_color(EIG)
            row = VGroup(m, link, y).arrange(RIGHT, buff=0.4)
            rows.add(row)
        rows.arrange(DOWN, buff=0.35).shift(LEFT * 2.2)
        keepcap = Text("keep every map fixed;\nreassign the outcomes",
                       font_size=23, color=WHITE, line_spacing=0.8)\
            .shift(RIGHT * 3.3)
        self.play_beat(FadeIn(rows, lag_ratio=0.2), FadeIn(keepcap))      # beat 1

        # shuffle the outcomes
        shuffled = ["0", "1", "0", "1"]
        anims = []
        for i, row in enumerate(rows.submobjects):
            ynew = MathTex(f"y_{i+1}", "=", shuffled[i]).scale(0.9)\
                .move_to(row.submobjects[2])
            ynew[0].set_color(EIG); ynew[2].set_color(BAD)
            anims.append(Transform(row.submobjects[2], ynew))
        self.play_beat(*anims, lag_ratio=0.15)                            # beat 2
        self.play(FadeOut(VGroup(rows, keepcap)), run_time=0.5)

        # recompute association, many times -> must beat the shuffles
        rule = VGroup(
            Text("recompute the map–outcome association each shuffle",
                 font_size=26, color=WHITE),
            Text("real association is meaningful only if it",
                 font_size=25, color=DIM),
            Text("beats almost every shuffled one", font_size=25, color=RES),
        ).arrange(DOWN, buff=0.25)
        self.play_beat(FadeIn(rule, lag_ratio=0.3))                       # beat 3
        self.play(FadeOut(rule), run_time=0.4)

        # the contrast with the shared term shown
        eq = MathTex(r"t_v", r"\ \propto\ ",
                     r"\big(\bar\beta^{(1)}-\bar\beta^{(0)}\big)\,u_{1,v}",
                     "+",
                     r"\big(\bar r^{(1)}-\bar r^{(0)}\big)")\
            .scale(0.95).shift(UP * 0.6)
        eq[2].set_color(BACK); eq[4].set_color(VAR)
        cap = Text("tᵥ : the impaired-vs-spared contrast at voxel v",
                   font_size=22, color=DIM).next_to(eq, UP, buff=0.3)
        sh_br = Brace(eq[2], DOWN, color=BACK)
        sh_lab = Text("shared backbone:  C ℓ₀ ,  the same in every map",
                      font_size=22, color=BACK).next_to(sh_br, DOWN, buff=0.2)
        ps_br = Brace(eq[4], DOWN, color=VAR)
        ps_lab = Text("residual: the C δᵢ part",
                      font_size=20, color=VAR).next_to(ps_br, DOWN, buff=0.12)
        self.play_beat(FadeIn(cap), Write(eq), GrowFromCenter(sh_br),
                       FadeIn(sh_lab), GrowFromCenter(ps_br),
                       FadeIn(ps_lab))                                     # beat 4

        # shuffling never moves it -> same on both sides
        same = Text("Shuffling outcomes never moves  C ℓ₀ :",
                    font_size=25, color=WHITE).next_to(sh_lab, DOWN, buff=0.5)
        same2 = Text("identical in the real statistic and in every null statistic",
                     font_size=24, color=DIM).next_to(same, DOWN, buff=0.2)
        self.play_beat(FadeIn(same), FadeIn(same2))                       # beat 5

        # it cancels
        self.play(FadeOut(VGroup(cap, eq, sh_br, sh_lab, ps_br, ps_lab,
                                 same, same2)), run_time=0.5)
        cancel = MathTex(r"\bar\beta^{(1)}-\bar\beta^{(0)}",
                         r"\ \longrightarrow\ ", r"\text{same on both sides}",
                         r"\ \Rightarrow\ ", r"0\ \text{leverage}")\
            .scale(1.0).shift(UP * 0.3)
        cancel[0].set_color(BACK); cancel[4].set_color(RES)
        cbox = SurroundingRectangle(cancel, color=RES, buff=0.22)
        cmsg = Text("the shared map cancels — it cannot fake an association",
                    font_size=25, color=WHITE).next_to(cbox, DOWN, buff=0.4)
        self.play_beat(Write(cancel), Create(cbox), FadeIn(cmsg))         # beat 6

        # same cancellation as ch5
        self.play(FadeOut(VGroup(cancel, cbox, cmsg)), run_time=0.4)
        callback = VGroup(
            Text("Same cancellation we proved for the scattered case",
                 font_size=26, color=WHITE),
            Text("(chapter 5).  Nothing about it needed scattered lesions.",
                 font_size=26, color=DIM),
        ).arrange(DOWN, buff=0.25)
        self.play_beat(FadeIn(callback, lag_ratio=0.3))                   # beat 7


# ----------------------------------------------------------------------
# Scene 3 — Freedman-Lane protects size
# ----------------------------------------------------------------------
class S3_SizeProtect(NarratedScene):
    scene_key = "S3_SizeProtect"

    def construct(self):
        self.header("Freedman–Lane protects size")

        head = Text("One more nuisance — and here the dangerous one:",
                    font_size=28, color=WHITE).shift(UP * 2.4)
        sizecorr = Text("lesion size correlates with outcome",
                        font_size=28, color=BAD).next_to(head, DOWN, buff=0.3)
        self.play_beat(FadeIn(head), FadeIn(sizecorr, shift=UP * 0.2))    # beat 1

        # define s_i
        sdef = MathTex("s_i", "=", r"\mathbf{1}^\top", r"\ell_i")\
            .scale(1.3).shift(UP * 0.6)
        sdef[0].set_color(BAD)
        sdef[2].set_color(WHITE); sdef[3].set_color(VAR)
        sbr = Brace(sdef, DOWN, color=BAD)
        slab = Text("lesion size: the count of destroyed voxels\n(the number of ones in ℓᵢ)",
                    font_size=22, color=BAD, line_spacing=0.8)\
            .next_to(sbr, DOWN, buff=0.2)
        self.play_beat(Write(sdef), GrowFromCenter(sbr), FadeIn(slab))    # beat 2

        # size IS most of delta_i
        self.play(FadeOut(VGroup(head, sizecorr, sbr, slab)),
                  sdef.animate.scale(0.75).to_edge(UP, buff=1.1), run_time=0.5)
        dom = VGroup(
            Text("In a single target,  size is most of what  δᵢ  is.",
                 font_size=27, color=WHITE),
            Text("It is the principal confound AND the principal source of variance.",
                 font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.6)
        self.play_beat(FadeIn(dom, lag_ratio=0.3))                        # beat 3

        # naive shuffle fails
        naive = Text("A raw shuffle of the outcome is not enough —\n"
                     "it scrambles the size effect and the map effect together.",
                     font_size=25, color=DIM, line_spacing=0.8)\
            .next_to(dom, DOWN, buff=0.6)
        self.play_beat(FadeIn(naive, shift=UP * 0.2))                     # beat 4
        self.play(FadeOut(VGroup(dom, naive)), run_time=0.5)

        # the GLM
        glm = MathTex("y_i", "=", r"\beta\,", "m_i(v)", "+", r"\gamma\,", "s_i",
                      "+", r"(\text{nuisance})", "+", r"\varepsilon_i")\
            .scale(1.0).shift(UP * 1.5)
        glm[0].set_color(EIG); glm[2].set_color(RES); glm[3].set_color(VAR)
        glm[5].set_color(RES); glm[6].set_color(BAD)
        # annotate the estimand and the two protected terms within the beat
        beta_br = Brace(glm[2:4], DOWN, color=RES)
        beta_lab = Text("β: the outcome–map link  (test H₀: β = 0)\n"
                        "mᵢ(v): the map at voxel v   εᵢ: noise",
                        font_size=21, color=DIM, line_spacing=0.8)\
            .next_to(beta_br, DOWN, buff=0.18)
        self.play_beat(Write(glm), GrowFromCenter(beta_br),
                       FadeIn(beta_lab))                                   # beat 5
        self.play(FadeOut(VGroup(beta_br, beta_lab)), run_time=0.3)

        # Freedman-Lane steps
        steps = VGroup(
            Text("Freedman–Lane:", font_size=26, color=RES),
            Text("1.  regress  y  on the nuisances (size, age, severity)",
                 font_size=24, color=WHITE),
            Text("2.  keep the residuals", font_size=24, color=WHITE),
            Text("3.  permute residuals, add back, refit",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(glm, DOWN, buff=0.5)
        self.play_beat(FadeIn(steps, lag_ratio=0.25))                     # beat 6

        # both held fixed -> only the link is tested
        self.play(FadeOut(VGroup(glm, steps)), run_time=0.5)
        held = VGroup(
            MathTex(r"C\ell_0", r"\ \text{fixed}\qquad", r"\gamma\, s_i",
                    r"\ \text{fixed}").scale(1.1),
            Text("the shuffle disturbs only the outcome–map link",
                 font_size=26, color=RES),
            Text("— that, and nothing else, is tested", font_size=26, color=RES),
        ).arrange(DOWN, buff=0.35)
        held[0][0].set_color(BACK); held[0][2].set_color(BAD)
        self.play_beat(FadeIn(held, lag_ratio=0.3))                       # beat 7


# ----------------------------------------------------------------------
# Scene 4 — why it is valid here
# ----------------------------------------------------------------------
class S4_Valid(NarratedScene):
    scene_key = "S4_Valid"

    def construct(self):
        self.header("Why it is valid here")

        head = Text("Valid even with one target and N in the tens — two reasons:",
                    font_size=27, color=WHITE).shift(UP * 2.5)
        self.play_beat(FadeIn(head))                                      # beat 1

        # reason 1: exchangeability
        exch = MathTex(r"H_0^{\text{sym}}:", r"\ \ (y_1,\dots,y_n)",
                       r"\ \text{exchangeable given fixed}", r"\ (m_1,\dots,m_n)")\
            .scale(0.85).shift(UP * 1.3)
        exch[1].set_color(EIG); exch[3].set_color(VAR)
        self.play_beat(Write(exch))                                       # beat 2

        # exactness
        exact = MathTex(r"\Pr(p \le \alpha)", r"\ \le\ ", r"\alpha")\
            .scale(1.2).shift(UP * 0.2)
        exact[0].set_color(WHITE); exact[2].set_color(RES)
        excap = Text("permutation exactness (chapter 5): counting labelings,\n"
                     "no distributional assumption, finite samples",
                     font_size=23, color=DIM, line_spacing=0.8)\
            .next_to(exact, DOWN, buff=0.3)
        self.play_beat(Write(exact), FadeIn(excap))                       # beat 3

        # ugly maps OK
        ugly = Text("Exactness does not care the maps are ugly, low-rank,\n"
                    "or backbone-dominated — only that labels are exchangeable.",
                    font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(excap, DOWN, buff=0.45)
        self.play_beat(FadeIn(ugly, shift=UP * 0.2))                      # beat 4
        self.play(FadeOut(VGroup(head, exch, exact, excap, ugly)),
                  run_time=0.5)

        # reason 2: the two cheaters controlled
        ctrl = VGroup(
            Text("The two things that could cheat are controlled:",
                 font_size=27, color=WHITE),
            Text("•  the shared backbone  C ℓ₀  cancels",
                 font_size=26, color=BACK),
            Text("•  the size effect is held fixed by Freedman–Lane",
                 font_size=26, color=BAD),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).shift(UP * 0.9)
        self.play_beat(FadeIn(ctrl, lag_ratio=0.3))                       # beat 5

        # single target makes it cleaner
        cleaner = Text("The single target makes the test cleaner, not weaker:\n"
                       "one location, not a confusing scatter.",
                       font_size=25, color=RES, line_spacing=0.8)\
            .next_to(ctrl, DOWN, buff=0.5)
        self.play_beat(FadeIn(cleaner, shift=UP * 0.2))                   # beat 6

        # the answerable question
        self.play(FadeOut(VGroup(ctrl, cleaner)), run_time=0.4)
        ans = VGroup(
            Text("Exactly answerable:", font_size=27, color=WHITE),
            Text("given these fixed lesions, does the outcome track",
                 font_size=25, color=DIM),
            Text("the patient-specific connectivity more than chance?",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.22)
        self.play_beat(FadeIn(ans, lag_ratio=0.3))                        # beat 7


# ----------------------------------------------------------------------
# Scene 5 — takeaway
# ----------------------------------------------------------------------
class S5_Takeaway(NarratedScene):
    scene_key = "S5_Takeaway"

    def construct(self):
        self.header("Takeaway")

        head = Text("Move 1, in one breath:", font_size=32, color=WHITE)\
            .shift(UP * 2.6)
        line = Text("a single-target study → a valid inference about outcome",
                    font_size=27, color=RES).next_to(head, DOWN, buff=0.3)
        self.play_beat(FadeIn(head), FadeIn(line, shift=UP * 0.2))        # beat 1

        # shuffle -> shared map drops out
        p1 = VGroup(
            Text("Shuffle the outcomes;", font_size=26, color=WHITE),
            Text("the shared map  C ℓ₀ , being label-independent,",
                 font_size=25, color=BACK),
            Text("drops out of the contrast.", font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.18).shift(UP * 0.6)
        self.play_beat(FadeIn(p1, lag_ratio=0.25))                        # beat 2

        # protect size
        p2 = VGroup(
            Text("Protect size with Freedman–Lane,", font_size=26, color=WHITE),
            Text("so the dominant dose confound cannot",
                 font_size=25, color=BAD),
            Text("masquerade as a network effect.", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.18).next_to(p1, DOWN, buff=0.5)
        self.play_beat(FadeIn(p2, lag_ratio=0.25))                        # beat 3
        self.play(FadeOut(VGroup(head, line, p1, p2)), run_time=0.5)

        # what's left
        left = MathTex(r"\text{exact test of}\ \ ", r"C\delta_i",
                       r"\ \ \text{vs}\ \ ", "y_i").scale(1.2).shift(UP * 1.0)
        left[1].set_color(VAR); left[3].set_color(EIG)
        leftcap = Text("the only thing that can carry genuine signal",
                       font_size=24, color=DIM).next_to(left, DOWN, buff=0.3)
        self.play_beat(Write(left), FadeIn(leftcap))                      # beat 4

        # immune to both threats
        immune = VGroup(
            Text("Immune to:", font_size=26, color=WHITE),
            Text("•  the shared-target map  C ℓ₀", font_size=25, color=BACK),
            Text("•  the size confound  sᵢ", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(leftcap, DOWN, buff=0.5)
        self.play_beat(FadeIn(immune, lag_ratio=0.3))                     # beat 5

        # calibration now; power next
        self.play(FadeOut(VGroup(left, leftcap, immune)), run_time=0.4)
        moral = VGroup(
            Text("Move 1 fixes calibration: the null cannot lie.",
                 font_size=29, color=WHITE),
            Text("Next: strip the backbone for power,",
                 font_size=27, color=DIM),
            Text("and demand out-of-sample proof.", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(moral, lag_ratio=0.3))                      # beat 6
