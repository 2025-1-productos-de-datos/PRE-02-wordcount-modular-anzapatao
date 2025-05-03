"""
This module contains a function to write word count results to a file in TSV format.
It creates the output directory if it doesn't exist.
"""

import os


def write_word_counts(counter, output_file):
    """
    Saves the word count results to a file in TSV format.
    Creates the output directory if it doesn't exist.
    """
    output_file = output_file + "/results.tsv"
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_file, "w", encoding="utf-8") as f:
        for key, value in counter.items():
            f.write(f"{key}\t{value}\n")
