# Autor: Mariana Mejía Béjar, A01374862
# Calcular precio de boletos en diferentes áreas del Auditorio Nacional


def calcularPago(boletosA, boletosB, boletosC) :
      # Calcula el total que se debe pagar por todos los boletos
    totalPago = boletosA*3250 + boletosB*1730 + boletosC*850
    return totalPago
    
def main ():
    # Define el programa principal
    numeroBoletosA = int(input("Número de boletos en la Zona A: "))
    numeroBoletosB = int(input("Número de boletos en la Zona B: "))
    numeroBoletosC = int(input("Número de boletos en la Zona C: "))
    
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    
    print("El costo total es: $%.2f" % totalPago)

    
# Llamar al programa principal
main ()

