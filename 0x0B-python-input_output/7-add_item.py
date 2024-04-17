#!/usr/bin/python3
"""
This script manages a list stored in a text file. It reads the list from the file,
adds command line arguments to the list, and saves it back to the file.
Handles creation of the file if it does not exist and re-writes to add items.
"""

filename = "add_item.json"

def main():
    try:
        with open(filename, 'r') as f:
            # Reading and converting string representation of list back to list
            items = eval(f.read())  # Using eval is a security risk
    except (FileNotFoundError, SyntaxError):
        items = []

    # Extend list with command line arguments
    items.extend(arg for arg in __import__('sys').argv[1:])

    with open(filename, 'w') as f:
        # Convert list to string and write to file
        f.write(str(items))

if __name__ == "__main__":
    main()
