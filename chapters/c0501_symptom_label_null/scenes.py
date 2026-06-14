"""c0501_symptom_label_null — "The symptom-label null".

Five narrated scenes. Introduce H0^sym: holding the lesions l_i and the
connectome C FIXED, shuffle the impaired/spared labels y_i and recompute the
contrast T each time. Contrast with the location null H0^loc. Define y_i, the
contrast statistic T (m_i = C l_i, the group means m-bar^1 and m-bar^0, and
Delta = m-bar^1 - m-bar^0). Preview the backbone cancellation, then set up the
two claims to prove next: (1) the permutation test is EXACT (c0502) and (2) the
backbone cancels algebraically (c0503).

All equations/claims are sourced from:
  responses/lnm_critique/sections/03_the_right_null.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0501_symptom_label_null ./render.sh \
      chapters/c0501_symptom_label_null/scenes.py -q ql \
      S1_Question S2_Procedure S3_Contrast S4_WhyItWorks S5_Bridge
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — a different question
# ----------------------------------------------------------------------
class S1_Question(NarratedScene):
    scene_key = "S1_Question"

    def construct(self):
        title = Text("A different question", font_size=42, color=WHITE)
        sub = Text("a null model is a question", font_size=24, color=DIM)\
            .next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # the old (location) null
        loc = MathTex(r"H_0^{\mathrm{loc}}", r":\ ",
                      r"\text{is the LOCATION of these lesions special?}")\
            .scale(0.9).shift(UP * 1.4)
        loc[0].set_color(BAD)
        loc_x = Text("the backbone made this unwinnable", font_size=24, color=BAD)\
            .next_to(loc, DOWN, buff=0.3)
        self.play_beat(Write(loc), FadeIn(loc_x))                          # beat 2

        # the new move: fix lesions and C, vary the label
        self.play(FadeOut(VGroup(loc, loc_x)), run_time=0.4)
        fixed = VGroup(
            MathTex(r"\text{FIX the lesions } \ell_i", color=VAR).scale(0.9),
            MathTex(r"\text{FIX the connectome } C", color=WHITE).scale(0.9),
            MathTex(r"\text{VARY only the label } y_i", color=EIG).scale(0.9),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).shift(UP * 1.0)
        self.play_beat(FadeIn(fixed, lag_ratio=0.3))                       # beat 3

        # define y_i
        yi = MathTex("y_i", r"\in", r"\{\,", "1", ",", "0", r"\,\}")\
            .scale(1.1).next_to(fixed, DOWN, buff=0.6)
        yi[0].set_color(EIG); yi[3].set_color(BAD); yi[5].set_color(BACK)
        ylab = VGroup(
            Text("1 = impaired", font_size=22, color=BAD),
            Text("0 = spared", font_size=22, color=BACK),
        ).arrange(RIGHT, buff=0.8).next_to(yi, DOWN, buff=0.25)
        self.play_beat(Write(yi), FadeIn(ylab))                            # beat 4

        # the formal null
        self.play(FadeOut(VGroup(fixed, yi, ylab)), run_time=0.4)
        null = MathTex(r"H_0^{\mathrm{sym}}", r":\ ",
                       r"(y_1,\dots,y_n)\ \text{exchangeable}")\
            .scale(0.95).shift(UP * 0.9)
        null[0].set_color(RES)
        given = MathTex(r"\text{given the fixed maps } (x_1,\dots,x_n)"
                        r"\text{ and covariates } Z")\
            .scale(0.7).set_color(DIM).next_to(null, DOWN, buff=0.3)
        plain = Text("the symptom carries no extra information about the wiring",
                     font_size=24, color=WHITE).next_to(given, DOWN, buff=0.4)
        self.play_beat(Write(null), FadeIn(given), FadeIn(plain))          # beat 5

        # what moves
        self.play(FadeOut(VGroup(null, given, plain)), run_time=0.4)
        moves = VGroup(
            VGroup(
                Text("location null", font_size=24, color=BAD),
                Text("the LESION moves", font_size=24, color=BAD),
            ).arrange(DOWN, buff=0.15),
            MathTex(r"\Big/", color=DIM).scale(1.6),
            VGroup(
                Text("symptom null", font_size=24, color=RES),
                Text("only the LABEL moves", font_size=24, color=RES),
            ).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=0.9).shift(UP * 0.6)
        self.play_beat(FadeIn(moves, lag_ratio=0.2))                       # beat 6

        moral = Text("Same data, two completely different questions.",
                     font_size=27, color=WHITE).next_to(moves, DOWN, buff=0.7)
        moral2 = Text("The critique breaks the first; it leaves this one untouched.",
                      font_size=25, color=DIM).next_to(moral, DOWN, buff=0.25)
        self.play_beat(FadeIn(moral, shift=UP * 0.2), FadeIn(moral2))      # beat 7


# ----------------------------------------------------------------------
# Scene 2 — shuffle the labels
# ----------------------------------------------------------------------
class S2_Procedure(NarratedScene):
    scene_key = "S2_Procedure"

    def construct(self):
        self.header("Shuffle the labels")

        intro = Text("the procedure, step by step", font_size=28, color=DIM)\
            .shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # fixed pieces
        fixed = VGroup(
            MathTex(r"\ell_i", r"\ \text{— each lesion, held fixed}").scale(0.95),
            MathTex("C", r"\ \text{— the connectome, held fixed}").scale(0.95),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).shift(UP * 1.3)
        fixed[0][0].set_color(VAR); fixed[1][0].set_color(WHITE)
        self.play_beat(FadeIn(fixed, lag_ratio=0.3),
                       intro.animate.set_opacity(0.4))                     # beat 2

        # the movable label y_i
        yi = MathTex("y_i", r"=", "1", r"\ \text{(impaired)}", r"\ \text{or}\ ",
                     "0", r"\ \text{(spared)}").scale(0.9)\
            .next_to(fixed, DOWN, buff=0.5)
        yi[0].set_color(EIG); yi[2].set_color(BAD); yi[5].set_color(BACK)
        yi_note = Text("the ONLY movable part", font_size=23, color=EIG)\
            .next_to(yi, DOWN, buff=0.25)
        self.play_beat(Write(yi), FadeIn(yi_note))                         # beat 3

        # the contrast statistic T
        self.play(FadeOut(VGroup(intro, fixed, yi, yi_note)), run_time=0.5)
        Tdef = MathTex("T", r"\ =\ ",
                       r"\text{how sharply the labels split the maps}")\
            .scale(0.95).shift(UP * 1.3)
        Tdef[0].set_color(RES)
        self.play_beat(Write(Tdef))                                        # beat 4

        # the permutation
        perm = MathTex(r"\pi", r":\ ", "y", r"\ \longmapsto\ ", r"y_\pi")\
            .scale(1.15).next_to(Tdef, DOWN, buff=0.7)
        perm[0].set_color(VAR); perm[2].set_color(EIG); perm[4].set_color(EIG)
        perm_lab = Text("a reshuffle of who is impaired and who is spared",
                        font_size=24, color=DIM).next_to(perm, DOWN, buff=0.3)
        self.play_beat(Write(perm), FadeIn(perm_lab))                      # beat 5

        # recompute over the group
        recompute = MathTex(r"\text{recompute }", r"T(y_\pi)",
                            r"\ \text{ for every } \pi \in G")\
            .scale(0.95).next_to(perm_lab, DOWN, buff=0.6)
        recompute[1].set_color(RES)
        same = Text("maps and C identical every single time",
                    font_size=23, color=BACK).next_to(recompute, DOWN, buff=0.25)
        self.play_beat(Write(recompute), FadeIn(same))                     # beat 6

        # the verdict
        self.play(FadeOut(VGroup(Tdef, perm, perm_lab, recompute, same)),
                  run_time=0.5)
        verdict = VGroup(
            Text("real T sharper than nearly all shuffles", font_size=26, color=RES),
            Text("the symptom genuinely tracks the lesions", font_size=26, color=WHITE),
            Text("otherwise, it does not", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(verdict, lag_ratio=0.3))                     # beat 7


# ----------------------------------------------------------------------
# Scene 3 — the contrast statistic
# ----------------------------------------------------------------------
class S3_Contrast(NarratedScene):
    scene_key = "S3_Contrast"

    def construct(self):
        self.header("The contrast statistic")

        intro = Text("type out every symbol, one at a time",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # m_i = C l_i
        mi = MathTex("m_i", "=", "C", r"\,\ell_i").scale(1.4).shift(UP * 1.2)
        mi[0].set_color(VAR); mi[2].set_color(WHITE); mi[3].set_color(VAR)
        brace = Brace(mi, DOWN, color=DIM)
        mi_lab = Text("push lesion l_i through the connectome C",
                      font_size=23, color=DIM).next_to(brace, DOWN, buff=0.2)
        self.play_beat(Write(mi), GrowFromCenter(brace), FadeIn(mi_lab),
                       intro.animate.set_opacity(0.4))                     # beat 2

        # the two groups
        self.play(FadeOut(VGroup(intro, brace, mi_lab)),
                  mi.animate.scale(0.7).to_edge(UP, buff=1.1), run_time=0.5)
        groups = VGroup(
            MathTex(r"\text{group 1: impaired,}\ ", "y_i", "=", "1").scale(0.9),
            MathTex(r"\text{group 0: spared,}\ ", "y_i", "=", "0").scale(0.9),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).shift(UP * 1.1)
        groups[0][1].set_color(EIG); groups[0][3].set_color(BAD)
        groups[1][1].set_color(EIG); groups[1][3].set_color(BACK)
        self.play_beat(FadeIn(groups, lag_ratio=0.3))                      # beat 3

        # group means
        means = VGroup(
            MathTex(r"\bar{m}^{1}", r"\ =\ \text{mean map of impaired}").scale(0.9),
            MathTex(r"\bar{m}^{0}", r"\ =\ \text{mean map of spared}").scale(0.9),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(groups, DOWN, buff=0.5)
        means[0][0].set_color(BAD); means[1][0].set_color(BACK)
        self.play_beat(FadeIn(means, lag_ratio=0.3))                       # beat 4

        # Delta = m-bar^1 - m-bar^0
        self.play(FadeOut(VGroup(groups, means)), run_time=0.4)
        delta = MathTex(r"\Delta", "=", r"\bar{m}^{1}", "-", r"\bar{m}^{0}")\
            .scale(1.4).shift(UP * 0.7)
        delta[0].set_color(RES); delta[2].set_color(BAD); delta[4].set_color(BACK)
        dbrace = Brace(delta, DOWN, color=RES)
        dlab = Text("how far the impaired mean sits from the spared mean",
                    font_size=23, color=WHITE).next_to(dbrace, DOWN, buff=0.2)
        self.play_beat(Write(delta), GrowFromCenter(dbrace), FadeIn(dlab))  # beat 5

        # sharpen to t per voxel, then max-statistic
        self.play(FadeOut(VGroup(dbrace, dlab)),
                  delta.animate.scale(0.7).to_edge(UP, buff=1.4), run_time=0.5)
        sharp = MathTex(r"t_v", r"\ \text{per voxel}", r"\ \longrightarrow\ ",
                        "T", r"=", r"\max_v |t_v|").scale(1.0).shift(UP * 0.4)
        sharp[0].set_color(RES); sharp[3].set_color(RES); sharp[5].set_color(RES)
        sharp_lab = Text("summarize the whole map by its largest value",
                         font_size=23, color=DIM).next_to(sharp, DOWN, buff=0.3)
        self.play_beat(Write(sharp), FadeIn(sharp_lab))                    # beat 6

        moral = Text("T is one scalar verdict: the size of the gap\nthe label opens between the two groups of maps",
                     font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(sharp_lab, DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 4 — why this question has an answer
# ----------------------------------------------------------------------
class S4_WhyItWorks(NarratedScene):
    scene_key = "S4_WhyItWorks"

    def construct(self):
        self.header("Why this question has an answer")

        intro = Text("the location null had none — look at what is shared",
                     font_size=27, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        shared = Text("lesions held fixed  →  the SAME backbone\nsits in every map, in both label groups",
                      font_size=27, color=BACK, line_spacing=0.8).shift(UP * 1.2)
        self.play_beat(FadeIn(shared, shift=UP * 0.2),
                       intro.animate.set_opacity(0.4))                     # beat 2

        # decomposition x_i = beta_i u_1 + r_i
        self.play(FadeOut(VGroup(intro, shared)), run_time=0.4)
        decomp = MathTex("x_i", "=", r"\beta_i\, u_1", "+", "r_i")\
            .scale(1.3).shift(UP * 1.0)
        decomp[0].set_color(VAR); decomp[2].set_color(BACK); decomp[4].set_color(EIG)
        bbrace = Brace(decomp[2], DOWN, color=BACK)
        blab = Text("backbone part", font_size=22, color=BACK)\
            .next_to(bbrace, DOWN, buff=0.15)
        rbrace = Brace(decomp[4], DOWN, color=EIG)
        rlab = Text("residual", font_size=22, color=EIG)\
            .next_to(rbrace, DOWN, buff=0.15)
        self.play_beat(Write(decomp),
                       GrowFromCenter(bbrace), FadeIn(blab),
                       GrowFromCenter(rbrace), FadeIn(rlab))               # beat 3

        # backbone is label-free
        self.play(FadeOut(VGroup(bbrace, blab, rbrace, rlab)),
                  decomp.animate.scale(0.75).to_edge(UP, buff=1.2), run_time=0.5)
        free = MathTex(r"\beta_i\, u_1", r"\ \text{depends on lesion location, }",
                       r"\text{NOT on } y_i").scale(0.85).shift(UP * 0.7)
        free[0].set_color(BACK); free[2].set_color(EIG)
        self.play_beat(Write(free))                                        # beat 4

        # cancellation in the contrast
        cancel = MathTex(r"\bar{x}^{1}_v - \bar{x}^{0}_v",
                         r"\ =\ ",
                         r"(\bar\beta^{1}-\bar\beta^{0})\,u_{1,v}",
                         r"\ +\ ",
                         r"(\bar r^{1}_v-\bar r^{0}_v)")\
            .scale(0.85).next_to(free, DOWN, buff=0.6)
        cancel[2].set_color(BACK); cancel[4].set_color(EIG)
        strike = Line(cancel[2].get_left(), cancel[2].get_right(),
                      color=BAD, stroke_width=5)
        cancel_lab = Text("same on both sides → it cancels",
                          font_size=23, color=BAD).next_to(cancel, DOWN, buff=0.3)
        self.play_beat(Write(cancel), Create(strike), FadeIn(cancel_lab))  # beat 5

        # what survives
        survive = MathTex(r"\text{only }", r"(\bar r^{1}_v-\bar r^{0}_v)",
                          r"\ \text{survives}").scale(0.95)\
            .next_to(cancel_lab, DOWN, buff=0.45)
        survive[1].set_color(EIG)
        survive_lab = Text("the part the symptom label could actually track",
                           font_size=23, color=WHITE).next_to(survive, DOWN, buff=0.25)
        self.play_beat(Write(survive), FadeIn(survive_lab))                # beat 6

        self.play(FadeOut(VGroup(decomp, free, cancel, strike, cancel_lab,
                                 survive, survive_lab)), run_time=0.5)
        moral = Text("The backbone detonated the location null.\nUnder label permutation, the same backbone goes inert.",
                     font_size=27, color=RES, line_spacing=0.8)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 5 — what we must prove
# ----------------------------------------------------------------------
class S5_Bridge(NarratedScene):
    scene_key = "S5_Bridge"

    def construct(self):
        self.header("What we must prove")

        intro = Text("two claims are still promises, not proofs",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # claim 1: exactness
        c1 = VGroup(
            Text("Claim 1  —  the permutation test is EXACT", font_size=27, color=RES),
            Text("valid p-value in finite samples, no distributional assumption",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).shift(UP * 1.3)
        self.play_beat(FadeIn(c1, shift=UP * 0.2),
                       intro.animate.set_opacity(0.4))                     # beat 2

        # why claim 1 is plausible
        c1why = MathTex(r"n!", r"\ \text{labelings} \Rightarrow ",
                        r"\text{rank of } T(y_{\mathrm{id}})", r"\ \text{is uniform}")\
            .scale(0.8).next_to(c1, DOWN, buff=0.45)
        c1why[0].set_color(EIG); c1why[2].set_color(RES)
        self.play_beat(Write(c1why))                                       # beat 3

        # claim 2: cancellation
        self.play(FadeOut(VGroup(c1, c1why)), run_time=0.4)
        c2 = VGroup(
            Text("Claim 2  —  the backbone CANCELS algebraically", font_size=27, color=BACK),
            MathTex(r"\beta_i\, u_1", r"\ \text{must drop out of the contrast}")\
                .scale(0.85),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.2)
        c2[1][0].set_color(BACK)
        self.play_beat(FadeIn(c2, shift=UP * 0.2))                         # beat 4

        # why claim 2 is plausible
        c2why = Text("beta_i is label-independent: its distribution is identical\nin the observed and every shuffled labeling, so it has no leverage",
                     font_size=24, color=WHITE, line_spacing=0.8)\
            .next_to(c2, DOWN, buff=0.45)
        self.play_beat(FadeIn(c2why, shift=UP * 0.2))                      # beat 5

        # the setup for next chapters
        self.play(FadeOut(VGroup(c2, c2why)), run_time=0.4)
        nxt = VGroup(
            Text("nail both  →  the symptom null is immune to the backbone",
                 font_size=26, color=RES),
            MathTex(r"\text{c0502: exactness}",
                    r"\ \cdot\ ",
                    r"\text{c0503: cancellation}").scale(0.85),
        ).arrange(DOWN, buff=0.5)
        nxt[1][0].set_color(RES); nxt[1][2].set_color(BACK)
        self.play_beat(FadeIn(nxt, lag_ratio=0.3))                         # beat 6
