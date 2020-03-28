# Sharone Márquez, A01746940
# Calcular el pago de un trabajador

# Define una función
def calcularPN(horas, pago):
    pagoNormal= horas * pago
    return pagoNormal

# Define una función
def calcularPE(horasE, pago):
    pagoExtra= ((pago*1.65) * horasE)
    return pagoExtra

# PROGRAMA PRINCIPAL
def main():
    n= int(input("Teclea las horas normales trabajadas: "))
    e= int(input("Teclea las horas extras trabajadas: "))
    p= int(input("Teclea el pago por hora: "))
    
    pagoNormal= calcularPN(n, p) # Usa la primera función
    pagoExtra= calcularPE(e, p) # Usa la segunda función
    pagoTotal= calcularPN(n, p) + calcularPE(e, p) # Usa la primera y segunda función
    
    print('''Pago normal: $%.2f
Pago extra: $%.2f
Pago Total: $%.2f''' % (pagoNormal, pagoExtra, pagoTotal))

main()

        