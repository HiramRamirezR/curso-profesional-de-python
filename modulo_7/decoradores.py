"""
a -> La función principal (Decorador)
b -> La función a decorar
c -> La función decorada

a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print(">>> Antes del llamado a la función b")
        resultado = funcion_b(*args, **kwargs)
        print(">>> Después del llamado a la función b")

        return resultado

    return funcion_c

@funcion_a
def suma(num_1, num_2):
    return num_1 + num_2

resultado = suma(3, 5)
print(resultado)