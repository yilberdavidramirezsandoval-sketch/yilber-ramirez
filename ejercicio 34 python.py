def pedir_precio():
    precio = float(input("digite el precio del articulo:"))
    return precio
def calcular_descuento(precio):
    descuento = precio * 0.10
    return descuento
def imprimir_resultado(descuento):
    print ("el descuento del articulo es:" + str(descuento))

#*************codigo principal*****************

precio = pedir_precio()
descuento = calcular_descuento(precio)
imprimir_resultado (descuento)