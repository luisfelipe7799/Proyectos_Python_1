import math

print("Ecuacion del tipo ax^2 + bx + c =0")
a = 0
b = 0
c = 0
x1 = 0
x2 = 0
resultado = 0

a = int(input("Ingrese a : "))
b = int(input("Ingrese b : "))
c = int(input("Ingrese c : "))

if a == 0:
    print("La ecuacion es de primer grado, intente con otro numero")
else:
    if ((b ** 2) - (4 * a * c)) < 0:
        print("La discriminante es negativa por lo que la ecuacion no tiene soluciones reales")
    else:
        if a != 0:
            x1 = ((-b) + math.sqrt((b**2)-(4*a*c))) / (2*a)
            x2 = ((-b) - math.sqrt((b**2)-(4*a*c))) / (2*a)
            print(f"x1={x1}  y x2={x2} ")
        else:
            if b != 0:
                print("La ecuacion no tiene solucion")
            else:
                print("La ecuacion tiene infinitas soluciones")

