def pedir_datos():
    longitud = float (input("digite el valor de la longitud:"))
    ancho = float (input("digite el valor del ancho:"))
    altura = float (input("digite el valor de la altura:"))
    return longitud,ancho,altura


def calcular_area(longitud,ancho,altura):
    area=longitud*ancho*altura
    return area
def mostra_resultado(area):
    print("el area del prisma rectangular es:",area)
    
#*****************codigo principal*******************
longitud,ancho,altura= pedir_datos()
calculo=calcular_area(longitud,ancho,altura)
area = mostra_resultado(calculo)