#José Manuel Rivera Sosapavón
# Pago

#Calcula el pago normal del trabajador
def calcularPagoNormal(horas, sueldo):
    pago = horas * sueldo
    return pago
#Calcula el apgo por horas extra
def calcularPagoExtra (horas, sueldo):
    pagoExtra = (horas * sueldo) *1.65
    return pagoExtra

def main ():
    
    horasnor = float(input("Teclea las horas normales trabajadas:"))
    horasextra = float(input("Teclea las horas extras trabajadas: "))
    pagohora = float(input("Teclea el pago por hora: "))
    pagonormal = calcularPagoNormal(horasnor, pagohora)
    pagoextra = calcularPagoExtra(horasextra, pagohora)
    
    print ("Pago Normal: $%.2f" % (pagonormal))
    print ("Pago Extra: $%.2f" % (pagoextra))
    print ("-----------------------------")
    pagototal = pagonormal + pagoextra
    print ("Pago Total: 4%.2f" % (pagototal))
    
    
main ()


    