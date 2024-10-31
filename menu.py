
from login import login
from Funciones import *
if __name__ == "__main__":
    if login():
        pass
    else:
        login()
menu = 0
while True:
    csvdestock = 'stock.csv'
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Acciones del menu ")
    print("""
    [0] Salir      
    [1] Editar o modificar el inventario 
    [2] Historial de movimientos 
    [3] Ver informe de stock actual
    [4] Realizar una transaccion
    """)
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    menu = int(input("Que accion desea realizar: "))
    while  menu not in (0,1,2,3,4) : 
        menu = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))
    if menu == 0:
        break
        #EDITAR O MODIFICAR EL INVENTARIO 
    if menu == 1:
        while True:
            print("""
                [0] Volver al menu principal
                [1] Ingresar nuevos productos al inventario 
                [2] Buscar productos 
                [3] Eliminar producto
                [4] Modificar productos
                
                
                """)
            opcion1 = int(input("Que accion desea realizar: "))
            while  opcion1 not in (1,2,3,4,0) : 
                opcion1 = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))
            if opcion1 == 1:
                nombre = input("Nombre: ")
                stock = input("Stock: ")
                precio = input("Precio: ")
                agregarproductos(csvdestock,nombre, stock, precio)
            if opcion1 == 2:
                buscar = input("Que producto desea buscar: ")
                buscar_producto(csvdestock, buscar)
                pass
            if opcion1 == 3:
                #ELIMINAR PRODUCTO
                eliminar = int(input("Ingrese el id del producto que desea eliminar:"))
                eliminar_producto(csvdestock, eliminar)
                pass
            if opcion1 == 4:
                inventario_stock(csvdestock)
                print("""  
                     """)
                #EDITAR PRODUCTO
                id_prod = int(input("Ingrese el id del producto que desea editar, o 0 para volver:")) #input number
                if id_prod == 0:
                    break  
                editar_valor = int(input("Que valor desea editar? [1]Nombre [2]Stock [3]Precio: "))
                

                while editar_valor not in (0,1,2,3) :
                    editar_valor = int(input("No existe opcion para ese numero, por favor introduzca un numero compatible:")) #Si pones un numero q no sea 0 1 2 3 te pide que pongas numero valido

                if editar_valor == 1: # Nombre
                    nuevo_nombre = str(input("Ingrese el nuevo nombre:"))
                    editar_producto(csvdestock,id_prod,nuevo_nombre) #Llama a la función 'editar_producto' con el nuevo valor de nombre

                if editar_valor == 2: # Stock
                    nuevo_stock = input("Ingrese el nuevo valor de stock:")
                    editar_producto(csvdestock,id_prod,None,nuevo_stock)  #Llama a la función 'editar_producto' con el nuevo valor de stock

                if editar_valor == 3: # Precio
                    nuevo_precio = input("Ingrese el nuevo precio:")
                    editar_producto(csvdestock,id_prod,None,None,nuevo_precio) #Llama a la función 'editar_producto' con el nuevo valor de precio
            if opcion1 == 0:
                break
        
        #Historial de movimientos
    if menu == 2 :
        while True:
            print("""
                [0] Volver al menu principal
                [1] Historial de ventas
                [2] Historial de compras
                
                """)
            opcion2 = int(input("Que accion desea realizar: "))
            while  opcion2 not in (0,1,2,3) :
                opcion2 = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))
            if opcion2 == 1:
                    pass
            if opcion2 == 2:
                    pass
            if opcion2 == 0:
                break
        

    if menu == 3 :
        while True:
            print("""
                [0] Volver al menu principal
                [1] Ver informe del stock actual
                [2] Consultar stock de un producto
                [3] Ordenar por productos con más stock
                [4] Ordenar por productos con menos stock
                [5] Ver productos agotados
                """)
            opcion3 = int(input("Que accion desea realizar: "))
            while  opcion3 not in (0,1,2,3,4,5) :
                opcion3 = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))
            if opcion3 == 1:
                #Ver informe del stock actual
                inventario_stock(csvdestock)
            if opcion3 == 2:
                #Consultar stock de un producto
                pass
            if opcion3 == 3:
                #Ordenar por productos con más stock
                pass
            if opcion3 == 4:
                #Ordenar por productos con menos stock
                pass
            if opcion3 == 5:
                #Ver productos agotados
                pass
            if opcion3 == 0:
                break

    if menu == 4:
        while True:
            print("""
                [0] Volver al menu principal
                [1] Realizar una compra
                [2] Realizar una venta""")
            
            opcion4 = int(input("Que accion desea realizar: "))
            while  opcion2 not in (0,1,2) :
                opcion2 = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))
            if opcion4 == 1:
                pass
            if opcion4 == 2:
                pass
            if opcion4 == 0:
                break
            pass

    