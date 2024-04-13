def add_integer(a, b=98):
    """
    This function adds two numbers together.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. If not provided, it defaults to 98.

    Returns:
        int: The sum of the two numbers.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Examples:
        >>> add_integer(2, 3)
        5
        >>> add_integer(100.3, -2)
        98
        >>> add_integer(4)
        102
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
