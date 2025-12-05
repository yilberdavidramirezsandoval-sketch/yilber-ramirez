def pedir_numero():
    num = int(input("digite un numero:"))
    return num
def hacer_calculo(num):
    num_cuadrado = num ** 2
    return num_cuadrado
def mostrar_resultado(num_cuadrado):
    print("el num_cuadrado del numeros es:" + str(num_cuadrado))
    
#*******************codigo principal****************
num = pedir_numero()
num_cuadrado = hacer_calculo(num)
mostrar_resultado(num_cuadrado)