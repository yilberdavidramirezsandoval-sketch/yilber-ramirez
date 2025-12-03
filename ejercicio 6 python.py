def pedir_radio():
    radio = float(input("digite el radio del cono:"))
    return radio
def pedir_altura():
    altura = float(input("digite la altura del cono:"))
    return altura
def definir_pi():
    black = float(3.14)
    return black
def calcular_vol(radio,altura,black):
    vol = 0.33 * black * (radio**2) * altura
    return vol
def imprimir_datos(radio,altura):
    mensaje = "el radio del cono es:"+ radio
    mensaje = "la altura de cono es:"+ altura

def imprimir_Resultado(resultado_vol):
    print("el volumen del cono es:" + str(resultado_vol))

#********************codigo principal********************
radio = pedir_radio()
altura = pedir_altura()
vol = calcular_vol(radio,altura,black=3.14)
resultado=imprimir_Resultado(vol)