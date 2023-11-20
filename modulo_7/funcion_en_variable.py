def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

mi_funcion = centigrados_a_farhenheit

print(type(mi_funcion))
print(mi_funcion(10))

# <class 'function'>
# 50.0