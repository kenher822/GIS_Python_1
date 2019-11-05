# Paso 01: Declarar Librerias y Variables

# Importar la libreria del ArcPy
import arcpy

# Sobreescribir los archivos de salidas
arcpy.env.overwriteOutput = True

# Especificar el FeatureClass a trabaar "Centrales Hidroelectricas" D:\Proyectos\GIS_Python_1\Nivel_01\Tema_08\Tema_08.gdb
entidad = r"D:\Proyectos\GIS_Python_1\Nivel_01\Tema_08\Tema_08.gdb\CentralesHidroelectricas"

# Recuperar todos los valores del FeatureClass
registros = arcpy.SearchCursor(entidad)

# ###########################################################################################################

# Paso 02: Obtener los registros de un campo del FeatureClass

# Deaclarar una lista vacia

valores = []

# Llenar los valores a la lista vacia
for registro in registros:
    valor = registro.getValue("Potencia")
    valores.append(valor)
    
print valores

# ###########################################################################################################

# Paso 03: Obtener la media aritmatica de los valores obtenidos

# Construir un funcion para obetener la media aritmetica
def media(lista):
    total = 0
    for i in lista:
        total += i
    media = total/len(lista)
    return media

# Llamar a la funcion media
resultadoMedia = media(valores)

print resultadoMedia

# ###########################################################################################################

# Paso 04: Seleccionar los valores mayores a la media aritmetica

# Crear una capa temporal que va a ser copia del FeatureClass CentralesHidroelecticas
arcpy.MakeFeatureLayer_management(entidad, "entidad_temporal")

# Crear una expresion que me indique: mayor a la media(Potencia>84.53333)
expresion = "Potencia>"+str(resultadoMedia)

# Seleccionar los registros mayores a la media aritmetica
arcpy.SelectLayerByAttribute_management("entidad_temporal","NEW_SELECTION",expresion)

# ###########################################################################################################

# Paso 05: Pasar la seleccion de la capa temporal a una capa fisica

# Especificar la ruta de la capa fisica
entidadMayorMedia = r"D:\Proyectos\GIS_Python_1\Nivel_01\Tema_08\Tema_08.gdb\CentralesHidroelectricasMayorMedia"

# Pasar los valores seleccionados a la capa fisica
arcpy.Select_analysis("entidad_temporal",entidadMayorMedia)

# Eliminar la capa temporal
arcpy.Delete_management("entidad_temporal")


# ###########################################################################################################

# Paso 06: Agregar y Calcular Campos

# Crear el campo UtilidadOperativa
campo = "UtilidadOperativa"
arcpy.AddField_management(entidadMayorMedia,campo,"TEXT","","","15")

# Agregar registro Muy Buena
cadena = '"Muy Buena"'
arcpy.CalculateField_management(entidadMayorMedia,campo,cadena,"VB")

print "Geoproceso Finalizado"