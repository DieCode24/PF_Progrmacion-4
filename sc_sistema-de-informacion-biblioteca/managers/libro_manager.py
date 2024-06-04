from typing import List
from clases.libro import Libro
from clases.libro import Estado
from clases.autor import Autor
from utils.validators import validar_input
from managers.autor_manager import AutorManager
from managers.data_manager import DataManager
from utils.helpers import pausar_sistema, limpiar_consola
from managers.copia_manager import CopiaManager

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

        # Validar que el ISBN no exista en la lista de libros
        for libro in self.data_manager.books:
            if libro.isbn == isbn:
                print("El ISBN ya existe en la base de datos.")
                return
        
        libro = Libro(genero, titulo, edicion, anio_publicacion, editorial, autores, estado, isbn, idiomas, numero_copias)
        genero = libro.genero
        print(f"Libro {genero} registrado exitosamente.")
        self.data_manager.books.append(libro)
        return libro

    def listado_libros(self):
        while True:
            print("1. Listar todos los libros")
            print("2. Listar libros activos")
            print("3. Listar libros inactivos")
            print ("0. Volver al menú principal")
            choice = input("Choose an option: ")
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
                break
            else:
                limpiar_consola()
                print("Opción inválida. Intente de nuevo.")
        
    def listado_completo(self):
        for libro in self.data_manager.books:
            self.print_libro(libro)
                
    def listado_libros_activos(self):
        for libro in self.data_manager.books:
            if libro.estado == Estado.DISPONIBLE:
                self.print_libro(libro)
                    
    def listado_libros_inactivos(self):
        for libro in self.data_manager.books:
            if libro.estado == Estado.NO_DISPONIBLE:
                self.print_libro(libro)
                
    def print_libro(self, libro: Libro):
        print("--------------------------------------")
        print("Título:", libro.titulo)
        print("ISBN:", libro.isbn)
        print("Autores:")
        for autor in libro.autores:
            print("> ", autor.nombre)
        print("Estado:", libro.estado)
        print("Idiomas:", libro.idiomas)
        print("Número de copias:", libro.numero_copias)
        print("--------------------------------------")
        
    def buscar_libro(self, query: str) -> List[Libro]:
        # buscar libro por título o ISBN y mostrar información
        resultados = []
        for libro in self.data_manager.books:
            if query.lower() in libro.titulo.lower() or query in libro.isbn:
                resultados.append(libro)
        print("Resultados de la búsqueda:")
        for libro in resultados:
            self.print_libro(libro)
        return resultados

    def modificar_libro(self, isbn: str, **kwargs):
        libro = self.get_libro_by_isbn(isbn)
        if libro:
            # validar que el libro esté disponible
            if libro.estado != Estado.DISPONIBLE:
                print("El libro no está disponible para modificar.")
                return
            
            # mostrar menú de opciones para modificar
            while True:
                print("1. Modificar título")
                print("2. Modificar género")
                print("3. Modificar edición")
                print("4. Modificar año de publicación")
                print("5. Modificar editorial")
                # print("6. Modificar autores")
                print("7. Modificar idiomas")
                print("8. Modificar número de copias")
                print("0. Volver al menú principal")
                choice = input("Choose an option: ")
                if choice == "1":
                    nuevo_titulo = validar_input("Ingrese el nuevo título: ", str)
                    libro.titulo = nuevo_titulo
                elif choice == "2":
                    nuevo_genero = validar_input("Ingrese el nuevo género: ", str)
                    libro.genero = nuevo_genero
                elif choice == "3":
                    nueva_edicion = validar_input("Ingrese la nueva edición: ", str)
                    libro.edicion = nueva_edicion
                elif choice == "4":
                    nuevo_anio = validar_input("Ingrese el nuevo año de publicación: ", int)
                    libro.anio_publicacion = nuevo_anio
                elif choice == "5":
                    nueva_editorial = validar_input("Ingrese la nueva editorial: ", str)
                    libro.editorial = nueva_editorial
                elif choice == "6":
                    nuevo_autor = validar_input("Ingrese el nuevo autor: ", str)
                    libro.autores.append(nuevo_autor)
                elif choice == "7":
                    nuevos_idiomas = validar_input("Ingrese los nuevos idiomas (separados por coma): ", list, separator=",")
                    libro.idiomas = nuevos_idiomas
                elif choice == "8":
                    nuevo_numero_copias = validar_input("Ingrese el nuevo número de copias: ", int)
                    libro.numero_copias = nuevo_numero_copias
                elif choice == "0":
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
                
            
    def habilitar_libro(self, isbn: str):
        libro = self.get_libro_by_isbn(isbn)
        if libro:
            libro.estado = Estado.DISPONIBLE

    def inhabilitar_libro(self, isbn: str):
        libro = self.get_libro_by_isbn(isbn)
        if libro:
            libro.estado = Estado.NO_DISPONIBLE
            
    def load_mock_data(self):
        autor1 = Autor("Juan Marulanda", "Colombia", "2004-06-08")
        autor2 = Autor("Daniel", "Venezuela", "2002-02-08")
        
        libro1 = Libro("Ciencia", "Libro de Ciencia", "Primera", 2020, "Editorial Uno", [autor1, autor2], Estado.DISPONIBLE, "123-456-789", ["Español", "Aleman", "Ingles"], 5)
        libro2 = Libro("Ficción", "Libro de Ficción", "Segunda", 2021, "Editorial Dos", [autor1], Estado.NO_DISPONIBLE, "987-654-321", ["Inglés"], 3)
        hola = AutorManager(self.data_manager)
        hola.asociar_libro([autor1,autor2], libro1)
        
        self.data_manager.autores = [autor1, autor2]

        self.data_manager.books = [libro1, libro2]
        
        asociador_copias = CopiaManager(self.data_manager)
        asociador_copias.registrar_copias("123-456-789", libro1.estado,5)
        print("Datos de prueba cargados exitosamente.")

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
