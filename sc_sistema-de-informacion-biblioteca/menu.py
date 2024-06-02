from menus.libro_menu import show_libro_menu
from menus.copy_menu import show_copy_menu

class Menu:
    def __init__(self, container):
        self.container = container

    def show(self):
        raise NotImplementedError("This method should be implemented by subclasses")
    

class AdminMenu(Menu):
    def show(self):
        while True:
            print("\nAdmin Menu")
            print("1. Libro Manager")
            print("2. Tesis Manager")
            print("3. Articulo Manager")
            print("4. Autor Manager")
            print("5. Lector Manager")
            print("6. Prestamo Manager")
            print("7. Multa Manager")
            print("8. Categoria Manager")
            print ("9. Copia Manager")
            print("0. Logout")
            choice = input("Seleccione la opcion: ")
            if choice == "1":
                show_libro_menu(self)
            elif choice == "2":
                self.show_tesis_menu()
            elif choice == "3":
                self.show_articulo_menu()
            elif choice == "4":
                self.show_autor_menu()
            elif choice == "5":
                self.show_lector_menu()
            elif choice == "6":
                self.show_prestamo_menu()
            elif choice == "7":
                self.show_multa_menu()
            elif choice == "8":
                self.show_categoria_menu()
            elif choice == "9":
                show_copy_menu(self)
            elif choice == "0":
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

class LibrarianMenu(Menu):
    def show(self):
        while True:
            print("\nAdmin Menu")
            print("1. Libro Manager")
            print("2. Tesis Manager")
            print("3. Articulo Manager")
            print("4. Autor Manager")
            print("5. Lector Manager")
            print("6. Prestamo Manager")
            print("7. Multa Manager")
            print("8. Categoria Manager")
            print ("9. Copia Manager")
            print("0. Logout")
            choice = input("Seleccione la opcion:")
            if choice == "1":
                show_libro_menu(self)
            elif choice == "2":
                self.show_articulo_menu()
            elif choice == "3":
                self.show_autor_menu()
            elif choice == "4":
                self.show_prestamo_menu()
            elif choice == "9":
                show_copy_menu(self)
            elif choice == "0":
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

    # Similar methods for other managers...

