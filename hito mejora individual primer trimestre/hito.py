class Cliente():
    def datos():
        while True:
                inicio=input('Bienvenido, registrese o inicie sesión: ')
                if inicio=='registrarse':
                    nombre=input('Introduzca nombre completo: ')
                    correo=input('Introduzca correo electronico: ')
                    contraseña=input('Introduzca una contraseña: ')
                    numero=input('Introduzca número de telefono: ')
                    DNI=input('Introduzca su DNI: ')
                    direccion=input('Introduzca su direccion: ')
                    print('Cliente registrado correctamente. Bienvenido')
                    break

                elif inicio=='iniciar sesión':
                    contraseña=input('Introduzca su contraseña ')
                    numero=0000000
                    nombre='X'
                    print('Inicio sesion')
                    break
                else:
                    print("no")
        
        
class Pedirproducto(Cliente):
    def compra():
        print('Tenemos 5 productos a la venta' )
        print('camiseta=10€(sin contar el iva)')
        print('gorro=5€(sin contar el iva)')
        print('pantalon=15€(sin contar el iva)')
        print('guantes=8€(sin contar el iva)')
        print('sudadera=20€(sin contar el iva)')
        print('Elige el producto que quiere comprar comprar camiseta,gorro,guantes,pantalon y sudadera, al finalzar de al boton terminar ')
        pedido=0
        facturación=0
        while True:
            pedidos=input('Elija los productos que desea comprar:')
            if pedidos=='camiseta':
                facturación=facturación+10
                pedido=pedido+1
                print('ha comprado camiseta')
            elif pedidos=='gorro':
                facturación=facturación+5
                pedido=pedido+1
                print('ha comprado gorro')
            elif pedidos=='pantalon':
                facturación=facturación+15
                pedido=pedido+1
            elif pedidos=='guantes':
                facturación=facturación+8
                pedido=pedido+1
                print('ha comprado guantes')
            elif pedidos=='sudadera':
                facturación=facturación+20
                pedido=pedido+1
                print('ha comprado sudadera')
            elif pedidos=='terminar':
                break
            else:
                print('No ha comprado nada')
        print(f'Rrealizo un total de {pedido} pedidos')
        pais=(input('Es de España: '))
        if pais== 'si':
            factura=facturación*1.21
            print(f'Su factura total es de {factura}')
        else:
            factura=facturación*1.59
            print(f'Su factura total es de {factura}')
        print('Su factura sera imprimida en un PDF y le enviaremos un seguimiento por el correo.')
        print('Muchas gracias por su compra, le esperamos pronto.')



cliente1=Pedirproducto
cliente1.datos()
cliente1.compra()
