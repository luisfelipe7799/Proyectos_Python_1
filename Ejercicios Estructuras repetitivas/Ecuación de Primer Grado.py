print("Ecuacion del tipo ax + b =0")
a = 0
b = 0
resultado = 0
a = int(input("Ingrese a :"))
b = int(input("Ingrese b :"))

if a != 0:
    resultado = (-b/a)
    print(f"El resultado de {a}x + {b} = 0 es que x = {resultado}")
else :
    if a == 0:
        if b != 0:
            print("La ecuacion no tiene solucion")
        else:
            print("La ecuacion tiene infinitas soluciones")
    else:
        print("La ecuacion tiene infinitas soluciones")
