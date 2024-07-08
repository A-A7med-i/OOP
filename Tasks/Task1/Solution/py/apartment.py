class Apartment:
    """Represents an apartment unit with an apartment number, number of rooms, and details about the rooms.

    Attributes:
        number_of_apartment (int): The unique identifier for the apartment.
        number_of_rooms (int): The total number of rooms in the apartment.
        rooms (list): A list containing details about each room (implementation details for rooms are left unspecified).
    """

    def __init__(self, number_of_apartment: int, number_of_rooms: int, rooms) -> None:
        """
        Initializes an Apartment object.

        Args:
            number_of_apartment (int): The unique identifier for the apartment.
            number_of_rooms (int): The total number of rooms in the apartment.
            rooms (list): A list containing details about each room (implementation details for rooms are left unspecified).
        """
        self.number_of_apartment = number_of_apartment
        self.number_of_rooms = number_of_rooms
        self.rooms = rooms

    def set_number_of_apartment(self, new_number_of_apartment: int) -> None:
        """
        Updates the apartment number.

        Args:
            new_number_of_apartment (int): The new unique identifier for the apartment.
        """
        self.number_of_apartment = new_number_of_apartment

    def get_number_of_apartment(self) -> int:
        """
        Returns the apartment number.

        Returns:
            int: The unique identifier for the apartment.
        """
        return self.number_of_apartment

    def set_number_of_rooms(self, new_number: int):
        """
        Updates the total number of rooms in the apartment.

        Args:
            new_number (int): The new total number of rooms.
        """
        self.number_of_rooms = new_number

    def get_number_of_rooms(self) -> int:
        """
        Returns the total number of rooms in the apartment.

        Returns:
            int: The total number of rooms.
        """
        return self.number_of_rooms

    def set_rooms(self, new_rooms):
        """
        Updates the list containing details about each room.

        Args:
            new_rooms (list): A list containing details about each room (implementation details for rooms are left unspecified).
        """
        self.rooms = new_rooms

    def get_rooms(self):
        """
        Returns the list containing details about each room.

        Returns:
            list: A list containing details about each room (implementation details for rooms are left unspecified).
        """
        return self.rooms
