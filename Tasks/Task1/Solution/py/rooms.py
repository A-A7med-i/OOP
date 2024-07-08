class Rooms:
    """
    Represents a rectangular room with a width and height.

    Attributes:
        width (int): The width of the room in meters (must be a positive integer).
        height (int): The height of the room in meters (must be a positive integer).
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Initializes a new `Rooms` object with the specified width and height.

        Args:
            width: The width of the room in meters (positive integer).
            height: The height of the room in meters (positive integer).

        Raises:
            ValueError: If either width or height is not a positive integer.
        """
        self.width = width
        self.height = height

    def set_height(self, new_height: int) -> None:
        """
        Updates the height of the room.

        Args:
            new_height: The new height of the room in meters (positive integer).

        Raises:
            ValueError: If the new height is not a positive integer.
        """
        self.height = new_height

    def get_height(self) -> int:
        """
        Returns the current height of the room.

        Returns:
            int: The current height of the room in meters.
        """
        return self.height

    def set_width(self, new_width: int) -> None:
        """
        Updates the width of the room.

        Args:
            new_width: The new width of the room in meters (positive integer).

        Raises:
            ValueError: If the new width is not a positive integer.
        """
        self.width = new_width

    def get_width(self) -> int:
        """
        Returns the current width of the room.

        Returns:
            int: The current width of the room in meters.
        """
        return self.width
