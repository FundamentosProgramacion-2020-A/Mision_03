#José Manuel Rivera Sosapavón
#Boletos

#Calcula el balor de los boletos
def calcularPago(boletosA, boletosB, boletosC):
    boletosA = boletosA * 3250
    boletosB = boletosB * 1730
    boletosC = boletosC * 850
    totalPago = boletosA + boletosB + boletosC
    return totalPago

def main():
    numA = float(input("Número de boletos en zona A:"))
    numB = float(input("Número de boletos en zona B:"))
    numC = float(input("Número de boletos en zona C:"))
    boletos = calcularPago (numA, numB, numC)
    
    print ("El costo total es:$ %.2f" % (boletos))
    
main()
    
    
    
    