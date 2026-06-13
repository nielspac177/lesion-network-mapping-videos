# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 3 (b): test UMP aleatorizado."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P3B_Intuicion": S(
        "En este video construimos el test uniformemente más potente, usando el teorema de "
        "Karlin y Rubin.",
        "La pregunta del inciso es: invocar Karlin y Rubin para construir el test UMP de nivel "
        "alfa; y como te es discreta, especificar la regla aleatorizada y dar la fórmula "
        "explícita de gamma alfa.",
        "¿Por qué importa? Karlin y Rubin convierten el MLR del video anterior en un test "
        "óptimo. Y la aleatorización resuelve el problema de que te es discreta.",
        "La intuición: rechazamos cuando te es grande. El único detalle técnico es clavar el "
        "nivel exactamente en alfa.",
        "Los símbolos: ce alfa es el umbral; gamma alfa es la probabilidad de rechazar justo en "
        "la frontera; y efe es la función de distribución de una Poisson de media ene lambda "
        "cero.",
        "La idea: imponer que la esperanza de fi bajo lambda cero sea alfa, y despejar gamma "
        "alfa.",
        "Empecemos.",
    ),
    "P3B_Setup": S(
        "Bajo la hipótesis nula exacta, lambda igual a lambda cero, el estadístico te sigue una "
        "Poisson de media ene lambda cero.",
        "Como esa distribución es discreta, en general no existe un entero ce alfa tal que la "
        "probabilidad de que te supere ce alfa sea exactamente alfa.",
        "Por eso introducimos aleatorización justo en el valor frontera.",
        "Definimos ce alfa como el menor entero ce tal que la probabilidad de que te supere ce "
        "es menor o igual que alfa.",
        "Falta calibrar gamma alfa para fijar el nivel exacto.",
    ),
    "P3B_Desarrollo": S(
        "La regla de decisión es: rechazar con certeza si te es mayor que ce alfa; rechazar con "
        "probabilidad gamma alfa si te es igual a ce alfa; y no rechazar si te es menor.",
        "Imponemos el nivel exacto: la esperanza de fi bajo lambda cero debe ser igual a alfa.",
        "Esa esperanza es la probabilidad de que te supere ce alfa, más gamma alfa por la "
        "probabilidad de que te sea igual a ce alfa.",
        "En términos de la función de distribución efe, eso es uno menos efe de ce alfa, más "
        "gamma alfa por efe de ce alfa menos efe de ce alfa menos uno.",
        "Igualamos a alfa y despejamos gamma alfa.",
        "El resultado es: gamma alfa igual a alfa, menos uno, más efe de ce alfa, todo dividido "
        "por efe de ce alfa menos efe de ce alfa menos uno.",
    ),
    "P3B_Conclusion": S(
        "Por el teorema de Karlin y Rubin, este test fi es uniformemente más potente de nivel "
        "alfa.",
        "El valor de gamma alfa cae siempre entre cero y uno, y garantiza el nivel exacto alfa.",
        "Recapitulando: rechazamos para te grande, y aleatorizamos solo en la frontera.",
        "La aleatorización es necesaria precisamente porque la distribución de Poisson es "
        "discreta.",
        "La moraleja: con MLR, Karlin y Rubin nos dan el test óptimo casi gratis; la "
        "aleatorización es el ajuste fino del nivel. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
