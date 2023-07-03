#Haz un programa para crear una matriz nula Mmxn,
# donde se le solicite al usuario su dimensión m x n, (m son las filas y n son las columnas).
# Imprime cada fila de la matriz en pantalla.
# Declaracion de Variables:
Longitud = 0
m_filas = 0
n_columnas = 0


m_filas = int(input(">>> Numero de filas (m): "))
n_columnas = int(input(">>> Numero de columnas (n): "))

M = []

for elemento in range(m_filas):
    M.append([0] * n_columnas)

# Longitud de la Matriz
Longitud = len(M)

print("\nMATRIZ M(%dx%d): %s\n" % (m_filas, n_columnas, M))

for fila in range(Longitud):
    print(M[fila])