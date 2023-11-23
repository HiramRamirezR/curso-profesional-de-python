def saludar():

    def mostrar_saludo():
        print("Hola")

    return mostrar_saludo

saludo = saludar()

print(saludo)