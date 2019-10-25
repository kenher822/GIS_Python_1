# Funciones Personalizadas
# Las funciones personalizadas en Python admiten argumentos en su llamada, ademas permiten devolver valores.
# Estas posibilidades permiten crear funciones utiles y facilmente reutilizadas

# def nombreFuncion(parametros)
# codigo
# codigo

# Caso 03: Funcion con parametros en variables

# Definir funcion

def media(a, b):
    media = (a + b)/2
    msg = "La media aritmetica de " + str(a) + " y " + str(b) + " es: "+ str(media)    
    return msg

# Declarar variables
a = 5
b = 12

# Asignar a una variable la funcion
resultado = media(a,b)

print resultado