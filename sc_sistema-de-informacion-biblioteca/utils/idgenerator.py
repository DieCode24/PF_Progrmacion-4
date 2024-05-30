import time
import random

def id_generator():
    timestamp = int(time.time())  # Tiempo actual en segundos desde Epoch
    short_timestamp = str(timestamp)[-5:]  # Últimos 5 dígitos del timestamp
    random_part = random.randint(100, 999)  # Parte aleatoria de 3 dígitos
    unique_id = f"{short_timestamp}{random_part}"  # Combina el short timestamp y la parte aleatoria
    return unique_id
