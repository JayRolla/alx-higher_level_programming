#!/usr/bin/python3
"""Module for the Square class."""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square, which is a kind of rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.
        The size parameter acts as both width and height for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width  # Since width and height are the same

    @size.setter
    def size(self, value):
        """Set the size of the square, which updates both width and height."""
        self.width = value
        self.height = value  # Ensures the square's properties remain uniform

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Update attributes of the square.
        Overloads the Rectangle update method by modifying it to accept size as an argument.
        """
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    if attrs[i] == 'size':
                        setattr(self, attrs[i], arg)
                        self.height = arg
                    else:
                        setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, key, value)
                    self.height = value
                elif key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
