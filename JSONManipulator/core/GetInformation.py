# -*- coding: utf-8 -*-
"""The module with ``GetInformation`` class"""

import json
from typing import List, Dict
from difflib import SequenceMatcher
import JSONManipulator.exceptions as exceptions


class GetInformation:
    """The base class to retrieve the information about desired object(s).

    Args:
        ``key (str)``: to find the object by the key in the JSON file.\n
        ``desc (str)``: to find the object by the description.\n
        ``full_path (str)``: the full path to the JSON file.\n
        ``value (str)``: the value of ``key``/``desc`` \
        which will be used to find the object(s).\n
        ``levenshtein (float)``: the similarity of the elicited objects \
        to the input. By default, seeks 100% similarity.\n

    Raises:
        ``exceptions.NoKeyAndDesc``: \
        if neither ``key`` nor ``desc`` is entered.\n
        ``FileNotFoundError``: \
        if the JSON file is not found by ``full_path``.\n
        ``IsADirectoryError``: \
        if ``full_path`` is to a directory, not to the JSON file.\n
    """

    __slots__ = ["value", "full_path", "levenshtein", "key",
                 "desc", "output_dict_container"]

    def __init__(self, value, full_path, levenshtein=1.0, key=None,
                 desc=None):
        self.desc = desc
        self.value = value
        self.levenshtein = levenshtein
        self.key = key
        self.full_path = full_path
        self.output_dict_container = []
        if self.__class__ == GetInformation:
            #  Call the function if not inherited.
            self.get_information()

    def get_information(self) -> List[Dict] or None:
        """Process the user's parameters and the JSON file's values, \
        then call additional in-class functions to analyse data \
        and output objects, accordingly.

        Returns:
            ``List[Dict]``: if ``GetInformation`` is a parent class - \
            for ``list of dictionaries`` manipulations.\n
            ``None``: else.
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
                "You have specified the directory, not the path to the JSON file."
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
                    and self.cap_sentence(self.value):
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
                self.output_for_key_and_value()

            elif self.desc and self.value:
                for dictionary in file_contents:
                    for value in dictionary.values():
                        if isinstance(value, dict):
                            for key, end_value in value.items():
                                if key == self.desc:
                                    self.levenshtein_calc(end_value, dictionary)
                                    continue

                self.output_for_key_and_value()

        if self.__class__ != GetInformation:
            return self.output_dict_container

    def levenshtein_calc(self, dictionary_value, dictionary) -> None:
        """Compare processed ``object.value`` and ``dictionary_value``, \
        and if the similarity is higher than ``object.levenshtein`` \
        - append to the list for the further output.
        """

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
                SequenceMatcher(
                    None, dictionary_value[i],
                    self.value[i]
                ).ratio() >= self.levenshtein
                for i in range(short_list)
            )

            if 1 >= short_list / long_list >= 0.8 * self.levenshtein \
                and similarity_of_lists >= 0.6 * self.levenshtein \
                and all(similarity_of_words):
                self.output_dict_container.append(dictionary)

    def output_for_key_and_value(self) -> None:
        """Process ``object.output_dict_container`` from ``levenshtein_calc()``, \
        beautify the output of the objects.
        """

        for dict_in_list in self.output_dict_container:
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
        if not self.output_dict_container:
            print("No objects found.")

    @staticmethod
    def cap_sentence(string) -> bool:
        """Check if ``string`` looks like a person's first, middle or/and last names.

        Returns:
            ``True``: if the entered data is about a person.\n
            ``False``: else.
        """

        str_for_check = " ".join(w[:1].upper() + w[1:] for w in string.split(" "))
        return str_for_check == string
