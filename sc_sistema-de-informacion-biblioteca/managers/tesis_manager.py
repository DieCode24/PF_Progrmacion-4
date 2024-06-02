from clases.tesis import Tesis
from clases.estado import Estado
from managers.autor_manager import AutorManager
from typing import List
import os 
from utils.validators import validar_input

class TesisManager:

    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.tesis = [ 
            Tesis(["juan", "pedro"], "utp", "2020-01-04", "2024-01-01", "Ciencia", Estado.DISPONIBLE, 100),
            Tesis(["maria", "luis"], "utp", "2020-01-04", "2024-01-01", "Matematicas", Estado.DISPONIBLE, 200),
            Tesis(["juan", "mateo"], "utp", "2020-01-04", "2024-01-01", "Ciencia", Estado.DISPONIBLE, 100),
            ]
    
    def agregar_tesis(self, autores):
        institucion = validar_input("Ingrese la institución de la tesis: ", str).title()
        f_investigacion = validar_input("Ingrese la fecha de investigación de la tesis (YYYY-MM-DD): ", str)
        f_presentacion = validar_input("Ingrese la fecha de presentación de la tesis (YYYY-MM-DD): ", str)
        campo_estudio = validar_input("Ingrese el campo de estudio de la tesis: ", str).title()
        estado = Estado.DISPONIBLE
        paginas = validar_input("Ingrese el número de páginas de la tesis: ", int)
        tesis  = Tesis(autores, institucion, f_investigacion, f_presentacion, campo_estudio, estado, paginas)
        self.tesis.append(tesis)             
        
    def listar_tesis(self):
        print("LISTA DE TESIS\n")
        if not self.tesis:
            print("No hay tesis registradas")
            return
        counter = 1
        for tesis in self.tesis: 
            print(counter,
                " Campo: ", tesis.CampoEstudio().title(), "\n" + 
                "   Páginas: ", tesis.Paginas(),"\n" + 
                "   Fecha publicacion: ", tesis.Fpresentacion()
                )
            print("   Autores ")
            for autor in tesis.Autores():
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
            os.system('cls')
            self.buscar_por_autor()
        elif op == 2:
            os.system('cls')
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

        for tesis in self.tesis:
            autores = tesis.Autores()
            nombres = [autor.nombre for autor in autores]
            if autor_B in nombres:
                Tesis.append(tesis)

        if not Tesis:
            print(f"No se encontraron tesis del autor {autor_B}.")
            print("Por favor, intente con otro autor.")
            
        else:
            for tesis in Tesis:
                print(
                    "   Campo: ", tesis.CampoEstudio(), "\n" + 
                    "   Páginas: ", tesis.Paginas(),"\n" + 
                    "   Institucion: ", tesis.Institucion(),"\n" +
                    "   Estado: ", tesis.Estado(),"\n" +
                    "   Fecha investigacion: ", tesis.Finvestigacion(),"\n" +
                    "   Fecha publicacion: ", tesis.Fpresentacion()
                    )
                print("   Autores ")
                for autor in tesis.Autores():
                    print (f"\t{autor.nombre}")
                print("\n\n")
                        
    def buscar_por_campo(self):
        print("\t Buscando por campo de estudio\n")
        campo = validar_input("Ingrese el campo de estudio: ", str).title()
        for tesis in self.tesis:
            if campo in tesis.CampoEstudio():
                print(
                "   Campo: ", tesis.CampoEstudio(), "\n" + 
                "   Páginas: ", tesis.Paginas(),"\n" + 
                "   Institucion: ", tesis.Institucion(),"\n" +
                "   Estado: ", tesis.Estado(),"\n" +
                "   Fecha investigacion: ", tesis.Finvestigacion(),"\n" +
                "   Fecha publicacion: ", tesis.Fpresentacion()
                )
            print("   Autores ")
            for autor in tesis.Autores():
                    print (f"\t{autor.nombre}")
            
                
    def modificar_tesis(self, autores : AutorManager):
    
        self.listar_tesis()
        if not self.tesis:
            print("No hay tesis registradas")
            return
        
        opcion = validar_input(f"Ingrese el número de la tesis que desea modificar: ", int)
    
        T_modificar = self.tesis[opcion - 1]
        print("\tDatos actuales de la tesis\n")
        print(" Campo: ", T_modificar.CampoEstudio(), "\n" + 
                "   Páginas: ", T_modificar.Paginas(),"\n" + 
                "   Fecha investigacion: ", T_modificar.Finvestigacion(),"\n" +
                "   Fecha publicacion: ", T_modificar.Fpresentacion(),"\n" +
                "   Institucion: ", T_modificar.Institucion(),"\n" +
                "   Autores ")
        for autor in T_modificar.Autores():
            print (f"\t{autor.nombre}")
            
        self.tesis.remove(T_modificar)
        
        print("\n\tDatos nuevos de la tesis\n")
        autoresModi = autores.seleccionar_autores()
        self.agregar_tesis(autoresModi)
                
        print("Tesis modificada correctamente.")
        
    def eliminar_tesis(self):
        self.listar_tesis()
        if not self.tesis:
            print("No hay tesis registradas")
            return
        
        opcion = validar_input(f"Ingrese el número de la tesis que desea eliminar: ", int)

        tesis_a_eliminar = self.tesis[opcion - 1]
        self.tesis.remove(tesis_a_eliminar) 
        print("Tesis eliminada correctamente.")
            