def pedir_datos():
    dinero = float(input("digite la cantidad de dinero que tiene en su cuenta:"))
    return dinero
def calculo_intereses(dinero):
    intereses = dinero * 0.05
    return intereses
def imprimir_resultado(intereses):
    print ("el 5% de intereses es:" + str(intereses))

#******************codigo principal************************
 
dinero = pedir_datos()
intereses = calculo_intereses(dinero)
imprimir_resultado(intereses)