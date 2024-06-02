import os
from clases.base import Base

class SistemaBiblioteca:
    def __init__(self):
        self.rol_actual = None

    
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

    
    def print_brand_sistema(self):
        print("\tSistema de Información Biblioteca\n\n")

        
    def verificar_acceso_administrador(self, rol):
        clave_admin = "clave_admin"  # Clave de administrador predeterminada

        if rol == "administrador":
            clave = input("Ingrese la clave de administrador: ")
            if clave != clave_admin:
                print("Clave incorrecta. Acceso denegado.")
                return

    def cambiar_rol(self, Base: Base):
        """Permite cambiar el rol actual del usuario."""
        self.limpiar_consola()
        self.print_brand_sistema()
        print("> Seleccione el rol:")
        print("\n> [1] Lector")
        print("> [2] Bibliotecario")
        print("> [3] Administrador")
        print("> [0] Salir")
        opcion = input("\n> Ingrese una opción => ")
        
        if opcion == '1':
            self.rol_actual = 'lector'
            self.mostrar_menu_lector()
            return
        
        elif opcion == '2':
            self.rol_actual = 'bibliotecario'
            self.mostrar_menu_bibliotecario(Base)
            return
        
        elif opcion == '3':
            self.rol_actual = 'administrador'
            self.verificar_acceso_administrador(self.rol_actual)
            self.mostrar_menu_administrador(Base)
            return
        
        elif opcion == '0':
            print("\n\n> Saliendo del sistema...")
            self.pausar_sistema(self)
            return
        
        else:
            input("Opción no válida, intente de nuevo.")
            self.cambiar_rol(Base)
    
    


    def mostrar_menu_lector(self, Base: Base):
        SistemaBiblioteca.limpiar_consola(self)
        SistemaBiblioteca.print_brand_sistema(self)

        print("# Menú de opciones | Lector")
        print("---------------------------------------------------")
        print("Seleccione una opción:")
        print("\n> [1] Buscar libros")
        print("> [2] Realizar préstamo de libro")
        print("> [3] Devolver libro")
        print("> [4] Consultar préstamos")
        print("> [5] Cambiar de rol")
        print("> [0] Salir")
        
        opcion = input("\n> Ingrese una opción => ")
        
        if opcion == '1':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
        
            # [1] Buscar libros
        
            SistemaBiblioteca.pausar_sistema(self)
        
        elif opcion == '2':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
        
            # [2] Realizar préstamo de libro
        
            SistemaBiblioteca.pausar_sistema(self)
        
        elif opcion == '3':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
        
            # [3] Devolver libro
        
            SistemaBiblioteca.pausar_sistema(self)
        
        elif opcion == '4':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
        
            # [4] Consultar préstamos
        
            SistemaBiblioteca.pausar_sistema(self)
        
        elif opcion == '5':
            self.cambiar_rol(Base)
            
        elif opcion == '0':
            print("\n\n> Saliendo del sistema...")
            SistemaBiblioteca.pausar_sistema(self)
            return
        
        else:
            input("Opción no válida, intente de nuevo.")
            
            self.mostrar_menu_lector()
        
        
    def mostrar_menu_bibliotecario (self, Base: Base):
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
        print("> [9] Cambiar de rol")
        print("> [0] Salir")
        
        opcion = input("\n> Ingrese una opción => ")
        
        if opcion == '1':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
        
            SistemaBiblioteca.gestionar_tesis(self, Base, 'bibliotecario')
        
        elif opcion == '2':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
        
            SistemaBiblioteca.gestionar_articulos(self, Base, 'bibliotecario')
        
        
        elif opcion == '3':
            SistemaBiblioteca.gestionar_libros(self, Base, 'bibliotecario')
        
            SistemaBiblioteca.pausar_sistema(self)        
        
        elif opcion == '4':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_categorias(self, Base, 'bibliotecario')
        
        elif opcion == '5':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
        
            SistemaBiblioteca.gestionar_autores(self, Base, 'bibliotecario')
        
        elif opcion == '6':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
        
            SistemaBiblioteca.gestionar_lectores(self, Base, 'bibliotecario')
        
        elif opcion == '7':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_prestamos(self, Base, 'bibliotecario')
        
        elif opcion == '8':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_multas(self, Base, 'bibliotecario')
        
        elif opcion == '9':
            self.cambiar_rol(Base)
        
        elif opcion == '0':
            print("\n\n> Saliendo del sistema...")
            SistemaBiblioteca.pausar_sistema(self)
            return
        
        else:
            print("Opción no válida, intente de nuevo.")
        
        
    def mostrar_menu_administrador(self, Base: Base):
        SistemaBiblioteca.limpiar_consola(self)
        SistemaBiblioteca.print_brand_sistema(self)
        
        print("# Menu de opciones | Administrador")
        print("---------------------------------------------------")
        print("Seleccione una opción:")
        print("> [1] Gestión de Tesis")
        print("> [2] Gestión de Artículos Científicos")
        print("> [3] Gestión de Libros")
        print("> [4] Gestión de Categorías")
        print("> [5] Gestión de Autores")
        print("> [6] Gestión de Lectores")
        print("> [7] Gestión de Préstamos")
        print("> [8] Gestión de Multas")
        print("> [9] Cambiar de rol")
        print("> [0] Salir")
        
        opcion = input("\n> Ingrese una opción => ")
        
        if opcion == '1':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_tesis(self, Base, 'administrador')
        
        elif opcion == '2':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_articulos(self, Base, 'administrador')
        
        elif opcion == '3':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_libros(self, Base, 'administrador')
            SistemaBiblioteca.pausar_sistema(self)
        
        elif opcion == '4':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_categorias(self, Base, 'administrador')
            SistemaBiblioteca.pausar_sistema(self)
        
        elif opcion == '5':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_autores(self, Base, 'administrador')
            SistemaBiblioteca.pausar_sistema(self)
        
        elif opcion == '6':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_lectores(self, Base, 'administrador')
        
        elif opcion == '7':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_prestamos(self, Base, 'administrador')
            SistemaBiblioteca.pausar_sistema(self)
        
        elif opcion == '8':
            SistemaBiblioteca.limpiar_consola(self)
            SistemaBiblioteca.print_brand_sistema(self)
            SistemaBiblioteca.gestionar_multas(self, Base, 'administrador')
            
        elif opcion == '9':
            self.cambiar_rol(Base)
        
        elif opcion == '0':
            print("\n\n> Saliendo del sistema...")
            SistemaBiblioteca.pausar_sistema(self)
            return
        else:
            print("Opción no válida, intente de nuevo.")



    def gestionar_tesis(self, Base: Base, menu_llamador):
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
            print("> [6] Mock")
            print("> [0] Volver al menú principal")
          
            opcion = input("\n> Ingrese una opción => ")
            
            if opcion == '1':
                autor = Base.AutorManager.seleccionar_autores()
                SistemaBiblioteca.limpiar_consola(self)
                Base.TesisManager.agregar_tesis(autor)
        
            elif opcion == '2':
                SistemaBiblioteca.limpiar_consola(self)
                Base.TesisManager.listar_tesis()
        
            elif opcion == '3':
                SistemaBiblioteca.limpiar_consola(self)
                Base.TesisManager.buscar_tesis()
        
            elif opcion == '4':
                SistemaBiblioteca.limpiar_consola(self)
                Base.TesisManager.eliminar_tesis()
        
            elif opcion == '5':
                SistemaBiblioteca.limpiar_consola(self)
                autor = Base.AutorManager
                Base.TesisManager.modificar_tesis(autor)
                
            elif opcion == '6':
                Base.TesisManager.mock()
        
            elif opcion == '0':
                input("\n\n> Volviendo al menú principal...")
        
                if menu_llamador == 'bibliotecario':
                    self.mostrar_menu_bibliotecario(Base)
        
                elif menu_llamador == 'administrador':
                    self.mostrar_menu_administrador(Base)
                
                return
        
            else:
                print("Opción no válida, intente de nuevo.")
            
            if opcion != '0':
                SistemaBiblioteca.pausar_sistema(self)
                SistemaBiblioteca.limpiar_consola(self)


    def gestionar_articulos(self, Base:Base , menu_llamador):
        while True:
            self.limpiar_consola()
            self.print_brand_sistema()
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
            
            opcion = input("\n> Ingrese una opción => ")
            
            if opcion == '1':
                Base.articulo_manager.registrar_articulo_desde_consola()
            
            elif opcion == '2':
                Base.articulo_manager.buscar_articulo_desde_consola()
                self.pausar_sistema()
            
            elif opcion == '3':
                Base.articulo_manager.modificar_articulo_desde_consola()
                self.pausar_sistema()
            
            elif opcion == '4':
                doi = input("Ingrese el DOI del artículo a eliminar: ")
                try:
                    Base.articulo_manager.eliminar_articulo(doi)
                    print("Artículo eliminado exitosamente.")
                except ValueError as e:
                    print(e)
                self.pausar_sistema()
            
            elif opcion == '5':
                doi = input("Ingrese el DOI del artículo a prestar: ")
                id_lector = int(input("Ingrese el ID del lector: "))
                try:
                    Base.articulo_manager.realizar_prestamo(doi, id_lector)
                    print("Préstamo realizado exitosamente.")
                except ValueError as e:
                    print(e)
                self.pausar_sistema()
            
            elif opcion == '6':
                doi = input("Ingrese el DOI del artículo a devolver: ")
                id_lector = int(input("Ingrese el ID del lector: "))
                try:
                    Base.articulo_manager.devolver_articulo(doi, id_lector)
                    print("Artículo devuelto exitosamente.")
                except ValueError as e:
                    print(e)
                self.pausar_sistema()
            
            elif opcion == '7':
                id_prestamo = int(input("Ingrese el ID del préstamo: "))
                try:
                    Base.articulo_manager.generar_multa(id_prestamo)
                    print("Multa generada exitosamente.")
                except ValueError as e:
                    print(e)
                self.pausar_sistema()
            
            elif opcion == '8':
                id_multa = int(input("Ingrese el ID de la multa: "))
                try:
                    Base.articulo_manager.levantar_multa(id_multa)
                    print("Multa levantada exitosamente.")
                except ValueError as e:
                    print(e)
                self.pausar_sistema()
            
            elif opcion == '0':
                input("\n\n> Volviendo al menú principal...")
                
                if menu_llamador == 'bibliotecario':
                    self.mostrar_menu_bibliotecario(Base)
                    
                elif menu_llamador == 'administrador':
                    self.mostrar_menu_administrador(Base)
                    
                break  # Salir del bucle while y regresar al menú anterior
            
            else:
                print("Opción no válida, intente de nuevo.")
                self.pausar_sistema()


    def gestionar_libros(self, Base: Base, menu_llamador):
        opcion = None

        while opcion != '0':
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
            
            opcion = input("\n> Ingrese una opción => ")
            
            if opcion == '1':
                autor = Base.AutorManager.seleccionar_autores()
                Base.LibroManager.registrar_libro(autor)
                
            elif opcion == '2':
                Base.LibroManager.listado_libros()
                SistemaBiblioteca.pausar_sistema(self)

            elif opcion == '3':
                query = input("Ingrese el título o ISBN del libro a buscar: ")
                Base.LibroManager.buscar_libro(query)
                SistemaBiblioteca.pausar_sistema(self)

            elif opcion == '4':
                query = input("Ingrese el ISBN del libro a modificar: ")
                Base.LibroManager.modificar_libro(query)
                SistemaBiblioteca.pausar_sistema(self)

            elif opcion == '5':
                query = input("Ingrese el ISBN del libro a habilitar: ")
                Base.LibroManager.habilitar_libro(query)
                SistemaBiblioteca.pausar_sistema(self)

            elif opcion == '6':
                query = input("Ingrese el ISBN del libro a inhabilitar: ")
                Base.LibroManager.inhabilitar_libro(query)
                SistemaBiblioteca.pausar_sistema(self)

        # elif opcion == '6':
        #     LibroManager.realizar_prestamo_libro()
        #     SistemaBiblioteca.pausar_sistema(self)

        # elif opcion == '7':
        #     LibroManager.devolver_libro()
        #     SistemaBiblioteca.pausar_sistema(self)

        # elif opcion == '8':
        #     LibroManager.generar_multa()
        #     SistemaBiblioteca.pausar_sistema(self)

        # elif opcion == '9':
        #     LibroManager.levantar_multa()
        #     SistemaBiblioteca.pausar_sistema(self)

            elif opcion == '0':
                input("\n\n> Volviendo al menú principal...")
            
                if menu_llamador == 'bibliotecario':
                    self.mostrar_menu_bibliotecario(Base)
            
                elif menu_llamador == 'administrador':
                    self.mostrar_menu_administrador(Base)
            
                return
            
            else:
                print("Opción no válida, intente de nuevo.")


    def gestionar_categorias(self, Base: Base, menu_llamador):
        print("# Gestión de Categorías")
        print("---------------------------------------------------")
        print("\n> [1] Crear Categoría")
        print("> [2] Buscar Categoría")
        print("> [3] Modificar Categoría")
        print("> [4] Eliminar Categoría")
        print("> [0] Volver al menú principal")


    def gestionar_autores(self, Base: Base, menu_llamador):
        opcion = None

        while opcion != '0':
            SistemaBiblioteca.limpiar_consola(self)
            print("Gestión de Autores")
            print("1. Crear Autor")
            print("2. Modificar Autor")
            print("3. Listar Autores")
            print("4. Habilitar Autor")
            print("5. Inhabilitar Autor")
            print("6. Mock")
            print("0. Volver al menú principal")
            opcion = input("\n\n> Ingrese una opción => ")

            if opcion == '1':
                Base.AutorManager.registrar_autor()

            elif opcion == '2':
                Base.AutorManager.modificar_autor()

            elif opcion == '3':
                Base.AutorManager.listas_d_autores()

            elif opcion == '4':
                Base.AutorManager.habilitar_autor()

            elif opcion == '5':
                Base.AutorManager.inhabilitar_autor()
                
            elif opcion == '6':
                Base.AutorManager.mock()

            elif opcion == '0':
                input("\n\n> Volviendo al menú principal...")

                if menu_llamador == 'bibliotecario':
                    self.mostrar_menu_bibliotecario(Base)

                elif menu_llamador == 'administrador':
                    self.mostrar_menu_administrador(Base)

                return

            else:
                print("Opción no válida, intente de nuevo.")

            if opcion != '0':
                SistemaBiblioteca.pausar_sistema(self)


    def gestionar_lectores(self, Base: Base, menu_llamador):
        while True:
            self.limpiar_consola()
            self.print_brand_sistema()
            print("# Gestión de Lectores")
            print("---------------------------------------------------")
            print("Seleccione una opción:")
            print("\n> [1] Registrar Lector")
            print("> [2] Buscar Lector")
            print("> [3] Modificar Lector")
            print("> [4] Habilitar Lector")
            print("> [5] Inhabilitar Lector")
            print("> [6] Listar Lectores")
            print("> [0] Regresar al menú anterior")
            
            opcion = input("\n> Ingrese una opción => ")
            
            if opcion == '1':
                Base.lector_manager.registrar_lector_desde_consola()
            
            elif opcion == '2':
                Base.lector_manager.buscar_lector_desde_consola()
                self.pausar_sistema()
            
            elif opcion == '3':
                Base.lector_manager.modificar_lector_desde_consola()
                self.pausar_sistema()
            
            elif opcion == '4':
                id_lector = int(input("Ingrese el ID del lector a habilitar: "))
                try:
                    Base.lector_manager.habilitar_lector(id_lector)
                    print("Lector habilitado exitosamente.")
                except ValueError as e:
                    print(e)
                self.pausar_sistema()
            
            elif opcion == '5':
                id_lector = int(input("Ingrese el ID del lector a inhabilitar: "))
                try:
                    Base.lector_manager.inhabilitar_lector(id_lector)
                    print("Lector inhabilitado exitosamente.")
                except ValueError as e:
                    print(e)
                self.pausar_sistema()
            
            elif opcion == '6':
                lectores = Base.lector_manager.listar_lectores()
                for lector in lectores:
                    print(lector)
                self.pausar_sistema()
            
            elif opcion == '0':
                input("\n\n> Volviendo al menú principal...")

                if menu_llamador == 'bibliotecario':
                    self.mostrar_menu_bibliotecario(Base)

                elif menu_llamador == 'administrador':
                    self.mostrar_menu_administrador(Base)

                break  # Salir del bucle while y regresar al menú anterior
            
            else:
                print("Opción no válida, intente de nuevo.")
                self.pausar_sistema()


    def gestionar_prestamos(self,Base: Base, menu_llamador):
        while True:
            self.limpiar_consola()
            self.print_brand_sistema()
            print("# Gestión de Préstamos")
            print("---------------------------------------------------")
            print("Seleccione una opción:")
            print("\n> [1] Registrar Préstamo")
            print("> [2] Consultar Préstamo")
            print("> [3] Calcular Fecha de Entrega")
            print("> [0] Regresar al menú anterior")
            
            opcion = input("\n> Ingrese una opción => ")
            
            if opcion == '1':
                # Logica 'Registrar Préstamo'.
                pass
            
            elif opcion == '2':
                # Logica 'Consultar Préstamo'.
                pass
            
            elif opcion == '3':
                # Logica 'Calcular Fecha de Entrega'.
                pass
            
            elif opcion == '0':
                input("\n\n> Volviendo al menú principal...")

                if menu_llamador == 'bibliotecario':
                    self.mostrar_menu_bibliotecario(Base)

                elif menu_llamador == 'administrador':
                    self.mostrar_menu_administrador(Base)

                break  # Salir del bucle while y regresar al menú anterior
            
            else:
                print("Opción no válida, intente de nuevo.")
                self.pausar_sistema()


    def gestionar_multas(self, Base: Base, menu_llamador):
        
        while True:
            self.limpiar_consola()
            self.print_brand_sistema()
            print("# Gestión de Multas")
            print("---------------------------------------------------")
            print("Gestión de Multas")
            print("1. Generar Multa")
            print("2. Levantar Multa")
            print("3. Calcular Días de Retraso")
            print("0. Volver al menú principal")
            opcion = input("\n\n> Ingrese una opción => ")
            
            if opcion == '1':
                Base.prestamo_manager.generar_multa()
            
            elif opcion == '2':
                Base.prestamo_manager.levantar_multa()
            
            elif opcion == '3':
                Base.prestamo_manager.calcular_dias_retraso()
            
            elif opcion == '0':
                input("\n\n> Volviendo al menú principal...")

                if menu_llamador == 'bibliotecario':
                    self.mostrar_menu_bibliotecario(Base)

                elif menu_llamador == 'administrador':
                    self.mostrar_menu_administrador(Base)

                break  # Salir del bucle while y regresar al menú anterior
            
            else:
                print("Opción no válida, intente de nuevo.")
                self.pausar_sistema()
        
        
