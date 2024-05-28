import os

class SistemaBiblioteca:
    def pausar_sistema(self):
        """Pausa el sistema, funciona en Windows y Linux."""
        try:
            command_pause = 'pause' if os.name == 'nt' else 'read -n 1 -s -r -p "Presione cualquier tecla para continuar..."'
            os.system(command_pause)
        except Exception as e:
            print(f"Error al pausar el sistema: {e}")
    
    def limpiar_consola(self):
        """Limpia la consola, funciona en Windows y Linux."""
        try:
            comando = 'cls' if os.name == 'nt' else 'clear'
            os.system(comando)
        except Exception as e:
            print(f"Error al limpiar la consola: {e}")

    def mostrar_menu_lector(self):
        print("\nMenú de Lector:")
        print("1. Buscar libros")
        print("2. Realizar préstamo de libro")
        print("3. Devolver libro")
        print("4. Consultar préstamos")
        print("0. Salir")
        SistemaBiblioteca.pausar_sistema(self)
        
    def mostrar_menu_bibliotecario(self):
        print("\nMenú de Bibliotecario:")
        print("1. Registrar nuevo libro")
        print("2. Buscar libros")
        print("3. Modificar libro")
        print("4. Inhabilitar libro")
        print("5. Registrar nuevo lector")
        print("6. Modificar lector")
        print("7. Buscar lectores")
        print("0. Salir")
        SistemaBiblioteca.pausar_sistema(self)
        
    def mostrar_menu_administrador(self):
        print("Sistema de Información Biblioteca")
        print("\nMenú de Administrador:")
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
        
        opcion = input("\n\n> Ingrese una opción => ")
        
        if opcion == '1':
            SistemaBiblioteca.gestionar_tesis(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '2':
            SistemaBiblioteca.gestionar_articulos(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '3':
            SistemaBiblioteca.gestionar_libros(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '4':
            SistemaBiblioteca.gestionar_categorias(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '5':
            SistemaBiblioteca.gestionar_autores(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '6':
            SistemaBiblioteca.gestionar_lectores(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '7':
            SistemaBiblioteca.gestionar_prestamos(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '8':
            SistemaBiblioteca.gestionar_multas(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '0':
            print("\n\n> Saliendo del sistema...")
            return
        else:
            print("Opción no válida, intente de nuevo.")

    def gestionar_tesis(self):
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

    def gestionar_articulos(self):
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

    def gestionar_libros(self):
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

    def gestionar_categorias(self):
        print("Gestión de Categorías")
        print("1. Crear Categoría")
        print("2. Buscar Categoría")
        print("3. Modificar Categoría")
        print("4. Eliminar Categoría")
        print("0. Volver al menú principal")

    def gestionar_autores(self):
        print("Gestión de Autores")
        print("1. Crear Autor")
        print("2. Modificar Autor")
        print("3. Actualizar Información de Autor")
        print("4. Habilitar Autor")
        print("5. Inhabilitar Autor")
        print("0. Volver al menú principal")

    def gestionar_lectores(self):
        print("Gestión de Lectores")
        print("1. Registrar Lector")
        print("2. Buscar Lector")
        print("3. Modificar Lector")
        print("4. Habilitar Lector")
        print("5. Inhabilitar Lector")
        print("0. Volver al menú principal")

    def gestionar_prestamos(self):
        print("Gestión de Préstamos")
        print("1. Registrar Préstamo")
        print("2. Consultar Préstamo")
        print("3. Calcular Fecha de Entrega")
        print("0. Volver al menú principal")

    def gestionar_multas(self):
        print("Gestión de Multas")
        print("1. Generar Multa")
        print("2. Levantar Multa")
        print("3. Calcular Días de Retraso")
        print("0. Volver al menú principal")