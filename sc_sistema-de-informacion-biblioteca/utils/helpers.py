import os
from managers.libro_manager import LibroManager
from managers.autor_manager import AutorManager
from managers.articulo_cientifico_manager import ArticuloCientificoManager
from managers.tesis_manager import TesisManager

class SistemaBiblioteca:
    
    def print_brand_sistema(self):
        print("\tSistema de Información Biblioteca\n\n")
    
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
        print("# Menú de opciones | Lector")
        print("---------------------------------------------------")
        print("Seleccione una opción:")
        print("\n> [1] Buscar libros")
        print("> [2] Realizar préstamo de libro")
        print("> [3] Devolver libro")
        print("> [4] Consultar préstamos")
        print("> [0] Salir")
        SistemaBiblioteca.pausar_sistema(self)
        
    def mostrar_menu_bibliotecario (self,libroManager: LibroManager, ArticuloManager: ArticuloCientificoManager, AutorManager: AutorManager, TesisManager: TesisManager):
        SistemaBiblioteca.limpiar_consola(self)
        SistemaBiblioteca.print_brand_sistema(self)
        print("# Menú de opciones | Bibliotecario")
        print("---------------------------------------------------")
        print("Seleccione una opción:")
        print("\n> [1] Gestión de Tesis")
        print("> [2] Gestión de Artículos Científicos")
        print("> [3] Gestión de Libros")
        print("> [4] Gestión de Categorías")
        print("> [5] Gestión de Autores")
        print("> [6] Gestión de Lectores")
        print("> [7] Gestión de Préstamos")
        print("> [8] Gestión de Multas")
        print("> [0] Salir")
        
        opcion = input("\n> Ingrese una opción => ")
        
        if opcion == '1':
                SistemaBiblioteca.limpiar_consola(self)
                SistemaBiblioteca.print_brand_sistema(self)
                SistemaBiblioteca.gestionar_tesis(self, TesisManager, 'bibliotecario')
        elif opcion == '2':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_articulos(self, ArticuloManager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '3':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_libros(self, libroManager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '4':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_categorias(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '5':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_autores(self, AutorManager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '6':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_lectores(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '7':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_prestamos(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '8':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_multas(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '0':
            print("\n\n> Saliendo del sistema...")
            SistemaBiblioteca.pausar_sistema(self)
            return
        else:
            print("Opción no válida, intente de nuevo.")
        
    def mostrar_menu_administrador(self,  AutorManager: AutorManager, LibroManager: LibroManager, ArticuloCientificoManager: ArticuloCientificoManager, TesisManager: TesisManager):
        SistemaBiblioteca.print_brand_sistema(self)
        
        print("# Menu de opciones | Administrador")
        print("---------------------------------------------------")
        print("Seleccione una opción:")
        print("\n> [1] Gestión de Tesis")
        print("> [2] Gestión de Artículos Científicos")
        print("> [3] Gestión de Libros")
        print("> [4] Gestión de Categorías")
        print("> [5] Gestión de Autores")
        print("> [6] Gestión de Lectores")
        print("> [7] Gestión de Préstamos")
        print("> [8] Gestión de Multas")
        print("> [0] Salir")
        
        opcion = input("\n> Ingrese una opción => ")
        
        if opcion == '1':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_tesis(self, TesisManager, 'administrador')
        elif opcion == '2':
            SistemaBiblioteca.gestionar_articulos(self, ArticuloCientificoManager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '3':
            SistemaBiblioteca.gestionar_libros(self, LibroManager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '4':
            SistemaBiblioteca.gestionar_categorias(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '5':
            SistemaBiblioteca.gestionar_autores(self, AutorManager, FECHA_ACTUAL)
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
            SistemaBiblioteca.pausar_sistema(self)
            return
        else:
            print("Opción no válida, intente de nuevo.")

    def gestionar_tesis(self, TesisManager, menu_llamador, libroManager=None, ArticuloManager=None, AutorManager=None):
        opcion = None
        while opcion != '0':
            print("# Gestión de Tesis")
            print("---------------------------------------------------")
            print("Seleccione una opción:")
            print("> [1] Registrar Tesis")
            print("> [2] Lista Tesis")
            print("> [3] Buscar Tesis")
            print("> [4] Eliminar Tesis")
            print("> [5] Modificar Tesis")
            print("> [0] Volver al menú principal")
          
            opcion = input("\n> Ingrese una opción => ")
            
            if opcion == '1':
                SistemaBiblioteca.limpiar_consola(self)
                TesisManager.agregar_tesis()
            elif opcion == '2':
                SistemaBiblioteca.limpiar_consola(self)
                TesisManager.listar_tesis()
            elif opcion == '3':
                SistemaBiblioteca.limpiar_consola(self)
                TesisManager.buscar_tesis()
            elif opcion == '4':
                SistemaBiblioteca.limpiar_consola(self)
                TesisManager.eliminar_tesis()
            elif opcion == '5':
                SistemaBiblioteca.limpiar_consola(self)
                TesisManager.modificar_tesis()
            elif opcion == '0':
                input("\n\n> Volviendo al menú principal...")
                if menu_llamador == 'bibliotecario':
                    self.mostrar_menu_bibliotecario(libroManager, ArticuloManager, AutorManager, TesisManager)
                elif menu_llamador == 'administrador':
                    self.mostrar_menu_administrador(AutorManager, libroManager, ArticuloManager, TesisManager)
                return
            else:
                print("Opción no válida, intente de nuevo.")
            
            if opcion != '0':
                SistemaBiblioteca.pausar_sistema(self)
                SistemaBiblioteca.limpiar_consola(self)

    def gestionar_articulos(self, ArticuloManager: ArticuloCientificoManager):
        print("# Gestión de Artículos Científicos")
        print("---------------------------------------------------")
        print("Seleccione una opción:")
        print("\n> [1] Registrar Artículo")
        print("> [2] Buscar Artículo")
        print("> [3] Modificar Artículo")
        print("> [4] Eliminar Artículo")
        print("> [5] Realizar Préstamo de Artículo")
        print("> [6] Devolver Artículo")
        print("> [7] Generar Multa")
        print("> [8] Levantar Multa")
        print("> [0] Volver al menú principal")

    def gestionar_libros(self, LibroManager: LibroManager):
        print("# Gestión de Libros")
        print("---------------------------------------------------")
        print("Seleccione una opción:")
        print("\n> [1] Registrar Libro")
        print("> [2] Buscar Libro")
        print("> [3] Modificar Libro")
        print("> [4] Habilitar Libro")
        print("> [5] Inhabilitar Libro")
        print("> [6] Realizar Préstamo de Libro")
        print("> [7] Devolver Libro")
        print("> [8] Generar Multa")
        print("> [9] Levantar Multa")
        print("> [0] Volver al menú principal")
        
        opcion = input("\n> Ingrese una opción => ")
        
        if opcion == '1':
            LibroManager.registrar_libro()
        elif opcion == '2':
            LibroManager.buscar_libro()
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '3':
            LibroManager.modificar_libro()
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '4':
            LibroManager.habilitar_libro()
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '5':
            LibroManager.inhabilitar_libro()
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '6':
            LibroManager.realizar_prestamo_libro()
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '7':
            LibroManager.devolver_libro()
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '8':
            LibroManager.generar_multa()
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '9':
            LibroManager.levantar_multa()
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '0':
            print("\n\n> Saliendo del sistema...")
            return
        else:
            print("Opción no válida, intente de nuevo.")

    def gestionar_categorias(self):
        print("# Gestión de Categorías")
        print("---------------------------------------------------")
        print("\n> [1] Crear Categoría")
        print("> [2] Buscar Categoría")
        print("> [3] Modificar Categoría")
        print("> [4] Eliminar Categoría")
        print("> [0] Volver al menú principal")

    def gestionar_autores(self, AutorManager: AutorManager, FECHA_ACTUAL: str):
        opcion = None
        while opcion != '0':
            SistemaBiblioteca.limpiar_consola(self)
            print("Gestión de Autores")
            print("1. Crear Autor")
            print("2. Modificar Autor")
            print("3. Listar Autores")
            print("4. Habilitar Autor")
            print("5. Inhabilitar Autor")
            print("6. Pasar dia")
            print("0. Volver al menú principal")
            opcion = input("\n\n> Ingrese una opción => ")

            if opcion == '1':
                AutorManager.registrar_autor()
            elif opcion == '2':
                AutorManager.modificar_autor()
            elif opcion == '3':
                AutorManager.listas_d_autores()
            elif opcion == '4':
                AutorManager.habilitar_autor()
            elif opcion == '5':
                AutorManager.inhabilitar_autor()
            elif opcion == '6':
                AutorManager.pasar_dia(FECHA_ACTUAL)
            elif opcion == '0':
                print("\n\n> Saliendo del sistema...")
            else:
                print("Opción no válida, intente de nuevo.")

            if opcion != '0':
                SistemaBiblioteca.pausar_sistema(self)

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