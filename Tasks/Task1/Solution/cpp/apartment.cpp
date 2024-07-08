#include "apartment.h"
#include <vector>
#include "rooms.h"

Apartment::Apartment(int n, std::vector<Rooms> r)
    : numberOfRooms(n), rooms(r) {}

void Apartment::setNumberOfRooms(int newNumber) { numberOfRooms = newNumber; }

int Apartment::getNumberOfRooms() { return numberOfRooms; }

void Apartment::setRooms(std::vector<Rooms> newRooms) { rooms = newRooms; }

std::vector<Rooms> Apartment::getRooms() { return rooms; }
