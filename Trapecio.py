#Autor: Samara Andrea Vega
#Leer la base mayor, base menor y altura de un trapecio isósceles y calcular posteriormente área y perímetro

def calcularArea(B,b,h):
    area=(B + b)/2*h
    return area

def calcularPerimetro (B, b, h, c):
    perimetro: 2*c + B + b
    return perimetro

def main():
    baseMayor =int(input("Escribe la base mayor:"))
    baseMenor =int(input("Escribe la base menor:"))
    altura =int (input("Escribe la altura: "))
    hipotenusa =int(input("Escribe la hipotenusa "))
    
    area=calcularArea(baseMayor,baseMenor,altura)
    perimetro = calcularPerimetro (baseMayor,baseMenor,altura,hipotenusa)
    
    print ("El área del trapecio es %.2f" %area, "cm2")
    print ("El perímetro es %.2f" %perimetro, "cm")
    
main()
    
    