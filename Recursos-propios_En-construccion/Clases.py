# Clases para el planteamiento

class Tesis:
    def __init__(self, nombre_autor, institucion_academica, fecha_investigacion, fecha_presentacion, campo_estudio, estado, numero_paginas):
        self.nombre_autor = nombre_autor
        self.institucion_academica = institucion_academica
        self.fecha_investigacion = fecha_investigacion
        self.fecha_presentacion = fecha_presentacion
        self.campo_estudio = campo_estudio
        self.estado = estado
        self.numero_paginas = numero_paginas

    def registrar_tesis(self):
        pass

    def buscar_tesis(self):
        pass

    def modificar_tesis(self):
        pass

    def eliminar_tesis(self):
        pass

    def realizar_prestamo_tesis(self):
        pass

    def devolver_tesis(self):
        pass

    def generar_multa(self):
        pass

    def levantar_multa(self):
        pass

class ArticuloCientifico:
    def __init__(self, titulo, doi, nombre_editor, fecha_publicacion, periodicidad, numero_volumen, campo_interes, estado):
        self.titulo = titulo
        self.doi = doi
        self.nombre_editor = nombre_editor
        self.fecha_publicacion = fecha_publicacion
        self.periodicidad = periodicidad
        self.numero_volumen = numero_volumen
        self.campo_interes = campo_interes
        self.estado = estado

    def registrar_articulo(self):
        pass

    def buscar_articulo(self):
        pass

    def modificar_articulo(self):
        pass

    def eliminar_articulo(self):
        pass

    def realizar_prestamo_articulo(self):
        pass

    def devolver_articulo(self):
        pass

    def generar_multa(self):
        pass

    def levantar_multa(self):
        pass

class Libro:
    def __init__(self, genero, titulo, edicion, anio_publicacion, editorial, autores, estado, isbn, idiomas, numero_copias):
        self.genero = genero
        self.titulo = titulo
        self.edicion = edicion
        self.anio_publicacion = anio_publicacion
        self.editorial = editorial
        self.autores = autores
        self.estado = estado
        self.isbn = isbn
        self.idiomas = idiomas
        self.numero_copias = numero_copias

    def registrar_libro(self):
        pass

    def buscar_libro(self):
        pass

    def modificar_libro(self):
        pass

    def habilitar_libro(self):
        pass

    def inhabilitar_libro(self):
        pass

    def realizar_prestamo_libro(self):
        pass

    def devolver_libro(self):
        pass

    def generar_multa(self):
        pass

    def levantar_multa(self):
        pass

class Categoria:
    def __init__(self, nombre, id, descripcion, subcategorias):
        self.nombre = nombre
        self.id = id
        self.descripcion = descripcion
        self.subcategorias = subcategorias

    def crear_categoria(self):
        pass

    def buscar_categoria(self):
        pass

    def modificar_categoria(self):
        pass

    def eliminar_categoria(self):
        pass

class Copia:
    def __init__(self, identificador, estado, isbn):
        self.identificador = identificador
        self.estado = estado
        self.isbn = isbn

    def registrar_copia(self):
        pass

    def eliminar_copia(self):
        pass

class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, cantidad_libros, libros_autor):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.cantidad_libros = cantidad_libros
        self.libros_autor = libros_autor

    def crear_autor(self):
        pass

    def modificar_autor(self):
        pass

    def actualizar_informacion_autor(self):
        pass

    def habilitar_autor(self):
        pass

    def inhabilitar_autor(self):
        pass

class Lector:
    def __init__(self, nombre, id, telefono, direccion, estado, cantidad_libros_prestados, libros_prestados, tiene_multa):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado
        self.cantidad_libros_prestados = cantidad_libros_prestados
        self.libros_prestados = libros_prestados
        self.tiene_multa = tiene_multa

    def registrar_lector(self):
        pass

    def buscar_lector(self):
        pass

    def modificar_lector(self):
        pass

    def habilitar_lector(self):
        pass

    def inhabilitar_lector(self):
        pass

class Prestamo:
    def __init__(self, id_prestamo, id_libro, id_lector, dias_prestamo, fecha_prestamo, fecha_entrega):
        self.id_prestamo = id_prestamo
        self.id_libro = id_libro
        self.id_lector = id_lector
        self.dias_prestamo = dias_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega

    def registrar_prestamo(self):
        pass

    def consultar_prestamo(self):
        pass

    def calcular_fecha_entrega(self):
        pass

class Multa:
    def __init__(self, id_multa, id_prestamo, dias_retraso, fecha_entrega, fecha_finalizacion_multa, estado):
        self.id_multa = id_multa
        self.id_prestamo = id_prestamo
        self.dias_retraso = dias_retraso
        self.fecha_entrega = fecha_entrega
        self.fecha_finalizacion_multa = fecha_finalizacion_multa
        self.estado = estado

    def generar_multa(self):
        pass

    def levantar_multa(self):
        pass

    def calcular_dias_retraso(self):
        pass