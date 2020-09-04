import json
import os
import sys

from JSONManipulator import DeleteObject


def test_delete_object():
    # -- testing the examples case
    with open(
            os.path.join(
                sys.path[0], "tests/books_after_set_up.json"
            ), "r"
    ) as file:
        initial_file_contents = json.load(file)

    with open(
            os.path.join(
                sys.path[0],
                "tests/using_classes/DeleteObject/books_after_deletion.json"
            ), "r"
    ) as file:
        new_file_contents = json.load(file)

    with open(
            os.path.join(
                sys.path[0],
                "tests/using_classes/DeleteObject/deleted_object.json"
            ), "r"
    ) as file:
        deleted_book = json.load(file)

    book = deleted_book[0]
    assert book in initial_file_contents
    assert book not in new_file_contents

    # -- testing the class
    try:
        DeleteObject(
            desc="The date of publishing", value="2020-07-16",
            full_path=os.path.join(
                sys.path[0],
                "tests/using_classes/DeleteObject/books_with_manual_books.json"
            )
        )
    except Exception:
        raise

    try:
        DeleteObject(
            key="title", value="Book for all Delete",
            levenshtein=0.79,
            full_path=os.path.join(
                sys.path[0],
                "tests/using_classes/DeleteObject/books_with_manual_books.json"
            )
        )
    except Exception:
        raise

    try:
        DeleteObject(
            key="title", value="Book for selective Delete",
            levenshtein=0.79,
            full_path=os.path.join(
                sys.path[0],
                "tests/using_classes/DeleteObject/books_with_manual_books.json"
            )
        )
    except Exception:
        raise

    try:
        DeleteObject(
            key="title", value="Is Decimal Delete",
            levenshtein=0.66,
            full_path=os.path.join(
                sys.path[0],
                "tests/using_classes/DeleteObject/books_with_manual_books.json"
            )
        )
    except Exception:
        raise
