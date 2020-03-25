# Autor: Mariana Mejía Béjar, A01374862
# Calcular el área y perímetro de un trapecio isósceles


def calcularArea(a, b, h) :
    # Calcula a través de su respectiva fórmula, el área del trapecio isósceles
    area = (a+b)/2*h
    return area

def calcularPerimetro(a, b, h) :
    # Calcula a través de su respectiva fórmula, el perímetro del trapecio isósceles
    perimetro =  ((((a-b)/2)**2 + h**2)**0.5)*2 + a + b 
    return perimetro
    
def main ():
    # Define el programa principal
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    
    Area = calcularArea(baseMayor, baseMenor, altura)
    Perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
    
    print("Área: %.2f" % Area)
    print("Perímetro: %.2f" % Perimetro)

    
# Llamar al programa principal
main ()


