#Autor: Alondra Miranda Aguilera
#PagoTrabajadores

def horasNor(horasNormales, pagoPorHora): #Calcula el pago de horas normales
    panor = horasNormales*pagoPorHora
    return panor

def horasEx(pagoPorHora, horasExtras): #Calcula el pago de las horas extra
    x = pagoPorHora*.65
    y = pagoPorHora + x
    paex = y*horasExtras
    return paex

def main(): #Pregunta horas normales, horas extras y el precio por hora; calcula, y luego suma el total.
    horasNormales = int(input("Horas normales: "))
    horasExtras = int(input("Horas extras: "))
    pagoPorHora = int(input("Pago por hora: "))
    paex = horasEx(pagoPorHora, horasExtras)
    panor = horasNor(horasNormales, pagoPorHora)
    print("Pago normal: ", panor)
    print("Pago extra: ", paex)
    pagoTotal = paex + panor
    print("Pago Total: ", pagoTotal)
    
main()
    