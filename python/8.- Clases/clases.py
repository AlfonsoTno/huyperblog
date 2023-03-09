# Attrs de clase (solo pertenecen a la clase y se ejecutan con la misma)
# Attrs de instancia (le pertencen a un objetos y se ocupan con el mismo) 

class Usuario:
    # Attrs de clase
    username = 'Usernmane por defualt'
    email = ''


#Usuario.username = 'User1'
#Usuario.email = 'info@codigofacilito.com'

# __dict__
user1 = Usuario()
# 1.- Verifica si el attr existe dentro del objeto 
# 2.- Verifica si el attrs existe dentro de la calase -> Lectura
# 3.- Lanza un error

user1.username = 'Cody' # Añadimos el attrs al objeto
user1.password = '1234'
print(user1.username) # De instancia
#print(Usuario.email)

print(user1.__dict__) # Dict