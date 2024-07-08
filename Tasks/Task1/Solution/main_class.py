from py.rooms import Rooms
from py.apartment import Apartment
from py.building import Building


r1 = Rooms(5, 10)
r2 = Rooms(7, 12)

if __name__ == "__main__":
    b = Building(
        "b1",
        True,
        Apartment(3, 2, [r1, r2]),
        [r1, r2],
    )

    b.display()
