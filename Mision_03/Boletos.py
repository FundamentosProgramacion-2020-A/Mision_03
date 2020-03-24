# Autor: Daniel Rojas, A01376572
# Calcular el costo total de boletos de diferentes precios

def calcularPago(boletosA, boletosB, boletosC) : #Calcula el costo total de los boletos
    totalPago = boletosA*3250 + boletosB*1730 + boletosC*850
    return totalPago

def main() :
    numeroBoletosA = int(input("Número de boletos en zona A: "))
    numeroBoletosB = int(input("Número de boletos en zona B: "))
    numeroBoletosC = int(input("Número de boletos en zona C: "))
    total = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.2f" % (total))
    
main()