# -*- coding: utf-8 -*-
"""The module with ``ChangeValue`` class"""

import json
import copy
from typing import List, Dict

from JSONManipulator.core.GetInformation import GetInformation


class ChangeValue(GetInformation):
    """A child class of ``GetInformation`` \
    to change values of found dictionary(-ies) simultaneously.

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
        if self.__class__ == ChangeValue:
            #  Call the function if not inherited.
            self.change_value()

    def change_value(self) -> None:
        """Inheritably call ``get_information()``, \
        then call additional in-class functions to change values of the object(s).
        """

        dictionary_container: list = self.get_information()

        if len(dictionary_container) == 1:
            print(
                "\n\nPress <Enter> if you do not want to change the value"
                "\nInput \'del\' if you want to delete that key"
                "\nOr assign the new value to the given descriptions:"
            )

            initial_dictionary = dictionary_container[0]
            self.change_one_object(initial_dictionary)

        elif len(dictionary_container) > 1:
            print("\n\n----Use this function if you want to change values "
                  "of the objects above simultaneously.----")

            option = input(
                f"\tWrite numbers of objects you want to change "
                f"(from 1 to {len(dictionary_container)}) "
                f"from the list above,"
                f"\n\ti.e. (1-3,5) or \'all\', or one number. "
            )

            print(
                "\nPress <Enter> if you do not want to change the value"
                "\nInput \'del\' if you want to delete that key"
                "\nOr assign the new value to the given descriptions:"
            )

            if option.isdecimal() and len(dictionary_container) >= int(option) >= 1:
                initial_dictionary = dictionary_container[int(option) - 1]
                self.change_one_object(initial_dictionary)

            elif option.lower() in ["all", "\'all\'"]:
                initial_dictionary_list = dictionary_container
                self.change_several_objects(initial_dictionary_list)

            elif self.format_several_objects(option, dictionary_container):
                initial_dictionary_list = self.format_several_objects(
                    option, dictionary_container
                )
                self.change_several_objects(initial_dictionary_list)

            else:
                print("Sorry, check your input.")

    def change_one_object(self, start_dictionary) -> None:
        """Change user-chosen values from the object - ``start_dictionary``."""

        changed_dictionary = copy.deepcopy(start_dictionary)

        for key_in_initial_dict, value_in_initial_dict in changed_dictionary.copy().items():
            if isinstance(value_in_initial_dict, dict):
                for desc, type_value in value_in_initial_dict.items():
                    new_value = input(f"--------<{desc}>: ")
                    if not new_value:
                        pass
                    elif new_value in ["del", "<del>"]:
                        del changed_dictionary[key_in_initial_dict]
                    else:
                        self.if_clauses(
                            type_value, changed_dictionary,
                            key_in_initial_dict, desc, new_value
                        )

        with open(self.full_path, 'r') as file:
            file_contents = json.load(file)

        file_contents = [
            element
            for element in file_contents
            if element != start_dictionary
        ]
        file_contents.append(changed_dictionary)

        with open(self.full_path, 'w') as file:
            json.dump(file_contents, file)
        print("\nSuccess!")

    def change_several_objects(self, start_list_dictionaries) -> None:
        """Change several objects from ``start_list_dictionaries`` simultaneously.
        """

        changed_list_dictionaries = copy.deepcopy(start_list_dictionaries)
        shortest_dict = min(changed_list_dictionaries, key=len)
        dict_for_change = shortest_dict.copy()
        for key, value in dict_for_change.items():
            if isinstance(value, dict):
                for desc, type_value in value.items():
                    new_value = input(f"--------<{desc}>: ")
                    if new_value in ["del", "<del>"]:
                        dict_for_change[key] = "<del>"
                    elif new_value == "":
                        dict_for_change[key] = "<continue>"
                    else:
                        self.if_clauses(
                            type_value, dict_for_change, key, desc, new_value
                        )

        for dictionary in changed_list_dictionaries:
            for initial_key in dictionary.copy().keys():
                for key_for_change, value_for_change in dict_for_change.items():
                    if initial_key == key_for_change:
                        if value_for_change == "<continue>":
                            pass
                        elif value_for_change == "<del>":
                            del dictionary[initial_key]
                        elif isinstance(value_for_change, dict):
                            dictionary[initial_key] = value_for_change

        with open(self.full_path, 'r') as file:
            file_contents = json.load(file)

        file_contents = [
            element
            for element in file_contents
            if element not in start_list_dictionaries
        ]
        file_contents.extend(changed_list_dictionaries)

        with open(self.full_path, 'w') as file:
            json.dump(file_contents, file)

        print("\nSuccess!")

    @staticmethod
    def format_several_objects(user_option, dictionary_container) -> List[Dict]:
        """Process ``user_option`` \
        and take user-chosen objects from ``dictionary_container``.

        Args:
            ``user_option (str)``: numbers of chosen dictionaries, for example, "2-4,10".
            ``dictionary_container (list)``: the list to take dictionaries from.

        Returns:
            ``List[Dict]``: the list of dictionaries which values it is necessary to change.
        """

        user_option = user_option.replace("(", "").replace(")", "")
        user_option = user_option.split(",")
        for element in user_option:
            if "-" in element:
                user_option.insert(0, element.split("-"))
                user_option.remove(element)

        if len(user_option) > 1 or \
                (len(user_option) == 1 and isinstance(user_option[0], list)):
            initial_dictionary_list = []
            for element in user_option:
                if isinstance(element, str) and element.isdecimal():
                    initial_dictionary_list.append(
                        dictionary_container[int(element) - 1]
                    )

                elif isinstance(element, list) and len(element) == 2 \
                        and int(element[0]) < int(element[1]):
                    extend_list = dictionary_container[
                                  int(element[0]) - 1: int(element[1])
                                ]
                    initial_dictionary_list.extend(extend_list)

                else:
                    print("Sorry, check your input.")
                    break
            return initial_dictionary_list

    @staticmethod
    def if_clauses(type_value, changed_dictionary,
                   key_in_initial_dict, desc, new_value) -> None:
        """Set new values to the objects in the JSON file."""

        if isinstance(type_value, (str, int, dict)):
            changed_dictionary[key_in_initial_dict] = {desc: new_value}
        elif isinstance(type_value, list):
            try:
                changed_dictionary[key_in_initial_dict] = \
                    {desc: json.loads(new_value)}
            except json.decoder.JSONDecodeError:
                changed_dictionary[key_in_initial_dict] = \
                    {desc: [new_value]}
