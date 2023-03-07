lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']

lista_cursos2 = ['C', 'C++', 'Docker']

primer_curso = lista_cursos[0]
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)

ultimo_curso= lista_cursos[4]
print(ultimo_curso)


# lista_cursos[4] = 'Rust'
print(len(lista_cursos))

#[inicio:fin:salto]
sub_lista = lista_cursos[0:3]
print(sub_lista)




lista_cursos.append('MongoDB')
lista_cursos.append('C#')
lista_cursos.append('JavaScript')

lista_cursos.insert(1, 'Rails')
lista_cursos.insert(0, 'PyGame')

lista_cursos.extend(lista_cursos2)

print(lista_cursos)

print(lista_cursos2)
print(len(lista_cursos))

lista_cursos.remove('MongoDB')
del lista_cursos[0]

lista_cursos.clear()

print(lista_cursos)


print('Ejercicio 2')

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

lista.sort(reverse=True)

print(lista)

print(min(lista))
print(max(lista))


print(5 in lista)

index = lista.index(5)
print (index)


print('Ejercicio 3')

cursos = ['Python', 'Django', 'Flask']

cursos_tupla = tuple(cursos)
print(cursos_tupla)


niveles = ('Básico', 'Intermedio', 'Avanzado')

niveles_lista = list(niveles)
print(type(niveles_lista))

