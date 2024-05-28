# Juan Marulanda
from clases import Autor
from datetime import datetime 

class AutorManager:
    def __init__(self):
        self.autores = []

    def agregar_autor(self, nombre: str, nacionalidad: str, fecha_nacimiento: str):
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        autor = Autor(nombre, nacionalidad, fecha_nacimiento)
        self.autores.append(autor)

    def listar_autores(self):
        for autor in self.autores:
            print(autor)

    def buscar_autor(self, nombre: str):
        for autor in self.autores:
            if autor.nombre == nombre:
                return autor
        return None


    def agregar_libro(self, nombre_autor: str, libro):
        autor = self.buscar_autor(nombre_autor)
        if autor:
            autor.libros.append(libro)
            autor.cantidad_libros = len(autor.libros)
            return True
        return False

    def listar_libros(self, nombre_autor: str):
        autor = self.buscar_autor(nombre_autor)
        if autor:
            for libro in autor.libros:
                print(libro)
        else:
            print("El autor no existe")

    def buscar_libro(self, nombre_autor: str, nombre_libro: str):
        autor = self.buscar_autor(nombre_autor)
        if autor:
            for libro in autor.libros:
                if libro.nombre == nombre_libro:
                    return libro
        return None

    def eliminar_libro(self, nombre_autor: str, nombre_libro: str):
        autor = self.buscar_autor(nombre_autor)
        if autor:
            libro = self.buscar_libro(nombre_autor, nombre_libro)
            if libro:
                autor.libros.remove(libro)
                autor.cantidad_libros = len(autor.libros)
                return True
        return False
    
