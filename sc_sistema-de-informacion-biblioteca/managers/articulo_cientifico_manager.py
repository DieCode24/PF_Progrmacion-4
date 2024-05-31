from datetime import date
from typing import List, Optional
from clases.articulo_cientifico import ArticuloCientifico
from clases.estado import Estado

class ArticuloCientificoManager:
    """
    Clase que gestiona las operaciones CRUD para los artículos científicos en el sistema de información de la biblioteca.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de ArticuloCientificoManager con una lista vacía de artículos científicos.
        """
        self.articulos = []

    def registrar_articulo(self, titulo: str, doi: str, editor: str, fecha_publicacion: date, periodicidad: str, volumen: int, campo_interes: str, estado: str = Estado.DISPONIBLE) -> ArticuloCientifico:
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
        nuevo_articulo = ArticuloCientifico(titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo_interes, estado)
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

    def modificar_articulo(self, doi: str, **kwargs) -> Optional[ArticuloCientifico]:
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
            raise ValueError("Artículo científico no encontrado")

    def eliminar_articulo(self, doi: str) -> bool:
        """
        Elimina un artículo científico del sistema.
        
        :param doi: Identificador único del artículo a eliminar.
        :return: True si el artículo fue eliminado, False de lo contrario.
        :raise ValueError: Si el artículo no se encuentra.
        """
        articulo = self.buscar_articulo(doi)
        if articulo:
            self.articulos.remove(articulo)
            return True
        else:
            return False

    def listar_articulos(self) -> List[ArticuloCientifico]:
        """
        Lista todos los artículos científicos registrados en el sistema.
        
        :return: Lista de artículos científicos.
        """
        return self.articulos

    def registrar_articulo_desde_consola(self):
        """
        Registra un nuevo artículo científico desde la consola.
        """
        titulo = input("Ingrese el título del artículo: ")
        doi = input("Ingrese el DOI del artículo: ")
        editor = input("Ingrese el editor del artículo: ")
        fecha_str = input("Ingrese la fecha de publicación (YYYY-MM-DD): ")
        fecha_publicacion = date.fromisoformat(fecha_str)
        periodicidad = input("Ingrese la periodicidad del artículo (Mensual, Semanal): ")
        volumen = int(input("Ingrese el volumen del artículo: "))
        campo_interes = input("Ingrese el campo de interés del artículo: ")

        self.registrar_articulo(titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo_interes, Estado.DISPONIBLE)
        print("Artículo científico registrado exitosamente.")

    def buscar_articulo_desde_consola(self):
        """
        Busca un artículo científico desde la consola.
        """
        doi = input("Ingrese el DOI del artículo a buscar: ")
        articulo = self.buscar_articulo(doi)
        if articulo:
            print(articulo)
        else:
            print("Artículo científico no encontrado.")

    def modificar_articulo_desde_consola(self):
        """
        Modifica un artículo científico desde la consola.
        """
        doi = input("Ingrese el DOI del artículo a modificar: ")
        kwargs = {}
        titulo = input("Ingrese el nuevo título del artículo (o presione Enter para omitir): ")
        if titulo:
            kwargs['titulo'] = titulo
        editor = input("Ingrese el nuevo editor del artículo (o presione Enter para omitir): ")
        if editor:
            kwargs['editor'] = editor
        fecha_str = input("Ingrese la nueva fecha de publicación (YYYY-MM-DD) (o presione Enter para omitir): ")
        if fecha_str:
            kwargs['fecha_publicacion'] = date.fromisoformat(fecha_str)
        periodicidad = input("Ingrese la nueva periodicidad del artículo (Mensual, Semanal) (o presione Enter para omitir): ")
        if periodicidad:
            kwargs['periodicidad'] = periodicidad
        volumen = input("Ingrese el nuevo volumen del artículo (o presione Enter para omitir): ")
        if volumen:
            kwargs['volumen'] = int(volumen)
        campo_interes = input("Ingrese el nuevo campo de interés del artículo (o presione Enter para omitir): ")
        if campo_interes:
            kwargs['campo_interes'] = campo_interes

        try:
            self.modificar_articulo(doi, **kwargs)
            print("Artículo científico modificado exitosamente.")
        except ValueError as e:
            print(e)

    def eliminar_articulo_desde_consola(self):
        """
        Elimina un artículo científico desde la consola.
        """
        doi = input("Ingrese el DOI del artículo a eliminar: ")
        try:
            if self.eliminar_articulo(doi):
                print("Artículo científico eliminado exitosamente.")
            else:
                print("Artículo científico no encontrado.")
        except ValueError as e:
            print(e)