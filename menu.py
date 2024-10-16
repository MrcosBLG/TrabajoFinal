
from login import login

if __name__ == "__main__":
    if login():
        pass
    else:
        login()
menu = 0
print("---------------------------------------------------------------------------------------------------------------------------------------------------")
print("Acciones del menu ")
print("""
[1] Editar o modificar el inventario 
[2] Historial de movimientos 
[3] Ver informe de stock actual """)
print("---------------------------------------------------------------------------------------------------------------------------------------------------")
menu = int(input("Que accion desea realizar: "))
while  menu not in (1,2,3) : 
    menu = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))
    #EDITAR O MODIFICAR EL INVENTARIO 
if menu == 1:
    print("""
          [1] Ingresar productos al inventario 
          [2] Buscar productos 
          [3] Ver productos agotados 
          [4] Modificar prodictos """)
    opcion1 = int(input("Que accion desea realizar: "))
    while  opcion1 not in (1,2,3,4) : 
        opcion1 = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))
        if opcion1 == 1:
            pass
        if opcion1 == 2:
            pass
        if opcion1 == 3:
            pass
        if opcion1 == 4:
            pass
    
    #Historial de movimientos
if menu == 2 :
    print("""
          [1] Cantidad de ventas realizadas
          [2] Producto mas vendido
          [3] Producto menos vendido""")
    opcion2 = int(input("Que accion desea realizar: "))
    while  opcion2 not in (1,2,3) :
        opcion2 = int(input("No existe opcion para ese numero dentro del menu, porfavor introduzca un numero  compatible: "))
    if opcion2 == 1:
            pass
    if opcion2 == 2:
            pass
    if opcion2 == 3:
        pass
    

if menu == 3 :
    pass



#productos=[]
#productos_agotados=[]
#productos_en_stock=[]
#ventas=[]
#ingresa_productos=[]
#extraer_priductos=[]
