#Roberto Sobrado
#Calcular el pago de un trabajador

def calcularPagoNormal (hrsNormal, pagoHrs):
    pago= hrsNormal * pagoHrs
    return pago
    
def calcularPagoExtra(hrsExtras, pagoHrs):
    pago= hrsExtras * (pagoHrs*1.65)
    return pago
    
def main():
    hrsNormal = int(input("¿Cuántas horas trabajaste?"))
    hrsExtras = int(input("¿Cuántas horas extra trabajaste?"))
    pagoHrs = int(input("¿Cuánto cobras por hora?"))
    
    normal = calcularPagoNormal(hrsNormal, pagoHrs)
    extra = calcularPagoExtra(hrsExtras, pagoHrs)
    total = normal + extra
    
    print ("Pago normal: $%.2f" % (normal))
    print ("Pago extra:  $%.2f" % (extra))
    print ("--------------------------")
    print ("Pago total:  $%.2f" % (total))
    
main()