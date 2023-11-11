# * -> Lista
# _ -> Omitir valor

# Descomprimir tupla

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

uno, _, tres, cuatro, *lista, nueve, diez = numeros

print(uno)
print(tres)
print(cuatro)
print(lista)
print(nueve)
print(diez)

"""
1
3
4
[5, 6, 7, 8]
9
10
"""

# Comprimir tupla

tupla1 = (1, 2, 3)
tupla2 = (10, 20, 30)
tupla3 = (100, 200, 300)

tupla_zip = zip(tupla1, tupla2, tupla3)
print(tuple(tupla_zip))

#((1, 10, 100), (2, 20, 200), (3, 30, 300))