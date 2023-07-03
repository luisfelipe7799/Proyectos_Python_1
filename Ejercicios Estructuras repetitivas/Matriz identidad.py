M = []
longitud = 0
dimension = 0

dimension = int(input(">>> Dimension de la matriz de tamaño n x n: "))

for elemento in range(dimension):
    M.append([0] * dimension)

for fila in range(dimension):
    for columna in range(dimension):
        # Si el numero de fila y columna es igual
        if fila == columna:
            # Guarda el número 1 en la posición
            M[fila][columna] = 1

print("\nMatriz M(%dx%d): %s\n" % (dimension, dimension, M))

longitud = len(M)

for valor in range(longitud):
    print(M[valor])