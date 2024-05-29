class Autor:
    def __init__(self, nombre: str, nacionalidad: str, fecha_nacimiento: str):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.libros = []
        self.cantidad_libros = len(self.libros)
        self.habilitado = True

    def __str__(self):
        return self.nombre
