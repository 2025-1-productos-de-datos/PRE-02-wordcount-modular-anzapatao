"""Preprocess lines by removing punctuation and converting to lowercase.
This function takes a list of lines as input and returns a list of cleaned lines.
Example usage:
    lines = ["Hello, world!", "This is a test."]
    cleaned_lines = preprocess_lines(lines)
    print(cleaned_lines)  # Output: ['hello world', 'this is a test']
"""

import string


def preprocess_lines(all_lines):
    # Crea una tabla de traducción para eliminar todos los signos de puntuación
    translator = str.maketrans("", "", string.punctuation)

    # Aplica la limpieza a cada línea
    return [line.lower().strip().translate(translator) for line in all_lines]
