from menus.libro_menu import show_libro_menu
from menus.copy_menu import show_copy_menu
from menus.tesis_menu import show_tesis_menu
from utils.helpers import pausar_sistema, print_brand_sistema, separador_en_consola, limpiar_consola



class Menu:
    def __init__(self, container):
        self.container = container


    def show(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    

class AdminMenu(Menu):
    def show(self):
        while True:
            limpiar_consola()
            print_brand_sistema()
            separador_en_consola()
            
            print("[-- Menu de Administrador --]\n")
            print("[1] Gestor de Libros")
            print("[2] Gestor de Tesis")
            print("[3] Gestor de Artículos")
            print("[4] Gestor de Autores")
            print("[5] Gestor de Lectores")
            print("[6] Gestor de Préstamos")
            print("[7] Gestor de Multas")
            print("[8] Gestor de Categorías")
            print("[9] Gestor de Copias")
            print("[0] Cerrar sesión")
            choice = input("\n\n> Seleccione una opción => ")
            
            if choice == "1":
                show_libro_menu(self)
            elif choice == "2":
                show_tesis_menu(self)
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
                print("\nOpción inválida. Por favor, intente de nuevo.")
                pausar_sistema()


class LibrarianMenu(Menu):
    def show(self):
        while True:
            limpiar_consola()
            print_brand_sistema()
            separador_en_consola()

            print("[-- Menú de Bibliotecario --]\n")
            print("[1] Gestor de Libros")
            print("[2] Gestor de Tesis")
            print("[3] Gestor de Artículos")
            print("[4] Gestor de Autores")
            print("[5] Gestor de Lectores")
            print("[6] Gestor de Préstamos")
            print("[7] Gestor de Multas")
            print("[8] Gestor de Categorías")
            print("[9] Gestor de Copias")
            print("[0] Cerrar sesión")
            choice = input("\n\n> Seleccione una opción => ")

            if choice == "1":
                show_libro_menu(self)
            elif choice == "2":
                show_tesis_menu(self)
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
                print("\nOpción inválida. Por favor, intente de nuevo.")
                pausar_sistema()

    # Similar methods for other managers...

