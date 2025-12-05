def pedir_numero():
    num = int(input("digite un numero:"))
    return num
def validar_numero(dato_numero):
    if dato_numero % 2 == 0:
        menasje = "el numero es par"
    else :
        mensaje = "el numero es impar"
        return mensaje
    
def mostrar_resultado(dato_mensaje):
    print ("el numero es :" + str(dato_mensaje))
    
#****************codigo principal************
dato_numero = pedir_numero()
dato_mensaje = validar_numero(dato_numero)
mostrar_resultado(dato_mensaje)