#Kathia Alejandra Cervantes López
#Este programa calcula el pago semanal de un trabajador incluyendo las horas extras que se pagan 65% más que las normales

def HorasTrabajo (horas, pago):
    #Multiplicación de las horas trabajadas por lo que se paga
    horasDeTrabajo = (pago*horas)
    return horasDeTrabajo

def HorasExtTrabajo (horasExt, pago):
    #Multiplicación de las horas extra trabajadas por 65% más de pago
    horasExtra = ((pago*65/100 + pago) * horasExt)
    return horasExtra

def main () :
    horas = int(input("Teclea las horas normales trabajadas: "))
    horasExt= int(input("Teclea las horas extras trabajadas: "))
    pago = int(input("Teclea el pago por hora: "))
    
    horasDeTrabajo = HorasTrabajo (horas, pago)
    print("El pago de trabajo normal es $%.02f" % (horasDeTrabajo))
    
    horasExtra = HorasExtTrabajo (horasExt, pago)
    print("El pago de trabajo por horas extras es $%.02f" % (horasExtra))
    
    pagoTotal= (horasDeTrabajo + horasExtra)
    print("El pago total es $%.02f" % (pagoTotal))

#Llamar al problema principal
main ()