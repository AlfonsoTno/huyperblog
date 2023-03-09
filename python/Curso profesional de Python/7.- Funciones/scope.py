animal ='León' # Variable global -> funcion, condicion o ciclo

def imprimir_animal():
    global animal # indica que modificará la variable globl
    animal = 'Ballena'   

    # animal = 'Ballena' # Variable local

    tipo = 'Mamifero' # Variable local

    print(animal)
    print(id(animal))

imprimir_animal()

print(animal)
print(id(animal))