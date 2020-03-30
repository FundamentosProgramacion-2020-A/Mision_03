#Autor: Guadalupe Iveth Serrano Hernández
#Descripción: Calcula el pago por horas normales, horas extra y
#el pago total de un trabajador. Las horas extra se pagan 65% más
#que las normales.

def calcularPagoNormal(horasNormales, pagoHora):
    pagoNormal = horasNormales*pagoHora
    return pagoNormal

def calcularPagoExtra(horasExtra, pagoHora):
    pagoExtra = (pagoHora*.65 + pagoHora)*horasExtra
    return pagoExtra

def calcularPagoTotal(pagoNormal, pagoExtra):
    pagoTotal = pagoNormal + pagoExtra
    return pagoTotal

def main ():
    
    horasN= int(input("Número de horas normales trabajadas: "))
    horasE = int(input("Número de horas extra trabajadas: "))
    pagoH = int(input("Cantidad de pago por hora: "))
    
    pagoN = calcularPagoNormal (horasN, pagoH)
    pagoE = calcularPagoExtra (horasE, pagoH)
    pagoT = calcularPagoTotal (pagoN, pagoE)
    
    print ("Pago normal: %.2f" % pagoN, "pesos")
    print("Pago extra: %.2f" % pagoE, "pesos" )
    print("Pago total: %.2f" % pagoT, "pesos")
    
main()