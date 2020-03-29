#Paulina Mendoza Iglesias
#Programa que devuelve el área y perímetro de un trapecio

# Función que calcula el área
def calcularArea(baseMayor, baseMenor, altura):
    area = (baseMayor + baseMenor) / 2 * altura
    return area

# Función que calcula el perímetro
def calcularPerimetro (baseMayor, baseMenor):
    perimetro = (baseMayor * 2) + (baseMenor * 2)
    return perimetro 
    
# Función principal que corre el programa 
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    totalarea = calcularArea (baseMayor, baseMenor, altura)
    totalperimetro = calcularPerimetro (baseMayor, baseMenor)
    
    
    print("Área: %.2f " % (totalarea))
    print("Perímetro: %.2f" %(totalperimetro))
    

main() 
