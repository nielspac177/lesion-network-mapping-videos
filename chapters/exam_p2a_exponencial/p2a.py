# -*- coding: utf-8 -*-
"""Problema 2 (a): Y = log(X/xm) ~ Exp(α); estimador insesgado de τ=1/α.
  ./render.sh chapters/exam_p2a_exponencial/p2a.py -q qh \
      P2A_Intuicion P2A_Setup P2A_Desarrollo P2A_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P2A_Intuicion(NarratedScene):
    scene_key = "P2A_Intuicion"

    def construct(self):
        title = Text("Problema 2 · (a)  Pareto → Exponencial", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("Un primer estimador insesgado de τ = 1/α", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Mostrar que Y = log(X/xm) ~ Exp(α) y proponer un estimador insesgado de "
            "τ = 1/α con un solo dato, hallando su varianza.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "Es el punto de partida: Rao–Blackwell lo hará óptimo después. Primero "
            "conseguimos algo insesgado, aunque sea simple.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = Text("La Pareto es una exponencial disfrazada.", font_size=30, color=BACK)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        syms = VGroup(
            MathTex(r"x:\ \text{dato}", font_size=34, color=VAR),
            MathTex(r"x_m:\ \text{escala (conocida)}", font_size=34, color=DIM),
            MathTex(r"\alpha:\ \text{forma (desconocida)}", font_size=34, color=EIG),
            MathTex(r"\tau=1/\alpha:\ \text{objetivo}", font_size=34, color=RES),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.2)
        self.play_beat(FadeOut(idea), LaggedStart(*[FadeIn(m) for m in syms], lag_ratio=0.3))  # 5

        plan = Text("Plan: transformar → reconocer exponencial → leer su media.",
                    font_size=26, color=VAR).shift(DOWN * 2.3)
        fitw(plan)
        self.play_beat(FadeIn(plan))                                               # 6

        self.play_beat(FadeOut(syms), FadeOut(plan))                               # 7


class P2A_Setup(NarratedScene):
    scene_key = "P2A_Setup"

    def construct(self):
        self.header("Planteamiento")
        dens = MathTex(r"f(x\mid\alpha)=\frac{\alpha\,x_m^{\alpha}}{x^{\alpha+1}}\,"
                       r"\mathbf{1}_{\{x\ge x_m\}}", font_size=44).shift(UP * 1.4)
        self.play_beat(Write(dens))                                                # 1

        tail = MathTex(r"\mathbb{P}(X>t)=\left(\frac{x_m}{t}\right)^{\alpha},\quad t\ge x_m",
                       font_size=40, color=BACK).shift(UP * 0.2)
        self.play_beat(Write(tail))                                                # 2

        ydef = MathTex(r"Y=\log(X/x_m)\ \ge 0", font_size=42, color=VAR).shift(DOWN * 1.0)
        self.play_beat(Write(ydef))                                                # 3

        tau = MathTex(r"\tau=\frac{1}{\alpha}", font_size=40, color=RES).shift(DOWN * 2.3)
        self.play_beat(FadeIn(tau))                                                # 4

        self.play_beat(tail.animate.set_opacity(0.0), tau.animate.set_opacity(0.0))  # 5


class P2A_Desarrollo(NarratedScene):
    scene_key = "P2A_Desarrollo"

    def construct(self):
        self.header("Desarrollo · distribución de Y")
        l1 = MathTex(r"\mathbb{P}(Y\le y)", font_size=44).shift(UP * 2.0)
        self.play_beat(Write(l1))                                                  # 1

        l2 = MathTex(r"=\ \mathbb{P}(X\le x_m e^{y})", font_size=44).next_to(l1, DOWN, buff=0.4)
        self.play_beat(Write(l2))                                                  # 2

        l3 = MathTex(r"=\ 1-e^{-\alpha y}", font_size=44, color=BACK).next_to(l2, DOWN, buff=0.4)
        self.play_beat(Write(l3))                                                  # 3

        concl = MathTex(r"\Longrightarrow\quad Y\sim \mathrm{Exp}(\alpha)",
                        font_size=46, color=RES).shift(DOWN * 1.1)
        self.play_beat(Write(concl))                                               # 4

        mean = MathTex(r"\mathbb{E}[Y]=\frac1\alpha=\tau,\qquad \mathrm{Var}(Y)=\frac{1}{\alpha^2}",
                       font_size=40).shift(DOWN * 2.4)
        fitw(mean)
        self.play_beat(FadeOut(l1), FadeOut(l2), FadeIn(mean))                     # 5

        est = MathTex(r"\hat\tau_0=Y_1=\log(X_1/x_m)", font_size=40, color=VAR).shift(DOWN * 3.3)
        self.play_beat(FadeIn(est))                                                # 6


class P2A_Conclusion(NarratedScene):
    scene_key = "P2A_Conclusion"

    def construct(self):
        self.header("Conclusión")
        unb = MathTex(r"\mathbb{E}_\alpha[\hat\tau_0]=\frac1\alpha=\tau\quad(\text{insesgado})",
                      font_size=42).shift(UP * 1.3)
        fitw(unb)
        self.play_beat(Write(unb))                                                 # 1

        var = MathTex(r"\boxed{\ \mathrm{Var}_\alpha(\hat\tau_0)=\alpha^{-2}\ }",
                      font_size=44, color=RES).shift(UP * 0.1)
        self.play_beat(Write(var))                                                 # 2

        r1 = Text("Una transformación log convirtió la Pareto en exponencial.",
                  font_size=26, color=DIM).shift(DOWN * 1.1)
        fitw(r1)
        self.play_beat(FadeIn(r1))                                                 # 3

        r2 = Text("Y la media de esa exponencial es justo τ.",
                  font_size=26, color=BACK).shift(DOWN * 1.9)
        self.play_beat(FadeIn(r2))                                                 # 4

        moral = wrapt("Moraleja: un insesgado simple es un gran punto de partida. "
                      "Rao–Blackwell lo hará óptimo.", width=52,
                      font_size=25, color=RES, line_spacing=0.8).shift(DOWN * 3.0)
        fitw(moral)
        self.play_beat(FadeOut(r1), FadeOut(r2), FadeIn(moral))                    # 5
