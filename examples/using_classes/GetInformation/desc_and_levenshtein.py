import sys
import os

from JSONManipulator.core.GetInformation import GetInformaton

GetInformation(
    desc="Title", value="Unlocing Android",
    full_path=os.path.join(
        sys.path[0],
        "examples/using_classes/books_after_set_up.json"
    ),
    levenshtein=0.8  # seek elements with 80% similarity (in case of misprint, etc.)
)
