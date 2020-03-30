#Autor: Anayansi Alexia Tafoya Soto
#Programa que calcule el area y el perimetro de un trapecio.

#Función para calcular el área del trapecio
def calcularArea (a, b, h):
    area = ((a + b) /2 ) * h
    return area

#Función para calcular el perimetro del trapecio
def calcularPerimetro (a, b, h):
    perimetro = ((((a-b)/2)**2 + h**2)**0.5)*2 + a + b
    return perimetro

#Función principal
def main ():
    baseMayor = int (input ("Escribe la longitud de la base mayor: "))
    baseMenor = int (input ("Escribe la longitud de la base menor: "))
    altura = int (input ("Escribe la altura: "))
    
     #LLama a función
    Area = calcularArea (baseMayor, baseMenor, altura)
    Perimetro = calcularPerimetro (baseMayor, baseMenor, altura)
    
    #Imprimir
    print ("Área: %.2f" % (Area))
    print ("Perimetro: %.2f" % (Perimetro))
    
    
#Llamar a función main
main()
    