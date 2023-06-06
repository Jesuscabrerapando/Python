#Caracteristicas POO
#modificadores de acceso : private,public,protected...
#ocultar atributos, metodos o clases al resto

#protected. Unicamente se puede utilizar en sus clases derivadas

class Encapsular():
    nombre='clase enapsulada' #atributo sin nada. es publico*
    __ciudad='sevilla' #atributo private
    def secreto(self):
        print('mensaje directo')
    def paraHija(self):
        print('mensaje para hija')

class Hija(Encapsular):
    pass

encapsulamiento=Encapsular()
print(encapsulamiento.nombre)
#print(encapsulamiento.__ciudad)



hija=Hija()
print(hija.nombre)
#print(hija.ciudad)
#hija.secreto()
hija._paraHija()