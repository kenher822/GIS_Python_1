
# Script para crear un buffer de 1 km de distancia
'''
Programa realizado por Kennett Herrera
Fecha: 11/04/2018
'''

# Importando modulo del sistema
import arcpy

# Sobreescribir resultados de geoprocesos
arcpy.env.overwriteOutput = True

# Declarando variable de entorno
arcpy.env.workspace = r"D:\GEOTALLER\Datos\GDB\Practica.gdb"

# Declarando variables locales
CapaEntrada = "Estaciones"
CapaSalida = "EstacionesBuffer1km"
Distancia = "1 kilometers"

# Herramienta de geoprocesamiento
arcpy.Buffer_analysis(CapaEntrada, CapaSalida, Distancia)

# Impresión de resultado final
print "Script finalizado!!!"