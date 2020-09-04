import sys
import os

from JSONManipulator.core.AddKey import AddKey

AddKey(
    os.path.join(
                sys.path[0], "examples/using_classes/AddKey/books_with_added_key.json"
            )
)
