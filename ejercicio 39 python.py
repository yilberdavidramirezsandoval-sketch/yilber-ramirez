def pedir_numeros():
    num1 = float(input("digite el primer numero:"))
    num2 = float(input("digite el segundo numero:"))
    return num1,num2
def hacer_calculo(num1,num2):
    promedio = (num1+num2)/2
    return promedio
def imprimir_resultado(promedio):
    print("el promedio es:" + str(promedio))

#*********codigo principal**************
num1,num2 = pedir_numeros()
promedio = hacer_calculo(num1,num2)
imprimir_resultado(promedio)