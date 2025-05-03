"""
Split a list of lines into a list of words.
This function takes a list of lines as input and returns a list of words.
It removes punctuation and converts words to lowercase.
Example usage:
    lines = ["Hello, world!", "This is a test."]
    words = split_into_words(lines)
    print(words)  # Output: ['hello', 'world', 'this', 'is', 'a', 'test']
"""


def split_into_words(all_lines):
    words = []
    for line in all_lines:
        words.extend(word.strip(",.!?") for word in line.split())
    return words
