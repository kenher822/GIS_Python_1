# Importar la libreria de arcpy
import arcpy

# Definir el espacio de trabajo
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_10\GDB\Practica.mdb"

# Listar los campos de un FeatureClasses
listFields = arcpy.ListFields("CentralesHidroelectricas")

# Mostrar el nombre y el tipo de dato de los campos del FeatureClass
for field in listFields:
    print "Nombre: " + field.name + "\t", "Tipo: " + field.type