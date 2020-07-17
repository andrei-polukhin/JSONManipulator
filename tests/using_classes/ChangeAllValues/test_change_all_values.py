import pytest
import json
import os
import sys

from JSONManipulator import ChangeAllValues


def test_change_all_values():
    # -- testing ChangeAllValues results from ``examples``
    with open(os.path.join(sys.path[0],
                           "tests/using_classes/ChangeAllValues/books_with_changed_values.json"), "r") \
            as file:
        file_contents = json.load(file)

    for dictionary in file_contents:
        dictionary: dict
        assert dictionary["reading_status"]["Reading Status"] == "Maybe Will Read Later..."

    # -- testing class ChangeAllValues
    with pytest.raises(SystemExit) as e:
        ChangeAllValues(
            full_path=os.path.join(
                sys.path[0],
                "tests/using_classes/ChangeAllValues/books_with_changed_values.json"
            )
        )
    assert e.value.code == 0
