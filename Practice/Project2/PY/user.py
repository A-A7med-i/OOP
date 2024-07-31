class User:
    """Represents a user registered in the library system."""

    def __init__(self, id: int, name: str) -> None:
        """
        Initializes a new User object.

        Args:
        id (int): The unique ID of the user.
        name (str): The name of the user.
        """
        self.id = id
        self.name = name
        self.borrowed_books = []

    def get_id(self) -> int:
        """Returns the user's ID."""
        return self.id

    def get_name(self) -> str:
        """Returns the user's name."""
        return self.name
