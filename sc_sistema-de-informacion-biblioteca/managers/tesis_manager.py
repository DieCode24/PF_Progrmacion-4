# Juan Castanio
import os
from clases.tesis import Tesis
from clases.estado import Estado

class tesis_manager:
    def __init__(self):
        self.tesisL = []
    
    def add_tesis(self):
        institucion_academica = input("Ingrese la institución académica: ")
        fecha_investigacion = input("Ingrese la fecha de investigación: ")
        fecha_presentacion = input("Ingrese la fecha de presentación: ")
        campo_estudio = input("Ingrese el campo de estudio: ")
        
        numero_paginas = int(input("Ingrese el número de páginas: "))
        tesis = Tesis(institucion_academica, fecha_investigacion, fecha_presentacion, campo_estudio, numero_paginas)
        
        self.tesisL.append(tesis)
        print("Tesis registrada con éxito.")
        
    def list_tesis(self):
        print("Listado de tesis\n")
        count = 1
        for tesis in self.tesisL:
            print(tesis)
            
    def search_tesis(self):
        estudio = input("Ingrese el campo de estudio: ")
        for tesis in self.tesisL:
            if tesis. == estudio:
                print(tesis)
                return
        print("Tesis no encontrada.")
        