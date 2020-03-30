#Autor: Anayansi Alexia Tafoya Soto
#Programar función para calcular la compra de boletos.

def calcularPago(boletosA, boletosB, boletosC) :
    #Calcula y guarda en la variable totalPago el total a pagar
    totalPago = (boletosA*3250) + (boletosB*1730) + (boletosC*850)
    return totalPago

def main() :
    #numeroBoletosA
    BoletosA = int (input ("Número de boletos en Zona A: "))
    #numeroBoletosB
    BoletosB = int (input ("Número de boletos en Zona B: "))
    #numeroBoletosC
    BoletosC = int (input ("Número de boletos en Zona C: "))
    
    #Llama a función
    totalBoletos = calcularPago (BoletosA, BoletosB, BoletosC)
    
    #Imprimir
    print ("El costo total es: $%.2f" % (totalBoletos))
    
#Llamar a función main
main()