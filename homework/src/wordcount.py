# obtain a list of files in the input directory
import os

from homework.src._internals.count_words import count_words
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_in_words import split_in_words
from homework.src._internals.write_count_words import write_count_words


def main():

    ## mover a la funcion "read_all_lines"
    all_lines = read_all_lines()

    ## mover "split_in_words"
    words = split_in_words(all_lines)

    ## mover a "count_words"
    counter = count_words(words)

    # count the frequency of the words in the files in the input directory
    # counter = {}
    # for filename in input_file_list:
    #     with open("data/input/" + filename) as f:
    #         for l in f:
    #             for w in l.split():
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    ##
    write_count_words(counter, "data/output/results.tsv")


if __name__ == "__main__":
    main()
    main()
    main()
