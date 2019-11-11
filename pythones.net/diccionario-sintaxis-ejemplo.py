# Creando un diccionario usando dict
dict((x, x * x) for x in (1,2,3,4))

# Para imprimirlo
print(dict(x,x*x) for x in (1,2,3,4))

# Almacenarlo e imprimirlo
ss = (dict((x,x*x) for x in (1,2,3,4)))
print (ss)

# Sintaxis
# dict(<clve>, <valor> for <elemento> in <iterable>)

