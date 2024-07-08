from Example2.animal import Animal
from Example2.eat import Eat


class TypeOne(Animal, Eat):
    """A class representing a specific type of animal (TypeOne) inheriting from Animal and Eat."""

    def __init__(
        self, type: str, age: float, eat: str, price: float, name: str
    ) -> None:
        """
        Initializes a TypeOne object, inheriting attributes from Animal and Eat.

        Args:
          type (str): The type of the animal (inherited from Animal).
          age (int): The age of the animal (inherited from Animal).
          eat (str): The type of food the animal eats.
          price (float): The estimated price of the food.
          name (str): The name of the animal.
        """
        super().__init__(type, age)  # Call Animal constructor first
        Eat.__init__(self, eat, price)  # Call Eat constructor with relevant arguments
        self.name = name

    def set_name(self, new_name: str) -> None:
        """Sets the name of the TypeOne object."""
        self.name = new_name

    def get_name(self) -> str:
        """Returns the name of the TypeOne object."""
        return self.name

    def display(self):
        """
        Displays information about the TypeOne object, combining details from Animal and Eat.

        This method calls the display methods from both Animal and Eat, followed by printing the name.
        """
        super().display()
        Eat.display(self)  # Call Eat's display method with self argument
        print(f"The name is: {self.name}")
