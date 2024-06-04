from typing import List
from datetime import date
from utils.idgenerator import id_generator

from clases.autor import Autor


class Tesis:
    def __init__(self, autores: List[Autor], institucion: str, f_investigacion: date, f_presentacion: date, campo_estudio: str, estado: str, paginas: int):
        self._autores = autores
        self._institucion = institucion
        self._f_investigacion = f_investigacion
        self._f_presentacion = f_presentacion
        self._campo_estudio = campo_estudio
        self._estado= estado
        self._paginas = paginas
        self._id = id_generator()
        
        
    def __str__(self):
        return f"ID: {self._id}"
    
    def id(self):
        return self._id       
        
    def autores(self):
        return self._autores
    
    def set_Autores(self, autores):
        self._autores = autores
        
        
    def institucion(self):
        return self._institucion
    
    def set_Institucion(self, institucion):
        self._institucion = institucion
        
        
    def finvestigacion(self):
        return self._f_investigacion
    
    def set_Finvestigacion(self, f_investigacion):
        self._f_investigacion = f_investigacion
        
        
    def fpresentacion(self):
        return self._f_presentacion
    
    def set_Fpresentacion(self, f_presentacion):
        self._f_presentacion = f_presentacion
        
        
    def campoEstudio(self):
        return self._campo_estudio
    
    def set_CampoEstudio(self, campo_estudio):
        self._campo_estudio = campo_estudio
        
        
    def estado(self):
        return self._estado
    
    def set_Estado(self, estado):
        self._estado = estado        


    def paginas(self):
        return self._paginas
    
    def set_Paginas(self, paginas):
        self._paginas = paginas
        
    