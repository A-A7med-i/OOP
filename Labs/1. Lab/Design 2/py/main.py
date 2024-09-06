from __future__ import annotations


class Fraction:
    """
    A class representing a fraction with numerator and denominator.
    """

    numerator = 0

    def set_denominator(self, new_denominator: int) -> None:
        """
        Set a new value for the denominator.

        Args:
            new_denominator (int): The new denominator value.

        Raises:
            ValueError: If the new denominator is zero.
        """

        if new_denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.__denominator = new_denominator

    def get_denominator(self) -> int:
        """
        Get the denominator of the fraction.

        Returns:
            int: The denominator value.
        """
        return self.__denominator

    def display(self) -> None:
        """
        Display the fraction in the format 'numerator / denominator'.
        """
        print(self.numerator, "/", self.__denominator)

    def add(self, other: Fraction) -> Fraction:
        """
        Add this fraction to another fraction.

        Args:
            other (Fraction): The fraction to add to this one.

        Returns:
            Fraction: A new Fraction object representing the sum.
        """
        num = (self.numerator * other.__denominator) + (
            self.__denominator * other.numerator
        )
        den = self.__denominator * other.__denominator

        print(num, "/", den)


if __name__ == "__main__":
    f1 = Fraction()

    f1.numerator = 3
    f1.set_denominator(4)

    f2 = Fraction()

    f2.numerator = 8
    f2.set_denominator(16)

    f1.display()
    f2.display()

    print(f1.get_denominator())

    # This would raise an error
    # f1.set_denominator(0)
    # print(f1.get_denominator())

    f1.set_denominator(2)
    print(f1.get_denominator())

    f1.add(f2)
