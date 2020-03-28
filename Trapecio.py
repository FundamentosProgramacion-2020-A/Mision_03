# Sharone Márquez, A01746940
# Calcular el área y perímetro de un Trapecio

# Define una función
def calcularArea(baseMayor, baseMenor, altura):
    area= (baseMayor+baseMenor)*altura/2
    return area

# Define una función
def calcularPerimetro(baseMayor, baseMenor, altura):
    catetoA= (baseMayor - baseMenor)/2
    c= ((catetoA**2) + (altura**2))**0.5
    perimetro= c*2 + baseMayor + baseMenor
    return perimetro

# PROGRAMA PRINCIPAL
def main():
    B= int(input("Escribe la longitud de la base mayor: "))
    b= int(input("Escribe la longitud de la base menor: "))
    a= int(input("Escribe la altura: "))
    
    area= calcularArea(B, b, a) # Usa la primera función
    perimetro= calcularPerimetro(B, b, a) # Usa la segunda función
    
    print ('''Área: %.2f
Perímetro: %.2f''' % (area, perimetro))
    
main()
    
    
     
