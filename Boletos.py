# Autor: Fernando Pérez González
# Calcular el total a pagar dependiendo el número de boletos

def calcularPago(boletosA, boletosB, boletosC) : #calcula el pago de los boletos
    pagoA = boletosA*3250
    pagoB = boletosB*1730
    pagoC = boletosC*850
    totalPago = pagoA + pagoB + pagoC
    return totalPago

def main() :
    boletosA = int(input("Número de boletos en zona A: "))
    boletosB = int(input("Número de boletos en zona B: "))
    boletosC = int(input("Número de boletos en zona C: "))
    Pago = calcularPago(boletosA, boletosB, boletosC)
    
    print("El costo total es: $%.2f" % Pago)
    
main()