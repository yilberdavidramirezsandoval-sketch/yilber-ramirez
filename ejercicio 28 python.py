def pedir_base():
    base = float (input("digite la base del triangulo:"))
    return base
def pedir_altura():
    altura = float(input("digite la altura del triangulo:"))
    return altura
def calcular_area(base,altura):
    area = (base*altura)/2
    return area
def imprimir_resultado(area):
    print ("el area del triangulo es:" + str(area))
    
#***************codigo principal*********
base = pedir_base()
altura = pedir_altura()
area = calcular_area(base,altura)
imprimir_resultado(area)