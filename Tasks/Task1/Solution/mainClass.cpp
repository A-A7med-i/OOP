#include <iostream>
#include "cpp\apartment.h"
#include "cpp\building.h"
#include "cpp\rooms.h"

using namespace std;

int main()
{

    string name = "Buildinh One";
    bool e = false;
    std::vector<Rooms> r = {Rooms(10, 10), Rooms(10, 15)};
    std::vector<Apartment> a = {Apartment(2, r)};
    Building b(name, e, a, r);

    b.displayInfo();

    return 0;
}