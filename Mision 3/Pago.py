# Autor: Patricio León
# Calcula el pago de un trabajador

def calcularPagoNormal(horasNormales, pagoPorHora):
    pagoSemanalNormal = horasNormales * pagoPorHora
    return pagoSemanalNormal

def calcularPagoExtra (horasExtras, pagoPorHora):
    pagoSemanalExtra = (.65 * pagoPorHora + pagoPorHora) * horasExtras
    return pagoSemanalExtra

def main():
    horasNormales = float(input("Teclea las horas normales trabajadas: "))
    horasExtras = float(input("Teclea las horas extras trabajadas: "))
    pagoPorHora = float(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horasNormales, pagoPorHora)
    pagoExtra = calcularPagoExtra (horasExtras, pagoPorHora)
    pagoTotal = pagoNormal + pagoExtra
    
    print ("Pago nomal: $%.2f" % (pagoNormal))
    print ("Pago extra: $%.2f" % (pagoExtra))
    print("-----------------------")
    print ("Pago total: $%.2f" % (pagoTotal))
    
main ()

 