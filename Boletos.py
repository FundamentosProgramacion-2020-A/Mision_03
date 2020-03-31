#Mariana Ponce Gonzàlez
#Ejercicio de boletos

#nuestra entradas seran los boletoa A, B, C
def calcularPago(boletosA, boletosB, boletosC):
#calcula el total del pago
    totalpago = (3250*boletosA) + (1730*boletosB) + (850*boletosC)
#La salida sera el total del pago
    return totalpago

def main():
    a = int(input("Cuantos boletos A compraste? "))
    b = int(input("Cuantos boletos B compraste? "))
    c = int(input("Cuantos boletos C compraste? "))
    total = calcularPago(a,b,c)
    
    print ("El total de los voletos es %.2f " % (total))
    
main()