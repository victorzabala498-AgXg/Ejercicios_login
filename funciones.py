USUARIO_ADMIN = "admin"
CLAVE_ADMIN = "123"
USUARIO_COMUN = "Victor"
CLAVE_COMUN = "abc"
 

def verificar_credenciales(u, c):
    if u == "admin" and c == "123":
        return "ADMINISTRADOR"
    if u == "Victor" and c == "abc":
        return "USUARIO"
    return "ERROR"