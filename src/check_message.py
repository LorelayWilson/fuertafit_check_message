"""
This module contains a function that determines if a message can be formed
using the characters available in a chest, ignoring spaces.
Each character in the chest can only be used once.
"""
from collections import Counter

def can_form_message(message, chest):
    """Determines if a message can be formed with the characters from the chest.
    Args:
        message (str): The message to be formed.
        chest (str): The characters available in the chest.
    Returns:
        tuple: A tuple containing a boolean indicating if the message can be formed, and a string with details about the result.
    """
    # Normalize inputs by removing spaces and converting to lowercase
    message = message.replace(" ", "").lower()
    chest = chest.replace(" ", "").lower()

    # If the message is empty, return True
    if not message:
        return True, "Empty message can always be formed."
    # If the chest is empty, return False
    if not chest:
        return False, "The chest is empty, cannot form any message."

    # Count the characters in the chest
    chest_counter = Counter(chest)

    # Count the characters in the message
    missing_counter = Counter()
    for char in message:
        if chest_counter[char] > 0:  # If the character is available in the chest
            chest_counter[char] -= 1  # Use the character
        else:
            missing_counter[char] += 1  # If not available, count it as missing

    # If there are any missing characters, return False with details
    if missing_counter:
        missing_str = ', '.join(f"{char}({count})" for char, count in missing_counter.items())
        return False, f"Missing characters: {missing_str}"
    
    return True, "The message can be formed with the available characters."

if __name__ == "__main__":
    print(can_form_message("SOS", "PELIGROSOS"))    # True
    print(can_form_message("HELP", "HELICOPTER"))   # True
    print(can_form_message("RESCUEA", "RSCU"))      # False
    print(can_form_message("Ñ", "N"))               # False
    print(can_form_message("112", "112A"))          # True
