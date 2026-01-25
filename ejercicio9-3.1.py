fechaIntroducida = input("Introduce una fecha con este formato DD/MM: ")
fechaSeparada = fechaIntroducida.split("/")
fechaNumero = [int(x) for x in fechaSeparada]

if (fechaNumero[0]>=1 and fechaNumero[0]<=31) and (fechaNumero[1]>=1 and fechaNumero[1]<=12) and (fechaNumero[1]==2 and fechaNumero[0]<=28 and fechaNumero[0]>=1) == True:
    if (fechaNumero[1] == 3 and fechaNumero[0] >= 21) or (fechaNumero[1] == 4 and fechaNumero[0] <= 20):
        print("Tu signo es Aries")
    elif (fechaNumero[1] == 4 and fechaNumero[0] >= 21) or (fechaNumero[1] == 5 and fechaNumero[0] <= 20):
        print("Tu signo es Tauro")
    elif (fechaNumero[1] == 5 and fechaNumero[0] >= 21) or (fechaNumero[1] == 6 and fechaNumero[0] <= 21):
        print("Tu signo es Géminis")
    elif (fechaNumero[1] == 6 and fechaNumero[0] >= 22) or (fechaNumero[1] == 7 and fechaNumero[0] <= 23):
        print("Tu signo es Cáncer")
    elif (fechaNumero[1] == 7 and fechaNumero[0] >= 24) or (fechaNumero[1] == 8 and fechaNumero[0] <= 23):
        print("Tu signo es Leo")
    elif (fechaNumero[1] == 8 and fechaNumero[0] >= 24) or (fechaNumero[1] == 9 and fechaNumero[0] <= 23):
        print("Tu signo es Virgo")
    elif (fechaNumero[1] == 9 and fechaNumero[0] >= 24) or (fechaNumero[1] == 10 and fechaNumero[0] <= 22):
        print("Tu signo es Libra")
    elif (fechaNumero[1] == 10 and fechaNumero[0] >= 23) or (fechaNumero[1] == 11 and fechaNumero[0] <= 22):
        print("Tu signo es Escorpio")
    elif (fechaNumero[1] == 11 and fechaNumero[0] >= 23) or (fechaNumero[1] == 12 and fechaNumero[0] <= 21):
        print("Tu signo es Sagitario")
    elif (fechaNumero[1] == 12 and fechaNumero[0] >= 22) or (fechaNumero[1] == 1 and fechaNumero[0] <= 20):
        print("Tu signo es Capricornio")
    elif (fechaNumero[1] == 1 and fechaNumero[0] >= 21) or (fechaNumero[1] == 2 and fechaNumero[0] <= 19):
        print("Tu signo es Acuario")
    elif (fechaNumero[1] == 2 and fechaNumero[0] >= 20) or (fechaNumero[1] == 3 and fechaNumero[0] <= 20):
        print("Tu signo es Piscis")
else:
    print("La fecha no es válida")



