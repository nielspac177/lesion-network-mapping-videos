# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 4 (a): pivote binomial e IC exacto."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P4A_Intuicion": S(
        "Bienvenido. En este problema tenemos dos muestras Poisson independientes, y queremos "
        "un intervalo de confianza para tau, igual a lambda uno sobre lambda dos.",
        "La pregunta del inciso es: mostrar que ese e equis, condicionado a que ese equis más "
        "ese ye sea ene, es Binomial de parámetros ene y pe; y usar esa binomial como pivote "
        "para construir un intervalo exacto de nivel uno menos alfa para tau, vía cuantiles "
        "Beta.",
        "¿Por qué importa? Tenemos dos tasas desconocidas, pero solo nos importa su cociente. "
        "Condicionar en el total elimina el nivel global molesto y deja una binomial limpia.",
        "La intuición: dado el total, el reparto entre las dos muestras es una binomial cuya pe "
        "depende únicamente de tau.",
        "Los símbolos: ese equis y ese ye son las sumas de cada muestra; ene es el total; tau es "
        "el cociente de las tasas; y pe es la probabilidad de la binomial.",
        "La idea: condicionar, reconocer una binomial, e invertir el pivote usando cuantiles "
        "Beta.",
        "Empecemos.",
    ),
    "P4A_Setup": S(
        "Las sumas son Poisson: ese equis sigue una Poisson de media eme lambda uno; ese ye "
        "sigue una Poisson de media ka lambda dos.",
        "Por independencia, su suma, ese equis más ese ye, sigue una Poisson de media eme "
        "lambda uno más ka lambda dos.",
        "Nuestro objetivo es tau, igual a lambda uno sobre lambda dos.",
        "La estrategia es condicionar ese equis en el total observado, ene.",
        "Veámoslo.",
    ),
    "P4A_Desarrollo": S(
        "La probabilidad condicional de que ese equis valga ese, dado el total ene, es la "
        "probabilidad de ese equis igual a ese, por la de ese ye igual a ene menos ese, sobre "
        "la del total.",
        "Al sustituir las masas de Poisson y simplificar, las exponenciales y los factoriales "
        "se reorganizan, exactamente, en una binomial.",
        "El resultado es ene sobre ese, por pe a la ese, por uno menos pe a la ene menos ese, "
        "con pe igual a eme tau sobre eme tau más ka.",
        "Esa pe es biyectiva y creciente en tau. Su inversa es tau igual a ka pe, sobre eme por "
        "uno menos pe.",
        "Para la binomial, el intervalo exacto de Clopper y Pearson para pe usa cuantiles Beta: "
        "pe ele y pe u, con parámetros que dependen de ese equis y ene.",
        "Y como tau es función creciente de pe, el intervalo para tau es, simplemente, la imagen "
        "de pe ele y pe u por esa transformación.",
    ),
    "P4A_Conclusion": S(
        "Condicionar en el total convirtió un problema de dos parámetros en una simple "
        "binomial.",
        "Y los parámetros de esa binomial dependen únicamente de tau, nuestro objetivo.",
        "Invertimos el pivote binomial, con cuantiles Beta, para obtener el intervalo exacto.",
        "Recapitulando: pivote condicional, intervalo de Clopper y Pearson, y transformación "
        "monótona a tau.",
        "La moraleja: condicionar en un total inteligente puede eliminar parámetros molestos y "
        "dejar la inferencia exacta y limpia. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
