while True:
    print("1. Convertir a mayúsculas")
    print("2. Convertir a minúsculas")
    print("3. Cambiar mayúsculas por minúsculas y viceversa")
    print("4. Mostrar solo vocales")
    print("5. Mostrar en reversa")
    print("6. Salir")

    entrada = int(input("Selecciona una opción (1-6): "))

    if entrada == 1:
        nombre = input("Escribe tu nombre: ")
        print(mayusculas(nombre))
    elif entrada == 2:
        nombre = input("Escribe tu nombre: ")
        print(minusculas(nombre))
    elif entrada == 3:
        nombre = input("Escribe tu nombre: ")
        print(swapcase(nombre))
    elif entrada == 4:
        nombre = input("Escribe tu nombre: ")
        print(vocales(nombre))
    elif entrada == 5:
        nombre = input("Escribe tu nombre: ")
        print(reves(nombre))
    elif entrada == 6:
        print("Adiós")
        break
    else:
        print("La opción no existe. Por favor, selecciona una opción válida.")
