def pares(): # Generador -> Lazy iterator
    for numero in range(0, 12, 2):
        yield numero # La función suspende su ejecución
    
        print('Se reanuda la ejecución')

#for par in pares():
#   print(par)

generador = pares()
#print(next(generador))
#print(next(generador))

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizó')
        break
