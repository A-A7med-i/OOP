#include <string>
#include "rooms.h"
#include "apartment.h"
#include <vector>

class Building
{
private:
    std::string name;
    bool elevators;
    std::vector<Apartment> apartments;
    std::vector<Rooms> rooms;

public:
    Building(std::string n, bool e, std::vector<Apartment> a,
             std::vector<Rooms> r);
    void displayInfo();
};
