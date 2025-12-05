def pedir_kilometros():
    kilometros = float(input("cuantos kilometros pasan a millas:"))
    return kilometros
def hacer_calculo(kilometros):
    millas = 0.621371 * kilometros
    return millas
def mostrar_resultado(millas):
    print ("sus kilometros en millas son:" + str(millas))
    
#*********************codigo principal*********************
kilometros = pedir_kilometros()
millas = hacer_calculo(kilometros)
mostrar_resultado(millas)
