fechaIntroducida = input("Introduce una fecha con este formato DD/MM/YYYY: ")
fechaSeparada = fechaIntroducida.split("/")
fechaNumero = [int(x) for x in fechaSeparada]
if fechaNumero[1] in [4,6,9,11]:
    if fechaNumero[0]<=30 and fechaNumero[0]>0:
        if fechaNumero[2]>0:
            print("La fecha es valida")
            diasRestantes=30-fechaNumero[0]
            print(diasRestantes,"día/s restantes para fin de mes.")
        else:
            print("La fecha no es valida")
    else:
        print("La fecha no es valida")
elif fechaNumero[1] in [1,3,5,7,8,10,12]:
    if fechaNumero[0]<=31 and fechaNumero[0]>0:
        if fechaNumero[2]>0:
            print("La fecha es valida")
            diasRestantes=31-fechaNumero[0]
            print(diasRestantes,"día/s restantes para fin de mes.")
        else:
            print("La fecha no es valida")
    else:
        print("La fecha no es valida")
elif fechaNumero[1] == 2:
    if fechaNumero[0]<=28 and fechaNumero[0]>0:
        if fechaNumero[2]>0:
            print("La fecha es valida")
            diasRestantes=28-fechaNumero[0]
            print(diasRestantes,"día/s restantes para fin de mes.")
        else:
            print("La fecha no es valida")
    else:
        print("La fecha no es valida")
else:
    print("La fecha no es valida")
