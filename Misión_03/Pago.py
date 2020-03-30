#Autor: Anayansi Alexia Tafoya Soto
# Calcular el pago de un trabajador

#Función que calcula el pago normal por hora
def calcularNormal(normal, pagoH):
    pagoNormal = normal * pagoH
    return pagoNormal

#Función que calcula el pago extra (65% más)
def calcularExtra (pagoH, extra):
    pagoExtra = pagoH * extra * 1.65
    return pagoExtra

#Función principal
def main ():
    hora = int (input ("Teclea las horas normales trabajadas: "))
    extra = int (input ("Teclea las horas extra trabajadas: "))
    pago = int (input ("Teclea el pago por hora: "))
    
    #LLama a función
    pagoNormal = calcularNormal (hora, pago)
    pagoExtra = calcularExtra (extra, pago)
    pagoTotal = pagoNormal + pagoExtra
    
    #Imprimir
    print ("Pago normal: $%.2f" % pagoNormal)
    print ("Pago extra: $%.2f" % pagoExtra)
    print ("----------------------------------")
    print ("Pago total: $%.2f" % pagoTotal)
    
#Llamar a función main
main ()