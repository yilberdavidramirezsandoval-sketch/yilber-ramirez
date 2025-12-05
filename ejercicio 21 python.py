def pedir_datos():
    num1 = int(input("digite un num1 para la suma:"))
    num2 = int(input("digite un num2 para la suma:"))
    return num1,num2
def calculo_suma(num1,num2):
    suma = num1 + num2
    return suma
def mostrar_resultado(suma):
    print("la suma de los do numeros es:" + str(suma))
    
#*******************codigo principal****************
num1,num2 = pedir_datos()
suma = calculo_suma(num1,num2)
mostrar_resultado(suma)
    