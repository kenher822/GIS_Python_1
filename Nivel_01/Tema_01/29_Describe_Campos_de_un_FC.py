# Importar Arcpy
import arcpy

# Definir el espacio de trabajo
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_09\Tema_09.gdb\CentralesHidroelectricas"

# Obtener las características del FC
descFC = arcpy.Describe(arcpy.env.workspace)

# Obtener las caracteristicas de los campos del FC
print "Caracteristicas de los Campos del FC:\n-------------------------------------------------------------------------"

for field in descFC.fields:
    print " Nombre: {0} | Tipo: {1} | Longitud: {2} | Requerido: {3} | Nulos: {4} | Alias: {5}".format(field.name,
                                                                                                      field.type,
                                                                                                      field.length,
                                                                                                       field.required,
                                                                                                      field.isNullable,
                                                                                                      field.aliasName)
    