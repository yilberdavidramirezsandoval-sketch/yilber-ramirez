def pedir_numero():
    numero = float(input("digite el numero:"))
    return numero
def hacer_calculo(numero):
    raiz = numero ** 0.5
    return raiz
def mostrar_resultado(raiz):
    print("la raiz del numero es." + str(raiz))
    
#****************codigo principal*****************

numero = pedir_numero()
raiz = hacer_calculo(numero)
mostrar_resultado(raiz)