primeraCuota = 10
sumaCuotas = 0

for i in range(1,21):
    if i == 1:
        primeraCuota = 10
        print(f"Mes {i}: {primeraCuota}")
    else:
        primeraCuota = primeraCuota*2
        sumaCuotas = sumaCuotas + primeraCuota
        print(f"Mes {i}: {primeraCuota}€.")

print(f"Todas las cuotas suman un total de {sumaCuotas} €.")



