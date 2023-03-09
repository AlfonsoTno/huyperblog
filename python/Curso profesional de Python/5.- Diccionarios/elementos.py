diccionario = {'a':1, 'b':2, 'c':3, 'd':4}

print('z' in diccionario)

valor = diccionario['d']
print(valor)

# get
# despues de la coma se muestra el vaor en caso de error 
valor = diccionario.get('z', 'La llave no existe en el diccionario')
print(valor)

#set 
#setdefault devuelve el valor de la variable y en caso de no exisitr la crea
# agrega valor a diccionario 
valor = diccionario.setdefault('e', 5)
print(valor)
