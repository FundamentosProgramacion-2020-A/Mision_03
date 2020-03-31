#Autor: Elena R. Tovar, A01376318
#Cuántos boletos quiere comprar por cada zona(3 de diferentes precios)
#Imprimir precio total

#calcula precio de boletos en area c
def calczC(numC):
    precioC= numC*850
    return precioC
#calcula precio de boletos en area a
def calczA(numA):
    precioA= numA*3250
    return precioA
#calcula precio de boletos en area b
def calczB(numB):
    precioB= numB*1730
    return precioB
#calcula total a pagar
def calctotal(numA, numB, numC):
    total= calczA(numA)+calczB(numB)+calczC(numC)
    return total

def main():
    numA= int(input("Número de boletos en zona A: "))
    numB= int(input("Número de boletos en zona A: "))
    numC= int(input("Número de boletos en zona A: "))
    total=calctotal(numA, numB, numC)
    print("El costo total es: $%0.2f" %(total))
    
    
main()