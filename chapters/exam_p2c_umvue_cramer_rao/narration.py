# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 2 (c): UMVUE, varianza, Cramér-Rao."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P2C_Intuicion": S(
        "En este video cerramos el problema dos: probamos que el estimador es el mejor "
        "insesgado, y que además es eficiente.",
        "La pregunta del inciso es: verificar que tau gorro erre be es insesgado, concluir por "
        "Lehmann y Scheffé que es el UMVUE, calcular su varianza, y compararla con la cota de "
        "Cramér y Rao.",
        "¿Por qué importa? Aquí encajan tres ideas. Rao y Blackwell construyen el estimador; "
        "Lehmann y Scheffé certifican que es el mejor; y Cramér y Rao miden cuán bueno es.",
        "Recordemos: UMVUE significa el estimador insesgado de mínima varianza. Y eficiente "
        "significa que alcanza la cota teórica mínima posible.",
        "Los símbolos nuevos: tau prima de alfa, la derivada del objetivo; e i uno de alfa, la "
        "información de Fisher de una observación.",
        "La idea final es comparar la varianza del estimador con esa cota inferior.",
        "Empecemos.",
    ),
    "P2C_Setup": S(
        "Primero, tau gorro erre be es insesgado: su esperanza es uno sobre alfa, que es tau.",
        "Es una función de un estadístico suficiente y completo, y es insesgado. Por el teorema "
        "de Lehmann y Scheffé, es el UMVUE.",
        "Ahora su varianza. Como tau gorro erre be es te ene sobre ene, la varianza es la "
        "varianza de te ene, dividida por ene al cuadrado.",
        "La Gamma de parámetros ene y alfa tiene varianza ene sobre alfa al cuadrado. Al "
        "dividir por ene al cuadrado, queda alfa a la menos dos, sobre ene.",
        "Tenemos la varianza. La comparamos con la cota de Cramér y Rao.",
    ),
    "P2C_Desarrollo": S(
        "La cota de Cramér y Rao es: tau prima de alfa al cuadrado, sobre ene por la "
        "información de Fisher de una observación.",
        "Calculamos las piezas. Como tau es uno sobre alfa, su derivada tau prima es menos alfa "
        "a la menos dos.",
        "La información de Fisher: la segunda derivada del logaritmo de la densidad da menos "
        "alfa a la menos dos, así que i uno de alfa es alfa a la menos dos.",
        "Sustituimos. Arriba, menos alfa a la menos dos, al cuadrado, es alfa a la menos cuatro. "
        "Abajo, ene por alfa a la menos dos.",
        "Simplificando, la cota es alfa a la menos dos, sobre ene.",
        "Y eso es, exactamente, la varianza de nuestro estimador.",
    ),
    "P2C_Conclusion": S(
        "La varianza del UMVUE coincide, exactamente, con la cota de Cramér y Rao.",
        "Por lo tanto, el estimador es eficiente para todo alfa positivo.",
        "Recapitulando las tres ideas: Rao y Blackwell construyen, Lehmann y Scheffé certifican, "
        "y Cramér y Rao miden.",
        "Alcanzar la cota es lo máximo a lo que un estimador insesgado puede aspirar.",
        "La moraleja: cuando la varianza iguala la cota de Cramér y Rao, no hay insesgado mejor. "
        "Hemos terminado el problema dos. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
