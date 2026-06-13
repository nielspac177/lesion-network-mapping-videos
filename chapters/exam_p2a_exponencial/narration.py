# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 2 (a): Y=log(X/xm)~Exp(α)."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P2A_Intuicion": S(
        "Bienvenido. Este problema trata de estimar tau, igual a uno sobre alfa, en una "
        "distribución de Pareto.",
        "La pregunta del inciso es: mostrar que ye, igual al logaritmo de equis sobre equis "
        "eme, sigue una exponencial de parámetro alfa; y usarlo para proponer un estimador "
        "insesgado de tau basado en un solo dato, calculando su varianza.",
        "¿Por qué importa? Este estimador simple será el punto de partida. Rao y Blackwell lo "
        "mejorarán después. Casi nunca empezamos con el óptimo; empezamos con algo insesgado.",
        "La idea clave: la Pareto es una exponencial disfrazada. Tiene una cola de potencia "
        "que, al tomar logaritmos, se convierte en una cola exponencial limpia.",
        "Recordemos los símbolos. Equis es el dato. Equis eme es la escala, conocida. Alfa es "
        "el índice de forma, desconocido. Y tau, nuestro objetivo, es uno sobre alfa.",
        "El plan: transformar la variable, reconocer una exponencial, y leer su media.",
        "Empecemos.",
    ),
    "P2A_Setup": S(
        "La densidad de la Pareto es alfa por equis eme elevado a alfa, sobre equis elevado a "
        "alfa más uno, válida para equis mayor o igual que equis eme.",
        "Su cola es muy simple: la probabilidad de que equis supere un valor te es equis eme "
        "sobre te, elevado a alfa.",
        "Definimos la transformación: ye igual al logaritmo de equis sobre equis eme. Como "
        "equis es al menos equis eme, ye es siempre no negativo.",
        "Y recordemos: nuestro objetivo tau es uno sobre alfa, la inversa del índice de forma.",
        "Con esto, vamos a hallar la distribución de ye.",
    ),
    "P2A_Desarrollo": S(
        "Calculamos la función de distribución de ye. Para ye no negativo, miramos la "
        "probabilidad de que ye sea menor o igual que un valor ye.",
        "Como ye es el logaritmo de equis sobre equis eme, eso equivale a que equis sea menor o "
        "igual que equis eme por e elevado a ye.",
        "Usamos la cola de la Pareto. El resultado es uno menos e elevado a menos alfa ye.",
        "Pero esa es, exactamente, la función de distribución de una exponencial. Por lo tanto, "
        "ye sigue una exponencial de parámetro alfa.",
        "La media de una exponencial de parámetro alfa es uno sobre alfa, que es justo tau. Y "
        "su varianza es uno sobre alfa al cuadrado.",
        "Por eso tomamos como estimador a tau gorro cero, igual a ye uno; es decir, el "
        "logaritmo de equis uno sobre equis eme.",
    ),
    "P2A_Conclusion": S(
        "El estimador tau gorro cero, basado en un solo dato, es insesgado para tau.",
        "Y su varianza es alfa elevado a menos dos.",
        "Recapitulando: una simple transformación logarítmica convirtió la Pareto en una "
        "exponencial.",
        "Y la media de esa exponencial resultó ser, exactamente, nuestro parámetro de interés.",
        "La moraleja: un estimador insesgado simple es un excelente punto de partida. En el "
        "próximo video lo volveremos óptimo con Rao y Blackwell. Nos vemos.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
