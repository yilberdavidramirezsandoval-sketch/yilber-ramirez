def pedir_num_horas():
    num_horas = float(input("digite el numero de horas que va a pasar a minutos:"))
    return num_horas
def hacer_calculo(num_horas):
    minutos = num_horas * 60
    return minutos
def imprimir_resultado(minutos):
    print ("las horas a minutos son:" + str(minutos))

#************codigo principal***********
num_horas = pedir_num_horas()
minutos = hacer_calculo(num_horas)
imprimir_resultado(minutos)

