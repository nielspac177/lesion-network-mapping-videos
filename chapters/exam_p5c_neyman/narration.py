# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 5 (c): ortogonalidad de Neyman y DML."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P5C_Intuicion": S(
        "En este último video verificamos la ortogonalidad de Neyman, y la conectamos con el "
        "double machine learning.",
        "La pregunta del inciso es: calcular las derivadas de Gâteaux del funcional de momento "
        "respecto del nuisance, evaluadas en el valor verdadero, y mostrar que se anulan; y "
        "explicar la consecuencia sobre el sesgo y la normalidad asintótica de beta.",
        "¿Por qué importa? La ortogonalidad de Neyman es la propiedad mágica que hace funcionar "
        "el double machine learning. Permite usar machine learning lento y sesgado para el "
        "nuisance, y aún así obtener inferencia válida para beta.",
        "La intuición: si la ecuación de momento es insensible, a primer orden, a los errores "
        "del nuisance, entonces el sesgo que queda es solo de segundo orden.",
        "Los símbolos: psi es el funcional de momento; eta agrupa los nuisances eme, g y sigma "
        "cuadrado; eme grande es la esperanza de psi; y usamos derivadas de Gâteaux.",
        "La idea: perturbar cada componente del nuisance, y verificar que la derivada es cero.",
        "La consecuencia: el sesgo del plug-in es de orden la norma al cuadrado, en vez de la "
        "norma.",
        "Empecemos.",
    ),
    "P5C_Setup": S(
        "El funcional de momento es psi: equis menos eme de zeta, por ye menos equis traspuesta "
        "beta menos g de zeta, todo sobre sigma cuadrado de zeta.",
        "Los nuisances son eta igual a eme, g y sigma cuadrado, donde eme de zeta es la "
        "esperanza de equis dado zeta.",
        "Definimos eme grande de beta y eta como la esperanza de psi.",
        "En el valor verdadero eta cero, la combinación ye menos equis traspuesta beta cero "
        "menos g cero es, exactamente, épsilon.",
        "Vamos a calcular las derivadas de Gâteaux respecto del nuisance.",
    ),
    "P5C_Desarrollo": S(
        "Primero, perturbamos g. La derivada es menos la esperanza de delta g sobre sigma "
        "cuadrado, por la esperanza de equis tilde dado zeta.",
        "Segundo, perturbamos eme. La derivada es menos la esperanza de delta eme sobre sigma "
        "cuadrado, por la esperanza de épsilon dado zeta.",
        "Tercero, perturbamos sigma cuadrado. La derivada es menos la esperanza de delta sigma "
        "cuadrado sobre sigma a la cuarta, por equis tilde, por la esperanza de épsilon dado "
        "equis y zeta.",
        "Las tres se anulan, usando dos hechos: la esperanza de equis tilde dado zeta es cero, "
        "y la esperanza de épsilon dado equis y zeta es cero.",
        "Por lo tanto, psi es Neyman ortogonal, y el sesgo del estimador plug-in es de orden la "
        "norma de eta gorro menos eta cero, al cuadrado.",
        "Si las tasas de g gorro y sigma cuadrado gorro son o pequeña de ene a la menos un "
        "cuarto, el sesgo es o pequeña de ene a la menos un medio. Entonces raíz de ene, por "
        "beta gorro menos beta cero, converge a una normal de varianza igual a la de fi "
        "estrella.",
    ),
    "P5C_Conclusion": S(
        "Las tres derivadas de Gâteaux se anulan: el funcional de momento es Neyman ortogonal.",
        "Como consecuencia, el sesgo del plug-in es de segundo orden, no de primer orden.",
        "Con tasas o pequeña de ene a la menos un cuarto para los nuisances, beta gorro es raíz "
        "de ene consistente y asintóticamente normal.",
        "El cross fitting de Chernozhukov y colaboradores, de dos mil dieciocho, elimina además "
        "el sesgo por sobreajuste, permitiendo machine learning flexible.",
        "La moraleja, y el cierre de todo el examen: la ortogonalidad de Neyman es el puente "
        "entre la estadística clásica y el machine learning moderno. Nos deja usar estimadores "
        "imperfectos del nuisance, y aún así hacer inferencia válida y eficiente sobre beta. "
        "Felicidades por llegar hasta aquí.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
