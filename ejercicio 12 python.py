def dar_lado1():
    lado1 = 5
    return lado1
def dar_lado2():
    lado2 = 5
    return lado2
def calcular_area(lado1,lado2):
    area = (lado1 * lado2)
    return area
def imprimir_datos(lado1,lado2):
    mensaje = "el lado1 es:"+lado1
    mensaje = "el lado2 es:"+lado2
    
def imprimir_resultado(resultado_area):
    print ("el area del cuadrado es:" + str(resultado_area))
    

#********************codigo principal***********************
lado1 = dar_lado1()
lado2 = dar_lado2()
area = calcular_area(lado1,lado2)
resultado = imprimir_resultado(area)
        
    
    