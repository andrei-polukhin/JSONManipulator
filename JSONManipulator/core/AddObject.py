# -*- coding: utf-8 -*-
"""The module with ``AddObject`` class"""

import json
from JSONManipulator.core.ChangeValue import ChangeValue


class AddObject:
    """A class to add a new object to the JSON file.

    Args:
        ``full_path (str)``: the full path to the JSON file.
    """

    def __init__(self, full_path):
        self.full_path = full_path
        self.add_object()

    def add_object(self) -> None:
        """Add an object to the JSON file."""

        print("\nAssign the value to the descriptions "
              "(press <Enter> if you don\'t need the description):")
        with open(self.full_path, 'r') as file:
            file_contents = json.load(file)

        if all(isinstance(dictionary, dict) for dictionary in file_contents):
            longest_dict = max(file_contents, key=len)
            example_dict = longest_dict.copy()
            for dict_key, dict_value in example_dict.copy().items():
                if isinstance(dict_value, dict):
                    for desc, initial_value in dict_value.items():
                        new_value = input(f"--------<{desc}>: ")
                        if not new_value:
                            del example_dict[dict_key]
                        else:
                            ChangeValue.if_clauses(
                                initial_value, example_dict, dict_key, desc, new_value
                            )
                else:
                    del example_dict[dict_key]

            file_contents.append(example_dict)

            with open(self.full_path, 'w') as file:
                json.dump(file_contents, file)

            print("\nSuccess!")
