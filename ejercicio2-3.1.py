puntuacion = float(input("Introduzca la puntuación: "))

if puntuacion == 0.0:
    print("Su nivel es: Inaceptable")
    recompensa = puntuacion * 2400
    print("Esta es su recompensa",recompensa,"€.")
elif puntuacion == 0.4:
    print("Su nivel es: Aceptable")
    recompensa = puntuacion * 2400
    print("Esta es su recompensa",recompensa,"€.")
elif puntuacion >= 0.6:
    print("Su nivel es: Meritorio")
    recompensa = puntuacion * 2400
    print("Esta es su recompensa",recompensa,"€.")
else:
    print("Esa puntuación no se contempla")


