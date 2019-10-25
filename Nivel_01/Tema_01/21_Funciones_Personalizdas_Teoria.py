# Funciones Personalizadas
# Las funciones personalizadas en Python admiten argumentos en su llamada, ademas permiten devolver valores.
# Estas posibilidades permiten crear funciones utiles y facilmente reutilizadas

# def nombreFuncion(parametros)
# codigo
# codigo

# Caso 01: Funcion sin parametros


def media():
    media = (a + b)/2
    msg = "La media aritmetica de " + str(a) + " y " + str(b) + " es: "+ str(media)
    print msg
    return

# Llamar a mi funcion
a = 50
b = 5

media()
