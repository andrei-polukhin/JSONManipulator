import json
import os
import sys

from JSONManipulator.core.AddKey import AddKey


def test_add_key():
    # -- testing books with already Added Key
    with open(
            os.path.join(
                sys.path[0],
                "tests/using_classes/AddKey/books_with_added_key.json"
            ), "r"
    ) as file:
        file_contents = json.load(file)

    for dictionary in file_contents:
        dictionary: dict
        assert isinstance(dictionary["reading_status"], dict)
        assert dictionary["reading_status"]["Reading Status"] == "Not Read"

    # -- testing class
    try:
        AddKey(
            os.path.join(
                sys.path[0],
                "tests/using_classes/AddKey/books_with_added_key.json"
            )
        )
    except Exception:
        raise

    try:
        AddKey(
            os.path.join(
                sys.path[0],
                "tests/using_classes/AddKey/books_with_added_key.json"
            )
        )
    except Exception:
        raise

    try:
        AddKey(
            os.path.join(
                sys.path[0],
                "tests/using_classes/AddKey/books_with_added_key.json"
            )
        )
    except Exception:
        raise
