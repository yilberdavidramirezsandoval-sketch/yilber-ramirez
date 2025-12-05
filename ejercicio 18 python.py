def dar_valor_lado():
    valor_lado = 8
    return valor_lado
def dar_apotema():
    apotema = 3.5
    return apotema
def calcular_perimetro(valor_lado):
    perimetro = 6*valor_lado
    return perimetro
def calcular_area_hexagono_regular(perimetro,apotema):
    area = (perimetro*apotema)/2
    return area
def imprimir_datos(valor_lado,apotema):
    mensaje = "el valor_lado es"+valor_lado
    mensaje = "el apotema es"+apotema
def imprimir_resultado(resultado_area):
    print ("el area del hexagono regular es:" + str(resultado_area))
    
#*********************codigo principal***************
valor_lado = dar_valor_lado()
apotema =dar_apotema()
perimetro = calcular_perimetro(valor_lado)
area = calcular_area_hexagono_regular(perimetro,apotema)
resultado_area = imprimir_resultado(area)
    