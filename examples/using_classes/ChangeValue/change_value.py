from JSONManipulator import ChangeValue

ChangeValue(
    key="title", value="Flex", levenshtein=0.3,  # to find all books with `Flex`
    full_path="/"
              "/examples/using_classes/ChangeValue/books_with_changed_value.json"  # specify your path.
)
