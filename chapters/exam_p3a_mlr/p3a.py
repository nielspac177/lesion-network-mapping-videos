# -*- coding: utf-8 -*-
"""Problema 3 (a): cociente de verosimilitudes monótono (MLR) en Poisson.
  ./render.sh chapters/exam_p3a_mlr/p3a.py -q qh \
      P3A_Intuicion P3A_Setup P3A_Desarrollo P3A_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P3A_Intuicion(NarratedScene):
    scene_key = "P3A_Intuicion"

    def construct(self):
        title = Text("Problema 3 · (a)  MLR en Poisson", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("Cociente de verosimilitudes monótono", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Probar que el cociente f(x|λ1)/f(x|λ2) es no decreciente en T = ΣXi, "
            "argumentando directamente sobre los enteros.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "El MLR es la llave de los tests UMP: convierte el mejor test en « rechazar "
            "cuando T es grande » (Karlin–Rubin).", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = wrapt("MLR: T grande = evidencia monótonamente más fuerte de λ grande.",
                     width=46, font_size=28, color=BACK, line_spacing=0.8)
        fitw(idea)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        hyp = MathTex(r"H_0:\lambda\le\lambda_0\qquad\text{vs}\qquad H_1:\lambda>\lambda_0",
                      font_size=40, color=VAR)
        fitw(hyp)
        self.play_beat(FadeOut(idea), Write(hyp))                                  # 5

        idea2 = Text("Idea: escribir el cociente para λ1 > λ2 y ver que crece en T.",
                     font_size=26, color=DIM).shift(DOWN * 1.5)
        fitw(idea2)
        self.play_beat(FadeIn(idea2))                                              # 6

        self.play_beat(FadeOut(hyp), FadeOut(idea2))                               # 7


class P3A_Setup(NarratedScene):
    scene_key = "P3A_Setup"

    def construct(self):
        self.header("Planteamiento")
        hyp = MathTex(r"H_0:\lambda\le\lambda_0\quad\text{vs}\quad H_1:\lambda>\lambda_0",
                      font_size=40, color=DIM).shift(UP * 1.6)
        fitw(hyp)
        self.play_beat(Write(hyp))                                                 # 1

        dens = MathTex(r"f(\mathbf{x}\mid\lambda)=e^{-n\lambda}\,"
                       r"\frac{\lambda^{T}}{\prod_i x_i!}", font_size=44).shift(UP * 0.3)
        self.play_beat(Write(dens))                                                # 2

        tdef = MathTex(r"T=\sum_{i=1}^n X_i", font_size=42, color=VAR).shift(DOWN * 0.9)
        self.play_beat(Write(tdef))                                                # 3

        two = MathTex(r"\lambda_1>\lambda_2>0", font_size=40, color=BACK).shift(DOWN * 2.1)
        self.play_beat(Write(two))                                                 # 4

        self.play_beat(hyp.animate.set_opacity(0.0))                               # 5


class P3A_Desarrollo(NarratedScene):
    scene_key = "P3A_Desarrollo"

    def construct(self):
        self.header("Desarrollo · el cociente")
        r = MathTex(r"\frac{f(\mathbf{x}\mid\lambda_1)}{f(\mathbf{x}\mid\lambda_2)}",
                    font_size=48).shift(UP * 2.0)
        self.play_beat(Write(r))                                                   # 1

        cap = Text("los factoriales ∏ xi! se cancelan", font_size=24, color=DIM).shift(UP * 0.9)
        self.play_beat(FadeIn(cap))                                                # 2

        full = MathTex(r"=\ e^{-n(\lambda_1-\lambda_2)}\left(\frac{\lambda_1}{\lambda_2}\right)^{T}",
                       font_size=44).shift(UP * 0.0)
        self.play_beat(FadeOut(cap), Write(full))                                  # 3

        gt = MathTex(r"\lambda_1>\lambda_2\ \Rightarrow\ \frac{\lambda_1}{\lambda_2}>1",
                     font_size=40, color=BACK).shift(DOWN * 1.2)
        self.play_beat(Write(gt))                                                  # 4

        mono = wrapt("base > 1 ⇒ (λ1/λ2)^t crece en t ∈ ℕ₀ (argumento discreto)",
                     width=50, font_size=26, color=EIG, line_spacing=0.8).shift(DOWN * 2.3)
        fitw(mono)
        self.play_beat(FadeIn(mono))                                              # 5

        box = MathTex(r"\boxed{\ \text{cociente no decreciente en } T\ \Rightarrow\ \text{MLR}\ }",
                      font_size=36, color=RES).shift(DOWN * 3.3)
        fitw(box)
        self.play_beat(FadeOut(gt), Write(box))                                    # 6


class P3A_Conclusion(NarratedScene):
    scene_key = "P3A_Conclusion"

    def construct(self):
        self.header("Conclusión")
        box = MathTex(r"\boxed{\ \text{Poisson tiene MLR no decreciente en } T=\textstyle\sum_i X_i\ }",
                      font_size=36, color=RES).shift(UP * 1.5)
        fitw(box)
        self.play_beat(Write(box))                                                 # 1

        l1 = Text("Sin suponer continuidad: argumento directo sobre ℕ₀.",
                  font_size=26, color=DIM).shift(UP * 0.3)
        fitw(l1)
        self.play_beat(FadeIn(l1))                                                 # 2

        l2 = Text("Clave: base > 1 ⇒ potencia creciente en el exponente.",
                  font_size=26, color=BACK).shift(DOWN * 0.5)
        fitw(l2)
        self.play_beat(FadeIn(l2))                                                 # 3

        l3 = Text("Esto habilita el Teorema de Karlin–Rubin (siguiente video).",
                  font_size=26, color=VAR).shift(DOWN * 1.3)
        fitw(l3)
        self.play_beat(FadeIn(l3))                                                 # 4

        moral = wrapt("Moraleja: el MLR es una propiedad estructural que vuelve casi automática "
                      "la construcción del test óptimo.", width=52, font_size=25, color=RES,
                      line_spacing=0.8).shift(DOWN * 2.7)
        fitw(moral)
        self.play_beat(FadeOut(l1), FadeOut(l2), FadeIn(moral))                    # 5
