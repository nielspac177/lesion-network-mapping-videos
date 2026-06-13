# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 2 (b): Rao-Blackwell."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P2B_Intuicion": S(
        "En este video mejoramos el estimador anterior usando el teorema de Rao y Blackwell.",
        "La pregunta del inciso es: mostrar que te ene, la suma de los logaritmos, es "
        "suficiente y completo para alfa; y aplicar Rao y Blackwell para obtener tau gorro "
        "erre be, igual a la esperanza de tau gorro cero dado te ene.",
        "¿Por qué importa? Rao y Blackwell reducen la varianza condicionando en un estadístico "
        "suficiente. Es la forma sistemática de pasar de un estimador tosco a uno fino.",
        "La intuición: condicionar en el estadístico suficiente promedia el ruido del estimador "
        "crudo dentro de cada nivel de te ene.",
        "Símbolos clave: te ene es la suma de los logaritmos de equis sub i sobre equis eme, y "
        "sigue una distribución Gamma de parámetros ene y alfa.",
        "La idea fina: por simetría, todas las esperanzas condicionales de las ye sub i son "
        "iguales, y juntas suman te ene.",
        "Empecemos.",
    ),
    "P2B_Setup": S(
        "Tomamos el logaritmo de la densidad. Da logaritmo de alfa, menos alfa por el logaritmo "
        "de equis sobre equis eme, menos logaritmo de equis.",
        "Esa forma es una familia exponencial regular, con estadístico natural el logaritmo de "
        "equis sobre equis eme.",
        "Por lo tanto, te ene, la suma de esos logaritmos, sigue una Gamma de parámetros ene y "
        "alfa.",
        "Y, como familia exponencial regular, te ene es suficiente y completo para alfa.",
        "Con un suficiente y completo en mano, aplicamos Rao y Blackwell.",
    ),
    "P2B_Desarrollo": S(
        "Rao y Blackwell nos dice: tomemos la esperanza del estimador crudo, condicionada en el "
        "suficiente. Es decir, la esperanza de ye uno dado te ene.",
        "Lo calculamos por simetría. La suma de las esperanzas condicionales de las ye sub i, "
        "dado te ene, es la esperanza de te ene dado te ene, que es te ene.",
        "Como las ye sub i son intercambiables, todas esas esperanzas son iguales. Dividiendo, "
        "cada una vale te ene sobre ene.",
        "La ruta alternativa que sugiere el enunciado: ye uno sobre te ene, dado te ene, sigue "
        "una Beta de parámetros uno y ene menos uno, cuya media es uno sobre ene.",
        "Ambas rutas coinciden: la esperanza de ye uno dado te ene es te ene sobre ene.",
        "Por lo tanto, el estimador de Rao y Blackwell es tau gorro erre be, igual a te ene "
        "sobre ene.",
    ),
    "P2B_Conclusion": S(
        "El teorema de Rao y Blackwell garantiza que este estimador tiene varianza menor o "
        "igual que la del estimador crudo.",
        "Y fíjate en lo natural del resultado: te ene sobre ene es, simplemente, el promedio de "
        "las ye sub i.",
        "El sentido común recuperado, pero ahora con una garantía de mejora.",
        "Es insesgado, y en el siguiente video probaremos que es el mejor de todos: el UMVUE, y "
        "además eficiente.",
        "La moraleja: Rao y Blackwell promedia el ruido dentro de cada nivel del estadístico "
        "suficiente. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
