# Importar la libreria del Arcpy
import arcpy

# Definir el espacio de trabajo
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_10\GDB\Practica.gdb"

# Listar los FeatureClass de la GDB
listFC = arcpy.ListFeatureClasses()

# print listFC

# Obtener linea por linea cada FeatureClasses
for featureclass in listFC:
    print featureclass
