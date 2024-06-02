import os
from clases.base import Base
from utils.validators import validar_input


def pausar_sistema():
    try:
        command_pause = 'pause' if os.name == 'nt' else 'read -n 1 -s -r -p "Presione cualquier tecla para continuar..."'
        os.system(command_pause)

    except Exception as e:
        print(f"Error al pausar el sistema: {e}")

def limpiar_consola():
    try:
        comando = 'cls' if os.name == 'nt' else 'clear'
        os.system(comando)

    except Exception as e:
        print(f"Error al limpiar la consola: {e}")

    def __init__(self):
        self.rol_actual = None

def print_brand_sistema():
    print("\tSistema de Información Biblioteca\n\n")
        
