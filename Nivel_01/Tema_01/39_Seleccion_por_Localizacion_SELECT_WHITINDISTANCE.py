# Importar la libreria de arcpy
import arcpy

# Sobreescribir los resultados
arcpy.env.overwriteOutput = True

# Declarar el entorno de trabajo
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_12\GDB\Practica.gdb"

# Consulta al municipi
sqlMunicipio = "CodigoTipoReferencia = '31'"

# Consulta de lugares de venta de licor
sqlVentaLicor = "CodigoTipoReferencia IN ('91','92','11')"

# Distancia (Radio de Influencia)
distancia = "500 meters"

# Capa temporal del Municipio
municipio = arcpy.MakeFeatureLayer_management("PuntoReferencia", "municipio", sqlMunicipio)

# Capa temporl de los puestos de venta de licor
ventaLicor = arcpy.MakeFeatureLayer_management("PuntoReferencia","ventaLicor", sqlVentaLicor)

# Selection por localizacion (venta de licores a 500 mts del municipio)
arcpy.SelectLayerByLocation_management(ventaLicor, "WITHIN_A_DISTANCE", municipio, distancia, "NEW_SELECTION")

# Contar cuantos puestos de venta existen dentro de un radio de 500 mts a partir del municipio
countVentaLicor = arcpy.GetCount_management(ventaLicor)

# Crear una capa de los establecimientos que se encuentran dentro del radio de 500 mts a partir del municipio
if countVentaLicor == 0:
    print "Dentro de los 500 mts, no se ha encontrado ningun puesto de venta de licor"
else:
    arcpy.CopyFeatures_management(ventaLicor, "ventaLicor_500mt")
    arcpy.Delete_management(municipio)
    arcpy.Delete_management(ventaLicor)
    print "Los puestos de venta de licor que se encuentran a 500mt a partir del municipio son: " + str(countVentaLicor)

print "Fin del geoprocesamiento"



















