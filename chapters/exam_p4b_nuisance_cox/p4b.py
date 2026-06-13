# -*- coding: utf-8 -*-
"""Problema 4 (b): parámetro de perturbación (nuisance) y condicionalidad de Cox.
  ./render.sh chapters/exam_p4b_nuisance_cox/p4b.py -q qh \
      P4B_Intuicion P4B_Setup P4B_Desarrollo P4B_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P4B_Intuicion(NarratedScene):
    scene_key = "P4B_Intuicion"

    def construct(self):
        title = Text("Problema 4 · (b)  Nuisance y Cox", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("Eliminar el parámetro de perturbación", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Identificar el nuisance ψ; reparametrizar (λ1,λ2)→(τ,ψ); ver que condicionar en "
            "SX+SY=n elimina ψ; conectar con Cox (1958).", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "Un nuisance no interesa pero ensucia la inferencia. Eliminarlo es una habilidad "
            "central en estadística.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = wrapt("Cox: condicionar en el « tamaño del experimento que ocurrió » (el total n). "
                     "Ahí ψ desaparece.", width=46, font_size=27, color=BACK, line_spacing=0.8)
        fitw(idea)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        syms = VGroup(
            MathTex(r"\tau:\ \text{interés}", font_size=32, color=VAR),
            MathTex(r"\psi=m\lambda_1+k\lambda_2:\ \text{perturbación}", font_size=32, color=BAD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.3)
        fitw(syms)
        self.play_beat(FadeOut(idea), FadeIn(syms))                                # 5

        idea2 = Text("Idea: reparametrizar → condicionar → Cox.",
                     font_size=26, color=VAR).shift(DOWN * 2.1)
        self.play_beat(FadeIn(idea2))                                              # 6

        self.play_beat(FadeOut(syms), FadeOut(idea2))                              # 7


class P4B_Setup(NarratedScene):
    scene_key = "P4B_Setup"

    def construct(self):
        self.header("Planteamiento · reparametrización")
        rep = MathTex(r"(\lambda_1,\lambda_2)\ \longleftrightarrow\ (\tau,\psi),"
                      r"\quad \psi=m\lambda_1+k\lambda_2", font_size=38).shift(UP * 1.5)
        fitw(rep)
        self.play_beat(Write(rep))                                                 # 1

        roles = VGroup(
            MathTex(r"\tau=\lambda_1/\lambda_2:\ \text{interés}", font_size=34, color=VAR),
            MathTex(r"\psi:\ \text{perturbación (}\propto\text{ media del total)}", font_size=34, color=BAD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 0.2)
        fitw(roles)
        self.play_beat(FadeIn(roles))                                              # 2

        sc = wrapt("(SX, SY) es suficiente y completo para (λ1, λ2): exponencial bivariada regular.",
                   width=48, font_size=26, color=BACK, line_spacing=0.8).shift(DOWN * 1.2)
        fitw(sc)
        self.play_beat(FadeIn(sc))                                                 # 3

        q = Text("¿Qué ocurre al condicionar en el total?", font_size=28, color=DIM).shift(DOWN * 2.3)
        self.play_beat(FadeIn(q))                                                  # 4

        self.play_beat(roles.animate.set_opacity(0.0), q.animate.set_opacity(0.0))  # 5


class P4B_Desarrollo(NarratedScene):
    scene_key = "P4B_Desarrollo"

    def construct(self):
        self.header("Desarrollo · el condicionamiento elimina ψ")
        l1 = MathTex(r"S_X\mid S_X+S_Y=n\ \sim\ \mathrm{Binomial}\bigl(n,\,p(\tau)\bigr)",
                     font_size=38).shift(UP * 2.0)
        fitw(l1)
        self.play_beat(Write(l1))                                                  # 1

        l2 = MathTex(r"p(\tau)=\frac{m\tau}{m\tau+k}\ \ \text{depende solo de }\tau",
                     font_size=36, color=BACK).shift(UP * 0.8)
        fitw(l2)
        self.play_beat(Write(l2))                                                  # 2

        l3 = MathTex(r"\Longrightarrow\ \text{el condicionamiento elimina }\psi",
                     font_size=36, color=RES).shift(UP * 0.0)
        fitw(l3)
        self.play_beat(Write(l3))                                                  # 3

        l4 = MathTex(r"N=S_X+S_Y\sim\mathrm{Poisson}(\psi)\ \ \text{(S-ancilar para }\tau)",
                     font_size=34, color=EIG).shift(DOWN * 1.1)
        fitw(l4)
        self.play_beat(FadeIn(l4))                                                 # 4

        cox = wrapt("Cox (1958): basar la inferencia de τ en el experimento condicional dado n.",
                    width=50, font_size=26, color=VAR, line_spacing=0.8).shift(DOWN * 2.2)
        fitw(cox)
        self.play_beat(FadeIn(cox))                                                # 5

        concl = Text("⇒ inferencia sobre τ libre de ψ.", font_size=28, color=RES).shift(DOWN * 3.1)
        self.play_beat(FadeOut(l1), FadeOut(l2), Write(concl))                     # 6


class P4B_Conclusion(NarratedScene):
    scene_key = "P4B_Conclusion"

    def construct(self):
        self.header("Conclusión")
        l1 = MathTex(r"\psi=m\lambda_1+k\lambda_2\ \ \text{es el nuisance}",
                     font_size=38, color=BAD).shift(UP * 1.6)
        fitw(l1)
        self.play_beat(Write(l1))                                                  # 1

        l2 = Text("condicionar en el total lo elimina, de forma exacta.",
                  font_size=27, color=BACK).shift(UP * 0.5)
        fitw(l2)
        self.play_beat(FadeIn(l2))                                                 # 2

        l3 = Text("Cox: usar el experimento efectivamente observado.",
                  font_size=27, color=VAR).shift(DOWN * 0.4)
        fitw(l3)
        self.play_beat(FadeIn(l3))                                                 # 3

        l4 = Text("Reparametrizar → suf-completo → condicionar → Cox.",
                  font_size=25, color=DIM).shift(DOWN * 1.3)
        fitw(l4)
        self.play_beat(FadeIn(l4))                                                 # 4

        moral = wrapt("Moraleja: si un estadístico ancilar fija el tamaño del experimento, "
                      "condicionar en él limpia la perturbación.", width=52, font_size=25,
                      color=RES, line_spacing=0.8).shift(DOWN * 2.7)
        fitw(moral)
        self.play_beat(FadeOut(l2), FadeOut(l3), FadeOut(l4), FadeIn(moral))       # 5
