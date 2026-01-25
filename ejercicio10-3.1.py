numero = int(input("Introduzca un número entero: "))

for i in range(1,numero + 1):
    fila = ""
    numeroMaximo = (2*i)-1
    for j in range(1,i+1):
        contador = 2*(j-1)
        fila = fila+str(numeroMaximo-contador)
    print(fila)


