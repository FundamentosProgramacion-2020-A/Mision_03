#Autor: Ana Martinez Garcia
# Calcular el costo de boletos para el concierto de Maroma 5 e imprimir el costo total

def calcularPago (boletosA, boletosB, boletosC) :
    totalPago = boletosA*3250 + boletosB* 1730 +  boletosC* 850
    return totalPago


def main ():
    nA= int (input("¿Cuantos boletos en zona A?: "))
    nB= int (input("¿Cuantos boletos en zona B?: "))
    nC= int (input("¿Cuantos boletos en zona C?: "))
    
    boletos = calcularPago (nA, nB, nC)
    
    
    print ("El costo total es: $%.02f" % boletos)
    
    
main ()
    

