# metodo. tiene una respuesta diferente en funcion del objeto que llame
#sobrecarga de metodos : suele estar relacionado

#metodo(argumentp,argumento=None)


def comer(quien,que,donde='en tu casa'):
    print(f'{quien}esta comiendo {que}  en {donde}')

comer('laura','chuletas')
comer('pepe','solomillo','en un bar')

# Polimorfismo en clases
class Estudiante():
    def hacerExamen(self):
        print('el examen es teorico de 20 preguntas tipo test')