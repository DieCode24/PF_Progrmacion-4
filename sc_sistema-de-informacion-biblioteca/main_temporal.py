import datetime

# Función para limpiar la consola (funciona en Windows y Unix)
import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clase base Producto
class Producto:
    def __init__(self, titulo, estado):
        self.titulo = titulo
        self.estado = estado  # Estado puede ser Disponible, Prestado en biblioteca, En revisión, En reparación, No disponible

    def modificar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

# Clase Tesis
class Tesis(Producto):
    def __init__(self, titulo, autores, institucion_academica, fecha_investigacion, fecha_presentacion, campo_estudio, estado, numero_paginas):
        super().__init__(titulo, estado)
        self.autores = autores
        self.institucion_academica = institucion_academica
        self.fecha_investigacion = fecha_investigacion
        self.fecha_presentacion = fecha_presentacion
        self.campo_estudio = campo_estudio
        self.numero_paginas = numero_paginas

    def registrar_tesis(self):
        pass  # Lógica para registrar tesis

    def buscar_tesis(self):
        pass  # Lógica para buscar tesis

    def modificar_tesis(self):
        pass  # Lógica para modificar tesis

    def eliminar_tesis(self):
        pass  # Lógica para eliminar tesis

# Clase ArticuloCientifico
class ArticuloCientifico(Producto):
    def __init__(self, titulo, doi, nombre_editor, fecha_publicacion, periodicidad, numero_volumen, campo_interes, estado):
        super().__init__(titulo, estado)
        self.doi = doi
        self.nombre_editor = nombre_editor
        self.fecha_publicacion = fecha_publicacion
        self.periodicidad = periodicidad
        self.numero_volumen = numero_volumen
        self.campo_interes = campo_interes

    def registrar_articulo(self):
        pass  # Lógica para registrar artículo científico

    def buscar_articulo(self):
        pass  # Lógica para buscar artículos científicos

    def modificar_articulo(self):
        pass  # Lógica para modificar artículos científicos

    def eliminar_articulo(self):
        pass  # Lógica para eliminar artículos científicos

# Clase Libro
class Libro(Producto):
    def __init__(self, titulo, genero, edicion, anio_publicacion, editorial, autores, estado, isbn, idiomas, numero_copias):
        super().__init__(titulo, estado)
        self.genero = genero
        self.edicion = edicion
        self.anio_publicacion = anio_publicacion
        self.editorial = editorial
        self.autores = autores
        self.isbn = isbn
        self.idiomas = idiomas
        self.numero_copias = numero_copias

    def registrar_libro(self):
        pass  # Lógica para registrar libro

    def buscar_libro(self):
        pass  # Lógica para buscar libros

    def modificar_libro(self):
        pass  # Lógica para modificar libros

    def habilitar_libro(self):
        pass  # Lógica para habilitar libro

    def inhabilitar_libro(self):
        pass  # Lógica para inhabilitar libro

# Función para seleccionar el rol y mostrar las funcionalidades
def seleccionar_rol():
    print("Bienvenido al Sistema de Información de la Biblioteca")
    print("Seleccione su rol:")
    print("1. Lector")
    print("2. Bibliotecario")

    rol = input("Ingrese el número de su rol: ")

    if rol == "1":
        print("\nFuncionalidades disponibles para Lectores:")
        print("1. Buscar libros")
        print("2. Realizar préstamo")
        print("3. Devolver libro")
        print("4. Consultar multas")
    elif rol == "2":
        print("\nFuncionalidades disponibles para Bibliotecarios:")
        print("1. Registrar productos (libros, tesis, artículos científicos)")
        print("2. Modificar productos")
        print("3. Eliminar productos (tesis, artículos científicos)")
        print("4. Realizar préstamo")
        print("5. Devolver producto")
        print("6. Gestionar categorías")
        print("7. Gestionar autores")
        print("8. Gestionar lectores")
        print("9. Gestionar préstamos")
        print("10. Gestionar multas")
    else:
        print("Rol no válido. Intente nuevamente.")
        seleccionar_rol()

# Ejecución del programa principal
if __name__ == "__main__":
    seleccionar_rol()