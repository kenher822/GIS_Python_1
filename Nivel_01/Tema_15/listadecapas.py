# Script que permite el uso de parametros para el buffer
'''
Programa realizado por KHERRERA
Fecha: 04/1/2019
'''

# Importar librerias de arcpy
import arcpy

# Sobre escribir los resultados
arcpy.env.overwriteOutput = True

# Declarar la variable de entorno
arcpy.env.workspace=r"D:\Proyectos\GIS_Python_1\GEOTALLER\Datos\GDB\Practica.gdb"

# Listar feature class
listaFC = arcpy.ListFeatureClasses()

encabezadoTitulo = "FeatureClass" + "\t" + "Tipo de Geometria"

# Crear reporte en formato xls
xlsFile = open(r"D:\Proyectos\GIS_Python_1\Nivel_01\Tema_15\Capas.xls", "w")
xlsFile.write(encabezadoTitulo)

xlsFile1 = open(r"D:\Proyectos\GIS_Python_1\Nivel_01\Tema_15\ListaDeEstaciones.xls", "w")
xlsFile1.write("Lista de Estaciones"+ "\n")
xlsFile1.write("==================="+ "\n")s

# Creando la lista de registros con un cursor
registrosEstaciones = arcpy.SearchCursor("Estaciones")

# Recorrer lista estaciones y agregar al reporte
for registro in registrosEstaciones:
    valor = str(registro.getValue('OBJECTID')) + "\t" + registro.getValue('NOM_ESTAC')
    xlsFile1.write("\n" + valor)

# Cerrar el archivo
xlsFile1.close()

# Crear reporte en formato txt
txtFile = open(r"D:\Proyectos\GIS_Python_1\Nivel_01\Tema_15\Capas.txt", "w")
txtFile.write(encabezadoTitulo)

# Crear reporte en formato doc
docFile = open(r"D:\Proyectos\GIS_Python_1\Nivel_01\Tema_15\Capas.doc", "w")
docFile.write(encabezadoTitulo)

# Recorrer la geodatabase
for capa in listaFC:
    listaCampos = arcpy.ListFields(capa)
    lista2 = arcpy.Describe(capa)
    # print lista2.name + "\t" + lista2.Shapetype
    encabezadoCapas ="\n" + lista2.name + "\t" + lista2.Shapetype + "\n"

    xlsFile.write(encabezadoCapas)
    txtFile.write(encabezadoCapas)
    docFile.write(encabezadoCapas)

    for campo in listaCampos:
        encabezadoCampos = "\n" + "\t" + "\t" + campo.name + "\t" + campo.type
        xlsFile.write(encabezadoCampos)
        txtFile.write(encabezadoCampos)
        docFile.write(encabezadoCampos)

    xlsFile.write("\n")
    txtFile.write("\n")
    docFile.write("\n")

xlsFile.close()
txtFile.close()
docFile.close()

# Impresion de resultado final
arcpy.AddMessage("Script finalizado")
