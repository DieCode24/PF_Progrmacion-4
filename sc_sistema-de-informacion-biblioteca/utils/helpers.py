import os
from managers.libro_manager import LibroManager
from managers.autor_manager import AutorManager
from managers.articulo_cientifico_manager import ArticuloCientificoManager
from managers.tesis_manager import TesisManager
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
        print("1. Registrar libro")
        print("1. Buscar libros")
        print("2. Realizar préstamo de libro")
        print("3. Devolver libro")
        print("4. Consultar préstamos")
        print("0. Salir")
        SistemaBiblioteca.pausar_sistema(self)
        
    def mostrar_menu_bibliotecario (self,autor_manager: AutorManager, libro_manager: LibroManager , articuloManager: ArticuloCientificoManager, TesisManager: TesisManager):
        print("menu de bibliotecario")
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
            SistemaBiblioteca.gestionar_tesis(self, TesisManager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '2':
            SistemaBiblioteca.gestionar_articulos(self, articuloManager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '3':
            SistemaBiblioteca.gestionar_libros(self, libro_manager, autor_manager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '4':
            SistemaBiblioteca.gestionar_categorias(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '5':
            SistemaBiblioteca.gestionar_autores(self, autor_manager)
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
        
    def mostrar_menu_administrador(self,  autor_manager: AutorManager, libro_manager: LibroManager, ArticuloCientificoManager: ArticuloCientificoManager, TesisManager: TesisManager):
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
            SistemaBiblioteca.gestionar_tesis(self, TesisManager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '2':
            SistemaBiblioteca.gestionar_articulos(self, ArticuloCientificoManager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '3':
            SistemaBiblioteca.gestionar_libros(self, libro_manager, autor_manager)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '4':
            SistemaBiblioteca.gestionar_categorias(self)
            SistemaBiblioteca.pausar_sistema(self)
        elif opcion == '5':
            SistemaBiblioteca.gestionar_autores(self, autor_manager)
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

    def gestionar_tesis(self, TesisManager: TesisManager):
        SistemaBiblioteca.limpiar_consola(self)
        opcion = None
        while opcion != '0':
            print("Gestión de Tesis")
            print("1. Registrar Tesis")
            print("2. Lista Tesis")
            print("3. Buscar Tesis")
            print("4. Eliminar Tesis")
            print("5. Realizar Préstamo de Tesis")
            print("6. Devolver Tesis")
            print("7. Generar Multa")
            print("8. Levantar Multa")
            print("0. Volver al menú principal")
            opcion = input("\n\n> Ingrese una opción => ")
            
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
            elif opcion == '0':
                print("\n\n> Saliendo del sistema...")
            else:
                print("Opción no válida, intente de nuevo.")
            if opcion != '0':
                SistemaBiblioteca.pausar_sistema(self)

    def gestionar_articulos(self, ArticuloManager: ArticuloCientificoManager):
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

    def gestionar_libros(self, libro_manager: LibroManager, autor_manager: AutorManager):
        opcion = None
        while opcion != '0':
            print("Gestión de Libros")
            print("1. Registrar Libro")
            print ("2. listado de Libros")
            print("3. Buscar Libro")
            print("4. Modificar Libro")
            print("5. Habilitar Libro")
            print("6. Inhabilitar Libro")
            print("7. Realizar Préstamo de Libro")
            print("8. Devolver Libro")
            # print("8. Generar Multa")
            # print("9. Levantar Multa")
            print("0. Volver al menú principal")
            
            opcion = input("\n\n> Ingrese una opción => ")
            
            if opcion == '1':
                # seleccionar autor para libro
                autor = autor_manager.seleccionar_autores()
                SistemaBiblioteca.limpiar_consola(self)
                libro_manager.registrar_libro(autor)
                SistemaBiblioteca.pausar_sistema(self)
            elif opcion == '2':
                libro_manager.listado_libros()
                SistemaBiblioteca.pausar_sistema(self)
            elif opcion == '3':
                query = input("Ingrese el título o ISBN del libro: ")
                libro_manager.buscar_libro(query)
                SistemaBiblioteca.pausar_sistema(self)
            elif opcion == '4':
                isbn = input("Ingrese el ISBN del libro a modificar: ")
                libro_manager.modificar_libro(isbn)
                SistemaBiblioteca.pausar_sistema(self)
            elif opcion == '5':
                libro_manager.habilitar_libro()
                SistemaBiblioteca.pausar_sistema(self)
            elif opcion == '6':
                libro_manager.inhabilitar_libro()
                SistemaBiblioteca.pausar_sistema(self)
            elif opcion == '7':
                libro_manager.realizar_prestamo_libro()
                SistemaBiblioteca.pausar_sistema(self)
            elif opcion == '8':
                libro_manager.devolver_libro()
                SistemaBiblioteca.pausar_sistema(self)
            elif opcion == '9':
                libro_manager.generar_multa()
                SistemaBiblioteca.pausar_sistema(self)
            elif opcion == '10':
                libro_manager.levantar_multa()
                SistemaBiblioteca.pausar_sistema(self)
            elif opcion == '0':
                print("\n\n> Saliendo del sistema...")
                return
            else:
                print("Opción no válida, intente de nuevo.")
                
            if opcion != '0':
                SistemaBiblioteca.pausar_sistema(self)

    def gestionar_categorias(self):
        print("Gestión de Categorías")
        print("1. Crear Categoría")
        print("2. Buscar Categoría")
        print("3. Modificar Categoría")
        print("4. Eliminar Categoría")
        print("0. Volver al menú principal")

    def gestionar_autores(self, autor_manager: AutorManager):
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
                autor_manager.registrar_autor()
            elif opcion == '2':
                autor_manager.modificar_autor()
            elif opcion == '3':
                autor_manager.listas_d_autores()
            elif opcion == '4':
                autor_manager.habilitar_autor()
            elif opcion == '5':
                autor_manager.inhabilitar_autor()
            elif opcion == '6':
                autor_manager.pasar_dia()
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