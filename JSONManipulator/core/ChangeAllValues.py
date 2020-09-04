# -*- coding: utf-8 -*-
"""The module with ``ChangeAllValues`` class"""

import json
from JSONManipulator.core.ChangeValue import ChangeValue


class ChangeAllValues(ChangeValue):
    """A class to change values of all objects in the JSON file.

    Args:
        ``value (str)``: a redundant parameter, \
        exists as mandatory in the parent class.\n
        ``full_path (str)``: the full path to the JSON file.\n

    Raises:
        ``FileNotFoundError``: \
        if the JSON file is not found by ``full_path``.\n
        ``IsADirectoryError``: \
        if ``full_path`` is to a directory, not to the JSON file.
    """

    def __init__(self, full_path, value=""):
        super().__init__(value, full_path)
        self.change_all_values()

    def change_all_values(self) -> None:
        """Change the values of all objects in the JSON file."""

        print(
            "--------Use this "
            "only if you want to change the key'(s) values "
            "of all objects--------"
        )
        option = input("Proceed? (Y/n) ")

        if option.lower() in ["y", "yes"]:
            print(
                "\nPress <Enter> if you do not want to change the value"
                "\nInput \'del\' if you want to delete that key"
                "\nOr assign the new value to the given descriptions:"
            )

            with open(self.full_path, 'r') as file:
                file_contents = json.load(file)

            self.change_several_objects(file_contents)
        else:
            print("Process terminated.")
