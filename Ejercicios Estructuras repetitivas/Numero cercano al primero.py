numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))
numero4 = int(input("Numero 4: "))
numero5 = int(input("Numero 5: "))


resta5 = numero5 - numero1
resta4 = numero4 - numero1
resta3 = numero3 - numero1
resta2 = numero2 - numero1

if resta5 < resta4 and resta5 < resta3 and resta5 < resta2:
    print(f"El mas cercano a {numero1} es {numero5}")

if resta4 < resta5 and resta4 < resta3 and resta4 < resta2:
    print(f"El mas cercano a {numero1} es {numero4}")

if resta3 < resta4 and resta3 < resta5 and resta3 < resta2:
    print(f"El mas cercano a {numero1} es {numero3}")

if resta2 < resta4 and resta2 < resta3 and resta2 < resta5:
    print(f"El mas cercano a {numero1} es {numero2}")
