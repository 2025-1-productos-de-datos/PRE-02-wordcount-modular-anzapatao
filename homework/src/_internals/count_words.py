"""
count_words.py
This module contains a function to count the frequency of words in a list.
It creates a dictionary with words as keys and their frequencies as values.
The function is designed to be used in a word counting application.
Example usage:
    words = ["hello", "world", "hello"]
    result = count_words(words)
    print(result)  # Output: {'hello': 2, 'world': 1}
"""


def count_words(words):
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter
