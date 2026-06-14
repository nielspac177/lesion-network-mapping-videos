"""c0403_specificity_collapse — "Why specificity collapses".

Five narrated scenes. We follow ONE failing question, the random-lesion / location
null, down a chain of links to its collapse, then fence the scope:

  R1 (alignment bound)  =>  every random seed is backbone-shaped
                        =>  T^(b) ~ T_obs (fakes reproduce the map)
                        =>  the null never rejects (p large by construction)
                        =>  specificity collapses — but ONLY for the LOCATION null
                            on the GROUP-AVERAGE map. The symptom CONTRAST under a
                            label null is a different object and is untouched.

All equations / numbers are page-cited in:
  responses/lnm_critique/sections/03_the_right_null.md
  responses/lnm_critique/sections/02_what_is_entailed.md
  responses/lnm_critique/papers/P1_critique.md   (70/78 and 71/78, p.1244)

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0403_specificity_collapse ./render.sh \
      chapters/c0403_specificity_collapse/scenes.py -q ql \
      S1_Chain S2_R1Recall S3_FakesMatch S4_NoRejection S5_Evidence
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — the collapse, previewed as a chain of links
# ----------------------------------------------------------------------
class S1_Chain(NarratedScene):
    scene_key = "S1_Chain"

    def construct(self):
        title = Text("The collapse, as a chain", font_size=42, color=WHITE)
        sub = Text("five links, one failing question", font_size=24, color=DIM)\
            .next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # Build the chain link by link, each on its own beat.
        l1 = self._link("R1", "every lesion map sits near the backbone  u_1", BACK)
        l2 = self._link("seeds", "every random seed lands near  u_1  too", VAR)
        l3 = self._link("fakes", r"so  T^{(b)}  \approx  T_{\text{obs}}", EIG, math=True)
        l4 = self._link("null", "fakes match  =>  the null cannot reject", BAD)
        l5 = self._link("collapse", "specificity falls — for THIS null, THIS map", RES)

        chain = VGroup(l1, l2, l3, l4, l5).arrange(DOWN, buff=0.34,
                                                    aligned_edge=LEFT).shift(DOWN * 0.2)
        arrows = VGroup(*[
            Arrow(chain[i].get_bottom(), chain[i + 1].get_top(),
                  color=DIM, buff=0.06, stroke_width=2.5,
                  max_tip_length_to_length_ratio=0.18)
            for i in range(4)
        ])

        self.play_beat(FadeIn(l1, shift=RIGHT * 0.2))                       # beat 2
        self.play_beat(GrowArrow(arrows[0]), FadeIn(l2, shift=RIGHT * 0.2)) # beat 3
        self.play_beat(GrowArrow(arrows[1]), FadeIn(l3, shift=RIGHT * 0.2)) # beat 4
        self.play_beat(GrowArrow(arrows[2]), FadeIn(l4, shift=RIGHT * 0.2)) # beat 5
        self.play_beat(GrowArrow(arrows[3]), FadeIn(l5, shift=RIGHT * 0.2),
                       l5.animate.set_opacity(1.0))                         # beat 6

    def _link(self, tag, body, color, math=False):
        chip = VGroup(
            RoundedRectangle(width=1.9, height=0.6, corner_radius=0.12,
                             stroke_color=color, stroke_width=2,
                             fill_color=color, fill_opacity=0.14),
            Text(tag, font_size=22, color=color),
        )
        chip[1].move_to(chip[0])
        if math:
            txt = MathTex(body, color=WHITE).scale(0.75)
        else:
            txt = Text(body, font_size=23, color=WHITE)
        row = VGroup(chip, txt).arrange(RIGHT, buff=0.4)
        return row


# ----------------------------------------------------------------------
# Scene 2 — recall the alignment bound R1
# ----------------------------------------------------------------------
class S2_R1Recall(NarratedScene):
    scene_key = "S2_R1Recall"

    def construct(self):
        self.header("Recall the alignment bound  (R1)")

        intro = Text("link one: theorem R1, proved earlier",
                     font_size=28, color=DIM).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # theta_ell = angle(m_ell, u_1)
        defn = MathTex(r"\theta_\ell", "=", r"\angle\big(", r"m_\ell", ",", "u_1",
                       r"\big)").scale(1.15).shift(UP * 1.5)
        defn[0].set_color(RES); defn[3].set_color(VAR); defn[5].set_color(BACK)
        dcap = Text("angle between a lesion's map and the backbone",
                    font_size=22, color=DIM).next_to(defn, DOWN, buff=0.25)
        self.play_beat(Write(defn), FadeIn(dcap))                          # beat 2

        # the bound itself
        self.play(FadeOut(VGroup(intro, dcap)), defn.animate.scale(0.7).to_edge(UP, buff=1.0),
                  run_time=0.5)
        bound = MathTex(r"\tan", r"\theta_\ell", r"\ \le\ ",
                        r"\frac{\lambda_2}{\lambda_1}",
                        r"\cdot",
                        r"\frac{\lVert \ell_\perp \rVert}{\lvert u_1^{\top}\ell \rvert}")\
            .scale(1.25).shift(UP * 0.5)
        bound[1].set_color(RES); bound[3].set_color(EIG); bound[5].set_color(VAR)
        self.play_beat(Write(bound))                                       # beat 3

        # annotate the spectral gap
        br_gap = Brace(bound[3], DOWN, color=EIG)
        gap_lab = Text("spectral gap:  lambda_1, lambda_2 = top eigenvalues of C",
                       font_size=21, color=EIG).next_to(br_gap, DOWN, buff=0.18)
        self.play_beat(GrowFromCenter(br_gap), FadeIn(gap_lab))            # beat 4

        # annotate the seed ratio
        self.play(FadeOut(VGroup(br_gap, gap_lab)), run_time=0.35)
        br_seed = Brace(bound[5], DOWN, color=VAR)
        seed_lab = Text("ell_perp = lesion mass off u_1   /   u_1^T ell = overlap with u_1",
                        font_size=21, color=VAR).next_to(br_seed, DOWN, buff=0.18)
        self.play_beat(GrowFromCenter(br_seed), FadeIn(seed_lab))          # beat 5

        # small gap -> small bound
        self.play(FadeOut(VGroup(br_seed, seed_lab)), run_time=0.35)
        small = MathTex(r"\frac{\lambda_2}{\lambda_1}\ \text{small}",
                        r"\ \Longrightarrow\ ",
                        r"\tan\theta_\ell\ \text{small}")\
            .scale(1.0).next_to(bound, DOWN, buff=0.7)
        small[0].set_color(EIG); small[2].set_color(RES)
        self.play_beat(Write(small))                                       # beat 6

        # tiny angle -> narrow cone
        cone = Text("tiny angle  =>  every map lives in a narrow cone hugging u_1",
                    font_size=24, color=BACK).next_to(small, DOWN, buff=0.55)
        self.play_beat(FadeIn(cone, shift=UP * 0.2))                       # beat 7


# ----------------------------------------------------------------------
# Scene 3 — fakes reproduce the map: T^(b) ~ T_obs
# ----------------------------------------------------------------------
class S3_FakesMatch(NarratedScene):
    scene_key = "S3_FakesMatch"

    def construct(self):
        self.header("Fakes reproduce the map")

        # The ensemble of fake seeds.
        ens = MathTex(r"\ell^{(1)}", ",", r"\ell^{(2)}", r",\ \dots\ ,",
                      r"\ell^{(B)}").scale(1.1).shift(UP * 2.4)
        for i in (0, 2, 4):
            ens[i].set_color(VAR)
        ens_cap = Text("random seeds drawn for the location null",
                       font_size=22, color=DIM).next_to(ens, DOWN, buff=0.2)
        self.play_beat(Write(ens), FadeIn(ens_cap))                        # beat 1

        # Each fake obeys R1.
        r1 = MathTex(r"\text{each }", r"\ell^{(b)}", r"\ \text{has nonzero }",
                     r"\lvert u_1^{\top}\ell^{(b)}\rvert",
                     r"\ \Rightarrow\ \text{obeys R1}").scale(0.85)\
            .next_to(ens_cap, DOWN, buff=0.35)
        r1[1].set_color(VAR); r1[3].set_color(BACK)
        self.play_beat(FadeIn(r1, shift=UP * 0.2))                         # beat 2

        # The cone picture: backbone axis + observed + fakes.
        self.play(FadeOut(VGroup(ens, ens_cap, r1)), run_time=0.4)
        axis = Arrow(ORIGIN, RIGHT * 4.2, color=BACK, buff=0,
                     stroke_width=4).shift(LEFT * 2.2 + DOWN * 0.3)
        axis_lab = MathTex("u_1", color=BACK).scale(0.9).next_to(axis, RIGHT, buff=0.15)
        # narrow cone edges
        origin = axis.get_start()
        c_up = DashedLine(origin, origin + np.array([3.9, 0.85, 0]), color=DIM,
                          stroke_width=1.6)
        c_dn = DashedLine(origin, origin + np.array([3.9, -0.85, 0]), color=DIM,
                          stroke_width=1.6)
        cone = VGroup(axis, axis_lab, c_up, c_dn)
        self.play_beat(Create(axis), FadeIn(axis_lab),
                       Create(c_up), Create(c_dn))                         # beat 3

        # observed map vector + a fan of fakes, all inside the cone.
        obs_vec = Arrow(origin, origin + np.array([3.4, 0.30, 0]),
                        color=RES, buff=0, stroke_width=5)
        obs_lab = MathTex(r"m_{\text{obs}}", color=RES).scale(0.8)\
            .next_to(obs_vec.get_end(), UR, buff=0.08)
        fakes = VGroup(*[
            Arrow(origin, origin + np.array([3.4, dy, 0]),
                  color=VAR, buff=0, stroke_width=2.5, fill_opacity=0.8)
            for dy in (-0.55, -0.30, 0.05, 0.45, 0.62)
        ])
        self.play_beat(GrowArrow(obs_vec), FadeIn(obs_lab),
                       LaggedStart(*[GrowArrow(f) for f in fakes], lag_ratio=0.15))  # beat 4

        # Summarize each map by one number T.
        Tdef = MathTex("T", "=", r"\cos\angle\big(", r"m", ",", "u_1", r"\big)")\
            .scale(0.95).to_edge(DOWN, buff=1.5)
        Tdef[0].set_color(EIG); Tdef[3].set_color(VAR); Tdef[5].set_color(BACK)
        Tcap = Text("T = how backbone-shaped a map is", font_size=21, color=DIM)\
            .next_to(Tdef, DOWN, buff=0.18)
        self.play_beat(Write(Tdef), FadeIn(Tcap))                          # beat 5

        # T^(b) close to T_obs
        self.play(FadeOut(VGroup(cone, obs_vec, obs_lab, fakes, Tcap)),
                  Tdef.animate.to_edge(UP, buff=1.2), run_time=0.5)
        near = MathTex(r"T^{(b)}", r"\ \approx\ ", r"T_{\text{obs}}",
                       r"\quad\text{for nearly every }", "b")\
            .scale(1.1).shift(UP * 0.3)
        near[0].set_color(VAR); near[2].set_color(RES); near[4].set_color(VAR)
        self.play_beat(Write(near))                                        # beat 6

        moral = Text("the whole crowd of fakes reproduces the observed map",
                     font_size=25, color=WHITE).next_to(near, DOWN, buff=0.6)
        self.play_beat(FadeIn(moral, shift=UP * 0.2))                      # beat 7


# ----------------------------------------------------------------------
# Scene 4 — nothing rejects: the p-value is large by construction
# ----------------------------------------------------------------------
class S4_NoRejection(NarratedScene):
    scene_key = "S4_NoRejection"

    def construct(self):
        self.header("Nothing rejects")

        # the p-value definition
        pdef = MathTex("p", "=", r"\frac{1}{B}\sum_{b}",
                       r"\mathbf{1}\!\left[\,", r"T^{(b)}", r"\ \ge\ ",
                       r"T_{\text{obs}}", r"\,\right]")\
            .scale(1.0).shift(UP * 2.3)
        pdef[0].set_color(EIG); pdef[4].set_color(VAR); pdef[6].set_color(RES)
        # decode the averaged indicator: 1/B sum_b of 1[T^(b) >= T_obs]
        br_p = Brace(VGroup(pdef[2], pdef[3], pdef[7]), DOWN, color=DIM)
        plab = Text("(1/B) * (# of fakes with T^(b) >= T_obs)  =  the indicator, averaged",
                    font_size=19, color=DIM).next_to(br_p, DOWN, buff=0.14)
        pcap = Text("p = right-tail rank of T_obs among the fakes",
                    font_size=22, color=DIM).next_to(plab, DOWN, buff=0.18)
        self.play_beat(Write(pdef), GrowFromCenter(br_p),
                       FadeIn(plab), FadeIn(pcap))                          # beat 1

        # the histogram: fakes piled at T_obs
        self.play(FadeOut(VGroup(pcap, br_p, plab)),
                  pdef.animate.scale(0.8).to_edge(UP, buff=1.0),
                  run_time=0.5)
        axes = Axes(x_range=[0, 1, 0.25], y_range=[0, 1.0, 0.5],
                    x_length=7.2, y_length=2.7,
                    axis_config={"include_tip": False, "color": DIM}).shift(DOWN * 0.5)
        xlab = Text("T  (backbone-shape score)", font_size=20, color=DIM)\
            .next_to(axes, DOWN, buff=0.2)
        # a sharp pile of fakes near T = 0.8
        bars = VGroup()
        heights = [0.05, 0.12, 0.35, 0.78, 0.95, 0.6, 0.18, 0.05]
        for i, h in enumerate(heights):
            xc = 0.45 + i * 0.07
            bar = Rectangle(width=0.34, height=h * 2.2, stroke_width=0,
                            fill_color=VAR, fill_opacity=0.65)
            bar.move_to(axes.c2p(xc, 0), aligned_edge=DOWN)
            bars.add(bar)
        self.play_beat(Create(axes), FadeIn(xlab),
                       LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars],
                                   lag_ratio=0.08))                        # beat 2

        # observed line sits inside the pile
        obs_x = 0.45 + 4 * 0.07
        obs_line = DashedLine(axes.c2p(obs_x, 0), axes.c2p(obs_x, 1.0),
                              color=RES, stroke_width=3)
        obs_lab = MathTex(r"T_{\text{obs}}", color=RES).scale(0.75)\
            .next_to(axes.c2p(obs_x, 1.0), UP, buff=0.1)
        self.play_beat(Create(obs_line), FadeIn(obs_lab))                  # beat 3

        # large p by construction
        big = MathTex(r"\Rightarrow\ ", "p", r"\ \text{large by construction}")\
            .scale(0.95).to_edge(DOWN, buff=0.95)
        big[1].set_color(BAD)
        self.play_beat(FadeIn(big, shift=UP * 0.2))                        # beat 4

        # cannot tell real from fake average map
        self.play(FadeOut(VGroup(axes, xlab, bars, obs_line, obs_lab, big)),
                  run_time=0.5)
        cannot = VGroup(
            Text("the location null cannot tell", font_size=27, color=WHITE),
            Text("a real AVERAGE map  from  a fake AVERAGE map", font_size=27, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.3)
        self.play_beat(FadeIn(cannot[0]), FadeIn(cannot[1], shift=UP * 0.2))  # beat 5

        spec = Text("specificity  ->  the floor   (for this null)",
                    font_size=26, color=RES).next_to(cannot, DOWN, buff=0.6)
        self.play_beat(FadeIn(spec, shift=UP * 0.2))                       # beat 6


# ----------------------------------------------------------------------
# Scene 5 — P1's own numbers, and the scope of the collapse
# ----------------------------------------------------------------------
class S5_Evidence(NarratedScene):
    scene_key = "S5_Evidence"

    def construct(self):
        self.header("P1's own failure counts  (P1, p.1244)")

        intro = Text("the critique's own re-analysis is the witness",
                     font_size=28, color=DIM).shift(UP * 2.5)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # 70/78 synthetic-lesion null
        f1 = VGroup(
            MathTex(r"70\,/\,78", color=BAD).scale(1.25),
            Text("maps fail a random synthetic-lesion null", font_size=24, color=WHITE),
            Text("(nominal two-sided alpha = 0.05, uncorrected)", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.18).shift(UP * 0.9)
        self.play_beat(Write(f1[0]), FadeIn(f1[1]), FadeIn(f1[2]))          # beat 2

        # 71/78 modular-prevalence permutation null
        f2 = VGroup(
            MathTex(r"71\,/\,78", color=BAD).scale(1.25),
            Text("fail a location-permutation null preserving modular prevalence",
                 font_size=24, color=WHITE),
            Text("(P_FDR > 0.05;  Supp. Note 16)", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.18).next_to(f1, DOWN, buff=0.5)
        self.play_beat(Write(f2[0]), FadeIn(f2[1]), FadeIn(f2[2]))          # beat 3

        # matches the prediction
        pred = Text("almost nothing rejects — exactly what the chain predicted",
                    font_size=24, color=RES).to_edge(DOWN, buff=0.8)
        self.play_beat(FadeIn(pred, shift=UP * 0.2))                       # beat 4

        # SCOPE: this indicts only the location null on the average map
        self.play(FadeOut(VGroup(intro, f1, f2, pred)), run_time=0.5)
        scope = VGroup(
            Text("Scope of the collapse:", font_size=28, color=RES),
            Text("indicts the LOCATION null on the GROUP-AVERAGE map", font_size=26, color=BAD),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.3)
        self.play_beat(FadeIn(scope[0]), FadeIn(scope[1], shift=UP * 0.2))  # beat 5

        # different object: the symptom contrast under a label null
        split = VGroup(
            VGroup(
                Text("AVERAGE  +  location null", font_size=24, color=DIM),
                Text("backbone DOMINATES  ->  collapses", font_size=23, color=BAD),
            ).arrange(DOWN, buff=0.15),
            MathTex(r"\neq", color=RES).scale(1.4),
            VGroup(
                Text("CONTRAST  +  label null", font_size=24, color=BACK),
                Text("backbone CANCELS  ->  survives", font_size=23, color=BACK),
            ).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=0.8).next_to(scope, DOWN, buff=0.6)
        self.play_beat(FadeIn(split, lag_ratio=0.2))                       # beat 6
