#Autor: Ana Martinez Garcia
# Calcular el perímetro y el área de un trapecio, dando altura y bases

def CalcularArea (baseMayor, baseMenor, altura):
    area = (baseMayor + baseMenor)/2 * altura
    return area

def CalcularPerimetro (baseMayor, baseMenor, altura):
    
    cateto= (baseMayor-baseMenor)/2
    hipotenusa = (cateto**2 + altura**2)**0.5
    
    perimetro= baseMayor + baseMenor + 2*hipotenusa
    
    return perimetro

def main ():
    
    BM = int (input ("Escribe Base Mayor: "))
    bm = int (input ("Escribe Base Menor: "))
    a = int (input ("Escribe la altura: "))
    
    TrapecioA = CalcularArea (BM,bm,a)
    TrapecioP = CalcularPerimetro (BM,bm,a)
    
    print ("El Área del trapecio es: %.02f" % TrapecioA)
    print ("El Perímetro del trapecio es: %.02f" % TrapecioP)
    
main()