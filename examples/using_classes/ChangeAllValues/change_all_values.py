import sys
import os

from JSONManipulator import ChangeAllValues

ChangeAllValues(
    os.path.join(
        sys.path[0],
        "examples/using_classes/ChangeAllValues/books_with_changed_values.json"
    )
)
