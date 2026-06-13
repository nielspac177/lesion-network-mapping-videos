# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 4 (b): nuisance y condicionalidad de Cox."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P4B_Intuicion": S(
        "En este video identificamos el parámetro de perturbación, y entendemos por qué "
        "condicionar en el total lo elimina.",
        "La pregunta del inciso es: identificar el nuisance; reparametrizar lambda uno y lambda "
        "dos como tau y psi; argumentar que ese equis y ese ye son suficientes y completos, y "
        "que condicionar en el total elimina psi; y conectar con la condicionalidad de Cox.",
        "¿Por qué importa? Un nuisance es un parámetro que no nos interesa, pero que ensucia la "
        "inferencia. Saber eliminarlo es una habilidad central en estadística.",
        "La intuición, debida a Cox: la inferencia debe condicionarse en el tamaño del "
        "experimento que realmente ocurrió, que aquí es el total ene. Y ahí psi desaparece.",
        "Los símbolos: tau es el parámetro de interés; psi es la perturbación, proporcional a la "
        "media del total.",
        "La idea: reparametrizar, condicionar, e invocar el principio de Cox.",
        "Empecemos.",
    ),
    "P4B_Setup": S(
        "Reparametrizamos. En lugar de lambda uno y lambda dos, usamos tau y psi, donde psi es "
        "eme lambda uno más ka lambda dos.",
        "Tau es el parámetro de interés. Psi es la perturbación, proporcional a la media del "
        "total.",
        "El par ese equis, ese ye es suficiente y completo para lambda uno y lambda dos, por ser "
        "una familia exponencial bivariada regular.",
        "La pregunta clave es: ¿qué ocurre al condicionar en el total?",
        "Veámoslo.",
    ),
    "P4B_Desarrollo": S(
        "Al condicionar en ese equis más ese ye igual a ene, la ley de ese equis es una "
        "Binomial de parámetros ene y pe de tau.",
        "Y esa pe de tau, igual a eme tau sobre eme tau más ka, depende únicamente de tau, no de "
        "psi.",
        "Por lo tanto, el condicionamiento elimina psi de la inferencia sobre tau.",
        "Además, el total, ene igual a ese equis más ese ye, sigue una Poisson de media psi, y "
        "es ese-ancilar para tau: su distribución no depende de tau.",
        "Aquí entra el principio de condicionalidad de Cox, de mil novecientos cincuenta y "
        "ocho: basar la inferencia sobre tau en el experimento condicional, dado el total ene.",
        "El resultado es una inferencia sobre tau completamente libre de la perturbación psi.",
    ),
    "P4B_Conclusion": S(
        "Identificamos psi, igual a eme lambda uno más ka lambda dos, como el parámetro de "
        "perturbación.",
        "Y vimos que condicionar en el total lo elimina, de forma exacta.",
        "El principio de Cox lo justifica: basamos la inferencia en el experimento que "
        "efectivamente observamos.",
        "Recapitulando: reparametrizar, usar la suficiencia y completitud, condicionar, e "
        "invocar a Cox.",
        "La moraleja: cuando un estadístico ancilar fija el tamaño del experimento, condicionar "
        "en él limpia la perturbación. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
