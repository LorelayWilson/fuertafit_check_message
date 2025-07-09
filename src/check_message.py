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
    message = message.replace(" ", "").lower()
    chest = chest.replace(" ", "").lower()

    # Si el mensaje queda vacío tras limpiar, devolver False
    if not message:
        return True, "Mensaje vacío: no requiere caracteres para formarse."

    if not chest:
        return False, "El cofre no contiene caracteres válidos."

    # Contar los caracteres disponibles en el cofre
    chest_counter = Counter(chest)

    # Contar los caracteres necesarios en el mensaje
    missing_counter = Counter()
    for char in message:
        if chest_counter[char] > 0:
            chest_counter[char] -= 1
        else:
            missing_counter[char] += 1

    # Si hay caracteres que faltan, devolver False con los caracteres que faltan
    if missing_counter:
        missing_str = ', '.join(f"{char}({count})" for char, count in missing_counter.items())
        return False, f"Faltan caracteres: {missing_str}"
    
    return True, "El mensaje puede ser formado con los caracteres del cofre."

if __name__ == "__main__":
    print(can_form_message("SOS", "PELIGROSOS"))    # True
    print(can_form_message("HELP", "HELICOPTER"))   # True
    print(can_form_message("RESCUEA", "RSCU"))       # False
    print(can_form_message("Ñ", "N"))       # False
    print(can_form_message("112", "112A"))       # True

