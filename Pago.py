#Autor: Ana Martinez Garcia
# Calcular el pago de un trabajador

def PagoNormal (horasNormales, pagoHora):
    pago = horasNormales * pagoHora
    return pago

def PagoExtra (horasExtra, pagoHora):
    Extra= (pagoHora + pagoHora*.65) * horasExtra
    return Extra
    
def main ():
    
    hNormal = int(input ("Introduce las horas normales que trabajaste: "))
    hExtra = int(input ("Introduce las horas extra que trabajaste: "))
    pago = int(input ("Introduce el pago de hora: "))
    
    PagoN = PagoNormal (hNormal,pago)
    PagoE = PagoExtra (hExtra,pago)
    totalPago = PagoN + PagoE
    
    print ("Pago normal es: $%.2f" % PagoN)
    print ("Pago extra es: $%.2f" % PagoE)
    print ("Pago total es: $%.2f" % totalPago)
     
main ()