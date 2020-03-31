#Mariana Ponce Gonzàlez
#Ejercicio de trapecio

#La entrada seran base mayor y menor
def calcularperimetro(basemayor, basemenor):
#calcula el perimetro
    perimetro = (basemayor + basemenor) / 2
#Los datos de salida seran el perimetro
    return perimetro

#La entrada sera la base mayor, la base menor y la altura
def calculararea(basemayor, basemenor, altura):
#calcula el area
    area = (((basemayor + basemenor) / 2) * altura)
#Los datos de salida sera la base
    return area

def main():
    B = int(input("Dame la base mayor "))
    b = int(input("Dame la base menor "))
    h = int(input("Dame la altura "))
    p = calcularperimetro(B,b)
    a = calculararea(B,b,h)
    
    print("El perimetro es %.2f " % (p))
    print("El area es %.2f " % (a))
    
main()