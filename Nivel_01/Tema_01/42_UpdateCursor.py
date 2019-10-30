# Importar la libreria de arcpy
import arcpy

# Sobreescribimos los archivos
arcpy.env.overwriteOutput = True

# Declaramos nuestra ruta de trabajo
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_13\Practica.gdb"

# Guardar en una variable el FC Estaciones
fc = "Estaciones"

# Borrar estaciones con el UpdateCursor (deleteRow)
with arcpy.da.UpdateCursor(fc,["COD_ESTAC"]) as cursor:
    for row in cursor:
        if (row[0] == "25") or (row[0] == "26") or (row[0] == "27"):
            cursor.deleteRow()

# Borramos el cursor
del cursor

print "Registros eliminados"

