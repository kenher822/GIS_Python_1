# Importar la libreria de arcpy
import arcpy

# Importar la libreria del sistema operativo
import os

# Sobreescribir los resultados
arcpy.env.overwriteOutput = True

# Crear una variable de ruta de trabajajo
ruta = r"C:\Cursos\Python_GIS\Nivel_01\Tema_11\GDB"

# Crear una variable de entorno de trabajo
arcpy.env.workspace = os.path.join(ruta, "Practica.gdb")

# Listar los FeatureClass de la GDB Practica.gdb
listFC = arcpy.ListFeatureClasses()

# Crear el archivo de reporte .doc .xls .txt
doc = open(os.path.join(ruta, "reporteFC.txt"), "w")

# Escribir en el archivo creado
doc.write("Nombre del FC" + "\t"+ "Tipo de Geometris")

# Escribir el nombre y tipo de geometría de los FC
for FC in listFC:
    descFC = arcpy.Describe(FC)
    doc.write("\n" + descFC.name + "\t" + descFC.Shapetype)
    
doc.close()

print "Script terminado"

