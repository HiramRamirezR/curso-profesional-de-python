def pares(): # Generador -> Lazy iterator
    for num in range(0, 100, 2):
        yield num

        print("Se ha ejecutado el yield")

for par in pares():
    print(par)