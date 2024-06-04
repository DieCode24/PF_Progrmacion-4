from datetime import date
from typing import Any, List
from clases.estado import Estado
from utils.idgenerator import id_generator
class Lector:
    def __init__(self, nombre: str, telefono: str, direccion: str, estado: str = Estado.NORMAL):
        self.nombre = nombre
        self.id = int(id_generator())
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado
        self.cantidad_libros_prestados = 0
        self.libros_prestados = []
        self.tiene_multa = False

    def __str__(self):
        return f"Lector: {self.nombre}, ID: {self.id}, Estado: {self.estado}\n"

    def agregar_libro_prestado(self, libro: str):
        self.libros_prestados.append(libro)
        self.cantidad_libros_prestados += 1

    def quitar_libro_prestado(self, libro: str):
        self.libros_prestados.remove(libro)
        self.cantidad_libros_prestados -= 1

    def activar_multa(self):
        self.tiene_multa = True

    def desactivar_multa(self):
        self.tiene_multa = False

    def sancionar(self):
        self.estado = Estado.SANCIONADO

    def suspender(self):
        self.estado = Estado.SUSPENDIDO

    def rehabilitar(self):
        self.estado = Estado.NORMAL

    def actualizar_informacion(self, nombre: str = None, telefono: str = None, direccion: str = None):
        if nombre:
            self.nombre = nombre
        if telefono:
            self.telefono = telefono
        if direccion:
            self.direccion = direccion
            
    def get_id(self):
        return self.id
    
    def __setattr__(self, name: str, value: Any) -> None:
        pass