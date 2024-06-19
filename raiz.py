# raiz.

# importaciones
import RegistrarPedido, ListarPedidos, Exportar

# inicalizaciones
opcion = 0
listaPedidos = []

# menu
while opcion != 4:
    print("\n###### MENU ######")
    print("1- Registrar pedido.")
    print("2- Listar todos los pedidos.")
    print("3- Imprimir hoja de ruta.")
    print("4- Salir.")

    try:
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            RegistrarPedido.registrarPedido(listaPedidos)
        
        elif opcion == 2:
            ListarPedidos.listarPedido(listaPedidos)

        elif opcion == 3:
            print("Seleccione el formato en que quere exportar: ")
            print("1- .txt")
            print("2- .csv")
            print("3- Salir.")

            opc = "0"
            while opc != "3":
                opc = input("Ingrese su opción: ")
                if opc == "1":
                    Exportar.exportar(listaPedidos)
                    break
                elif opc == "2":
                    Exportar.exportarCSV(listaPedidos)
                    break

    except ValueError:
        print("Ingrese una opción válida.\n")

print("Cerrando sesión.")