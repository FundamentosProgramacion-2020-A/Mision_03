#Autor: Michelle Ojeda Manjarrez
# Calcular el área y el perímetro de un trapecio isóceles


#Definir función calcular área
def calcularArea (baseMayor, baseMenor, altura):
    area = (baseMayor + baseMenor)/2 * altura
    return area

#Definir función calcular perímetro
def calcularPerimetro (baseMayor, baseMenor, altura):
    perimetro = ((((((baseMayor-baseMenor)/2)**2) + (altura**2))**0.5) * 2) + (baseMayor+baseMenor)
    return perimetro

#Programa inicial
def main ():
    B = int (input ("Escribe la longitud de la base mayor: "))
    b = int (input ("Escribe la longitud de la base menor: "))
    a = int (input ("Escribe la altura: "))
    
    trianguloArea = calcularArea (B,b,a)                      #Se usa la función calcular área con los datos que ingreso el usuario
    trianguloPerimetro = calcularPerimetro (B,b,a)            #Se usa la función calcular perímetro con los datos que ingreso el usuario
    
    print ("Área: %.02f" % trianguloArea)
    print ("Perímetro: %.02f" % trianguloPerimetro)
    
main ()
