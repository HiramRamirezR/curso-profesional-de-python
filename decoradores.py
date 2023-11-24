"""
a -> La función principal (Decorador)
b -> La función a decorar
c -> La función decorada

a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c():
        print(">>> Antes del llamado a la función b")
        funcion_b()
        print(">>> Después del llamado a la función b")

    return funcion_c

@funcion_a
def suma():
    print(1+1)

@funcion_a
def resta():
    print(5-2)

suma()
resta()