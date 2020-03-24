# Autor: Daniel Rojas, A01376572
# Calcular el pago de un trabajador

def calcularHoras(horas,pago) : #Calcula el pago por horas normales
    pagoNormal = horas*pago
    return pagoNormal

def calcularExtras(extras,pago) : #Calcula el pago por horas extras
    pagoExtras = extras*(pago+(pago*.65))
    return pagoExtras

def main() :
    h = int(input("Teclea las horas normales trabajadas: "))
    e = int(input("Teclea las horas extras trabajadas: "))
    p = int(input("Teclea el pago por hora: "))
    normal = calcularHoras(h,p)
    extra = calcularExtras(e,p)
    total = normal+extra
    print("""
Pago normal: $%0.2f""" % (normal))
    print("""Pago extra: $%0.2f

Pago total: $%0.2f""" % (extra, total))

#Programa principal
main()
    