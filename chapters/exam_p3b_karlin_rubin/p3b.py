# -*- coding: utf-8 -*-
"""Problema 3 (b): test UMP aleatorizado (Karlin-Rubin) y fórmula de γα.
  ./render.sh chapters/exam_p3b_karlin_rubin/p3b.py -q qh \
      P3B_Intuicion P3B_Setup P3B_Desarrollo P3B_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P3B_Intuicion(NarratedScene):
    scene_key = "P3B_Intuicion"

    def construct(self):
        title = Text("Problema 3 · (b)  Test UMP (Karlin–Rubin)", font_size=32, color=RES).to_edge(UP, buff=0.5)
        sub = Text("Aleatorización por discreción de T", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Construir el test UMP de nivel α por Karlin–Rubin; como T es discreta, dar la "
            "regla aleatorizada y la fórmula de γα.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "Karlin–Rubin convierte el MLR en test óptimo; la aleatorización resuelve la "
            "discreción para clavar el nivel.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = Text("Rechazar para T grande; clavar el nivel exactamente en α.",
                    font_size=28, color=BACK)
        fitw(idea)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        syms = VGroup(
            MathTex(r"c_\alpha:\ \text{umbral}", font_size=32, color=VAR),
            MathTex(r"\gamma_\alpha:\ \text{prob. de rechazo en la frontera}", font_size=32, color=EIG),
            MathTex(r"F:\ \text{f.d.a. de } \mathrm{Poisson}(n\lambda_0)", font_size=32, color=DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.3)
        fitw(syms)
        self.play_beat(FadeOut(idea), FadeIn(syms))                                # 5

        idea2 = MathTex(r"\text{Idea: imponer } \mathbb{E}_{\lambda_0}[\varphi]=\alpha"
                        r"\ \text{y despejar }\gamma_\alpha", font_size=32, color=VAR).shift(DOWN * 2.3)
        fitw(idea2)
        self.play_beat(FadeIn(idea2))                                              # 6

        self.play_beat(FadeOut(syms), FadeOut(idea2))                              # 7


class P3B_Setup(NarratedScene):
    scene_key = "P3B_Setup"

    def construct(self):
        self.header("Planteamiento")
        dist = MathTex(r"\text{bajo }H_0\text{ exacta: }\ T\sim\mathrm{Poisson}(n\lambda_0)",
                       font_size=40).shift(UP * 1.6)
        fitw(dist)
        self.play_beat(Write(dist))                                                # 1

        disc = wrapt("T es discreta: en general no hay entero cα con P(T>cα)=α exactamente.",
                     width=48, font_size=26, color=BAD, line_spacing=0.8).shift(UP * 0.5)
        fitw(disc)
        self.play_beat(FadeIn(disc))                                               # 2

        rnd = Text("⇒ aleatorizamos en la frontera T = cα.", font_size=28, color=BACK).shift(DOWN * 0.4)
        self.play_beat(FadeIn(rnd))                                                # 3

        ca = MathTex(r"c_\alpha=\inf\{c\in\mathbb{N}_0:\ \mathbb{P}_{\lambda_0}(T>c)\le\alpha\}",
                     font_size=38, color=VAR).shift(DOWN * 1.6)
        fitw(ca)
        self.play_beat(Write(ca))                                                  # 4

        self.play_beat(disc.animate.set_opacity(0.0))                              # 5


class P3B_Desarrollo(NarratedScene):
    scene_key = "P3B_Desarrollo"

    def construct(self):
        self.header("Desarrollo · calibrar γα")
        phi = MathTex(r"\varphi(\mathbf{X})=\begin{cases}1,& T>c_\alpha\\ "
                      r"\gamma_\alpha,& T=c_\alpha\\ 0,& T<c_\alpha\end{cases}",
                      font_size=40).shift(UP * 1.7)
        self.play_beat(Write(phi))                                                 # 1

        lvl = MathTex(r"\mathbb{E}_{\lambda_0}[\varphi]=\alpha", font_size=40, color=BACK).shift(UP * 0.1)
        self.play_beat(Write(lvl))                                                 # 2

        e1 = MathTex(r"=\ \mathbb{P}(T>c_\alpha)+\gamma_\alpha\,\mathbb{P}(T=c_\alpha)",
                     font_size=36).next_to(lvl, DOWN, buff=0.35)
        fitw(e1)
        self.play_beat(Write(e1))                                                  # 3

        e2 = MathTex(r"=\ \bigl(1-F(c_\alpha)\bigr)+\gamma_\alpha\bigl(F(c_\alpha)-F(c_\alpha-1)\bigr)",
                     font_size=34).next_to(e1, DOWN, buff=0.35)
        fitw(e2)
        self.play_beat(Write(e2))                                                  # 4

        solve = Text("igualar a α  y despejar γα", font_size=24, color=DIM).next_to(e2, DOWN, buff=0.3)
        self.play_beat(FadeIn(solve))                                              # 5

        box = MathTex(r"\boxed{\ \gamma_\alpha=\dfrac{\alpha-1+F(c_\alpha)}"
                      r"{F(c_\alpha)-F(c_\alpha-1)}\ }", font_size=38, color=RES).shift(DOWN * 2.9)
        fitw(box)
        self.play_beat(FadeOut(lvl), FadeOut(e1), FadeOut(solve), Write(box))      # 6


class P3B_Conclusion(NarratedScene):
    scene_key = "P3B_Conclusion"

    def construct(self):
        self.header("Conclusión")
        box = MathTex(r"\boxed{\ \varphi\ \text{es UMP de nivel }\alpha\ \ (\text{Karlin–Rubin})\ }",
                      font_size=36, color=RES).shift(UP * 1.5)
        fitw(box)
        self.play_beat(Write(box))                                                 # 1

        g = MathTex(r"\gamma_\alpha\in[0,1]\ \Rightarrow\ \text{nivel exacto }\alpha",
                    font_size=36, color=BACK).shift(UP * 0.3)
        self.play_beat(Write(g))                                                   # 2

        l2 = Text("Rechazar para T grande; aleatorizar solo en la frontera.",
                  font_size=26, color=DIM).shift(DOWN * 0.6)
        fitw(l2)
        self.play_beat(FadeIn(l2))                                                 # 3

        l3 = Text("La aleatorización es necesaria por ser Poisson discreta.",
                  font_size=26, color=VAR).shift(DOWN * 1.4)
        fitw(l3)
        self.play_beat(FadeIn(l3))                                                 # 4

        moral = wrapt("Moraleja: con MLR, Karlin–Rubin da el test óptimo; la aleatorización es "
                      "el ajuste fino del nivel.", width=52, font_size=25, color=RES,
                      line_spacing=0.8).shift(DOWN * 2.7)
        fitw(moral)
        self.play_beat(FadeOut(l2), FadeOut(l3), FadeIn(moral))                    # 5
