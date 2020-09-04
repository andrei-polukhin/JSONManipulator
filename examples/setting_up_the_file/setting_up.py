import sys
import os

from JSONManipulator.core.set_up import set_up

set_up(
    full_path=os.path.join(
                sys.path[0], "examples/setting_up_the_file/books_after_set_up.json"
            )
)
