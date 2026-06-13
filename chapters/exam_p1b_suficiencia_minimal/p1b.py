# -*- coding: utf-8 -*-
"""Problema 1 (b): suficiencia minimal (criterio de Lehmann-Scheffé).
  ./render.sh chapters/exam_p1b_suficiencia_minimal/p1b.py -q qh \
      P1B_Intuicion P1B_Setup P1B_Desarrollo P1B_Conclusion
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


class P1B_Intuicion(NarratedScene):
    scene_key = "P1B_Intuicion"

    def construct(self):
        title = Text("Problema 1 · (b)  Suficiencia minimal", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("El criterio de Lehmann–Scheffé", font_size=22, color=DIM).next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Probar que f(x|λ)/f(y|λ) es constante en λ  ⟺  T(x)=T(y), "
            "y concluir que T es suficiente minimal.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "El suficiente minimal es la compresión óptima de los datos: "
            "ni se pierde información sobre λ, ni sobra nada.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        t = Text("Minimal = el resumen más comprimido posible.", font_size=30, color=BACK)
        self.play_beat(FadeOut(why), FadeIn(t))                                    # 4

        crit = MathTex(r"\frac{f(\mathbf{x}\mid\lambda)}{f(\mathbf{y}\mid\lambda)}"
                       r"\ \text{constante en }\lambda \iff T(\mathbf{x})=T(\mathbf{y})",
                       font_size=40)
        fitw(crit)
        self.play_beat(FadeOut(t), Write(crit))                                    # 3

        cap = Text("« indistinguibles »   ⟺   « mismo resumen »", font_size=24, color=DIM)
        cap.next_to(crit, DOWN, buff=0.7)
        self.play_beat(FadeIn(cap))                                                # 4

        strat = Text("Estrategia: escribir el cociente y ver desaparecer λ.",
                     font_size=26, color=VAR).shift(DOWN * 1.3)
        self.play_beat(FadeOut(crit), FadeOut(cap), FadeIn(strat))                 # 5

        self.play_beat(FadeOut(strat))                                             # 6


class P1B_Setup(NarratedScene):
    scene_key = "P1B_Setup"

    def construct(self):
        self.header("Planteamiento · densidad conjunta")
        prod = MathTex(r"f(\mathbf{x}\mid\lambda)=\prod_{i=1}^{n} f(x_i\mid\lambda)",
                       font_size=44).shift(UP * 1.3)
        self.play_beat(Write(prod))                                                # 1

        grouped = MathTex(
            r"f(\mathbf{x}\mid\lambda)=",
            r"\lambda^{n/2}",
            r"\Big[\textstyle\prod_i (2\pi x_i^3)^{-1/2}\Big]",
            r"\exp\!\Big\{-\tfrac{\lambda}{2\mu^2}\,T(\mathbf{x})\Big\}",
            font_size=38,
        ).shift(UP * 0.2)
        fitw(grouped)
        self.play_beat(FadeIn(grouped))                                            # 2

        tdef = MathTex(r"T(\mathbf{x})=\sum_{i=1}^{n}\frac{(x_i-\mu)^2}{x_i}",
                       font_size=40, color=VAR).next_to(grouped, DOWN, buff=0.7)
        self.play_beat(Write(tdef))                                                # 3

        b1 = SurroundingRectangle(grouped[1], color=EIG, buff=0.08)
        b2 = SurroundingRectangle(grouped[3], color=EIG, buff=0.08)
        cap = Text("λ solo aparece aquí", font_size=24, color=EIG).next_to(tdef, DOWN, buff=0.55)
        self.play_beat(Create(b1), Create(b2), FadeIn(cap))                        # 4

        self.play_beat(FadeOut(b1), FadeOut(b2), FadeOut(cap))                     # 5


class P1B_Desarrollo(NarratedScene):
    scene_key = "P1B_Desarrollo"

    def construct(self):
        self.header("Desarrollo · el cociente")
        ratio = MathTex(r"\frac{f(\mathbf{x}\mid\lambda)}{f(\mathbf{y}\mid\lambda)}",
                        font_size=52).shift(UP * 1.8)
        self.play_beat(Write(ratio))                                               # 1

        cap = Text("los factores λ^(n/2) se cancelan", font_size=24, color=DIM).shift(UP * 0.6)
        self.play_beat(FadeIn(cap))                                                # 2

        full = MathTex(r"=\ C(\mathbf{x},\mathbf{y})\,"
                       r"\exp\!\Big\{-\tfrac{\lambda}{2\mu^2}\big(T(\mathbf{x})-T(\mathbf{y})\big)\Big\}",
                       font_size=40)
        fitw(full)
        self.play_beat(FadeOut(cap), ratio.animate.scale(0.7).to_edge(UP, buff=1.0),
                       Write(full))                                                # 3

        ccap = Text("C(x,y): libre de λ", font_size=22, color=DIM).next_to(full, DOWN, buff=0.5)
        self.play_beat(FadeIn(ccap))                                               # 4

        imp1 = VGroup(
            Text("(⇒)  si T(x)=T(y):", font_size=26, color=BACK),
            MathTex(r"\text{exponente}=0\ \Rightarrow\ \text{cociente}=C\ (\text{const en }\lambda)",
                    font_size=34),
        ).arrange(DOWN, buff=0.3).shift(DOWN * 1.6)
        self.play_beat(FadeOut(ccap), FadeIn(imp1))                                # 5

        imp2 = VGroup(
            Text("(⇐)  si el cociente es const en λ:", font_size=26, color=BACK),
            MathTex(r"e^{c\lambda}\ \text{const},\quad c=-\tfrac{1}{2\mu^2}\big(T(\mathbf{x})-T(\mathbf{y})\big)",
                    font_size=34),
        ).arrange(DOWN, buff=0.3).shift(DOWN * 1.6)
        self.play_beat(FadeOut(imp1), FadeIn(imp2))                                # 6

        concl = MathTex(r"\exp\ \text{inyectiva}\ \Rightarrow\ c=0\ \Rightarrow\ T(\mathbf{x})=T(\mathbf{y})",
                        font_size=36, color=RES).shift(DOWN * 3.0)
        fitw(concl)
        self.play_beat(Write(concl))                                               # 7


class P1B_Conclusion(NarratedScene):
    scene_key = "P1B_Conclusion"

    def construct(self):
        self.header("Conclusión")
        equiv = MathTex(r"\frac{f(\mathbf{x}\mid\lambda)}{f(\mathbf{y}\mid\lambda)}"
                        r"\ \text{const}\iff T(\mathbf{x})=T(\mathbf{y})", font_size=42).shift(UP * 1.2)
        fitw(equiv)
        self.play_beat(Write(equiv))                                               # 1

        cap = Text("equivalencia probada en ambas direcciones", font_size=24, color=DIM)
        cap.next_to(equiv, DOWN, buff=0.5)
        self.play_beat(FadeIn(cap))                                                # 2

        name = Text("Criterio de Lehmann–Scheffé", font_size=30, color=BACK).shift(DOWN * 0.3)
        self.play_beat(FadeOut(cap), FadeIn(name))                                 # 3

        res = MathTex(r"\boxed{\,T(\mathbf{X})=\sum_{i=1}^n\frac{(X_i-\mu)^2}{X_i}"
                      r"\ \text{es suficiente minimal}\,}", font_size=36, color=RES)
        fitw(res)
        res.shift(DOWN * 1.5)
        self.play_beat(Write(res))                                                 # 4

        moral = Text("Moraleja: la inyectividad de exp convierte « const en λ » en « T iguales ».",
                     font_size=24, color=RES).shift(DOWN * 3.0)
        fitw(moral)
        self.play_beat(FadeOut(name), FadeIn(moral))                               # 5
