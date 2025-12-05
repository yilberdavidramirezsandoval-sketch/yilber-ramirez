def dar_base():
    base = 15
    return base
def dar_altura():
    altura = 20
    return altura
def calcular_area(base,altura):
    area = (base*altura)
    return area
def imprimir_datos(base,altura):
    mensaje = "la base es:"+base
    mensaje = "la altura es:"+altura
def imprimir_resultado(resultado_area):
    print ("el area del paralelograma es:" + str(resultado_area))


#******************codigo principal********************
base = dar_base()
altura = dar_altura()
area = calcular_area(base,altura)
resultado_area = imprimir_resultado(area)    