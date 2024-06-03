from clases import Categoria

class CategoriaManager:
    """
    Clase que gestiona las operaciones CRUD para las categorías en el sistema de gestión de la biblioteca.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de CategoriaManager con una lista vacía de categorías.
        """
        self.categorias = []

    def crear_categoria(self, nombre: str, categoria_id: int, descripcion: str):
        """
        Crea una nueva categoría y la agrega al sistema.

        :param nombre: Nombre de la categoría.
        :param categoria_id: Identificador único de la categoría.
        :param descripcion: Descripción de la categoría.
        """
        nueva_categoria = Categoria(nombre, categoria_id, descripcion)
        self.categorias.append(nueva_categoria)

    def buscar_categoria_por_id(self, categoria_id: int):
        """
        Busca una categoría por su identificador único.

        :param categoria_id: Identificador único de la categoría a buscar.
        :return: La categoría si se encuentra, de lo contrario None.
        """
        for categoria in self.categorias:
            if categoria.categoria_id == categoria_id:
                return categoria
        return None

    def modificar_categoria(self, categoria_id: int, nuevo_nombre: str = None, nueva_descripcion: str = None):
        """
        Modifica los detalles de una categoría existente.

        :param categoria_id: Identificador único de la categoría a modificar.
        :param nuevo_nombre: Nuevo nombre para la categoría (opcional).
        :param nueva_descripcion: Nueva descripción para la categoría (opcional).
        :raise ValueError: Si la categoría no se encuentra.
        """
        categoria = self.buscar_categoria_por_id(categoria_id)
        if categoria:
            if nuevo_nombre:
                categoria.nombre = nuevo_nombre
            if nueva_descripcion:
                categoria.descripcion = nueva_descripcion
        else:
            raise ValueError("Categoría no encontrada")

    def eliminar_categoria(self, categoria_id: int):
        """
        Elimina una categoría del sistema.

        :param categoria_id: Identificador único de la categoría a eliminar.
        :raise ValueError: Si la categoría no se encuentra.
        """
        categoria = self.buscar_categoria_por_id(categoria_id)
        if categoria:
            self.categorias.remove(categoria)
        else:
            raise ValueError("Categoría no encontrada")