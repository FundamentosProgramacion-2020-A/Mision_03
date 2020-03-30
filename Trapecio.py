# Autor: Fernando Pérez González
# Calcular área y perímetro de un trapecio isósceles 

def calcularArea(baseMayor, baseMenor, altura) : #encuentra el área del trapecio
    area = ((baseMayor + baseMenor)/2)*altura
    return area

def calcularPerimetro(baseMayor, baseMenor, altura) : #encuentra el perímetro del trapecio 
    x = (baseMayor - baseMenor)/2                     #encuentra la longitud del lado con solo las bases y la altura
    lado = ((altura**2) + (x**2))**(1/2)
    perimetro = baseMayor + baseMenor + (lado*2)
    return perimetro

def main() :
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)
    
main()
