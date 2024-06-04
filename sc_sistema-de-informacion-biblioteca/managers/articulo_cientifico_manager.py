from datetime import date
from typing import List, Optional

from clases.articulo_cientifico import ArticuloCientifico
from clases.estado import Estado
from utils.validators import validar_input


class ArticuloCientificoManager:
    """
    Clase que gestiona las operaciones CRUD para los artículos científicos en el sistema de información de la biblioteca.
    """

    def __init__(self, data_manager):
        """
        Inicializa una nueva instancia de ArticuloCientificoManager con una lista vacía de artículos científicos.
        """
        self.data_manager = data_manager

    def registrar_articulo(self, titulo: str, doi: str, editor: str, fecha_publicacion: date, periodicidad: str, volumen: int, campo_interes: str, estado: str = Estado.DISPONIBLE) -> ArticuloCientifico:
        """
        Registra un nuevo artículo científico en el sistema.
        
        :param titulo: Título del artículo.
        :param doi: Identificador único del artículo (DOI).
        :param editor: Nombre del editor del artículo.
        :param fecha_publicacion: Fecha de publicación del artículo.
        :param periodicidad: Periodicidad de la publicación (mensual, semanal).
        :param volumen: Número de volumen del artículo.
        :param campo_interes: Campo de interés del artículo.
        :param estado: Estado del artículo (predeterminado a "Disponible").
        :return: El artículo científico recién creado.
        """
        nuevo_articulo = ArticuloCientifico(titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo_interes, estado)
        self.data_manager.articulos.append(nuevo_articulo)
        return nuevo_articulo

    def buscar_articulo(self, doi: str) -> Optional[ArticuloCientifico]:
        """
        Busca un artículo científico por su DOI.
        
        :param doi: Identificador único del artículo (DOI).
        :return: El artículo científico si se encuentra, de lo contrario None.
        """
        for articulo in self.data_manager.articulos:
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
            self.data_manager.articulos.remove(articulo)
            return True
        else:
            return False

    def listar_articulos(self):
        print("LISTA DE ARTÍCULOS CIENTÍFICOS\n")
        if not self.data_manager.articulos:
            print("No hay artículos científicos registrados")
            return
        for idx, articulo in enumerate(self.data_manager.articulos, start=1):
            print(f"{idx}. Título: {articulo.titulo}, DOI: {articulo.doi}, Editor: {articulo.editor}")
            print(f"   Fecha de Publicación: {articulo.fecha_publicacion}, Periodicidad: {articulo.periodicidad}, Volumen: {articulo.volumen}")
            print(f"   Campo de Interés: {articulo.campo_interes}, Estado: {articulo.estado}\n")

    def registrar_articulo_desde_consola(self):
        """
        Registra un nuevo artículo científico desde la consola.
        """
        titulo = validar_input("Ingrese el título del artículo: ", str)
        doi = validar_input("Ingrese el DOI del artículo: ", str)
        editor = validar_input("Ingrese el editor del artículo: ", str)
        fecha_str = validar_input("Ingrese la fecha de publicación (YYYY-MM-DD): ", str)
        fecha_publicacion = date.fromisoformat(fecha_str)
        periodicidad = validar_input("Ingrese la periodicidad del artículo (Mensual, Semanal): ", str)
        volumen = validar_input("Ingrese el volumen del artículo: ", int)
        campo_interes = validar_input("Ingrese el campo de interés del artículo: ", str)

        self.registrar_articulo(titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo_interes, Estado.DISPONIBLE)
        print("Artículo científico registrado exitosamente.")


    def mostrar_detalles_articulo(articulo, idx):
        """
        Muestra los detalles de un artículo.
        
        Args:
            articulo (Articulo): El objeto Artículo cuyos detalles se mostrarán.
            idx (int): El índice del artículo en la lista.
        """
        print(f"{idx}. Título: {articulo.titulo}, DOI: {articulo.doi}, Editor: {articulo.editor}")
        print(f"   Fecha de Publicación: {articulo.fecha_publicacion}, Periodicidad: {articulo.periodicidad}, Volumen: {articulo.volumen}")
        print(f"   Campo de Interés: {articulo.campo_interes}, Estado: {articulo.estado}\n")

    def buscar_articulo_desde_consola(self):
        """
        Busca un artículo científico desde la consola.
        """
        print("¿Cómo desea buscar el artículo científico?")
        print("1. Título")
        print("2. Campo de interés")
        print("0. Salir")

        opcion = validar_input("\n> Ingrese una opción => ", int)

        if opcion == 1:
            self.buscar_por_titulo()
        elif opcion == 2:
            self.buscar_por_campo()
        elif opcion == 0:
            return
        else:
            print("Opción no válida")
            return
        
    def buscar_por_titulo(self):
        print("\tBuscando por título\n")
        titulo = validar_input("Ingrese el título: ", str).title()
        articulos_encontrados = [art for art in self.data_manager.articulos if titulo in art.titulo]

        if not articulos_encontrados:
            print(f"No se encontraron artículos con el título {titulo}.")
        else:
            for idx, articulo in enumerate(articulos_encontrados, start=1):
                ArticuloCientificoManager.mostrar_detalles_articulo(articulo, idx)


    def buscar_por_campo(self):
        print("\tBuscando por campo de interés\n")
        campo = validar_input("Ingrese el campo de interés: ", str).lower().title()
        articulos_encontrados = [art for art in self.data_manager.articulos if campo in art.campo_interes]

        if not articulos_encontrados:
            print(f"No se encontraron artículos en el campo de interés {campo}.")
        else:
            for idx, articulo in enumerate(articulos_encontrados, start=1):
                ArticuloCientificoManager.mostrar_detalles_articulo(articulo, idx)

    def modificar_articulo_desde_consola(self):
        """
        Modifica un artículo científico desde la consola.
        """
        doi = validar_input("Ingrese el DOI del artículo a modificar: ", str)
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
        doi = validar_input("Ingrese el DOI del artículo a eliminar: ", str)
        try:
            if self.eliminar_articulo(doi):
                print("Artículo científico eliminado exitosamente.")
            else:
                print("Artículo científico no encontrado.")
        except ValueError as e:
            print(e)