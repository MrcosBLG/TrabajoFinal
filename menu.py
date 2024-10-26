from login import login
from funciones import *

if __name__ == "__main__":
    if login():
        pass
    else:
        login()

while True:
    menu = 0
    archivoStock = 'stock.csv'
    archivoCompras = 'compras.csv'
    archivoVentas = 'ventas.csv'
    linea = "-" * 150      

    print(linea)
    print("Acciones del menu principal:")
    print("\t[0] Salir\n\t[1] Ver informe de stock actual\n\t[2] Manipular Productos\n\t[3] Realizar una transaccion\n\t[4] Historial de transacciiones")
    print(linea)
    menu = int(input("Que accion desea realizar: "))

    while  menu not in (0,1,2,3,4) : 
        menu = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))

    if menu == 1:
        while True:
            print(linea + "\n Acciones del menu 1:")
            print("\t\t[0] Volver al menu principal\n\t\t[1] Ver informe de stock actual\n\t\t[2] Ordenar por productos con más stock\n\t\t[3] Ordenar por productos con menos stock\n\t\t[4] Ver productos agotados")
            print(linea)
            opcion1 = int(input("Que accion desea realizar: "))
            while  opcion1 not in (1,2,3,4,0) : 
                opcion1 = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero compatible: "))

            if opcion1 == 1:
                inventario_stock(archivoStock)
                
            if opcion1 == 2:
                inventario_stock_ordenado(archivoStock,"mayor",None)

            if opcion1 == 3:
                inventario_stock_ordenado(archivoStock,"menor",None)

            if opcion1 == 4:
                inventario_stock_ordenado(archivoStock,None,"noStock")
                
            if opcion1 == 0:
                break
        
        #Historial de movimientos
    if menu == 2 :
        while True:  
            print(linea + "\n Acciones del menu 2:")
            print("\t\t[0] Volver al menu principal\n\t\t[1] Editar producto\n\t\t[2] Ingresar nuevos productos\n\t\t[3] Eliminar productos\n\t\t[4] Buscar productos")
            print(linea)
            opcion2 = int(input("Que accion desea realizar: "))

            while  opcion2 not in (0,1,2,3,4) :
                opcion2 = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))

            if opcion2 == 1:
                id_prod = int(input("Ingrese el id del producto que desea editar:"))
                editar_valor = int(input("Que valor desea editar? [1]Nombre [2]Stock [3]Precio: "))

                while editar_valor not in (0,1,2,3) :
                    editar_valor = int(input("No existe opcion para ese numero, por favor introduzca un numero compatible:"))

                if editar_valor == 1: # Nombre
                    nuevo_nombre = str(input("Ingrese el nuevo nombre:"))
                    editar_producto(archivoStock,id_prod,nuevo_nombre)

                if editar_valor == 2: # Stock
                    nuevo_stock = input("Ingrese el nuevo valor de stock:")
                    editar_producto(archivoStock,id_prod,None,nuevo_stock)

                if editar_valor == 3: # Precio
                    nuevo_precio = input("Ingrese el nuevo precio:")
                    editar_producto(archivoStock,id_prod,None,None,nuevo_precio)

            if opcion2 == 2:
                nombre = input("Nombre:")
                stock = input("Stock:")
                precio = input("Precio:")
                agregar_producto(archivoStock,nombre,stock,precio)

            if opcion2 == 3:
                eliminar = int(input("Ingrese el id del producto que desea eliminar:"))
                eliminar_producto(archivoStock, eliminar)

            if opcion2 == 4:
                buscar = input("Nombre del producto que desea buscar:")
                buscar_producto(archivoStock, buscar)

            if opcion2 == 0:
                break
        

    if menu == 3 :
        while True:
            print(linea + "\n Acciones del menu 3:")
            print("\t\t[0] Volver al menu principal\n\t\t[1] Realizar una compra\n\t\t[2] Realizar una venta")
            print(linea)
            opcion3 = int(input("Que accion desea realizar: "))
            if opcion3 == 1:
                comp_nombre = input("Nombre del producto:")
                comp_stock = int(input("Stock entrante:"))
                comp_precio = int(input("Precio actual:"))
                realizar_compra(archivoStock,comp_nombre,comp_stock,comp_precio)
            if opcion3 == 2:
                vent_nombre = input("Nombre del producto:")
                vent_stock = int(input("Stock saliente:"))
                vent_precio = int(input("Precio de venta:"))
                realizar_venta(archivoStock,vent_nombre,vent_stock)
            if opcion3 == 0:
                break

    if menu == 4:
        while True:
            print(linea + "\nOpciones del menu 4:")
            print("\t\t[0] Volver al menu principal\n\t\t[1] Historial de compras\n\t\t[2] Historial de ventas")
            print(linea)
            opcion4 = int(input("Que accion desea realizar: "))
            if opcion4 == 1:
                print("Historial de compras:")
                historial_transacciones(archivoCompras)
            if opcion4 == 2:
                print("Historial de ventas:")
                historial_transacciones(archivoVentas)
            if opcion4 == 0:
                break

    if menu == 0:
        print(0)
        break

