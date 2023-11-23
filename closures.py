def saludar(nombre):
    mensaje = f"Hola {nombre}"

    def mostrar_saludo():
        print(mensaje)

    return mostrar_saludo

nombre = "Hiram"
saludo = saludar(nombre)

saludo()