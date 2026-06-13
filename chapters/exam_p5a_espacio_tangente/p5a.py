# -*- coding: utf-8 -*-
"""Problema 5 (a): espacio tangente nuisance y representación de Riesz (EIF).
  ./render.sh chapters/exam_p5a_espacio_tangente/p5a.py -q qh \
      P5A_Intuicion P5A_Setup P5A_Desarrollo P5A_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P5A_Intuicion(NarratedScene):
    scene_key = "P5A_Intuicion"

    def construct(self):
        title = Text("Problema 5 · (a)  Espacio tangente y Riesz", font_size=30, color=RES).to_edge(UP, buff=0.5)
        sub = Text("Inferencia semiparamétrica", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Definir el espacio tangente nuisance Λ ⊂ L²(P), su norma, y enunciar la "
            "representación de Riesz para la EIF φ*.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "Es el puente clásico ↔ machine learning: estimar β bien aunque g y σ² se estimen "
            "con ML imperfecto.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        idea = wrapt("Geometría: las perturbaciones del nuisance forman Λ; estimar β = proyectar "
                     "fuera de Λ.", width=46, font_size=27, color=BACK, line_spacing=0.8)
        fitw(idea)
        self.play_beat(FadeOut(why), FadeIn(idea))                                 # 4

        s1 = VGroup(
            MathTex(r"Y:\ \text{respuesta}", font_size=28, color=VAR),
            MathTex(r"X:\ \text{covariables de interés}", font_size=28, color=VAR),
            MathTex(r"Z:\ \text{covariables nuisance}", font_size=28, color=DIM),
            MathTex(r"\beta:\ \text{parámetro finito}", font_size=28, color=RES),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).shift(DOWN * 0.3)
        fitw(s1)
        self.play_beat(FadeOut(idea), FadeIn(s1))                                  # 5

        s2 = VGroup(
            MathTex(r"g,\ \sigma^2(Z):\ \text{nuisance}", font_size=28, color=BAD),
            MathTex(r"O=(Y,X,Z),\quad \widetilde{X}=X-\mathbb{E}[X\mid Z]", font_size=28, color=EIG),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).shift(DOWN * 0.3)
        fitw(s2)
        self.play_beat(FadeOut(s1), FadeIn(s2))                                    # 6

        idea2 = Text("Idea: producto interno → tangente → Riesz.",
                     font_size=26, color=VAR).shift(DOWN * 2.2)
        self.play_beat(FadeIn(idea2))                                              # 7

        self.play_beat(FadeOut(s2), FadeOut(idea2))                                # 8


class P5A_Setup(NarratedScene):
    scene_key = "P5A_Setup"

    def construct(self):
        self.header("Planteamiento · el modelo y L²(P)")
        model = MathTex(r"Y_i=X_i^\top\beta+g(Z_i)+\epsilon_i", font_size=42).shift(UP * 1.7)
        self.play_beat(Write(model))                                               # 1

        cond = MathTex(r"\mathbb{E}[\epsilon\mid X,Z]=0,\quad \mathbb{E}[\epsilon^2\mid X,Z]=\sigma^2(Z)",
                       font_size=36, color=DIM).shift(UP * 0.6)
        fitw(cond)
        self.play_beat(Write(cond))                                               # 2

        inner = MathTex(r"\langle f,h\rangle=\mathbb{E}[f(O)\,h(O)],\quad \|f\|^2=\mathbb{E}[f(O)^2]",
                        font_size=36, color=BACK).shift(DOWN * 0.5)
        fitw(inner)
        self.play_beat(Write(inner))                                              # 3

        roles = MathTex(r"\beta:\ \text{finito}\qquad g,\ \sigma^2:\ \text{infinito-dim. (nuisance)}",
                        font_size=34, color=VAR).shift(DOWN * 1.7)
        fitw(roles)
        self.play_beat(FadeIn(roles))                                             # 4

        self.play_beat(cond.animate.set_opacity(0.0), roles.animate.set_opacity(0.0))  # 5


class P5A_Desarrollo(NarratedScene):
    scene_key = "P5A_Desarrollo"

    def construct(self):
        self.header("Desarrollo · tangente y Riesz")
        l1 = wrapt("Λ = perturbaciones de camino de la log-verosimilitud al variar g y σ².",
                   width=50, font_size=27, color=DIM, line_spacing=0.8).shift(UP * 2.1)
        fitw(l1)
        self.play_beat(FadeIn(l1))                                                 # 1

        score = MathTex(r"\text{perturbar }g\ \text{en }a(Z)\ \Rightarrow\ "
                        r"\text{score}=\frac{a(Z)\,\epsilon}{\sigma^2(Z)}",
                        font_size=36, color=BACK).shift(UP * 1.0)
        fitw(score)
        self.play_beat(Write(score))                                               # 2

        clo = MathTex(r"\Lambda=\overline{\mathrm{span}}^{\,L^2}\{\text{scores nuisance}\}",
                      font_size=36, color=VAR).shift(UP * 0.0)
        fitw(clo)
        self.play_beat(Write(clo))                                                 # 3

        riesz = MathTex(r"\dot\Psi_\eta(s)=\langle \phi^*,\,s\rangle_{L^2}"
                        r"\quad \forall s\in\text{tangente}", font_size=38, color=RES).shift(DOWN * 1.1)
        fitw(riesz)
        self.play_beat(FadeOut(l1), Write(riesz))                                  # 4

        perp = MathTex(r"\phi^*\in\Lambda^{\perp}", font_size=42, color=EIG).shift(DOWN * 2.2)
        self.play_beat(Write(perp))                                                # 5

        why = Text("⇒ φ* es inmune a errores de 1er orden en g y σ².",
                   font_size=26, color=DIM).shift(DOWN * 3.1)
        fitw(why)
        self.play_beat(FadeIn(why))                                                # 6


class P5A_Conclusion(NarratedScene):
    scene_key = "P5A_Conclusion"

    def construct(self):
        self.header("Conclusión")
        l1 = Text("Definimos Λ y la norma de L²(P).", font_size=27, color=DIM).shift(UP * 1.6)
        self.play_beat(FadeIn(l1))                                                 # 1

        l2 = MathTex(r"\text{Riesz}\ \Rightarrow\ \phi^*\ \text{representa la derivada de }\beta",
                     font_size=34, color=BACK).shift(UP * 0.6)
        fitw(l2)
        self.play_beat(Write(l2))                                                  # 2

        l3 = MathTex(r"\boxed{\ \phi^*\in\Lambda^{\perp}\ \ (\text{ortogonal al nuisance})\ }",
                     font_size=36, color=RES).shift(DOWN * 0.3)
        fitw(l3)
        self.play_beat(Write(l3))                                                  # 3

        l4 = Text("Esa ortogonalidad es la fuente de la robustez (siguiente: la EIF explícita).",
                  font_size=24, color=VAR).shift(DOWN * 1.4)
        fitw(l4)
        self.play_beat(FadeIn(l4))                                                 # 4

        moral = wrapt("Moraleja: pensar con proyecciones en L² vuelve manejable un problema "
                      "infinito-dimensional.", width=52, font_size=25, color=RES,
                      line_spacing=0.8).shift(DOWN * 2.7)
        fitw(moral)
        self.play_beat(FadeOut(l1), FadeOut(l4), FadeIn(moral))                    # 5
