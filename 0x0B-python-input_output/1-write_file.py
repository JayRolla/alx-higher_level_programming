#!/usr/bin/python3
"""
Defines a function that writes a string to a text file and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
