#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# sin titulo.py
# Copyright 2018 https://pythones.net
#

'''
Función zip() Fusionamos listas y las  convertimos en diccionarios
Para convertir una lista común a una lista de esta manera podemos utilizar la función zip() 
que admite como parámetro un conjunto de listas, veámoslo en un ejemplo fusionando dos listas
para crear un diccionario:
'''

L1 = ['María', 'Juan', 'Pedro']  # Listas con los nombre
LEdades = [14, 16, 18]  # Lista con las edades
# Creamos un diccionario fusionando con zip()
diccionario = (dict(zip(L1, LEdades)))
print(diccionario, "\n")

#################################################################################################
'''
Iterando diccionarios: claves o valores, y ambas con bucle for
Podemos iterar un diccionario para obtener solo las claves, los valores o ambos a la vez. 
Primeramente aclararte que puedes utilizar el método keys(), values() como hemos visto en 
métodos de los diccionarios que nos facilitaran la iteracion de un único elemento clave, 
o valor. O para ambos podemos utilizar el método items().
Iterando las claves de un diccionario
'''

semaforo = {'Rojo': 'Detenerse', 'Amarillo': 'Despacio', 'Verde': 'Avance'}
colores = semaforo.keys()
for color in colores:
    print(color)
print("\n")
'''
Si almacenamos en una variable las claves mediante el método keys obtenemos una vista del 
diccionario que nos permite trabajar solo con las claves y nos presenta la ventaja de que
al cambiar un elemento del diccionario automáticamente se actualizara...
Iterando los valores de un diccionario
'''

acciones = semaforo.values()
for accion in acciones:
    print(accion)
print("\n")

'''
Si almacenamos en una variable los valores mediante el método values obtenemos una vista del
diccionario que nos permite trabajar solo con los valores y nos presenta la ventaja de que 
al cambiar un elemento del diccionario automáticamente se actualizara..
Iterando ambos, claves y valores de un diccionario
'''

# Creamos la variable elementos que almacena la clave(key) y valor (values)
elementos = semaforo.items()
for k, v in elementos:
    # Imprimimos k(key) y su respectivo v(value)
    print((k), ('significa'), (v))
