def pedir_numeros_enteros():
    num1 = float(input("digite un numero entero:"))
    num2 = float(input("digite un numero entero:"))
    return num1,num2
def hacer_division_entero(num1,num2):
    cociente = num1 // num2 
    return cociente
def imprimir_resultado(cociente):
    print ("el cociente de la division entera es:" + str(cociente))

#***************codigo principal*****************
num1,num2 = pedir_numeros_enteros()
cociente = hacer_division_entero(num1,num2)
imprimir_resultado(cociente)    