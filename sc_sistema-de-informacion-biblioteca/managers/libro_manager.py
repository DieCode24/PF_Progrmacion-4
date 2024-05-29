from typing import List
from clases.libro import Libro
from clases.libro import Estado
from clases.autor import Autor
from utils.validators import validar_input

class LibroManager():
    def __init__(self):
        self.libros = [
            Libro("Ciencia", "Libro de Ciencia", "Primera", 2020, "Editorial Uno", [Autor("Autor Uno", "Nacionalidad Uno", "Fecha Nacimiento Uno"), Autor("Autor Dos", "Nacionalidad Dos", "Fecha Nacimiento Dos")], Estado.DISPONIBLE, "123-456-789", ["Español"], 5)
        ]

    def registrar_libro(self):
        genero = validar_input("Ingrese el género del libro: ", str)
        titulo = validar_input("Ingrese el título del libro: ", str)
        edicion = validar_input("Ingrese la edición del libro: ", str)
        anio_publicacion = validar_input("Ingrese el año de publicación del libro: ", int)
        editorial = validar_input("Ingrese la editorial del libro: ", str)
        autores = validar_input("Ingrese los autores del libro (separados por coma): ", list, separator=",")
        autores = validar_input("Ingrese los autores del libro (separados por coma): ", list, separator=",")
        estado = Estado.DISPONIBLE
        isbn = validar_input("Ingrese el ISBN del libro: ", str)
        idiomas = validar_input("Ingrese los idiomas del libro (separados por coma): ", list, separator=",")
        numero_copias = validar_input("Ingrese el número de copias del libro: ", int)
        libro = Libro(genero, titulo, edicion, anio_publicacion, editorial, autores, estado, isbn, idiomas, numero_copias)
        self.libros.append(libro)

    def listado_libros(self):
        for libro in self.libros:
            print("Título:", libro.titulo + "\n" + "ISBN:", libro.isbn)
        
    def buscar_libro(self, query: str) -> List[Libro]:
        return [libro for libro in self.libros if query in libro.titulo or query in libro.isbn]

    def modificar_libro(self, isbn: str, **kwargs):
        libro = self.get_libro_by_isbn(isbn)
        if libro:
            for key, value in kwargs.items():
                if hasattr(libro, key):
                    setattr(libro, key, value)

    def habilitar_libro(self, isbn: str):
        libro = self.get_libro_by_isbn(isbn)
        if libro:
            libro.estado = Estado.DISPONIBLE

    def inhabilitar_libro(self, isbn: str):
        libro = self.get_libro_by_isbn(isbn)
        if libro:
            libro.estado = Estado.NO_DISPONIBLE

    def realizar_prestamo_libro(self, isbn: str):
        libro = self.get_libro_by_isbn(isbn)
        if libro and libro.estado == Estado.DISPONIBLE:
            libro.estado = Estado.PRESTADO

    def devolver_libro(self, isbn: str):
        libro = self.get_libro_by_isbn(isbn)
        if libro and libro.estado == Estado.PRESTADO:
            libro.estado = Estado.DISPONIBLE

    def generar_multa(self, isbn: str):
        libro = self.get_libro_by_isbn(isbn)
        if libro:
            # Lógica para generar multa
            pass

    def levantar_multa(self, isbn: str):
        libro = self.get_libro_by_isbn(isbn)
        if libro:
            # Lógica para levantar multa
            pass

    def get_libro_by_isbn(self, isbn: str) -> Libro:
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

class LibroFactory:
    @staticmethod
    def create_libro(genero: str, titulo: str, edicion: str, anio_publicacion: int, editorial: str,
                     autores: List[Autor], estado: Estado, isbn: str, idiomas: List[str], numero_copias: int) -> Libro:
        return Libro(genero, titulo, edicion, anio_publicacion, editorial, autores, estado, isbn, idiomas, numero_copias)

# # Uso del Singleton y Factory Method para la gestión de libros
# if __name__ == "__main__":
#     manager = LibroManager()

#     autor1 = Autor("Autor Uno", "Nacionalidad Uno", "Fecha Nacimiento Uno")
#     autor2 = Autor("Autor Dos", "Nacionalidad Dos", "Fecha Nacimiento Dos")

#     libro1 = LibroFactory.create_libro(
#         genero="Ciencia",
#         titulo="Libro de Ciencia",
#         edicion="Primera",
#         anio_publicacion=2020,
#         editorial="Editorial Uno",
#         autores=[autor1, autor2],
#         estado=Estado.DISPONIBLE,
#         isbn="123-456-789",
#         idiomas=["Español"],
#         numero_copias=5
#     )
#     manager.registrar_libro(libro1)

#     resultados = manager.buscar_libro("Libro de Ciencia")
#     for libro in resultados:
#         print(libro.titulo, libro.isbn)

#     manager.modificar_libro("123-456-789", titulo="Nuevo Título de Ciencia")

#     libro_modificado = manager.get_libro_by_isbn("123-456-789")
#     print(libro_modificado.titulo)

#     manager.habilitar_libro("123-456-789")
#     manager.inhabilitar_libro("123-456-789")
