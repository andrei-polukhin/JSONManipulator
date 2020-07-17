import sys
import os

from JSONManipulator import GetInformation

GetInformation(
    key="authors", value="Glen Smith, Peter Ledbrook",
    full_path=os.path.join(
        sys.path[0],
        "examples/using_classes/books_after_set_up.json"
    )
)
