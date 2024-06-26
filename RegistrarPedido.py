# registrar pedido

# inicializaciones.


def registrarPedido(listaPedidos):

    pedido = {}
    paquetesGrandes = 0
    paquetesMedianos = 0
    paquetesPequeños = 0

    print("Registrando pedido:")
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    dirección = input("Ingrese la dirección del cliente: ")
    comuna = input("Ingrese la comuna del cliente: ")

    # ingreso de paquetes: grande, mediano y chico.
    opc = 0
    while opc != 4:
        print("Qué tipo de paquete quiere comprar? ")
        print("1- Paquete grande.")
        print("2- Paquete mediano.")
        print("3- Paquete pequeño.")
        print("4- Salir.")
        try:
            opc = int(input("Ingrese su opción: "))
            # si 1.
            if opc == 1:
                print("Há selecionado el paquete grande, cuantos quiere? ")
                cantidad = 0
                while cantidad < 1:
                    try:
                        cantidad = int(input("Ingrese la cantidad por favor: "))
                        if cantidad >= 1: 
                            paquetesGrandes += cantidad
                        else:
                            print("Ingrese una cantidad positiva.")
                    except:
                        print("Ingrese una cantidad válida")
            
            # si 2.
            if opc == 2:
                print("Há selecionado el paquete mediano, cuantos quiere? ")
                cantidad = 0
                while cantidad < 1:
                    try:
                        cantidad = int(input("Ingrese la cantidad por favor: "))
                        if cantidad >= 1: 
                            paquetesMedianos += cantidad 
                        else:
                            print("Ingrese una cantidad positiva.")
                    except:
                        print("Ingrese una cantidad válida")
            
            # si 2.
            if opc == 3:
                print("Há selecionado el paquete pequeño, cuantos quiere? ")
                cantidad = 0
                while cantidad < 1:
                    try:
                        cantidad = int(input("Ingrese la cantidad por favor: "))
                        if cantidad >= 1: 
                            paquetesPequeños += cantidad 
                        else:
                            print("Ingrese una cantidad positiva.")
                    except:
                        print("Ingrese una cantidad válida")
        
        except ValueError:
            print("Ingrese una opción válida.\n")


    # tabulaciones
    pedido['nombre'] = nombre
    pedido['apellido'] = apellido
    pedido['dirección'] = dirección
    pedido['comuna'] = comuna
    pedido['Pgrande'] = paquetesGrandes
    pedido['Pmediano'] = paquetesMedianos
    pedido['Ppequeño'] = paquetesPequeños
    listaPedidos.append(pedido)