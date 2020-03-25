#Autor: Michelle Ojeda Manjarrez
# Calcular los datos de pago semanal de un trabajador

def calcularPagoNormal (horasNormales, pagoHora):
    pago = horasNormales * pagoHora
    return pago

def calcularPagoExtra (horasExtra, pagoHora):
    extra = (pagoHora * .65 + pagoHora) * horasExtra
    return extra

def main ():
    normal = float (input ("Teclea las horas normales trabajadas: "))
    extra = float (input ("Teclea las horas extras trabajadas: "))
    hora = float (input ("Teclea el pago por hora: "))
    
    normalPago = calcularPagoNormal (normal,hora)
    extraPago = calcularPagoExtra (hora, extra)
    totalPago = normalPago + extraPago
    
    print ("Pago normal: $%.02f" % normalPago)
    print ("Pago Extra: $%.02f" % extraPago)
    print ("Pago total: $%.02f" % totalPago)
    
main()
    
    
            
                   
    

