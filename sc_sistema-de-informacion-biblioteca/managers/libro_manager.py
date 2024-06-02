from typing import List
from clases.libro import Libro
from clases.libro import Estado
from clases.autor import Autor
from utils.validators import validar_input
from managers.autor_manager import AutorManager
from managers.data_manager import DataManager
from utils.helpers import pausar_sistema, limpiar_consola

class LibroManager():
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def registrar_libro(self, autores):
        genero = validar_input("Ingrese el género del libro: ", str)
        titulo = validar_input("Ingrese el título del libro: ", str)
        edicion = validar_input("Ingrese la edición del libro: ", str)
        anio_publicacion = validar_input("Ingrese el año de publicación del libro: ", int)
        editorial = validar_input("Ingrese la editorial del libro: ", str)
        estado = Estado.DISPONIBLE
        isbn = validar_input("Ingrese el ISBN del libro: ", str)
        idiomas = validar_input("Ingrese los idiomas del libro (separados por coma): ", list, separator=",")
        numero_copias = validar_input("Ingrese el número de copias del libro: ", int)
        libro = Libro(genero, titulo, edicion, anio_publicacion, editorial, autores, estado, isbn, idiomas, numero_copias)
        self.data_manager.books.append(libro)

    def listado_libros(self):
        print("1. Listar todos los libros")
        print("2. Listar libros activos")
        print("3. Listar libros inactivos")
        print ("0. Volver al menú principal")
        choice = validar_input("Choose an option: ", int)
        if choice == "1":
            limpiar_consola()
            self.listado_completo()
            pausar_sistema()
        elif choice == "2":
            limpiar_consola()
            self.listado_libros_activos()
            pausar_sistema()
        elif choice == "3":
            limpiar_consola()
            self.listado_libros_inactivos()
            pausar_sistema()
        elif choice == "0":
            pass
        else:
            limpiar_consola()
            print("Opción inválida. Intente de nuevo.")
            pausar_sistema()
    
    def listado_completo(self):
        for libro in self.data_manager.books:
            print("Título:", libro.titulo + "\n" + "ISBN:", libro.isbn)
            print("Autores:")
            for autor in libro.autores:
                print(autor.nombre)
                
    def listado_libros_activos(self):
        for libro in self.data_manager.books:
            if libro.estado == Estado.DISPONIBLE:
                print("Título:", libro.titulo + "\n" + "ISBN:", libro.isbn)
                print("Autores:")
                for autor in libro.autores:
                    print(autor.nombre)
                    
    def listado_libros_inactivos(self):
        for libro in self.data_manager.books:
            if libro.estado == Estado.NO_DISPONIBLE:
                print("Título:", libro.titulo + "\n" + "ISBN:", libro.isbn)
                print("Autores:")
                for autor in libro.autores:
                    print(autor.nombre)
                    
    
    
    # def show_menu(self):
    #     while True:
    #         print("\nArticle Manager")
    #         print("1. Registrar libro")
    #         print("2. ver libros")
    #         print("0. Back")
    #         choice = input("Choose an option: ")
    #         if choice == "1":
    #             autores = AutorManager.seleccionar_autores(self)
    #             self.registrar_libro(autores)
    #         elif choice == "2":
    #             self.listado_libros()
    #         elif choice == "0":
    #             break
    #         else:
    #             print("Invalid choice. Please try again.")
        
    def buscar_libro(self, query: str) -> List[Libro]:
        # buscar libro por título o ISBN y mostrar información
        resultados = []
        for libro in self.data_manager.books:
            if query.lower() in libro.titulo.lower() or query in libro.isbn:
                resultados.append(libro)
        print("Resultados de la búsqueda:")
        for libro in resultados:
            print("Título:", libro.titulo)
            print("ISBN:", libro.isbn)
            print("Autores:")
            for autor in libro.autores:
                print(autor.nombre)
        return resultados

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
            
    def load_mock_data(self):
        autor1 = Autor("Autor Uno", "Nacionalidad Uno", "Fecha Nacimiento Uno")
        autor2 = Autor("Autor Dos", "Nacionalidad Dos", "Fecha Nacimiento Dos")

        libro1 = Libro("Ciencia", "Libro de Ciencia", "Primera", 2020, "Editorial Uno", [autor1, autor2], Estado.DISPONIBLE, "123-456-789", ["Español"], 5)
        libro2 = Libro("Ficción", "Libro de Ficción", "Segunda", 2021, "Editorial Dos", [autor1], Estado.NO_DISPONIBLE, "987-654-321", ["Inglés"], 3)
        self.data_manager.books = [libro1, libro2]

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

# class LibroFactory:
#     @staticmethod
#     def create_libro(genero: str, titulo: str, edicion: str, anio_publicacion: int, editorial: str,
#                      autores: List[Autor], estado: Estado, isbn: str, idiomas: List[str], numero_copias: int) -> Libro:
#         return Libro(genero, titulo, edicion, anio_publicacion, editorial, autores, estado, isbn, idiomas, numero_copias)

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
