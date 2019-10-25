# Paso 01: Declarar Librer�as y Variables

# Importar la libreria del ArcPy
import arcpy

# Sobreescribir los archivos de salidas
arcpy.env.overwriteOutput = True

# Especificar el FeatureClass a trabaar "Centrales Hidroelectricas"
entidad = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_08\Tema_08.gdb\CentralesHidroelectricas"

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

# Paso 03: Obtener la media aritm�tica de los valores obtenidos

# Construir un funci�n para obetener la media aritm�tica
def media(lista):
    total = 0
    for i in lista:
        total += i
    media = total/len(lista)
    return media

# Llamar a la funci�n media
resultadoMedia = media(valores)

print resultadoMedia

# ###########################################################################################################

# Paso 04: Seleccionar los valores mayores a la media aritm�tica

# Crear una capa temporal que va a ser copia del FeatureClass CentralesHidroel�cticas
arcpy.MakeFeatureLayer_management(entidad, "entidad_temporal")

# Crear una expresi�n que me indique: mayor a la media(Potencia>84.53333)
expresion = "Potencia>"+str(resultadoMedia)

# Seleccionar los registros mayores a la media aritm�tica
arcpy.SelectLayerByAttribute_management("entidad_temporal","NEW_SELECTION",expresion)

# ###########################################################################################################

# Paso 05: Pasar la selecci�n de la capa temporal a una capa fisica

# Especificar la ruta de la capa f�sica
entidadMayorMedia = "D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_08\Tema_08.gdb\CentralesHidroelectricasMayorMedia"

# Pasar los valores seleccionados a la capa f�sica
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