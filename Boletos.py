#Autor: Guadalupe Iveth Serrano Hernández
#Descripción: Calcular pago que recibe como parámetros el número
#de boletos que se quiere comprar para cada zona y regresa el total
#a pagar.

def calcularPago(boletosA, boletosB, boletosC):
    totalPago = boletosA*3250 + boletosB*1730 + boletosC*850
    return totalPago

def main ():
    numeroBoletosA = int(input("¿Cuántos boletos en zona A requiere? "))
    numeroBoletosB = int(input("¿Cuántos boletos en zona B requiere? "))
    numeroBoletosC = int(input("¿Cuántos boletos en zona C requiere? "))
    
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    
    print ("El costo total es de %.2f" % totalPago, "pesos")

main()