#!/usr/bin/python3
"""
Defines a function that reads a text file and prints its contents to stdout.
"""

def read_file(filename=""):
    """Read a file and print its contents to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
