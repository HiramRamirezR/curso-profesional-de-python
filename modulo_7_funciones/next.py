def pares(): # Generador -> Lazy iterator
    for num in range(0, 100, 2):
        yield num

        print("Se ha ejecutado el yield")

generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print("El generador ha terminado")
        break