def comprobarNumeroCaracteres(nombre):
    if len(nombre)<6:
        print("El nombre de usuario debe contener al menos 6 caracteres.")
        return False
    elif len(nombre)>12:
        print("El nombre de usuario no puede contener más de 12 caracteres.")
        return False
    else:
        return True

def comprobarAlfanumerico(nombre):
    if nombre.isalnum() == True:
        return True
    else:
        print("El nombre de usuario puede contener solo letras y números")
        return False

nombre = input("Introduce el nombre de usuario: ")

while not comprobarNumeroCaracteres(nombre) or not comprobarAlfanumerico(nombre):
    nombre = input("Introduce el nombre de usuario: ")

print("El nombre de usuario es correcto")


