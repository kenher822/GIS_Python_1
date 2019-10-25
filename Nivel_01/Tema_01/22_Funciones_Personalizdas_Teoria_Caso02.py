# Funciones Personalizadas
# Las funciones personalizadas en Python admiten argumentos en su llamada, ademas permiten devolver valores.
# Estas posibilidades permiten crear funciones utiles y facilmente reutilizadas

# def nombreFuncion(parametros)
# codigo
# codigo

# Caso 02: Funcion con parametros


def media(a, b):
    media = (a + b)/2
    msg = "La media aritmetica de " + str(a) + " y " + str(b) + " es: "+ str(media)
    print msg
    return

# Llamar a mi funcion
media(5024,125)