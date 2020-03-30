#Autor: Guadalupe Iveth Serrano Hernández
#Descripción: Lee la base mayor, la base menor y la altura
#de un trapecio isósceles e imprime el área y el perímetro.

def calcularArea(B, b, h):
    area = (B + b)/2*h
    return area

def calcularPerimetro(B, b, h, c):
    perimetro = 2*c + B + b
    return perimetro

def main():
    baseMayor = int(input("Escribe la base mayor: "))
    baseMenor = int(input("Escribe la base menor: "))
    altura = int(input("Escribe la altura: "))
    hipotenusa = int(input("Escribe la hipotenusa: "))
    
    area = calcularArea (baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura, hipotenusa)
    
    print ("el área es %.2f" % area, "cm2")
    print ("el perimetro es %.2f" % perimetro, "cm")
    
main()
