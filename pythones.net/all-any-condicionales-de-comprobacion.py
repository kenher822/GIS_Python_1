#!/usr/bin/env python
#-*- codign: utf-8 -*-
#
# sin titulo.py
#
# Copyright 2018 https://pythones.net
#

PeticionNumeritos="Ingrese un número mayor de 5 y menor de 10 \n"
Numeros = []
while True:
    Numerito1 = (int(input(PeticionNumeritos))) # Pedidos número 1
    Numeros.append(Numerito1) # Agregamos número a la lista
    Numerito2 = (int(input(PeticionNumeritos))) # Pedido número 2
    Numeros.append(Numerito2) # Agregamos número a la lista
    Numerito3 = (int(input(PeticionNumeritos))) # Pedido número 3
    Numeros.append(Numerito3)  # Agregamos número a la lista

    print(Numeros) # Imprimimos numeros ingresados

    if all (numero >= 5 and numero <= 10 for numero in Numeros):
        # Comprueba si todos los números cumplen la condición mayo o igual a 5 y menor o igual a 102
        print("Correcto! Los números ingresados son mayor que 5 y menores a 10")
        print("Gracias y hasta pronto")
        break # Rompemos el bucle
    elif any (numero >= 5 and numero <= 10 for numero in Numeros):
        # Comprueba si algún número es mayor a 5 o mayor a 10
        print("Algún número no es correcto")
        Numeros=[] # Reseteamos la lista
        print ("Vuelva a intentarlo")
    else:
        print("Error no has ingresado ningún número mayor a 5 o menor a 10")
        print("Suerte la próxima perdedor, ni siquiera un solo número")
        break # Rompemos el bucle