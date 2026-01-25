TreintaUnoDias = ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]
TreintaDias = ["abril", "junio", "septiembre", "noviembre"]
VeinteOcho = ["febrero"]

mes = input("Escribe un mes del año para saber sus dias: ")
sinFormato = mes.lower()

if sinFormato in TreintaUnoDias:
    print("El mes tiene 31 días.")
elif sinFormato in TreintaDias:
    print("El mes tiene 30 días.")
elif sinFormato in VeinteOcho:
    print("El mes tiene 28 días.")
