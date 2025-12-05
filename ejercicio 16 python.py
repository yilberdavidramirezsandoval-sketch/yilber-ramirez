def pedir_lado():
    lado = float(input("digite la longitud del lado:"))
    return lado
def calcular_volumen(lado):
    volumen = lado**2
    return volumen
def mostrar_resultado(resultado_volumen):
    print("el volumen del cubo es:" + str(resultado_volumen))
    
#*******************codigo principal**************

lado = pedir_lado()
volumen = calcular_volumen(lado)
mostrar_resultado (volumen)