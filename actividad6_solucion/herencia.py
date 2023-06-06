#Caracteristicas de POO. Python la soporta
#sobreescritura : override : Caracteristicas en la herencia

#clase Padre, base, superclase
class Padre:
    nombre='maria perez'
    def __init__(self,nombre,ciudad) -> None:
        self.nombre=nombre
        self.ciudad=ciudad
    @staticmethod
    def saludar():
        print('estoy saludando')

class Madre:
    unidades=15


#clase derivada, hija, subclase
class Hija(Padre,Madre): #heredar
    def __init__(self, nombre, ciudad) -> None:
        self.nombre=nombre
        self.ciudad=ciudad
        super().__init__(nombre, ciudad)
    @staticmethod
    def saludar():
        print('estoy saludando desde la hija')


#instanciar las clases : crea un objeto de esa clase en memoria
hija=Hija('marta sanchez','segovia')
hija.saludar()
print(hija.nombre)
print(hija.unidades)