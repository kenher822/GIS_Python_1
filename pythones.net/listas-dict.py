#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# sin titulo.py
#
# Copyright 2019 root <root@debian>
Nombrevocales = [] 
vocales = ['A','E','I','O','U']
Nombres=['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel', 'Alejandro', 'Leonel', 'Antonio', 'Omar', 'Antonia', 'Amalia', 'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']
# Para el elemento nombre, iteramos la lista nombres
for nombre in Nombres:
    # Si el indice 0 del elemento nombre esta en la lista vocales (Si el nombre inicia con vocal)
    if nombre[0] in vocales:
        # Agregar a la lista nombrevocales
        Nombrevocales.append(nombre)

# Imprimit la lista nombrevocales
print(Nombrevocales)
