from clases.articulo_cientifico import ArticuloCientifico
from datetime import date
from typing import List, Optional

class ArticuloCientificoManager:
    """
    Clase que gestiona las operaciones CRUD para los artículos científicos en el sistema de información de la biblioteca.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de ArticuloCientificoManager con una lista vacía de artículos científicos.
        """
        self.articulos = []

    def registrar_articulo(self, titulo: str, doi: str, editor: str, fecha_publicacion: date, 
                           periodicidad: str, volumen: int, campo_interes: str, estado: str = "Disponible"):
        """
        Registra un nuevo artículo científico en el sistema.
        
        :param titulo: Título del artículo.
        :param doi: Identificador único del artículo (DOI).
        :param editor: Nombre del editor del artículo.
        :param fecha_publicacion: Fecha de publicación del artículo.
        :param periodicidad: Periodicidad de la publicación (mensual, semanal, etc.).
        :param volumen: Número de volumen del artículo.
        :param campo_interes: Campo de interés del artículo.
        :param estado: Estado del artículo (predeterminado a "Disponible").
        :return: El artículo científico recién creado.
        """
        nuevo_articulo = ArticuloCientifico(titulo, doi, editor, fecha_publicacion, periodicidad, 
                                            volumen, campo_interes, estado)
        self.articulos.append(nuevo_articulo)
        return nuevo_articulo

    def buscar_articulo(self, doi: str) -> Optional[ArticuloCientifico]:
        """
        Busca un artículo científico por su DOI.
        
        :param doi: Identificador único del artículo (DOI).
        :return: El artículo científico si se encuentra, de lo contrario None.
        """
        for articulo in self.articulos:
            if articulo.doi == doi:
                return articulo
        return None

    def modificar_articulo(self, doi: str, **kwargs):
        """
        Modifica la información de un artículo científico existente.
        
        :param doi: Identificador único del artículo a modificar.
        :param kwargs: Diccionario de atributos a actualizar.
        :return: El artículo científico modificado.
        :raise ValueError: Si el artículo no se encuentra.
        """
        articulo = self.buscar_articulo(doi)
        if articulo:
            articulo.actualizar_informacion(**kwargs)
            return articulo
        else:
            raise ValueError("Artículo no encontrado")

    def eliminar_articulo(self, doi: str):
        """
        Elimina un artículo científico del sistema.
        
        :param doi: Identificador único del artículo a eliminar.
        :raise ValueError: Si el artículo no se encuentra.
        """
        articulo = self.buscar_articulo(doi)
        if articulo:
            self.articulos.remove(articulo)
        else:
            raise ValueError("Artículo no encontrado")

    def listar_articulos(self) -> List[ArticuloCientifico]:
        """
        Lista todos los artículos científicos registrados en el sistema.
        
        :return: Lista de artículos científicos.
        """
        return self.articulos