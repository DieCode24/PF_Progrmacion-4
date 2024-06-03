# Juan Marulanda
from clases.autor import Autor
from datetime import datetime, timedelta
from utils.validators import validar_input
from managers.data_manager import DataManager
from utils.helpers import limpiar_consola, pausar_sistema
class AutorManager:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def registrar_autor(self):
        nombre = validar_input("Ingrese el nombre del autor: ", str).title()
        nacionalidad = validar_input("Ingrese la nacionalidad del autor: ", str).title()
        fecha_nacimiento = validar_input("Ingrese la fecha de nacimiento del autor (YYYY-MM-DD): ", str)
        self.agregar_autor(nombre, nacionalidad, fecha_nacimiento)
        print(f"Autor {nombre} registrado exitosamente.")
        limpiar_consola()

    def agregar_autor(self, nombre: str, nacionalidad: str, fecha_nacimiento: str):
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        autor = Autor(nombre, nacionalidad, fecha_nacimiento)
        self.data_manager.autores.append(autor)
        limpiar_consola()
        return autor

    def buscar_autor(self, nombre: str):
        for autor in self.data_manager.autores:
            if autor.nombre == nombre:
                return autor
        return None
    

    def asociar_libro(self, autores, isbn):
        for autor in autores:
            autor.libros.append(isbn)

    def modificar_autor(self):
        nombre = validar_input("Ingrese el nombre del autor que desea modificar: ", str).title()
        autor = self.buscar_autor(nombre)
        
        if autor.gethabilitado() == False:
            print("No se puede modificar un autor inhabilitado")
            return
         
        if autor:
            nacionalidad = validar_input("Ingrese la nueva nacionalidad del autor: ", str).title()
            fecha_nacimiento = validar_input("Ingrese la nueva fecha de nacimiento del autor (YYYY-MM-DD): ", str)
            self.actualizar_autor(autor, nacionalidad, fecha_nacimiento)
            print(f"Autor {nombre} modificado exitosamente.")
        else:
            print("El autor no existe.")

    def actualizar_autor(self, autor: Autor, nacionalidad: str, fecha_nacimiento: str):
        autor.nacionalidad = nacionalidad
        autor.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

    def mostrar_informacion_autor(self, nombre: str):
        autor = self.buscar_autor(nombre)
        if autor:
            print(f"Información Actual de {autor.nombre}:")
            print(f"Nacionalidad: {autor.nacionalidad}")
            print(f"Fecha de nacimiento: {autor.fecha_nacimiento}")
            print("Libros:")
            for libro in autor.libros:
                print(libro)
        else:
            print("El autor no existe")

    def see_authors(self, bool=None, mas_info=None):
        count = 1
        autores_lista = []
        if bool is None:
            print("Autores:")
            for autor in self.data_manager.autores:
                print(f"{count}. {autor.nombre}")
                autores_lista.append(autor)
                count += 1
                
        elif bool:
            print("Autores Habilitados:")
            for autor in self.data_manager.autores:
                if autor.habilitado:
                    print(f"{count}. {autor.nombre}")
                    autores_lista.append(autor)
                    count += 1
                    
        else:
            print("Autores Inhabilitados:")
            for autor in self.data_manager.autores:
                if not autor.habilitado:
                    print(f"{count}. {autor.nombre}")
                    autores_lista.append(autor)
                    count += 1
                    
        if mas_info:
            numero = int(input("Ingrese el número del autor del que desea ver más información: "))
            if 1 <= numero <= len(autores_lista):
                autor = autores_lista[numero - 1]
                self.mostrar_informacion_autor(autor.nombre)
                pausar_sistema()
            else:
                print("Número inválido. Por favor, ingrese un número válido.")  
                     
                            
    def listas_d_autores(self):
        while True:
            limpiar_consola()
            print("\nSeleccione una opción:")
            print("1. Todos los autores")
            print("2. Autores habilitados")
            print("3. Autores inhabilitados")
            print("0. Salir")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                limpiar_consola()
                self.see_authors(None, True)
            elif opcion == "2":
                limpiar_consola()
                self.see_authors(True, True)
            elif opcion == "3":
                limpiar_consola()
                self.see_authors(False, True)
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
    
    def seleccionar_autores(self):
        autores_seleccionados = []
        while True:
            if not self.data_manager.autores:
                limpiar_consola()
                print("No hay autores registrados.")
                self.registrar_autor()
                pausar_sistema()
            
            limpiar_consola()
            print(">. Seleccione los autores que desea agregar al libro (separados por coma):")
            print("0. Crear un autor nuevo")
            print("Autores:")
            for i, autor in enumerate(self.data_manager.autores):
                print(f"{i + 1}. {autor.nombre}")
            try:
                seleccion = input("Autores: ")
                seleccion = [int(x) for x in seleccion.split(",")]
                for i in seleccion:
                    if i == 0:
                        self.registrar_autor()
                    elif 1 <= i <= len(self.data_manager.autores):
                        autores_seleccionados.append(self.data_manager.autores[i - 1])
                    else:
                        print("Opción inválida. Por favor, intente de nuevo.")
                if autores_seleccionados:
                    pausar_sistema()
                    limpiar_consola()
                    return autores_seleccionados
            except ValueError:
                print("Opción inválida. Por favor, intente de nuevo.")

                
    def habilitar_autor(self):
        nombre = input("Ingrese el nombre del autor que desea habilitar: ").title()
        autor = self.buscar_autor(nombre)
        if autor:
            autor.habilitar()
            print(f"Autor {nombre} habilitado exitosamente.")
        else:
            print("El autor no existe.")
            
    def inhabilitar_autor(self):
        nombre = input("Ingrese el nombre del autor que desea inhabilitar: ").title()
        autor = self.buscar_autor(nombre)
        if autor:
            autor.inhabilitar()
            print(f"Autor {nombre} inhabilitado exitosamente.")
        else:
            print("El autor no existe.")
            
    def mock(self):
        
        autor1 = Autor ("Gabriel Garcia Marquez", "Colombiano", "1927-03-06")
        autor1.inhabilitar()
        self.data_manager.autores.append(autor1)
        autor2 = Autor ("Julio Cortazar", "Argentino", "1914-08-26")
        self.data_manager.autores.append(autor2)
        autor3 = Autor ("Jorge Luis Borges", "Argentino", "1899-08-24")
        self.data_manager.autores.append(autor3)
        autor4 = Autor ("Mario Vargas Llosa", "Peruano", "1936-03-28")
        self.data_manager.autores.append(autor4)
        autor5 = Autor ("Isabel Allende", "Chilena", "1942-08-02")
        self.data_manager.autores.append(autor5)
        
         
        
        
            

    