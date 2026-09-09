def ejecutar_sistema_usuario():
    print("n/ ---MENU USUARIO---")
    print ("1.Ver informacion")
    print ("2 Cerrar sesion")
try:
    opcion = input ("Opcion:  ")
    if opcion == "1":
        print ("Mostrando datos del usuario...")
    else:
        print ("Sesion de usuario cerrada" )
except Exception as e:
    print ("Ocurrio un eror en el sitema:",e)