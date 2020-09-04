import sys
import os

from JSONManipulator.core.ChangeValue import ChangeValue

ChangeValue(
    key="title", value="Flex", levenshtein=0.3,  # to find all the books with `Flex`
    full_path=os.path.join(
        sys.path[0],
        "examples/using_classes/ChangeValue/books_with_changed_value.json"
            )
)
