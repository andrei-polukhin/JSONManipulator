import sys
import os

from JSONManipulator.core.GetInformation import GetInformaton

GetInformation(
    desc="Categories", value=["Java"],  # ``desc`` was specified by a user in set_up()
    full_path=os.path.join(
        sys.path[0],
        "examples/using_classes/books_after_set_up.json"
            )
)
