fechaIntroducida = input("Introduce una fecha con este formato DD/MM/YYYY: ")
fechaSeparada = fechaIntroducida.split("/")
fechaNumero = [int(x) for x in fechaSeparada]
diasMeses = ["vacio",31,28,31,30,31,30,31,31,30,31,30,31]
if fechaNumero[1] in [4,6,9,11]:
    if fechaNumero[0]<=30 and fechaNumero[0]>0:
        if fechaNumero[2]>0:
            print("La fecha es valida")
        else:
            print("La fecha no es valida")
    else:
        print("La fecha no es valida")
elif fechaNumero[1] in [1,3,5,7,8,10,12]:
    if fechaNumero[0]<=31 and fechaNumero[0]>0:
        if fechaNumero[2]>0:
            print("La fecha es valida")
        else:
            print("La fecha no es valida")
    else:
        print("La fecha no es valida")
elif fechaNumero[1] == 2:
    if fechaNumero[0]<=28 and fechaNumero[0]>0:
        if fechaNumero[2]>0:
            print("La fecha es valida")
        else:
            print("La fecha no es valida")
    else:
        print("La fecha no es valida")
else:
    print("La fecha no es valida")

diasRestantes = 0
diasMesRestantes = diasMeses[fechaNumero[1]]-fechaNumero[0]
for i in diasMeses[(fechaNumero[1]+1):]:
    diasRestantes = diasRestantes + i
diasTotales = diasRestantes+diasMesRestantes
print("Falta",diasTotales,"día/s para terminar el año.")


