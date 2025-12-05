def pedir_datos():
    num1 = int(input("digite un num1 para la multiplicacion:"))
    num2 = int(input("digite un num2 para la multiplicacio:"))
    return num1,num2
def calculo_multiplicacion(num1,num2):
    mult = num1 * num2
    return mult 
def mostrar_resultado(mult):
    print("la mult de los dos numeros es:" + str(mult))
    
#*******************codigo principal****************
num1,num2 = pedir_datos()
mult = calculo_multiplicacion(num1,num2)
mostrar_resultado(mult)