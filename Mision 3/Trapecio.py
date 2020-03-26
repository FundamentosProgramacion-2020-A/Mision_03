# Autor: Patricio León
# Calcula el área y perimetro de un trapecio

def calcularArea(baseMayor, baseMenor, altura):
    areaFormula = (baseMayor + baseMenor)/2*altura
    return areaFormula

def calcularPerimetro(baseMayor, baseMenor, altura):
    perimetroFormula = (baseMayor + baseMenor) + ((((((baseMayor-baseMenor)/2)**2) + (altura**2))**0.5)*2)
    return perimetroFormula
    
def main ():
    baseMayor = float(input("Escribe la longitud de la base mayor: "))
    baseMenor = float(input("Escribe la longitud de la base menor: "))
    altura = float(input("Escribe la altura: "))
    
    areaFinal = calcularArea(baseMayor, baseMenor, altura)
    perimetroFinal = calcularPerimetro(baseMayor, baseMenor, altura)
    
    print ("Área: %.02f" % (areaFinal))
    print ("Perimetro: %.02f" % (perimetroFinal))

main ()
