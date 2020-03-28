# Sharone Márquez, A01746940
# Calcular el precio de la cantidad de boletos que se requieren

# Define una función
def calcularPago(boletosA, boletosB, boletosC):
    totalPago = boletosA*3250 + boletosB*1730 + boletosC*850
    return totalPago

# PROGRAMA PRINCIPAL
def main():
    numeroBoletosA = int(input("Número de boletos en zona A: "))
    numeroBoletosB = int(input("Número de boletos en zona B: "))
    numeroBoletosC = int(input("Número de boletos en zona C: "))
    
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC) # Usa la función
    print ("El costo total es: $%.2f" % (totalPago))
    
main()
    
    