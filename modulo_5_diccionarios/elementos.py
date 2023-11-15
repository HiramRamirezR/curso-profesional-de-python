diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}

valor = diccionario["d"]
print(valor)

valor = diccionario.get("g", None)
print(valor)

# setdefault -> Obtener o establecer un valor.
valor = diccionario.setdefault("e", 5)
print(diccionario)

# 4
# None
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}