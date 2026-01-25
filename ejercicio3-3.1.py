edad = int(input("Introduzca la edad del cliente: "))

if edad < 4:
    print("Puede entrar gratis")
elif edad in range(4,19):
    print("Debe pagar 5€")
else:
    print("Debe pagar 10€")
