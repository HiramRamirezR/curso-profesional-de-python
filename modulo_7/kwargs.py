def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(hiram=[10,9,10], jahaziel=[9,9,9])

# {'hiram': [10, 9, 10], 'jahaziel': [9, 9, 9]}
# <class 'dict'>

def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion("a", "b", "c", p1=10, p2=20, p3=30)

# ('a', 'b', 'c')
# {'p1': 10, 'p2': 20, 'p3': 30}

# args -> ('a', 'b', 'c') => Tupla
# kwargs -> {'p1': 10, 'p2': 20, 'p3': 30} => Diccionario