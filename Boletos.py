#Roberto Sobrado
#Total a pagar por boletos.

def calcularBoletosA(numeroBoletosA):
    boletosA = numeroBoletosA * 3250
    return boletosA

def calcularBoletosB(numeroBoletosB):
    boletosB = numeroBoletosB * 1730
    return boletosB

def calcularBoletosC(numeroBoletosC):
    boletosC = numeroBoletosC * 850
    return boletosC

def calcularPago(boletosA, boletosB, boletosC):
    totalPago = boletosA + boletosB + boletosC
    return totalPago

def main():
    numeroBoletosA = int(input("¿Cuántos boletos para la zona A quiere?"))
    numeroBoletosB = int(input("¿Cuántos boletos para la zona B quiere?"))
    numeroBoletosC = int(input("¿Cuántos boletos para la zona C quiere?"))
    boletosA= calcularBoletosA(numeroBoletosA)
    boletosB= calcularBoletosB(numeroBoletosB)
    boletosC= calcularBoletosC(numeroBoletosC)
    total = calcularPago (boletosA, boletosB, boletosC)
    print ("El costo total es: $%.2f" % (total))
    
main()