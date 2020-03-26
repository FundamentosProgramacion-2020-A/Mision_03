#Kathia Alejandra Cervantes López
#Este programa calcula el area y la base de un triángulo isósceles

def areaTrapecio (baseMayor,baseMenor,altura):
    #Fórmula para sacar el área de un trapecio isósceles
    areaTrapecioIso= ((baseMayor+baseMenor) *altura /2)
    return areaTrapecioIso

def perimetroTrapecio (baseMayor, baseMenor, altura):
    #Fórmula para sacar el perímetro del trapecio isósceles
    perimetroTrapecioIso = (baseMayor + baseMenor + (2*altura))
    return perimetroTrapecioIso

def main () :
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    
    areaTrapecioIso = areaTrapecio (baseMayor, baseMenor, altura)
    print("El área del trapecio isósceles es: %.02f" % (areaTrapecioIso))
    
    perimetroTrapecioIso = perimetroTrapecio (baseMayor, baseMenor, altura)
    print("El perímetro del trapecio isósceles es: %.02f" % (perimetroTrapecioIso))
    

#Llamar al los programas  
main ()

