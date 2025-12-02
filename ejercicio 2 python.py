def dar_radio():
    radio = 10
    return radio

def calcular_volumen(radio):
    volumen = ( 4 * 3.14 * 10)
    return volumen

def imprimir_datos(radio):
    mensaje = "el radio es:"+ radio
    
def imprimir_mensaje(resultado):
    print ("el volumen de la esfera es:" + str(resultado))
    
    
#****************codigo principal**********************
radio = dar_radio()
volumen = calcular_volumen(radio)
resultado = imprimir_mensaje(volumen)
