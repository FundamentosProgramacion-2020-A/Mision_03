#José Manuel Rivera Sosapavón
#Trapecio

#Calcula el area del trapecio
def calcularArea(baseMayor, baseMenor,altura):
    area = ((baseMayor+baseMenor)/2)*altura
    return area

#Calcula el perimetro del trapecio
def calcularPerimetro(baseMayor, baseMenor,altura):
    basetriangulo = baseMayor - baseMenor
    hipotenusa = ((basetriangulo**2) + (altura**2))**.5
    perimetro = 2*(hipotenusa) + baseMayor + baseMenor
    return perimetro

def main ():
    bMayor = float(input("Escribe la longitud de la base mayor:"))
    bMenor = float(input("Escribe la longitud de la base menor:"))
    H = float(input("Escribe la altura:"))
    Area = calcularArea(bMayor, bMenor, H)
    Perimetro = calcularPerimetro (bMayor, bMenor, H)
    
    print ("Area: %.2f" % (Area))
    print ("Perimetro: %.2f" % (Perimetro))
    
main()
    
    
    
    
