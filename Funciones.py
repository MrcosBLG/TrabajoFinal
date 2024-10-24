import csv
from tabulate import tabulate

def agregarproductos(archivo, nombre, stock, precio):
    try:
        with open(archivo, 'a', newline='') as f:
         escritor_csv = csv.writer(f)
         escritor_csv.writerow([nombre, int(stock), str(precio)])
    except: 
        print('error')