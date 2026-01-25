cadena = input("Vamos a sustuir los espacios, escribe algo: ")
separador = cadena.split(" ")
listaGuardada = []
for i in separador:
    nuevaCadena = listaGuardada.append(i)
    guion = "-".join(listaGuardada)
print(guion)

