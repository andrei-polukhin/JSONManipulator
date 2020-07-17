import pytest
import json
import os
import sys

from JSONManipulator import set_up
from JSONManipulator.exceptions import NotSupportedJSONFile


def test_set_up():
    # -- testing already set up books from ``examples``
    with open(os.path.join(sys.path[0], "tests/books_after_set_up.json"), "r") as file:
        file_contents = json.load(file)

    for dictionary in file_contents:
        dictionary: dict

        if dictionary.get("title"):
            assert isinstance(dictionary["title"], dict)
        if dictionary.get("isbn"):
            assert isinstance(dictionary["isbn"], dict)
        if dictionary.get("pageCount"):
            assert isinstance(dictionary["pageCount"], dict)
        if dictionary.get("publishedDate"):
            assert isinstance(dictionary["publishedDate"], dict)
        if dictionary.get("shortDescription"):
            assert isinstance(dictionary["shortDescription"], dict)
        if dictionary.get("authors"):
            assert isinstance(dictionary["authors"], dict)
        if dictionary.get("categories"):
            assert isinstance(dictionary["categories"], dict)

    # -- testing set_up() function
    with pytest.raises(NotSupportedJSONFile):
        assert set_up(
            os.path.join(
                sys.path[0],
                "tests/set_up/unsupported_file.json"
            )
        )

    with pytest.raises(FileNotFoundError):
        assert set_up("some_folder/file.json")

    with pytest.raises(IsADirectoryError):
        assert set_up(os.path.join(sys.path[0],
                                   "tests"))

    # -- real set up
    with pytest.raises(SystemExit) as e:
        set_up(
            os.path.join(
                sys.path[0],
                "tests/set_up/books_to_set_up.json"
            )
        )
    assert e.value.code == 0  # exited at code 0 (successfully finished)
