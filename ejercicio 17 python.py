def pedir_libras():
    libras = float(input("digite cuasntas libras va a pasar a kilogramos:"))
    return libras
def hacer_calculo(libras):
    kilogramos = libras * 0.453592
    return kilogramos
def mostrar_resultado(kilogramos):
    print ("las libras en kilogramos son :" + str(kilogramos))
        
#****************codigo principal********************

libras = pedir_libras()
kilogramos = hacer_calculo(libras)
mostrar_resultado(kilogramos)