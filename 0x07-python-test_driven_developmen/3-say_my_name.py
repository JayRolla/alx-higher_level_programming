def say_my_name(first_name, last_name=""):
    """
    This function prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name, which must be a string.
        last_name (str, optional): The last name, which must be a string. If not provided, it defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Examples:
        >>> say_my_name("John", "Doe")
        My name is John Doe

        >>> say_my_name("Alice")
        My name is Alice 
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
