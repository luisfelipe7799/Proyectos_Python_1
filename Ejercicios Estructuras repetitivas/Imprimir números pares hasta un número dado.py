#Escribir un programa que imprima los números pares de
# forma creciente hasta un número introducido por el usuario.

contador = 1
limite = int(input("Ingrese limite: "))

while contador < limite:
    if contador % 2 == 0:
        print(f"{contador} es par")
        contador = contador +1
    else:
        contador = contador +1