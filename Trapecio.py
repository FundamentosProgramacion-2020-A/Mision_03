#RobertoSobrado
#Calcular área y perimietro de un trapecio isósceles.

def calcularArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor) / 2) * altura
    return area

def calcularPerimetro(baseMayor, baseMenor, altura):
    b = (baseMayor-baseMenor)/2
    pitagoras = (b**2 + altura**2)**.5
    perimetro = baseMayor + baseMenor + (pitagoras * 2)
    return perimetro

def main():
    baseMayor = int(input("¿Cuánto mide la base mayor de tu trapecio?"))
    baseMenor = int(input("¿Cuánto mide la base menor de tu trapecio?"))
    altura = int(input("¿Cuánto mide la altura de tu trapecio?"))
    
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    
    print ("El área mide: %.2f" % (area))
    print ("El perímetro mide: %.2f" % (perimetro))
    
main()