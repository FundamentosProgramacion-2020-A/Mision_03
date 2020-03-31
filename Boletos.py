# Miguel Castillo Ordaz
# Programa que calcula costo de boletos.

def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    totalPago = numeroBoletosA*3250 + numeroBoletosB*1730 + numeroBoletosC*850
    return totalPago

def main():
    numeroBoletosA = int(input("Número de boletos en zona A: "))
    numeroBoletosB = int(input("Número de boletos en zona B: "))
    numeroBoletosC = int(input("Número de boletos en zona C: "))
    
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
  
    print("El costo total es: ",'$%.2f'% round(totalPago,2))
    
main()