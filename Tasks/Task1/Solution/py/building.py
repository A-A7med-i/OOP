class Building:
    """
    Represents a building with a name, elevator access, apartments, and unattached rooms.

    Attributes:
        name (str): The name of the building.
        has_elevators (bool): Whether the building has elevators.
        apartments (list[Apartment]): A list of Apartment objects representing the apartments in the building.
        rooms (list[UnattachedRoom]): A list of UnattachedRoom objects representing the unattached rooms in the building (implementation details for UnattachedRoom are left unspecified).
        count (int): A class-level counter used for assigning a unique number to each unattached room when displaying details (starts at 1).

    """

    count = 1

    def __init__(self, name: str, has_elevators: bool, apartments, rooms) -> None:
        self.name = name
        self.has_elevators = has_elevators
        self.apartments = apartments
        self.rooms = rooms

    def display(self):
        """
        Prints information about the building, including name, elevator access, number of apartments,
        number of unattached rooms, and details for each unattached room (dimensions and a numbered counter).

        This method assumes the `apartments` object has a `get_number_of_apartment()` method
        that returns the number of apartments.
        """
        print(f"Building Name: {self.name}")
        print(f"Has Elevators: {self.has_elevators}")
        print(f"Number of Apartments: {self.apartments.get_number_of_apartment()}")
        print(f"Number of Unattached Rooms: {len(self.rooms)}")
        print("Printing room details for apartment")
        print("Room dimensions:")
        for room in self.rooms:
            print(f" Room {Building.count}")
            print(f"    Height: {room.get_height()}")
            print(f"    Width: {room.get_width()}")
            Building.count += 1
