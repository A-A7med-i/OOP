#include "building.h"
#include "rooms.h"
#include <string>
#include <iostream>

Building::Building(std::string n, bool e, std::vector<Apartment> a,
                   std::vector<Rooms> r)
    : name(n), elevators(e), apartments(a), rooms(r) {}

void Building::displayInfo()
{
    std::cout << "Building Name: " << name << std::endl;
    std::cout << "Has Elevators: " << (elevators ? "Yes" : "No") << std::endl;
    std::cout << "Number of Apartments: " << apartments.size() << std::endl;
    for (auto it = apartments.begin(); it != apartments.end(); ++it)
    {
        std::cout << "Printing room details for apartment #"
                  << it - apartments.begin() + 1 << std::endl;
        std::vector<Rooms> currentRooms = it->getRooms();
        for (auto it2 = currentRooms.begin(); it2 != currentRooms.end(); ++it2)
        {
            std::cout << "  Room dimensions:" << std::endl;
            std::cout << "    Height: " << it2->getHeight() << std::endl;
            std::cout << "    Width:  " << it2->getWidth() << std::endl;
        }
    }
}
