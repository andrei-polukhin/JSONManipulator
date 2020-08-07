import json
import os
import sys

from JSONManipulator import AddObject


def test_add_object():
    # -- testing already Added Object from ``examples``
    with open(
            os.path.join(
                sys.path[0],
                "tests/using_classes/AddObject/books_with_added_object.json"
            ), "r"
    ) as file:
        file_contents = json.load(file)

    with open(
            os.path.join(
                sys.path[0],
                "tests/using_classes/AddObject/added_object.json"
            ), "r"
    ) as file:
        added_object = json.load(file)

    added_dictionary = added_object[0]
    assert added_dictionary in file_contents

    # -- testing class AddObject
    try:
        AddObject(
            os.path.join(
                sys.path[0],
                "tests/using_classes/AddObject/books_with_added_object.json"
            )
        )
    except Exception:
        raise
