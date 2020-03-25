#Autor: Michelle Ojeda Manjarrez
# Calcular el total a pagar de unos boletos con diferentes precios


#Definir función calcular pago
def calcularPago (boletosA, boletosB, boletosC) :
    totalPago = boletosA*3250 + boletosB*1730 + boletosC*850
    return totalPago

#Programa inicial
def main ():
    numeroBoletosA = int (input ("Número de boletos en zona A: "))
    numeroBoletosB = int (input ("Número de boletos en zona B: "))
    numeroBoletosC = int (input ("Número de boletos en zona C: "))
   
    boletos = calcularPago (numeroBoletosA, numeroBoletosB, numeroBoletosC)        #Se usa la función calcular pago con los datos que ingreso el usuario
    
    print ("El costo total es : $%.02f"  % boletos)
    
    
main ()