def pedir_litros():
    litros = float(input("digite el numero de litros que va pasar a galones:"))
    return litros
def hacer_calculo(litros):
    galones = litros * 0.264172
    return galones
def imprimir_resultado(galones):
    print ("los litros a galones son:" + str(galones))
    
#*****************codigo principal****************
litros = pedir_litros()
galones = hacer_calculo(litros)
imprimir_resultado(galones)