ingredientesVeg = ["Pimiento", "Tofu"]
ingredientesNoVeg = ["Pepperoni", "Jamón", "Salmón"]
pizza = ["Tomate", "Mozarella"]

opcion = input("Elige, vegetariana o no vegetariana: ")

if opcion == "vegetariana":
    print("Ingredientes disponibles:",ingredientesVeg)
    ingredienteElegido = input("Elige uno: ")
elif opcion == "no vegetariana":
    print("Ingredientes disponibles:",ingredientesNoVeg)
    ingredienteElegido = input("Elige uno: ")

pizza.append(ingredienteElegido)

for i in pizza:
    if i in ingredientesVeg:
        print("Tu pizza es vegetariana")
    elif i in ingredientesNoVeg:
        print("Tu pizza no es vegetariana")

print(f"{pizza}")
