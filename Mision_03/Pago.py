# Autor: Mariana Mejía Béjar, A01374862
# Calcular el pago que debe recibir un trabajador por un horario normal, el pago por sus horas extras de trabajo
# y el pago total


def calcularPagoNormal(horasNormales, pagoHora) :
    # Calcula cuánto es el dinero que un trabajador debe recibir en un horario normal
    pagoNormal = horasNormales*pagoHora
    return pagoNormal

def calcularPagoExtra(pagoHora, horasExtra) :
    # Calcula cuánto dinero debe recibir un trabajador por sus horas extra de trabajo
    pagoExtra = pagoHora*horasExtra*1.65
    return pagoExtra
    
def main ():
    # Define el programa principal
    normales = int(input("Teclea las horas normales trabajadas: "))
    extra = int(input("Teclea las horas extra trabajadas: "))
    pago = int(input("Teclea el pago por hora: "))
    
    
    pagoNormal = calcularPagoNormal(normales, pago)
    pagoExtra = calcularPagoExtra(pago, extra)
    pagoTotal = pagoNormal+pagoExtra
    
    print(" ")
    print("Pago normal: $%.2f" % pagoNormal)
    print("Pago extra: $%.2f" % pagoExtra)
    print("-----------------------")
    print("Pago total: $%.2f" % pagoTotal)

    
# Llamar al programa principal
main ()


