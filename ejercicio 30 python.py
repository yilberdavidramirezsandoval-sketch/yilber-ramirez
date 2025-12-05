def pedir_radio():
    radio = float(input("digite el radio del circulo:"))
    return radio
def dar_pi():
    pi = 3.14
    return pi
def calcular_circunferencia(radio,pi):
    circunferencia = 2*pi*radio
    return circunferencia
def imprmir_resultado(circunferencia):
    print ("la circunferencia del circulo es:" + str(circunferencia))

#*******************codigo principal***************

radio = pedir_radio()
pi = dar_pi()
circunferencia = calcular_circunferencia(radio,pi)
imprmir_resultado(circunferencia)