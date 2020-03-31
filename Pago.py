#Autor: Elena R.Tovar, A01376318
#Calcular el pago semanal de un trabajador, contando horas extra (65% más)
#Leer horas normales, extras, y pago por hora.
#Imprimir pago normal + extra y total

#calcula precio por hora normal
def calcPN(hn,ph):
    pn=hn*ph
    return pn
#calcula precio por hora extra
def calcPE(he, ph):
    pe=he*(ph*1.65)
    return pe
#calcula precio total
def calcT(pe, pn):
    pt= (pe+pn)
    return pt
    
def main():
    hn= float(input("Teclea las horas normales trabajadas: "))
    he= float(input("Teclea las horas extras trabajadas: "))
    ph= float(input("Teclea el pago por hora: "))
    pn= calcPN(hn,ph)
    pe= calcPE(he, ph)
    pt= calcT(pe, pn)
    print("Pago normal: $%0.2f" %(pn))
    print("Pago extra: $%0.2f" %(pe))
    print("-------------------------")
    print("Pago total: $%0.2f" %(pt))
main()