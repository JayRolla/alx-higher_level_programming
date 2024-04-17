#!/usr/bin/python3
"""
This module contains a script that simulates adding items to a persistent list stored in a file.
The script reads from 'add_item.json', adds command line arguments to the list, and saves it back.
If 'add_item.json' doesn't exist, it creates it. Handles adding multiple items across executions.
"""

filename = "add_item.json"

def main():
    """Main function that manages the list stored in the file."""
    try:
        # Attempt to read from the file and evaluate its content as a list
        with open(filename, 'r') as file:
            items = eval(file.read())
            if not isinstance(items, list):
                items = []
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        items = []

    # Extend the list with command line arguments from the second element onwards
    import sys
    items.extend(sys.argv[1:])

    # Write the updated list back to the file
    with open(filename, 'w') as file:
        file.write(str(items))

if __name__ == "__main__":
    main()
