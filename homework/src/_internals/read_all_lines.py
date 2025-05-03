"""
@file: read_all_lines.py
@description: This module contains a function to read all lines from files in the input directory.
It creates the input directory if it doesn't exist.
"""

import os


def read_all_lines(input_folder="data/input"):
    all_lines = []
    input_file_list = os.listdir(input_folder)
    for filename in input_file_list:
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)

    ## mover a "preprocess_lines"
    all_lines = [line.lower().strip() for line in all_lines]
    return all_lines
