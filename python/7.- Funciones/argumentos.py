def promedio(*args): # tupla
    return sum(args) / len(args)


#resultado = promedio(10, 10, 5, 7, 10)
#print (resultado)

#print('String', 10, 14.5, True)

def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)

# combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, p4=1000)


def usuarios(**kwargs): # dict
    print(kwargs)
    print(type(kwargs))

#usuarios(eduardo=[10, 10, 8], fernando=[10, 9, 9])

def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1, 2, 3, 4, 5, cody=True, curso='Python')