class InVoive:
    """
    Represents an invoice item with details like name, item number, price, and quantity.

    Attributes:
        name (str): The name of the item on the invoice.
        item_number (int): A unique identifier for the item (must be non-negative).
        price (float): The price of the item (must be non-negative).
        quantity (int): The quantity of the item purchased (must be non-negative).
    """

    def __init__(
        self, name: str, item_number: int, price: float, quantity: int
    ) -> None:
        """
        Initializes a new `InVoive` object with the specified details.

        Args:
            name (str): The name of the item on the invoice.
            item_number (int): A unique identifier for the item (must be non-negative).
            price (float): The price of the item (must be non-negative).
            quantity (int): The quantity of the item purchased (must be non-negative).
        """
        self.name = name
        self.item_number = item_number
        self.price = price
        self.quantity = quantity

    def set_item_number(self, new_item_number):
        """
        Updates the item number for the invoice item.

        Args:
            new_item_number (int): The new unique identifier for the item (must be non-negative).
        """
        if new_item_number >= 0:
            self.item_number = new_item_number
        else:
            print("Error: Item number must be non-negative.")

    def get_item_number(self):
        """
        Returns the current item number for the invoice item.

        Returns:
            int: The unique identifier for the item.
        """
        return self.item_number

    def set_name(self, new_name):
        """
        Updates the name for the invoice item.

        Args:
            new_name (str): The new name of the item on the invoice.
        """
        if new_name:  # Check for truthiness (not empty string)
            self.name = new_name
        else:
            print("Error: Item name cannot be empty.")

    def get_name(self):
        """
        Returns the current name for the invoice item.

        Returns:
            str: The name of the item on the invoice.
        """
        return self.name

    def set_price(self, new_price):
        """
        Updates the price for the invoice item.

        Args:
            new_price (float): The new price of the item (must be non-negative).
        """
        if new_price >= 0:
            self.price = new_price
        else:
            print("Error: Item price must be non-negative.")

    def get_price(self):
        """
        Returns the current price for the invoice item.

        Returns:
            float: The price of the item.
        """
        return self.price

    def set_quantity(self, new_quantity):
        """
        Updates the quantity for the invoice item.

        Args:
            new_quantity (int): The new quantity of the item purchased (must be non-negative).
        """
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Error: Item quantity must be non-negative.")

    def get_quantity(self):
        """
        Returns the current quantity of the item.

        Returns:
            int: The quantity of the item purchased.
        """
        return self.quantity

    def get_total_price(self):
        """
        Calculates and returns the total price for the invoice item.

        Returns:
            float: The total price (price * quantity) of the item.
        """
        return self.price * self.quantity

    def print_invoice(self):
        """
        Prints the details of the invoice item, including name, price, quantity, item number,
        and total price.
        """
        print("Item Name:", self.get_name())
        print(f"Item Price: ${self.get_price():.2f}")
        print("Item Quantity:", self.get_quantity())
        print("Item number:", self.get_item_number())
        print(f"Item Total Price: ${self.get_total_price():.2f}")
