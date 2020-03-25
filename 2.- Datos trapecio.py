#Autor: Andy (Dino) Martínez Hernández, A01376720
#Funcion para sacar área y perímetro del trapecio usando B, b y h

#Función 1, para calcular área del trapecio
def AreaTrapecio (B, b, h):
    Area= (B+b)/2*h
    
    return Area


#Función 2, para calcular el perímetro del trapecio
def PerimetroTrapecio (B, b, h):
    CatetoBase= (B-b)/2
    lado= (CatetoBase**2+h**2)**(1/2)
    
    perimetro = B+b+lado*2
    
    return perimetro

#función main, para pedir Base Mayor, mase menor y altura, y sacar Area y perimetro
def main():
    B= int(input("Inserte la Base mayor del trapecio, usando cm enteros:"))
    b= int(input("Inserte la base menor del trapecio, usando cm enteros:"))
    h= int(input("Inserte la altura del trapecio, usando cm enteros:"))
    
    Area= AreaTrapecio (B, b, h)
    Perimetro= PerimetroTrapecio (B, b, h)
    
    print ("El área del trapecio es de: %.02f cm2. El perímetro es de: %.02f cm" % (Area, Perimetro))
    
#Llamar a la función main para que empieze el programa

main ()
    