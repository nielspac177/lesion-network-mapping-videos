# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 3 (c): función de potencia."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P3C_Intuicion": S(
        "En este video cerramos el problema tres: derivamos y analizamos la función de "
        "potencia del test.",
        "La pregunta del inciso es: derivar beta de lambda, igual a la esperanza de fi bajo "
        "lambda; expresarla con la función de distribución de una Poisson de media ene lambda; "
        "y probar que es estrictamente creciente, y que tiende a uno.",
        "¿Por qué importa? La función de potencia mide la capacidad de detección del test. Un "
        "buen test detecta mejor cuanto más lejos está la verdad de la hipótesis nula.",
        "La intuición: cuanto mayor es lambda, más probable es rechazar. Y para lambda enorme, "
        "rechazamos casi con certeza.",
        "Los símbolos: beta de lambda es la potencia; y efe sub lambda es la función de "
        "distribución de una Poisson de media ene lambda.",
        "La idea: usar la monotonía que da el MLR para lo creciente, y la ley de los grandes "
        "números para el límite.",
        "Empecemos.",
    ),
    "P3C_Setup": S(
        "Bajo un lambda general, el estadístico te sigue una Poisson de media ene lambda, con "
        "función de distribución efe sub lambda.",
        "La potencia es la esperanza de fi bajo lambda, que llamamos beta de lambda.",
        "Sustituyendo la regla del test, beta de lambda es uno menos efe sub lambda de ce alfa, "
        "más gamma alfa, por efe sub lambda de ce alfa, menos efe sub lambda de ce alfa menos "
        "uno.",
        "Tenemos dos propiedades por demostrar: que es creciente, y que su límite es uno.",
        "Vamos con ambas.",
    ),
    "P3C_Desarrollo": S(
        "Primero, observa que fi es una función no decreciente y no constante de te.",
        "Y ya sabemos, del inciso a, que la familia Poisson tiene MLR.",
        "El lema de monotonía bajo MLR dice que, en esas condiciones, la esperanza de fi de te "
        "es estrictamente creciente en lambda.",
        "La interpretación es clara: cuanto mayor es lambda, mayor es la probabilidad de "
        "rechazar. Justo lo que queremos.",
        "Para el límite, usamos la ley de los grandes números: te sobre ene converge en "
        "probabilidad a lambda.",
        "Por lo tanto, la probabilidad de que te supere ce alfa tiende a uno, y entonces beta "
        "de lambda tiende a uno cuando lambda crece.",
    ),
    "P3C_Conclusion": S(
        "Hemos probado las dos propiedades: beta de lambda es estrictamente creciente.",
        "Y beta de lambda tiende a uno cuando lambda tiende a infinito.",
        "Recapitulando: la monotonía vino del MLR, y el límite, de la ley de los grandes "
        "números.",
        "Esto es exactamente lo que esperamos de un buen test: detectar mejor cuanto más lejos "
        "está la verdad de la hipótesis nula.",
        "La moraleja: MLR no solo construye el test óptimo, también garantiza que su potencia se "
        "comporte bien. Hemos terminado el problema tres. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
