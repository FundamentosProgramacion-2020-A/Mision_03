#Autor: Samara Andrea Vega
#Realizar compra de boletos y calcular total a pagar

def calcularPago (boletosA, boletosB, boletosC):
    totalPago = boletosA*3250 + boletosB*1730 + boletosC*850
    return totalPago

def main ():
    numeroboletosA =int(input("¿Cuántos boletos requiere en zona A?"))
    numeroboletosB =int(input("¿Cuántos boletos requiere en zona B?"))
    numeroboletosC = int(input("¿Cuántos boletos requiere en zona C?"))
    
    totalPago = calcularPago(numeroboletosA, numeroboletosB, numeroboletosC)
    
    print("El costo total es de %.2f" % totalPago, "pesos MXN")
    
main()
    
