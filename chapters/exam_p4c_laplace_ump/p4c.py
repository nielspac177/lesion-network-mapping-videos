# -*- coding: utf-8 -*-
"""Problema 4 (c): test UMP en Laplace (MLR, χ²(2n), sin aleatorización).
  ./render.sh chapters/exam_p4c_laplace_ump/p4c.py -q qh \
      P4C_Intuicion P4C_Setup P4C_Desarrollo P4C_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P4C_Intuicion(NarratedScene):
    scene_key = "P4C_Intuicion"

    def construct(self):
        title = Text("Problema 4 · (c)  UMP en Laplace", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("MLR, χ²(2n) y sin aleatorización", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Probar MLR en T=Σ|Xi−μ|; por Karlin–Rubin rechazar para T grande; mostrar "
            "2T/b ~ χ²(2n) y dar la región crítica; contrastar con Poisson.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "Mismo esquema MLR → Karlin–Rubin, pero la ley nula es continua: no hace falta "
            "aleatorizar.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = wrapt("b es la escala; T grande = mucha dispersión = evidencia de b grande.",
                     width=46, font_size=28, color=BACK, line_spacing=0.8)
        fitw(idea)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        syms = VGroup(
            MathTex(r"T=\sum_i|X_i-\mu|:\ \text{desvíos absolutos}", font_size=30, color=VAR),
            MathTex(r"b:\ \text{escala}\qquad \chi^2_{2n}", font_size=30, color=EIG),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.3)
        fitw(syms)
        self.play_beat(FadeOut(idea), FadeIn(syms))                                # 5

        idea2 = Text("Idea: cociente → MLR → distribución de T → región crítica.",
                     font_size=26, color=VAR).shift(DOWN * 2.1)
        fitw(idea2)
        self.play_beat(FadeIn(idea2))                                              # 6

        self.play_beat(FadeOut(syms), FadeOut(idea2))                              # 7


class P4C_Setup(NarratedScene):
    scene_key = "P4C_Setup"

    def construct(self):
        self.header("Planteamiento")
        hyp = MathTex(r"\text{Laplace}(\mu,b),\ \mu\text{ conocido};\quad "
                      r"H_0:b\le b_0\ \text{vs}\ H_1:b>b_0", font_size=36).shift(UP * 1.6)
        fitw(hyp)
        self.play_beat(Write(hyp))                                                 # 1

        tdef = MathTex(r"T=\sum_{i=1}^n |X_i-\mu|", font_size=42, color=VAR).shift(UP * 0.4)
        self.play_beat(Write(tdef))                                                # 2

        dens = MathTex(r"f(\mathbf{x}\mid b)=(2b)^{-n}\,e^{-T/b}",
                       font_size=42).shift(DOWN * 0.7)
        self.play_beat(Write(dens))                                                # 3

        two = MathTex(r"b_1>b_2>0", font_size=40, color=BACK).shift(DOWN * 1.9)
        self.play_beat(Write(two))                                                 # 4

        self.play_beat(hyp.animate.set_opacity(0.0))                               # 5


class P4C_Desarrollo(NarratedScene):
    scene_key = "P4C_Desarrollo"

    def construct(self):
        self.header("Desarrollo · MLR y región crítica")
        ratio = MathTex(r"\frac{f(\mathbf{x}\mid b_1)}{f(\mathbf{x}\mid b_2)}"
                        r"=\left(\frac{b_2}{b_1}\right)^{n}\exp\!\Big\{T\Big(\tfrac{1}{b_2}-\tfrac{1}{b_1}\Big)\Big\}",
                        font_size=36).shift(UP * 2.0)
        fitw(ratio)
        self.play_beat(Write(ratio))                                               # 1

        mlr = MathTex(r"b_1>b_2\ \Rightarrow\ \tfrac{1}{b_2}-\tfrac{1}{b_1}>0"
                      r"\ \Rightarrow\ \text{creciente en }T\ (\text{MLR})",
                      font_size=32, color=BACK).shift(UP * 0.9)
        fitw(mlr)
        self.play_beat(Write(mlr))                                                 # 2

        kr = Text("Karlin–Rubin: rechazar para T grande.", font_size=28, color=DIM).shift(UP * 0.0)
        self.play_beat(FadeIn(kr))                                                 # 3

        chi = MathTex(r"|X_i-\mu|\sim\mathrm{Exp}(\text{media }b)\ \Rightarrow\ "
                      r"\frac{2T}{b}\sim\chi^2_{2n}", font_size=36, color=EIG).shift(DOWN * 1.1)
        fitw(chi)
        self.play_beat(FadeOut(kr), Write(chi))                                    # 4

        box = MathTex(r"\boxed{\ T>\dfrac{b_0}{2}\,\chi^2_{2n;\alpha}\ }",
                      font_size=40, color=RES).shift(DOWN * 2.4)
        self.play_beat(FadeOut(mlr), Write(box))                                   # 5

        cont = Text("ley nula de T continua ⇒ sin aleatorización.",
                    font_size=26, color=VAR).shift(DOWN * 3.3)
        fitw(cont)
        self.play_beat(FadeIn(cont))                                               # 6


class P4C_Conclusion(NarratedScene):
    scene_key = "P4C_Conclusion"

    def construct(self):
        self.header("Conclusión")
        l1 = Text("Laplace tiene MLR; el test UMP rechaza para T grande.",
                  font_size=27, color=BACK).shift(UP * 1.6)
        fitw(l1)
        self.play_beat(FadeIn(l1))                                                 # 1

        box = MathTex(r"T>\frac{b_0}{2}\,\chi^2_{2n;\alpha}", font_size=42, color=RES).shift(UP * 0.5)
        self.play_beat(Write(box))                                                 # 2

        contrast = VGroup(
            Text("Poisson (discreto):  requiere aleatorización", font_size=25, color=BAD),
            Text("Laplace (continuo):  NO la requiere", font_size=25, color=BACK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.7)
        fitw(contrast)
        self.play_beat(FadeIn(contrast))                                           # 3

        rec = Text("Cociente → MLR → χ²(2n) → región crítica.",
                   font_size=25, color=DIM).shift(DOWN * 1.9)
        fitw(rec)
        self.play_beat(FadeIn(rec))                                                # 4

        moral = wrapt("Moraleja: que haya o no aleatorización es puro reflejo de discreto vs "
                      "continuo.", width=52, font_size=25, color=RES, line_spacing=0.8).shift(DOWN * 2.9)
        fitw(moral)
        self.play_beat(FadeOut(contrast), FadeOut(rec), FadeIn(moral))             # 5
