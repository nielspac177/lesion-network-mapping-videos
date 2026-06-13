# -*- coding: utf-8 -*-
"""Narración (español, voz em_santa @ speed 0.9) — Problema 1 (a).

Duraciones AUTO-calculadas del nº de palabras (≈0.36 s/palabra + margen).
Cada símbolo se explica explícitamente en la voz.
Regla dura: nº de play_beat()/wait_beat() == len(SCENES[clave]).
"""


def _dur(text, spw=0.36, pad=1.4, lo=2.6):
    return max(lo, round(spw * len(text.split()) + pad, 1))


def S(*texts):
    return [(t, _dur(t)) for t in texts]


SCENES = {
    "P1A_Intuicion": S(
        "Bienvenido. En este primer video vamos a reescribir la densidad de la normal "
        "inversa en su forma canónica de familia exponencial.",
        "La pregunta del inciso es esta: reescribir la densidad en forma canónica, "
        "identificando el parámetro natural eta, el estadístico suficiente te de equis, la base "
        "hache de equis, y la log partición a de eta; y verificar que la familia es regular.",
        "¿Por qué importa? Porque la forma canónica es la puerta de entrada a toda la teoría: "
        "suficiencia, completitud y eficiencia se deducen casi sin esfuerzo cuando el modelo "
        "está en esta forma.",
        "¿Qué es una familia exponencial? Es la forma normalizada de un modelo. Cuando una "
        "densidad se escribe de cierta manera estándar, casi toda la teoría útil sale gratis.",
        "Esa forma estándar es la siguiente: hache de equis, por e elevado a, eta por te de "
        "equis, menos a de eta. Vamos a explicar cada símbolo.",
        "Hache de equis es la parte que no depende del parámetro. Eta es la coordenada natural "
        "del parámetro. Te de equis es el estadístico suficiente, el resumen de los datos. Y a "
        "de eta es la constante que hace que la densidad integre uno.",
        "El premio es enorme: una vez en esta forma, el estadístico suficiente te de equis "
        "aparece solo, sin ningún cálculo adicional.",
        "Nuestro plan tiene dos pasos. Primero, abrir el cuadrado del exponente. Segundo, leer "
        "cada pieza por separado. Empecemos.",
    ),
    "P1A_Setup": S(
        "Esta es la densidad de la normal inversa. La letra equis es el dato observado, "
        "siempre positivo. Mu es el parámetro de media, y lambda es el parámetro de forma.",
        "Una aclaración que usaremos todo el tiempo: mu es conocido. El único parámetro "
        "desconocido, el que queremos estudiar, es lambda.",
        "La densidad tiene dos partes. La primera es la raíz cuadrada de lambda sobre dos pi "
        "equis al cubo. Dentro de esa raíz aparece el lambda que nos interesa.",
        "La segunda parte es el exponente: menos lambda, por equis menos mu al cuadrado, sobre "
        "dos mu cuadrado equis. También aquí aparece lambda multiplicando.",
        "Nuestra meta es separar limpiamente lo que depende de lambda de lo que depende solo "
        "de los datos, hasta llegar a la forma canónica.",
        "Tenemos todo lo que necesitamos. Vamos al desarrollo.",
    ),
    "P1A_Desarrollo": S(
        "Paso uno: abrir el cuadrado que está dentro del exponente.",
        "Tomamos equis menos mu, elevado al cuadrado, dividido entre equis. El numerador, al "
        "desarrollar el cuadrado, es equis cuadrado, menos dos mu equis, más mu cuadrado.",
        "Dividimos cada término del numerador entre equis. Queda equis, menos dos mu, más mu "
        "cuadrado sobre equis. El término menos dos mu es una simple constante.",
        "Sustituyendo, el exponente completo es menos lambda sobre dos mu cuadrado, "
        "multiplicado por equis menos mu al cuadrado, sobre equis.",
        "Ahora leemos las piezas comparando con la forma canónica. La primera pieza: el "
        "estadístico suficiente te de equis es equis menos mu al cuadrado, sobre equis. Es lo "
        "que multiplica al parámetro.",
        "La segunda pieza: la función base hache de equis recoge todo lo que no depende de "
        "lambda. Es dos pi equis al cubo, elevado a menos un medio.",
        "La tercera pieza: el parámetro natural eta es justo el factor que multiplica a te de "
        "equis. Es decir, eta es menos lambda sobre dos mu cuadrado.",
        "Falta la cuarta pieza. El factor lambda elevado a un medio que sobra se reescribe "
        "como e elevado a un medio del logaritmo de lambda.",
        "Comparando con menos a de eta en el exponente, concluimos que a de eta es menos un "
        "medio del logaritmo de lambda. Ya tenemos las cuatro piezas.",
    ),
    "P1A_Conclusion": S(
        "Para cerrar, verificamos la regularidad de la familia. Eso se decide mirando el "
        "espacio paramétrico natural, que llamamos hache caligráfica.",
        "El espacio natural es el conjunto de todos los valores que puede tomar eta cuando "
        "lambda recorre los números positivos.",
        "Como eta es menos lambda sobre dos mu cuadrado, y lambda es positivo, eta recorre "
        "todo el intervalo que va desde menos infinito hasta cero.",
        "Ese intervalo es abierto. Y contener un intervalo abierto es exactamente la condición "
        "para que la familia sea exponencial regular de rango uno.",
        "Recapitulemos las cuatro piezas. Te de equis, el estadístico suficiente. Hache de "
        "equis, la base. Eta, el parámetro natural. Y a de eta, la log partición.",
        "¿Por qué importa la regularidad? Porque es justo la hipótesis que habilita los grandes "
        "teoremas que veremos después: la completitud y la eficiencia.",
        "La moraleja: en forma canónica, la suficiencia deja de ser un cálculo y pasa a ser una "
        "simple lectura. Nos vemos en el siguiente video.",
    ),
}

if __name__ == "__main__":
    grand = 0.0
    for k, beats in SCENES.items():
        total = sum(d for _, d in beats)
        grand += total
        print(f"{k:18s} {len(beats)} beats  {total:5.1f}s")
    print(f"{'TOTAL':18s}          {grand:5.1f}s  ({grand/60:.1f} min)")
