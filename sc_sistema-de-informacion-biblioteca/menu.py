from menus.libro_menu import show_libro_menu
from menus.copy_menu import show_copy_menu
from menus.tesis_menu import show_tesis_menu
from menus.autores_menu import show_autor_menu
from menus.prestamo_menu import show_prestamo_menu
from menus.articulo_menu import show_articulo_menu
from menus.lector_menu import show_lector_menu
from menus.categoria_menu import show_categoria_menu

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


class LectorMenu(Menu):
    def show(self):
        while True:
            limpiar_consola()
            print_brand_sistema()
            separador_en_consola()

            print("[-- Menú de Lector --]\n")
            print("[1] Consultar información personal")
            print("[2] Buscar libros")
            print("[3] Solicitar préstamo de libro")
            print("[4] Renovar préstamo")
            print("[5] Devolver libro")
            print("[6] Consultar historial de préstamos")
            print("[7] Pagar multas")
            print("[8] Actualizar información personal")
            print("[0] Cerrar sesión")
            choice = input("\n\n> Seleccione una opción => ")

            if choice == "1":
                self.consultar_informacion_personal()
            elif choice == "2":
                self.buscar_libros()
            elif choice == "3":
                self.solicitar_prestamo_libro()
            elif choice == "4":
                self.renovar_prestamo()
            elif choice == "5":
                self.devolver_libro()
            elif choice == "6":
                self.consultar_historial_prestamos()
            elif choice == "7":
                self.pagar_multas()
            elif choice == "8":
                self.actualizar_informacion_personal()
            elif choice == "0":
                return False
            else:
                print("\nOpción inválida. Por favor, intente de nuevo.")
                pausar_sistema()

