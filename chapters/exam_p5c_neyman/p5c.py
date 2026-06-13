# -*- coding: utf-8 -*-
"""Problema 5 (c): ortogonalidad de Neyman y double machine learning.
  ./render.sh chapters/exam_p5c_neyman/p5c.py -q qh \
      P5C_Intuicion P5C_Setup P5C_Desarrollo P5C_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P5C_Intuicion(NarratedScene):
    scene_key = "P5C_Intuicion"

    def construct(self):
        title = Text("Problema 5 · (c)  Ortogonalidad de Neyman", font_size=30, color=RES).to_edge(UP, buff=0.5)
        sub = Text("y double machine learning", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Calcular las derivadas de Gâteaux de M respecto del nuisance en η0 y ver que se "
            "anulan; explicar la consecuencia sobre el sesgo y la normalidad de β.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "Es lo que hace funcionar el double machine learning: ML imperfecto para el "
            "nuisance, inferencia válida para β.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = wrapt("Insensible a 1er orden a errores del nuisance ⇒ sesgo de 2º orden.",
                     width=46, font_size=28, color=BACK, line_spacing=0.8)
        fitw(idea)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        syms = VGroup(
            MathTex(r"\psi:\ \text{funcional de momento}", font_size=30, color=VAR),
            MathTex(r"\eta=(m,g,\sigma^2):\ \text{nuisance}", font_size=30, color=BAD),
            MathTex(r"M(\beta,\eta)=\mathbb{E}[\psi]", font_size=30, color=DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).shift(DOWN * 0.3)
        fitw(syms)
        self.play_beat(FadeOut(idea), FadeIn(syms))                                # 5

        idea2 = Text("Idea: perturbar cada nuisance y ver que la derivada = 0.",
                     font_size=26, color=VAR).shift(DOWN * 2.1)
        fitw(idea2)
        self.play_beat(FadeIn(idea2))                                              # 6

        cons = MathTex(r"\text{consecuencia: sesgo}\ =O(\|\hat\eta-\eta_0\|^2)",
                       font_size=32, color=RES).shift(DOWN * 2.9)
        fitw(cons)
        self.play_beat(FadeOut(syms), FadeOut(idea2), FadeIn(cons))                # 7

        self.play_beat(FadeOut(cons))                                              # 8


class P5C_Setup(NarratedScene):
    scene_key = "P5C_Setup"

    def construct(self):
        self.header("Planteamiento · funcional de momento")
        psi = MathTex(r"\psi(O;\beta,\eta)=\big(X-m(Z)\big)\,"
                      r"\frac{Y-X^\top\beta-g(Z)}{\sigma^2(Z)}", font_size=38).shift(UP * 1.6)
        fitw(psi)
        self.play_beat(Write(psi))                                                 # 1

        eta = MathTex(r"\eta=(m,g,\sigma^2),\quad m(Z)=\mathbb{E}[X\mid Z]",
                      font_size=36, color=DIM).shift(UP * 0.5)
        fitw(eta)
        self.play_beat(Write(eta))                                                 # 2

        M = MathTex(r"M(\beta,\eta)=\mathbb{E}[\psi]", font_size=38, color=VAR).shift(DOWN * 0.4)
        self.play_beat(Write(M))                                                   # 3

        true = MathTex(r"\text{en }\eta_0:\quad Y-X^\top\beta_0-g_0=\epsilon",
                       font_size=36, color=BACK).shift(DOWN * 1.5)
        fitw(true)
        self.play_beat(Write(true))                                                # 4

        self.play_beat(eta.animate.set_opacity(0.0))                               # 5


class P5C_Desarrollo(NarratedScene):
    scene_key = "P5C_Desarrollo"

    def construct(self):
        self.header("Desarrollo · derivadas de Gâteaux")
        dg = MathTex(r"\partial_{\Delta g}M=-\mathbb{E}\!\Big[\tfrac{\Delta g}{\sigma^2}\,"
                     r"\mathbb{E}[\widetilde{X}\mid Z]\Big]=0", font_size=34).shift(UP * 2.0)
        fitw(dg)
        self.play_beat(Write(dg))                                                  # 1

        dm = MathTex(r"\partial_{\Delta m}M=-\mathbb{E}\!\Big[\tfrac{\Delta m}{\sigma^2}\,"
                     r"\mathbb{E}[\epsilon\mid Z]\Big]=0", font_size=34).shift(UP * 1.0)
        fitw(dm)
        self.play_beat(Write(dm))                                                  # 2

        ds = MathTex(r"\partial_{\Delta\sigma^2}M=-\mathbb{E}\!\Big[\tfrac{\Delta\sigma^2}{\sigma^4}\,"
                     r"\widetilde{X}\,\mathbb{E}[\epsilon\mid X,Z]\Big]=0", font_size=34).shift(UP * 0.0)
        fitw(ds)
        self.play_beat(Write(ds))                                                  # 3

        use = MathTex(r"\mathbb{E}[\widetilde{X}\mid Z]=0,\quad \mathbb{E}[\epsilon\mid X,Z]=0"
                      r"\ \Rightarrow\ \text{todas }=0", font_size=32, color=BACK).shift(DOWN * 1.0)
        fitw(use)
        self.play_beat(Write(use))                                                 # 4

        ortho = MathTex(r"\Rightarrow\ \psi\ \text{Neyman-ortogonal},\quad "
                        r"\text{sesgo}=O(\|\hat\eta-\eta_0\|^2)", font_size=32, color=RES).shift(DOWN * 1.9)
        fitw(ortho)
        self.play_beat(FadeOut(dg), FadeOut(dm), FadeOut(ds), Write(ortho))        # 5

        clt = MathTex(r"\text{tasas } o(n^{-1/4})\ \Rightarrow\ "
                      r"\sqrt{n}\,(\hat\beta-\beta_0)\xrightarrow{d}N\!\big(0,\mathrm{Var}[\phi^*]\big)",
                      font_size=30, color=EIG).shift(DOWN * 3.0)
        fitw(clt)
        self.play_beat(Write(clt))                                                 # 6


class P5C_Conclusion(NarratedScene):
    scene_key = "P5C_Conclusion"

    def construct(self):
        self.header("Conclusión · cierre del examen")
        l1 = Text("Las derivadas de Gâteaux se anulan ⇒ Neyman-ortogonal.",
                  font_size=26, color=BACK).shift(UP * 1.8)
        fitw(l1)
        self.play_beat(FadeIn(l1))                                                 # 1

        l2 = MathTex(r"\text{sesgo del plug-in}=O(\|\hat\eta-\eta_0\|^2)\ \ (\text{2º orden})",
                     font_size=32, color=DIM).shift(UP * 0.8)
        fitw(l2)
        self.play_beat(Write(l2))                                                  # 2

        l3 = MathTex(r"\boxed{\ \sqrt{n}\,(\hat\beta-\beta_0)\xrightarrow{d}N\!\big(0,\mathrm{Var}[\phi^*]\big)\ }",
                     font_size=34, color=RES).shift(DOWN * 0.1)
        fitw(l3)
        self.play_beat(Write(l3))                                                  # 3

        l4 = Text("Cross-fitting (Chernozhukov et al. 2018) quita el sesgo por sobreajuste.",
                  font_size=24, color=VAR).shift(DOWN * 1.2)
        fitw(l4)
        self.play_beat(FadeIn(l4))                                                 # 4

        moral = wrapt("Moraleja final: la ortogonalidad de Neyman une la estadística clásica y "
                      "el ML moderno. ¡Felicidades por llegar hasta aquí!", width=52,
                      font_size=25, color=RES, line_spacing=0.8).shift(DOWN * 2.7)
        fitw(moral)
        self.play_beat(FadeOut(l1), FadeOut(l4), FadeIn(moral))                    # 5
