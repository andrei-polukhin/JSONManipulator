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

from JSONManipulator.core import *

__author__ = """Andrew Polukhin"""
__email__ = """andrewmathematics2003@gmail.com"""
__version__ = """2.0"""
