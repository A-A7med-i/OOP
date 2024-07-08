class Person:
    """
    Represents a basic person with attributes for name and age.

    Attributes:
        name (str): The person's name.
        age (int): The person's age.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Initializes a Person object with a name and age.

        Args:
            name (str): The person's name.
            age (int): The person's age.

        Raises:
            TypeError: If either name or age is not of the expected type (str or int).
        """

        self.name = name
        self.age = age
        print("From Person")

    def set_name(self, new_name: str) -> None:
        """
        Updates the person's name.

        Args:
            new_name (str): The new name for the person.

        Raises:
            TypeError: If the new_name argument is not a string.
        """
        self.name = new_name

    def get_name(self) -> str:
        """
        Returns the person's current name.

        Returns:
            str: The person's name.
        """
        return self.name

    def set_age(self, new_age: int) -> None:
        """
        Updates the person's age.

        Args:
            new_age (int): The new age for the person.

        Raises:
            TypeError: If the new_age argument is not an integer.
        """
        self.age = new_age

    def get_age(self) -> None:
        return self.age

    def display(self):
        """
        Prints a greeting message with the person's name and age.
        """
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
