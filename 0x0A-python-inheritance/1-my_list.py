#!/usr/bin/python3
"""MyList module for creating lists"""


class MyList(list):
    """class MyList for creating lists"""

    def print_sorted(self):
        """Method for printing a sorted list

        Args:
            self

        Return:
            nothing
        """
        print(sorted(self))
