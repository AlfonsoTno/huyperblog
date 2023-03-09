diccionario = {'a':1, 'b':2, 'c':3, 'd':4}
print(len(diccionario))

del diccionario['a'] # 1
valor = diccionario.pop('c') # 2
print(valor)

diccionario.clear()


print(len(diccionario))
print(diccionario)