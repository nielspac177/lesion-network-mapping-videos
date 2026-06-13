# -*- coding: utf-8 -*-
"""Problema 2 (c): UMVUE, varianza y eficiencia (Cramér-Rao).
  ./render.sh chapters/exam_p2c_umvue_cramer_rao/p2c.py -q qh \
      P2C_Intuicion P2C_Setup P2C_Desarrollo P2C_Conclusion
"""
from manim import *
from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM
from exam_common import fitw, wrapt, context_block
from narration import SCENES

NarratedScene.narration = SCENES


class P2C_Intuicion(NarratedScene):
    scene_key = "P2C_Intuicion"

    def construct(self):
        title = Text("Problema 2 · (c)  UMVUE y eficiencia", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("Lehmann–Scheffé y la cota de Cramér–Rao", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Ver que τ̂_RB es insesgado ⇒ UMVUE (Lehmann–Scheffé); calcular su varianza "
            "α⁻²/n y compararla con la cota de Cramér–Rao.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "Tres ideas encajan: Rao–Blackwell construye, Lehmann–Scheffé certifica, "
            "Cramér–Rao mide.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        defs = VGroup(
            Text("UMVUE = mejor insesgado (mínima varianza)", font_size=26, color=VAR),
            Text("Eficiente = alcanza la cota teórica mínima", font_size=26, color=BACK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        fitw(defs)
        self.play_beat(FadeOut(why), FadeIn(defs))                                 # 4

        syms = VGroup(
            MathTex(r"\tau'(\alpha):\ \text{derivada del objetivo}", font_size=32, color=DIM),
            MathTex(r"I_1(\alpha):\ \text{información de Fisher}", font_size=32, color=EIG),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 1.4)
        self.play_beat(FadeOut(defs), FadeIn(syms))                                # 5

        idea = Text("Idea: comparar la varianza con la cota inferior.",
                    font_size=26, color=VAR).shift(DOWN * 0.2)
        self.play_beat(FadeIn(idea))                                               # 6

        self.play_beat(FadeOut(syms), FadeOut(idea))                               # 7


class P2C_Setup(NarratedScene):
    scene_key = "P2C_Setup"

    def construct(self):
        self.header("Planteamiento · UMVUE y varianza")
        unb = MathTex(r"\mathbb{E}_\alpha[\hat\tau_{RB}]=\frac1\alpha=\tau",
                      font_size=42).shift(UP * 1.6)
        self.play_beat(Write(unb))                                                 # 1

        ls = wrapt("Función de un suficiente-completo + insesgado ⇒ UMVUE (Lehmann–Scheffé).",
                   width=48, font_size=26, color=BACK, line_spacing=0.8).shift(UP * 0.5)
        fitw(ls)
        self.play_beat(FadeIn(ls))                                                 # 2

        v1 = MathTex(r"\mathrm{Var}_\alpha(\hat\tau_{RB})=\frac{\mathrm{Var}(T_n)}{n^2}",
                     font_size=42).shift(DOWN * 0.6)
        self.play_beat(Write(v1))                                                  # 3

        v2 = MathTex(r"=\frac{n/\alpha^2}{n^2}=\frac{\alpha^{-2}}{n}",
                     font_size=42, color=RES).next_to(v1, DOWN, buff=0.4)
        self.play_beat(Write(v2))                                                  # 4

        self.play_beat(ls.animate.set_opacity(0.0))                                # 5


class P2C_Desarrollo(NarratedScene):
    scene_key = "P2C_Desarrollo"

    def construct(self):
        self.header("Desarrollo · cota de Cramér–Rao")
        cr = MathTex(r"\mathrm{CR}(\tau)=\frac{[\tau'(\alpha)]^2}{n\,I_1(\alpha)}",
                     font_size=44).shift(UP * 2.0)
        self.play_beat(Write(cr))                                                  # 1

        d = MathTex(r"\tau(\alpha)=\alpha^{-1}\ \Rightarrow\ \tau'(\alpha)=-\alpha^{-2}",
                    font_size=38, color=BACK).shift(UP * 0.7)
        self.play_beat(Write(d))                                                   # 2

        fish = MathTex(r"\frac{\partial^2}{\partial\alpha^2}\log f=-\alpha^{-2}"
                       r"\ \Rightarrow\ I_1(\alpha)=\alpha^{-2}",
                       font_size=38, color=EIG).shift(DOWN * 0.2)
        fitw(fish)
        self.play_beat(Write(fish))                                                # 3

        sub_ = MathTex(r"\mathrm{CR}(\tau)=\frac{(-\alpha^{-2})^2}{n\,\alpha^{-2}}"
                       r"=\frac{\alpha^{-4}}{n\,\alpha^{-2}}", font_size=40).shift(DOWN * 1.4)
        fitw(sub_)
        self.play_beat(FadeOut(d), FadeOut(fish), Write(sub_))                     # 4

        eq = MathTex(r"=\ \frac{\alpha^{-2}}{n}", font_size=42, color=RES).next_to(sub_, DOWN, buff=0.4)
        self.play_beat(Write(eq))                                                  # 5

        same = MathTex(r"=\ \mathrm{Var}_\alpha(\hat\tau_{RB})",
                       font_size=42, color=VAR).next_to(eq, RIGHT, buff=0.3)
        self.play_beat(Write(same))                                                # 6


class P2C_Conclusion(NarratedScene):
    scene_key = "P2C_Conclusion"

    def construct(self):
        self.header("Conclusión")
        eq = MathTex(r"\mathrm{Var}_\alpha(\hat\tau_{RB})=\mathrm{CR}(\tau)=\frac{\alpha^{-2}}{n}",
                     font_size=44).shift(UP * 1.5)
        fitw(eq)
        self.play_beat(Write(eq))                                                  # 1

        box = MathTex(r"\boxed{\ \text{el UMVUE es eficiente para todo }\alpha>0\ }",
                      font_size=38, color=RES).shift(UP * 0.2)
        fitw(box)
        self.play_beat(Write(box))                                                 # 2

        recap = VGroup(
            Text("Rao–Blackwell  →  construye", font_size=24, color=DIM),
            Text("Lehmann–Scheffé  →  certifica", font_size=24, color=DIM),
            Text("Cramér–Rao  →  mide", font_size=24, color=DIM),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(DOWN * 1.3)
        self.play_beat(FadeIn(recap))                                              # 3

        top = Text("Alcanzar la cota es lo máximo para un insesgado.",
                   font_size=25, color=BACK).shift(DOWN * 2.6)
        fitw(top)
        self.play_beat(FadeIn(top))                                                # 4

        moral = wrapt("Moraleja: si la varianza iguala la cota de Cramér–Rao, no hay insesgado "
                      "mejor.", width=52, font_size=25, color=RES, line_spacing=0.8).shift(DOWN * 3.3)
        fitw(moral)
        self.play_beat(FadeOut(recap), FadeOut(top), FadeIn(moral))                # 5
