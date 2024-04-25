#!/usr/bin/python3
"""Module for the Rectangle class."""

from models.base import Base

class Rectangle(Base):
    """Represents a rectangle shape inheriting from Base."""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width ensuring it is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Add similar property and setter for height, x, y

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using the '#' character, considering 'x' and 'y' offsets."""
        print(("\n" * self.y) + "\n".join((" " * self.x + "#" * self.width) for _ in range(self.height)))

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes from no-keyword and keyword arguments."""
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            if i < len(attrs):
                setattr(self, attrs[i], arg)
        if not args:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

