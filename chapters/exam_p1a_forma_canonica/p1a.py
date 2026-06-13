# -*- coding: utf-8 -*-
"""Problema 1 (a): forma canónica de familia exponencial (Normal Inversa).
Estándar detallado/lento, layout sin overlap. Render:
  ./render.sh chapters/exam_p1a_forma_canonica/p1a.py -q qh \
      P1A_Intuicion P1A_Setup P1A_Desarrollo P1A_Conclusion
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
    g = VGroup(head, body).arrange(DOWN, buff=0.3)
    return fitw(g, 12.4)


class P1A_Intuicion(NarratedScene):
    scene_key = "P1A_Intuicion"

    def construct(self):
        title = Text("Problema 1 · (a)  Forma canónica", font_size=34, color=RES).to_edge(UP, buff=0.5)
        sub = Text("La Normal Inversa como familia exponencial", font_size=22, color=DIM)
        sub.next_to(title, DOWN, buff=0.22)
        self.play_beat(Write(title), FadeIn(sub))                                  # 1

        ask = context_block(
            "La pregunta",
            "Reescribir la densidad IG en forma canónica: hallar η, T(x), h(x) y A(η), "
            "y verificar que la familia es regular.", BACK).shift(DOWN * 0.3)
        self.play_beat(FadeIn(ask))                                                # 2

        why = context_block(
            "Por qué importa",
            "La forma canónica es la puerta a toda la teoría: suficiencia, completitud y "
            "eficiencia salen casi gratis desde aquí.", EIG).shift(DOWN * 0.3)
        self.play_beat(FadeOut(ask), FadeIn(why))                                  # 3

        tnorm = Text("Es la forma normalizada de un modelo.", font_size=30, color=BACK)
        self.play_beat(FadeOut(why), FadeIn(tnorm))                                # 4

        form = MathTex(r"f(x)=h(x)\,\exp\bigl\{\eta\,T(x)-A(\eta)\bigr\}", font_size=50)
        form.shift(UP * 0.8)
        self.play_beat(FadeOut(tnorm), Write(form))                                # 5

        labels = VGroup(
            Text("h(x): parte sin parámetro", font_size=24, color=BACK),
            Text("η: parámetro natural", font_size=24, color=EIG),
            Text("T(x): estadístico suficiente", font_size=24, color=VAR),
            Text("A(η): normaliza a uno", font_size=24, color=RES),
        ).arrange_in_grid(rows=2, cols=2, buff=(1.2, 0.5), col_alignments="ll")
        labels.next_to(form, DOWN, buff=0.8)
        self.play_beat(LaggedStart(*[FadeIn(m) for m in labels], lag_ratio=0.35))  # 4

        payoff = Text("El premio: el estadístico suficiente aparece solo.",
                      font_size=26, color=VAR).shift(DOWN * 1.2)
        self.play_beat(FadeOut(labels), FadeOut(form), FadeIn(payoff))             # 5

        plan = Text("Plan:   1) abrir el cuadrado     2) leer cada pieza",
                    font_size=26, color=DIM).shift(DOWN * 1.2)
        self.play_beat(FadeOut(payoff), FadeIn(plan))                              # 6


class P1A_Setup(NarratedScene):
    scene_key = "P1A_Setup"

    def construct(self):
        self.header("Planteamiento")
        dens = MathTex(
            r"f(x\mid\lambda)=",
            r"\left(\frac{\lambda}{2\pi x^{3}}\right)^{1/2}",
            r"\exp\!\left\{-\frac{\lambda(x-\mu)^2}{2\mu^2 x}\right\}",
            font_size=46,
        ).shift(UP * 1.1)
        self.play_beat(Write(dens))                                               # 1

        known = MathTex(r"x>0\ \text{dato}\qquad \mu\ \text{conocido}\qquad "
                        r"\lambda>0\ \text{desconocido}", font_size=32)
        known.set_color(DIM).next_to(dens, DOWN, buff=0.7)
        self.play_beat(FadeIn(known))                                             # 2

        b_root = SurroundingRectangle(dens[1], color=BACK, buff=0.12)
        cap1 = Text("la raíz", font_size=22, color=BACK).next_to(known, DOWN, buff=0.6)
        self.play_beat(Create(b_root), FadeIn(cap1))                              # 3

        b_exp = SurroundingRectangle(dens[2], color=BAD, buff=0.12)
        cap2 = Text("el exponente", font_size=22, color=BAD).next_to(known, DOWN, buff=0.6)
        self.play_beat(FadeOut(b_root), FadeOut(cap1), Create(b_exp), FadeIn(cap2))  # 4

        goal = Text("Meta: separar lo que depende de λ de lo que depende solo de x.",
                    font_size=26, color=RES).next_to(known, DOWN, buff=0.9)
        fitw(goal)
        self.play_beat(FadeOut(b_exp), FadeOut(cap2), FadeIn(goal))               # 5

        self.play_beat(FadeOut(goal))                                            # 6


class P1A_Desarrollo(NarratedScene):
    scene_key = "P1A_Desarrollo"

    def construct(self):
        self.header("Desarrollo")
        step1 = Text("Paso 1 · abrir el cuadrado", font_size=28, color=BACK).to_edge(UP, buff=1.0)
        self.play_beat(FadeIn(step1))                                             # 1

        eq1 = MathTex(r"\frac{(x-\mu)^2}{x}", r"=", r"\frac{x^2-2\mu x+\mu^2}{x}",
                      font_size=46).next_to(step1, DOWN, buff=0.55)
        self.play_beat(Write(eq1))                                               # 2

        eq2 = MathTex(r"=\ x-2\mu+\frac{\mu^2}{x}", font_size=46).next_to(eq1, DOWN, buff=0.4)
        self.play_beat(Write(eq2))                                               # 3

        expo = MathTex(r"\text{exponente}=-\frac{\lambda}{2\mu^2}\cdot\frac{(x-\mu)^2}{x}",
                       font_size=44).next_to(eq2, DOWN, buff=0.5)
        self.play_beat(Write(expo))                                              # 4

        expo_top = MathTex(r"-\frac{\lambda}{2\mu^2}\cdot\frac{(x-\mu)^2}{x}",
                           font_size=34, color=DIM).to_edge(UP, buff=0.95)
        pT = MathTex(r"T(x)=\frac{(x-\mu)^2}{x}", font_size=40, color=VAR).move_to([-3.2, 0.7, 0])
        ph = MathTex(r"h(x)=(2\pi x^3)^{-1/2}", font_size=40, color=BACK).move_to([3.2, 0.7, 0])
        pe = MathTex(r"\eta=-\frac{\lambda}{2\mu^2}", font_size=40, color=EIG).move_to([-3.2, -1.3, 0])
        pA = MathTex(r"A(\eta)=-\tfrac12\log\lambda", font_size=40, color=RES).move_to([3.2, -1.3, 0])
        plam = MathTex(r"\lambda^{1/2}=e^{\frac12\log\lambda}", font_size=38, color=DIM).move_to([0, -2.7, 0])

        self.play_beat(FadeOut(step1), FadeOut(eq1), FadeOut(eq2),
                       ReplacementTransform(expo, expo_top), FadeIn(pT))          # 5
        self.play_beat(FadeIn(ph))                                               # 6
        self.play_beat(FadeIn(pe))                                               # 7
        self.play_beat(FadeIn(plam))                                             # 8
        self.play_beat(FadeOut(plam), Write(pA))                                 # 9


class P1A_Conclusion(NarratedScene):
    scene_key = "P1A_Conclusion"

    def construct(self):
        self.header("Conclusión")
        intro = Text("Verificamos la regularidad: miramos el espacio natural ℋ.",
                     font_size=26, color=DIM).to_edge(UP, buff=1.0)
        fitw(intro)
        self.play_beat(FadeIn(intro))                                            # 1

        nat = MathTex(r"\mathcal{H}=\{\eta(\lambda):\lambda>0\}", font_size=48).shift(UP * 0.9)
        self.play_beat(Write(nat))                                               # 2

        interval = MathTex(r"=\ (-\infty,\,0)", font_size=48, color=EIG)
        interval.next_to(nat, DOWN, buff=0.45)
        self.play_beat(Write(interval))                                          # 3

        reg = Text("intervalo abierto  ⇒  familia exponencial regular (rango 1)",
                   font_size=26, color=BACK).next_to(interval, DOWN, buff=0.7)
        fitw(reg)
        self.play_beat(FadeOut(intro), FadeIn(reg))                              # 4

        recap = MathTex(
            r"T(x)=\tfrac{(x-\mu)^2}{x},\ \ h(x)=(2\pi x^3)^{-\frac12},\ \ "
            r"\eta=-\tfrac{\lambda}{2\mu^2},\ \ A(\eta)=-\tfrac12\log\lambda",
            font_size=32,
        ).set_color(DIM).shift(UP * 0.8)
        fitw(recap)
        self.play_beat(FadeOut(nat), FadeOut(interval), FadeOut(reg), FadeIn(recap))  # 5

        why = Text("La regularidad habilita completitud y eficiencia (próximos videos).",
                   font_size=24, color=DIM).next_to(recap, DOWN, buff=0.6)
        fitw(why)
        self.play_beat(FadeIn(why))                                             # 6

        moral = Text("Moraleja: en forma canónica, la suficiencia se lee, no se calcula.",
                     font_size=27, color=RES).next_to(why, DOWN, buff=0.55)
        fitw(moral)
        self.play_beat(Write(moral))                                            # 7
