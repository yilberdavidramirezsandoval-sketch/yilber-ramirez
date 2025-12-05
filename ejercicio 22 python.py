def pedir_datos():
    num1 = int(input("digite un num1 para la resta:"))
    num2 = int(input("digite un num2 para la resta:"))
    return num1,num2
def calculo_resta(num1,num2):
    resta = num1 - num2
    return resta
def mostrar_resultado(resta):
    print("la resta de los dos numeros es:" + str(resta))
    
#*******************codigo principal****************
num1,num2 = pedir_datos()
resta = calculo_resta(num1,num2)
mostrar_resultado(resta)
    