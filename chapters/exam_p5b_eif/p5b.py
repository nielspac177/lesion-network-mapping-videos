# -*- coding: utf-8 -*-
"""Problema 5 (b): derivación de la EIF (residualizar + ponderar por 1/σ²).
  ./render.sh chapters/exam_p5b_eif/p5b.py -q qh \
      P5B_Intuicion P5B_Setup P5B_Desarrollo P5B_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P5B_Intuicion(NarratedScene):
    scene_key = "P5B_Intuicion"

    def construct(self):
        title = Text("Problema 5 · (b)  La EIF explícita", font_size=32, color=RES).to_edge(UP, buff=0.5)
        sub = Text("Residualizar y ponderar por 1/σ²", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Ecuación de momento ponderada por 1/σ²; ver que X̃ε/σ² es ortogonal a funciones "
            "de Z; concluir la fórmula de la EIF.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "La EIF da el estimador eficiente y su varianza; los pesos 1/σ² corrigen la "
            "heteroscedasticidad.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = wrapt("Residualizar X contra Z mata la confusión con g; ponderar por 1/σ² da el "
                     "peso óptimo.", width=46, font_size=27, color=BACK, line_spacing=0.8)
        fitw(idea)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        syms = VGroup(
            MathTex(r"\widetilde{X}=X-\mathbb{E}[X\mid Z]:\ \text{residual}", font_size=30, color=VAR),
            MathTex(r"\sigma^2(Z):\ \text{varianza condicional}", font_size=30, color=DIM),
            MathTex(r"\mathcal{I}:\ \text{información eficiente}", font_size=30, color=EIG),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).shift(DOWN * 0.3)
        fitw(syms)
        self.play_beat(FadeOut(idea), FadeIn(syms))                                # 5

        idea2 = Text("Idea: score → residualizar → ortogonalidad → EIF.",
                     font_size=26, color=VAR).shift(DOWN * 2.2)
        fitw(idea2)
        self.play_beat(FadeIn(idea2))                                              # 6

        self.play_beat(FadeOut(syms), FadeOut(idea2))                              # 7


class P5B_Setup(NarratedScene):
    scene_key = "P5B_Setup"

    def construct(self):
        self.header("Planteamiento · score y residualización")
        sc = MathTex(r"\text{score de trabajo:}\quad \frac{X\,\epsilon}{\sigma^2(Z)}",
                     font_size=40).shift(UP * 1.6)
        self.play_beat(Write(sc))                                                  # 1

        prob = wrapt("Problema: X está confundida con g(Z) a través de Z.",
                     width=46, font_size=27, color=BAD, line_spacing=0.8).shift(UP * 0.5)
        fitw(prob)
        self.play_beat(FadeIn(prob))                                               # 2

        res = MathTex(r"\text{residualizar:}\quad \widetilde{X}=X-\mathbb{E}[X\mid Z]",
                      font_size=38, color=VAR).shift(DOWN * 0.5)
        self.play_beat(Write(res))                                                 # 3

        seff = MathTex(r"S_{\mathrm{eff}}=\frac{\widetilde{X}\,\epsilon}{\sigma^2(Z)}",
                       font_size=40, color=BACK).shift(DOWN * 1.7)
        self.play_beat(Write(seff))                                                # 4

        self.play_beat(prob.animate.set_opacity(0.0))                              # 5


class P5B_Desarrollo(NarratedScene):
    scene_key = "P5B_Desarrollo"

    def construct(self):
        self.header("Desarrollo · ortogonalidad y EIF")
        l1 = MathTex(r"\mathbb{E}\!\left[\frac{\widetilde{X}\epsilon}{\sigma^2}\cdot"
                     r"\frac{a(Z)\epsilon}{\sigma^2}\right]", font_size=38).shift(UP * 2.1)
        self.play_beat(Write(l1))                                                  # 1

        l2 = MathTex(r"=\ \mathbb{E}\!\left[a(Z)\,\widetilde{X}\,\frac{\epsilon^2}{\sigma^4}\right]",
                     font_size=38).shift(UP * 1.1)
        fitw(l2)
        self.play_beat(Write(l2))                                                  # 2

        l3 = MathTex(r"=\ \mathbb{E}\!\left[\frac{a(Z)}{\sigma^2}\,\mathbb{E}[\widetilde{X}\mid Z]\right]",
                     font_size=38, color=BACK).shift(UP * 0.1)
        fitw(l3)
        self.play_beat(Write(l3))                                                  # 3

        l4 = MathTex(r"\mathbb{E}[\widetilde{X}\mid Z]=0\ \Longrightarrow\ =0\ \ (\text{ortogonal})",
                     font_size=38, color=RES).shift(DOWN * 0.9)
        fitw(l4)
        self.play_beat(Write(l4))                                                  # 4

        eif = MathTex(r"\phi^*=\Big(\mathbb{E}\big[\tfrac{\widetilde{X}\widetilde{X}^\top}{\sigma^2(Z)}\big]\Big)^{-1}"
                      r"\frac{\widetilde{X}\,\epsilon}{\sigma^2(Z)}", font_size=36, color=EIG).shift(DOWN * 2.1)
        fitw(eif)
        self.play_beat(FadeOut(l1), FadeOut(l2), FadeOut(l3), Write(eif))          # 5

        robin = MathTex(r"\sigma^2\equiv\text{const}:\ \phi^*=(\mathbb{E}[\widetilde{X}\widetilde{X}^\top])^{-1}"
                        r"\widetilde{X}\epsilon\ \ (\text{Robinson 1988})", font_size=30, color=DIM).shift(DOWN * 3.2)
        fitw(robin)
        self.play_beat(FadeIn(robin))                                              # 6


class P5B_Conclusion(NarratedScene):
    scene_key = "P5B_Conclusion"

    def construct(self):
        self.header("Conclusión")
        box = MathTex(r"\boxed{\ \phi^*(O_i)=\Big(\mathbb{E}\big[\tfrac{\widetilde{X}_i\widetilde{X}_i^\top}{\sigma^2(Z_i)}\big]\Big)^{-1}"
                      r"\frac{\widetilde{X}_i\,\epsilon_i}{\sigma^2(Z_i)}\ }", font_size=34, color=RES).shift(UP * 1.4)
        fitw(box)
        self.play_beat(Write(box))                                                 # 1

        l2 = Text("Los pesos 1/σ² = corrección por heteroscedasticidad.",
                  font_size=26, color=BACK).shift(UP * 0.1)
        fitw(l2)
        self.play_beat(FadeIn(l2))                                                 # 2

        l3 = Text("Homoscedástico ⇒ Robinson (1988), sin pesos.",
                  font_size=26, color=DIM).shift(DOWN * 0.7)
        fitw(l3)
        self.play_beat(FadeIn(l3))                                                 # 3

        l4 = Text("Residualizar + ponderar por varianza inversa = score eficiente.",
                  font_size=25, color=VAR).shift(DOWN * 1.5)
        fitw(l4)
        self.play_beat(FadeIn(l4))                                                 # 4

        moral = wrapt("Moraleja: residualizar mata el sesgo por el nuisance; ponderar por 1/σ² "
                      "alcanza la eficiencia.", width=52, font_size=25, color=RES,
                      line_spacing=0.8).shift(DOWN * 2.8)
        fitw(moral)
        self.play_beat(FadeOut(l2), FadeOut(l3), FadeOut(l4), FadeIn(moral))       # 5
