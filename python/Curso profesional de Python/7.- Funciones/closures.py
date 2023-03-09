"""
def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'
        nonlocal b
        b = 'Cambio de valor'

        print(a)
        print(b)

    funcion_anidada()
    

funcion_principal()



def saludar():


    def mostrar_mensaje():
        print('Hola, nos encontramos en el curso de Python')

    return mostrar_mensaje

respuesta = saludar()

respuesta()

"""

def saludar(username):
    mensaje =  f'Hola {username}' #Variable local

    def mostrar_mensaje():
        print(mensaje)

    return mostrar_mensaje
username = 'Cody' 
respuesta = saludar(username)

respuesta()

username = 'Alfonso' 

respuesta()

