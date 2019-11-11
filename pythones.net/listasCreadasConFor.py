#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# sin titulo.py
#
# Copyright 2018 https://pythones.net
#

Nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel', 'Alejandro', 'Leonel', 'Antonio', 'Omar',
           'Antonia', 'Amalia', 'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

# Creamos la lista de los femeninos
ListaFemininos = [nombre for nombre in Nombres if nombre[-1]
                  == 'a' or nombre[-1] == 'e']

# Creamos la lista de los masculinos
ListaMasculinos = [nombre for nombre in Nombres if nombre[-1]
                   != 'a' or nombre[-1] != 'e']

print("La lista de nombres femeninos es: ", ListaFemininos)
print("----------------------------------------------------")
print("La lista de nombres masculinos es: ", ListaMasculinos)
