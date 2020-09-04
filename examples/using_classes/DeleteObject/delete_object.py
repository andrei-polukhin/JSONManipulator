import sys
import os

from JSONManipulator.core.DeleteObject import DeleteObject

DeleteObject(
    key="isbn", value=1935182927,
    full_path=os.path.join(
        sys.path[0],
        "examples/using_classes/DeleteObject/books_after_deletion.json"
            )
)
