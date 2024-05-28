from typing import List
from clases.autor import Autor
from clases.estado import Estado

class Libro:
    def __init__(self, genero: str, titulo: str, edicion: str, anio_publicacion: int, editorial: str,
                 autores: List[Autor], estado: Estado, isbn: str, idiomas: List[str], numero_copias: int):
        self._genero = genero
        self._titulo = titulo
        self._edicion = edicion
        self._anio_publicacion = anio_publicacion
        self._editorial = editorial
        self._autores = autores
        self._estado = estado
        self._isbn = isbn
        self._idiomas = idiomas
        self._numero_copias = numero_copias

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def edicion(self):
        return self._edicion

    @edicion.setter
    def edicion(self, value):
        self._edicion = value

    @property
    def anio_publicacion(self):
        return self._anio_publicacion

    @anio_publicacion.setter
    def anio_publicacion(self, value):
        self._anio_publicacion = value

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, value):
        self._editorial = value

    @property
    def autores(self):
        return self._autores

    @autores.setter
    def autores(self, value):
        self._autores = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value

    @property
    def idiomas(self):
        return self._idiomas

    @idiomas.setter
    def idiomas(self, value):
        self._idiomas = value

    @property
    def numero_copias(self):
        return self._numero_copias

    @numero_copias.setter
    def numero_copias(self, value):
        self._numero_copias = value
