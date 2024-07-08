#include "rooms.h"
#include <vector>

class Apartment
{
private:
    int numberOfRooms;
    std::vector<Rooms> rooms;

public:
    Apartment(int n, std::vector<Rooms> r);
    void setNumberOfRooms(int newNumber);
    int getNumberOfRooms();
    void setRooms(std::vector<Rooms> newRooms);
    std::vector<Rooms> getRooms();
};