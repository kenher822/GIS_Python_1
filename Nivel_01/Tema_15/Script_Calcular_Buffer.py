# Script que permite el uso de parametros para el buffer
'''
Programa realizado por KHERRERA
Fecha: 04/1/2019
'''

# Importar librerias de arcpy
import arcpy

# Declarar variables e instanciando con os parametros de entrada

CapaEntrada = arcpy.GetParameterAsText(0)
CapaSalida = arcpy.GetParameterAsText(1)
Distancia = arcpy.GetParameterAsText(2)

# Herramienta de geoprocesamiento BUFFER
arcpy.Buffer_analysis(CapaEntrada, CapaSalida, Distancia)

# Impresion de resultado final
arcpy.AddMessage("Proceso finalizado")
