def mayusculas(nombre):
    mayus = nombre.upper()
    return mayus
def minusculas(nombre):
    minus = nombre.lower()
    return minus
def swapcase(nombre):
    swapcase = nombre.swapcase()
    return swapcase
def vocales(nombre):
    a = (nombre.replace("a","1"))
    e = (a.replace("e","2"))
    i = (e.replace("i","3"))
    o = (i.replace("o","4"))
    u = (o.replace("u","5"))
    return u
def reves(nombre):
    return nombre[::-1]
print("Opción 1: Tu nombre en mayúsculas")
print("Opción 2: Tu nombre en minúsculas")
print("Opción 3: Tu nombre intercambiando mayúsculas y minúsculas")
print("Opción 4: Las vocales de tu nombre en números")
print("Opción 5: Tu nombre al reves")
print("Opción 6: Salir")
while True:
    entrada = int(input("Elige: "))
    match entrada:
        case 1:
            nombre = input("Escribe tu nombre: ")
            print(mayusculas(nombre))
        case 2:
            nombre = input("Escribe tu nombre: ")
            print(minusculas(nombre))
        case 3:
            nombre = input("Escribe tu nombre: ")
            print(swapcase(nombre))
        case 4:
            nombre = input("Escribe tu nombre: ")
            print(vocales(nombre))
        case 5:
            nombre = input("Escribe tu nombre: ")
            print(reves(nombre))
        case 6:
            print("Adiós")
            break
        case _:
            print("La opción no existe")
