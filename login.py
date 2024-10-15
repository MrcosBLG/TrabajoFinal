def login():
    
    usuario = input('Escribe tu usuario =>')
    usuario_valido = 'ucel123'
    
    while usuario!= usuario_valido: 
        usuario= input("usuario incorrecto, intente con un usuiario valido: ")
        
    if usuario  in usuario_valido:
        print('usuario valido, puedes continuar')
 
    contraseña = input('ingresa tu contrasena =>')
    contraseña_valida = "123"
   
    while contraseña != contraseña_valida:
        contraseña = input("la contraseña es incorrecta, intente con una contraseña valida: ")
   
    if contraseña == contraseña_valida:
        print('usuario valido')
    else:
        print("usuario invalido, intente denuevo")
if __name__ == "__main__":
    login()

