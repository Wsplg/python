numero = int(input("Introduzca un número entero: "))
contador = 0

while numero<=1:
    numero = int(input("Introduzca un número mayor que uno: "))

if numero>1:
    for i in range(2,numero):
        mod = numero % i
        if mod == 0:
            contador += 1
    if contador == 0:
        print("El número es primo.")
    else:
        print("El número no es primo.")
