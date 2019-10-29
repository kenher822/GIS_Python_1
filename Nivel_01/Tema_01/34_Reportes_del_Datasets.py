# Importar la libreria de arcpy
import arcpy

# Importar la libreria del sistema operativo
import os

# Sobreescribir los resultados
arcpy.env.overwriteOutput = True

# Crear una variable de ruta de trabajo
ruta = r"C:\Cursos\Python_GIS\Nivel_01\Tema_11\GDB"

# Crear una variable de espacio de trabajo
#arcpy.env.workspace = ruta + "\Mundo.gdb"

#print arcpy.env.workspace

# Crear una variable de espacio de trabajo
arcpy.env.workspace = os.path.join(ruta, "Mundo.gdb")

#print arcpy.env.workspace

# Definir una list de datasets de la GDB Mundo.gdb
listDatasets = arcpy.ListDatasets()

# Crear nuestro archivo de reporte .doc .xls .txt
doc = open(os.path.join(ruta, "reporteDatasets.xls"), "w")

# Escribir el titulo del reporte
doc.write("Lista de Datasets"+"\n")
doc.write("========================================================="+"\n")

# Escribir los datasets
for dataset in listDatasets:
    doc.write("\n"+dataset)

doc.close()

