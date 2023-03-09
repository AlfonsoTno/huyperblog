class SerVivo:
    def dormir(self):
        print('El ser duerme.')



class Animal(SerVivo):
    def comer(self):
        print('El animal come.')
    
    def dormir(self):
        print('El animal duerme.')


class Mascota(Animal): #Clase Padre
    
    def comer(self):
        print('La mascota come.')
    


class Perro(Mascota): #Clase Hija
    pass


class Felino:

    def cazar(self):
        print('El felino caza.')


class Gato(Mascota, Felino):
    
    
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer() #ejecuta la  funcion del padre inmediato
        print(f'{self.nombre} come.')

    def dormir(self):
        print(f'{self.nombre} duerme.')

#duke = Perro()
#duke.comer()
#duke.dormir()

patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()
patricio.cazar()
#patricio.nombre()