#Kathia Alejandra Cervantes López
#Este programa calcula el total a pagar por una compra de boletos en diferentes zonas para un concierto.

def calcularPago(zonaA, zonaB, zonaC):
    #Multiplicación de número de boletos por el costo
    totalPago = (zonaA*3250) + (zonaB*1730) + (zonaC*850)
    return totalPago

def main ():
    zonaA= int(input("Número boletos de la 'Zona A' con costo de $3250: "))
    zonaB= int(input("Número boletos de la 'Zona B' con costo de $1730: "))
    zonaC= int(input("Número boletos de la 'Zona C' con costo de $850: "))

    totalPago = calcularPago(zonaA, zonaB, zonaC)
    print("El total a pagar es: $%.02f" % (totalPago))

#Llamar programa principal
main ()