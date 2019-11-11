# lista por extension
"""
Cómo ves el resultado será el mismo, la diferencia es que la 
lista por comprensión fue creada a partir de la propiedad en 
común (ser pares) de los números en rango de 0 a 9 iterandolos
para descartar aquellos que no cumplen la condición de ser
 divisibles por 2 con resto cero.
"""
a = [0, 2, 4, 6, 8]
print("Listas por extensión (a = [0, 2, 4, 6, 8]): ", a)

# lista por compresión.
a = [x for x in range(9) if x % 2 == 0]
print("Lista por compresnsión (a = [x for x in range(9) if x % 2 == 0]): ", a)

# lista de cuadrados
ListaCuadrados = [x**2 for x in range(10)]
#                 <Expresion> for <Element> in <Iterable>
print (ListaCuadrados)