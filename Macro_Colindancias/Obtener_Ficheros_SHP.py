# Coding: utr-8

# Importar libreria de arcpy
import arcpy

# Importar libreria del Sistema Operativo
import os


# Sobre escribir los resultados
arcpy.env.overwriteOutput = True

# Variable para la ruta al directorio del SO
path = r"D:\Proyectos\GIS_Python_1\Macro_Colindancias\SHP"

# Declaramos entorno de trabajo para arcpy
arcpy.env.workspace = r"D:\Proyectos\GIS_Python_1\Macro_Colindancias\SHP"

# Crear y enlistar todos los ficheros del directorio
listDir = os.walk(path)

# Crear lista vacia para agregar los ficheros del directorio
listFiles = []

# Agregar ficheros a la lista con formato shp que existen en el directorio
for root, dirs, files in listDir:
    for fichero in files:
        (nameFile, extension) = os.path.splitext(fichero)
        file = nameFile+extension
        if(file == "PARCELAS.shp"): 
            listFiles.append(file)
            print file

# print listFiles
print "Longitud de la lista = ", len(listFiles)
print "Script finalizado"