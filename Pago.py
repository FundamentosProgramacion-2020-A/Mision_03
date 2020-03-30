#Autor: Valeria Huerta Pedregal
#Calcular el pago semanal de un trabajador

def pagoNormal(horas,pagoHora):
    pago = horas*pagoHora
    return pago

def pagoExtra(horasExtra,pagoHora):
    pagoBono = horasExtra*pagoHora*1.65
    return pagoBono

def main():
    horas = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    pagoNormal1 = pagoNormal(horas,pagoHora)
    pagoExtra1 = pagoExtra(horasExtra,pagoHora)
    pagoTotal = pagoNormal(horas,pagoHora) + pagoExtra(horasExtra,pagoHora)
    
    print("")
    print("Pago normal: $%.2f" % pagoNormal1)
    print("Pago extra: $%.2f" % pagoExtra1)
    print("-----------------------")
    print("Pago total: $%.2f" % pagoTotal)
    
main()
