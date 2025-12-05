def pedir_base():
    base = float(input("digite el valor de la base del prisma triangula:"))
    return base
def pedir_altura():
    altura = float(input("digite el valor de la altura del prisma triangular:"))
    return altura
def pedir_ancho():
    ancho = float(input("digite el valor del ancho del prisma triangula:"))
    return ancho 

def calcular_area_base(base,altura):
    area_base = (base*altura)/2
    return area_base
def calcular_volumen(area_base,altura):
    volumen = area_base*altura
    return volumen
def imprimir_datos(base,altura,ancho):
    mensaje = "la base es:"+base
    mensaje = "la altura es:"+altura
    mensaje = "el ancho es"+ancho
    
def imprimir_resultado(resultado_volumen):
    print ("el volumen del prima triangular es: " + str(resultado_volumen))
    
#*************************codigo principal*********************

base = pedir_base()
altura = pedir_altura()
ancho = pedir_ancho()
area_base = calcular_area_base(base,altura)
volumen = calcular_volumen(area_base,altura)
resultado_volumen = imprimir_resultado(volumen)