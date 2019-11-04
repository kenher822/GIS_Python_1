# Script que permite el uso de parametros para el buffer
'''
Programa realizado por KHERRERA
Fecha: 04/1/2019
'''

# Importar librerias de arcpy
import arcpy

# Sobre escribir los resultados
arcpy.env.overwriteOutput = True

# Declarar la variable de entorno
arcpy.env.workspace=r"D:\Proyectos\GIS_Python_1\GEOTALLER\Datos\GDB\Practica.gdb"

# Listar feature class
listaFC = arcpy.ListFeatureClasses()

# Recorrer la geodatabase
for capa in listaFC:
    lista2 = arcpy.Describe(capa)
    print lista2.name + "\t" + lista2.Shapetype

# Impresion de resultado final
arcpy.AddMessage("Script finalizado")
