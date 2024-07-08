class Eat:
    """A class representing eating habits of an animal."""

    def __init__(self, type_of_eat: str, price: float) -> None:
        """
        Initializes the eating habits object with type of food and price.

        Args:
          type_of_eat (str): The type of food the animal eats.
          price (float): The estimated price of the food.
        """
        self.type_of_eat = type_of_eat
        self.price = price

    def set_type_of_eat(self, new_eat: str) -> None:
        """
        Sets the type of food the animal eats.

        Args:
          new_eat (str): The new type of food the animal eats.
        """
        self.type_of_eat = new_eat

    def get_type_of_eat(self) -> str:
        """
        Returns the type of food the animal eats.

        Returns:
          str: The type of food the animal eats.
        """
        return self.type_of_eat

    def set_price(self, new_price: float) -> None:
        """
        Sets the estimated price of the food.

        Args:
          new_price (float): The new estimated price of the food.
        """
        self.price = new_price

    def get_price(self) -> float:
        """
        Returns the estimated price of the food.

        Returns:
          float: The estimated price of the food.
        """
        return self.price

    def display(self):
        """
        Prints information about the eating habits.

        This method displays the type of food and its estimated price.
        """
        print(f"Type of eat is: {self.type_of_eat} and price is: {self.price}")
