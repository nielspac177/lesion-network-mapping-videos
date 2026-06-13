# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 4 (c): UMP en Laplace."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P4C_Intuicion": S(
        "En este video construimos el test uniformemente más potente en el modelo de Laplace, "
        "para la escala be.",
        "La pregunta del inciso es: probar que Laplace tiene MLR no decreciente en te, la suma "
        "de los valores absolutos; por Karlin y Rubin, rechazar para te grande; mostrar que dos "
        "te sobre be sigue una chi cuadrado con dos ene grados de libertad; y contrastar con el "
        "caso Poisson.",
        "¿Por qué importa? Es el mismo esquema MLR seguido de Karlin y Rubin. Pero aquí la "
        "distribución nula es continua, así que no hace falta aleatorizar.",
        "La intuición: be es la escala. Un te grande indica mucha dispersión, que es evidencia "
        "de un be grande.",
        "Los símbolos: te es la suma de los desvíos absolutos respecto de mu; be es la escala; y "
        "chi cuadrado con dos ene grados de libertad.",
        "La idea: cociente, MLR, distribución de te, y región crítica.",
        "Empecemos.",
    ),
    "P4C_Setup": S(
        "El modelo es Laplace de centro mu, conocido, y escala be. Contrastamos be menor o igual "
        "que be cero, contra be mayor que be cero.",
        "El estadístico es te, igual a la suma de los valores absolutos de equis sub i menos mu.",
        "La densidad conjunta es dos be, elevado a menos ene, por e elevado a menos te sobre be.",
        "Tomamos dos valores de la escala, be uno estrictamente mayor que be dos.",
        "Escribamos el cociente.",
    ),
    "P4C_Desarrollo": S(
        "El cociente de las densidades en be uno y be dos es be dos sobre be uno, elevado a ene, "
        "por e elevado a te, por uno sobre be dos menos uno sobre be uno.",
        "Como be uno es mayor que be dos, uno sobre be dos menos uno sobre be uno es positivo. "
        "Por lo tanto el cociente es creciente en te. Hay MLR.",
        "Por Karlin y Rubin, el test UMP rechaza para valores grandes de te.",
        "Ahora la distribución de te. Cada valor absoluto, equis sub i menos mu, es exponencial "
        "de media be; por eso dos te sobre be sigue una chi cuadrado con dos ene grados de "
        "libertad.",
        "Así, la región crítica de nivel alfa es: te mayor que be cero sobre dos, por el cuantil "
        "superior alfa de la chi cuadrado con dos ene grados de libertad.",
        "Y un detalle importante: la ley nula de te es continua, así que no se requiere "
        "aleatorización.",
    ),
    "P4C_Conclusion": S(
        "Laplace tiene MLR, y el test UMP rechaza para te grande.",
        "La región crítica se expresa con un cuantil de la chi cuadrado con dos ene grados de "
        "libertad.",
        "El contraste con Poisson es revelador: allí, por ser discreto, hacía falta aleatorizar. "
        "Aquí, por ser continuo, no.",
        "Recapitulando: cociente, MLR, distribución chi cuadrado, y región crítica.",
        "La moraleja: la aparición o no de aleatorización es puro reflejo de discreto contra "
        "continuo. Hemos terminado el problema cuatro. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
