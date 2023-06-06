#Crear una clase cliente con las propiedades, nombre, ciudad y facturacion de constructor
#Alta al cliente : indra,madrid,15000/repsol,sevilla,20000
#crea un metodo para mostrar los datos de los clientes


from random import random


class Cliente:
    def __init__(self,nombre,ciudad, facturacion) -> None:
       self.nombre=nombre
       self.ciudad=ciudad
       self.facturacion=facturacion
    def datos(self):
        print(f'{self.nombre} de {self.ciudad} factura {self.facturacion}')
    def totalFactura(self):
        if self.facturacion>50000:
            self.facturacion=self.facturacion*0.95
        total=self.facturacion*1.21
        print(f'El total de factura es {total} euros')
    def setFacturacion(self,facturacion):  #ejemplo de setter
        self.facturacion=facturacion


cliente1=Cliente('indra','madrid',1500)
cliente2=Cliente('repsol','sevilla',20000)
cliente1.datos()
cliente2.datos()


#prepara un metodo en la clase cliente para calcular el totalfactura
#facturacion de +21% de iva. Si la facturacion es superior a 50000 tiene un decuento
# antes de iva del 5%


#muestra el total de facturacion para cada cliente
#tenemos un nuevo cliente : Iberia,Sevilla,65000¿cuanto es su totalfactura?
cliente1.totalFactura()
cliente2.totalFactura()
cliente3=Cliente('iberia','sevilla',65000)
cliente3.totalFactura()


#crea un metodo para cambiar la facturacion del cliente
#el nuevo metodo pide como parametro la nueva facturacion 
#llama la metodo verDetalle y comprueba que la facturacion se ha actualizado

cliente1.setFacturacion(54000)
cliente2.datos()


#necesitamos crear 10 clientes nuevos
#nombre y la ciudad, cliente100, cliente101 ....y la ciudad madrid
#la facturación será un número aleatorio entre 1000 y 50000
#muestra el detalle de los 10 nuevos clientes


clientes=[]
for i in range(11):
    if i>=10:
        ciente=Cliente(f'cliente1{i}','madrid', round(50000*random(),2))
    else:
        ciente=Cliente(f'cliente10{i}','madrid',round(50000*random(),2))
    clientes.append(Cliente)
for c in clientes:
    c.datos()