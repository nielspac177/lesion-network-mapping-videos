"""v0608_full_conformal_nonconformity —
"Full conformal and nonconformity-score design (deep dive)".

Six narrated scenes. Motivate full (transductive) conformal as the every-point
ideal that split conformal approximates; walk the refit-per-candidate loop;
prove exact coverage by the same rank-uniformity symmetry; design the
nonconformity score (absolute residual, normalized residual, signed CQR) and
show validity is preserved regardless; tally the compute cost; name the
hierarchy full > CV+/jackknife+ > split.

All equations/numbers are sourced from:
  volumes/vol6_conformal/chapters/02_split_conformal.md
  volumes/vol6_conformal/chapters/01_the_guarantee.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/v0608_full_conformal_nonconformity ./render.sh \
      chapters/v0608_full_conformal_nonconformity/scenes.py -q ql \
      S1_Why S2_Procedure S3_Coverage S4_ScoreDesign S5_Cost S6_Takeaway
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — why full conformal (split wastes data + split noise)
# ----------------------------------------------------------------------
class S1_Why(NarratedScene):
    scene_key = "S1_Why"

    def construct(self):
        self.header("Why full conformal")

        title = Text("Split conformal wastes data", font_size=34, color=WHITE)\
            .shift(UP * 2.5)
        self.play_beat(FadeIn(title, shift=UP * 0.2))                       # beat 1

        # the two piles
        train = self._pile("training pile\n(fits the model)", BACK)
        calib = self._pile("calibration pile, size n\n(sets q-hat)", VAR)
        piles = VGroup(train, calib).arrange(RIGHT, buff=1.4).shift(DOWN * 0.2)
        self.play_beat(FadeIn(train, shift=RIGHT * 0.2),
                       FadeIn(calib, shift=LEFT * 0.2))                     # beat 2

        split_note = Text("data carved in half — neither part uses all of it",
                          font_size=24, color=DIM).next_to(piles, DOWN, buff=0.6)
        self.play_beat(FadeIn(split_note))                                 # beat 3

        # the tiny-n bite: q-hat is the worst calibration patient
        self.play(FadeOut(VGroup(title, piles, split_note)), run_time=0.5)
        nq = MathTex(r"n = 9,\ \ 1-\alpha = 0.9", r"\ \Rightarrow\ ",
                     r"k = \lceil 0.9 \times 10 \rceil = 9").scale(1.0)\
            .shift(UP * 1.1)
        nq[2].set_color(RES)
        worst = Text("q-hat = the 9th of 9 scores = the single WORST patient",
                     font_size=25, color=BAD).next_to(nq, DOWN, buff=0.4)
        self.play_beat(Write(nq), FadeIn(worst, shift=UP * 0.2))           # beat 4

        noisy = VGroup(
            Text("one weird case sets the whole bar  →  noisy", font_size=25, color=BAD),
            Text("and the bar depends on which split you drew", font_size=25, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(worst, DOWN, buff=0.5)
        self.play_beat(FadeIn(noisy[0]), FadeIn(noisy[1], shift=UP * 0.2))  # beat 5

        # full conformal: every point fits AND calibrates
        self.play(FadeOut(VGroup(nq, worst, noisy)), run_time=0.5)
        full = VGroup(
            Text("Full (transductive) conformal", font_size=32, color=RES),
            Text("every point takes part in BOTH fitting and calibration",
                 font_size=25, color=WHITE),
            Text("→  more stable sets from the same data", font_size=25, color=BACK),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.3)
        self.play_beat(FadeIn(full, lag_ratio=0.3))                        # beat 6

        cost = Text("the price is compute — paid in full in scene five",
                    font_size=24, color=DIM).next_to(full, DOWN, buff=0.7)
        self.play_beat(FadeIn(cost))                                       # beat 7

    def _pile(self, label, color):
        box = RoundedRectangle(width=3.2, height=1.5, corner_radius=0.15,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.12)
        t = Text(label, font_size=21, color=color, line_spacing=0.8).move_to(box)
        return VGroup(box, t)


# ----------------------------------------------------------------------
# Scene 2 — the transductive procedure (refit per candidate label)
# ----------------------------------------------------------------------
class S2_Procedure(NarratedScene):
    scene_key = "S2_Procedure"

    def construct(self):
        self.header("The transductive procedure")

        intro = Text("we never see the test label, so we TRY every candidate y",
                     font_size=27, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # augment the data with (x_test, y)
        aug = MathTex(r"\mathcal{D}", r"\ \cup\ ", r"\{(x_{\text{test}},\, y)\}")\
            .scale(1.25).shift(UP * 1.4)
        aug[0].set_color(VAR); aug[2].set_color(EIG)
        b_data = Brace(aug[0], UP, color=VAR)
        l_data = Text("D = all the patients we already hold",
                      font_size=20, color=VAR).next_to(b_data, UP, buff=0.12)
        b_aug = Brace(aug[2], DOWN, color=EIG)
        l_aug = Text("pretend candidate y is the truth, add the pair",
                     font_size=22, color=EIG).next_to(b_aug, DOWN, buff=0.15)
        self.play_beat(Write(aug),
                       GrowFromCenter(b_data), FadeIn(l_data),
                       GrowFromCenter(b_aug), FadeIn(l_aug),
                       intro.animate.set_opacity(0.4))                     # beat 2

        # refit on n+1 points -> f-hat-y
        self.play(FadeOut(VGroup(b_data, l_data, b_aug, l_aug)), run_time=0.4)
        refit = MathTex(r"\text{refit on } n+1 \text{ points}",
                        r"\ \longrightarrow\ ", r"\hat{f}_y")\
            .scale(1.05).next_to(aug, DOWN, buff=0.7)
        refit[2].set_color(BAD)
        rcap = Text("the model depends on the candidate y",
                    font_size=22, color=DIM).next_to(refit, DOWN, buff=0.2)
        self.play_beat(Write(refit), FadeIn(rcap))                        # beat 3

        # score all n+1 points
        self.play(FadeOut(VGroup(aug, refit, rcap, intro)), run_time=0.5)
        score = MathTex(r"s(x_i, y_i)", r"\ \text{for all } n+1 \text{ points}")\
            .scale(1.1).shift(UP * 1.6)
        score[0].set_color(VAR)
        sb = Brace(score[0], DOWN, color=VAR)
        sl = Text("how strange the pair looks — higher = stranger",
                  font_size=22, color=VAR).next_to(sb, DOWN, buff=0.15)
        self.play_beat(Write(score), GrowFromCenter(sb), FadeIn(sl))      # beat 4

        # rank of the test score
        self.play(FadeOut(VGroup(sb, sl)), run_time=0.4)
        rank = MathTex(r"R", r"=", r"\text{rank of }", r"s_{\text{test}}",
                       r"\text{ among the } n+1 \text{ scores}")\
            .scale(0.95).next_to(score, DOWN, buff=0.7)
        rank[0].set_color(RES); rank[3].set_color(BAD)
        rcap2 = Text("rank one = smallest, least strange",
                     font_size=22, color=DIM).next_to(rank, DOWN, buff=0.2)
        self.play_beat(Write(rank), FadeIn(rcap2))                        # beat 5

        # include y if rank not extreme
        keep = MathTex(r"\text{keep } y", r"\iff", r"R \le k",
                       r",\quad k = \lceil (1-\alpha)(n+1) \rceil")\
            .scale(0.95).next_to(rcap2, DOWN, buff=0.55)
        keep[0].set_color(EIG); keep[2].set_color(RES)
        self.play_beat(Write(keep))                                       # beat 6

        # loop over candidates -> collect keepers
        self.play(FadeOut(VGroup(score, rank, rcap2, keep)), run_time=0.5)
        loop = VGroup(
            Text("loop over every candidate label y", font_size=26, color=WHITE),
            MathTex(r"C(x_{\text{test}}) = \{\, y : R(y) \le k \,\}")
                .scale(1.05).set_color(RES),
            Text("the keepers form the full conformal set", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.35).shift(UP * 0.3)
        self.play_beat(FadeIn(loop, lag_ratio=0.3))                       # beat 7

        moral = Text("one refit per candidate — the model is no longer fixed",
                     font_size=25, color=BAD).next_to(loop, DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                     # beat 8


# ----------------------------------------------------------------------
# Scene 3 — coverage by symmetry (rank is uniform)
# ----------------------------------------------------------------------
class S3_Coverage(NarratedScene):
    scene_key = "S3_Coverage"

    def construct(self):
        self.header("Coverage by symmetry")

        claim = Text("why coverage is at least 1 minus alpha, using EVERY point",
                     font_size=28, color=RES).shift(UP * 2.6)
        self.play_beat(FadeIn(claim))                                     # beat 1

        # run at the true label -> augmented set is the real data
        true_run = MathTex(r"y = y_{\text{test}}", r"\ \Rightarrow\ ",
                           r"\{Z_1,\dots,Z_n,\, Z_{n+1}\}")\
            .scale(1.05).shift(UP * 1.5)
        true_run[0].set_color(EIG); true_run[2].set_color(VAR)
        tcap = Text("the augmented set is just the real n+1 patients",
                    font_size=23, color=DIM).next_to(true_run, DOWN, buff=0.25)
        self.play_beat(Write(true_run), FadeIn(tcap))                     # beat 2

        # exchangeability
        self.play(FadeOut(VGroup(true_run, tcap)), run_time=0.4)
        exch = MathTex(r"(Z_1,\dots,Z_{n+1})", r"\;\stackrel{d}{=}\;",
                       r"(Z_{\pi(1)},\dots,Z_{\pi(n+1)})")\
            .scale(1.0).shift(UP * 1.5)
        exch[0].set_color(VAR); exch[2].set_color(VAR)
        ecap = Text("Z are the patients;  pi is any reordering;  =d means same distribution\n"
                    "exchangeable: any reordering has the same law — order carries no information",
                    font_size=21, color=DIM, line_spacing=0.8)\
            .next_to(exch, DOWN, buff=0.3)
        self.play_beat(Write(exch), FadeIn(ecap))                         # beat 3

        # fixed symmetric score, no privileged view
        fixed = Text("the score is ONE fixed, symmetric function of all n+1 points",
                     font_size=25, color=WHITE).next_to(ecap, DOWN, buff=0.5)
        fcap = Text("the refit used every point together — no privileged view of the test point",
                    font_size=22, color=DIM).next_to(fixed, DOWN, buff=0.2)
        self.play_beat(FadeIn(fixed), FadeIn(fcap))                       # beat 4

        # exchangeable -> exchangeable rank
        self.play(FadeOut(VGroup(claim, exch, ecap, fixed, fcap)), run_time=0.5)
        chain = MathTex(r"\text{exch. points}", r"\Rightarrow",
                        r"\text{exch. scores}", r"\Rightarrow",
                        r"\text{exch. rank}").scale(0.95).shift(UP * 1.6)
        chain[0].set_color(VAR); chain[2].set_color(VAR); chain[4].set_color(RES)
        self.play_beat(Write(chain))                                      # beat 5

        # uniform rank
        unif = MathTex(r"\Pr(R = r)", r"=", r"\frac{1}{\,n+1\,}",
                       r",\quad r = 1,\dots,n+1")\
            .scale(1.05).next_to(chain, DOWN, buff=0.6)
        unif[0].set_color(RES); unif[2].set_color(RES)
        ucap = Text("the test score has no preferred position",
                    font_size=23, color=DIM).next_to(unif, DOWN, buff=0.25)
        self.play_beat(Write(unif), FadeIn(ucap))                         # beat 6

        # count: coverage = k/(n+1)
        count = MathTex(r"\Pr(\text{covered})", r"=", r"\Pr(R \le k)", r"=",
                        r"\frac{k}{\,n+1\,}",
                        r"=", r"\frac{\lceil (1-\alpha)(n+1) \rceil}{\,n+1\,}")\
            .scale(0.9).next_to(ucap, DOWN, buff=0.5)
        count[0].set_color(WHITE); count[4].set_color(RES); count[6].set_color(RES)
        self.play_beat(Write(count))                                      # beat 7

        # bound: >= 1 - alpha
        self.play(FadeOut(VGroup(chain, unif, ucap, count)), run_time=0.5)
        bound = MathTex(r"\frac{\lceil (1-\alpha)(n+1) \rceil}{n+1}",
                        r"\ \ge\ ", r"1-\alpha").scale(1.25).shift(UP * 0.6)
        bound[2].set_color(RES)
        box = SurroundingRectangle(bound, color=RES, buff=0.25)
        bmoral = Text("exact finite-sample coverage, distribution-free,\nusing ALL of the data",
                      font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(box, DOWN, buff=0.6)
        self.play_beat(Write(bound), Create(box), FadeIn(bmoral))         # beat 8


# ----------------------------------------------------------------------
# Scene 4 — designing the nonconformity score
# ----------------------------------------------------------------------
class S4_ScoreDesign(NarratedScene):
    scene_key = "S4_ScoreDesign"

    def construct(self):
        self.header("Designing the score")

        free = Text("the proof used only the ORDER of scores, never their values",
                    font_size=27, color=RES).shift(UP * 2.6)
        free2 = Text("→  design the score freely; validity always holds",
                     font_size=24, color=DIM).next_to(free, DOWN, buff=0.25)
        self.play_beat(FadeIn(free), FadeIn(free2))                       # beat 1

        # absolute residual
        self.play(FadeOut(VGroup(free, free2)), run_time=0.4)
        abs_s = MathTex(r"s(x,y)", r"=", r"\lvert\, y - \hat{y}\, \rvert")\
            .scale(1.2).shift(UP * 1.6)
        abs_s[0].set_color(VAR); abs_s[2].set_color(WHITE)
        ab = Brace(abs_s[2], DOWN, color=WHITE)
        al = Text("gap between truth and the model's point prediction",
                  font_size=22, color=DIM).next_to(ab, DOWN, buff=0.15)
        self.play_beat(Write(abs_s), GrowFromCenter(ab), FadeIn(al))      # beat 2

        # constant-width band
        band = MathTex(r"C(x)", r"=", r"\hat{y}", r"\pm", r"\hat{q}")\
            .scale(1.1).next_to(al, DOWN, buff=0.55)
        band[0].set_color(RES); band[4].set_color(EIG)
        bcap = Text("a CONSTANT-width band — same width for every patient",
                    font_size=23, color=DIM).next_to(band, DOWN, buff=0.2)
        self.play_beat(Write(band), FadeIn(bcap))                         # beat 3

        # crude -> want adaptive
        crude = VGroup(
            Text("constant width is crude:", font_size=25, color=BAD),
            Text("easy patients deserve tight bands, hard patients wide ones",
                 font_size=24, color=WHITE),
        ).arrange(DOWN, buff=0.2).next_to(bcap, DOWN, buff=0.5)
        self.play_beat(FadeIn(crude[0]), FadeIn(crude[1], shift=UP * 0.2))  # beat 4

        # normalized residual
        self.play(FadeOut(VGroup(abs_s, ab, al, band, bcap, crude)), run_time=0.5)
        norm = MathTex(r"s(x,y)", r"=", r"\frac{\lvert\, y - \hat{y}\, \rvert}"
                       r"{\hat{\sigma}(x)}").scale(1.25).shift(UP * 1.4)
        norm[0].set_color(VAR); norm[2].set_color(BACK)
        nb = Brace(norm[2], DOWN, color=BACK)
        nl = Text("divide by a learned local scale sigma-hat(x)\nlocally adaptive: the band breathes with difficulty",
                  font_size=22, color=BACK, line_spacing=0.8)\
            .next_to(nb, DOWN, buff=0.15)
        self.play_beat(Write(norm), GrowFromCenter(nb), FadeIn(nl))       # beat 5

        # signed CQR
        self.play(FadeOut(VGroup(norm, nb, nl)), run_time=0.4)
        cqr = MathTex(r"s = \max\big(\, \hat{q}_{\text{lo}} - y,\ "
                      r"y - \hat{q}_{\text{hi}} \,\big)")\
            .scale(1.05).shift(UP * 1.4)
        cqr.set_color(VAR)
        cl = Text("conformalized quantile regression (signed CQR):\nhow far OUTSIDE the low/high quantile pair the truth fell",
                  font_size=22, color=DIM, line_spacing=0.8)\
            .next_to(cqr, DOWN, buff=0.3)
        self.play_beat(Write(cqr), FadeIn(cl))                           # beat 6

        # each shapes the set, all valid
        self.play(FadeOut(VGroup(cqr, cl)), run_time=0.4)
        three = VGroup(
            Text("absolute residual  →  constant band", font_size=24, color=WHITE),
            Text("normalized residual  →  locally adaptive band", font_size=24, color=BACK),
            Text("signed CQR  →  asymmetric quantile band", font_size=24, color=VAR),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).shift(UP * 0.6)
        same = Text("every one inherits the SAME exact coverage guarantee",
                    font_size=25, color=RES).next_to(three, DOWN, buff=0.5)
        self.play_beat(FadeIn(three, lag_ratio=0.3), FadeIn(same))        # beat 7

        # separation: score=sharpness, rank=validity
        self.play(FadeOut(VGroup(three, same)), run_time=0.4)
        sep = VGroup(
            Text("the SCORE controls sharpness", font_size=27, color=VAR),
            Text("the RANK controls validity", font_size=27, color=RES),
            Text("swap the score freely — the guarantee does not move",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.2)
        self.play_beat(FadeIn(sep, lag_ratio=0.3))                        # beat 8


# ----------------------------------------------------------------------
# Scene 5 — the compute cost
# ----------------------------------------------------------------------
class S5_Cost(NarratedScene):
    scene_key = "S5_Cost"

    def construct(self):
        self.header("The compute cost")

        head = Text("full conformal pays its bill in REFITS",
                    font_size=30, color=BAD).shift(UP * 2.6)
        self.play_beat(FadeIn(head))                                      # beat 1

        # refits per candidate per test point
        cost = MathTex(r"\#\,\text{refits}", r"=",
                       r"(\#\,\text{candidate labels})", r"\times",
                       r"(\#\,\text{test patients})").scale(0.95).shift(UP * 1.4)
        cost[0].set_color(BAD); cost[2].set_color(EIG); cost[4].set_color(VAR)
        ccap = Text("binary AE: 2 refits per patient;  a fine regression grid: hundreds",
                    font_size=22, color=DIM).next_to(cost, DOWN, buff=0.3)
        self.play_beat(Write(cost), FadeIn(ccap))                        # beat 2

        blow = Text("a 1-minute model  →  hours or days across grid × cohort",
                    font_size=25, color=BAD).next_to(ccap, DOWN, buff=0.5)
        self.play_beat(FadeIn(blow, shift=UP * 0.2))                     # beat 3

        # split refits once
        self.play(FadeOut(VGroup(cost, ccap, blow)), run_time=0.5)
        split = VGroup(
            Text("often simply infeasible as written", font_size=26, color=BAD),
            Text("split conformal  →  refit ONCE, one held-out partition",
                 font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.2)
        self.play_beat(FadeIn(split[0]), FadeIn(split[1], shift=UP * 0.2))  # beat 4

        # CV+ / jackknife+ middle ground
        mid = VGroup(
            Text("CV+ / jackknife+  →  refit once per FOLD", font_size=25, color=BACK),
            Text("every patient calibrates out-of-fold", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(split, DOWN, buff=0.6)
        self.play_beat(FadeIn(mid, lag_ratio=0.3))                       # beat 5

        # the trade stated
        self.play(FadeOut(VGroup(split, mid)), run_time=0.5)
        trade = VGroup(
            Text("The trade:", font_size=28, color=RES),
            Text("full conformal spends COMPUTE to recover EFFICIENCY",
                 font_size=25, color=WHITE),
            Text("every point informs both the fit and the calibration",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.28).shift(UP * 0.7)
        self.play_beat(FadeIn(trade, lag_ratio=0.3))                     # beat 6

        worth = Text("worth it when: data is scarce, the model is cheap to refit,\n"
                     "and no calibration patient can be spared — the small-cohort regime",
                     font_size=24, color=BACK, line_spacing=0.8)\
            .next_to(trade, DOWN, buff=0.6)
        self.play_beat(FadeIn(worth, shift=UP * 0.2))                    # beat 7


# ----------------------------------------------------------------------
# Scene 6 — takeaway: name the hierarchy
# ----------------------------------------------------------------------
class S6_Takeaway(NarratedScene):
    scene_key = "S6_Takeaway"

    def construct(self):
        self.header("Takeaway")

        title = Text("Full conformal: the purest form", font_size=34, color=RES)\
            .shift(UP * 2.5)
        self.play_beat(FadeIn(title, shift=UP * 0.2))                     # beat 1

        all_data = Text("✓  all the data — no held-out pile wasted",
                        font_size=27, color=BACK).shift(UP * 1.4)
        self.play_beat(FadeIn(all_data, shift=RIGHT * 0.2))              # beat 2

        cover = MathTex(r"\checkmark\ \ \Pr(\text{covered})", r"\ge", r"1-\alpha")\
            .scale(1.05).next_to(all_data, DOWN, buff=0.45)
        cover[2].set_color(RES)
        ccap = Text("exact, finite-sample, distribution-free, any model",
                    font_size=22, color=DIM).next_to(cover, DOWN, buff=0.2)
        self.play_beat(Write(cover), FadeIn(ccap))                       # beat 3

        any_score = VGroup(
            Text("any score:", font_size=25, color=VAR),
            MathTex(r"\lvert y-\hat{y}\rvert,\ \ "
                    r"\frac{\lvert y-\hat{y}\rvert}{\hat{\sigma}(x)},\ \ "
                    r"\text{signed CQR}").scale(0.8).set_color(VAR),
        ).arrange(RIGHT, buff=0.3).next_to(ccap, DOWN, buff=0.45)
        rv = Text("validity rides the rank, sharpness rides the score",
                  font_size=22, color=DIM).next_to(any_score, DOWN, buff=0.2)
        self.play_beat(FadeIn(any_score), FadeIn(rv))                    # beat 4

        # split / CV+ are approximations
        self.play(FadeOut(VGroup(title, all_data, cover, ccap, any_score, rv)),
                  run_time=0.5)
        approx = Text("split and CV+ are practical APPROXIMATIONS of this ideal\n"
                      "— a little efficiency traded for huge compute savings",
                      font_size=26, color=WHITE, line_spacing=0.8).shift(UP * 1.9)
        self.play_beat(FadeIn(approx, shift=UP * 0.2))                   # beat 5

        # the hierarchy
        hier = VGroup(
            self._rung("FULL conformal", "all data · exact · any score", RES, 4.4),
            self._rung("CV+ / jackknife+", "once per fold · every point calibrates", BACK, 3.6),
            self._rung("SPLIT conformal", "refit once · cheapest", VAR, 2.8),
        ).arrange(DOWN, buff=0.3).next_to(approx, DOWN, buff=0.6)
        self.play_beat(FadeIn(hier, lag_ratio=0.3))                     # beat 6

        choose = Text("choose by budget — the guarantee is the same at every rung",
                      font_size=25, color=RES).next_to(hier, DOWN, buff=0.5)
        self.play_beat(FadeIn(choose, shift=UP * 0.2))                  # beat 7

    def _rung(self, name, sub, color, width):
        box = RoundedRectangle(width=width, height=0.85, corner_radius=0.12,
                               stroke_color=color, stroke_width=2.5,
                               fill_color=color, fill_opacity=0.12)
        t = VGroup(
            Text(name, font_size=22, color=color),
            Text(sub, font_size=15, color=DIM),
        ).arrange(DOWN, buff=0.08).move_to(box)
        return VGroup(box, t)
