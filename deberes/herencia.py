class Trabajo:
    pass
class Trabajador(Trabajo):
    pass
class Trabajo:
    def __init__(self,nombre,edad) -> None:
        self.nombre=nombre
        self.edad=edad
    def asistencia(self):
        pass
class Trabajador(Trabajo):
    def trabajo(self):
        print(f'{self.nombre} trabaja de ingeniero y tiene {self.edad}')
class Trabajadora(Trabajo):
    def trabajo(self):
        print(f'{self.nombre} trabaja de conductora y tiene {self.edad}')


trabajador1=Trabajador('Jaime',36)
trabajador1.trabajo()
trabajadora1=Trabajadora('Marta',42)
trabajadora1.trabajo()