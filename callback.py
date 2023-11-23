promedio = lambda *args: sum(args) / len(args)

aprobado = lambda calificacion: calificacion >= 6

# Crear función que combine las 2 funciones anteriores

def mensaje(func_promedio, func_aprobado, *args):
    if func_aprobado(func_promedio(*args)):
        print(f"Aprobado con {func_promedio(*args)}")
    else:
        print("Reprobado")

mensaje(promedio, aprobado, 10, 9, 8)
