def comprobarNumeroCaracteres(nombre_usuario):
    if len(nombre_usuario) < 6:
        return "El nombre de usuario debe contener al menos 6 caracteres"
    elif len(nombre_usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres"
    else:
        return None

def comprobarAlfanumerico(nombre_usuario):
    if nombre_usuario.isalnum():
        return None
    else:
        return "El nombre de usuario puede contener solo letras y números"

def validarNombreUsuario(nombre_usuario):
    longitud_resultado = comprobarNumeroCaracteres(nombre_usuario)
    alfanumerico_resultado = comprobarAlfanumerico(nombre_usuario)

    if longitud_resultado:
        return longitud_resultado
    elif alfanumerico_resultado:
        return alfanumerico_resultado
    else:
        return "El nombre de usuario es correcto"

# Ejemplos de uso:
nombre_usuario = input("Ingrese su nombre de usuario: ")
resultado_validacion = validarNombreUsuario(nombre_usuario)
print(resultado_validacion)


while not comprobarNumeroCaracteres(nombre) or not comprobarAlfanumerico(nombre):
    nombre = input("Introduce el nombre de usuario: ")



if comprobarNumeroCaracteres(nombre) and comprobarAlfanumerico(nombre):
    print("El nombre es valido")
else:
    print("El nombre no es válido")
