# Funciones Personalizadas
# Las funciones personalizadas en Python admiten argumentos en su llamada, ademas permiten devolver valores.
# Estas posibilidades permiten crear funciones utiles y facilmente reutilizadas

# def nombreFuncion(parametros)
# codigo
# codigo

# Caso 05: Funcion con multiples condicionales (http://www.ditutor.com/estadistica/desviacion_estandar.html)

# Definir funcion

def media_desviacion(*lista):
    total=0
    for i in lista:
        total += i
    media = total/len(lista)
    total = 0
    for i in lista:
        total+=(i-media)**2
        desviacion = (total/len(lista))**0.5
    return media, desviacion

# Declarar variables
a,b,c,d,e,f,g = 2,4,6,8,10,20,30

# Asignar a una variable la funcion
resultadoM, resultadoD = media_desviacion(a,b,c,d,e,f,g)


print "La media es: " + str(resultadoM)
print "La desviacion es: " + str(resultadoD)