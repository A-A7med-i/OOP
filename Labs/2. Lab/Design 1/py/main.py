from __future__ import annotations
from math import sqrt


class Point:
    """Represents a point in 3D space."""

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def display(self) -> None:
        print(f"Point: ({self.x}, {self.y}, {self.z})")

    def calculate_Distance(self, p: Point) -> float:
        """
        Calculate the Euclidean distance between this point and another point.

        Args:
            p (Point): The other point.

        Returns:
            float: The distance between the two points.
        """
        return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2 + (self.z - p.z) ** 2)


def main() -> None:
    """Create two points and demonstrate their methods."""
    p1 = Point(3, 4, 5)

    p2 = Point(6, 8, 10)

    p1.display()
    p2.display()

    p3 = Point()

    p3.display()

    distance_1 = p1.calculate_Distance(p2)
    print(f"Distance between p1 and p2: {distance_1:.2f}")

    distance_2 = p3.calculate_Distance(p2)
    print(f"Distance between p1 and p2: {distance_2:.2f}")


if __name__ == "__main__":
    main()
