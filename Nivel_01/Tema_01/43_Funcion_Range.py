# Paso 01: Importar librerias y declarar variables
import arcpy

# Importar libreria de math(matemáticas)
import math

# Sobreescribir los resultados
arcpy.env.overwrithOutput = True

# Especificar el FC a trabajar ------------> CentralesHidroelectricas
fc = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_14\GDB\Practica.gdb\CentralesHidroelectricas"

# Obtener la informacion tabular del FC ------------> CentralesHidroelectricas
table = arcpy.SearchCursor(fc)

# Crear una variable con el nombre de campo para los intervalos
campoIntervalos = "Intervalos"

# Paso 02: Obtener los registros del campo potencia

# Declarar la lista potencia (vacia)
potencia = []

# Recuperar los valores del campo "Potencia"
for rows in table:
    row = rows.getValue("Potencia")
    potencia.append(row)

# print "Valores del Campo Potencia: " + str(potencia)

# Paso 03.- Calcular el rango

# Calcular el rango - Declaramos variable rango
rango = int(max(potencia)-min(potencia))
# print "El rango es: ", rango