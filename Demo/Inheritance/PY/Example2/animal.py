class Animal:
    """A class representing an animal."""

    def __init__(self, type: str, age: float) -> None:
        """
        Initializes the animal object with type and age.

        Args:
          type (str): The type of animal.
          age (int): The age of the animal.
        """
        self.type = type
        self.age = age

    def set_type(self, new_type: str) -> None:
        """
        Sets the type of the animal.

        Args:
          new_type (str): The new type of the animal.
        """
        self.type = new_type

    def get_type(self) -> str:
        """
        Returns the type of the animal.

        Returns:
          str: The type of the animal.
        """
        return self.type

    def set_age(self, new_age: float) -> None:
        """
        Sets the age of the animal.

        Args:
          new_age (int): The new age of the animal.
        """
        self.age = new_age

    def get_age(self) -> float:
        """
        Returns the age of the animal.

        Returns:
          int: The age of the animal.
        """
        return self.age

    def display(self):
        """
        Prints the animal's type and age.

        This method would also be added and committed using Git commands after its definition.
        """
        print(f"Type is: {self.type} and age: {self.age}")
