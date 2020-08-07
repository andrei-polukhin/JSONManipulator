import pytest
import os
import sys

from JSONManipulator import GetInformation


def test_get_information():
    # -- testing the class
    with pytest.raises(FileNotFoundError):
        assert GetInformation(
            key="categories", value=["Web Development"],
            full_path="some_folder/file.json"
        )

    with pytest.raises(IsADirectoryError):
        assert GetInformation(
            desc="The date of publishing", value="2018-09-20",
            full_path=os.path.join(sys.path[0],
                                   "tests"
                                   )
        )

    try:
        GetInformation(
            desc="Categories", value="Java",
            full_path=os.path.join(
                sys.path[0], "tests/books_after_set_up.json"
            )
        )
    except Exception:
        raise

    try:
        GetInformation(
            key="title", value="SBCD Exam Study Kit",  # mistake, but correlated by levenshtein
            levenshtein=0.7,
            full_path=os.path.join(
                sys.path[0], "tests/books_after_set_up.json"
            )
        )
    except Exception:
        raise

    try:
        GetInformation(
            desc="Authors",
            value="W. Frank Aleson, Charlie Collins, Robi Sen",  # mistake, but correlated by levenshtein
            levenshtein=0.6,
            full_path=os.path.join(
                sys.path[0], "tests/books_after_set_up.json"
            )
        )
    except Exception:
        raise

    try:
        GetInformation(
            desc="Title",
            value="Not found book",
            full_path=os.path.join(
                sys.path[0], "tests/books_after_set_up.json"
            )
        )
    except Exception:
        raise
