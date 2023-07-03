#Crea una Matriz 4x4 que almacene los valores de un
# teclado matricial. Imprime la matriz, la cuarta fila y el asterisco (*) en pantalla.


Matriz = []
Fila = 3
Columna = 0


Matriz = [['1', '2', '3', 'A'],
          ['4', '5', '6', 'B'],
          ['7', '8', '9', 'C'],
          ['*', '0', '#', 'D']]


print(f">>> Matriz  : {Matriz}" )
print(f">>> FILA A   : {Matriz[Fila]}" )
print(f">>> DATO A   :{Matriz[Fila][Columna]}")
