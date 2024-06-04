from menus.libro_menu import show_libro_menu
from menus.copy_menu import show_copy_menu
from menus.tesis_menu import show_tesis_menu
from menus.autores_menu import show_autor_menu
from menus.prestamo_menu import show_prestamo_menu
from menus.articulo_menu import show_articulo_menu
from menus.lector_menu import show_lector_menu
from menus.categoria_menu import show_categoria_menu

from utils.validators import validar_input

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
                show_articulo_menu(self)
            elif choice == "4":
                show_autor_menu(self)
            elif choice == "5":
                show_lector_menu(self)
            elif choice == "6":
                show_prestamo_menu(self)
            elif choice == "7":
                self.show_multa_menu(self)
            elif choice == "8":
                show_categoria_menu(self)
            elif choice == "9":
                show_copy_menu(self)
            elif choice == "0":
                return False
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
                show_articulo_menu(self)
            elif choice == "4":
                show_autor_menu(self)
            elif choice == "5":
                show_lector_menu(self)
            elif choice == "6":
                show_prestamo_menu(self)
            elif choice == "7":
                show_multa_menu(self)
            elif choice == "8":
                show_categoria_menu(self)
            elif choice == "9":
                show_copy_menu(self)
            elif choice == "0":
                return False
            else:
                print("\nOpción inválida. Por favor, intente de nuevo.")
                pausar_sistema()


class ReaderMenu(Menu):
    def show(self):
        while True:
            limpiar_consola()
            print_brand_sistema()
            separador_en_consola()

            print("[-- Menú de Lector --]\n")
            print("[1] listas")
            print("[2] busqueda")
            print("[3] Solicitar préstamos")
            print("[4] Devolver libro")
            print("[5] Pagar multas")
            print("[0] Cerrar sesión")
            choice = input("\n\n> Seleccione una opción => ")

            if choice == "1":
                self.show_listas()
            elif choice == "2":
                self.show_busqueda()
            elif choice == "3":
                self.show_solicitar_prestamos()
            elif choice == "4":
                self.show_devolver_libro()
            elif choice == "5":
                self.show_pagar_multas()
            elif choice == "0":
                return False
            else:
                print("\nOpción inválida. Por favor, intente de nuevo.")
                pausar_sistema()
                
                
    def show_listas(self):
        while True:
            limpiar_consola()
            print_brand_sistema()
            separador_en_consola()

            print("[-- Listas --]\n")
            print("[1] Autores habilitados")
            print("[2] Libros disponibles")
            print("[3] Tesis disponibles")
            print("[4] Artículos disponibles")
            
            print("[0] Salir")
            choice = validar_input("\n\n> Seleccione una opción => ", int)
            
            if choice == 1:
                self.container.autor_manager.see_authors(True, True)
            elif choice == 2:
                self.container.libro_manager.listado_libros_activos()
            elif choice == 3:   
                self.container.tesis_manager.listado_tesis()
            elif choice == 4:
                self.container.articulo_manager.listar_articulos()
            elif choice == 0:
                return False

            
            else:
                print("\nOpción inválida. Por favor, intente de nuevo.")
                pausar_sistema()
                
    