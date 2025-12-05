def pedir_datos():
    num1 = int(input("digite un num1 para la division:"))
    num2 = int(input("digite un num2 para la division:"))
    return num1,num2
def calculo_division(num1,num2):
    divi = num1 / num2
    return divi
def mostrar_resultado(divi):
    print("la divi de los dos numeros es:" + str(divi))
    
#*******************codigo principal****************
num1,num2 = pedir_datos()
divi = calculo_division(num1,num2)
mostrar_resultado(divi)