import arcpy
import pythonaddins

class ButtonClass1(object):
    """Implementation for Herramienta_addin.button_Ayuda (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.MessageBox("Herramienta para geoprocesamiento SISCAT","SISCAT PY",0)

class ButtonClass15(object):
    """Implementation for Herramienta_addin.button_Desactivar_Capas (Button)"""
    def __init__(self):
        self.enabled = True
    def onClick(self):
        pythonaddins.GPToolDialog(r"D:\Proyectos\GIS_Python_1\Nivel_01\Tema_15\Modelos\ModeloConParametros_Buffer.tbx", "Buffer")

class ButtonClass16(object):
    """Implementation for Herramienta_addin.button_GenerarID (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClass7(object):
    """Implementation for Herramienta_addin.button_Buffer (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClass8(object):
    """Implementation for Herramienta_addin.button_Activar_Capas (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass