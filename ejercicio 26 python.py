def pedir_numeros():
    num1 = float(input("digite un numero:"))
    num2 = float(input("digite un numero:"))
    return num1,num2

def hacer_division(num1,num2):
    residuo = num1 // num2
    return residuo

def imprimir_resultado(residuo):
    print("el residuo de la division es:"+str(residuo))

#************codigo principal*************
num1,num2 = pedir_numeros()
residuo = hacer_division(num1,num2)
imprimir_resultado(residuo)