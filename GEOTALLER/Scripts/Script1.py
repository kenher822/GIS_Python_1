# Script para crear reporte enlistando capas de un featureclass en excel
'''
Programa realizado por Kennett Herrera
Fecha: 12/04/2018
'''

# Importando modulo del sistema
import arcpy

# Sobreescribir resultados de geoprocesos
arcpy.env.overwriteOutput = True

# Declarando variable de entorno
arcpy.env.workspace = r"D:\GEOTALLER\Datos\GDB\Practica.gdb"

# Declarando lista de capas a recorrer
listaDeCapas = arcpy.ListFeatureClasses()

# Ruta para generar reporte en excel
xlsFile=open(r"D:\GEOTALLER\Reportes\Registros.xls","w")
xlsFile.write("Lista de Estaciones" + "\n")
xlsFile.write("===================" + "\n")

# Delarando variable de registros 
registros = arcpy.SearchCursor("Estaciones")

for registro in registros:
    valor = registro.getValue('NOM_ESTAC')
    xlsFile.write("\n" + valor)

'''
# Reccorriendo lista de capas con for
for capa in listaDeCapas:
    listaCampos = arcpy.ListFields(capa)
    lista2 = arcpy.Describe(capa)    
    xlsFile.write("\n" + lista2.name + "\t" + lista2.Shapetype)
    for campo in listaCampos:
        xlsFile.write("\n" + "\t" + "\t" + campo.name + "\t" + campo.type )
'''
# Cerrando archivo
xlsFile.close()

# Impresión de resultado final
print "Reporte Generado..."