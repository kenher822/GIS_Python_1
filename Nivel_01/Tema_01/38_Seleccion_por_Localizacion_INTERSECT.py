# Importar la libreria de arcpy
import arcpy

# Sobreescribir los resultados
arcpy.env.overwriteOutput = True

# Especificar el espacio de trabajo
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_12\GDB\Practica.gdb"

# Consulta a Comedores
consultaComedores = "CodigoTipoReferencia = '10'"

# Crear una capa temporal del FC PuntoReferencia
temporalPuntoReferencia = arcpy.MakeFeatureLayer_management("PuntoReferencia", "PuntoReferencia_lyr")

# Seleccionar los Puntos de Referencia que se intersectan con las manzanas
arcpy.SelectLayerByLocation_management(temporalPuntoReferencia, "INTERSECT","Manzana","","NEW_SELECTION")

# De lo seleccionado, seleccionar los comedores
arcpy.SelectLayerByAttribute_managment(temporalPuntoReferencia, "SUBSET_SELECTION", consultaComedores)

# Contar cuantos comedores se intersectan con las manzanas
contarComedores = arcpy.GetCount_management(temporalPuntoReferencia)
print contarComedores

# Copiar los comedores a un FC
if contarComedores == 0:
    "No existe ningun comedor que se intersecte con las manzanas"
else:
    arcpy.CopyFeatures_management(temporalPuntoReferencia, "Comedores_Intersectados")
    print "La cantidad de comedores intersectados con las manzanas son: " + str(contarComedores)

arcpy.Delete_managment(temporalPuntoReferencia)