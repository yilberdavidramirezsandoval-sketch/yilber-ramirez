def pedir_datos():
    base = float(input("digite el valor de la base del rectangulo:"))
    altura = float(input("digite el valor de la altura del rectangulo:"))
    return base,altura
def calcular_area(base,altura):
    area = base*altura
    return area
def imprimir_resultado(area):
    print ("el area del rectangulo es:" + str(area))

#***********codigo principal*************
base,altura = pedir_datos()
area = calcular_area(base,altura)
imprimir_resultado(area)