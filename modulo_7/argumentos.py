# Esta función solamente acepta un argumento

def promedio(listado):
    return sum(listado) / len(listado)

promedios = [10, 8, 6, 9, 7]

print(promedio(promedios))

# Usando *args para aceptar varios argumentos
# Los argumentos se pasan como una tupla

def promedio_args(*args):
    return sum(args) / len(args)

print(promedio_args(10, 8, 6, 9, 7))