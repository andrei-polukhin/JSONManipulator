# -*- coding: utf-8 -*-
"""The module with ``set_up`` function"""

import json
import JSONManipulator.exceptions as exceptions


def set_up(full_path) -> None:
    """Configure the initial JSON file. Add descriptions for the keys in \
    the JSON file for the further more readable retrieval.

    Args:
        ``full_path (str)``: the path to the desired file.

    Raises:
        ``FileNotFoundError``: \
        if the JSON file is not found by ``full_path``.

        ``IsADirectoryError``: \
        if ``full_path`` is to a directory, not to the JSON file.

        ``exception.NotSupportedJSONFile``: \
        if the JSON file is not supported by the package.

    """

    with open(full_path, 'r') as file:
        file_contents = json.load(file)

    if all(isinstance(dictionary, dict) for dictionary in file_contents):
        keys_list = [
            list(dictionary.keys())
            for dictionary in file_contents
        ]
        longest_key_list = max(keys_list, key=len)
        print("\nAssign a short description to the keys "
              "(press <Enter> if you don\'t need this key):")
        keys_and_description = dict()

        for item in longest_key_list:
            desc = input(f"<{item}>: ")
            if desc:
                keys_and_description[item] = desc

        for dictionary in file_contents:
            for key, desc_to_key in keys_and_description.items():
                if key in dictionary:
                    dictionary[key] = {desc_to_key: dictionary[key]}

        with open(full_path, 'w') as file:
            json.dump(file_contents, file)
        print("\nSuccess!")
    else:
        raise exceptions.NotSupportedJSONFile
