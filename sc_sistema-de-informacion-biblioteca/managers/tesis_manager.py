# Juan Castanio
import os
from clases.tesis import Tesis

class tesis_manager:
    def __init__(self):
        self.tesis = []
    
    def add_tesis(self):
        institucion_academica = input("Ingrese la institución académica: ")
        fecha_investigacion = input("Ingrese la fecha de investigación: ")
        fecha_presentacion = input("Ingrese la fecha de presentación: ")
        campo_estudio = input("Ingrese el campo de estudio: ")
        
        numero_paginas = int(input("Ingrese el número de páginas: "))
        tesis = Tesis(institucion_academica, fecha_investigacion, fecha_presentacion, campo_estudio, numero_paginas)
        