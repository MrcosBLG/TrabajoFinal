import csv
from tabulate import tabulate

def agregarproductos(archivo, nombre, stock, precio):
    try:
        with open(archivo, 'a', newline='') as f:
         escritor_csv = csv.writer(f)
         escritor_csv.writerow([nombre, int(stock), str(precio)])
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
            print(f"error {e}")
        
def buscar_producto(archivo, buscar):
    productos =[]
    with open(archivo, 'r', newline= '') as f:
        lector_csv = csv.reader(f)
        for fila in lector_csv:
            nombre, stock, precio = fila
            if buscar.lower() in nombre.lower():
                productos.append([str(nombre), int(stock), float(precio)])
    print(tabulate(productos, headers=["Nombre", "Stock", "Precio"]))
            
def inventario_stock(archivo):
    try:
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            productos = []
            for indice, fila in enumerate(lector_csv, start=1):
                nombre, stock, precio = fila
                productos.append([indice, str(nombre), int(stock), float(precio)])
        print(tabulate(productos, headers=["ID", "Nombre", "Stock", "Precio"]))
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error: {e}")
        
            