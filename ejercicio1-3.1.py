edad = int(input("¿Qué edad tienes? "))
ingresos = float(input("¿Cuáles son tus ingresos? "))

if edad<=16:
    print("Usted no tiene la edad necesaria para tributar")
elif ingresos < 1000:
        print("Usted no tiene que tributar")
elif ingresos >= 1000:
        print("Usted tiene que tributar")




