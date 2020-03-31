# Miguel Castillo Ordaz
# Programa que calcula el pago de un trabajador.

def calcularPagoNormal(horasNormales, horasExtra, pagoHora):
    pagoNormal = horasNormales*pagoHora
    return pagoNormal

def calcularPagoExtra(horasNormales, horasExtra, pagoHora):
    pagoExtra = ((pagoHora*0.65)+pagoHora)*horasExtra
    return pagoExtra

def calcularPagoTotal(horasNormales, horasExtra, pagoHora):
    pagoTotal = (horasNormales*pagoHora)+(((pagoHora*0.65)+pagoHora)*horasExtra)
    return pagoTotal

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    
    pagoNormal= calcularPagoNormal(horasNormales, horasExtra, pagoHora)
    pagoExtra = calcularPagoExtra(horasNormales, horasExtra, pagoHora)    
    pagoTotal= calcularPagoTotal(horasNormales, horasExtra, pagoHora)
     
    print("                                          ")
    print("Pago normal: ",'$%.2f'% round(pagoNormal,2))
    print("Pago extra: ",'$%.2f'% round(pagoExtra,2))
    print("-----------------------")
    print("Pago total: ",'$%.2f'% round(pagoTotal,2))

main()
