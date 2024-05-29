class Autor:
    def __init__(self, nombre: str, nacionalidad: str, fecha_nacimiento: str):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.libros = []
        self.cantidad_libros = len(self.libros)
        self.habilitado = True

    def __str__(self):
        return print(f"Nombre: {self.nombre}\nNacionalidad: {self.nacionalidad}\nFecha de nacimiento: {self.fecha_nacimiento}\nCantidad de libros: {self.cantidad_libros}\n")

