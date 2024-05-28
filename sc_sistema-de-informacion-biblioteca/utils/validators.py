def validar_input(prompt: str, expected_type: type, separator=None):
    while True:
        try:
            user_input = input(prompt)
            if expected_type == int:
                return int(user_input)
            elif expected_type == list and separator:
                return [item.strip() for item in user_input.split(separator)]
            elif expected_type == str:
                if user_input.isdigit():
                    raise ValueError("Entrada no válida. Se esperaba una cadena de texto, no un número.")
                return user_input
            else:
                return expected_type(user_input)
        except ValueError as e:
            print(f"Error: {e}")
            print(f"Entrada no válida. Se esperaba un valor de tipo {expected_type.__name__}.")
