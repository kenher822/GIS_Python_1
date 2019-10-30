# Importar la libreria de arcpy
import arcpy

# Sobreescribir los registros
arcpy.env.overwriteOutput = True

# Especificar la ruta de trabajo
arcpy.env.workspace = r"D:\Este Equipo\OneDrive\Cursos\GIS-Python\Nivel_01\Tema_13\Practica.gdb"

# Guardar en una variable el FC Estaciones y los registros a insertar
fc = "Estaciones"
registros = [('21', 'Colmena', (-77.03279420699994, -12.052360990999944)),
             ('22', 'Jiron de La Union', (-77.03313791899996, -12.049097341999982)),
             ('23', 'Tacna', (-77.03788199899998, -12.046206414999972)),
             ('25', 'Espana', (-77.04177575099999, -12.057597874999942)),
             ('26', 'Quilca', (-77.04231663299998, -12.051428646999966)),
             ('27', 'Dos de Mayo', (-77.04275817099995, -12.046392511999954)),]

# Insetar registro utilizando el InsertCursor
with arcpy.da.InsertCursor(fc, ["COD_ESTAC","NOM_ESTAC","SHAPE@XY"]) as cursor:
    for registro in registros:
        cursor.insertRow(registro)

# Eliminamos el cursor
del cursor

print "Se insertaron " + str(len(registros)) + " registros.\nInsercion realizada"
