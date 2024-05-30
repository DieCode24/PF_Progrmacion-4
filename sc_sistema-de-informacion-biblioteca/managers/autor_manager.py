# Juan Marulanda
from clases.autor import Autor
from datetime import datetime, timedelta
from utils.validators import validar_input

class AutorManager:
    def __init__(self):
        self.autores = []

    def registrar_autor(self, bool=None, param = None):
        nombre = validar_input("Ingrese el nombre del autor: ", str).capitalize()
        nacionalidad = validar_input("Ingrese la nacionalidad del autor: ", str).capitalize()
        fecha_nacimiento = validar_input("Ingrese la fecha de nacimiento del autor (YYYY-MM-DD): ", str)
        retorna = self.agregar_autor(nombre, nacionalidad, fecha_nacimiento)
        if bool is not True:
            print(f"Autor {nombre} registrado exitosamente.")
            return retorna.__getattribute__(param)
            
        print(f"Autor {nombre} registrado exitosamente.")

    def agregar_autor(self, nombre: str, nacionalidad: str, fecha_nacimiento: str):
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        autor = Autor(nombre, nacionalidad, fecha_nacimiento)
        self.autores.append(autor)
        return autor

    def buscar_autor(self, nombre: str):
        for autor in self.autores:
            if autor.nombre == nombre:
                return autor
        return None



    def modificar_autor(self):
        nombre = validar_input("Ingrese el nombre del autor que desea modificar: ", str).capitalize()
        autor = self.buscar_autor(nombre)
        
        if autor.__getattribute__("habilitado") == False:
            print("No se puede modificar un autor inhabilitado")
            return
         
        if autor:
            nacionalidad = validar_input("Ingrese la nueva nacionalidad del autor: ", str).capitalize()
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
            print(f"Fecha de nacimiento: {autor.fecha_nacimiento.strftime('%Y-%m-%d')}")
            print("Libros:")
            for libro in autor.libros:
                print(libro)
        else:
            print("El autor no existe")

    def see_authors(self, bool=None, mas_info=None):
        count = 1
        if bool is None:
            print("Autores:")
            for autor in self.autores:
                print(f"{count}. {autor}")
                count += 1
                if mas_info is not None:
                    print("Desea saber más información de un autor?")
                    respuesta = input("Si/No: ").lower()
                    if respuesta == "si":
                        nombre = ("Ingrese el nombre del autor: ").capitalize()
                        self.mostrar_informacion_autor(nombre)
            
        elif bool:
            print("Autores Habilitados:")
            for autor in self.autores:
                if autor.habilitado:
                    print(f"{count}. {autor}")
                    count += 1
                    if mas_info is not None:
                        print("Desea saber más información de un autor?")
                        respuesta = input("Si/No: ").lower()
                        if respuesta == "si":
                            nombre = ("Ingrese el nombre del autor: ").capitalize()
                            self.mostrar_informacion_autor(nombre)
        else:
            print("Autores Inhabilitados:")
            for autor in self.autores:
                if not autor.habilitado:
                    print(f"{count}. {autor}")
                    count += 1
                    if mas_info is not None:
                        print("Desea saber más información de un autor?")
                        respuesta = input("Si/No: ").lower()
                        if respuesta == "si":
                            nombre = ("Ingrese el nombre del autor: ").capitalize()
                            self.mostrar_informacion_autor(nombre)
                            
                            
    def listas_d_autores(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Todos los autores")
            print("2. Autores habilitados")
            print("3. Autores inhabilitados")
            print("0. Salir")
            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.see_authors(None, True)
            elif opcion == "2":
                self.see_authors(True, True)
            elif opcion == "3":
                self.see_authors(False, True)
            elif opcion == "0":
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
                
    def habilitar_autor(self):
        nombre = input("Ingrese el nombre del autor que desea habilitar: ")
        autor = self.buscar_autor(nombre)
        if autor:
            autor.habilitado = True
            print(f"Autor {nombre} habilitado exitosamente.")
        else:
            print("El autor no existe.")
            
    def inhabilitar_autor(self):
        nombre = input("Ingrese el nombre del autor que desea inhabilitar: ")
        autor = self.buscar_autor(nombre)
        if autor:
            autor.habilitado = False
            print(f"Autor {nombre} inhabilitado exitosamente.")
        else:
            print("El autor no existe.")
            
    def pasar_dia(self, FECHA_ACTUAL: datetime):
        print (f"Fecha actual: {FECHA_ACTUAL}")
        FECHA_ACTUAL += timedelta(days=1)
        
        print (f"Fecha actualizada: {FECHA_ACTUAL}")
        
        FECHA_ACTUAL += timedelta(days=1)
        
        print (f"Fecha actualizada: {FECHA_ACTUAL}")
        return FECHA_ACTUAL
    