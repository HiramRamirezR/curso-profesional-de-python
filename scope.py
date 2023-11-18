animal = "cat" # global scope

def imprimir_animal():
    animal = "dog" # local scope
    print(animal)

imprimir_animal()
print(animal)