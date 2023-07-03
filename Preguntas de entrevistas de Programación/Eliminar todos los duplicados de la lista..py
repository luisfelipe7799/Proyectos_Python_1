lista = list(range(10)) + list(range(10))
print(lista)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista = list(set(lista))
print(lista)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]