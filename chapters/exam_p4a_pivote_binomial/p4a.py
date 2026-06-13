# -*- coding: utf-8 -*-
"""Problema 4 (a): pivote binomial condicional e IC exacto (Clopper-Pearson).
  ./render.sh chapters/exam_p4a_pivote_binomial/p4a.py -q qh \
      P4A_Intuicion P4A_Setup P4A_Desarrollo P4A_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P4A_Intuicion(NarratedScene):
    scene_key = "P4A_Intuicion"

    def construct(self):
        title = Text("Problema 4 · (a)  Pivote binomial", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("IC exacto para τ = λ1/λ2", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Mostrar que SX | SX+SY=n ~ Binomial(n, p) con p función de τ, y usarlo como "
            "pivote para un IC exacto de τ vía cuantiles Beta.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "Dos tasas, pero solo importa su cociente. Condicionar en el total elimina el "
            "nivel global y deja una binomial limpia.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = wrapt("Dado el total, el reparto entre muestras es binomial, con p que depende "
                     "solo de τ.", width=46, font_size=28, color=BACK, line_spacing=0.8)
        fitw(idea)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        syms = VGroup(
            MathTex(r"S_X,\,S_Y:\ \text{sumas de cada muestra}", font_size=30, color=VAR),
            MathTex(r"n=S_X+S_Y:\ \text{total}", font_size=30, color=DIM),
            MathTex(r"\tau=\lambda_1/\lambda_2,\quad p:\ \text{prob. binomial}", font_size=30, color=EIG),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.3)
        fitw(syms)
        self.play_beat(FadeOut(idea), FadeIn(syms))                                # 5

        idea2 = Text("Idea: condicionar → binomial → invertir (cuantiles Beta).",
                     font_size=26, color=VAR).shift(DOWN * 2.3)
        fitw(idea2)
        self.play_beat(FadeIn(idea2))                                              # 6

        self.play_beat(FadeOut(syms), FadeOut(idea2))                              # 7


class P4A_Setup(NarratedScene):
    scene_key = "P4A_Setup"

    def construct(self):
        self.header("Planteamiento")
        s1 = MathTex(r"S_X\sim\mathrm{Poisson}(m\lambda_1),\quad S_Y\sim\mathrm{Poisson}(k\lambda_2)",
                     font_size=40).shift(UP * 1.6)
        fitw(s1)
        self.play_beat(Write(s1))                                                  # 1

        s2 = MathTex(r"S_X+S_Y\sim\mathrm{Poisson}(m\lambda_1+k\lambda_2)",
                     font_size=40, color=BACK).shift(UP * 0.4)
        fitw(s2)
        self.play_beat(Write(s2))                                                  # 2

        tau = MathTex(r"\tau=\frac{\lambda_1}{\lambda_2}", font_size=42, color=RES).shift(DOWN * 0.9)
        self.play_beat(Write(tau))                                                 # 3

        cond = Text("Estrategia: condicionar SX en el total n.", font_size=28, color=VAR).shift(DOWN * 2.1)
        fitw(cond)
        self.play_beat(FadeIn(cond))                                               # 4

        self.play_beat(s1.animate.set_opacity(0.0), cond.animate.set_opacity(0.0))  # 5


class P4A_Desarrollo(NarratedScene):
    scene_key = "P4A_Desarrollo"

    def construct(self):
        self.header("Desarrollo · binomial condicional")
        f = MathTex(r"\mathbb{P}(S_X=s\mid S_X+S_Y=n)="
                    r"\frac{\mathbb{P}(S_X=s)\,\mathbb{P}(S_Y=n-s)}{\mathbb{P}(S_X+S_Y=n)}",
                    font_size=34).shift(UP * 1.9)
        fitw(f)
        self.play_beat(Write(f))                                                   # 1

        cap = Text("sustituir masas Poisson y simplificar →", font_size=24, color=DIM).shift(UP * 0.8)
        self.play_beat(FadeIn(cap))                                                # 2

        bino = MathTex(r"=\binom{n}{s}p^{s}(1-p)^{n-s},\quad p=\frac{m\tau}{m\tau+k}",
                       font_size=38, color=BACK).shift(UP * 0.0)
        fitw(bino)
        self.play_beat(FadeOut(cap), Write(bino))                                  # 3

        inv = MathTex(r"p\ \text{creciente en }\tau,\qquad \tau=\frac{k\,p}{m(1-p)}",
                      font_size=36).shift(DOWN * 1.1)
        fitw(inv)
        self.play_beat(Write(inv))                                                 # 4

        cp = MathTex(r"p_L=\mathrm{Beta}_{\alpha/2}(s_x,\,n-s_x+1),\ \ "
                     r"p_U=\mathrm{Beta}_{1-\alpha/2}(s_x+1,\,n-s_x)",
                     font_size=28, color=EIG).shift(DOWN * 2.2)
        fitw(cp)
        self.play_beat(FadeIn(cp))                                                 # 5

        box = MathTex(r"\boxed{\ \text{IC}(\tau)=\Big(\tfrac{k\,p_L}{m(1-p_L)},\ "
                      r"\tfrac{k\,p_U}{m(1-p_U)}\Big)\ }", font_size=34, color=RES).shift(DOWN * 3.3)
        fitw(box)
        self.play_beat(FadeOut(inv), Write(box))                                   # 6


class P4A_Conclusion(NarratedScene):
    scene_key = "P4A_Conclusion"

    def construct(self):
        self.header("Conclusión")
        l1 = Text("Condicionar en el total → una simple binomial.", font_size=27, color=BACK).shift(UP * 1.6)
        fitw(l1)
        self.play_beat(FadeIn(l1))                                                 # 1

        l2 = Text("cuyos parámetros dependen solo de τ.", font_size=27, color=DIM).shift(UP * 0.7)
        self.play_beat(FadeIn(l2))                                                 # 2

        box = MathTex(r"\text{IC}(\tau)=\Big(\tfrac{k\,p_L}{m(1-p_L)},\ \tfrac{k\,p_U}{m(1-p_U)}\Big)",
                      font_size=36, color=RES).shift(DOWN * 0.3)
        fitw(box)
        self.play_beat(Write(box))                                                 # 3

        l3 = Text("Pivote condicional → Clopper–Pearson → transformar a τ.",
                  font_size=25, color=VAR).shift(DOWN * 1.5)
        fitw(l3)
        self.play_beat(FadeIn(l3))                                                 # 4

        moral = wrapt("Moraleja: condicionar en un total inteligente elimina parámetros "
                      "molestos y deja inferencia exacta.", width=52, font_size=25, color=RES,
                      line_spacing=0.8).shift(DOWN * 2.8)
        fitw(moral)
        self.play_beat(FadeOut(l1), FadeOut(l2), FadeOut(l3), FadeIn(moral))       # 5
