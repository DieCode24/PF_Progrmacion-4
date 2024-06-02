from utils.helpers import pausar_sistema, limpiar_consola

def show_libro_menu(self):
    libro_manager = self.container.libro_manager
    autor_manager = self.container.autor_manager
    copy_manager = self.container.copy_manager
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
        # print("> [7] Realizar Préstamo de Libro")
        # print("> [8] Devolver Libro")
        print("> [9] Cargar mock data")
        print("> [0] Volver al menú principal")
        choice = input("Choose an option: ")
        if choice == "1":
            autores = autor_manager.seleccionar_autores()
            libro = libro_manager.registrar_libro(autores)
            autor_manager.asociar_libro(autores, libro.isbn)
            # crear numero de copias
            copy_manager.registrar_copias(libro.isbn, "Disponible", libro.numero_copias)
        elif choice == "2":
            libro_manager.listado_libros()
            limpiar_consola()
        elif choice == "3":
            query = input("Buscar libro por ISBN o título: ")
            libro_manager.buscar_libro(query)
            pausar_sistema()
        elif choice == "4":
            isbn = input("Ingrese el ISBN del libro que desea modificar: ")
            libro_manager.modificar_libro(isbn)
        elif choice == "5":
            isbn = input("Ingrese el ISBN del libro que desea habilitar: ")
            libro_manager.habilitar_libro(isbn)
        
        elif choice == "6":
            isbn = input("Ingrese el ISBN del libro que desea inhabilitar: ")
            libro_manager.inhabilitar_libro(isbn)
        
        elif choice == "9":
            limpiar_consola()
            libro_manager.load_mock_data()
            pausar_sistema()
            
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")