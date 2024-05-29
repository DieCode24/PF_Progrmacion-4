import os
from clases.tesis import Tesis
from clases.estado import Estado
from utils.validators import validar_input

class TesisManager:
    def __init__(self):
        self.tesis = []
        estadoi = Estado() 
    
    def agregar_tesis(self, autores: list, institucion: str, f_investigacion: str, f_presentacion: str, campo_estudio: str, estado: str, paginas: int):
        nueva_tesis = Tesis(autores, institucion, f_investigacion, f_presentacion, campo_estudio, estado, paginas)
        self.tesis.append(nueva_tesis)
        
        
        
    def listar_tesis(self):
        print("LISTA DE TESIS\n")
        for tesis in self.tesis:
            print(tesis)   
            
            
    def buscar_tesis(self): 
        print("Como desea buscar la tesis?")
        print("1. Por autor")
        print("2. Por campo de estudio")
        op = input("Ingrese la opcion: ")
        
        if op == '1':
            self.buscar_por_autor()
            
        elif op == '2':
            self.buscar_por_campo()
        
    def buscar_por_autor(self):
        autor = input("Ingrese el autor: ")
        for tesis in self.tesis:
            if autor in tesis.get_Autores():
                print(tesis)
                    
    def buscar_por_campo(self):
        campo = input("Ingrese el campo de estudio: ")
        for tesis in self.tesis:
            if campo in tesis.get_CampoEstudio():
                print(tesis)
        
        

    
    