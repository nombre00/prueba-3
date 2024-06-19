# imprimir hoja de ruta

import csv

# exportar .txt
def exportar(listaPedidos):
    print("Exportando un archivo .txt")
    with open("Lista_de_pedidos.txt","w") as archivo:
        for pedido in listaPedidos:
            archivo.write(f"Nombre: {pedido['nombre']} {pedido['apellido']}\n")
            archivo.write(f"Dierección: {pedido['dirección']}, comuna: {pedido['comuna']}\n")
            archivo.write("Paquetes pedidos:\n")
            archivo.write(f"Paquetes grandes: {pedido['Pgrande']}\n")
            archivo.write(f"Paquetes medianos: {pedido['Pmediano']}\n")
            archivo.write(f"Paquetes pequeños: {pedido['Ppequeño']}\n\n")


# exportar .csv
def exportarCSV(listaPedidos):
    print("Exortando un archivo .csv")
    with open("Lista_de_pedidos.csv","w") as archivo:
        try:
            llaves = listaPedidos[0].keys()
        except:
            llaves = 'nombre', 'apellido', 'dirección', 'comuna', 'Pgrande', 'Pmediano', 'Ppequeño'
        escritor_csv = csv.DictWriter(archivo, fieldnames=llaves)
        escritor_csv.writeheader()
        for pedido in listaPedidos:
            escritor_csv.writerow(pedido)



# iba a incorporar esta función pero algo me fallo, lo podía resolver goggleando, pero bueno... hicimos un poquito extra.
""" # importar .csv
def importarCSV():
    listaPedidos = []
    print("Archivo importado.")
    with open("Lista_de_pedidos.csv","r") as archivo:
        lector_csv = csv.reader(archivo)

        for pedido in lector_csv:
            listaPedidos.append(dict(pedido))
    return listaPedidos """


