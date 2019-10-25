# Importar la libreria ArcPy
import arcpy

# Definir Espacio de Trabajo
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_10\GDB\Mundo.gdb"

# Obtener un listado de los Feature Datasets
listDatasets = arcpy.ListDatasets()

# print listDatasets

# Lista por linea de cada Feature Datasets
for dataset in listDatasets:
    print dataset