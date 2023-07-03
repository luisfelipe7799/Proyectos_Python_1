#Escribir un programa que imprima todos los números
# primos hasta un número introducido por el usuario.

limite = int(input('>>> Dame un mumero: '))

for numero in range(2, limite + 1):
    creo_que_es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            creo_que_es_primo = False
            break

    if creo_que_es_primo:
        print(numero)
