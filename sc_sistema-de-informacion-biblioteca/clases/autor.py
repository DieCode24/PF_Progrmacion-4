from typing import Any


class Autor:
    def __init__(self, nombre: str, nacionalidad: str, fecha_nacimiento: str):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.libros = []
        self.tesis = []
        self.articulos = []
        self.cantidad_libros = 0
        self.habilitado = True

    def __str__(self):
        return print(f"Nombre: {self.nombre}\nNacionalidad: {self.nacionalidad}\nFecha de nacimiento: {self.fecha_nacimiento}\nCantidad de libros: {self.cantidad_libros}\n")
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.cantidad_libros += 1
        
    def nombre(self):
        return self.nombre
    
    def nacionalidad(self):
        return self.nacionalidad
    
    def fecha_nacimiento(self): 
        return self.fecha_nacimiento
    
    def cantidad_libros(self):
        return self.cantidad_libros
    
    def gethabilitado(self):
        return self.habilitado
    
    def inhabilitar(self):
        self.habilitado = False
        
    def habilitar(self):
        self.habilitado = True
        
