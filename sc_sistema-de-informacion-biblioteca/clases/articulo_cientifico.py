# clases/articulo_cientifico.py

from datetime import date
from typing import List
from clases.estado import Estado


class ArticuloCientifico:
    """
    Clase que representa un artículo científico en el sistema de información de la biblioteca.
    """

    def __init__(self, titulo: str, doi: str, editor: str, fecha_publicacion: date, periodicidad: str, volumen: int, campo_interes: str, 
                 estado: str = Estado.DISPONIBLE):
        """
        Inicializa una nueva instancia de ArticuloCientifico.
        
        :param titulo: Título del artículo.
        :param doi: Identificador único del artículo (DOI).
        :param editor: Nombre del editor del artículo.
        :param fecha_publicacion: Fecha de publicación del artículo.
        :param periodicidad: Periodicidad de la publicación (mensual, semanal, etc.).
        :param volumen: Número de volumen del artículo.
        :param campo_interes: Campo de interés del artículo.
        :param estado: Estado del artículo (predeterminado a "Disponible").
        """
        self.titulo = titulo
        self.doi = doi
        self.editor = editor
        self.fecha_publicacion = fecha_publicacion
        self.periodicidad = periodicidad
        self.volumen = volumen
        self.campo_interes = campo_interes
        self.estado = estado

    def __str__(self):
        """
        Retorna una representación en cadena del artículo científico.
        
        :return: Una cadena que representa el artículo científico.
        """
        return (f"ArticuloCientifico(titulo={self.titulo}, doi={self.doi}, editor={self.editor}, "
                f"fecha_publicacion={self.fecha_publicacion}, periodicidad={self.periodicidad}, "
                f"volumen={self.volumen}, campo_interes={self.campo_interes}, estado={self.estado})")

    def actualizar_estado(self, nuevo_estado: str):
        """
        Actualiza el estado del artículo científico.
        
        :param nuevo_estado: Nuevo estado del artículo.
        :raise ValueError: Si el nuevo estado no es válido.
        """
        # Verifica si el nuevo estado es uno de los estados definidos en la clase Estado.
        if nuevo_estado in vars(Estado).values():
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado no válido")

    def actualizar_informacion(self, titulo: str = None, editor: str = None, 
                               fecha_publicacion: date = None, periodicidad: str = None, 
                               volumen: int = None, campo_interes: str = None):
        """
        Actualiza la información del artículo científico.
        
        :param titulo: Nuevo título del artículo (opcional).
        :param editor: Nuevo editor del artículo (opcional).
        :param fecha_publicacion: Nueva fecha de publicación del artículo (opcional).
        :param periodicidad: Nueva periodicidad de la publicación del artículo (opcional).
        :param volumen: Nuevo volumen del artículo (opcional).
        :param campo_interes: Nuevo campo de interés del artículo (opcional).
        """
        if titulo:
            self.titulo = titulo
        if editor:
            self.editor = editor
        if fecha_publicacion:
            self.fecha_publicacion = fecha_publicacion
        if periodicidad:
            self.periodicidad = periodicidad
        if volumen is not None:
            self.volumen = volumen
        if campo_interes:
            self.campo_interes = campo_interes