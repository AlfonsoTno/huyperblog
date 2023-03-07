# * -> convierte en lista
# _ -> Omitir valor
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

uno, dos, tres, cuatro, *resto_valores, nueve, diez = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)

print(nueve)
print(diez)
