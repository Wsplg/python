def comprobarMinimoCaracteres(contraseña):
    if len(contraseña)<8:
        return False
    else:
        return True
def comprobarMayusculas(contraseña):
    for i in contraseña:
        if i.isupper():
            return True
    return False
def comprobrarMinusculas(contraseña):
    for i in contraseña:
        if i.islower():
            return True
    return False
def comprobrarNumeros(contraseña):
    for i in contraseña:
        if i.isnumeric():
            return True
    return False
def comprobarAlfanumerico(contraseña):
    for i in contraseña:
        if not i.isalnum():
            return True
    return False
def comprobarEspaciosEnBlanco(contraseña):
    espacio = " "
    for i in contraseña:
        if espacio in i:
            return False
    return True

contraseña = input("Introduce la contraseña: ")
while not comprobarMinimoCaracteres(contraseña) or not comprobarMayusculas(contraseña) or not comprobrarMinusculas(contraseña) or not comprobrarNumeros(contraseña) or not comprobarAlfanumerico(contraseña) or not comprobarEspaciosEnBlanco(contraseña):
   print("La contraseña elegida no es segura")
   contraseña = input("Introduce la contraseña: ")

print("La contraseña elegida es segura")
