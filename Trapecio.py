# Miguel Castillo Ordaz
# Programa que calcula el area y el perímetro de un trapecio.

import math

def calcularArea(baseMayor, baseMenor, altura):
    area = (baseMenor+baseMayor)*(altura/2)
    return area

def calcularPerimetro(baseMayor, baseMenor, altura):
    perimetro =  baseMenor + math.sqrt(altura**2+((baseMayor-baseMenor)/2)**2)+baseMayor+ + math.sqrt(altura**2+((baseMayor-baseMenor)/2)**2)
    return perimetro

def main():
    baseMayor= int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la estatura: "))
    
    area = calcularArea(baseMayor, baseMenor, altura)
    perimetro = calcularPerimetro(baseMayor, baseMenor, altura)
  
    print("Área: ",'%.2f'% round(area,2))
    print("Perímetro: ",'%.2f'% round(perimetro,2))
    
main()