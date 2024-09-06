from __future__ import annotations
from math import sqrt


class Point:
    """Represents a point in 3D space."""

    x = y = z = 0

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
    p1 = Point()

    p1.x = 3
    p1.y = 4
    p1.z = 5

    p2 = Point()

    p2.x = 6
    p2.y = 8
    p2.z = 10

    p1.display()
    p2.display()

    distance = p1.calculate_Distance(p2)
    print(f"Distance between p1 and p2: {distance:.2f}")


if __name__ == "__main__":
    main()
