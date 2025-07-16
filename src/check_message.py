"""
This module contains a function that determines if a message can be formed
using the characters available in a chest, ignoring spaces.
Each character in the chest can only be used once.
"""
from collections import Counter, defaultdict

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
    
    # If the chest is significantly larger than the message
    if len(chest) > 5 * len(message):
        message_counter = Counter(message)
        chest_counter = _count_relevant(chest, message_counter)
    # If the message is larger than the chest
    elif len(message) > len(chest):
        return _scan_message_vs_small_chest(message, Counter(chest))
    # If the chest is small enough to compare directly
    else:
        message_counter = Counter(message)
        chest_counter = Counter(chest)

    return _compare_counts(message_counter, chest_counter)

def _count_relevant(chest: str, needed_chars: Counter) -> Counter:
    """Counts only the characters in the chest that are relevant to the message.
    Args:
        chest (str): The characters available in the chest.
        needed_chars (Counter): A Counter of characters needed for the message.
    Returns:
        Counter: A Counter of characters in the chest that are relevant to the message.
    """
    result = Counter()
    for c in chest:
        if c in needed_chars:
            result[c] += 1
    return result

def _scan_message_vs_small_chest(message: str, chest_counter: Counter) -> tuple[bool, str]:
    """Scans the message against a small chest to determine if it can be formed.
    Args:
        message (str): The message to be formed.
        chest_counter (Counter): A Counter of characters available in the chest.
    Returns:
        tuple: A tuple containing a boolean indicating if the message can be formed, and a string with details about the result.
    """
    missing = Counter()
    for c in message:
        if chest_counter[c] > 0:
            chest_counter[c] -= 1
        else:
            missing[c] += 1

    if missing:
        return False, _format_missing(missing)
    return True, "The message can be formed with the available characters."

def _compare_counts(message_counter: Counter, chest_counter: Counter) -> tuple[bool, str]:
    """Compares the counts of characters needed for the message with those available in the chest.
    Args:
        message_counter (Counter): A Counter of characters needed for the message.
        chest_counter (Counter): A Counter of characters available in the chest.
    Returns:
        tuple: A tuple containing a boolean indicating if the message can be formed, and a string with details about the result.
    """
    missing = {
        c: needed - chest_counter.get(c, 0)
        for c, needed in message_counter.items()
        if chest_counter.get(c, 0) < needed
    }
    if missing:
        return False, _format_missing(missing)
    return True, "The message can be formed with the available characters." 

def _format_missing(missing: Counter) -> str:
    """Formats the missing characters into a readable string.
    Args:
        missing (Counter): A Counter of characters that are missing.
    Returns:
        str: A formatted string listing the missing characters and their counts.
    """
    missing_str = ', '.join(f"{char}({count})" for char, count in missing.items())
    return f"Missing characters: {missing_str}"
    
if __name__ == "__main__":
    print(can_form_message("SOS", "PELIGROSOS"))    # True
    print(can_form_message("HELP", "HELICOPTER"))   # True
    print(can_form_message("RESCUEA", "RSCU"))      # False
    print(can_form_message("Ñ", "N"))               # False
    print(can_form_message("112", "112A"))          # True
    print(can_form_message("NEVERGONNAGIVEYOUUPNEVERGONNALETYOUDOWN"*10, "NEVERGONNAGIVEYOUUPNEVERGONNALETYOUDOWN"))          # False
    print(can_form_message("NEVERGONNAGIVEYOUUPNEVERGONNALETYOUDOWN", "NEVERGONNAGIVEYOUUPNEVERGONNALETYOUDOWN"*10))          # True
