# -*- coding: utf-8 -*-
"""
NAME
    JSONManipulator

DESCRIPTION
    A Python library to manipulate objects in JSON files.

PACKAGE CONTENTS
    set_up(full_path): initially set up the JSON file.
    GetInformation(value, full_path, levenshtein=1.0, key=None,
                 desc=None): retrieve information about specific objects.
    ChangeValue(value, full_path, levenshtein=1.0, key=None,
                 desc=None): change values of specific objects in the file.
    AddObject(full_path): add a new object to the file.
    DeleteObject(value, full_path, levenshtein=1.0, key=None,
                 desc=None): delete specific objects in the file.
    AddKey(full_path): add a new key to each object in the file.
    ChangeAllValues(value, full_path): change values of all objects in the file.
"""

import json
import copy
from typing import List, Dict
from difflib import SequenceMatcher

import JSONManipulator.exceptions as exceptions


def set_up(full_path) -> None:
    """Configure the initial *.json file.
    Add descriptions for the keys in the file
    for the further more readable retrieval.

    Args:
        full_path (str): path to the desired file.

    Raises:
        FileNotFoundError:
         if the file is not found by ``full_path``.
        IsADirectoryError:
         if ``full_path`` is for a directory, not for the file.
        exception.NotSupportedJSONFile:
         if the file is not supported by the package.
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


output_dict_container = list()


class GetInformation:
    """The base class to retrieve the information about desired object(s).

    Args:
        key (str): to find the object by the key in the *.json file.
        desc (str): to find the object by the description.
        full_path (str): the full path to the *.json file.
        value (str): the value of the key/desc
         which will be used to find the object(s).
        levenshtein (float): the similarity of the elicited objects
         to the input. By default, seeks 100% similarity.

    Raises:
        exceptions.EnterKeyOrDesc:
         if neither ``key`` nor ``desc`` is entered.
        FileNotFoundError: if the file is not found by the ``full_path``.
        IsADirectoryError:
         if ``full_path`` is for a directory, not for the file.
    """

    def __init__(self, value, full_path, levenshtein=1.0, key=None,
                 desc=None):
        self.desc = desc
        self.value = value
        self.levenshtein = levenshtein
        self.key = key
        self.full_path = full_path
        if self.__class__ == GetInformation:
            #  Calls the function if not inherited.
            self.get_information()

    def get_information(self) -> List[Dict] or None:
        """Process the user's parameters and the *.json file's values,
        after which call additional in-class functions
        to analyse data and output objects, accordingly.

        Returns:
            List[Dict]: if ``GetInformation`` is a parent class -
             for ``list of dictionaries`` manipulations.
            None: else.
        """

        if not (self.key or self.desc):
            raise exceptions.NoKeyAndDesc
        try:
            with open(self.full_path, 'r') as file:
                file_contents = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Check the path to your file")
        except IsADirectoryError:
            raise IsADirectoryError(
                "You have specified the directory, not the path to the file."
            )
        else:
            if isinstance(self.value, list):
                self.value = [
                    str(element).upper().strip().replace(",", "")
                    for element in self.value
                    if isinstance(element, (str, int, float))
                ]

            if isinstance(self.value, (str, int, float)):
                if isinstance(self.value, str) and ", " in self.value \
                        and self.cap_sentence():
                    self.value = self.value.upper().strip().split(", ")
                else:
                    str_value = str(self.value)
                    self.value = str_value.upper().strip().replace(",", "").split()

            if self.key and self.value:
                for dictionary in file_contents:
                    if self.key in dictionary:
                        temporary_key = dictionary[self.key]
                        self.levenshtein_calc(temporary_key, dictionary)
                        continue
                self.output_for_key_and_value(output_dict_container)

            elif self.desc and self.value:
                for dictionary in file_contents:
                    for value in dictionary.values():
                        if isinstance(value, dict):
                            for key, end_value in value.items():
                                if key == self.desc:
                                    temporary_key = end_value
                                    self.levenshtein_calc(temporary_key, dictionary)
                                    continue

                self.output_for_key_and_value(output_dict_container)

        if self.__class__ != GetInformation:
            return output_dict_container

    def levenshtein_calc(self, dictionary_value, dictionary) -> None:
        """Compare processed ``self.value`` and ``dictionary_value``,
        and if the similarity is higher than ``self.levenshtein`` -
        append to the list for the further output."""

        while isinstance(dictionary_value, dict):
            dictionary_value = list(dictionary_value.values())[0]

        if isinstance(dictionary_value, list):
            dictionary_value = [
                str(element).upper().strip().replace(",", "")
                for element in dictionary_value
                if element and isinstance(element, (str, int, float))
            ]

        if isinstance(dictionary_value, (str, int, float)):
            str_value = str(dictionary_value)
            new_str_value = str_value.upper().strip().replace(",", "")
            dictionary_value = new_str_value.split()

        if isinstance(self.levenshtein, (float, int)) \
                and 1 >= self.levenshtein > 0:
            long_list = len(max(dictionary_value, self.value))
            short_list = len(min(dictionary_value, self.value))

            similarity_of_lists = SequenceMatcher(
                None, dictionary_value, self.value
            ).ratio()

            similarity_of_words = (
                SequenceMatcher(None, dictionary_value[i],
                                self.value[i]).ratio() >=
                self.levenshtein for i in range(short_list)
            )

            if 1 >= short_list / long_list >= 0.8 * self.levenshtein \
                    and similarity_of_lists >= 0.6 * self.levenshtein \
                    and all(similarity_of_words):
                output_dict_container.append(dictionary)

    @staticmethod
    def output_for_key_and_value(list_container) -> None:
        """Process ``list_container`` from ``levenshtein_calc()``,
        beautify the output of the objects."""

        for dict_in_list in list_container:
            print()
            for value in dict_in_list.values():
                if isinstance(value, dict):
                    for description, exact_value in value.items():
                        while exact_value and isinstance(exact_value, dict):
                            exact_value = list(exact_value.values())[0]

                        if isinstance(exact_value, str) and len(exact_value) >= 50:
                            str_output = exact_value.replace(". ", ".\n\r\t\t\t\t\t")
                            print(f"{description}:\t{str_output}")
                            continue

                        if exact_value and isinstance(exact_value, list):
                            exact_value = [
                                element for element in exact_value
                                if element
                            ]
                            list_output = ", ".join(exact_value)
                            print(f"{description}:\t\t{list_output}")
                            continue

                        if exact_value:
                            print(f"{description}:\t\t{exact_value}")
                            continue
        if not list_container:
            print("No objects found.")

    def cap_sentence(self) -> bool:
        """Check if ``string`` looks like person's first or/and last names.

        Returns:
            True: if the entered data is about a person.
            False: else.
        """

        str_for_check = " ".join(w[:1].upper() + w[1:] for w in self.value.split(" "))
        return str_for_check == self.value


class ChangeValue(GetInformation):
    """A child class of ``GetInformation``
    to change values simultaneously of found dictionary(-ies).

    Args:
        key (str): to find the object by the key in the *.json file.
        desc (str): to find the object by the description.
        full_path (str): the full path to the *.json file.
        value (str): the value of the key/desc
         which will be used to find the object(s).
        levenshtein (float): the similarity of the elicited objects
         to the input. By default, seeks 100% similarity.

    Raises:
        exceptions.EnterKeyOrDesc:
         if neither ``key`` nor ``desc`` is entered.
        FileNotFoundError:
         if the file is not found by the ``full_path``.
        IsADirectoryError:
         if ``full_path`` is for a directory, not for the file.
    """

    def __init__(self, value, full_path, levenshtein=1.0, key=None,
                 desc=None):
        super().__init__(value, full_path, levenshtein, key, desc)
        if self.__class__ == ChangeValue:
            #  Calls the function if not inherited.
            self.change_value()

    def change_value(self) -> None:
        """Inheritably call ``get_information()``, then call additional
        in-class functions to change values of object(s)."""

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
        """Change user-chosen values from the object -
        ``start_dictionary``."""

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
        """Change several objects from ``start_list_dictionaries``
        simultaneously."""

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
        """Process ``user_option`` and take several
        user-chosen objects from ``dictionary_container``.

        Args:
            user_option (str): numbers of chosen dictionaries,
             for example "2-4,10".
            dictionary_container (list): the list to take
             dictionaries from.

        Returns:
            List[Dict]: the list of dictionaries which values
             it is necessary to change.
        """

        user_option = user_option.replace("(", "").replace(")", "")
        user_option = user_option.split(",")
        for element in user_option:
            if "-" in element:
                user_option.insert(0, element.split("-"))
                user_option.remove(element)

        if len(user_option) > 1 or \
                (len(user_option) == 1 and isinstance(user_option[0], list)):
            initial_dictionary_list = list()
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
        """Set new values to the objects."""

        if isinstance(type_value, (str, int, dict)):
            changed_dictionary[key_in_initial_dict] = {desc: new_value}
        elif isinstance(type_value, list):
            try:
                changed_dictionary[key_in_initial_dict] = \
                    {desc: json.loads(new_value)}
            except json.decoder.JSONDecodeError:
                changed_dictionary[key_in_initial_dict] = \
                    {desc: [new_value]}


class AddObject:
    """A class to add a new object to the file.

    Args:
        full_path (str): the full path to the *.json file.
    """

    def __init__(self, full_path):
        self.full_path = full_path
        self.add_object()

    def add_object(self) -> None:
        """Add an object to the file."""

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


class DeleteObject(ChangeValue):
    """A class to delete found objects.

    Args:
        key (str): to find the object by the key in the *.json file.
        desc (str): to find the object by the description.
        full_path (str): the full path to the *.json file.
        value (str): the value of the key/desc
         which will be used to find the object(s).
        levenshtein (float): the similarity of the elicited objects
         to the input. By default, seeks 100% similarity.

    Raises:
        exceptions.EnterKeyOrDesc:
         if neither ``key`` nor ``desc`` is entered.
        FileNotFoundError:
         if the file is not found by the ``full_path``.
        IsADirectoryError:
         if ``full_path`` is for a directory, not for the file.
    """

    def __init__(self, value, full_path, levenshtein=1.0, key=None,
                 desc=None):
        super().__init__(value, full_path, levenshtein, key, desc)
        self.delete_object()

    def delete_object(self) -> None:
        """Take the list of objects, after a user chose ones to delete,
        call ``execute_delete()`` function."""

        dictionary_container: list = self.get_information()

        if len(dictionary_container) == 1:
            option = input("\nDelete the object (Y/n)? ")
            if option.lower() in ["y", "yes"]:
                execution_container = dictionary_container
                self.execute_delete(execution_container)

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
                execution_container = dictionary_container[int(option) - 1]

                self.execute_delete(execution_container)
            elif option.lower() in ["all", "\'all\'"]:
                execution_container = dictionary_container

                self.execute_delete(execution_container)
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


class AddKey:
    """A class to add a new key to each object.

    Args:
        full_path (str): the full path to the *.json file.

    Raises:
        FileNotFoundError:
         if the file is not found by ``full_path``.
        IsADirectoryError:
         if ``full_path`` is for a directory, not for the file.
    """

    def __init__(self, full_path):
        self.full_path = full_path
        self.add_key()

    def add_key(self) -> None:
        """Add a key to each object in the file, optionally with description,
        with a default value."""

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


class ChangeAllValues(ChangeValue):
    """A class to change values of all objects in the file.

    Args:
        value (str):
         a redundant parameter, exists as mandatory in the parent class.
        full_path (str): the full path to the *.json file.

    Raises:
        FileNotFoundError: if the file is not found by ``full_path``.
        IsADirectoryError: if ``full_path`` is for a directory,
         not for the file.
    """

    def __init__(self, full_path, value=""):
        super().__init__(value, full_path)
        self.change_all_values()

    def change_all_values(self) -> None:
        """Change the values of all objects in the file."""

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
