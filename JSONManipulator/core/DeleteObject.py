# -*- coding: utf-8 -*-
"""The module with ``DeleteObject`` class"""

import json
from JSONManipulator.core.ChangeValue import ChangeValue


class DeleteObject(ChangeValue):
    """A class to delete found objects.

    Args:
        ``key (str)``: to find the object by the key in the JSON file.\n
        ``desc (str)``: to find the object by the description.\n
        ``full_path (str)``: the full path to the JSON file.\n
        ``value (str)``: the value of ``key``/``desc`` \
        which will be used to find the object(s).\n
        ``levenshtein (float)``: the similarity of the elicited objects \
        to the input. By default, seeks 100% similarity.

    Raises:
        ``exceptions.NoKeyAndDesc``: \
        if neither ``key`` nor ``desc`` is entered.\n
        ``FileNotFoundError``: \
        if the JSON file is not found by ``full_path``.\n
        ``IsADirectoryError``: \
        if ``full_path`` is to a directory, not to the JSON file.
    """

    __slots__ = ["value", "full_path", "levenshtein", "key", "desc"]

    def __init__(self, value, full_path, levenshtein=1.0, key=None,
                 desc=None):
        super().__init__(value, full_path, levenshtein, key, desc)
        self.delete_object()

    def delete_object(self) -> None:
        """Take the list of objects, after a user chose ones to delete, \
        call ``execute_delete()`` function.
        """

        dictionary_container: list = self.get_information()

        if len(dictionary_container) == 1:
            option = input("\nDelete the object (Y/n)? ")
            if option.lower() in ["y", "yes"]:
                self.execute_delete(dictionary_container)

        elif len(dictionary_container) > 1:
            print("\n\n----Use this function if you want to delete "
                  "several objects above simultaneously.----")

            option = input(
                f"\tWrite numbers of objects you want to change "
                f"(from 1 to {len(dictionary_container)}) "
                f"from the list above,"
                f"\n\ti.e. (1-3,5) or \'all\', or one number. "
            )

            if option.isdecimal() and len(dictionary_container) >= int(option) >= 1:
                execution_dict = dictionary_container[int(option) - 1]
                execution_container = [execution_dict]

                self.execute_delete(execution_container)
            elif option.lower() in ["all", "\'all\'"]:
                self.execute_delete(dictionary_container)

            elif self.format_several_objects(option, dictionary_container):
                execution_container = self.format_several_objects(
                    option, dictionary_container
                )

                self.execute_delete(execution_container)
            else:
                print("\nSorry, check your input.")

    def execute_delete(self, dict_container) -> None:
        """Delete redundant objects."""

        with open(self.full_path, 'r') as file:
            file_contents = json.load(file)

        file_contents = [
            dictionary
            for dictionary in file_contents
            if dictionary not in dict_container
        ]

        with open(self.full_path, 'w') as file:
            json.dump(file_contents, file)

        print("\nSuccess!")
