from Example1.shape import Shape


class Square(Shape):
    """
    Represents a square shape with a side length.
    """

    def __init__(self, side_length):
        """
        Initializes a Square object with the given side length.

        Args:
            side_length (float): The length of a side of the square. Must be a positive value.
        """
        self.side_length = side_length

    def get_area(self):
        """
        Calculates and returns the area of the square.

        Overrides the abstract method from the Shape class.

        Returns:
            float: The area of the square (side_length * side_length).
        """

        return self.side_length * self.side_length
