#Autor: Andy (Dino) Martínez Hernández, A01376720
#Funcion para sacar área y perímetro del trapecio usando B, b y h

#Función 1, para calcular pago normal
def PagoNor (hrsNormal, hraPago):
    pagoN= hrsNormal*hraPago
    return pagoN

#Función 2, para calcular pago de horas extra
def PagoEx (hrsNormal, hrsExtra, hraPago):
    pagoE= hrsExtra*(hraPago+(hraPago*.65))
    return pagoE

#Función main, para pedir horas normales, extra, pago por hora, y sacar el pago semanal
def main():
    HrsNormal= int (input("Ingresa las horas normales trabajadas en la semana: "))
    HrsExtra= int (input("Ingresa las horas extra trabajadas en la semana: "))
    Pagohra= float (input("Ingresa el pago por hora en $MXN: "))
    
    pagoNormal= PagoNor (HrsNormal, Pagohra)
    pagoExtra= PagoEx (HrsNormal, HrsExtra, Pagohra)
    
    PagoSemanal= pagoNormal+pagoExtra
    
    print ("""Pago normal: $%.02f MXN.
Pago extra: $%.02f MXN
----------------------
Pago Semanal: $%.02f MXN""" % (pagoNormal, pagoExtra, PagoSemanal))
    
#Llamar a función main
main()