#Mariana Ponce Gonzàlez
#Ejercicio de trapecio

#La entrada seran las horas trabajadas y el pago por hora
def calcularpago(horastrabajadas, pagoxhora):
#calcula el pago
    pago = horastrabajadas * pagoxhora
#Los datos de salida seran el pago
    return pago

#La entrada seran las horas trabajadas y el pago por hora
def calculextra(horastrabajadas, pagoxhora):
#calcula el pago extra
    extra = ((horastrabajadas * pagoxhora)*.65)+(horastrabajadas * pagoxhora)
#Los datos de salida seran el pago extra
    return extra

def main():
    h = int(input("Teclea las horas normales trabajadas "))
    p = int(input("Teclea las horas extras trabajadas "))
    e = int(input("Teclea lael pago por hora "))
    t = calcularpago(h,e)
    te = calculextra(e, p)
    to = t + te
    
    print("El pago normal es %.2f " % (t))
    print("El pago extra es %.2f " % (te))
    print("El pago total %.2f " % (to))
    
main()