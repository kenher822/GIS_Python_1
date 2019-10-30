# Importamos la libreria de arcpy
import arcpy

# Sobreecribir los resultados
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_13\Practica.gdb"

# Crear una variable para borrar el FC NuevasEstacionesque vamos a utilizar y para buscar los campos que deseamos
fc = "NuevasEstaciones"
fields = ["C_ESTACION","N_ESTACION","SHAPE@Y"]

# Imprimir los dregistros requeridos a partir del SearchCursor
with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        print "('{0}', '{1}', {2}),".format(row[0], row[1], row[2])
del cursor

# Consultar el numero de registros
