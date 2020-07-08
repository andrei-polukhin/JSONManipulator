from JSONManipulator.core import GetInformation

GetInformation(
    desc="Title", value="Unlocing Android",
    full_path="/"
              "/examples/using_classes/books_after_set_up.json",  # specify your path.
    levenshtein=0.8  # seek elements with 80% similarity (in case of misprint, etc.)
)
