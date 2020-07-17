# -*- coding: utf-8 -*-

"""The JSONManipulator's exceptions."""


class NoKeyAndDesc(Exception):
    """Raised when a user has entered neither key nor desc."""

    def __init__(self):
        super().__init__(
            "You have entered neither ``key``, nor ``desc``,"
            " process terminated."
        )


class NotSupportedJSONFile(Exception):
    """Raised when the JSON file's structure \
    does not confront to [{...},{...},...]."""

    def __init__(self):
        super().__init__(
            "\nSorry, we don\'t support your structure of JSON."
        )
