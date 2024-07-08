class Calculator:
    """
    A versatile calculator class designed for performing basic arithmetic
    operations on two numbers. It can handle addition and division,
    providing informative error messages for potential exceptions.

    Attributes:
        __num1 (float): The first private number for calculation.
        __num2 (float): The second private number for calculation.
    """

    def __init__(self, num1: float, num2: float) -> None:
        """
        Initializes the calculator object with two numbers.

        Args:
            num1 (float): The first number for calculations.
            num2 (float): The second number for calculations.

        Raises:
            Type
        """
        self.__num1 = num1  # make num1, num2 private
        self.__num2 = num2

    def add(self) -> float:
        """
        Calculates and returns the sum of the two stored numbers.

        Returns:
            float: The sum of num1 and num2.
        """
        return self.__num1 + self.__num2

    def division(self) -> float:
        """
        Calculates and returns the quotient of the two stored numbers,
        handling division by zero gracefully.

        Returns:
            float: The quotient of num1 and num2 (if num2 is not zero).
            None: If num2 is zero, indicating a division by zero error.

        Raises:
            ZeroDivisionError: If a serious error occurs during division.
        """
        try:
            return self.__num1 / self.__num2
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
