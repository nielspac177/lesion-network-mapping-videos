# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 3 (a): MLR en Poisson."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P3A_Intuicion": S(
        "Bienvenido. En este video probamos que la familia Poisson tiene cociente de "
        "verosimilitudes monótono, que abreviamos como MLR.",
        "La pregunta del inciso es: demostrar que el cociente de verosimilitudes es no "
        "decreciente en te, la suma de los equis sub i, argumentando directamente sobre los "
        "enteros, sin suponer continuidad.",
        "¿Por qué importa? El MLR es la llave de los tests óptimos. Convierte el mejor test en "
        "algo trivial: rechazar cuando te es grande. Eso lo garantiza Karlin y Rubin.",
        "La intuición: con MLR, valores más grandes de te son evidencia monótonamente más "
        "fuerte a favor de un lambda grande.",
        "Los símbolos: te es la suma de los equis sub i. Lambda cero es el valor de referencia. "
        "Y contrastamos lambda menor o igual que lambda cero, contra lambda mayor.",
        "La idea: escribir el cociente para dos valores, lambda uno mayor que lambda dos, y ver "
        "que crece en te.",
        "Empecemos.",
    ),
    "P3A_Setup": S(
        "El modelo es Poisson de parámetro lambda. Contrastamos la hipótesis nula, lambda menor "
        "o igual que lambda cero, contra la alternativa, lambda mayor que lambda cero.",
        "La densidad conjunta es e elevado a menos ene lambda, por lambda elevado a te, sobre "
        "el producto de los factoriales de los equis sub i.",
        "El estadístico es te, igual a la suma de los equis sub i.",
        "Tomamos dos valores del parámetro, lambda uno estrictamente mayor que lambda dos.",
        "Con esto, escribamos el cociente.",
    ),
    "P3A_Desarrollo": S(
        "Formamos el cociente de las densidades en lambda uno y en lambda dos.",
        "Los productos de los factoriales son idénticos arriba y abajo, así que se cancelan.",
        "Lo que queda es e elevado a menos ene por lambda uno menos lambda dos, por el cociente "
        "lambda uno sobre lambda dos, elevado a te.",
        "Como lambda uno es mayor que lambda dos, el cociente lambda uno sobre lambda dos es "
        "mayor que uno.",
        "Y una base mayor que uno, elevada a un exponente entero te, crece cuando te crece. "
        "Este es el argumento directo sobre los enteros, sin necesidad de continuidad.",
        "Por lo tanto, el cociente es no decreciente en te. La familia tiene MLR.",
    ),
    "P3A_Conclusion": S(
        "Hemos probado que la familia Poisson tiene cociente de verosimilitudes monótono, no "
        "decreciente en te.",
        "Y lo hicimos sin suponer continuidad: el argumento fue directo sobre los enteros no "
        "negativos.",
        "La clave fue simple: una base mayor que uno da una potencia creciente en el exponente.",
        "Esto es justo lo que habilita el teorema de Karlin y Rubin, que usaremos en el "
        "siguiente video.",
        "La moraleja: MLR es una propiedad estructural que convierte la construcción del test "
        "óptimo en algo casi automático. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
