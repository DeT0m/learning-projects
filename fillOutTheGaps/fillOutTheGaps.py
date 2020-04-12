#!usr/bin/env python3

#  Fill out gaps in numbering in filenames of a given folder

import os
import re
from pathlib import Path

# Input from user
p_input = Path(input('Folder path: '))  # Path to folder
prefix = input('File prefix: ')  # File number prefix

# Building Regex
files_regex = re.compile(rf'''
    ({prefix})      # Filenumber prefix
    (0*)            # Zeroes preceding number
    ([0-9]+)        # Actual file number
    (.*)            # Filenumber suffix
    (\.)            # Dot
    ([a-z]{{3}})    # File extensions
    ''', re.VERBOSE)

file_names = {}  # Dictionary for all matched files

for filename in os.listdir(p_input):  # Iterating over folder files
    if files_regex.match(filename):
        regex_found = files_regex.search(filename)

        # Building necessary dictionary items
        file_names[filename] = {
            'zeroes': regex_found.group(2),
            'numbers': regex_found.group(3),
            'suffix': regex_found.group(4),
            'extension': regex_found.group(6),
        }

file_numbers = list(sorted(file_names.keys()))  # Sorted all original filenames

for i in range(1, len(file_numbers)):  # Iterating from second file in list
    original_filename = file_numbers[i]
    # Defining correct order of file numbers
    minus_one = (int(file_names[file_numbers[i]]['numbers']) - 1)
    previous = int(file_names[file_numbers[i - 1]]['numbers'])

    if minus_one != previous:  # Detecting incorrect file number order
        # Counting file number length
        num_length = (len(file_names[file_numbers[i]]['numbers'])
                      + len(file_names[file_numbers[i]]['zeroes']))

        new_filenumber = str(previous + 1)  # defining new file number
        new_zeroes = num_length - len(new_filenumber)  # defining zeroes count

        # Assigning new values to filename key in dictionary
        file_names[file_numbers[i]]['zeroes'] = new_zeroes * '0'
        file_names[file_numbers[i]]['numbers'] = new_filenumber

        # Building new filename
        new_filename = (
            prefix
            + file_names[file_numbers[i]]['zeroes']
            + file_names[file_numbers[i]]['numbers']
            + file_names[file_numbers[i]]['suffix']
            + '.'
            + file_names[file_numbers[i]]['extension']
        )
        print(f'\nRenaming:\n\tOriginal filename: {original_filename}')
        print(f'\tto new filename: {new_filename}')

        # Defining filepaths
        file_path = Path(p_input / original_filename)
        new_file_path = Path(p_input / new_filename)

        # Renaming files
        os.rename(file_path, new_file_path)
