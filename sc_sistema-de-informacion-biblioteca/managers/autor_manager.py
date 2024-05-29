# Juan Marulanda
from clases.autor import Autor
from datetime import datetime

class AutorManager:
    def __init__(self):
        self.autores = []

    def registrar_autor(self):
        nombre = input("Ingrese el nombre del autor: ")
        nacionalidad = input("Ingrese la nacionalidad del autor: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del autor (YYYY-MM-DD): ")
        self.agregar_autor(nombre, nacionalidad, fecha_nacimiento)
        print(f"Autor {nombre} registrado exitosamente.")

    def agregar_autor(self, nombre: str, nacionalidad: str, fecha_nacimiento: str):
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        autor = Autor(nombre, nacionalidad, fecha_nacimiento)
        self.autores.append(autor)

    def buscar_autor(self, nombre: str):
        for autor in self.autores:
            if autor.nombre == nombre:
                return autor
        return None

    def modificar_autor(self):
        nombre = input("Ingrese el nombre del autor que desea modificar: ")
        autor = self.buscar_autor(nombre)
        if autor:
            nacionalidad = input("Ingrese la nueva nacionalidad del autor: ")
            fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del autor (YYYY-MM-DD): ")
            self.actualizar_autor(autor, nacionalidad, fecha_nacimiento)
            print(f"Autor {nombre} modificado exitosamente.")
        else:
            print("El autor no existe.")

    def actualizar_autor(self, autor: Autor, nacionalidad: str, fecha_nacimiento: str):
        autor.nacionalidad = nacionalidad
        autor.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

    def mostrar_informacion_autor(self, nombre: str):
        autor = self.buscar_autor(nombre)
        if autor:
            print(f"Información Actual de {autor.nombre}:")
            print(f"Nacionalidad: {autor.nacionalidad}")
            print(f"Fecha de nacimiento: {autor.fecha_nacimiento.strftime('%Y-%m-%d')}")
            print("Libros:")
            for libro in autor.libros:
                print(libro)
        else:
            print("El autor no existe")

    def see_authors(self, bool=None):
        if bool is None:
            print("Autores:")
            for autor in self.autores:
                print(autor)
        elif bool:
            print("Autores Habilitados:")
            for autor in self.autores:
                if autor.habilitado:
                    print(autor)
        else:
            print("Autores Inhabilitados:")
            for autor in self.autores:
                if not autor.habilitado:
                    print(autor)

    def listas_d_autores(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Todos los autores")
            print("2. Autores habilitados")
            print("3. Autores inhabilitados")
            print("0. Salir")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.see_authors()
            elif opcion == "2":
                self.see_authors(True)
            elif opcion == "3":
                self.see_authors(False)
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")