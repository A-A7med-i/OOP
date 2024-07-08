from Example1.shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        """
        Initializes a Circle object with the given radius.

        Args:
            radius (float): The radius of the circle. Must be a positive value.
        """

        self.radius = radius

    def get_area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle (π * radius^2).
        """

        return 3.14159 * self.radius * self.radius
