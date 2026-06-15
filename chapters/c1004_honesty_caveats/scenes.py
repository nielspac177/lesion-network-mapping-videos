"""c1004_honesty_caveats — "Honesty caveats".

The closing chapter of the LNM series. It does the thing the source file insists
on: a fair treatment flags what is verified versus what is not. Three columns:
proven math (R1 alignment, backbone cancellation, permutation exactness, R5 SNR)
plus page-cited critique numbers = VERIFIED; abstract-only empirical figures and
the author's unpublished FUS-VIM numbers = [verify against primary source]; one
genuinely open methods question (Freedman-Lane vs raw label-shuffle). Then the
honest stance: take the critique seriously, give the rebuttal full standing,
label the uncertainty.

All claims/numbers are sourced from:
  responses/lnm_critique/sections/09_references_caveats.md
  responses/lnm_critique/papers/_papers_verified.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c1004_honesty_caveats ./render.sh \
      chapters/c1004_honesty_caveats/scenes.py -q ql \
      S1_Why S2_Verified S3_Pending S4_OpenQuestion S5_Stance
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — why a caveats chapter
# ----------------------------------------------------------------------
class S1_Why(NarratedScene):
    scene_key = "S1_Why"

    def construct(self):
        title = Text("Why a caveats chapter", font_size=42, color=WHITE)
        sub = Text("a fair treatment flags what is verified, and what is not",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))            # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        principle = VGroup(
            Text("A paper that accuses a field of over-reading its evidence",
                 font_size=27, color=WHITE),
            Text("has no business over-reading its own.",
                 font_size=27, color=RES),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.4)
        hands = Text("So: we show our hands. We flag what is verified, and what is not.",
                     font_size=24, color=DIM).next_to(principle, DOWN, buff=0.5)
        self.play_beat(FadeIn(principle, shift=UP * 0.2), FadeIn(hands))     # beat 2

        # two tracks of honesty
        self.play(FadeOut(VGroup(principle, hands)), run_time=0.4)
        twokinds = Text("Two kinds of claim → two different standards",
                        font_size=28, color=WHITE).shift(UP * 1.9)
        self.play_beat(FadeIn(twokinds))                                    # beat 3

        proof = VGroup(
            Text("US DOING MATH", font_size=24, color=BACK),
            Text("theorems we prove on the page — owned fully",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.15).shift(UP * 0.4)
        self.play_beat(FadeIn(proof, shift=UP * 0.2))                       # beat 4

        report = VGroup(
            Text("US REPORTING OTHERS", font_size=24, color=EIG),
            Text("only as sure as our sources",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.15).next_to(proof, DOWN, buff=0.6)
        self.play_beat(FadeIn(report, shift=UP * 0.2))                      # beat 5

        keep = Text("kept visibly apart — never mistake a proof for a report",
                    font_size=24, color=RES).to_edge(DOWN, buff=0.9)
        self.play_beat(FadeIn(keep, shift=UP * 0.2))                        # beat 6


# ----------------------------------------------------------------------
# Scene 2 — what is verified
# ----------------------------------------------------------------------
class S2_Verified(NarratedScene):
    scene_key = "S2_Verified"

    def construct(self):
        self.header("What is verified")

        head = Text("The verified column — the mathematical spine stands alone",
                    font_size=27, color=BACK).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                        # beat 1

        # R1 alignment:  m_ell = C ell ,  leans on u_1.
        # Every symbol braced on screen (HARD RULE 1) inside this one beat.
        r1 = MathTex("m_{\\ell}", "=", "C", r"\ell").scale(1.3).shift(UP * 1.1)
        r1[0].set_color(VAR); r1[2].set_color(WHITE); r1[3].set_color(VAR)
        br_m = Brace(r1[0], UP, color=VAR)
        lb_m = Text("lesion map", font_size=20, color=VAR).next_to(br_m, UP, buff=0.12)
        br_C = Brace(r1[2], DOWN, color=WHITE)
        lb_C = Text("normative connectome", font_size=20, color=WHITE)\
            .next_to(br_C, DOWN, buff=0.12)
        br_l = Brace(r1[3], DOWN, color=VAR)
        lb_l = Text("0/1 lesion vector", font_size=20, color=VAR)\
            .next_to(br_l, DOWN, buff=0.12)
        r1lab = MathTex(r"\text{aligns with the leading eigenvector } u_1")\
            .scale(0.8).set_color(BACK).next_to(VGroup(lb_C, lb_l), DOWN, buff=0.3)
        self.play_beat(Write(r1), GrowFromCenter(br_m), FadeIn(lb_m),
                       GrowFromCenter(br_C), FadeIn(lb_C),
                       GrowFromCenter(br_l), FadeIn(lb_l),
                       FadeIn(r1lab))                                       # beat 2

        # backbone cancellation
        self.play(FadeOut(VGroup(r1, r1lab, br_m, lb_m, br_C, lb_C, br_l, lb_l)),
                  run_time=0.4)
        cancel = MathTex(r"\text{contrast}", "=", r"\text{signal}", "+",
                         r"\underbrace{\text{backbone}}_{\text{cancels}}")\
            .scale(1.0).shift(UP * 1.1)
        cancel[2].set_color(VAR); cancel[4].set_color(BAD)
        cancel_lab = Text("the label-independent backbone subtracts out",
                          font_size=23, color=DIM).next_to(cancel, DOWN, buff=0.3)
        self.play_beat(Write(cancel), FadeIn(cancel_lab))                  # beat 3

        # permutation exactness — every symbol braced on screen inside one beat.
        self.play(FadeOut(VGroup(cancel, cancel_lab)), run_time=0.4)
        perm = MathTex(r"\Pr\big(", "T(\\pi s)", r"\geq", "t", r"\big)",
                       "=", r"\frac{\#\{\pi : T(\pi s) \geq t\}}{|\Pi|}")\
            .scale(0.95).shift(UP * 1.1)
        perm[1].set_color(VAR); perm[3].set_color(EIG); perm[6].set_color(RES)
        br_T = Brace(perm[1], UP, color=VAR)
        lb_T = Text("statistic on shuffled labels  π s", font_size=19, color=VAR)\
            .next_to(br_T, UP, buff=0.1)
        br_t = Brace(perm[3], DOWN, color=EIG)
        lb_t = Text("threshold", font_size=19, color=EIG).next_to(br_t, DOWN, buff=0.1)
        br_P = Brace(perm[6], DOWN, color=RES)
        lb_P = Text("fraction of all |Π| label shuffles that exceed it",
                    font_size=19, color=RES).next_to(br_P, DOWN, buff=0.1)
        perm_lab = Text("shuffling symptom labels → an exactly valid null under exchangeability",
                        font_size=22, color=DIM).next_to(lb_P, DOWN, buff=0.25)
        self.play_beat(Write(perm), GrowFromCenter(br_T), FadeIn(lb_T),
                       GrowFromCenter(br_t), FadeIn(lb_t),
                       GrowFromCenter(br_P), FadeIn(lb_P),
                       FadeIn(perm_lab))                                    # beat 4

        # R5 residualization SNR — symbols braced on screen inside one beat.
        self.play(FadeOut(VGroup(perm, perm_lab, br_T, lb_T, br_t, lb_t,
                                 br_P, lb_P)), run_time=0.4)
        r5 = MathTex(r"\tilde m_{\ell}", "=", "m_{\\ell}", "-",
                     r"\Pi_{\mathcal{B}}\, m_{\ell}").scale(1.1).shift(UP * 1.1)
        r5[0].set_color(VAR); r5[2].set_color(VAR); r5[4].set_color(BAD)
        br_res = Brace(r5[0], UP, color=VAR)
        lb_res = Text("residualized map", font_size=19, color=VAR)\
            .next_to(br_res, UP, buff=0.1)
        br_raw = Brace(r5[2], DOWN, color=VAR)
        lb_raw = Text("raw map", font_size=19, color=VAR)\
            .next_to(br_raw, DOWN, buff=0.1)
        br_proj = Brace(r5[4], DOWN, color=BAD)
        lb_proj = Text("projection onto the backbone B", font_size=19, color=BAD)\
            .next_to(br_proj, DOWN, buff=0.1)
        r5_lab = Text("remove the low-rank backbone → the contrast survives",
                      font_size=23, color=DIM)\
            .next_to(VGroup(lb_raw, lb_proj), DOWN, buff=0.25)
        self.play_beat(Write(r5), GrowFromCenter(br_res), FadeIn(lb_res),
                       GrowFromCenter(br_raw), FadeIn(lb_raw),
                       GrowFromCenter(br_proj), FadeIn(lb_proj),
                       FadeIn(r5_lab))                                      # beat 5

        # check the algebra, not us
        self.play(FadeOut(VGroup(r5, r5_lab, head, br_res, lb_res,
                                 br_raw, lb_raw, br_proj, lb_proj)),
                  run_time=0.4)
        audit = VGroup(
            Text("You do not have to trust us.", font_size=29, color=WHITE),
            Text("You have to check the algebra — and it closes on the page.",
                 font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.3)
        self.play_beat(FadeIn(audit, lag_ratio=0.3))                       # beat 6

        # page-cited critique numbers
        cited = Text("Also verified: the page-cited critique numbers\n(read from the four core papers' full texts)",
                     font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(audit, DOWN, buff=0.55)
        self.play_beat(FadeIn(cited))                                      # beat 7

        nums = VGroup(
            self._num_chip("same-symptom", "r = 0.44", BACK),
            self._num_chip("degree map", "r = 0.16", BAD),
            self._num_chip("t > 10", "0 FP / 1000", RES),
        ).arrange(RIGHT, buff=0.55).to_edge(DOWN, buff=0.7)
        self.play_beat(FadeIn(nums, lag_ratio=0.2))                        # beat 8

    def _num_chip(self, label, value, color):
        box = RoundedRectangle(width=3.0, height=1.0, corner_radius=0.12,
                               stroke_color=color, stroke_width=2,
                               fill_color=color, fill_opacity=0.10)
        lab = Text(label, font_size=20, color=DIM)
        val = MathTex(value, color=color).scale(0.8)
        inner = VGroup(lab, val).arrange(DOWN, buff=0.12).move_to(box)
        return VGroup(box, inner)


# ----------------------------------------------------------------------
# Scene 3 — what is marked pending
# ----------------------------------------------------------------------
class S3_Pending(NarratedScene):
    scene_key = "S3_Pending"

    def construct(self):
        self.header("What is marked pending")

        head = Text("The pending column — gaps tagged in plain sight",
                    font_size=27, color=EIG).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                       # beat 1

        # two abstract-only preprints
        pre = VGroup(
            Text("Two response-side preprints — abstract-level only",
                 font_size=26, color=WHITE),
            self._tag("[verify against primary source]"),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.2)
        self.play_beat(FadeIn(pre[0]), FadeIn(pre[1], shift=UP * 0.2))     # beat 2

        # dim-reduction accuracies
        self.play(FadeOut(pre), run_time=0.4)
        acc = VGroup(
            Text("Dimensionality-reduction accuracies", font_size=24, color=DIM),
            MathTex(r"0.51\ (\text{schizophrenia}) \;\to\; 0.61\ (\text{epilepsy})")
                .scale(0.85).set_color(VAR),
            self._tag("[verify against primary source]"),
        ).arrange(DOWN, buff=0.28).shift(UP * 0.9)
        self.play_beat(FadeIn(acc, lag_ratio=0.2))                        # beat 3

        # Petersen cross-domain
        pet = VGroup(
            Text("Petersen et al. cross-domain similarities", font_size=24, color=DIM),
            MathTex(r"2{,}950\ \text{stroke patients},\ 12\ \text{cohorts}")
                .scale(0.85).set_color(VAR),
        ).arrange(DOWN, buff=0.25).next_to(acc, DOWN, buff=0.55)
        self.play_beat(FadeIn(pet, lag_ratio=0.2))                        # beat 4

        # the tag on screen
        self.play(FadeOut(VGroup(acc, pet, head)), run_time=0.4)
        tagdemo = VGroup(
            Text("On screen, each wears the same tag:", font_size=26, color=WHITE),
            self._tag("[verify against primary source]", big=True),
        ).arrange(DOWN, buff=0.4).shift(UP * 1.3)
        self.play_beat(FadeIn(tagdemo[0]), Write(tagdemo[1]))             # beat 5

        # FUS-VIM, separate, unpublished
        fus = VGroup(
            Text("Separate again: the author's own FUS-VIM numbers",
                 font_size=25, color=WHITE),
            Text("essential tremor / Parkinson's",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.18).next_to(tagdemo, DOWN, buff=0.6)
        self.play_beat(FadeIn(fus, shift=UP * 0.2))                       # beat 6

        # the actual numbers + flag
        # NOTE: two SEPARATE MathTex (not one with a \qquad spacer arg, which
        # renders to zero glyphs and shifts sub-indices — pitfall #1).
        self.play(FadeOut(VGroup(tagdemo, fus)), run_time=0.4)
        sens = MathTex(r"\text{sensitivity}", "=", r"r \approx 0.99").scale(0.9)
        sens[0].set_color(BACK); sens[2].set_color(BACK)
        spec = MathTex(r"\text{specificity}", "=", r"r \approx -0.21").scale(0.9)
        spec[0].set_color(BAD); spec[2].set_color(BAD)
        nums = VGroup(sens, spec).arrange(DOWN, buff=0.3).shift(UP * 1.0)
        rkey = Text("r = spatial correlation between maps",
                    font_size=20, color=DIM).next_to(nums, UP, buff=0.3)
        flag = Text("UNPUBLISHED · in progress · not peer reviewed",
                    font_size=24, color=BAD).next_to(nums, DOWN, buff=0.4)
        self.play_beat(Write(nums), FadeIn(rkey), FadeIn(flag))           # beat 7

        moral = Text("A worked example from the author's desk —\nan illustration, never a datum that settles anything.",
                     font_size=25, color=DIM, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 8

    def _tag(self, text, big=False):
        fs = 26 if big else 22
        t = Text(text, font_size=fs, color=BAD)
        box = SurroundingRectangle(t, color=BAD, buff=0.15,
                                   corner_radius=0.08)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 4 — an open methods question
# ----------------------------------------------------------------------
class S4_OpenQuestion(NarratedScene):
    scene_key = "S4_OpenQuestion"

    def construct(self):
        self.header("An open methods question")

        head = VGroup(
            Text("One honest open question.", font_size=29, color=RES),
            Text("We will not pretend it is decided.", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.8)
        self.play_beat(FadeIn(head, lag_ratio=0.3))                       # beat 1

        q = Text("The symptom-label null can be built two ways —\nnot fully settled for THIS exact statistic.",
                 font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(head, DOWN, buff=0.6)
        self.play_beat(FadeIn(q, shift=UP * 0.2))                         # beat 2

        # scheme one: raw label shuffle (Manly)
        self.play(FadeOut(VGroup(head, q)), run_time=0.4)
        s1 = VGroup(
            Text("Scheme 1 — raw label shuffle (Manly)", font_size=26, color=VAR),
            Text("swap each patient's symptom with another patient's map",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.18).shift(UP * 1.7)
        self.play_beat(FadeIn(s1, shift=UP * 0.2))                        # beat 3

        used = Text("← exactly what the rebuttal uses",
                    font_size=23, color=RES).next_to(s1, DOWN, buff=0.35)
        self.play_beat(FadeIn(used, shift=RIGHT * 0.2))                   # beat 4

        # scheme two: Freedman-Lane
        s2 = VGroup(
            Text("Scheme 2 — Freedman–Lane", font_size=26, color=BACK),
            Text("residualize on nuisance covariates → permute → refit",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.18).next_to(used, DOWN, buff=0.55)
        self.play_beat(FadeIn(s2, shift=UP * 0.2))                        # beat 5

        # both cancel backbone; only FL exact with covariates
        both = VGroup(
            Text("Both cancel the backbone (it is label-independent).",
                 font_size=24, color=WHITE),
            Text("Only Freedman–Lane stays exact when covariates are present.",
                 font_size=24, color=RES),
        ).arrange(DOWN, buff=0.22).to_edge(DOWN, buff=1.0)
        self.play_beat(FadeIn(both[0]), FadeIn(both[1], shift=UP * 0.2))   # beat 6

        # genuinely open
        self.play(FadeOut(VGroup(s1, used, s2, both)), run_time=0.5)
        openq = VGroup(
            Text("Which is right for this precise statistic", font_size=28, color=WHITE),
            Text("is genuinely OPEN.", font_size=30, color=RES),
            Text("Our case holds under either — and we leave the seam visible.",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3)
        self.play_beat(FadeIn(openq, lag_ratio=0.3))                      # beat 7


# ----------------------------------------------------------------------
# Scene 5 — the honest stance
# ----------------------------------------------------------------------
class S5_Stance(NarratedScene):
    scene_key = "S5_Stance"

    def construct(self):
        self.header("The honest stance")

        head = Text("The stance we close on — the spine of our honesty",
                    font_size=28, color=WHITE).shift(UP * 2.5)
        self.play_beat(FadeIn(head))                                      # beat 1

        # take the critique seriously
        c1 = VGroup(
            Text("1.  Take the critique seriously", font_size=27, color=RES),
            Text("its strongest form is page-cited; we concede the true part verbatim",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 1.3)
        self.play_beat(FadeIn(c1, shift=UP * 0.2))                        # beat 2

        avg = MathTex(r"M \to I", r"\ \Longrightarrow\ ",
                      r"\text{average} \to \deg(C)").scale(0.95)
        avg[0].set_color(VAR); avg[2].set_color(BAD)
        avg.next_to(c1, DOWN, buff=0.4)
        avgcap = Text("under uniform, non-overlapping sampling",
                      font_size=21, color=DIM).next_to(avg, DOWN, buff=0.2)
        self.play_beat(Write(avg), FadeIn(avgcap))                        # beat 3

        # give rebuttal full standing
        self.play(FadeOut(VGroup(c1, avg, avgcap)), run_time=0.4)
        c2 = VGroup(
            Text("2.  Give the rebuttal full standing", font_size=27, color=BACK),
            Text("real symptom lesions overlap and are non-random;",
                 font_size=23, color=WHITE),
            Text("the CONTRAST — not the average — carries the signal",
                 font_size=23, color=WHITE),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).shift(UP * 1.4)
        self.play_beat(FadeIn(c2, shift=UP * 0.2))                        # beat 4

        # label the uncertainty
        c3 = VGroup(
            Text("3.  Label the uncertainty", font_size=27, color=EIG),
            Text("proven math · pending figures · the open question named",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(c2, DOWN, buff=0.55)
        self.play_beat(FadeIn(c3, shift=UP * 0.2))                        # beat 5

        # the goal
        self.play(FadeOut(VGroup(c2, c3, head)), run_time=0.5)
        goal = VGroup(
            Text("The goal was never to win the argument.", font_size=30, color=WHITE),
            Text("The goal is to understand the math —", font_size=30, color=WHITE),
            Text("cleanly enough that you can audit it yourself.", font_size=30, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.4)
        self.play_beat(FadeIn(goal, lag_ratio=0.3))                       # beat 6

        close = Text("The premises true · the narrow conclusion true ·\nevery hedge shown in the open.",
                     font_size=26, color=DIM, line_spacing=0.8)\
            .to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(close, shift=UP * 0.2))                     # beat 7
