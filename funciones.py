import csv
from tabulate import tabulate
from datetime import date, datetime

def inventario_stock(archivo): #Muestra inventario completo junto a ids
    try:
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            productos = []
            
            for indice, fila in enumerate(lector_csv, start=1):
                nombre, stock, precio = fila
                productos.append([indice, nombre, int(stock), float(precio)])

            print(tabulate(productos, headers=["ID", "Nombre", "Stock", "Precio"], tablefmt="github"))

    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error: {e}")

def inventario_stock_ordenado(archivo, orden=None, tock=None):
    try:
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            tabla = []
            
            for fila in lector_csv:
                nombre, stock, precio = fila
                stock = int(stock)
                if tock == "noStock" and stock == 0:
                    tabla.append([nombre,stock,float(precio)])
                elif not tock and stock > 0:
                    tabla.append([nombre,stock,float(precio)])

            if orden == "mayor":
                tabla.sort(key=lambda x: x[1], reverse=True)
            elif orden == "menor":
                tabla.sort(key=lambda x: x[1])

            print(tabulate (tabla, headers=["Nombre","Stock","Precio"],tablefmt="github"))
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error: {e}")

def agregar_producto(archivo, nombre, stock, precio):
    try:
        with open(archivo, 'a', newline='') as f:
            escritor_csv = csv.writer(f)
            escritor_csv.writerow([nombre, int(stock), str(precio)])
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error: {e}")

def buscar_producto(archivo, nombre_buscar):
    try:
        encontrado = False
        productos = []
        
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            
            for fila in lector_csv:
                nombre, stock, precio = fila
                if nombre_buscar.lower() in nombre.lower():
                    encontrado = True
                    productos.append([str(nombre), int(stock), float(precio)])

        if not encontrado:
            print("Producto no encontrado.")
            return

        print(tabulate(productos, headers=["Nombre", "Stock", "Precio"], tablefmt="github"))

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

def editar_producto(archivo, id_producto, nuevo_nombre=None, nuevo_stock=None, nuevo_precio=None):
    try:
        productos = []
        producto_encontrado = False
        
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            for indice, fila in enumerate(lector_csv, start=1):  # start=1 para generar ids desde 1
                nombre, stock, precio = fila
                stock = int(stock)
                precio = float(precio)

                if indice == id_producto:
                    producto_encontrado = True
                    nombre = nuevo_nombre if nuevo_nombre else nombre
                    stock = nuevo_stock if nuevo_stock is not None else stock
                    precio = nuevo_precio if nuevo_precio is not None else precio
                    print(f"Producto editado: ID: {id_producto}, Nombre: {nombre}, Stock: {stock}, Precio: {precio}")
                
                productos.append([nombre, stock, precio])

        if not producto_encontrado:
            print(f"Producto con ID {id_producto} no encontrado.")
            return

        with open(archivo, 'w', newline='') as f:
            escritor_csv = csv.writer(f)
            escritor_csv.writerows(productos)
            print("Archivo actualizado correctamente.")
    
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

def eliminar_producto(archivo, id_producto):
    try:
        productos = []
        producto_encontrado = False
        producto_eliminar = None
        
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            for indice, fila in enumerate(lector_csv, start=1):
                nombre, stock, precio = fila
                stock = int(stock)
                precio = float(precio)

                if indice == id_producto:
                    producto_encontrado = True
                    producto_eliminar = [nombre, stock, precio]
                else:
                    productos.append([nombre, stock, precio])

        if not producto_encontrado:
            print(f"Producto con ID {id_producto} no encontrado.")
            return

        print("Producto seleccionado para eliminar:")
        print(tabulate([producto_eliminar], headers=["Nombre", "Stock", "Precio"], tablefmt="github"))

        confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ").lower()

        if confirmacion == 's':
            with open(archivo, 'w', newline='') as f:
                escritor_csv = csv.writer(f)
                escritor_csv.writerows(productos)
            print("Producto eliminado y archivo actualizado correctamente.")
        else:
            print("Eliminación cancelada.")

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

def realizar_compra(archivo,nombre,stock,precio):
    nombre = nombre.lower()
    producto_existente = False
    productos = []
    
    try:
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            for fila in lector_csv:
                nombre_existente, stock_existente, precio_existente = fila
                stock_existente = int(stock_existente)
                precio_existente = float(precio_existente)

                if nombre_existente.lower() == nombre:
                    nuevo_stock = stock_existente + int(stock)
                    productos.append([nombre_existente, nuevo_stock, precio])
                    producto_existente = True
                else:
                    productos.append([nombre_existente, stock_existente, precio_existente])

        if not producto_existente:
            productos.append([nombre, int(stock), precio])

        with open(archivo, 'w', newline='') as f:
            escritor_csv = csv.writer(f)
            escritor_csv.writerows(productos)

        registrar_compra(nombre, stock)

        print("Producto agregado o actualizado correctamente.")
    
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

def registrar_compra(nombre, stock):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    try:
        with open("compras.csv", 'a', newline='') as f:
            escritor_csv = csv.writer(f)
            escritor_csv.writerow([fecha_actual, nombre, stock])
        print("Transacción registrada correctamente en 'compras.csv'.")
    except Exception as e:
        print(f"Error al registrar la compra: {e}")

def realizar_venta(archivo, nombre, cantidad_vendida):
    nombre = nombre.lower()  # Convertir el nombre a minúsculas para la comparación
    producto_existente = False
    productos = []
    venta_exitosa = False
    
    try:
        # Leer el archivo CSV para verificar si el producto existe y tiene suficiente stock
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            for fila in lector_csv:
                nombre_existente, stock_existente, precio_existente = fila
                stock_existente = int(stock_existente)
                precio_existente = float(precio_existente)

                # Comparar nombres ignorando mayúsculas/minúsculas
                if nombre_existente.lower() == nombre:
                    producto_existente = True
                    if stock_existente >= int(cantidad_vendida):
                        # Si hay suficiente stock, restar la cantidad vendida
                        nuevo_stock = stock_existente - int(cantidad_vendida)
                        productos.append([nombre_existente, nuevo_stock, precio_existente])
                        venta_exitosa = True
                    else:
                        # Si no hay suficiente stock o es 0, avisar al usuario
                        print(f"No se puede realizar la venta. Stock disponible: {stock_existente}, solicitado: {cantidad_vendida}")
                        return
                else:
                    # Si no es el producto que buscamos, agregarlo tal cual
                    productos.append([nombre_existente, stock_existente, precio_existente])

        # Si no existe el producto, informar al usuario
        if not producto_existente:
            print(f"Producto '{nombre}' no encontrado.")
            return

        # Sobrescribir el archivo con el nuevo stock después de la venta
        if venta_exitosa:
            with open(archivo, 'w', newline='') as f:
                escritor_csv = csv.writer(f)
                escritor_csv.writerows(productos)

            # Registrar la venta en el archivo "ventas.csv"
            registrar_venta(nombre, cantidad_vendida)

            print("Venta realizada y archivo actualizado correctamente.")
    
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error: {e}")

def registrar_venta(nombre, cantidad_vendida):
    """Registra la venta en el archivo 'ventas.csv'"""
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    try:
        with open("ventas.csv", 'a', newline='') as f:
            escritor_csv = csv.writer(f)
            escritor_csv.writerow([fecha_actual, nombre, cantidad_vendida])
        print("Transacción registrada correctamente en 'ventas.csv'.")
    except Exception as e:
        print(f"Error al registrar la venta: {e}")

def historial_transacciones(archivo):
    try:
        with open(archivo, 'r', newline='') as f:
            lector_csv = csv.reader(f)
            tabla = [] 
            for fila in lector_csv:
                nombre, stock, precio = fila
                tabla.append([nombre, stock, precio])
            
            print(tabulate(tabla, headers=["Fecha", "Nombre", "Stock"], tablefmt="github"))
            
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error: {e}")
