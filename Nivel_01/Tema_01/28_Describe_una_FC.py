# Importar las librerias de ArcPy
import arcpy

# Especificar el espacio de trabajo
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_09\Tema_09.gdb\CentralesHidroelectricas"

# Obtener las caracteristicas del FC
descFC = arcpy.Describe(arcpy.env.workspace)

# Mostar el nombre, la ruta, tipo de geometría y el tipo de dataset
print "Caracteristicas del FC:\n-----------------------------------------------------------------------------------"

print " Nombre\t\t: {0}\n Ruta\t: {1}\n Geometria\t\t: {2}\n Dataset\t\t: {3}\n Datatype\t\t: {4} ".format(descFC.name,
                                                                                                       descFC.path,
                                                                                                       descFC.shapeType,
                                                                                                       descFC.datasetType,
                                                                                                       descFC.dataType)
