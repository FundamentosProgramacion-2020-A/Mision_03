#Autor: Valeria Huerta Pedregal
#Calcular área y perímetro de un trapecio

def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor)*altura)/2
    return area

def calcularPerimetro(baseMayor, baseMenor, altura):
    perimetro = baseMayor+baseMenor+(((altura**2)+((baseMayor-baseMenor)/2)**2)**(1/2))*2
    return perimetro

def main():
    
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    
    print("Área: %.2f" % area)
    print("Perímetro: %.2f" % perimetro)
    
main()