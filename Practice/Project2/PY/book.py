class Book:
    """Represents a book in the library system."""

    def __init__(self, id: int, name: str, quantity: int) -> None:
        """
        Initializes a new Book object.

        Args:
          id (int): The unique ID of the book.
          name (str): The name of the book.
          quantity (int): The number of copies available in the library.
        """
        self.id = id
        self.name = name
        self.quantity = quantity
        self.borrowed_by = []

    def get_id(self) -> int:
        """Returns the book's ID."""
        return self.id

    def get_name(self) -> str:
        """Returns the book's name."""
        return self.name

    def get_quantity(self) -> int:
        """Returns the number of available copies of the book."""
        return self.quantity
