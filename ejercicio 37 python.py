def leer_datos():
    num1 = int(input("digite el primer numero :"))
    num2 = int(input("digite el segundo numero :"))
    return num1,num2
def determinar_multiplo(num1,num2):
    if num1 % num2 == 0:
        resultado = "es multiplo"
    else:
        resultado = "no es multiplo"
    return resultado
def mostrar_resultado(resultado):
    print ("el primer numero" + str(resultado)+"del segundo numero")

#**************codigo principal****************
num1,num2 =leer_datos()
resultado = determinar_multiplo(num1,num2)
mostrar_resultado(resultado)