# Escribir un programa en el cual se solicite al usuario un número
# y se imprima la tabla de multiplicar del 1 al 10 del valor introducido.

numero = int(input("Ingrese numero para ver su table de multiplicar del 1 al 10: "))

contador = 1

while contador < 11:
    mult = numero * contador
    print(f"{contador} x {numero} = {mult}")
    contador = contador + 1