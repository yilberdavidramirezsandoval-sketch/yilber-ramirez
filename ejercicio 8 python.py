def pedir_datos():
    dolar = float(input("ingrese la cantidad de dinero(USD):"))
    T_cambio = float (input("ingrese la tasa de cambios:"))
    return dolar, T_cambio

def convertir_dolar(dolar,T_cambio):
    euros = dolar * T_cambio
    return euros

def mostrar_convercion(euros):
    print("los dolares(USD)ingresados a euros son:",euros)
    
#******************codigo principal****************

dolar, T_cambio = pedir_datos()
convercion = convertir_dolar(dolar,T_cambio)
resultado = mostrar_convercion (convercion)