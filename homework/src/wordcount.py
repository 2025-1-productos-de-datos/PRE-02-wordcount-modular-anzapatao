"""Word count program.
This program counts the frequency of words in a given text file.
It reads the input files from a specified directory, processes the lines,
splits them into words, counts the occurrences of each word, and writes the results to an output file.
Example usage:
    python wordcount.py data/input data/output
"""

import sys

from homework.src._internals.count_words import count_words
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words
from homework.src._internals.write_word_counts import write_word_counts


# "homework/src/_internals/count_words.py",
# "homework/src/_internals/read_all_lines.py",
# "homework/src/_internals/split_into_words.py",
# "homework/src/_internals/write_word_counts.py",
def main():
    if len(sys.argv) != 3:
        print("Usage: python3 -m homework <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)

    words = split_into_words(all_lines)

    counter = count_words(words)

    write_word_counts(counter, output_folder)


if __name__ == "__main__":
    main()
