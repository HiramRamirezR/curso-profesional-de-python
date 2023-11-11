lista = list(range(1,11))
print(lista)

lista.insert(0, "Hiram")
print(lista)

lista2 = ["uno", "dos", "tres"]
lista.extend(lista2)
print(lista)

lista.remove("Hiram")
print(lista)

del lista[-1]
print(lista)

lista.clear()
print(lista)

"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
['Hiram', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
['Hiram', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'uno', 'dos', 'tres']
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'uno', 'dos', 'tres']
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'uno', 'dos']
[]
"""