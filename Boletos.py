#Autor: Alondra Miranda Aguilera A01746742
#Pago de Boletos para Maroma 5

def CalcularPago(boletosA,boletosB,boletosC): #Calcula el total
    totalPago = (boletosA*3250) + (boletosB*1730) + (boletosC*850)
    return totalPago
 
def main(): #Pregunta numero de boletos de casa zona, calcula e imprime
     boletosA = int(input("¿Cuántos boletos Zona A quieres?"))
     boletosB = int(input("¿Cuántos boletos Zona B quieres?"))
     boletosC = int(input("¿Cuántos boletos Zona C quieres?"))
     totalPago = CalcularPago(boletosA,boletosB,boletosC)
     print("El total a pagar es: ", totalPago, "wuu")
     
main()
        
    
