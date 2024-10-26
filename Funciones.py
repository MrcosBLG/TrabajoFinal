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
        
def eliminar_producto(archivo, id_producto):
    try:
        productos= [] #Aca se guardan los productos que no se van a eliminar
        producto_encontrado = False
        producto_eliminar = None #Aca se va a guardar el producto que vamos a eliminar junto a sus detalles
        
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            for indice, fila in enumerate(lector_csv, start=1):
                nombre, stock, precio = fila
                stock = int(stock)
                precio = float(precio)
                if indice == id_producto: #Si el indice coincide con el ID del producto que queremos eliminar pasa esto, el ID lo ponemos en el input del menu
                    producto_encontrado = True #Indica que el producto fue encontrado
                    producto_eliminar = ([nombre, stock, precio]) #Almacena los detalles del producto a eliminar
                else :
                    productos.append([nombre, stock, precio]) #Si el ID no es el del producto que queremos borrar se guarda en productos, lista donde guardamos los productos que no queremos eliminar
                    
        if not producto_encontrado: 
            print(f"Producto con ID {id_producto} no encontrado.")
            return
        
        print("Producto seleccionado para eliminar:")
        print(tabulate([producto_eliminar], headers=["Nombre", "Stock", "Precio"])) #Mostramos el producto a eliminar para que el usuario confirme o rechace si se arrepiente o se equivoco
        
        confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ").lower()
        
        if confirmacion == 's':
            with open(archivo, 'w', newline='') as f:
                escritor_csv = csv.writer(f)
                escritor_csv.writerows(productos) #Se rescribe todo el archivo pero eliminando el producto que se eligio
            print("Producto eliminado y archivo actualizado correctamente.")
        else:
            print("Eliminación cancelada.") #Si la confirmacion no es 's' se cancela
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")
        
def editar_producto(archivo, id_producto, nuevo_nombre=None, nuevo_stock=None, nuevo_precio=None):
    try: 
        productos = [] #Lista que guarda todos los productos
        producto_encontrado = False
        
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            for indice, fila in enumerate(lector_csv, start=1): #Start=1 para generar ids desde 1
                nombre, stock, precio = fila
                stock = int(stock)
                precio = float(precio)
                
                if indice == id_producto: #Verifica si el ID del producto a editar coincide con el indice de algun producto 
                    producto_encontrado = True 
                    nombre = nuevo_nombre if nuevo_nombre else nombre
                    stock = nuevo_stock if nuevo_stock is not None else stock      #Aca se le modifica el valor a las variables nombre stock y precio
                    precio = nuevo_precio if nuevo_precio is not None else precio
                    print(f"Producto editado : ID: {id_producto}, Nombre: {nombre}, Stock: {stock}, Precio: {precio}") #Muestra el producto editado
                    
                productos.append([nombre, stock, precio]) #Anade el producto editado o no a la lista de productos
        if not producto_encontrado:
            print(f"Producto con id {id_producto} no encontrado.") #Si no encuentra el id del producto tira esto
            return
        
        with open(archivo, 'w', newline='') as f:
            escritor_csv = csv.writer(f)
            escritor_csv.writerows(productos)
            print("Archivo actualizado correctamente.") #Aca entro al csv como escritor y escrivo todos los productos de nuevo incluido el editado para que se guarde
            
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error: {e}")
        
            
        
        
        
    
    
            