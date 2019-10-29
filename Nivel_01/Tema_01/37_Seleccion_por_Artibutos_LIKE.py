# Importar la libreria arcpy
import arcpy

# Declarar la variable para sobreescribit resultados
arcpy.env.overwriteOutput = True

# Delcalrar variable de entorno de trabajo
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_11\GDB\Practica.gdb"

# Declarar una consulta del FC Estaciones, para que me seleccione todos aquellos que comiencen con 1
consultaEstaciones_1n = "COD_ESTAC LIKE '1%'"

# Crear capa temporal del FC Estaciones
temporalEstaciones = arcpy.MakeFeatureLayer_management("Estaciones","Estaciones_lyr")

# Seleccionar las estaciones que comiencen con el numero 1
arcpy.SelectLayerByAttribute_management(temporalEstaciones,"NEW_SELECTION",consultaEstaciones_1n)

# Copiar la seleccion a una nueva capa
arcpy.CopyFeatures_management(temporalEstaciones,"Estaciones_1n")

# Contar las estaciones seleccionadas
contarEstaciones = arcpy.GetCount_management(temporalEstaciones)

print "Las estaciones que comienzan con numero 1 son: " + str(contarEstaciones)

# Borrar la capa temporal
arcpy.Delete_management(temporalEstaciones)

# Fin
print "Fin del Proceso"