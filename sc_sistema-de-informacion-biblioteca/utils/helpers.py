import os

def system_pause():
    """Pause the system, works on Windows and Linux."""
    try:
        if os.name == 'nt':  # For Windows
            os.system('pause')
        else:  # For Linux/Unix
            os.system('read -n 1 -s -r -p "Press any key to continue..."')
    except Exception as e:
        print(f"Error al pausar el sistema: {e}")


def mostrar_menu():
    print("Sistema de Información Biblioteca")
    print("Seleccione una opción:")
    print("1. Gestión de Tesis")
    print("2. Gestión de Artículos Científicos")
    print("3. Gestión de Libros")
    print("4. Gestión de Categorías")
    print("5. Gestión de Autores")
    print("6. Gestión de Lectores")
    print("7. Gestión de Préstamos")
    print("8. Gestión de Multas")
    print("0. Salir")

def gestionar_tesis():
    print("Gestión de Tesis")
    print("1. Registrar Tesis")
    print("2. Buscar Tesis")
    print("3. Modificar Tesis")
    print("4. Eliminar Tesis")
    print("5. Realizar Préstamo de Tesis")
    print("6. Devolver Tesis")
    print("7. Generar Multa")
    print("8. Levantar Multa")
    print("0. Volver al menú principal")

def gestionar_articulos():
    print("Gestión de Artículos Científicos")
    print("1. Registrar Artículo")
    print("2. Buscar Artículo")
    print("3. Modificar Artículo")
    print("4. Eliminar Artículo")
    print("5. Realizar Préstamo de Artículo")
    print("6. Devolver Artículo")
    print("7. Generar Multa")
    print("8. Levantar Multa")
    print("0. Volver al menú principal")

def gestionar_libros():
    print("Gestión de Libros")
    print("1. Registrar Libro")
    print("2. Buscar Libro")
    print("3. Modificar Libro")
    print("4. Habilitar Libro")
    print("5. Inhabilitar Libro")
    print("6. Realizar Préstamo de Libro")
    print("7. Devolver Libro")
    print("8. Generar Multa")
    print("9. Levantar Multa")
    print("0. Volver al menú principal")

def gestionar_categorias():
    print("Gestión de Categorías")
    print("1. Crear Categoría")
    print("2. Buscar Categoría")
    print("3. Modificar Categoría")
    print("4. Eliminar Categoría")
    print("0. Volver al menú principal")

def gestionar_autores():
    print("Gestión de Autores")
    print("1. Crear Autor")
    print("2. Modificar Autor")
    print("3. Actualizar Información de Autor")
    print("4. Habilitar Autor")
    print("5. Inhabilitar Autor")
    print("0. Volver al menú principal")

def gestionar_lectores():
    print("Gestión de Lectores")
    print("1. Registrar Lector")
    print("2. Buscar Lector")
    print("3. Modificar Lector")
    print("4. Habilitar Lector")
    print("5. Inhabilitar Lector")
    print("0. Volver al menú principal")

def gestionar_prestamos():
    print("Gestión de Préstamos")
    print("1. Registrar Préstamo")
    print("2. Consultar Préstamo")
    print("3. Calcular Fecha de Entrega")
    print("0. Volver al menú principal")

def gestionar_multas():
    print("Gestión de Multas")
    print("1. Generar Multa")
    print("2. Levantar Multa")
    print("3. Calcular Días de Retraso")
    print("0. Volver al menú principal")
