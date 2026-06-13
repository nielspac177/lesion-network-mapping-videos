# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 1 (c): completitud."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P1C_Intuicion": S(
        "En este video probamos que te de equis es completo. Es la pieza que faltaba para "
        "construir estimadores óptimos.",
        "La pregunta del inciso es: demostrar que te de equis es completo para lambda, "
        "identificando su distribución Gamma y usando la unicidad de la transformada de Laplace.",
        "¿Por qué importa? Porque suficiente más completo es la receta de Lehmann y Scheffé "
        "para construir el mejor estimador insesgado posible, el UMVUE.",
        "Completitud significa que te de equis no tiene grados de libertad sobrantes; no esconde "
        "información redundante.",
        "Formalmente: la única función fi de te cuya esperanza es cero para todo lambda, es la "
        "función cero.",
        "La estrategia tiene tres pasos. El primero: hallar la distribución de te.",
        "El segundo: ver que esa distribución es, otra vez, una familia exponencial. Y el "
        "tercero: usar la unicidad de la transformada de Laplace.",
        "Empecemos por la distribución de te.",
    ),
    "P1C_Setup": S(
        "Una propiedad conocida de la normal inversa: lambda por equis sub i menos mu al "
        "cuadrado, sobre mu cuadrado equis sub i, sigue una chi cuadrado con un grado de "
        "libertad.",
        "Además, estas ene variables son independientes entre sí.",
        "Al sumarlas, obtenemos lambda sobre mu cuadrado, por te, que sigue una chi cuadrado "
        "con ene grados de libertad.",
        "Despejando, te sigue una distribución Gamma, con forma ene medios y escala dos mu "
        "cuadrado sobre lambda.",
        "Ya tenemos la distribución de te. Sigamos.",
    ),
    "P1C_Desarrollo": S(
        "La densidad de te es proporcional a te elevado a ene medios menos uno, por e elevado a "
        "menos lambda te sobre dos mu cuadrado.",
        "Esto es una familia exponencial en el parámetro natural eta, igual a menos lambda sobre "
        "dos mu cuadrado, y es regular.",
        "Ahora supongamos que la esperanza de fi de te es cero, para todo lambda positivo.",
        "Hacemos el cambio de variable: ese igual a lambda sobre dos mu cuadrado, que también "
        "recorre los positivos.",
        "La condición se transforma en: la integral, de cero a infinito, de fi de te, por te a "
        "la ene medios menos uno, por e a la menos ese te, igual a cero, para todo ese.",
        "Y ese lado izquierdo es, exactamente, la transformada de Laplace de fi de te, por te a "
        "la ene medios menos uno.",
    ),
    "P1C_Conclusion": S(
        "Tenemos una transformada de Laplace que vale cero en todo un intervalo de ese.",
        "Por el teorema de unicidad de la transformada de Laplace, la función original debe ser "
        "cero en casi todo punto.",
        "Es decir, fi de te por te a la ene medios menos uno es cero. Y como ese factor es "
        "estrictamente positivo, concluimos que fi es idénticamente cero.",
        "Por lo tanto, te de equis es un estadístico completo para lambda.",
        "La moraleja: distribución, luego exponencial, luego unicidad de Laplace. Memoriza ese "
        "esqueleto, porque se repite siempre. Nos vemos en el siguiente video.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
