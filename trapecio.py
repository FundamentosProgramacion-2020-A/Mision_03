#Autor: Alondra Miranda Aguilera A01746742
#Area y perímetro del trapecio

import math

def calcularArea(baseMayor,baseMenor,altura): #Calcula es área
    area = ((baseMayor+baseMenor)*altura)/2
    return area
    
def calcularPerimetro(baseMayor, baseMenor,altura): #Calcula el perímetro
    cachito = (baseMayor-baseMenor)/2
    ladoquefalta = math.sqrt(cachito**2)+(altura**2)
    perimetro = (2*ladoquefalta)+baseMenor+baseMayor
    return perimetro

def main(): #Pregunta bases y áreas, hace el cálculo y las imprime
    baseMayor = int(input("Escribe la base mayor: "))
    baseMenor = int(input("Escribe la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor,baseMenor,altura)
    perimetro = calcularPerimetro(baseMayor,baseMenor,altura)
    print("Área: ", area)
    print("Perímetro: ", perimetro)
    
main()