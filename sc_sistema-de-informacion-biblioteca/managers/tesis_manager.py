from clases.tesis import Tesis
from clases.estado import Estado
from clases.autor import Autor
from managers.autor_manager import AutorManager
from managers.data_manager import DataManager
from utils.validators import validar_input
from typing import List
from utils.helpers import limpiar_consola

class TesisManager():

    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager
    
    def agregar_tesis(self, autores):
        institucion = validar_input("Ingrese la institución de la tesis: ", str).title()
        f_investigacion = validar_input("Ingrese la fecha de investigación de la tesis (YYYY-MM-DD): ", str)
        f_presentacion = validar_input("Ingrese la fecha de presentación de la tesis (YYYY-MM-DD): ", str)
        campo_estudio = validar_input("Ingrese el campo de estudio de la tesis: ", str).title()
        estado = Estado.DISPONIBLE
        paginas = validar_input("Ingrese el número de páginas de la tesis: ", int)
        tesis  = Tesis(autores, institucion, f_investigacion, f_presentacion, campo_estudio, estado, paginas)
        self.data_manager.thesis.append(tesis)             
        
    def listado_tesis(self):
        print("\tLISTA DE TESIS\n")
        if not self.data_manager.thesis:
            print("No hay tesis registradas")
            return
        counter = 1
        for tesis in self.data_manager.thesis: 
            print(counter,
                " Campo: ", tesis.campoEstudio(), "\n" + 
                "   Páginas: ", tesis.paginas(),"\n" + 
                "   Fecha publicacion: ", tesis.fpresentacion(), "\n" +
                "   Autores ")
            for autor in tesis.autores():
                    print (f"\t{autor.nombre}")
            print("\n\n")
            counter += 1

            
    def buscar_tesis(self): 
        print("Como desea buscar la tesis?")
        print("1. Autor")
        print("2. Campo de estudio")
        print("0. Salir")
        
        op = validar_input("\n> Ingrese una opción => ", int)
        
        if op == 1:
            limpiar_consola()
            self.buscar_por_autor()
        elif op == 2:
            limpiar_consola()
            self.buscar_por_campo()
        elif op == 0:
            return
        else:
            print("Opción no válida")
            return
        
    def buscar_por_autor(self):
        print("\t BUscanco por autor\n")
        autor_B = validar_input("Ingrese el autor: ", str).title()
        Tesis = []

        for tesis in self.data_manager.thesis:
            autores = tesis.autores()
            nombres = [autor.nombre for autor in autores]
            if autor_B in nombres:
                Tesis.append(tesis)

        if not Tesis:
            print(f"No se encontraron tesis del autor {autor_B}.")
            print("Por favor, intente con otro autor.")
            
        else:
            for tesis in Tesis:
                self.mostrar_tesis(tesis)
                        
    def buscar_por_campo(self):
        print("\t Buscando por campo de estudio\n")
        campo = validar_input("Ingrese el campo de estudio: ", str).title()
        for tesis in self.data_manager.thesis:
            if campo in tesis.campoEstudio():
                self.mostrar_tesis(tesis)
                
    def modificar_tesis(self, autores : AutorManager):
    
        self.listado_tesis()
        if not self.data_manager.thesis:
            print("No hay tesis registradas")
            return
        opcion = validar_input(f"Ingrese el número de la tesis que desea modificar: ", int)
    
        T_modificar = self.data_manager.thesis[opcion - 1]
        if T_modificar.estado() != Estado.DISPONIBLE:
            print("La tesis no se puede modificar porque no está disponible.")
            return
        print("\tDatos actuales de la tesis\n")
        print(" Campo: ", T_modificar.CampoEstudio(), "\n" + 
                "   Páginas: ", T_modificar.Paginas(),"\n" + 
                "   Fecha investigacion: ", T_modificar.Finvestigacion(),"\n" +
                "   Fecha publicacion: ", T_modificar.Fpresentacion(),"\n" +
                "   Institucion: ", T_modificar.Institucion(),"\n" +
                "   Autores ")
        for autor in T_modificar.Autores():
            print (f"\t{autor.nombre}")
            
        self.data_manager.thesis.remove(T_modificar)
        
        print("\n\tDatos nuevos de la tesis\n")
        autoresModi = autores.seleccionar_autores()
        self.agregar_tesis(autoresModi)
                
        print("Tesis modificada correctamente.")
        
    def eliminar_tesis(self):
        self.listado_tesis()
        if not self.data_manager.thesis:
            print("No hay tesis registradas")
            return
        
        opcion = validar_input(f"Ingrese el número de la tesis que desea eliminar: ", int)

        tesis_a_eliminar = self.data_manager.thesis[opcion - 1]
        self.data_manager.thesis.remove(tesis_a_eliminar) 
        print("Tesis eliminada correctamente.")
        
        
    def mock(self):
        autor1 = Autor("Juan Perez", "Colombiano", "2000-09-23")
        autor2 = Autor("Maria Rodriguez", "Mexicano", "1990-09-23")
        autor3 = Autor("Pedro Gomez", "Argentino", "1995-09-23")
        
        Tesis1 = Tesis([autor1], "Universidad Nacional", "2020-09-23", "2024-09-23", "Ingenieria", Estado.DISPONIBLE, 100)
        Tesis2 = Tesis([autor1, autor2], "Universidad de Andes", "2010-09-23", "2024-09-23", "Fisica", Estado.DISPONIBLE, 100)  
        Tesis3 = Tesis([autor2], "Universidad de los Andes", "2010-09-23", "2024-09-23", "Fisica", Estado.DISPONIBLE, 100)
        Tesis4 = Tesis([autor3, autor2, autor1], "Universidad de los Andes", "2010-09-23", "2024-09-23", "Matecaticas", Estado.DISPONIBLE, 100)
        self.data_manager.thesis = [Tesis1, Tesis2, Tesis3, Tesis4]
        
        print("Datos de prueba listos.")
        
    def mostrar_tesis(self, tesis: Tesis):
        print(f"Campo de estudio: {tesis.campoEstudio()}")
        print(f"Páginas: {tesis.paginas()}")
        print(f"Institución: {tesis.institucion()}")
        print(f"Estado: {tesis.estado()}")
        print(f"Fecha de investigación: {tesis.finvestigacion()}")
        print(f"Fecha de presentación: {tesis.fpresentacion()}")
        print("Autores:")
        for autor in tesis.autores():
            print(f"\t{autor.nombre}")
        print("\n\n")
        