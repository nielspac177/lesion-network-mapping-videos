"""c0404_steelman_second_reason — "Steelman, and the second reason".

Five narrated scenes. Steelman the location null (for a LOCATION claim it is the
right referee, and LNM average maps honestly fail it), show that the error is
using a location verdict to certify a SYMPTOM relationship, then give the
rebuttal full standing via a SECOND, independent reason: a random,
non-overlapping ensemble is the WRONG reference class for real lesions, which
overlap and are spatially non-random (Siddiqi et al. p.5). Both reasons push the
same direction: on average the location null under-rejects. Bridge to the
symptom null: change the question to a symptom-label contrast and the reference
to label permutations; the backbone cancels, signal survives, zero false
positives in 1000 iterations at t > 10.

All equations/numbers are page-cited in:
  responses/lnm_critique/sections/03_the_right_null.md
  responses/lnm_critique/papers/REBUTTAL_sound.md

Render (see render.sh):
  MEDIA=$HOME/lnm_media/c0404_steelman_second_reason ./render.sh \
      chapters/c0404_steelman_second_reason/scenes.py -q ql \
      S1_Steelman S2_RightToolWhen S3_WrongReference S4_TwoReasons S5_Bridge
"""

from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
from narration import SCENES

# Bind this chapter's narration to the shared engine for this render process.
NarratedScene.narration = SCENES


# ----------------------------------------------------------------------
# Scene 1 — Steelman the critique  (7 beats)
# ----------------------------------------------------------------------
class S1_Steelman(NarratedScene):
    scene_key = "S1_Steelman"

    def construct(self):
        title = Text("Steelman the critique", font_size=42, color=WHITE)
        sub = Text("its strongest form, given full standing",
                   font_size=24, color=DIM).next_to(title, DOWN)
        self.play_beat(Write(title), FadeIn(sub, shift=UP * 0.2))           # beat 1
        self.play(title.animate.scale(0.6).to_edge(UP), FadeOut(sub),
                  run_time=0.6)

        # a null is a question
        q = VGroup(
            Text("A null model is a question.", font_size=28, color=WHITE),
            Text("the random-lesion null asks:", font_size=25, color=DIM),
            Text("\"is the LOCATION of these lesions special?\"",
                 font_size=27, color=VAR),
        ).arrange(DOWN, buff=0.25).shift(UP * 0.9)
        self.play_beat(FadeIn(q[0]), FadeIn(q[1]), FadeIn(q[2]))            # beat 2

        proc = Text("scatter fake lesions → run LNM on each →\ndoes the real map stand out from the crowd of fakes?",
                    font_size=24, color=DIM, line_spacing=0.8)\
            .next_to(q, DOWN, buff=0.5)
        self.play_beat(FadeIn(proc, shift=UP * 0.2))                       # beat 3

        # the claim it correctly judges
        self.play(FadeOut(VGroup(q, proc)), run_time=0.5)
        claim = VGroup(
            Text("Suppose the claim really IS about location:", font_size=27, color=WHITE),
            Text("\"lesions HERE, not THERE, produce this network\"",
                 font_size=26, color=VAR),
        ).arrange(DOWN, buff=0.25).shift(UP * 1.1)
        self.play_beat(FadeIn(claim[0]), FadeIn(claim[1], shift=UP * 0.2))  # beat 4

        right = VGroup(
            Text("→ then the location null is the RIGHT referee",
                 font_size=27, color=BACK),
            Text("a valid test of the location hypothesis",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(claim, DOWN, buff=0.5)
        self.play_beat(FadeIn(right, shift=UP * 0.2))                      # beat 5

        # and the average maps honestly fail
        self.play(FadeOut(VGroup(claim, right)), run_time=0.5)
        fail1 = MathTex(r"70 \,/\, 78", r"\ \text{maps fail a random synthetic-lesion null}")\
            .scale(0.95).shift(UP * 0.8)
        fail1[0].set_color(BAD)
        f1cap = Text("(van den Heuvel et al., P1 p.1244)",
                     font_size=22, color=DIM).next_to(fail1, DOWN, buff=0.25)
        self.play_beat(Write(fail1), FadeIn(f1cap))                        # beat 6

        fail2 = MathTex(r"71 \,/\, 78", r"\ \text{fail a modular-prevalence location-permutation null}")\
            .scale(0.9).next_to(f1cap, DOWN, buff=0.6)
        fail2[0].set_color(BAD)
        concede = Text("On a LOCATION claim, the LNM average maps genuinely fail.  We concede this fully.",
                       font_size=24, color=RES).next_to(fail2, DOWN, buff=0.5)
        self.play_beat(Write(fail2), FadeIn(concede))                      # beat 7


# ----------------------------------------------------------------------
# Scene 2 — The right tool, for the right claim  (7 beats)
# ----------------------------------------------------------------------
class S2_RightToolWhen(NarratedScene):
    scene_key = "S2_RightToolWhen"

    def construct(self):
        self.header("The right tool, for the right claim")

        intro = Text("the location null is not broken — it is valid and well-aimed,\nas long as the claim really is about location",
                     font_size=26, color=WHITE, line_spacing=0.8).shift(UP * 2.1)
        self.play_beat(FadeIn(intro))                                      # beat 1

        verdict = VGroup(
            Text("claim:  \"this location is special\"", font_size=26, color=VAR),
            Text("location null correctly says:  NO", font_size=27, color=BACK),
            Text("(for scattered cortical lesions sampling one connectome)",
                 font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.22).shift(UP * 0.2)
        self.play_beat(FadeIn(verdict, lag_ratio=0.3))                     # beat 2

        # why: the backbone makes all locations alike
        self.play(FadeOut(VGroup(intro, verdict)), run_time=0.5)
        why = MathTex(r"m_\ell", r"\approx", r"\lambda_1", r"(u_1^\top \ell)\,", "u_1")\
            .scale(1.2).shift(UP * 1.4)
        why[0].set_color(VAR); why[2].set_color(EIG); why[4].set_color(BACK)
        legend = VGroup(
            Text("m_ℓ = the seed's network map", font_size=20, color=VAR),
            Text("λ₁ = top eigenvalue   u₁ᵀℓ = how much lesion ℓ projects onto u₁",
                 font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.15).next_to(why, UP, buff=0.35)
        br = Brace(why[4], DOWN, color=BACK)
        brlab = Text("u₁ = the same fixed direction for almost every seed",
                     font_size=22, color=BACK).next_to(br, DOWN, buff=0.2)
        self.play_beat(Write(why), FadeIn(legend),
                       GrowFromCenter(br), FadeIn(brlab))                  # beat 3

        glued = Text("so fake maps ≈ real map → observed value sits dead-center\nin the null → nothing rejects, and rightly so",
                     font_size=25, color=WHITE, line_spacing=0.8)\
            .next_to(brlab, DOWN, buff=0.5)
        self.play_beat(FadeIn(glued, shift=UP * 0.2))                      # beat 4

        # honest failure — the error is downstream
        self.play(FadeOut(VGroup(why, legend, br, brlab, glued)), run_time=0.5)
        honest = Text("That is the HONEST failure of a real claim.",
                      font_size=28, color=WHITE).shift(UP * 1.6)
        self.play_beat(FadeIn(honest, shift=UP * 0.2))                     # beat 5

        over = VGroup(
            Text("✗ the over-reach:", font_size=26, color=BAD),
            Text("using the LOCATION verdict to certify — or deny —", font_size=25, color=WHITE),
            Text("a SYMPTOM relationship.  A different claim entirely.", font_size=25, color=WHITE),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).next_to(honest, DOWN, buff=0.5)
        self.play_beat(FadeIn(over, shift=UP * 0.2))                       # beat 6

        misread = VGroup(
            Text("\"the location test is non-significant\"", font_size=24, color=DIM),
            Text("misread as  →  \"LNM doesn't work\"", font_size=25, color=BAD),
            Text("truth  →  the location question was the wrong one to ask",
                 font_size=25, color=RES),
        ).arrange(DOWN, buff=0.2).next_to(over, DOWN, buff=0.5)
        self.play_beat(FadeIn(misread, lag_ratio=0.3))                     # beat 7


# ----------------------------------------------------------------------
# Scene 3 — The wrong reference class  (8 beats)
# ----------------------------------------------------------------------
class S3_WrongReference(NarratedScene):
    scene_key = "S3_WrongReference"

    def construct(self):
        self.header("The wrong reference class  (Siddiqi et al., p.5)")

        intro = Text("a SECOND, independent reason — and this one is the responders',\nnot ours",
                     font_size=26, color=WHITE, line_spacing=0.8).shift(UP * 2.2)
        self.play_beat(FadeIn(intro))                                      # beat 1

        ens = VGroup(
            Text("the random ensemble R scatters lesions", font_size=26, color=WHITE),
            Text("RANDOMLY  and  NON-OVERLAPPING", font_size=27, color=DIM),
            Text("that is its built-in reference population", font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).shift(UP * 0.5)
        self.play_beat(FadeIn(ens, lag_ratio=0.3))                         # beat 2

        # but real lesions overlap and are non-random
        self.play(FadeOut(VGroup(intro, ens)), run_time=0.5)
        real = Text("\"actual lesions causing specific symptoms ... do overlap\nand their spatial distributions are not random\"",
                    font_size=25, color=WHITE, line_spacing=0.8).shift(UP * 1.7)
        realcap = Text("— Siddiqi et al., p.5", font_size=22, color=DIM)\
            .next_to(real, DOWN, buff=0.25)
        self.play_beat(FadeIn(real), FadeIn(realcap))                      # beat 3

        amnesia = VGroup(
            Text("amnesia lesions repeatedly sample the hippocampus", font_size=24, color=VAR),
            Text("and are unlikely to sample the motor cortex", font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(realcap, DOWN, buff=0.5)
        self.play_beat(FadeIn(amnesia, shift=UP * 0.2))                    # beat 4

        # the discount
        self.play(FadeOut(VGroup(real, realcap, amnesia)), run_time=0.5)
        discount = Text("a null of random, non-overlapping blobs DISCOUNTS exactly\nthe structure that makes a symptom-causing lesion set special",
                        font_size=25, color=WHITE, line_spacing=0.8).shift(UP * 1.6)
        self.play_beat(FadeIn(discount, shift=UP * 0.2))                   # beat 5

        impossible = VGroup(
            Text("it models an IMPOSSIBLE population:", font_size=27, color=BAD),
            Text("scattered, independent lesions no real disease produces", font_size=24, color=WHITE),
            Text("→ the reference class is simply wrong", font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.2).next_to(discount, DOWN, buff=0.5)
        self.play_beat(FadeIn(impossible, lag_ratio=0.3))                  # beat 6

        # the FPR trace
        self.play(FadeOut(VGroup(discount, impossible)), run_time=0.5)
        trace = VGroup(
            Text("the rebuttal traces P1's headline false-positive rate to this:",
                 font_size=25, color=WHITE),
            Text("high FPR  ⇐  a simulation assuming HIGH lesion overlap",
                 font_size=25, color=BAD),
        ).arrange(DOWN, buff=0.3).shift(UP * 1.0)
        self.play_beat(FadeIn(trace[0]), FadeIn(trace[1], shift=UP * 0.2)) # beat 7

        collapse = VGroup(
            Text("LOW overlap  (randomly drawn real lesions)", font_size=25, color=WHITE),
            Text("→ the false-positive rate COLLAPSES", font_size=26, color=BACK),
            Text("(REBUTTAL p.3 — the number is coming in Scene 5)", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.22).next_to(trace, DOWN, buff=0.6)
        self.play_beat(FadeIn(collapse, lag_ratio=0.3))                    # beat 8


# ----------------------------------------------------------------------
# Scene 4 — Two reasons, same direction  (7 beats)
# ----------------------------------------------------------------------
class S4_TwoReasons(NarratedScene):
    scene_key = "S4_TwoReasons"

    def construct(self):
        self.header("Two reasons, same direction")

        intro = Text("two independent reasons — both push the location null the SAME way",
                     font_size=27, color=WHITE).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # build the two columns
        head1 = Text("REASON 1 — the QUESTION", font_size=26, color=VAR)\
            .shift(LEFT * 3.4 + UP * 1.5)
        body1 = Text("backbone blurs all\nlocations alike →\n\"is this place special?\"\ncan never reject",
                     font_size=22, color=WHITE, line_spacing=0.85)\
            .next_to(head1, DOWN, buff=0.3)
        self.play_beat(FadeIn(head1), FadeIn(body1, shift=UP * 0.2))       # beat 2

        ours = Text("ours:  location vs symptom\nwrong question → guaranteed non-rejection",
                    font_size=21, color=DIM, line_spacing=0.85)\
            .next_to(body1, DOWN, buff=0.4)
        self.play_beat(FadeIn(ours, shift=UP * 0.2))                       # beat 3

        head2 = Text("REASON 2 — the REFERENCE", font_size=26, color=BACK)\
            .shift(RIGHT * 3.4 + UP * 1.5)
        body2 = Text("random, non-overlapping\nensemble is the wrong\ncomparison population\nfor real lesions",
                     font_size=22, color=WHITE, line_spacing=0.85)\
            .next_to(head2, DOWN, buff=0.3)
        divider = Line(UP * 2.0, DOWN * 2.6, color=DIM, stroke_width=1)
        self.play_beat(Create(divider), FadeIn(head2), FadeIn(body2, shift=UP * 0.2))  # beat 4

        theirs = Text("theirs:  random vs real\nnull models a population that does not exist",
                      font_size=21, color=DIM, line_spacing=0.85)\
            .next_to(body2, DOWN, buff=0.4)
        self.play_beat(FadeIn(theirs, shift=UP * 0.2))                     # beat 5

        # either alone, together
        self.play(FadeOut(VGroup(head1, body1, ours, head2, body2, theirs,
                                 divider, intro)), run_time=0.5)
        joint = VGroup(
            Text("either reason alone  →  the location null is the wrong question",
                 font_size=26, color=WHITE),
            Text("together  →  the OBVIOUSLY wrong one", font_size=27, color=RES),
        ).arrange(DOWN, buff=0.3).shift(UP * 0.9)
        self.play_beat(FadeIn(joint[0]), FadeIn(joint[1], shift=UP * 0.2)) # beat 6

        same = VGroup(
            Text("same direction:  on average, the location null UNDER-REJECTS",
                 font_size=26, color=BAD),
            Text("it will miss a true lesion–symptom signal even when one is there",
                 font_size=24, color=DIM),
        ).arrange(DOWN, buff=0.25).next_to(joint, DOWN, buff=0.6)
        self.play_beat(FadeIn(same, shift=UP * 0.2))                       # beat 7


# ----------------------------------------------------------------------
# Scene 5 — Bridge to the symptom null  (7 beats)
# ----------------------------------------------------------------------
class S5_Bridge(NarratedScene):
    scene_key = "S5_Bridge"

    def construct(self):
        self.header("Bridge to the symptom null  →  Part 5")

        intro = Text("the fix is two moves:  change the QUESTION, change the REFERENCE",
                     font_size=27, color=WHITE).shift(UP * 2.6)
        self.play_beat(FadeIn(intro))                                      # beat 1

        # move 1: the question
        m1 = VGroup(
            Text("1.  question  →  a SYMPTOM-LABEL CONTRAST", font_size=26, color=VAR),
            Text("\"do these labels track these fixed lesions more than chance allows?\"",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).shift(UP * 1.4)
        self.play_beat(FadeIn(m1, shift=UP * 0.2))                         # beat 2

        m2 = VGroup(
            Text("2.  reference  →  LABEL PERMUTATIONS", font_size=26, color=BACK),
            Text("keep every lesion in place; only shuffle impaired vs spared",
                 font_size=23, color=DIM),
        ).arrange(DOWN, buff=0.2).next_to(m1, DOWN, buff=0.5)
        self.play_beat(FadeIn(m2, shift=UP * 0.2))                         # beat 3

        # the cancellation
        self.play(FadeOut(VGroup(intro, m1, m2)), run_time=0.5)
        decomp = MathTex("x_i", "=", r"\underbrace{\beta_i\, u_1}_{\text{backbone, label-free}}",
                         "+", "r_i").scale(1.1).shift(UP * 1.3)
        decomp[0].set_color(VAR); decomp[2].set_color(BACK); decomp[4].set_color(RES)
        dleg = VGroup(
            Text("x_i = patient i's fixed map    β_i = backbone loading (lesion-only)",
                 font_size=20, color=DIM),
            Text("u₁ = backbone direction    r_i = residual (the label-sensitive part)",
                 font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.15).next_to(decomp, DOWN, buff=0.45)
        self.play_beat(Write(decomp), FadeIn(dleg))                        # beat 4

        cancel = MathTex(r"\bar{x}^{(1)}", "-", r"\bar{x}^{(0)}", "=",
                         r"\underbrace{(\bar\beta^{(1)}-\bar\beta^{(0)})\,u_1}_{\text{cancels}}",
                         "+", r"(\bar r^{(1)} - \bar r^{(0)})").scale(0.9)
        cancel[4].set_color(BACK); cancel[6].set_color(RES)
        cancel.next_to(dleg, DOWN, buff=0.5)
        strike = Line(cancel[4].get_corner(DL), cancel[4].get_corner(UR),
                      color=BAD, stroke_width=4)
        cancap = Text("label-independent → identical on both sides → cancels EXACTLY",
                      font_size=23, color=WHITE).next_to(cancel, DOWN, buff=0.3)
        self.play_beat(Write(cancel), Create(strike), FadeIn(cancap))      # beat 5

        # the witness
        self.play(FadeOut(VGroup(decomp, dleg, cancel, strike, cancap)),
                  run_time=0.5)
        witness = MathTex(r"t > 10:\quad", r"0\ \text{false positives}",
                          r"\ /\ 1000\ \text{iterations}").scale(1.1).shift(UP * 0.9)
        witness[1].set_color(RES)
        wbox = SurroundingRectangle(witness, color=RES, buff=0.2)
        wcap = Text("t = the specificity two-sample t-statistic; t > 10 is the standard threshold\n(REBUTTAL p.3)",
                    font_size=21, color=DIM, line_spacing=0.8)\
            .next_to(witness, DOWN, buff=0.3)
        self.play_beat(Write(witness), Create(wbox), FadeIn(wcap))         # beat 6

        leak = MathTex(r"t = 3.0:\quad", r"4.6\%\ \text{leakage}",
                       r"\ \text{(sub-standard threshold only)}").scale(0.9)
        leak[1].set_color(BAD)
        leak.next_to(wcap, DOWN, buff=0.6)
        lead = Text("change the question, change the reference — Part 5 proves all of this",
                    font_size=24, color=RES).next_to(leak, DOWN, buff=0.5)
        self.play_beat(Write(leak), FadeIn(lead))                          # beat 7
