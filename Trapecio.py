#Autor: Elena R.Tovar, A01376318
#Calcular área y perímetro midiendo base mayor, base menor y altura de trapecio isóceles
import math
#calcula area
def calcArea(ba,bb,h):
    a=((ba+bb)/2)*h
    return a
#calcula hipotenusa
def hipotenusa(ba,bb,h):
    hip= math.sqrt((h**2)+(((ba-bb)/2)**2))
    return hip
#calcula perimetro  
def calcPerimetro(ba, bb,h):
    P=ba+bb+(2*(hipotenusa(ba,bb,h)))
    return P

def main():
    ba= float(input("Escribe la longitud de la base mayor: "))
    bb= float(input("Escribe la longitud de la base menor: "))
    h= float(input("Escribe la altura: "))
    a= calcArea(ba, bb, h)
    P= calcPerimetro(ba,bb,h)
    print("Área: %0.2f" %(a))
    print("Perímetro: %0.2f" %(P))

main()
