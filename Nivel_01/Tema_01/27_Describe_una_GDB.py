# Importar las librerias del Arcpy
import arcpy

# Especificar el espacio de trabajo
arcpy.env.workspace = (r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_09\Tema_09.gdb")

# Obtener las características de una GDB
descGDB = arcpy.Describe(arcpy.env.workspace)

# Mostrar el nombre, la ruta, el tipo de espacio de trabajo y la versión de la GDB
print "Caracteristicas de la GDB:\n-----------------------------------------------"

print " Nombre\t\t: {0}\n Ruta\t\t: {1}\n Tipo\t\t: {2}\n Version\t: {3}".format(descGDB.name,
                                                                               descGDB.path,
                                                                               descGDB.workspaceType,
                                                                               descGDB.release)