import os



def pausar_sistema():
    try:
        print("\n")
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
    print("Sistema de Información Biblioteca\n")

    
def separador_en_consola():
    print("----------------------------------------\n")
    

def validar_contraseña(rol):
    """
    Valida la contraseña basada en el rol proporcionado.

    :param rol: El rol del usuario (1: Administrador, 2: Bibliotecario, 3: Lector).
    :return: True si la contraseña es correcta, False en caso contrario.
    """
    if rol == "1":
        contraseña_correcta = os.getenv("ADMIN_PASSWORD")
    elif rol == "2":
        contraseña_correcta = os.getenv("LIBRARIAN_PASSWORD")
    elif rol == "3":
        contraseña_correcta = os.getenv("READER_PASSWORD")
    else:
        return False

    contraseña = input("\n> Ingrese la contraseña => ")
    return contraseña == contraseña_correcta