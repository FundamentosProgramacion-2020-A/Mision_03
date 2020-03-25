#Autor: Andy (Dino) Martínez Hernández, A01376720
#Funciones para precio de boletos de distintas zonas

#Función para calcular el pago, multiplicación del precio, suma de los totales, totalPago
def calculoPago(boletosA, boletosB, boletosC):
    PrecioA= boletosA*3250
    PrecioB= boletosB*1730
    PrecioC= boletosC*850
    
    totalPago= PrecioA+PrecioB+PrecioC
    return totalPago

#Función principal para pedir el número de boletos y hacer le calculo con la otra función
def main():
    boletosA= int(input("Teclee el número de boletos para la ZONA A que va a comprar:"))
    boletosB= int(input("Teclee el número de boletos para la ZONA B que va a comprar:"))
    boletosC= int(input("Teclee el número de boletos para la ZONA C que va a comprar:"))
    
    pagoFinal= calculoPago (boletosA, boletosB, boletosC)
    print ("El precio total de sus boletos es de: $", pagoFinal, "MXN.")

#Ahora si a llamar a la función principal

main()