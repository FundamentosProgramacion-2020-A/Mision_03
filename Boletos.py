#Paulina Mendoza Iglesias
#Programa que devuelve la cantidad a pagar por cierta cantidad de boletos

#Función calcula el pago de acuerdo a la cantidad de boletos en cada zona
def calcularPago(boletosA, boletosB, boletosC):
    numeroBoletosA = boletosA * 3250
    numeroBoletosB = boletosB * 1730
    numeroBoletosC = boletosC * 850
    totalPago = numeroBoletosA + numeroBoletosB + numeroBoletosC
    return totalPago
    

#Función principal
def main():
    boletosA = int(input("Cantidad de boletos en zona A: "))
    boletosB = int(input("Cantidad de boletos en zona B: "))
    boletosC = int(input("Cantidad de boletos en zona C: "))
    totalboletos = calcularPago (boletosA, boletosB, boletosC)
    
    print("El costo total es: $%.2f" % (totalboletos))
    

main() 


    
