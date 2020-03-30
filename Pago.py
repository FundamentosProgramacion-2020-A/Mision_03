# Autor: Fernando Pérez González
# Calcular el pago de un trabajador

def calcularPagoNormal(horas, pago) : #Calcula el pago de las horas normales
    pagoHoras = horas*pago
    return pagoHoras
    
def calcularPagoExtra(horasExtra, pago) : #Calcula el pago de las horas extra
    pagoHorasExtra = horasExtra*pago + pago*.65*horasExtra
    return pagoHorasExtra

def main() :
    horas = int(input("Teclea las horas normales trabajadas: "))
    horasExtra = int(input("Teclea las horas extra trabajadas: "))
    pago = int(input("Teclea el pago por hora: "))
    pagoHoras = calcularPagoNormal(horas, pago)
    pagoHorasExtra = calcularPagoExtra(horasExtra, pago)
    pagoTotal = pagoHoras + pagoHorasExtra

    print("Pago normal: $%.2f" % pagoHoras)
    print("Pago extra: $%.2f" % pagoHorasExtra)
    print("- - - - - - - - - - - - -")
    print("Pago total: $%.2f" % pagoTotal)
    
main()