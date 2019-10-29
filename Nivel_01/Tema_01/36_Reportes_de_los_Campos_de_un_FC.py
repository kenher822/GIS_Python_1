# Importando la libreria de arcpy
import arcpy

# Importar la libreria os
import os

# Sobreescribir los resultados
arcpy.env.overwriteOutput = True

# Crear una variable de ruta de trabajo
ruta = r"C:\Cursos\Python_GIS\Nivel_01\Tema_11\GDB"

# Especificar el espacio de trabajo
arcpy.env.workspace = os.path.join(ruta, "Practica_07.mdb")

# Listar los campos del FeatureClass Centrales Hidroelectricas
listFields = arcpy.ListFields("CentralesHidroelectricas")

# Crear el archivo de reporte .doc .xls .txt
doc = open(os.path.join(ruta, "reporteFeields.xls"), "w")

# Escribit el titulo del reporte
doc.write("Lista de Campos del FeatureClass Centrales Hidroelectricas"+"\n")
doc.write("==================================================================" + "\n")

for field in listFields:
    descField = "Campo: {0}, Tipo: {1}, Longitud: {2}".format(field.name,
                                                               field.type,
                                                               field.length)
    doc.write(descField)

doc.close()
print "Script Terminado"