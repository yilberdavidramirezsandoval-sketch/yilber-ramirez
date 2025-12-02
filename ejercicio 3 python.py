def dar_ancho():
    ancho = 18
    return ancho
def dar_longitud():
    longitud = 22
    return longitud
def calcular_area(ancho,longitud):
    area = (ancho * longitud)
    return area
def imprimir_datos(ancho, longitud):
    mensaje = "el ancho es:"+ ancho
    mensaje = "la longitud es:"+ longitud
    
def imprimir_resultado(resultado_area):
    print("el area del rectangulo es :" + str(resultado_area))
    
    
#*******************codigo principal******************
ancho = dar_ancho()
longitud = dar_longitud()
area = calcular_area(ancho,longitud)
resultado = imprimir_resultado(area)