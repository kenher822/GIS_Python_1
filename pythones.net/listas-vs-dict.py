#!/usr/bin/env python
#-*- codign: utf-8 -*-
#
# sin titulo.py
#
# Copyright 2019 root <root@debian>

ListaFemeninos = []
ListaMasculinos = []

Nombres =['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel', 'Alejandro', 'Leonel', 'Antonio', 'Omar',
'Antonia', 'Amalia', 'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

for nombre in Nombres:
    if nombre[-1] == 'a' or nombre[-1] == 'e':
        ListaFemeninos.append(nombre)
    else:
        ListaMasculinos.append(nombre)

print("La lista de nombres femeninos es: ",ListaFemeninos)
print("----------------------------------------------------")
print("La lista de nombres masculinos es: ", ListaMasculinos)