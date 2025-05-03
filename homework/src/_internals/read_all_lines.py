"""
@file: read_all_lines.py
@description: This module contains a function to read all lines from files in the input directory.
It creates the input directory if it doesn't exist.
"""

import os


def read_all_lines():
    all_lines = []
    input_file_list = os.listdir("data/input/")
    for filename in input_file_list:
        file_path = os.path.join("data/input", filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)

    ## mover a "preprocess_lines"
    all_lines = [line.lower().strip() for line in all_lines]
    return all_lines
