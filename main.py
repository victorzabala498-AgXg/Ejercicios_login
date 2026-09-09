import funciones
import administrador
import usuario
try:
    u = input ("Usuario:")
    c = input ("Contraseña:")
    rol = funciones.verificar_credenciales(u, c)
    if rol == "ADMINISTRADOR":
        print ("Bienvenido Admin")
        administrador.ejecutar_sistema_admin()
    elif rol == "USUARIO" :
        print("Bienvenido usuario")    
        usuario.ejecutar_sistema_usuario()

    else:
         print ("Datos incorrectos.")    
except Exception as e:  
      print("Ocuurio un error al ejecutar el programa:",e)   