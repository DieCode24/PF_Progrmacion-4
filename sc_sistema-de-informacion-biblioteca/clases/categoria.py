class Categoria:
    """
    Clase que representa una categoría en el sistema de gestión de la biblioteca.
    """

    def __init__(self, nombre: str, categoria_id: int, descripcion: str):
        """
        Inicializa una nueva instancia de Categoria.

        :param nombre: Nombre de la categoría.
        :param categoria_id: Identificador único de la categoría.
        :param descripcion: Descripción de la categoría.
        """
        self.nombre = nombre
        self.categoria_id = categoria_id
        self.descripcion = descripcion
        self.subcategorias = []

    def __str__(self):
        """
        Retorna una representación en cadena de la categoría.

        :return: Una cadena que representa la categoría.
        """
        return f"Categoria(ID={self.categoria_id}, nombre={self.nombre}, descripcion={self.descripcion})"

    def agregar_subcategoria(self, subcategoria):
        """
        Agrega una subcategoría a la categoría actual.

        :param subcategoria: Objeto de tipo Categoria que representa la subcategoría a agregar.
        """
        self.subcategorias.append(subcategoria)

    def eliminar_subcategoria(self, subcategoria):
        """
        Elimina una subcategoría de la categoría actual.

        :param subcategoria: Objeto de tipo Categoria que representa la subcategoría a eliminar.
        """
        if subcategoria in self.subcategorias:
            self.subcategorias.remove(subcategoria)