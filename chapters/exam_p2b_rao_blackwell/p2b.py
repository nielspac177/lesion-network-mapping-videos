# -*- coding: utf-8 -*-
"""Problema 2 (b): Tn suficiente-completo y Rao-Blackwell → τ̂_RB = Tn/n.
  ./render.sh chapters/exam_p2b_rao_blackwell/p2b.py -q qh \
      P2B_Intuicion P2B_Setup P2B_Desarrollo P2B_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P2B_Intuicion(NarratedScene):
    scene_key = "P2B_Intuicion"

    def construct(self):
        title = Text("Problema 2 · (b)  Rao–Blackwell", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("De un estimador tosco a uno fino", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Probar que Tn = Σ log(Xi/xm) es suficiente y completo, y aplicar Rao–Blackwell "
            "para obtener τ̂_RB = E[τ̂₀ | Tn] = Tn/n.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "Rao–Blackwell reduce la varianza condicionando en un suficiente: el modo "
            "sistemático de mejorar un estimador.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = wrapt("Condicionar en el suficiente promedia el ruido del estimador crudo.",
                     width=46, font_size=28, color=BACK, line_spacing=0.8)
        fitw(idea)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        tn = MathTex(r"T_n=\sum_{i=1}^n\log(X_i/x_m)\ \sim\ \mathrm{Gamma}(n,\alpha)",
                     font_size=40, color=VAR)
        fitw(tn)
        self.play_beat(FadeOut(idea), Write(tn))                                   # 5

        sym = Text("Por simetría: todas las E[Yi | Tn] son iguales y suman Tn.",
                   font_size=26, color=DIM).shift(DOWN * 1.6)
        fitw(sym)
        self.play_beat(FadeIn(sym))                                                # 6

        self.play_beat(FadeOut(tn), FadeOut(sym))                                  # 7


class P2B_Setup(NarratedScene):
    scene_key = "P2B_Setup"

    def construct(self):
        self.header("Planteamiento · familia exponencial")
        logf = MathTex(r"\log f(x\mid\alpha)=\log\alpha-\alpha\,\log(x/x_m)-\log x",
                       font_size=40).shift(UP * 1.5)
        fitw(logf)
        self.play_beat(Write(logf))                                                # 1

        note = MathTex(r"\text{exp. regular},\quad \text{estadístico natural }\ \log(X/x_m)",
                       font_size=34, color=DIM).shift(UP * 0.5)
        fitw(note)
        self.play_beat(FadeIn(note))                                               # 2

        tn = MathTex(r"T_n=\sum_{i=1}^n\log(X_i/x_m)\ \sim\ \mathrm{Gamma}(n,\alpha)",
                     font_size=40, color=VAR).shift(DOWN * 0.6)
        fitw(tn)
        self.play_beat(Write(tn))                                                  # 3

        sc = MathTex(r"\Longrightarrow\quad T_n\ \text{suficiente y completo para }\alpha",
                     font_size=38, color=BACK).shift(DOWN * 1.9)
        fitw(sc)
        self.play_beat(Write(sc))                                                  # 4

        self.play_beat(note.animate.set_opacity(0.0))                              # 5


class P2B_Desarrollo(NarratedScene):
    scene_key = "P2B_Desarrollo"

    def construct(self):
        self.header("Desarrollo · esperanza condicional")
        rb = MathTex(r"\hat\tau_{RB}=\mathbb{E}[\hat\tau_0\mid T_n]=\mathbb{E}[Y_1\mid T_n]",
                     font_size=42).shift(UP * 2.0)
        fitw(rb)
        self.play_beat(Write(rb))                                                  # 1

        s1 = MathTex(r"\sum_{i=1}^n \mathbb{E}[Y_i\mid T_n]=\mathbb{E}[T_n\mid T_n]=T_n",
                     font_size=38, color=BACK).shift(UP * 0.7)
        fitw(s1)
        self.play_beat(Write(s1))                                                  # 2

        s2 = MathTex(r"\text{(intercambiables, todas iguales)}\ \Rightarrow\ "
                     r"\mathbb{E}[Y_1\mid T_n]=\frac{T_n}{n}", font_size=36).shift(DOWN * 0.4)
        fitw(s2)
        self.play_beat(Write(s2))                                                  # 3

        alt = MathTex(r"\text{Alt.: }\ Y_1/T_n\mid T_n\sim\mathrm{Beta}(1,n-1),\ "
                      r"\text{media}=\tfrac1n", font_size=34, color=DIM).shift(DOWN * 1.6)
        fitw(alt)
        self.play_beat(FadeIn(alt))                                                # 4

        same = Text("ambas rutas coinciden", font_size=24, color=DIM).shift(DOWN * 2.4)
        self.play_beat(FadeIn(same))                                               # 5

        box = MathTex(r"\boxed{\ \hat\tau_{RB}=\dfrac{T_n}{n}\ }",
                      font_size=46, color=RES).shift(DOWN * 3.2)
        self.play_beat(FadeOut(s1), FadeOut(same), Write(box))                     # 6


class P2B_Conclusion(NarratedScene):
    scene_key = "P2B_Conclusion"

    def construct(self):
        self.header("Conclusión")
        g = MathTex(r"\mathrm{Var}(\hat\tau_{RB})\ \le\ \mathrm{Var}(\hat\tau_0)",
                    font_size=42, color=BACK).shift(UP * 1.4)
        self.play_beat(Write(g))                                                   # 1

        avg = MathTex(r"\hat\tau_{RB}=\frac{T_n}{n}=\frac1n\sum_{i=1}^n Y_i\ \ (\text{promedio})",
                      font_size=40).shift(UP * 0.1)
        fitw(avg)
        self.play_beat(Write(avg))                                                 # 2

        r = Text("Condicionar en el suficiente = promediar el ruido.",
                 font_size=26, color=DIM).shift(DOWN * 1.1)
        fitw(r)
        self.play_beat(FadeIn(r))                                                  # 3

        nxt = Text("Siguiente: es el UMVUE y además eficiente.",
                   font_size=26, color=VAR).shift(DOWN * 1.9)
        self.play_beat(FadeIn(nxt))                                                # 4

        moral = wrapt("Moraleja: Rao–Blackwell promedia el ruido dentro de cada nivel del "
                      "estadístico suficiente.", width=52, font_size=25, color=RES,
                      line_spacing=0.8).shift(DOWN * 3.0)
        fitw(moral)
        self.play_beat(FadeOut(r), FadeOut(nxt), FadeIn(moral))                    # 5
