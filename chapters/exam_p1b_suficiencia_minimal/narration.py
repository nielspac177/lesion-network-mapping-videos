# -*- coding: utf-8 -*-
"""Narración (es, em_santa @0.9) — Problema 1 (b): suficiencia minimal."""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P1B_Intuicion": S(
        "En este video demostramos que te de equis es suficiente minimal, usando el criterio "
        "de Lehmann y Scheffé.",
        "La pregunta del inciso es: probar que el cociente de verosimilitudes de dos muestras "
        "es constante en lambda si y solo si te de equis y te de ye coinciden; y concluir que "
        "te es suficiente minimal.",
        "¿Por qué importa? Porque el suficiente minimal es la compresión óptima de los datos: "
        "comprimir más perdería información sobre lambda; comprimir menos sería redundante.",
        "Ya sabemos que es suficiente: te de equis contiene toda la información sobre lambda. "
        "Minimal significa que es el resumen más comprimido posible.",
        "El criterio es elegante. Dos muestras, equis e ye, deben ser indistinguibles para la "
        "inferencia exactamente cuando te de equis vale lo mismo en ambas.",
        "Y aquí indistinguibles quiere decir algo preciso: que el cociente de sus "
        "verosimilitudes no depende de lambda.",
        "La estrategia es escribir ese cociente y ver que lambda desaparece si y solo si las "
        "dos te coinciden.",
        "Vamos a verlo paso a paso.",
    ),
    "P1B_Setup": S(
        "Por independencia, la densidad conjunta de la muestra es el producto de las densidades "
        "individuales.",
        "Agrupando términos, queda lambda elevado a ene medios, por el producto de las "
        "bases, por e elevado a menos lambda sobre dos mu cuadrado, por te de equis.",
        "Aquí te de equis es la suma, sobre i, de equis sub i menos mu, al cuadrado, sobre "
        "equis sub i. Ese es nuestro estadístico.",
        "Fíjate bien: lambda solo aparece en dos lugares, el factor lambda a la ene medios, y "
        "el exponente. Esto será clave.",
        "Con esta forma, el cociente entre dos muestras saldrá muy limpio.",
    ),
    "P1B_Desarrollo": S(
        "Tomamos dos muestras, equis e ye, y dividimos sus densidades conjuntas.",
        "Los factores lambda a la ene medios son idénticos arriba y abajo, así que se cancelan.",
        "El cociente de los productos de las bases no depende de lambda. Lo llamamos ce de "
        "equis, ye: una constante respecto del parámetro.",
        "Lo único que queda con lambda es e elevado a menos lambda sobre dos mu cuadrado, por "
        "te de equis menos te de ye.",
        "Primera implicación. Si te de equis es igual a te de ye, el exponente es cero, y el "
        "cociente vale ce, que es constante en lambda.",
        "Segunda implicación. Si el cociente es constante en lambda, entonces e elevado a ce "
        "por lambda es constante, donde ce es la diferencia de las te.",
        "Pero la exponencial es inyectiva: solo es constante si ce es cero. Por lo tanto te de "
        "equis es igual a te de ye.",
    ),
    "P1B_Conclusion": S(
        "Hemos probado la equivalencia en las dos direcciones, ida y vuelta.",
        "El cociente de verosimilitudes es constante en lambda si y solo si te de equis y te de "
        "ye coinciden.",
        "Eso es precisamente el criterio de Lehmann y Scheffé para suficiencia minimal.",
        "Por lo tanto, te de equis, la suma de equis sub i menos mu al cuadrado sobre equis sub "
        "i, es suficiente minimal.",
        "La moraleja: en familias exponenciales, la inyectividad de la exponencial convierte "
        "constante en el parámetro, en te iguales. Nos vemos en el siguiente video.",
    ),
}

if __name__ == "__main__":
    for k, b in SCENES.items():
        print(f"{k:18s} {len(b)} beats  {sum(d for _, d in b):5.1f}s")
