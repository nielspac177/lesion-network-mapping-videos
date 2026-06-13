# -*- coding: utf-8 -*-
"""Problema 1 (c): completitud (distribución Gamma + unicidad de Laplace).
  ./render.sh chapters/exam_p1c_completitud/p1c.py -q qh \
      P1C_Intuicion P1C_Setup P1C_Desarrollo P1C_Conclusion
"""
import textwrap
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from narration import SCENES

NarratedScene.narration = SCENES


def fitw(m, w=12.6):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def wrapt(s, width=42, **kw):
    return Text("\n".join(textwrap.wrap(s, width)), **kw)


def context_block(label, text, lcolor, width=44):
    head = Text(label, font_size=26, color=lcolor)
    body = wrapt(text, width=width, font_size=24, color="#D8DBE0", line_spacing=0.8)
    return fitw(VGroup(head, body).arrange(DOWN, buff=0.3), 12.4)


class P1C_Intuicion(NarratedScene):
    scene_key = "P1C_Intuicion"

    def construct(self):
        title = Text("Problema 1 · (c)  Completitud", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("Distribución de T y unicidad de Laplace", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Demostrar que T(X) es completo para λ: hallar su distribución Gamma y usar "
            "la unicidad de la transformada de Laplace.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "Suficiente + completo = la receta de Lehmann–Scheffé para el mejor estimador "
            "insesgado posible: el UMVUE.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        t = Text("Completitud: T no tiene grados de libertad sobrantes.",
                 font_size=28, color=BACK)
        fitw(t)
        self.play_beat(FadeOut(why), FadeIn(t))                                    # 4

        formal = MathTex(r"\mathbb{E}_\lambda[\varphi(T)]=0\ \ \forall\lambda"
                         r"\ \ \Longrightarrow\ \ \varphi\equiv 0", font_size=42)
        formal.shift(UP * 0.3)
        self.play_beat(FadeOut(t), Write(formal))                                  # 5

        steps = VGroup(
            Text("1)  hallar la distribución de T", font_size=26, color=DIM),
            Text("2)  ver que es familia exponencial", font_size=26, color=DIM),
            Text("3)  unicidad de la transformada de Laplace", font_size=26, color=DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 1.6)
        self.play_beat(FadeIn(steps[0]))                                           # 6
        self.play_beat(FadeIn(steps[1]), FadeIn(steps[2]))                         # 7
        self.play_beat(formal.animate.set_opacity(0.0), steps.animate.set_opacity(0.0))  # 8


class P1C_Setup(NarratedScene):
    scene_key = "P1C_Setup"

    def construct(self):
        self.header("Planteamiento · distribución de T")
        chi1 = MathTex(r"\frac{\lambda(X_i-\mu)^2}{\mu^2 X_i}\ \sim\ \chi^2_1",
                       font_size=44).shift(UP * 1.5)
        self.play_beat(Write(chi1))                                                # 1

        cap = Text("independientes para i = 1, …, n", font_size=24, color=DIM)
        cap.next_to(chi1, DOWN, buff=0.45)
        self.play_beat(FadeIn(cap))                                                # 2

        chin = MathTex(r"\frac{\lambda}{\mu^2}\,T=\sum_{i=1}^n\frac{\lambda(X_i-\mu)^2}{\mu^2 X_i}"
                       r"\ \sim\ \chi^2_n", font_size=40)
        fitw(chin)
        self.play_beat(FadeOut(cap), Write(chin))                                  # 3

        gam = MathTex(r"\Longrightarrow\quad T\ \sim\ \mathrm{Gamma}\!\left(\tfrac{n}{2},"
                      r"\ \text{escala }\tfrac{2\mu^2}{\lambda}\right)", font_size=42, color=RES)
        fitw(gam)
        gam.shift(DOWN * 1.7)
        self.play_beat(Write(gam))                                                 # 4

        self.play_beat(chi1.animate.set_opacity(0.0), chin.animate.set_opacity(0.0))  # 5


class P1C_Desarrollo(NarratedScene):
    scene_key = "P1C_Desarrollo"

    def construct(self):
        self.header("Desarrollo · unicidad de Laplace")
        dens = MathTex(r"g_\lambda(t)\ \propto\ t^{\,n/2-1}\,e^{-\lambda t/(2\mu^2)}",
                       font_size=44).shift(UP * 1.6)
        self.play_beat(Write(dens))                                                # 1

        note = MathTex(r"\text{familia exponencial en }\ \eta=-\tfrac{\lambda}{2\mu^2}"
                       r"\quad(\text{regular})", font_size=34, color=DIM)
        note.next_to(dens, DOWN, buff=0.45)
        self.play_beat(FadeIn(note))                                               # 2

        assume = MathTex(r"\mathbb{E}_\lambda[\varphi(T)]=0\quad\forall\lambda>0",
                         font_size=40, color=BACK).shift(UP * 0.1)
        self.play_beat(FadeOut(note), FadeIn(assume))                              # 3

        chg = MathTex(r"s=\tfrac{\lambda}{2\mu^2}>0", font_size=36, color=EIG)
        chg.next_to(assume, DOWN, buff=0.45)
        self.play_beat(FadeIn(chg))                                                # 4

        integ = MathTex(r"\int_0^\infty \varphi(t)\,t^{\,n/2-1}\,e^{-st}\,dt=0"
                        r"\quad\forall s>0", font_size=40)
        fitw(integ)
        integ.shift(DOWN * 1.5)
        self.play_beat(FadeOut(assume), FadeOut(chg), Write(integ))               # 5

        lap = Text("↑  transformada de Laplace de  φ(t)·t^(n/2−1)", font_size=26, color=RES)
        fitw(lap)
        lap.next_to(integ, DOWN, buff=0.5)
        self.play_beat(FadeIn(lap))                                                # 6


class P1C_Conclusion(NarratedScene):
    scene_key = "P1C_Conclusion"

    def construct(self):
        self.header("Conclusión")
        l1 = Text("Laplace = 0 en todo un intervalo de s.", font_size=28, color=DIM).shift(UP * 1.6)
        self.play_beat(FadeIn(l1))                                                 # 1

        l2 = Text("Por unicidad de Laplace ⇒ función = 0 casi en todo punto.",
                  font_size=28, color=BACK).shift(UP * 0.6)
        fitw(l2)
        self.play_beat(FadeIn(l2))                                                 # 2

        l3 = MathTex(r"\varphi(t)\,t^{\,n/2-1}=0,\quad t^{\,n/2-1}>0"
                     r"\ \Longrightarrow\ \varphi\equiv 0", font_size=38)
        fitw(l3)
        l3.shift(DOWN * 0.4)
        self.play_beat(Write(l3))                                                  # 3

        res = MathTex(r"\boxed{\,T(\mathbf{X})\ \text{es completo para }\lambda\,}",
                      font_size=40, color=RES).shift(DOWN * 1.8)
        self.play_beat(Write(res))                                                 # 4

        moral = wrapt("Moraleja: distribución → exponencial → unicidad de Laplace. "
                      "Ese esqueleto se repite siempre.", width=52,
                      font_size=25, color=RES, line_spacing=0.8)
        fitw(moral)
        moral.shift(DOWN * 3.05)
        self.play_beat(FadeOut(l1), FadeOut(l2), FadeIn(moral))                    # 5
