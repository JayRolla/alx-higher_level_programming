def text_indentation(text):
    """
    Let's add some line breaks after certain punctuation marks!

    This function takes a string (text) and prints it with two new lines
    after each occurrence of the characters '.', '?', and ':'.

    Args:
        text (str): The input text to process.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> text_indentation("Hello. How are you? I'm doing great: Thanks for asking!")
        Hello.
        <BLANKLINE>
        How are you?
        <BLANKLINE>
        I'm doing great:
        <BLANKLINE>
        Thanks for asking!
        <BLANKLINE>
    """
    if not isinstance(text, str):
        raise TypeError("Text must be a string!")

    characters = ['.', '?', ':']
    new_text = ""
    for char in text:
        new_text += char
        if char in characters:
            new_text += "\n\n"
    print(new_text.strip(" "))
