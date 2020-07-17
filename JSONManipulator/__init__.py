# -*- coding: utf-8 -*-

"""
NAME
    JSONManipulator.

DESCRIPTION
    A Python library to manipulate objects in JSON files.

PACKAGE CONTENTS
    ``set_up(full_path)``: initially set up the JSON file.\n
    ``GetInformation(value, full_path, levenshtein=1.0, key=None, desc=None)``: \
    retrieve information about particular objects.\n
    ``ChangeValue(value, full_path, levenshtein=1.0, key=None, desc=None)``: \
    change values of particular objects in the JSON file.\n
    ``AddObject(full_path)``: add a new object to the JSON file.\n
    ``DeleteObject(value, full_path, levenshtein=1.0, key=None, desc=None)``: \
    delete particular objects in the JSON file.\n
    ``AddKey(full_path)``: add a new key to each object in the JSON file.\n
    ``ChangeAllValues(value, full_path)``: \
    change values of all objects in the JSON file.
"""

from JSONManipulator.core import set_up, GetInformation, ChangeValue, \
    AddObject, DeleteObject, AddKey, ChangeAllValues

__author__ = """Andrew Polukhin"""
__email__ = """andrewmathematics2003@gmail.com"""
__version__ = """3.0"""
