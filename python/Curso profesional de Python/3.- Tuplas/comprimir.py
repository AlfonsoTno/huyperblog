lista = [1, 2, 3, 4, 5]

tupla = (10, 20, 30, 40, 50)

lista_2= [100, 200, 300, 400, 5000]

tupla_2 = (1000, 2000, 3000, 4000, 5000)

resultado = zip(lista, tupla, lista_2, tupla_2) # -> zip
resultado = tuple(resultado)


print(resultado)