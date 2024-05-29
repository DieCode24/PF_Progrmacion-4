from datetime import date
from typing import List
from clases.estado import Estado

class Tesis:
    def __init__(self, autores: List[str], institucion: str, f_investigacion: date, f_presentacion: date, campo_estudio: str, estado: str, paginas: int):
        self._autores = autores
        self._institucion = institucion
        self._f_investigacion = f_investigacion
        self._f_presentacion = f_presentacion
        self._campo_estudio = campo_estudio
        self._estado= estado
        self._paginas = paginas
        
        
        
    def get_Autores(self):
        return self._autores
    
    def set_Autores(self, autores):
        self._autores = autores
        
        
    def get_Institucion(self):
        return self._institucion
    
    def set_Institucion(self, institucion):
        self._institucion = institucion
        
        
    def get_Finvestigacion(self):
        return self._f_investigacion
    
    def set_Finvestigacion(self, f_investigacion):
        self._f_investigacion = f_investigacion
        
        
    def get_Fpresentacion(self):
        return self._f_presentacion
    
    def set_Fpresentacion(self, f_presentacion):
        self._f_presentacion = f_presentacion
        
        
    def get_CampoEstudio(self):
        return self._campo_estudio
    
    def set_CampoEstudio(self, campo_estudio):
        self._campo_estudio = campo_estudio
        
        
    def get_Estado(self):
        return self._estado
    
    def set_Estado(self, estado):
        self._estado = estado        


    def get_Paginas(self):
        return self._paginas
    
    def set_Paginas(self, paginas):
        self._paginas = paginas
    
        
        
    


