#Paulina Mendoza Iglesias
#Programa que hace el cálculo sobre el pago de un trabajador

# Función que calcula el pago por horas normales
def calcularHorasNormales(horasNormales, pagoHora):
    hora = horasNormales * pagoHora
    return hora

# Función que calcula el pago por horas extras
def calcularHorasExtra (horasExtras, pagoHora):
    porcentageExtra = (pagoHora * .65) + pagoHora
    horaExtra = horasExtras * porcentageExtra
    return horaExtra
    
# Función principal que corre el programa 
def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    
    pagoNormal = calcularHorasNormales (horasNormales, pagoHora)
    pagoExtra = calcularHorasExtra (horasExtras, pagoHora)
    pagoTotal = pagoNormal + pagoExtra
    
    
    print("Pago normal: $%.2f " % (pagoNormal))
    print("Pago extra: $%.2f" % (pagoExtra))
    print("-----------------------")
    print("Pago total: $%.2f" % (pagoTotal))
    

main() 