#!/usr/bin/env python
#-*- coding: utf-8 -*-
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

L1 = ['María', 'Juan', 'Pedro'] # Listas con los nombre
LEdades = [14,16,18] # Lista con las edades
diccionario = (dict(zip(L1,LEdades))) # Creamos un diccionario fusionando con zip()
print(diccionario,"\n")

#################################################################################################
'''
Iterando diccionarios: claves o valores, y ambas con bucle for
Podemos iterar un diccionario para obtener solo las claves, los valores o ambos a la vez. 
Primeramente aclararte que puedes utilizar el método keys(), values() como hemos visto en 
métodos de los diccionarios que nos facilitaran la iteracion de un único elemento clave, 
o valor. O para ambos podemos utilizar el método items().
Iterando las claves de un diccionario
'''

semaforo = {'Rojo': 'Detenerso', 'Amarillo':'Despacio','Verde':'Avance'}
colores = semaforo.keys()
for color in colores:
    print(color, "\n")

