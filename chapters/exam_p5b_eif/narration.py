# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 5 (b): derivación de la EIF."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P5B_Intuicion": S(
        "En este video derivamos la fórmula explícita de la función de influencia eficiente "
        "para beta, bajo heteroscedasticidad de forma desconocida.",
        "La pregunta del inciso es: escribir la ecuación de momento eficiente, ponderada por "
        "uno sobre sigma cuadrado; mostrar que equis tilde épsilon, sobre sigma cuadrado, es "
        "ortogonal a cualquier función de zeta; y concluir la fórmula de la E I F.",
        "¿Por qué importa? La E I F da el estimador asintóticamente eficiente y su varianza. Los "
        "pesos uno sobre sigma cuadrado corrigen, justamente, la heteroscedasticidad.",
        "La intuición: residualizar equis contra zeta elimina la confusión con g. Y ponderar por "
        "uno sobre sigma cuadrado da el peso óptimo a cada observación.",
        "Los símbolos: equis tilde es equis menos su esperanza dado zeta, el residual. Sigma "
        "cuadrado de zeta es la varianza condicional. E i es la información eficiente.",
        "La idea: score de trabajo, residualizar, verificar ortogonalidad, y leer la E I F.",
        "Empecemos.",
    ),
    "P5B_Setup": S(
        "Bajo un modelo de trabajo gaussiano, el score de beta es equis épsilon, sobre sigma "
        "cuadrado de zeta.",
        "El problema es que equis está confundida con g de zeta, a través de zeta.",
        "La solución es residualizar: definimos equis tilde igual a equis menos su esperanza "
        "dado zeta.",
        "Con eso, el score eficiente es equis tilde épsilon, sobre sigma cuadrado de zeta.",
        "Falta verificar que este score es ortogonal al nuisance.",
    ),
    "P5B_Desarrollo": S(
        "Verificamos la ortogonalidad del score eficiente con cualquier perturbación a de zeta, "
        "épsilon, sobre sigma cuadrado.",
        "El producto esperado es la esperanza de a de zeta, por equis tilde, por épsilon al "
        "cuadrado, sobre sigma a la cuarta.",
        "Usando que la esperanza de épsilon al cuadrado dado equis y zeta es sigma cuadrado, "
        "esto se reduce a la esperanza de a de zeta, sobre sigma cuadrado, por la esperanza de "
        "equis tilde dado zeta.",
        "Y la esperanza de equis tilde dado zeta es cero, por la propia definición del residual. "
        "Por lo tanto, el producto es cero. Hay ortogonalidad.",
        "La información eficiente es la esperanza de equis tilde por equis tilde traspuesta, "
        "sobre sigma cuadrado. Y la E I F es su inversa, por equis tilde épsilon sobre sigma "
        "cuadrado.",
        "En el caso homoscedástico, con sigma cuadrado constante, los pesos desaparecen y la E I "
        "F se reduce a la del estimador de Robinson, de mil novecientos ochenta y ocho.",
    ),
    "P5B_Conclusion": S(
        "La función de influencia eficiente es la inversa de la esperanza de equis tilde equis "
        "tilde traspuesta sobre sigma cuadrado, por equis tilde épsilon sobre sigma cuadrado.",
        "Los pesos uno sobre sigma cuadrado son, exactamente, la corrección por "
        "heteroscedasticidad.",
        "En el caso homoscedástico, se reduce a la fórmula sin pesos de Robinson.",
        "Recapitulando: residualizar contra zeta, y ponderar por la varianza inversa, da el "
        "score eficiente.",
        "La moraleja: la E I F combina dos ideas. Residualizar mata el sesgo por el nuisance; "
        "ponderar por la varianza inversa alcanza la eficiencia. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
