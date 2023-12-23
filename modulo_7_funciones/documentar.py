# Docstring
# __doc__ (Módulos, Clases, Métodos y Funciones)

def suma(num_1, num_2):
    """
    Funcion que suma dos numeros
    
    Parametros:
    num_1 -> (int)
    num_2 -> (int)

    Retorna la suma de los dos argumentos.

    >>> suma(1, 2)
    3

    >>> suma(10, 5)
    15
    """
    return num_1 + num_2

# print(suma.__doc__)

# Para testear la función:
# python -m doctest documentar.py