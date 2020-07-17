import pytest
import json
import os
import sys

from JSONManipulator import ChangeValue
from JSONManipulator.exceptions import NoKeyAndDesc


def test_change_value():
    # -- testing ChangeValue results from ``examples``
    with open(os.path.join(sys.path[0], "tests/books_after_set_up.json"), "r") as file:
        file_contents = json.load(file)

    with open(os.path.join(sys.path[0],
                           "tests/using_classes/ChangeValue/books_with_changed_value.json"), "r") as file:
        changed_contents = json.load(file)

    with open(os.path.join(sys.path[0],
                           "tests/using_classes/ChangeValue/found_objects.json"), "r") as file:
        found_objects = json.load(file)

    def test_frequency():
        for changed_dict in changed_contents:
            if changed_dict["title"]["Title"] == "Just one Flex book":
                yield changed_dict

    unchanged_object = found_objects[3]
    later_changed_objects = found_objects[0:3]

    for found_dict in found_objects:
        assert found_dict in file_contents
    for later_changed_object in later_changed_objects:
        assert later_changed_object not in changed_contents
    assert unchanged_object in changed_contents

    g = test_frequency()
    assert sum(1 for _ in g) == 3  # To circumvent absence of len() for generators.

    # testing class ``ChangeValue``
    with pytest.raises(NoKeyAndDesc):
        assert ChangeValue(
            value="alphabet",
            full_path=os.path.join(
                sys.path[0], "tests/books_after_set_up.json"
            )
        )
    with pytest.raises(SystemExit) as e:
        ChangeValue(
            desc="Authors", value=["Andrew Polukhin"],
            full_path=os.path.join(
                sys.path[0],
                "tests/using_classes/ChangeValue/books_with_manual_book.json"
            )
        )
    assert e.value.code == 0
