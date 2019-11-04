
# Script para crear un buffer y que permite el uso de parametros
'''
Programa realizado por Kennett Herrera
Fecha: 11/04/2018
'''

# Importando modulo del sistema
import arcpy

# Declarando los parametros de entrada
CapaEntrada = arcpy.GetParameterAsText(0)
CapaSalida = arcpy.GetParameterAsText(1)
Distancia = arcpy.GetParameterAsText(2)

# Herramienta de geoprocesamiento
arcpy.Buffer_analysis(CapaEntrada, CapaSalida, Distancia)

# Impresi�n de resultado final
arcpy.AddMessage("Proceso finalizado")