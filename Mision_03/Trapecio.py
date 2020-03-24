# Autor: Daniel Rojas, A01376572
# Calcular área y perímetro de un trapecio

def calcularArea(B,b,h) : #Calcula el área del trapecio
    area = (B+b)*h/2
    return area

def calcularPerimetro(B,b,h) : #Calcula el perímetro del trapecio
    perimetro = B + b + 2*((((B-b)/2)**2)+h**2)**(1/2)
    return perimetro

def main() :
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    a = calcularArea (baseMayor, baseMenor, altura)
    p = calcularPerimetro (baseMayor, baseMenor, altura)
    print("Área: %.2f" % (a))
    print("Perímetro: %.2f" % (p))

#Programa principal
main()