#Autor: Samara Andrea Vega
#Calcular horas normales trabajadas y horas extra, así como el pago por hora y datos de pago semanal

def calcularPagoNormal(horasNormales, pagoHora):
    pagoNormal = horasNormales*pagoHora
    return pagoNormal

def calcularPagoExtra(horasExtra, pagoHora):
    pagoExtra = (pagoHora*.65 + pagoHora)*horasExtra
    return pagoExtra

def calcularPagoTotal(pagoNormal, pagoExtra):
    pagoTotal = pagoNormal + pagoExtra
    return PagoTotal

def main()
