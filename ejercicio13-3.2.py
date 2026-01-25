vocales = ["a","e","i","o","u"]

while True:
    caracter = input("Introduce un caracter: ")
    if caracter != " ":
        if caracter in vocales:
            print("VOCAL")
        else:
            print("NO VOCAL")
    print("Para salir escribe un espacio")
    if caracter == " ":
        print("Se termina la comprobación")
        break
