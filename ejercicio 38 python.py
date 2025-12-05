def pedir_datos():
    num1 =float(input("digite el primer numero:"))
    num2 = float(input ("digite el segundo numero:"))
    return num1,num2
def hacer_calculo(num1,num2):
    mayor = ( num1 + num2 + abs(num1-num2))/2
    return mayor
def mostrar_resultado(mayor):
    print ("el numero mayor es:"+str(mayor))

#************+codigo principal**********+
num1,num2 = pedir_datos()
mayor = hacer_calculo(num1,num2)
mostrar_resultado(mayor)