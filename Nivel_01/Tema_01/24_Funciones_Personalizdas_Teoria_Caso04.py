# Funciones Personalizadas
# Las funciones personalizadas en Python admiten argumentos en su llamada, ademas permiten devolver valores.
# Estas posibilidades permiten crear funciones utiles y facilmente reutilizadas

# def nombreFuncion(parametros)
# codigo
# codigo

# Caso 04: Funcion con parametros arbitrarios: def funcion (*lista) por convencion (*args)

# Definir funcion

def media(*lista):
    total=0
    for i in lista:
        total += i
    media = total/len(lista)        
    return media

# Declarar variables
a, b, c,d,e = 5, 3, 5,8,10

# Asignar a una variable la funcion
resultado = "La media aritmetica es: " + str(media(a,b,c,d,e))

print resultado