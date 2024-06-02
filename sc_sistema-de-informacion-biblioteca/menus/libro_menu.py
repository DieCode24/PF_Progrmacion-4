from utils.helpers import pausar_sistema

def show_libro_menu(self):
    libro_manager = self.container.libro_manager
    autor_manager = self.container.autor_manager
    while True:
        print("# Gestión de Libros")
        print("---------------------------------------------------")
        print("Seleccione una opción:")
        print("\n> [1] Registrar Libro")
        print("> [2] Listar Libros")
        print("> [3] Buscar Libro")
        print("> [4] Modificar Libro")
        print("> [5] Habilitar Libro")
        print("> [6] Inhabilitar Libro")
        print("> [7] Realizar Préstamo de Libro")
        print("> [8] Devolver Libro")
        print("> [0] Volver al menú principal")
        choice = input("Choose an option: ")
        if choice == "1":
            autores = autor_manager.seleccionar_autores()
            libro_manager.registrar_libro(autores)
        elif choice == "2":
            libro_manager.listado_libros()
            pausar_sistema()

        elif choice == "3":
            isbn = input("Enter ISBN: ")
            libro_manager.disable_libro(isbn)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")