import sys
import os

from JSONManipulator import AddObject

AddObject(
    os.path.join(
        sys.path[0],
        "examples/using_classes/AddObject/books_with_added_object.json"
    )
)
