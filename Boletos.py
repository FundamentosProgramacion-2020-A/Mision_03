# Autor: Paloma Cueto
# Calcular el precio total en diferentes áreas de un concierto

def calcularPago(boletosA, boletosB, boletosC):
    #Sacar precio total de # de boletos
    totalPagoA = 3250*boletosA
    totalPagoB = 1730*boletosB
    totalPagoC = 850*boletosC
    totalPago = totalPagoA+totalPagoB+totalPagoC
    return totalPago

def main ():
    boletosA = int (input("Número de boletos en zona A: "))
    boletosB = int (input("Número de boletos en zona B: "))
    boletosC = int (input("Número de boletos en zona C: "))
    
    totalPagar = calcularPago(boletosA,boletosB,boletosC)
    
    print ("El costo total es: $%.2f" % (totalPagar))
    
main ()
    
    