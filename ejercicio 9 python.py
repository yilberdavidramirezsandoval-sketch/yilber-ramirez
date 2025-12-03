def recibir_datos():
    base_mayor=float(input("digite el valor de la base mayor:"))
    base_menor=float(input("digite el valor de la base menor:"))
    altura = float (input("digite el valor de la altura:"))
    return base_mayor,base_menor,altura

def calcular_area(base_mayor,base_menor,altura):
    area = ((base_mayor + base_menor)/2)*altura
    return area

def mostrar_resultado(area):
    print("el area del trapecio es:",area)
    
#****************codigo principal*****************+

base_mayor,base_menor,altura=recibir_datos()
area=calcular_area(base_mayor,base_menor,altura)
resultado_area= mostrar_resultado(area)