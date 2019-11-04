# Paso 01: Importar librerias y declarar variables
import arcpy

# Importar libreria de math(matematicas)
import math

# Sobreescribir los resultados
arcpy.env.overwrithOutput = True

# Especificar el FC a trabajar ------------> CentralesHidroelectricas
fc = r"D:\Proyectos\GIS_Python_1\Nivel_01\Tema_14\GDB\Practica.gdb\CentralesHidroelectricas"

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

# Paso 04: Calcular el numero de intervalos

# Calcular el numero de intervalos, aplicando la regla de Sturges (k = 1+3.3*log10(n)) # de registros
numeroIntervalos = int(round(1+3.2*math.log10(len(potencia))))
print "El numero de intervalos es: ", numeroIntervalos

# Calcular la amplitud (amplitud = rango/numeroIntervalos)
amplitud = rango/numeroIntervalos
print "La amplitud es: ", amplitud

# Paso 06: Calcular los valores de cada intervalo

# Calcular los primeros valores de cada intervalo (Funcion Range)
intervalo1 = range(int(min(potencia)), int(max(potencia)), amplitud)
print "Los primeros valores de los intervalos son: ", intervalo1

# Paso 07: Calcular los intervalos

# Crear una lista de intervalos (vacia)
intervalos = []

# Calcular los segundos valores y los intervalos
for i in intervalo1:
    intervalo2 = "["  + str(i) + ";" + str(i+amplitud) + ">"
    intervalos.append(intervalo2)

print "Los intervalos son: ", intervalos

# Paso 08: Crear el campo intervalos

# Crear el campo Intervalos
arcpy.AddField_management(fc, campoIntervalos, "TEXT","","","25")
print "Campo creado"


