# Autor: Patricio León
# Calcular el total a pagar de los boletos de un concierto

# Define una función
def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    boletosA = 3250 * numeroBoletosA
    boletosB = 1730 * numeroBoletosB
    boletosC = 850 * numeroBoletosC
    totalPago = boletosA + boletosB + boletosC
    return totalPago

# Programa Inicial
def main() :
    numeroBoletosA = int(input("Cuantos boletos quieres para la zona A?"))
    numeroBoletosB = int(input("Cuantos boletos quieres para la zona B?"))
    numeroBoletosC = int(input("Cuantos boletos quieres para la zona C?"))
    totalPagar = calcularPago (numeroBoletosA, numeroBoletosB, numeroBoletosC)
    
    print ("El costo total es: $%.2f" % (totalPagar))
    
# Programa principal
main ()

