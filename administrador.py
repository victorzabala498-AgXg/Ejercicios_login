def ejecutar_sistema_admin():
    print("/n--- MENU ADMINISTRADOR---")
    print ("1. Registrar usuario")
    print ("2.  Cerrar sesion")
    try:
      opcion = input("Opcion:  ")
      if opcion == "1":
        print ( "Registrando usuario...")
      else:
        print ("Sesion de Admin cerrada.") 
    except:
       print("Ocurrio un error inesperado en elm sistema.")      
