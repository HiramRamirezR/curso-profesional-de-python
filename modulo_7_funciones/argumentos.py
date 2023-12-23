# Esta función solamente acepta un argumento
def promedio(listado):
    return sum(listado) / len(listado)

promedios = [10, 8, 6, 9, 7]

print(promedio(promedios))
# 8.0


# Usando *args para aceptar varios argumentos
# Los argumentos se pasan como una tupla
def promedio_args(*args):
    return sum(args) / len(args)

print(promedio_args(10, 8, 6, 9, 7))
# 8.0


# Haciendo una combinación de argumentos
def combinacion(p1, p2, *args, p3):
    print(p1)
    print(p2)
    print(args)
    print(p3)

combinacion("p1", "p2", 1, 2, 3, 4, 5, p3="p3")
# p1
# p2
# (1, 2, 3, 4, 5)
# p3