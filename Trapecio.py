#Autor: Michelle Ojeda Manjarrez
# Calcular el área y el perimetro de un trapecio iscóceles

def calcularArea (baseMayor, baseMenor, altura):
    area = (baseMayor + baseMenor)/2 * altura
    return area

def calcularPerimetro (baseMayor, baseMenor, altura):
    perimetro = (baseMenor + baseMayor + 2*altura)
    return perimetro

def main ():
    B = int (input ("Escribe la longitud de la base mayor: "))
    b = int (input ("Escribe la longitud de la base menor: "))
    a = int (input ("Escribe la longitud de la altura: "))
    
    trianguloArea = calcularArea (B, b, a)
    trianguloPerimetro = calcularPerimetro (B, b , a)
    
    print ("Área: %.02f" % trianguloArea)
    print ("Perímetro: %.02f" % trianguloPerimetro)
    
main ()
