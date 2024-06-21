class Usuario:
    username = "Default username"
    email = "Default email"

user1 = Usuario()
# 1.- Python verifica si el atributo existe dentro del objeto
# 2.- Python verifica si el atributo existe dentro de la clase (sólo para lectura)
# 3.- Python lanzará un error si el atributo no existe

# user1.username = "Hiram" # Añadimons un atributo al objeto
print(user1.username)
print(id(user1.username))
print(Usuario.username)
print(id(Usuario.username))
print(user1.__dict__)

# Asi se añade de forma dinamica un atributo al objeto
user1.password = "1234"
# Python al encontrar que el atributo no existe, lo crea en tiempo de ejecución