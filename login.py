def login():
    
    usuario = input('Escribe tu usuario: ')
    usuario_valido = 'ucel123'
    
    while usuario!= usuario_valido: 
        usuario= input("Usuario incorrecto, intente con un usuario valido: ")
        
    if usuario  in usuario_valido:
        print('Usuario valido, puedes continuar')
 
    contraseña = input('Ingresa tu contraseña: ')
    contraseña_valida = "123"
   
    while contraseña != contraseña_valida:
        contraseña = input("La contraseña es incorrecta, intente con otra: ")
        
   
    if contraseña == contraseña_valida:
        print('Usuario valido.')
        return True
    else:
        print("Usuario invalido, intente de nuevo.")
        return False

