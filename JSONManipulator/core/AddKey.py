# -*- coding: utf-8 -*-
"""The module with ``AddKey`` class"""

import json


class AddKey:
    """A class to add a new key to each object in the JSON file.

    Args:
        ``full_path (str)``: the full path to the JSON file.

    Raises:
        ``FileNotFoundError``: \
        if the JSON file is not found by ``full_path``.\n
        ``IsADirectoryError``: \
        if ``full_path`` is to a directory, not to the JSON file.
    """

    def __init__(self, full_path):
        self.full_path = full_path
        self.add_key()

    def add_key(self) -> None:
        """Add a key to each object in the JSON file, \
        optionally with a description, with a default value.
        """

        print(
            "--------This function will add "
            "a new key to each object in your file--------"
            "\nInput all the data \'as is\', press <Enter> "
            "in case you do not need the description.\n"
        )

        input_key = input("Enter your new key: ")
        input_desc = input("Enter the description of your new key: ")
        default_value = input("Enter the default value of your key: ")

        with open(self.full_path, 'r') as file:
            file_contents = json.load(file)

        if input_key and input_desc:
            for dictionary in file_contents:
                if not dictionary.get(input_key):
                    dictionary[input_key] = {input_desc: default_value}
                elif dictionary.get(input_key):
                    print("\nSorry, your key already exists. "
                          "Try our ChangeAllValues functionality instead.")
                    break
            else:
                print("\nSuccess!")

        elif input_key and not input_desc:
            for dictionary in file_contents:
                if not dictionary.get(input_key):
                    dictionary[input_key] = default_value
                elif dictionary.get(input_key):
                    print("\nSorry, your key already exists. "
                          "Try our ChangeAllValues functionality instead.")
                    break
            else:
                print("\nSuccess!")

        else:
            print("\nSorry, you have not specified the key.")

        with open(self.full_path, 'w') as file:
            json.dump(file_contents, file)
