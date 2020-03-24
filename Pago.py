#Autor: Michelle Ojeda Manjarrez
# Calcular los datos de pago semanal de un trabajador

def pagoNormal (horasNormales, pagoHora):
    pago = horasNormales * pagoHora
    return pago

def pagoExtra (horasExtra, pagoHora):
    extra = (pagoHora * .65 + pagoHora) * horasExtra
    return extra

def main ():
    normal = float (input ("Teclea las horas normales trabajadas: "))
    extra = float (input ("Teclea las horas extras trabajadas: "))
    hora = float (input ("Teclea el pago por hora: "))
    
    normalPago = pagoNormal (normal,hora)
    extraPago = pagoExtra (hora, extra)
    totalPago = normalPago + extraPago
    
    print ("Pago normal: $%.02f" % normalPago)
    print ("Pago Extra: $%.02f" % extraPago)
    print ("Pago total: $%.02f" % totalPago)
    
main()
    
    
            
                   
    

