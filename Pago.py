# Autor: Paloma Cueto
# Calcular los datos de pago semanal de un trabajador

def CalcularPagoNormal (pagoNormal, pagoPorHora):
    normal = pagoNormal * pagoPorHora
    return normal

def CalcularPagoExtra (horasExtra,pagoPorHora):
    extra = horasExtra * ((pagoPorHora*.65) + pagoPorHora)
    return extra

def main ():
    pagoNormal = int (input ("Teclea las horas normales trabajadas: "))
    horasExtra = int (input ("Teclea las horas extras trabajadas: "))
    pagoPorHora = int (input ("Teclea el pago por hora: "))
    
    pagoNormal = CalcularPagoNormal(pagoNormal, pagoPorHora)
    pagoExtra = CalcularPagoExtra(horasExtra, pagoPorHora)
    pagoTotal = pagoNormal + pagoExtra
    
    print ("Pago normal: $%.2f " % (pagoNormal))
    print ("Pago extra: $%.2f" % (pagoExtra))
    print (" -------------------------------")
    print ("Pago total: $%.2f" % (pagoTotal))
    
main ()    