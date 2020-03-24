#Autor: Michelle Ojeda Manjarrez
# Calcular el total a pagar de unos boletos con diferentes precios

def calcularPago (boletosA, boletosB, boletosC) :
    totalPago = boletosA*3250 + boletosB*1730 + boletosC*850
    return totalPago

def main ():
    numeroBoletosA = int (input ("¿Cuántos boletos compraste en la zona A?: "))
    numeroBoletosB = int (input ("¿Cuántos boletos compraste en la zona B?: "))
    numeroBoletosC = int (input ("¿Cuántos boletos compraste en la zona C?: "))
   
    boletos = calcularPago (numeroBoletosA, numeroBoletosB, numeroBoletosC)
    
    print ("El costo total es : $%.02f"  % boletos)
    
main ()