
from login import login
from Funciones import agregarproductos, buscar_producto, inventario_stock
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
    [4] Realizar una venta
    """)
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    menu = int(input("Que accion desea realizar: "))
    while  menu not in (0,1,2,3,4) : 
        menu = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))
        #EDITAR O MODIFICAR EL INVENTARIO 
    if menu == 1:
        while True:
            print("""
                [0] Volver al menu principal
                [1] Ingresar productos al inventario 
                [2] Buscar productos 
                [3] Ver productos agotados 
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
                print(3)
                pass
            if opcion1 == 4:
                print(4)
                pass
            if opcion1 == 0:
                break
        
        #Historial de movimientos
    if menu == 2 :
        while True:
            print("""
                [0] Volver al menu principal
                [1] Cantidad de ventas realizadas
                [2] Producto mas vendido
                [3] Producto menos vendido
                """)
            opcion2 = int(input("Que accion desea realizar: "))
            while  opcion2 not in (0,1,2,3) :
                opcion2 = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))
            if opcion2 == 1:
                    pass
            if opcion2 == 2:
                    pass
            if opcion2 == 3:
                pass
            if opcion2 == 0:
                break
        

    if menu == 3 :
        while True:
            print("""
                [0] Volver al menu principal
                [1] Ver informe del stock actual
                [2] Consultar stock de un producto
                """)
            opcion3 = int(input("Que accion desea realizar: "))
            if opcion3 == 1:
                inventario_stock(csvdestock)
            if opcion3 == 2:
                pass
            if opcion3 == 0:
                break

    if menu == 4:
        while True:
            print(4)
            pass

    if menu == 0:
        print(0)
        break

