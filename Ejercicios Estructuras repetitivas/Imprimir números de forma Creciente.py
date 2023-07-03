#Escribir un programa que imprima los números
# pares entre 0 y 200 de forma creciente.

contador = 1
while contador < 200:
    if contador % 2 == 0:
        print(f"{contador} es par")
        contador = contador +1
    else:
        contador = contador +1