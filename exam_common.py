# -*- coding: utf-8 -*-
"""Utilidades compartidas para los capítulos del examen (serie Teoría Estadística).

Importable porque render.sh pone la raíz del repo en PYTHONPATH.
Reglas: layouts sin overlap (fitw), texto envuelto (wrapt) y bloque de contexto
« La pregunta / Por qué importa » para abrir cada video.
"""
import textwrap
from manim import VGroup, Text, DOWN

BODY = "#D8DBE0"


def fitw(m, w=12.6):
    """Encoge un mobject si excede el ancho seguro del frame."""
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def wrapt(s, width=42, **kw):
    """Text con saltos de línea automáticos (manim Text no envuelve solo)."""
    return Text("\n".join(textwrap.wrap(s, width)), **kw)


def context_block(label, text, lcolor, width=44):
    """Bloque « etiqueta + párrafo » para enunciar la pregunta / su importancia."""
    head = Text(label, font_size=26, color=lcolor)
    body = wrapt(text, width=width, font_size=24, color=BODY, line_spacing=0.8)
    return fitw(VGroup(head, body).arrange(DOWN, buff=0.3), 12.4)
