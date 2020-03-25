#Autor: Michelle Ojeda Manjarrez
# Calcular los datos de pago semanal de un trabajador

#Definir función calcular pago normal
def calcularPagoNormal (horasNormales, pagoHora):
    pago = horasNormales * pagoHora
    return pago

#Definir función calcular pago extra
def calcularPagoExtra (horasExtra, pagoHora):
    extra = (pagoHora * .65 + pagoHora) * horasExtra
    return extra

#Programa inicial
def main ():
    normal = float (input ("Teclea las horas normales trabajadas: "))
    extra = float (input ("Teclea las horas extras trabajadas: "))
    hora = float (input ("Teclea el pago por hora: "))
    
    normalPago = calcularPagoNormal (normal,hora)            #Se usa la función calcular pago normal con los datos que ingreso el usuario
    extraPago = calcularPagoExtra (hora, extra)              #Se usa la función calcular pago extra con los datos que ingreso el usuario
    totalPago = normalPago + extraPago
    
    print ("Pago normal: $%.02f" % normalPago)
    print ("Pago Extra: $%.02f" % extraPago)
    print ("Pago total: $%.02f" % totalPago)
    
main()
    
    
            
                   
    

