"""Este código crea una tupla llamada multiplos_de_3 que contiene los múltiplos de 3 desde 99 hasta 78 en sentido decreciente.
La función range(99, 77, -3) genera números en el rango de 99 a 78 (no inclusive) con un paso de -3,
por lo cual que se incluyen solo los múltiplos de 3 en ese rango."""

multiplos_de_3 = tuple(x for x in range(99, 77, -3))
print(multiplos_de_3)