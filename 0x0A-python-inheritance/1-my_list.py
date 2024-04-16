#!/usr/bin/python3
"""My List Module"""


class MyList(list):
    """
    MyList class inherits from list and adds print_sorted method
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order
        """
        print(sorted(self))
