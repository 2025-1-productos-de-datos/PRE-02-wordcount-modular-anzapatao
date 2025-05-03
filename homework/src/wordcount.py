"""Word Count Program
This program reads all lines from input files, counts the frequency of each word,
and writes the results to a TSV file.
It creates the output directory if it doesn't exist.
"""

import os

from homework.src._internals.write_count_words import write_count_words


def read_all_lines():
    """
    Reads all lines from the input files and returns a list of lines.
    """
    input_file_list = os.listdir("data/input/")
    lines = []
    for filename in input_file_list:
        with open("data/input/" + filename, encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines


def main():

    all_lines = read_all_lines()

    # count the frequency of the words in the files
    counter = {}
    for line in all_lines:
        for w in line.split():
            w = w.lower().strip(",.!?")
            counter[w] = counter.get(w, 0) + 1

    write_count_words(counter, "data/output/results.tsv")


if __name__ == "__main__":
    main()
