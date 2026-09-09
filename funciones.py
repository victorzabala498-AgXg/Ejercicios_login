USUARIO_ADMIN = "admin"
CLAVE_ADMIN = "123"
USUARIO_COMUN = "Victor"
CLAVE_COMUN = "abc"

def verificar_credenciales(u, c):
    try:
        if u == USUARIO_ADMIN and c == CLAVE_ADMIN:
            return "ADMINISTRADOR"
        if u == USUARIO_COMUN and c == CLAVE_COMUN:
            return "USUARIO"
        
        return "ERROR"
        
    except Exception as e:
        return f"ERROR_SISTEMA: {e}" 