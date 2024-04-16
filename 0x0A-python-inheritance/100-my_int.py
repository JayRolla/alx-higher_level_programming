#!/usr/bin/python3
"""MyInt Module"""


class MyInt(int):
    """
    MyInt class inherits from int and inverts == and != operators
    """

    def __eq__(self, other):
        """
        Inverts the == operator

        Args:
            other (int): The other value to compare with

        Returns:
            bool: True if not equal, False otherwise
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator

        Args:
            other (int): The other value to compare with

        Returns:
            bool: True if equal, False otherwise
        """
        return super().__eq__(other)
