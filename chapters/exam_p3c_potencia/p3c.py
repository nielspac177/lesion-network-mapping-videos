# -*- coding: utf-8 -*-
"""Problema 3 (c): función de potencia β(λ), monotonía por MLR, límite 1.
  ./render.sh chapters/exam_p3c_potencia/p3c.py -q qh \
      P3C_Intuicion P3C_Setup P3C_Desarrollo P3C_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P3C_Intuicion(NarratedScene):
    scene_key = "P3C_Intuicion"

    def construct(self):
        title = Text("Problema 3 · (c)  Función de potencia", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("Monotonía por MLR y límite", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Derivar β(λ)=E_λ[φ] en términos de la f.d.a. de Poisson(nλ); probar que es "
            "estrictamente creciente (MLR) y que β(λ)→1.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "La potencia mide la detección del test: detecta mejor cuanto más lejos está la "
            "verdad de H0.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = wrapt("Mayor λ ⇒ más probable rechazar; para λ enorme, rechazo casi seguro.",
                     width=46, font_size=28, color=BACK, line_spacing=0.8)
        fitw(idea)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        syms = VGroup(
            MathTex(r"\beta(\lambda):\ \text{potencia}", font_size=32, color=VAR),
            MathTex(r"F_\lambda:\ \text{f.d.a. de }\mathrm{Poisson}(n\lambda)", font_size=32, color=DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.4)
        self.play_beat(FadeOut(idea), FadeIn(syms))                                # 5

        idea2 = Text("Idea: monotonía por MLR + ley de grandes números.",
                     font_size=26, color=VAR).shift(DOWN * 1.9)
        fitw(idea2)
        self.play_beat(FadeIn(idea2))                                              # 6

        self.play_beat(FadeOut(syms), FadeOut(idea2))                              # 7


class P3C_Setup(NarratedScene):
    scene_key = "P3C_Setup"

    def construct(self):
        self.header("Planteamiento")
        dist = MathTex(r"T\sim\mathrm{Poisson}(n\lambda),\quad \text{f.d.a. } F_\lambda",
                       font_size=40).shift(UP * 1.7)
        fitw(dist)
        self.play_beat(Write(dist))                                                # 1

        beta = MathTex(r"\beta(\lambda)=\mathbb{E}_\lambda[\varphi(\mathbf{X})]",
                       font_size=42, color=VAR).shift(UP * 0.6)
        self.play_beat(Write(beta))                                                # 2

        full = MathTex(r"=\bigl(1-F_\lambda(c_\alpha)\bigr)+\gamma_\alpha"
                       r"\bigl(F_\lambda(c_\alpha)-F_\lambda(c_\alpha-1)\bigr)",
                       font_size=34).shift(DOWN * 0.5)
        fitw(full)
        self.play_beat(Write(full))                                                # 3

        todo = VGroup(
            Text("por probar:", font_size=24, color=DIM),
            Text("(1) estrictamente creciente   (2) límite = 1", font_size=26, color=BACK),
        ).arrange(DOWN, buff=0.2).shift(DOWN * 1.9)
        fitw(todo)
        self.play_beat(FadeIn(todo))                                               # 4

        self.play_beat(todo.animate.set_opacity(0.0))                              # 5


class P3C_Desarrollo(NarratedScene):
    scene_key = "P3C_Desarrollo"

    def construct(self):
        self.header("Desarrollo · monotonía y límite")
        f1 = Text("φ es no decreciente y no constante en T.", font_size=28, color=DIM).shift(UP * 2.0)
        fitw(f1)
        self.play_beat(FadeIn(f1))                                                 # 1

        f2 = Text("la familia tiene MLR (inciso a).", font_size=28, color=DIM).shift(UP * 1.1)
        self.play_beat(FadeIn(f2))                                                 # 2

        lemma = MathTex(r"\text{lema de monotonía}\ \Rightarrow\ "
                        r"\beta(\lambda)\ \text{estrictamente creciente}",
                        font_size=36, color=BACK).shift(UP * 0.1)
        fitw(lemma)
        self.play_beat(Write(lemma))                                               # 3

        interp = Text("mayor λ ⇒ mayor probabilidad de rechazar", font_size=26, color=VAR).shift(DOWN * 0.9)
        fitw(interp)
        self.play_beat(FadeIn(interp))                                             # 4

        lln = MathTex(r"\text{LGN:}\quad \frac{T}{n}\ \xrightarrow{P}\ \lambda",
                      font_size=38, color=EIG).shift(DOWN * 1.9)
        self.play_beat(FadeOut(f1), FadeOut(f2), FadeIn(lln))                      # 5

        lim = MathTex(r"\Rightarrow\ \mathbb{P}_\lambda(T>c_\alpha)\to 1,\quad \beta(\lambda)\to 1",
                      font_size=36, color=RES).shift(DOWN * 3.0)
        fitw(lim)
        self.play_beat(Write(lim))                                                 # 6


class P3C_Conclusion(NarratedScene):
    scene_key = "P3C_Conclusion"

    def construct(self):
        self.header("Conclusión")
        b1 = MathTex(r"\beta(\lambda)\ \text{estrictamente creciente en }\lambda",
                     font_size=38, color=BACK).shift(UP * 1.6)
        fitw(b1)
        self.play_beat(Write(b1))                                                  # 1

        b2 = MathTex(r"\boxed{\ \lim_{\lambda\to\infty}\beta(\lambda)=1\ }",
                     font_size=42, color=RES).shift(UP * 0.4)
        self.play_beat(Write(b2))                                                  # 2

        r = Text("Monotonía ← MLR     Límite ← ley de grandes números",
                 font_size=25, color=DIM).shift(DOWN * 0.7)
        fitw(r)
        self.play_beat(FadeIn(r))                                                  # 3

        good = Text("Exactamente lo esperado de un buen test.",
                    font_size=26, color=VAR).shift(DOWN * 1.5)
        self.play_beat(FadeIn(good))                                               # 4

        moral = wrapt("Moraleja: el MLR construye el test óptimo y además garantiza que su "
                      "potencia se comporte bien.", width=52, font_size=25, color=RES,
                      line_spacing=0.8).shift(DOWN * 2.8)
        fitw(moral)
        self.play_beat(FadeOut(r), FadeOut(good), FadeIn(moral))                   # 5
