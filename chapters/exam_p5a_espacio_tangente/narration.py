# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 5 (a): espacio tangente y Riesz."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P5A_Intuicion": S(
        "Bienvenido al problema cinco, el más avanzado: inferencia semiparamétrica en un modelo "
        "parcialmente lineal con heteroscedasticidad.",
        "La pregunta de este inciso es: definir el espacio tangente nuisance, que llamamos "
        "lambda mayúscula, dentro del espacio ele dos; especificar su norma; y enunciar el "
        "teorema de representación de Riesz para la función de influencia eficiente, la E I F.",
        "¿Por qué importa? Esto es el puente entre la estadística clásica y el machine learning "
        "moderno. Nos permitirá estimar beta bien, aunque las partes nuisance se estimen con "
        "machine learning imperfecto.",
        "La intuición es geométrica. Las direcciones en que podemos perturbar el nuisance forman "
        "un subespacio lambda. Estimar beta sin contaminarse equivale a proyectar fuera de "
        "lambda.",
        "Símbolos, primera parte. Ye es la respuesta. Equis son las covariables de interés. Zeta "
        "son las covariables del nuisance. Beta es el parámetro finito que queremos.",
        "Símbolos, segunda parte. G es la función nuisance. Sigma cuadrado de zeta es la "
        "varianza condicional. Épsilon es el error. O es la observación, ye, equis, zeta. Y "
        "equis tilde es equis menos su esperanza dado zeta.",
        "La idea: definir el producto interno de ele dos, construir el espacio tangente, y "
        "aplicar Riesz.",
        "Empecemos.",
    ),
    "P5A_Setup": S(
        "El modelo es: ye igual a equis traspuesta beta, más g de zeta, más épsilon. El error "
        "tiene media condicional cero, y varianza condicional sigma cuadrado de zeta.",
        "Trabajamos en el espacio ele dos de pe, con el producto interno: efe con hache es la "
        "esperanza del producto efe de o, por hache de o.",
        "La norma asociada es la raíz de la esperanza del cuadrado. Es el lenguaje natural para "
        "hablar de proyecciones.",
        "Beta, de dimensión finita, es el interés. G y sigma cuadrado son nuisances de dimensión "
        "infinita.",
        "Con este escenario, definamos el espacio tangente.",
    ),
    "P5A_Desarrollo": S(
        "El espacio tangente nuisance lambda está generado por las perturbaciones de camino de "
        "la log verosimilitud, al variar g y sigma cuadrado.",
        "Por ejemplo, perturbar g en la dirección a de zeta produce el score a de zeta, por "
        "épsilon, sobre sigma cuadrado de zeta.",
        "El espacio lambda es la clausura, en ele dos, de todos esos scores nuisance.",
        "El teorema de representación de Riesz dice: existe una única función, la E I F fi "
        "estrella, tal que la derivada de camino del funcional objetivo beta es el producto "
        "interno de fi estrella con cada dirección ese del tangente.",
        "Y, crucialmente, fi estrella vive en lambda perpendicular, el complemento ortogonal del "
        "nuisance.",
        "Por eso fi estrella es inmune a los errores de primer orden en g y en sigma cuadrado.",
    ),
    "P5A_Conclusion": S(
        "Hemos definido el espacio tangente lambda y la norma del espacio ele dos.",
        "Riesz nos da la función de influencia eficiente fi estrella como el representante de la "
        "derivada del objetivo.",
        "Y lo esencial: fi estrella es ortogonal al nuisance; está en lambda perpendicular.",
        "Esa ortogonalidad es la fuente de la robustez, y en el siguiente video la "
        "aprovecharemos para derivar la fórmula explícita de la E I F.",
        "La moraleja: en modelos semiparamétricos, pensar geométricamente, con proyecciones en "
        "ele dos, convierte un problema infinito-dimensional en algo manejable. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
