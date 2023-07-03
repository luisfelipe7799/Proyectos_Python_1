#Escribir un programa en el cual se solicite al usuario un número y
# se imprima la tabla de potencias del 1 al 10 del valor introducido.

numero = int(input("Numero: "))
final = 0
contador = 1
while contador < 11:
    final = numero * contador
    print(f"{numero} x {contador} = {final}")
    contador = contador+1