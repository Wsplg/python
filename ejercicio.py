cadena = input("Introduce una cadena: ")
separado = cadena.split(" ")
listaCadena = []

for i in separado:
    mayus = i.capitalize()
    guardarCadena = listaCadena.append(mayus)
    cadenaCapital = " ".join(listaCadena)

print(cadenaCapital)
