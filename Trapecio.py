# Autor: Paloma Cueto
# Calcular el área y el perimetro de un trapecio isósceles

def calcularArea (baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor)/2) * altura
    return area

def calcularPerimetro (baseMayor, baseMenor, altura):
    perimetro = baseMayor + baseMenor + ((((((baseMayor-baseMenor)/2)**2)+(altura**2))**.5)*2)
    return perimetro

def main ():
    baseMayor = int (input("Escribe la longitud de la base mayor: "))
    baseMenor = int (input("Escribe la longitud de la base menor: "))
    altura = int (input("Escribre la altura: "))
    
    areaF = calcularArea(baseMayor, baseMenor, altura)
    perimetroF = calcularPerimetro(baseMayor, baseMenor, altura)
    
    print ("Área: %.2f" % (areaF))
    print ("Perímetro: %.2f" % (perimetroF))
    
main ()