# listar todos los pedidos

def listarPedido(listaPedidos):
    print("\nLista de pedidos durante esta sesión: \n")
    for pedido in listaPedidos:
        print(f"Nombre del cliente: {pedido['nombre']} {pedido['apellido']}")
        print(f"Dirección: {pedido['dirección']}, comuna: {pedido['comuna']}")
        print("Paquetes pedidos:")
        print(f"Paquetes grandes: {pedido['Pgrande']}")
        print(f"Paquetes medianos: {pedido['Pmediano']}")
        print(f"Paquetes pequeños: {pedido['Ppequeño']}")
        print("")