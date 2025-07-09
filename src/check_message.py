# File: src/check_message.py
"""
Este módulo contiene una función que determina si un mensaje puede ser formado
utilizando los caracteres disponibles en un cofre, ignorando espacios
Cada caracter del cofre solo se puede usar una vez.
"""
from collections import Counter

def can_form_message(message, chest):
    """Determina si el mensaje puede ser formado con los caracteres del cofre.
    Args:
        message (str): El mensaje que se quiere formar.
        chest (str): Los caracteres disponibles en el cofre.
    Returns:
        tuple: (bool, str) indicando si se puede formar y un mensaje explicativo.
    """
    # Normalizar el mensaje y el cofre: eliminar espacio
    message = message.replace(" ", "")
    chest = chest.replace(" ", "")

    # Si el mensaje queda vacío tras limpiar, devolver False
    if not message:
        return True, "Mensaje vacío: no requiere caracteres para formarse."

    if not chest:
        return False, "El cofre no contiene caracteres válidos."

    # Contar los caracteres disponibles en el cofre
    letter_count = Counter(chest)

    # Verificar si cada caracter del mensaje puede ser formada con los caracteres del cofre
    for letter in message:
        if letter_count[letter] > 0:
            letter_count[letter] -= 1
        else:
            return False, f"No hay suficientes caracteres '{letter}' en el cofre."

    return True, "El mensaje puede ser formado con los caracteres del cofre."

if __name__ == "__main__":
    print(can_form_message("SOS", "PELIGROSOS"))    # True
    print(can_form_message("HELP", "HELICOPTER"))   # True
    print(can_form_message("RESCUE", "RSCU"))       # False
    print(can_form_message("Ñ", "N"))       # False
    print(can_form_message("112", "112A"))       # True

