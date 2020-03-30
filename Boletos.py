#Autor: Valeria Huerta Pedregal
#Calcular pago total de boletos para un concierto


def calcularPago(boletosA, boletosB, boletosC):
    #Calcula y guarda en la variable totalPago el total a pagar
    totalPago = (boletosA*3250)+(boletosB*1730)+(boletosC*850)
    #Regresa totalPago
    return totalPago

def main():
    #numeroBoletosA = Leer el número de boletos en zona A
    #numeroBoletosB = Leer el número de boletos en zona B
    #numeroBoletosC = Leer el número de boletos en zona C
    boletosA = int(input("Número de boletos en zona A: "))
    boletosB = int(input("Número de boletos en zona B: "))
    boletosC = int(input("Número de boletos en zona C: "))
    #Llama a la función calcularPago, envía como argumentos los valores leídos. Guarda el resultado.
    totalPago = calcularPago(boletosA, boletosB, boletosC)
    #Imprimir el resultado

    print("El costo total es $%.2f " % totalPago)

main()

    